/ * Author        : Nadeem Mohammad
 * Version       : 1.0
 * Last Modified : May 5th, 2014
 * Platform      : PTX, MX
 * Release       : 10.4 and above
 *
 * Assumption:
 *                The user of this script needs to create a BFD session between
 *                the p-core (CE) routers and the PE routers. This BFD session
 *                MUST run on the CITM ifl with vlan-id value of 100. This ifl
 *                MUST be on the same IFD on which OSPF adjacencies are formed 
 *                between the pcore routers over the l2circuit connection. 
 *                During the maintenance window user needs
 *                to bring down this BFD session by bringing down the IFL on 
 *                which this BFD session is running. this is will be done via
 *                an op script (PWE-OVERLOAD-TL) running on the PE (TL) router. 
 *                Please refer to the PWE-OVERLOAD-TL-README.txt file for the 
 *                functionality and working of this op script.
 *
 * Description   : This event script is simulating an ospf overload functionality.
 *                 It has two parts. local part which runs on the local router
 *                 connected to PE over an l2circuit connection. When PE is about
 *                 to get into a maintenance window it brings down the ifl
 *                 on which a BFD session is running between the local router
 *                 and the PE router. Local router detects this BFD session
 *                 going down and this acts as the TRIGGER for *this* script
 *                 running on the local router to run.
 *
 *                 As this script runs when BFD session goes down, it first 
 *                 checks the associated ifl on which the BFD session went
 *                 down. if the ifl is on vlan-id 100 it will then compare
 *                 the IFD of this IFL with the IFD of the ospf interface.
 *                 If the IFD matched, script will then find rest of the ifls
 *                 on this IFD. All these ifls are where OSPF session is
 *                 running between the local router (CE1) and the remote router
 *                 (CE2). After finding all these IFLs it raises the ospf metric
 *                 value on all these IFLs. it first finds the existing metric
 *                 value and adds 30000 to that.
 *
 *                 When this happens, this will trigger OSPF to select an
 *                 alternate route to reach remote CE2, via PE2.
 *
 *                 After raising the metric this script then logs in to the
 *                 remote CE router and invokes an op script responsible to
 *                 do the same thing on the remote side. i.e raise the OSPF
 *                 metric on links towards PE1 such that return traffic also
 *                 takes path towards PE2. It does this by sending OSPF
 *                 neighbor address to the remote CE2. the script running
 *                 on the remote CE2 uses the neighbor info and finds the
 *                 corresponding IFLs on which this ospf session is running
 *                 and increases the metric value.
 *
 *                 When maintenance window is completed and the IFL is brought
 *                 up on the PE1. this triggers a BFD UP event on the local
 *                 router CE1 where this script is running. When this happens
 *                 script restores the old metric values on all the IFLs and
 *                 logs into the remote CE2 and executes the same op script
 *                 to restore metric values on the other side. As a result of
 *                 this old path should get restored.
 *
 *                 NOTE: The password and user-name used to log into the remote
 *                       CE2 is jnpr/pass123. change this accordingly. you may
 *                       also need to add CE1 on CE2 and CE2 on CE1 as known
 *                       hosts for successful login. use the following command:
 *
 *                       set security ssh-known-hots fetch-from-server
 *
 * INSTRUCTIONS:
 *
 *    CE1------PE1--------PE2------CE2.
 *
 * ON LOCAL ROUTER (CE1)
 *
 * copy PWE-OVERLOAD-LOCAL.slax (event script) to
 * /var/db/scripts/event on both RE0 and RE1 where applicable.
 *
 * Then configure JUNOS with the following:
 * 'set event-options event-script file PWE-OVERLOAD-LOCAL.slax'
 *
 * ON REMOTE ROUTER (CE2)
 *
 * copy PWE-OVERLOAD-REMOTE.slax (op script) to /var/db/scripts/op
 * on both RE0 and RE1 where applicable.
 *
 * Then configure JUNOS with the following:
 * 'set system scripts op file PWE-OVERLOAD-REMOTE.slax'
 *
 * COMMANDS USED:
 *
 * PWE-OVERLOAD-LOCAL.slax
 * show ospf neighbors. To extract the ospf nbr addr and ospf ifl
 * show ospf intf detail. To get the existing metric value
 * 
 * PWE-OVERLOAD-REMOTE.slax
 * show interface terse. To locate the ospf nbr and the corrisponding ifl.
 * show ospf intf detail. To get the existing metric values.
 *
 */