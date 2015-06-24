Author        	 : 	Vijay Kumar Badugu
                	vbadugu@juniper.net

Date          	 : 	06/19/2015.

Description   	 : 	The purpose of this commit script is to make sure MTU is configured on "Live" interfaces.The script is 
			invoked when a "commit" is issued on the JUNOS device in configuration mode.
 
			The script determines the liveliness of the interface by checking for "unit" and "disable" on the interfaces. 
			If the interface configuration doesn't contain "disable" and "unit" is present the script considers that 
			interface as "live". The script ignores fxp,em,lo interfaces. The script also works in a scenario where 
			an interface inherits "MTU" from apply-group configuration.

Pseudo Code    	 : 	1. 	Ignore the interfaces starting with "fxp", "em", "lo", "ats".

		   	2. 	Consider the interfaces which have "unit" in configuration and doesn't have "disable" in the 
				configuration.

		   	3. 	Check for "MTU" in the interface configuration. If "MTU" is not present the script throws a 
				warning saying "MTU is not configured". This message is logged in syslog.
		
		   	4. 	If "MTU" is present the script checks whether configured "MTU" is less than 2000 .If "MTU" is 
				less than 2000 the script throws a warning saying "MTU is less than 2000". This message is logged in
				syslog.
			
			5. 	The facility of the syslog message is "user" and severity level is "error".

CLI Commands Used	:	No cli commands are used in the script. The script just reads the configuration.
	
Instructions	 	:	To set this script up on your JUNOS device copy this script 
				to the following folder: /var/run/scripts/commit
			
				Then configure JUNOS with the following :
				set system scripts commit file MTU-checker.slax

				The syslog messages can be viewed in /var/log/messages.
				
				
			
		
 		

 