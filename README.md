daemontools
===========

Python Daemon Tools

A python module to make unix daemons with ease.
Just call daemontools.startDaemon(mainFunc, pidfile, termFunc)
where

  - mainFunc is your program main function to daemonize
  - pidfile - is the filename where process id would be stored
  - termFunc is the term signal handler
 
