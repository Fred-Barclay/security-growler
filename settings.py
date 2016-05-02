"""Setup and defaults for Security Growler app"""

from os.path import expanduser, isfile
from sys import platform as _platform

APP_NAME = 'Security Growler'

# {ports or files to watch: parser (or list of parsers)}
WATCHED_SOURCES = {
    # 80: 'http_auth',      # TODO
    21: 'connections',      # FTP
    445: 'connections',     # SMB
    585: 'connections',     # AFP
    3689: 'connections',    # iTunes sharing
    3306: 'connections',    # MySQL
    5432: 'connections',    # PostgreSQL
    5900: 'vnc',            # VNC
    #'/var/log/system.log': ('sudo', 'ssh', 'portscan', 'ostiarius'),
    'systemd': ('sudo', 'ssh', 'portscan', 'ostiarius'),
}

# Enabled output/display methods
LOGGERS = [
    'stdout',
    'logfile',
    #'osxnotifications',
    'gnomenotifications',
    # 'growl',
]

# Delay in seconds between logfile checks
POLLING_SPEED = 2

# File logger output settings
EVENT_LOGFILE = None
if _platform == "Darwin":
    EVENT_LOGFILE = expanduser('~/Library/Logs/SecurityGrowler.log')
else:
    EVENT_LOGFILE = expanduser('~/.logs/SecurityGrowler.log')

# Growl/OSX notification display settings
INFO_TYPE = 'secnotify'
INFO_ICON = 'https://pirate.github.io/security-growler/notify.png'
INFO_TITLE = 'Security Info'
INFO_STICKY = False
INFO_PRIORITY = 1
INFO_SOUND = False

ALERT_TYPE = 'secalert'
ALERT_ICON = 'https://pirate.github.io/security-growler/alert.png'
ALERT_TITLE = 'Security ALERT'
ALERT_STICKY = True
ALERT_PRIORITY = 2
ALERT_SOUND = True

NOTIFICATION_TYPES = [INFO_TYPE, ALERT_TYPE]



### DO NOT MODIFY BELOW THIS LINE ###
WATCHED_SOURCES = {
    source: parsers for source, parsers in WATCHED_SOURCES.items()
    if type(source) == int or isfile(source) or source == 'systemd'
}