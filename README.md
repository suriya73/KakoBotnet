# Kako Botnet
This is a Python DDoS botnet.<br>
This botnet may have a few bugs, but, for what I have seen it works so far<br>
If I have made fixes I will post them here and state what was fixed<br>
# Compiling
Ok so if you are trying to use this botnet for mass infecting busy boxes or something like that. I recommend Nuitka it allows you to compile python2 or 3 into a linux binary file<br>
# Contact Information
Skype: live:zerefdragneelbro<br>
Discord: [SuperNova] Law#6800<br>
Email: gotenblack321@gmail.com<br>
# Current Updates
[FIX] Kako.py - Bots have been recently disconnecting for no reason. So I have fixed the issue<br>
[ADDED] Client.py - Added auto reconnect functionality<br>
# 25/02/2018
[ADDED] Client.py - Added Shell command to access bots terminal<br>
[ADDED] Client.py - Added multi threading<br>
[ADDED] Kako.py - Just added information on how to use shell comand in ">help"<br>
# 28/02/2018
[ADDED] Kako.py - New command ">password" changes the guest password temporarily for the session, (only admins can use it)<br>
[ADDED] Kako.py - ">help" command now shows how to use ">password" only admins can see the command<br>
# 01/03/2018
[ADDED] Client.py - New DDoS command ">http" there is no timer but the attack does stop once all the threads have been sent<br>
[ADDED] Kako.py - ">help" command has been updated to have the information on how to use ">http"<br>
# 03/03/2018
[FIX] Kako.py - Command ">password" has been fixed the issue was there was a indent not needing to be there<br>
[FIX] Kako.py - Guest account would not work because the var "pwordGuest" was not global, now it is<br>
# 04/03/2018
[ADDED] Client.py - Command ">http" now supports a time limit in the attack<br>
[ADDED] Kako.py - Updated info in ">help" on how to use ">http"<br>
# 05/03/2018
[ADDED] Client.py - Command ">http" now attacks with HTTP GET and has User-Agents<br>
# 19/03/2018
[ADDED] Client.py - New function makes the bot open the file on startup no matter what the file is called.
