# rpi-backup
Tools to help with backing up rpi

# Octoprint Backup Generation
You can generate backups automatically by adding a cron task
TODO: add more info

# tidy_folder.py

Requires python 3.

Original intention was to keep an Octoprint backup folder tidy.  The script
keeps only a specified number of the most recent backup files, and removes
older ones as long as they have been backed up to a specified mount. 

User must modify the file to indicate:

- working_folder: mountpoint backups should have been copied to
- backup_folder: location backup zips are created
- num_backups_to_keep: number of most recent backups to keep

Written in python as it would take me too long to figure out how to 
get a bash script going.

