#Google Calendar Synchronization Module 


##Description 


This module is a tool that permits synchronization between a Google
Calendar, designated by its CalendarId, and a third party MySQL Database.
    
##Usage


- Use the templates provided in the ![MySQL Table Templates](https://github.com/vonSchmidt/GoogleCalendarSync/tree/master/MySQL_Table_Templates)
directory to create the 3rd party database.
- Change the CalendarId by setting the `cal_id` variable in the scripts.
(This will most certainly change in the future)
- Call the `sync_script.py` script to procede with the divergences'
correction of both events sources.

##Notes

Consider using this service within a cron job like the one described here: 
![CRON Example](https://github.com/vonSchmidt/GoogleCalendarSync/tree/master/cronsched)
This script will store all authentication information in `$HOME/.credentials`.

##License

Google Calendar Sync. Module
Copyright 2015 zshulu (Von Schmidt)

Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
zshulu (Von Schmidt) wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer or coffee in return
