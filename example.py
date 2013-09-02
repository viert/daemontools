#!/usr/bin/env python

import time
import daemontools

def main():
  time.sleep(300)

if __name__ == '__main__':
  daemontools.startDaemon(main, "example.pid")
