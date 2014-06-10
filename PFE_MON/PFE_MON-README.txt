   Author        : Nadeem Mohammad
		   nmohammad@juniper.net
   Date          : 02/24/2014.
 
   Description   : This event/op script takes threshold values as arguments and
		   runs periodically every five minutes and checks pfe traffic
		   statistics for each fpc in the system. On the first run it saves
		   the read values to an accounting profile file "pfe-stats.acct".
		   On successive runs, it first reads the last saved values
		   and then compares them with the current values. This gives a 
		   delta for all the captured counters. This delta value is then checked
		   against a threshold value for each of these counters. if delta 
		   exceeds this threshold value it will log a pfe error.

  CLI Commands Used:

  show pfe statistics traffic fpc <fpc#>

  Instructions:

  To set this up on your JUNOS device copy this script to the following folder:
  /var/db/scripts/event/ and 
  /var/db/scripts/op/
 
  Then configure JUNOS with the following:

  'set event-options event-script file PFE-STATS-EVENT.slax'
  'set accounting-options file pfe-stats.acct'
  'set accounting-options file pfe-stats.acct size 2m
  'set accounting-options file pfe-stats.acct transfer-interval 2000
 
  Make sure you name the script 'PFE-STATS-EVENT' or change references in
  the script and JUNOS config to be whatever you named it.

  Note: You can also run this as an op script, doing so you can give the
	threshold values as arguments to the script. default values currently
	are set to zero for all. Idea is to run this first time as an op
	script giving threshold values as arguments and then successive
	runs will be periodic running as an event script.

	To run as an op script:

	op PFE-STATS-EVENT
