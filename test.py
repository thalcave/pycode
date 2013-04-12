#!/usr/bin/env python

def run_restores(restores, rpath):
    """
    Run all the restores at the same time.
    """
    def go(bk, res):
        """
        Effectively run the restore.
        """
        # compiling command line
        cmd = '%s run_restore cid %s bpath %s vpath %s timestamp %s rcid %s rpath %s mkdirp' % \
            (BKSTOOL, bk['cid'], bk['bpath'], bk['vpath'], bk['timestamp'], bk['rcid'], bk['rpath'])
        start = time.time()
        child = subprocess.Popen(cmd.split(), stdout = subprocess.PIPE)
        output = ''
        readcount = 0
        bk['jobid'] = '??????????????????'
        while True:
            if child.poll() != None:
                while True:
                    ln = child.stdout.readline()
                    if not ln:
                        break
                    if 'JOB_ID' in ln:
                        bk['jobid'] = ln.split('JOB_ID')[1].strip()
                break
        bk['returncode'] = child.returncode
        end = time.time()
        bk['tstart'] = start
        bk['tend'] = end
        bk['cmd'] = cmd
        res.put(bk)
        return
