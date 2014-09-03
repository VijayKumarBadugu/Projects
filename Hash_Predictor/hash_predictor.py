#!/usr/bin/env python

from __future__ import print_function
import sys
import re
import socket
import time
import os
import getpass
import base64

from ncclient import manager
from scapy.all import IP, IPv6, UDP, hexdump
from scapy.contrib.mpls import MPLS
from lxml import etree

DEBUG = True

def validate_ip(address, version):
    """ Returns True if address is valid for specified IP version (2 or 4) """
    if version == 4:
        try:
            socket.inet_pton(socket.AF_INET, address)
        except:
            return False
    elif version == 6:
        try:
            socket.inet_pton(socket.AF_INET6, address)
        except:
            return False
    return True
        

def get_user_input():
    """ 
    Performs the work of obtaining and validating user input.
    """
    
    inputs = {}
    
    # base64 encode password so that password doesn't show up  
    # in debugging output
    inputs['base64_password'] = base64.b64encode(getpass.getpass())

    # Per https://matrix.juniper.net/docs/DOC-182829, only IPv4 packets
    # are currently supported.

    #print("Packet type (IPv4, IPv6, MPLS): ", end='')
    #inputs['type'] = sys.stdin.readline().strip().lower()
    inputs['type'] = 'ipv4'

    # default to IPv4
    if inputs['type'] == '' or not inputs['type'] in [ 'ipv4', 'ipv6', 'mpls']:
        print("defaulting to IPv4")
        inputs['type'] = 'ipv4'
        version = 4

    if inputs['type'] in ['ipv4', 'ipv6']:
        version = int(inputs['type'][-1:])
    else: # MPLS
        # version 4 and exp 0 are only values supported
        version = 4
        inputs['exp'] = 0

    if inputs['type'] == 'mpls':
        while True:
            print("Incoming label: ", end='')
            text_from_user = sys.stdin.readline().strip()
            if text_from_user:
                if text_from_user.isdigit():
                    label = int(text_from_user)
                    if label >=0 and label <= 1048576:
                        inputs['label'] = int(text_from_user)
                        break
                    else:
                        print("please specify label within valid range")
                else:
                    print("invalid input for label")
            else:
                print("invalid input for label")
                continue

#        print("IP version in MPLS packet (4 or 6): ", end='')
#        text_from_user = sys.stdin.readline().strip()
#        if text_from_user in [ '4', '6' ]:
#            version = int(text_from_user)
#        else:
#            print("defaulting to IPv4 in MPLS packet")
        
    while True:
        print("Incoming Interface: ", end='')
        text_from_user = sys.stdin.readline().strip()
        if text_from_user:
            inputs['iif'] = text_from_user
            break
        else: print("Incoming interface is a required field")        
    
    # strip the first number after the interface type and hyphen (e.g. ge-7/2/1.0)
    match = re.match('\w+-(\d+)/', inputs['iif'])
    if match:
        inputs['fpc'] = 'fpc' + match.group(1)
    else:
        print('Error: Unable to parse interface to obtain FPC number')
        print(inputs)
        sys.exit(1)

    while True:
        print("Source IP address: ", end='')
        text_from_user = sys.stdin.readline().strip()
        if text_from_user:
            if validate_ip(text_from_user, version):
                inputs['src'] = text_from_user
                break
            else:
                print("invalid IPv{} address detected".format(version))
                continue
        else: print("Source IP address is a required field")

    while True:
        print("Destination IP address: ", end='')
        text_from_user = sys.stdin.readline().strip()
        if text_from_user:
            if validate_ip(text_from_user, version):
                inputs['dst'] = text_from_user
                break
            else:
                print("invalid IPv{} address detected".format(version))
                continue
        else: print("Destination IP address is a required field")

    while True:
        print("Source port: ", end='')
        text_from_user = sys.stdin.readline().strip()
        if text_from_user:
            if text_from_user.isdigit():
                port = int(text_from_user)
                if port >=1 and port <= 65535:
                    inputs['sport'] = int(text_from_user)
                    break
                else:
                    print("please specify port within range 1 to 65535")
            else:
                print("invalid input for source port")
                continue
        else: 
            print("defaulting to source port 1200")
            inputs['sport'] = 1200
            break

    while True:
        print("Destination port: ", end='')
        text_from_user = sys.stdin.readline().strip()
        if text_from_user:
            if text_from_user.isdigit():
                port = int(text_from_user)
                if port >=1 and port <= 65535:
                    inputs['sport'] = int(text_from_user)
                    break
                else:
                    print("please specify port within range 1 to 65535")
            else:
                print("invalid input for destination port")
                continue
        else: 
            print("defaulting to destination port 53")
            inputs['dport'] = 53
            break

    # only UDP supported currently
    inputs['protocol_id'] = 17

