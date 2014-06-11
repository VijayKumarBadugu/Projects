   Author        : Nadeem Mohammad
                   nmohammad@juniper.net
   Date          : 01/23/2014.

   Description   : This event script runs periodically every 5 minutes (can be 
                   changed to less frequent run) and checks for pfe error on each 
                   pfe in the system by excuting following command:
                   "show si53xx 0x2100 0x6a si5368" and then look for register 129 
                   value of 0x1c which indicates an error has occoured. if error 
                   is found it reports it to the system log message file. The 
                   message itself contains the exact command to excute to do 
                   the CCG switchover if desired. It also checks if enough time 
                   has gone by since last switchover (30 mins) before an actual
                   switchover can be performed. if enough time has not gone by, 
                   then script will log message indicating issue has happened 
                   but switchover cant be performed at this time.

		   Note: There are two versions of this script:
		   1. That does whats described above but doesnt do the actual
		      CCG switchover (CCG_MON.slax)
		   2. That does whats described above and also performs the
		      CCG switchover. (CCG_MON_SWITCH.slax)

  CLI Commands Used:

  request pfe execute target <fpc> command "show si53xx 0x2100 0x6a si5368"; 

  Instructions:

  To set this up on your JUNOS device copy this script to the following folder:
  /var/db/scripts/event/

  Then configure JUNOS with the following:

  'set event-options event-script file CCG_MON.slax or CCG_MON_SWITCH.slax'
