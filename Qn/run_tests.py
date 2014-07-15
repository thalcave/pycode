#!/usr/bin/env python

"""
Run test with different workloads (found in Workloads directory)
"""
import os
import sys
import logging
import get_sql_data
import time
import paramiko
import subprocess

WDIR = "./Workloads"
WNAME="Workload.properties.filetransfer_"

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger(__name__)

def setup_server(server):
    logger.debug("Setup server {0}".format(server))
    command = "sudo -u qtalk -i /opt/qnective/clean_server.sh"
    run_command(server, "florin", command, True)

def setup_sender(sender, wfile):
    logger.debug("Setup sender {0}".format(sender))
    scp = subprocess.Popen(["scp",
                           os.path.join(WDIR, wfile),
                           "ubuntu@{0}:/home/ubuntu/qtalk_scala/Workload.properties".format(sender)],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    result = scp.stdout.readlines()
    if result == []:
        error = scp.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print result

    command = "rm -fr /mnt/local/share/data/*"
    run_command(sender, "ubuntu", command, False)

def setup_receiver(receiver):
    logger.debug("Setup receiver {0}".format(receiver))
    command = "rm -fr /mnt/local/share/data/*"
    run_command(receiver, "ubuntu", command)

def stop_test(host):
    logger.debug("Stop test on {0}".format(host))
    command = "killall -9 java"
    run_command(host, "ubuntu", command)

def run_command(host, user, command, force_pseudo = False):
    if force_pseudo:
        ssh = subprocess.Popen(["ssh",
                           "-t",
                           "{0}@{1}".format(user, host), command],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    else:
        ssh = subprocess.Popen(["ssh",
                           "{0}@{1}".format(user, host), command],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print result


def stop_previous_test(test_params, prev_start_date):
    filename = get_sql_data.fetch_sql_data(test_params["server"], prev_start_date)
    logger.info("Saved previous test results in {0}".format(filename))

    stop_test(test_params["sender"])
    stop_test(test_params["receiver"])

def start_test(delay, wfile, sender, receiver):
    logger.debug("Starting test {0}".format(wfile))
    command = "cd qtalk_scala; ./file_transfer.sh"
    run_command(receiver, "ubuntu", command, False)
    run_command(sender, "ubuntu", command, False)

    logger.debug("Started test, will sleep {0}".format(delay))
    time.sleep(delay)

def run_tests(workload_files, test_params):
    prev_start_date = ""
    for wfile in workload_files:
        test_name = wfile[len(WNAME):]
        logger.info("Start test '%s'", test_name)

        if prev_start_date:
            stop_previous_test(test_params, prev_start_date)

        setup_server(test_params["server"])

        setup_sender(test_params["sender"], wfile)
        setup_receiver(test_params["receiver"])

        prev_start_date = time.strftime('%Y-%m-%d %H:%M:%S')
        logger.debug("Start date: %s", prev_start_date)
        print "{0}".format("".join(["-" for x in range(1, 100)]))

        start_test(5400, wfile, test_params["sender"], test_params["receiver"])


    stop_previous_test(test_params, prev_start_date)


def get_workload_files():
    return sorted([f for f in os.listdir(WDIR) if os.path.isfile(os.path.join(WDIR, f)) and f.startswith(WNAME)])

def read_hosts(filename):
    params = {}
    with open(filename) as f:
        for line in f:
            if line:
                split_line = line.translate(None, '\n').split("=")
                if split_line[0] == 'server':
                    params["server"] = split_line[1]
                elif split_line[0] == 'sender':
                    params["sender"] = split_line[1]
                elif split_line[0] == 'receiver':
                    params["receiver"] = split_line[1]
    return params


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage: ./run_tests.py <hosts>"
        sys.exit(1)

    test_params = read_hosts(sys.argv[1])
    if len(test_params) != 3:
        logger.error("Invalid <hosts> file! should contain 'server', 'sender' and 'receiver'\nread configuration: {0}".format(test_params))
        sys.exit(2)

    if not os.path.isdir(WDIR) or not os.path.exists(WDIR):
        logger.error("Missing {0} dir".format(WDIR))
        sys.exit(3)

    workload_files = get_workload_files()
    if not workload_files:
        logger.error("No {0}* files found in {1}".format(WNAME, WDIR))

    run_tests(workload_files, test_params)
