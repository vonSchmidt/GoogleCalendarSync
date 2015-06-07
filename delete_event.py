#!/usr/bin/env python

# Event Deletion Module
# Given An Event's ID
# Event Gets Deleted.

from datetime import datetime
from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools
import authentication

cal_id = 'primary'

try:
    import argparse
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('-eid', type=str, help="Event ID", required=True)
    flags = parser.parse_args()
except ImportError:
    print "Package argparse is needed."
    flags = None;




def main():
    credentials = authentication.get_credentials()
    service = build('calendar', 'v3',
            http=credentials.authorize(Http()),
            developerKey=authentication.API_CONSOLE_KEY
            )

    print 'Delete Event From Primary Calendar'
    eventid = flags.eid.strip()

    ev = service.events().get(calendarId=cal_id, eventId=eventid).execute()
    print ev['summary']

    service.events().delete(calendarId=cal_id, eventId=eventid).execute()
    print "Deleted."


if __name__ == '__main__':
    main()
