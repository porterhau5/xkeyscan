# xkeyscan

Simple script for parsing keycodes from an X-based keylogger on Linux.

## Usage
```
$ python xkeyscan.py -h
Usage: python [-u] xkeyscan.py [LOGFILE]

A simple script for converting xinput output to legible keystokes.
Can process a log file directly when passed as an argument, or can
convert keystrokes in near real-time if tailing a log file.
If tailing a log file, use python's -u switch to avoid buffering.

Examples:
  python xkeyscan.py xkey.log (post-process log file)
  cat xkey.log | python xkeyscan.py (accept logs from stdin)
  tail -f -n +1 xkey.log | python -u xkeyscan.py (tail log file)

Type -h or --help for a full listing of options.
```

## Background

For an introduction to the tool and some example usage, check out my blog post: http://porterhau5.com/blog/xkeyscan-parse-linux-keylogger/

For an in-depth description of using an X-based keylogger, check out @skawasec's blog post: https://www.popped.io/2016/06/natively-keylogging-nix-systems.html

