#  http://pymotw.com/2/subprocess/index.html#signaling-between-processes
# The os examples include a demonstration of signaling between processes using os.fork() and os.kill().
#  Since each Popen instance provides a pid attribute with the process id of the child process,
#  it is possible to do something similar with subprocess.
# Child process:
import os
import signal
import time
import sys

pid = os.getpid()
received = False


def signal_usr1(signum, frame):
    "Callback invoked when a signal is received"
    global received
    received = True
    print('CHILD %6s: Received USR1' % pid)
    sys.stdout.flush()


print('CHILD %6s: Setting up signal handler' % pid)
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)
print('CHILD %6s: Pausing to wait for signal' % pid)
sys.stdout.flush()
time.sleep(3)

if not received:
    print('CHILD %6s: Never received signal' % pid)

"""
SHOULD BE SEPARATE FILE
PARENT PROCESS:

import os
import signal
import subprocess
import time
import sys

proc = subprocess.Popen(['python', 'signal_child.py'])
print 'PARENT      : Pausing before sending signal...'
sys.stdout.flush()
time.sleep(1)
print 'PARENT      : Signaling child'
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
"""
