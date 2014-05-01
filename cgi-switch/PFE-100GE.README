This event script runs periodically every 5 minutes (can be changed to less frequen run) and checks for pfe error on each pfe in the system by excuting following 
command "show si53xx 0x2100 0x6a si5368" looks for register 129 value of 0x1c which
indicates error. if error is found it reports it to the system log message file. themessage itself contains the exact command to excute to do the switchover if desired.
it also checks if enough time has gone by since last switchover (30 mins) before
switchover can be performed. if enough time has not gone by then it will log message
indicating issue has happened but switchover cant be performed at this time.
