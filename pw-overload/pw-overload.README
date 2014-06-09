/ * Author        : Nadeem Mohammad
 * Version       : 1.0
 * Last Modified : May 5th, 2014
 * Platform      : PTX, MX
 * Release       : 10.4 and above
 *
 * Assumption:
 *                The user of this script needs to create a BFD session between
 *                the p-core (CE) routers and the PE routers. This BFD session
 *                should run on and ifl which is on the same IFD on which 
 *                OSPF adjacencies are formed between the pcore routers over the 
 *                l2circuit connection. During the maintenance window user needs
 *                to bring down this BFD session by bringing down the IFL on 
 *                which this BFD session is running. this is done on the PE. 
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
 *                 As this script runs when BFD session goes down, it looks
 *                 for rest of the IFLs on the IFD on which the BFD session
 *                 just went down. All these ifls are where OSPF session is
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
 * ON LOCAL ROUTER WHERE BFD SESSION IS RUNNING (CE1)
 *
 * copy pw-overload.slax to
 * /var/db/scripts/event
 *
 * Then configure JUNOS with the following:
 * 'set event-options event-script file pw-overload.slax'
 *
 * ON REMOTE ROUTER WHERE OSPF NBRS EXISTS (CE2)
 *
 * copy pw-overload-remote.slax in /var/db/scripts/op
 *
 * COMMANDS USED:
 *
 * pw-overload.slax (local)
 * show ospf neighbors. To extract the ospf nbr addr and ospf ifl
 * show ospf intf detail. To get the existing metric value
 * 
 * pw-overload-remote.slax (remote)
 * show interface terse. To locate the ospf nbr and the corrisponding ifl.
 * show ospf intf detail. To get the existing metric values.
 *
 */