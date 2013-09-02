#!/usr/bin/env python
#
#    python-daemontools
#
#    by Pavel Vorobyov <aquavitale@yandex.ru>
#    https://github.com/viert/daemontools
# 

import os
import atexit
import signal

def __defaultTermHandler(signalnum, frame):
  os.sys.exit(0)


def __removePidfile(pidfile):
  try:
    os.unlink(pidfile)
  except:
    pass

def startDaemon(mainFunc, pidfile, termFunc=__defaultTermHandler):
  if not pidfile is None:
    atexit.register(__removePidfile, pidfile)

  if not termFunc is None:
    signal.signal(signal.SIGTERM, termFunc)

  try:
    pid = os.fork()
  except OSError as e:
    raise Exception, "%s [%d]" % (e.strerror, e.errno)

  if pid == 0:
    os.setsid()
    try:
      pid = os.fork()

    except OSError as e:
      raise Exception, "%s [%d]" % (e.strerror, e.errno)

    if pid == 0:
      mainFunc()

    else:
      if not pidfile is None:
        with open(pidfile, "w") as pf:
          pf.write(str(pid))
      os._exit(0)
  else:
    os._exit(0)
