#!/usr/bin/env python

"""
Selects SQL data into outfile; parse outfile, compute throughput for keys
"""

import sys
import collections
import datetime as dt
import time
import dateutil.parser
import numpy as np

def timestamp(date):
    return time.mktime(date.timetuple())

def get_throughput(sorted_vals):
    start_date = 0
    start_val = 0
    for key, val in sorted_vals.items():
        if val > 0:
            start_date = key
            start_val = val
            break
    end_date = sorted_vals.keys()[-1]
    end_val = sorted_vals[end_date]

    if end_date > 0:
        end = dateutil.parser.parse(end_date);
        if start_date > 0:
            start = dateutil.parser.parse(start_date);
            duration = (timestamp(end) - timestamp(start))
            print "duration: {0} s".format(duration)
            return (end_val - start_val)/duration
    return 0

def get_metrics(filename, received_key, sent_key):
    print "get metrics for {0},{1} from {2}".format(received_key, sent_key, filename)

    recv = dict()
    sent = dict()

    diff = dict()

    with open(filename) as f:
        for line in f:
            if line:
                split_line = line.split(",")
                key = split_line[2]
                date = split_line[1]
                value = int(split_line[3].split(".")[0].translate(None, "\n\r"))
                if key == received_key:
                    recv[date] = value
                    if date in sent:
                        diff[date] = value - sent[date]
                elif key == sent_key:
                    sent[date] = value
                    if date in recv:
                        diff[date] = recv[date] - value

    sorted_diff = collections.OrderedDict(sorted(diff.items()))

    compute_metrics(received_key, sent_key, collections.OrderedDict(sorted(recv.items())), collections.OrderedDict(sorted(sent.items())), sorted_diff)

def compute_metrics(received_key, sent_key, sorted_recv, sorted_sent, sorted_diff):

    throughput_recv = get_throughput(sorted_recv)
    print "Throughput: {1} {0}/s".format(received_key, throughput_recv)
    throughput_sent = get_throughput(sorted_sent)
    print "Throughput: {1} {0}/s".format(sent_key, throughput_sent)

    diff_list = sorted_diff.values()
    avg_diff = sum(diff_list)/len(diff_list)
    print "avg. diff: {0}".format(avg_diff)

    compute_percentile(avg_diff, diff_list, 50)
    compute_percentile(avg_diff, diff_list, 75)
    compute_percentile(avg_diff, diff_list, 90)

    print "{0}".format("".join(["-" for x in range(1, 100)]))

def compute_percentile(avg_diff, diff_list, percentile):
    val_percentile = np.percentile(diff_list, percentile)
    print "{0}% percentile for (recv - sent): {1}".format(percentile, val_percentile)
    if avg_diff > 0:
        print "({0} percentile - avg)/avg: {1}".format(percentile, (val_percentile-avg_diff)/avg_diff)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage: ./parse_sql_data.py <server_id> <date_since>"
        sys.exit(1)

    server = sys.argv[1]
    date = sys.argv[2]

#    filename = get_sql_data.fetch_sql_data(server, date)
    filename = "/tmp/file.20140714-180908.csv"

    get_metrics(filename, "NoMediaMessagesReceived", "NoMediaMessagesSent")
