import os
import time


def change_file_times(directory, new_time):
    """
    Set to work on the current directory and down
    Pass an obsolute or relative path to directory if needed
    Else run script from target parth

    Uses current date time stamp to update file time
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.utime(file_path, times=(new_time, new_time))


directory_path = "F:/May 2006"
new_time = time.time()
change_file_times(directory_path, new_time)
