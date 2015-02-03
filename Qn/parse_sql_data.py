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

def get_metrics(filename, pair_keys_list, single_keys_list):

    print "Processing file {0}".format(filename)

    pair_keys_dict = dict()
    for pair in pair_keys_list:
        pair_keys_dict[pair[0]] = dict()
        pair_keys_dict[pair[1]] = dict()


    single_keys_dict = dict()
    for skey in single_keys_list:
        single_keys_dict[skey] = list()

    with open(filename) as f:
        for line in f:
            if line:
                split_line = line.split(",")
                key = split_line[2]
                date = split_line[1]
                value = int(split_line[3].split(".")[0].translate(None, "\n\r"))

                found = False
                for skey in single_keys_list:
                    if skey == key:
                        single_keys_dict[key].append(value)
                        found = True
                        break

                if found:
                    # move to next line
                    continue

                for pair in pair_keys_list:
                    if pair[0] == key or pair[1] == key:
                        pair_keys_dict[key][date] = value
                        break

    compute_metrics(pair_keys_list, pair_keys_dict, single_keys_dict)

#    print single_keys_dict
#    print "-----"
#    print pair_keys_dict

def compute_metrics(pair_keys_list, pair_keys_dict, single_keys_dict):

    compute_single_key_metrics(single_keys_dict)

    for pair in pair_keys_list:
        compute_pair_key_metrics(pair[0], collections.OrderedDict(sorted(pair_keys_dict[pair[0]].items())), pair[1], collections.OrderedDict(sorted(pair_keys_dict[pair[1]].items())))

def compute_single_key_metrics(single_keys_dict):

    for key, value in single_keys_dict.items():
        print "{0}".format(key)
        value.sort()
        avg = sum(value)/len(value)
        print "avg.: {0}".format(avg)
        compute_percentile(avg, value, 50)
        compute_percentile(avg, value, 75)
        compute_percentile(avg, value, 90)

    print "{0}".format("".join(["-" for x in range(1, 100)]))

def compute_pair_key_metrics(recv_key, received_values, sent_key, sent_values):
    print "{0} {1}".format(recv_key, sent_key)

    throughput_recv = get_throughput(received_values)
    print "Throughput: {1} {0}/s".format(recv_key, throughput_recv)
    throughput_sent = get_throughput(sent_values)
    print "Throughput: {1} {0}/s".format(sent_key, throughput_sent)

    diff_list = []
    for key_date in received_values.keys():
        if key_date in sent_values:
            diff_list.append(received_values[key_date] - sent_values[key_date])

    diff_list.sort()
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
    filename = "/tmp/file.20140715-113507.csv"

    pair_keys_list = [("NoMediaMessagesReceived", "NoMediaMessagesSent")]
    single_keys_list = ['cpu']
    get_metrics(filename, pair_keys_list, single_keys_list)
