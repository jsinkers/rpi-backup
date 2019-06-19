# tidy the working folder where backups are created.  keep only the last num_backups_to_keep files, provided
# that they have been backed up to backup_folder.
import os
import glob
import logging

logging.basicConfig(level=logging.DEBUG)

working_folder = "/home/pi/.octoprint/data/backup"
backup_folder = "/mnt/nasty_backup"
num_backups_to_keep = 3

assert(os.path.exists(backup_folder))
assert(os.path.exists(working_folder))

# move to working folder and get a backup file listing
os.chdir(working_folder)
files = glob.glob("*.zip")

# sort files by modification date (ascending)
files.sort(key=os.path.getmtime)

# find the files to delete.  we will keep the most recent ones
del_files = files[:-num_backups_to_keep]

# check if these files have been copied to the mount point
backup_files = glob.glob(os.path.join(backup_folder,"*.zip"))
backup_files = [os.path.basename(x) for x in backup_files]
del_files = [x for x in del_files if x in backup_files]
not_backed_up_files = [x for x in files if x not in backup_files]

logging.info("Not backed up: \n" + "\n".join(not_backed_up_files))
logging.info("To delete: \n" + "\n".join(del_files))

# now delete the files
for file in del_files:
    if os.path.exists(file):
        os.remove(file)
        logging.info("Deleted " + file)

logging.info("Backup tidying complete")

