import os
import sys
import shutil
import threading
import datetime


def remove_blanks(arr):  # function removing blanks
    return arr.remove('')


def replace_path(old_value, new_value):  # function replacing path
    return old_value.replace(new_value, "")


# function returning difference of two arrays
def difference_of_arrays(array_one, array_two):
    return list(set(array_one) - set(array_two))


def flush_log(log_file):  # function flushing the log to the log file
    return log_file.flush()


def write_log(path):  # function writing log to the log file
    return log_file.write(path + "\n")


def is_file(name):  # function to check if file/folder name is a file
    return os.path.isfile(name)


def is_folder(name):  # function to check if file/folder name is a folder
    return os.path.isdir(name)


def check_path_exists(path):  # function to check if a path exists
    return os.path.exists(path)


def remove_file(name):  # function to remove a file
    return os.remove(name)


def remove_folder(name):  # function to remove a folder
    return shutil.rmtree(name)


def get_current_time():  # function to get current timestamp
    return datetime.datetime.now()


def get_modified_time(name):  # function to get the timestamp a file was modified at
    return os.path.getmtime(name)


def join_path(a, b):  # function to concatenate paths
    return os.path.join(a, b)


def copy_file(source, destination):  # function to copy a file from source to destination
    return shutil.copy(source, destination)


def display_exception(e):  # function to display exceptions
    return print(e)


def display_log(log):  # function to display logs
    return print(log)


def list_dir(name):  # function to list all files and directories
    return os.listdir(name)


def append_to_arr(a, b):  # function to append an item to a list
    return a.append(b)


def ignore_files(directory, files):  # function to ignore files and folders in the directory
    return [file for file in files if is_file(join_path(directory, file)) or is_folder(join_path(directory, file))]


# function to create a new folder
def create_folder(source, destination):
    return shutil.copytree(source, destination, ignore=ignore_files,
                           dirs_exist_ok=False)


def copy_folder(source, destination):  # function to copy a new folder
    return shutil.copytree(source, destination, ignore=ignore_files,
                           dirs_exist_ok=True)


def get_directories(root_dir_path, root_dir_contents):  # function to get directories
    try:
        for path in list_dir(root_dir_path):
            new_path = join_path(root_dir_path, path)
            append_to_arr(root_dir_contents, new_path)
            if is_folder(new_path):
                get_directories(new_path, root_dir_contents)
        return root_dir_contents
    except Exception as e:
        display_exception(e)


# function to remove files from replica when not in source
def remove_operation(source_path, replica_path, source_contents, replica_contents):
    try:
        source_contents_new = []
        replica_contents_new = []
        for source_content in source_contents:
            append_to_arr(source_contents_new, replace_path(
                source_content, source_path))
        for replica_content in replica_contents:
            append_to_arr(replica_contents_new, replace_path(
                replica_content, replica_path))
        remove_blanks(source_contents_new)
        remove_blanks(replica_contents_new)
        # get all files in replica and not in source
        diff = difference_of_arrays(replica_contents_new, source_contents_new)
        for item in diff:
            name = join_path(replica_path, item)
            str_send = "Deleted " + name + " at " + str(get_current_time())
            if is_file(name):
                remove_file(name)
                display_log(str_send)
                write_log(str_send)
                flush_log(log_file)
            elif is_folder(name):
                remove_folder(name)
                display_log(str_send)
                write_log(str_send)
                flush_log(log_file)
    except Exception as e:
        display_exception(e)


# function to create a file in replica
def create_file_in_replica(source, replica):
    try:
        copy_file(source, replica)
        str_send = "Created " + replica + " at " + str(get_current_time())
        display_log(str_send)
        write_log(str_send)
        flush_log(log_file)
    except Exception as e:
        display_exception(e)


def copy_file_to_replica(source, replica):  # function to copy a file to replica
    try:
        copy_file(source, replica)
        str_send = "Modified " + replica + " at " + str(get_current_time())
        display_log(str_send)
        write_log(str_send)
        flush_log(log_file)
    except Exception as e:
        display_exception(e)


# function to create a folder in replica
def create_folder_in_replica(source, replica):
    try:
        create_folder(source, replica)
        str_send = "Created " + replica + " at " + str(get_current_time())
        display_log(str_send)
        write_log(str_send)
    except Exception as e:
        display_exception(e)


# function to copy a folder to replica
def copy_folder_to_replica(source, replica):
    try:
        copy_folder(source, replica)
        str_send = "Modified " + replica + " at " + str(get_current_time())
        display_log(str_send)
        write_log(str_send)
        flush_log(log_file)
    except Exception as e:
        display_exception(e)


# function to create files/folders and copy file/folders
def create_copy_operations(source_path, replica_path):
    try:
        for file in list_dir(source_path):
            if(file.startswith(".")):
                continue
            source = join_path(source_path, file)
            replica = join_path(replica_path, file)
            if is_file(source):
                if(check_path_exists(replica) and get_modified_time(source) > get_modified_time(replica)):
                    copy_file_to_replica(source, replica)
                elif(not check_path_exists(replica)):
                    create_file_in_replica(source, replica)
                else:
                    continue
            if is_folder(source):
                if(check_path_exists(replica) and get_modified_time(source) > get_modified_time(replica)):
                    copy_folder_to_replica(source, replica)
                elif(not check_path_exists(replica)):
                    create_folder_in_replica(source, replica)
                create_copy_operations(source, replica)
    except Exception as e:
        display_exception(e)


# initialisation from command line arguments
source_path = sys.argv[1]
replica_path = sys.argv[2]
sync_interval = sys.argv[3]
log_file_path = sys.argv[4]

if not source_path or not replica_path:
    raise NameError('Required path to directories')

# open the log file
log_file = open(
    log_file_path, "w")


def synchronize_folders():  # function to synchronize folders periodically
    try:
        create_copy_operations(source_path, replica_path)
        get_source_contents = get_directories(
            source_path, root_dir_contents=[source_path])
        get_replica_contents = get_directories(
            replica_path, root_dir_contents=[replica_path])
        remove_operation(source_path, replica_path,
                         get_source_contents, get_replica_contents)
        threading.Timer(int(sync_interval), synchronize_folders).start()
    except Exception as e:
        display_exception(e)


synchronize_folders()
