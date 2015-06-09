#!/usr/bin/env python

# Event Fetching Module
# Given A Maximum Number
# Of Events To Fetch.

from datetime import datetime
from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools
import authentication

try:
    import argparse
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('-maxevents', type=int, default=0, help='Maximum number of events to display') # 0 => No Limit
    parser.add_argument('-future', action='store_true', help='Show only upcoming events')
    parser.add_argument('-updated', type=str, help='Shows events updated since specified time')
    flags = parser.parse_args()
except ImportError:
    print "Package argparse is needed."
    flags = None;

cal_id = 'primary'

def fetch(max_events=0, future=False, up_min=None):
    """Shows basic usage of the Google Calendar API.
    Creates a Google Calendar API service object and outputs a list
    of events on the user's calendar. Returns [confirmed_events],
    [deleted_events] and lastUpdateTime.
    """

    credentials = authentication.get_credentials()
    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    if(max_events != 0 and future):
        print 'Getting the upcoming ' + str(flags.maxevents) + ' events'
    elif(max_events != 0 and ~future):
        print 'Getting ' + str(max_events) + ' events'
    elif(max_events == 0 and future):
        print 'Getting all upcoming events'
    elif(max_events == 0 and ~future):
        print 'Getting all events'

    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    if(future): time_min = now
    else:       time_min = None
    if max_events == 0: max_events = None

    eventsResult = service.events().list(calendarId=cal_id, singleEvents=True, orderBy='updated',
            maxResults=max_events, timeMin=time_min, updatedMin=up_min, showDeleted=True).execute()
    events = eventsResult.get('items', [])
    events.reverse()

    deleted_events = []
    confirmed_events = []

    print 'Total: ', len(events), ' events.'

    for event in events:
        if event['status'] == "cancelled":
            deleted_events.append(event)
        elif event['status'] == "confirmed":
            confirmed_events.append(event)

    if events:
        last_update = events[0]['updated']
    else:
        last_update = ''
    return confirmed_events, deleted_events, last_update



if __name__ == '__main__':
    events, deleted_events, time = fetch(flags.maxevents, flags.future, flags.updated)

    if not events:
        print 'No events found.'
    else:
        for event in events:
            start = event['start']['dateTime']
            print event['status'], start, event['summary'], event['id'], event['updated']
    print '\nDELETED\n'
    if not deleted_events:
        print 'No deleted events.'
    else:
        for event in deleted_events:
            start = event['start']['dateTime']
            print event['status'], start, event['summary'], event['id'], event['updated']


