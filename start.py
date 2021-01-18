#!/usr/bin/python3

import os

# Schedule a filesystem scan at 13:00 (GMT) (which is 11PM) every FRIDAY.
os.system("echo \"0 13 * * fri   /scan.sh > /proc/1/fd/1 2>&1\" > /root.crontab")
os.system("fcrontab -u root /root.crontab")
os.system("rm /root.crontab")

# Bootstrap the database if clamav is running for the first time
os.system("[ -f /data/main.cvd ] || freshclam")

# Run the update daemon
os.system("freshclam -d -c 6")

# Run cron
os.system("/usr/sbin/fcron -d")

# Run clamav
os.system("clamd")
