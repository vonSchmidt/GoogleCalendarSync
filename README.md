#Google Calendar Synchronization Module 


##Description 

This module is a tool that permits synchronization between a Google
Calendar, designated by its CalendarId, and a third party MySQL Database.
Google Calendar API is used throughout the tool's source


##Usage

- Use the templates provided in the [MySQL Table Templates](https://github.com/vonSchmidt/GoogleCalendarSync/tree/master/MySQL_Table_Templates)
directory to create the 3rd party database. (The most important factor is the tables' structure)
- Change the CalendarId by setting the `cal_id` variable in the scripts.
(This will most certainly change in the future)
- Call the `sync_script.py` script to procede with the divergences'
correction of both events sources.
- If you are running this tool remotely (e.g via `ssh`), be sure to pass in the
`--noauth_local_webserver` argument.


##Notes

Consider using this service within a cron job like the one described here: 
[CRON Example](https://github.com/vonSchmidt/GoogleCalendarSync/tree/master/cronsched)


This script will store all authentication information in `$HOME/.credentials`.

##Requirements


The following Python modules are required:
    - argparse
    - python-mysqldb

Create a database called `events` if you don't want to meddle with the
configuration of the module, otherwise change the database connection
parameters in `sync_script.py`.

Make sure to configure the correct timezone for MySQL as it is set to +00:00 by
default.


##License

Google Calendar Sync. Module
Copyright 2015 zshulu (Von Schmidt)

Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
zshulu (Von Schmidt) wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer or coffee in return.

_NB: The Google Calendar API is licensed under Apache License, Version 2.0. Its
text is available in every separate module provided in the API._
