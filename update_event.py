#!/usr/bin/env python

# Event Update Module
# Given An Event ID,
# And Updated Data,
# Changes Event's Conf
# On Google Calendar.

from datetime import datetime
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import tools
import authentication

cal_id = 'primary'

try:
    import argparse
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('-eid',     type=str, help="Event ID", required=True)
    parser.add_argument('-title',   type=str, help="Event Title")
    parser.add_argument('-desc',    type=str, help="Event Description")
    parser.add_argument('-loc',     type=str, help="Event Location")
    parser.add_argument('-sd',      type=str, help="Event Start Date (yyyy-mm-dd)")
    parser.add_argument('-st',      type=str, help="Event Start Time (hh:mm)")
    parser.add_argument('-ed',      type=str, help="Event End Date (yyyy-mm-dd)")
    parser.add_argument('-et',      type=str, help="Event End Time (hh:mm)")
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
    event = service.events().get(calendarId=cal_id, eventId=flags.eid).execute()

    if(flags.title):
        event['summary'] = flags.title

    if(flags.desc):
        event['description'] = flags.desc

    if(flags.loc):
        event['location'] = flags.loc

    if(flags.sd and flags.st):
        event['start']['dateTime'] = flags.sd + 'T' + flags.st + ':00.000000'

    if(flags.ed and flags.et):
        event['end']['dateTime'] = flags.ed + 'T' + flags.et + ':00.000000'

    service.events().update(calendarId=cal_id, eventId=event['id'], body=event).execute()


if __name__ == '__main__':
    main()
