#!/usr/bin/env python

# Authentication Module, Returns
# User Credentials From Specified
# Storage Location.

import os
import oauth2client
from oauth2client import client
from oauth2client import tools


try:
    import argparse
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    flags = parser.parse_args()
except ImportError:
    print "Package argparse is needed."
    flags = None;

SCOPES                  = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE      = 'client_secret.json'
APPLICATION_NAME        = 'Calendar Sync'
API_CONSOLE_KEY         = 'AIzaSyBNR0aWYjZZpayUF354KfZyObeTu7QPcrs'


def get_credentials():
    """
    Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.

    """

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-api-rw.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials
