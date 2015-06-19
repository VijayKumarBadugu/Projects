Author        	 : 	Vijay Kumar Badugu
                	  	vbadugu@juniper.net

Date          	 : 	06/19/2015.

Description   	 : 	The purpose of this commit script is to make sure MTU is 
					configured on "live" interfaces.The script is invoked when a "commit" is issued on the JUNOS device in configuration mode.
 
					The script determines the livliness of the interface by checking for "unit" and "disable" on the interfaces. If the 
					interface configuration doesn't contain "disable" and "unit" is present the script considers that interface as "live".  
					The script ignores fxp,em,lo interfaces. The script also works in a scenario where an interface inherits mtu from apply-group configuration.

Pseudo Code    	 : 	1. 	Ignore the interfaces starting with "fxp", "em", "lo".

		   			2. 	Consider the interfaces which have "unit" in 
						configuration and doesn't have "disable" in the configuration.

		   			3. 	Check for "mtu" in the interface configuration. If "mtu" 
						is not present the script throws a warning saying mtu is 
						not configured. This message is logged in syslog.
		
		   			4. 	If "mtu" is present the script checks whether configured 
						"mtu" is less than 2000 .If "mtu" is less than 2000 the
						script throws a warning saying mtu is less than 2000. 
						This message is logged in syslog.

CLI Commands Used	:	No cli commands are used in the script. The script just reads 
					the configuration.
	
Instructions	 :		To set this script up on your JUNOS device copy this script 
					to the following folder: /var/run/scripts/commit
			
					Then configure JUNOS with the following :
					set system scripts commit file MTU-checker.slax
			
		
 		

 