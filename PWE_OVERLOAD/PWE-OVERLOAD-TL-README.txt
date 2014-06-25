/*
 * Author        : Nadeem Mohammad
 * Version       : 1.0
 * Last Modified : June 25th, 2014
 * Platform      : PTX/MX
 * Release       : 10.0 and above
 *
 * Description   : This is an op script to be executed on the TL (PE)
 *                 routers. This script is part of the PWE Overload
 *                 functionality as described in PWE-OVERLOAD-README.txt
 *                 This script takes an argument named "state" with the
 *                 value of "on" indicating pwe overload is initiated and
 *                 "off" indicating pwe overload is turned off.
 *                 Once initiated, this script looks at all the .100 ifls
 *                 in the system (CITM) ifls (please refer to the PWE-
 *                 OVERLOAD-README.txt file) and brings them down.
 *                 Once turned off, this script will once again scan and
 *                 find all the .100 ifls and bring them up. overall this
 *                 will cause the BFD sessions running on the CITM ifls
 *                 to go down and up on the P-Core routers (CEs).
 *
 *                 Note: Its operators responsibility to configure these
 *                 CITM .100 ifls correctly as these should be exclusively
 *                 dedicated to the BFD sessions that need to be toggled.
 *
 *
 *
 * INSTRUCTIONS:
 *
 * To set this up on your JUNOS device copy this script to the following folder:
 * /var/db/scripts/op
 *
 *
 * Make sure you name the script 'PWE-OVERLOAD-TL' or change references in
 * the script and JUNOS config to be whatever you named it.
 *
 * COMMANDS USED:
 *
 * show interface terse
 *
 */