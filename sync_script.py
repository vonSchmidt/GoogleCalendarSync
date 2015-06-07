#!/usr/bin/env python
import datetime
import MySQLdb
from MySQLdb import IntegrityError
from fetch_events import *
from subprocessing import *
from StringIO import StringIO

fout, ferr = StringIO(), StringIO()
db = MySQLdb.connect(
    host="localhost",
    user="mountain",
    passwd="tiger",
    db="events"
)
cursor = db.cursor()

def insert(est, esd, eet, eed, edesc, etitle, gooid):
    return [
                './insert_event.py',
                '-title', etitle,
                '-desc', edesc,
                '-sd', esd,
                '-st', est,
                '-ed', eed,
                '-et', eet
           ]

def update(est, esd, eet, eed, edesc, etitle, gooid):
    return [
                './update_event.py',
                '-eid', gooid,
                '-title', etitle,
                '-desc', edesc,
                '-sd', esd,
                '-st', est,
                '-ed', eed,
                '-et', eet
           ]

def delete(est, esd, eet, eed, edesc, etitle, gooid):
    return [
                './delete_event.py',
                '-eid', gooid
           ]

operations = {
            0: insert,
            1: update,
            2: delete
        }

def main():
    print 'Committing database changes...'
    ###################################################################

    # Documentation for the UNSYNC_EVENT table:
        # 0 -> Insert Operation
        # 1 -> Update Operation
        # 2 -> Delete Operation

    ###################################################################
    # Always insert events with no google event id
    # To the UNSYNC_EVENT table with OPERATION_MODE 0
    try:
        cursor.execute("INSERT INTO UNSYNC_EVENT (EVENTS_PUID, OPERATION_MODE) "\
                + "SELECT EVENTS_PUID, 0 AS OPERATION_MODE "\
                + "FROM EVENT WHERE GOO_EVENT_ID IS NULL"
                )
    except IntegrityError:
        # Already awaiting synchronization
        pass

    # Checking UNSYNC_EVENT
    sql = "SELECT EVENTS_PUID, EVENTS_START_TIME, "\
    + "EVENTS_START_DAY, EVENTS_END_TIME, EVENTS_END_DAY, "\
    + "EVENTS_DESC, "\
    + "EVENTS_TITLE, GOO_EVENT_ID, OPERATION_MODE "\
    + "FROM EVENT NATURAL JOIN UNSYNC_EVENT"
    cursor.execute(sql)

    for (eid, est, esd, eet, eed, edesc, etitle, gooid, op_mode) in cursor:
        cmd_args = operations[int(op_mode)](str(est)[:-3], str(esd), str(eet)[:-3], str(eed), edesc, etitle, gooid)
        exit_code = call(cmd_args, stdout=fout, stderr=ferr)

        # Clean up in the database
        if op_mode == 0:
            cursor.execute("UPDATE EVENT SET GOO_EVENT_ID = %s "\
                    + "WHERE EVENTS_PUID = %s",
                    (str(fout.getvalue()).strip(), # Insert script outputs new GOO_EVENT_ID
                    str(eid).strip())
                    )
        elif op_mode == 2:
            cursor.execute("DELETE FROM EVENT WHERE "\
                    + "EVENTS_PUID = %s", str(eid)
                    )

        cursor.execute("DELETE FROM UNSYNC_EVENT WHERE EVENTS_PUID = %s",
                str(eid)
                )

    print 'Committing Google Calendar Changes...'
    last_update = open('update.dat', 'a+') # Create the file if it does not exist
    last_update_time = last_update.read()
    last_update.close()
    if last_update_time == '': last_update_time = None
    print 'Last update time: ', last_update_time
    print 'Synchronizing deviations past that point...'

    # Checking Google Calendar
    confirmed_events, deleted_events, last_update_time = fetch(max_events=0, future=False, up_min=last_update_time)
    if confirmed_events:
        for event in confirmed_events:
            # Preparing data
            es = __import__('re').search("(.+)T(.+)\+(?:.+)", event['start']['dateTime'])
            ee = __import__('re').search("(.+)T(.+)\+(?:.+)", event['end']['dateTime'])
            esd = es.groups()[0]
            est = es.groups()[1]
            eed = ee.groups()[0]
            eet = ee.groups()[1]
            if 'description' in event.keys():
                edesc = event['description']
            else:
                edesc = 'No Description'
            etitle = event['summary']
            gooevid = event['id']

            result = cursor.execute("SELECT EVENTS_PUID FROM EVENT WHERE GOO_EVENT_ID = %s",
                    str(event['id'])
                    )
            if(not result):
                # Insert Operation
                cursor.execute("INSERT INTO EVENT ("\
                    + "EVENTS_START_TIME, "\
                    + "EVENTS_START_DAY, "\
                    + "EVENTS_END_TIME, "\
                    + "EVENTS_END_DAY, "\
                    + "EVENTS_DESC, "\
                    + "EVENTS_TITLE, "\
                    + "GOO_EVENT_ID "\
                    + ") VALUES ( "\
                    + "%s, %s, %s, "\
                    + "%s, %s, %s, "\
                    + "%s)",
                    (est,
                    esd,
                    eet,
                    eed,
                    edesc,
                    etitle,
                    gooevid)
                    )
            else:
                # Update Operation
                cursor.execute("UPDATE EVENT "\
                    + "SET "\
                    + "EVENTS_START_TIME = %s, "\
                    + "EVENTS_START_DAY = %s, "\
                    + "EVENTS_END_TIME = %s, "\
                    + "EVENTS_END_DAY = %s, "\
                    + "EVENTS_DESC = %s, "\
                    + "EVENTS_TITLE = %s "\
                    + "WHERE GOO_EVENT_ID = %s",
                    (est,
                    esd,
                    eet,
                    eed,
                    edesc,
                    etitle,
                    gooevid)
                    )
    if deleted_events:
        cursor.execute("DELETE FROM EVENT "\
                + "WHERE GOO_EVENT_ID IN ("\
                + ", ".join(["'"+str(i['id'])+"'" for i in deleted_events])
                + ")"\
                )


    db.commit()
    db.close()

    # Updating Last Update Time
    print 'Updating last synchronization to ', last_update_time
    last_update = open('update.dat', 'w')
    last_update.write(last_update_time)
    last_update.close()

if __name__ == '__main__':
    try:
        print 'Synchronization started...'
        main()
        print 'All good. Exiting...'
    except KeyboardInterrupt:
        print 'Operation was interrupted.'
        exit()