#    while True:
#        print("Protocol ID: ", end='')
#        text_from_user = sys.stdin.readline().strip()
#        if text_from_user:
#            if text_from_user.isdigit():
#                inputs['protocol_id'] = text_from_user
#                break
#            else:
#                print("invalid input for protocol ID")
#                continue
#        else: 
#            print("defaulting to protocol ID 17 (UDP)")
#            inputs['protocol_id'] = 17
#            break

    while True:
        print("DSCP (decimal): ", end='')
        text_from_user = sys.stdin.readline().strip()
        if text_from_user:
            # check for valid hex input
            dscp_ecn = int(text_from_user) * 4 # add two binary 0 bits
            if int(text_from_user) >= 0 and int(text_from_user) < 64:
                inputs['dscp_ecn'] = dscp_ecn
                break
            else:
                print("invalid input DSCP")
                continue
        else: 
            print("defaulting to best effort)")
            inputs['dscp_ecn'] = 0
            break

    if DEBUG:
        print(inputs)

    return inputs

def print_ecmp(conn, ip_address):
    # Prints a list of ECMP for the provided destination IP

    rpc = """
    <get-route-information>
        <destination>{ip_address}</destination>
    </get-route-information>
    """.format(ip_address=ip_address)

    results = conn.rpc(rpc)

    tree = etree.XML(results.tostring)

    #print(etree.tostring(tree, pretty_print=True))

    filtered_tree = tree.xpath('//route-table//via')
    
    table_entries = {}
    for interface in filtered_tree:
        # use the name of the route table as key (e.g., 'inet.0') 
        key = interface.xpath('ancestor::route-table/table-name')[0].text
        # use a set to avoid duplicates
        if key not in table_entries:
            table_entries[key] = set()

        table_entries[key].add(interface.text)

    # print the possible OIFs for each routing table
    for table_name in table_entries:
        interface_set = table_entries[table_name]
        print('\n' + table_name + ': ')
        for interface in interface_set:
            print(interface + ' ')
    print('---')

def build_packet(inputs):
    # Returns hex string representation of packet

    if inputs['type'] == 'ipv4':
        ip_header = IP(len=40, flags='DF', ihl=5, id=os.getpid())
    elif inputs['type'] == 'ipv6':
        ip_header = IPv6(plen=8)
    elif inputs['type'] == 'mpls': 
        mpls_header = MPLS(label=inputs['label'], cos=inputs['exp'], s=1, ttl=64) 
        ip_header = IP(len=40, flags='DF', ihl=5, id=os.getpid())
        #print("mpls not implemented")
        #sys.exit(1)            

    udp_header = UDP()

    for key, value in inputs.iteritems():
        if key in [ 'src', 'dst']: # IPv4/v6 header
           setattr(ip_header, key, value)
        elif key in [ 'protocol_id' ]:
            if ip_header.version == 6:   # IPv6 header has Next Header
                setattr(ip_header, 'nh', value)
            else:
                setattr(ip_header, key, value)                
        elif key in ['dscp_ecn']:
            if ip_header.version == 6:   # IPv6 header has traffic class
                setattr(ip_header, 'tc', value)
            else:
                setattr(ip_header, 'tos', value)
        elif key in [ 'sport', 'dport']: # UDP header
            setattr(udp_header, key, value)

    if ip_header.version == 4:
        del ip_header[IP].chksum

    # note: wireshark indicates the resulting UDP checksum is
    # invalid. The PFE doesn't care.
    del udp_header[UDP].chksum

    if 'ip' in inputs['type']:
        packet = ip_header / udp_header
    else: # packet is MPLS
        packet = mpls_header / ip_header / udp_header

    if DEBUG:
        print(packet.show2())

    if packet.version == 4:
        # add padding to 40 bytes
        retval = str(packet).encode('hex') + '00000000000000000000FFFF'
    elif packet.version == 6:
        retval = str(packet).encode('hex') 
    else:
        print("Not an IP packet. MPLS not implemented")
        sys.exit(1)

    return retval
            
def get_results(conn, inputs, packet):

    iif = inputs['iif']
    
    # need to hack in mpls support later
    address_family = 'inet' if inputs['type'] == 'ipv4' else 'inet6'

    # clear the ukern_trace 12 buffer
    rpc_clear = """
    <request-pfe-execute>
        <target>{fpc}</target>
        <command>clear ukern_trace 12</command>
    </request-pfe-execute>
    """.format(fpc=inputs['fpc'])

    conn.rpc(rpc_clear)

    rpc_inject = """
    <request-pfe-execute>
        <target>{fpc}</target>
        <command>test jnh inject-lb-test {iif} {address_family} {packet}</command>
    </request-pfe-execute>
    """.format(fpc=inputs['fpc'], iif=iif, address_family=address_family, packet=packet)

    if(DEBUG):
        print("rpc: {}".format(rpc_inject))

    result = conn.rpc(rpc_inject)

    rpc_trace = """
    <request-pfe-execute>
        <target>{fpc}</target>
        <command>show ukern_trace 12</command>
    </request-pfe-execute>
    """.format(fpc=inputs['fpc'])

    result = conn.rpc(rpc_trace)
    tree = etree.XML(result.tostring)

    return etree.tostring(tree)

def get_cmd_line_parameters():
    cmd_line = {}

    try:
        cmd_line['router'] = sys.argv[1]
    except IndexError:
        print("please specify router as first argument")
        sys.exit(1)

    try:
        cmd_line['user'] = sys.argv[2]
    except IndexError:
        print ("please specify router username as second argument")
        sys.exit(1)

    return cmd_line

def print_debug(string):
    print("Collecting debugging info ", end='')
    for _ in range(3):
        time.sleep(1)
        print(".", end='')
    print("")    
    print(output)
    sys.exit(1)

def get_ifl(output):
    # Returns the IFL associated with the OIF in the probe packet logs

    ifl = 0

    index = output.rfind('RX: LB test probe pkt')
    if index:
        relevant_line = output[index:index+72]
    else:
        print("Error in parsing results!")
        print_debug(output)
        sys.exit()

    match = re.search('OIF:(\d+)', relevant_line)

    if match:
        ifl = match.group(1)

    return ifl

def validate_pfe_output(output):
    pass

def ifl_to_oif(ifl, conn):
    """ Returns OIF associated with provided IFL """

    rpc = """
    <get-interface-information>
        <extensive></extensive>
    </get-interface-information>
    """

    result = conn.rpc(rpc)
    tree = etree.XML(result.tostring)
    
    filtered_tree = tree.xpath('//logical-interface')

    oif = "unknown"
    for logical_interface in filtered_tree:
        # position 0 is name
        # position 1 is IFL
        observed_ifl = logical_interface.getchildren()[1].text.strip()
        if observed_ifl == ifl:
            oif = logical_interface.getchildren()[0].text.strip()
    return oif

def print_lag_members(conn, bundle_interface):

    print("bundle interface: {}".format(bundle_interface))
    rpc = """
     <get-interface-information>
        <extensive/>
        <interface-name>{interface}</interface-name>
     </get-interface-information>
    """.format(interface=bundle_interface)

    results = conn.rpc(rpc)
    tree = etree.XML(results.tostring)

    filtered_tree = tree.xpath('//lag-link/name')
    for name in filtered_tree:
        print('   ' + name.text.strip())

if __name__ == '__main__':

    cmd_line = get_cmd_line_parameters()

    inputs = get_user_input()

    conn = manager.connect(host=cmd_line['router'],
            port=830,
            username=cmd_line['user'],
            password=base64.b64decode(inputs['base64_password']),
            timeout=30,
            device_params = {'name':'junos'},
            hostkey_verify=False)

#    conn = manager.connect(host='5.1.0.1',
#            port=830,
#            username='jeffl',
#            password='PASS',
#            timeout=30,
#            device_params = {'name':'junos'},
#            hostkey_verify=False)
    
    if conn:
        print_lag_members(conn, 'ae2.0')
        sys.exit(1)
        print_ecmp(conn, inputs['dst'])
        packet = build_packet(inputs)

        if DEBUG: 
            print("hex string of packet: {}".format(packet))

        results = get_results(conn, inputs, packet)
        ifl  = get_ifl(results)
        if not ifl:
            print("Error: Unable to obtain IFL from local index")
            print(results)        
            sys.exit(1)

        if DEBUG: print("IFL: {}".format(ifl))

        outgoing_interface = ifl_to_oif(ifl, conn)
        print(outgoing_interface)
    else:
        print("netconf connection failed") 
        sys.exit(1)


