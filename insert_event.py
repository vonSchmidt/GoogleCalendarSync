#!/usr/bin/env python

# Event Insertion Module
# Given Event Related
# Data, Creates A New
# Event, And Returns
# That Event's ID.

from datetime import datetime
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import tools
import authentication

cal_id = 'primary'

try:
    import argparse
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('-title',   type=str, help="Event Title",                   required=True)
    parser.add_argument('-desc',    type=str, help="Event Description",             required=True)
    parser.add_argument('-loc',     type=str, help="Event Location")
    parser.add_argument('-sd',      type=str, help="Event Start Date (yyyy-mm-dd)", required=True)
    parser.add_argument('-st',      type=str, help="Event Start Time (hh:mm)",      required=True)
    parser.add_argument('-ed',      type=str, help="Event End Date (yyyy-mm-dd)",   required=True)
    parser.add_argument('-et',      type=str, help="Event End Time (hh:mm)",        required=True)
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

    tz = open('/etc/timezone', 'r').read().strip()

    event = {
        'summary': flags.title,
        'description': flags.desc,
        'location': flags.loc,
        'start':
        {
            'dateTime': flags.sd + 'T' + flags.st + ':00.000000',
            'timeZone': tz
        },
        'end':
        {
            'dateTime': flags.ed + 'T' + flags.et + ':00.000000',
            'timeZone': tz
        },
    }

    new_event = service.events().insert(
            calendarId=cal_id,
            body=event
    ).execute()

    print new_event['id'],


if __name__ == '__main__':
    main()
