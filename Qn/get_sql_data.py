#!/usr/bin/env python

"""
Selects SQL data into outfile
"""

import sys
import MySQLdb as dbapi
import sys
import csv
import time

def read_credentials(filename):

    db_params = {}
    with open(filename) as f:
        for line in f:
            if line:
                split_line = line.translate(None, '\n').split("=")
                if split_line[0] == 'server':
                    db_params["server"] = split_line[1]
                elif split_line[0] == 'pass':
                    db_params["pass"] = split_line[1]
                elif split_line[0] == 'schema':
                    db_params["schema"] = split_line[1]
                elif split_line[0] == 'user':
                    db_params["user"] = split_line[1]
    return db_params

def fetch_sql_data(server, date):

    db_params = read_credentials("credentials.txt")
    dbServer = db_params["server"]
    dbPass = db_params["pass"]
    dbSchema = db_params["schema"]
    dbUser = db_params["user"]

    dbQuery = "SELECT TestReports.* from TestReports WHERE `time` > \"{1}\" AND `reporter_id` LIKE '%{0}%'".format(server, date)

    db = dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass, db=dbSchema)
    cur = db.cursor()
    cur.execute(dbQuery)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    outfile = "/tmp/file.{0}.csv".format(timestr)

    rows = cur.fetchall()
    fp = open(outfile, 'w')
    myFile = csv.writer(fp)
    myFile.writerows(rows)
    fp.close()

    print "created {0}".format(outfile)
    return outfile

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage: ./get_sql_data.py <server_id> <date_since>"
        sys.exit(1)

    server = sys.argv[1]
    date = sys.argv[2]

    fetch_sql_data(server, date)
