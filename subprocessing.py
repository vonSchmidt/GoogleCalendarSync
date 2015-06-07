import sys
from subprocess import Popen, PIPE
from threading import Thread

def thr_w(infile, *files):
    """print infile to files in a separate thread"""
    def fanout(infile, *files):
        for line in iter(infile.readline, ''):
            for f in files:
                f.write(line)
        infile.close()
    t = Thread(target=fanout, args=(infile,)+files)
    t.daemon = True
    t.start()
    return t


def call(cmd_args, **kwargs):
    stdout, stderr = [kwargs.pop(s, None) for s in 'stdout', 'stderr']
    p = Popen(cmd_args,
            stdout=PIPE if stdout is not None else None,
            stderr=PIPE if stderr is not None else None,
            **kwargs)
    threads = []

    if stdout is not None: threads.append(thr_w(p.stdout, stdout, sys.stdout))
    if stderr is not None: threads.append(thr_w(p.stderr, stderr, sys.stderr))
    for t in threads: t.join()
    return p.wait()

