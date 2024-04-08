
import os
import copy

ROOT_PATH = r"/home/preetam/Desktop/Hub/"

def iterate(directory):
    directory = ROOT_PATH + directory
    tracked_files = dict()
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != '.lvcs']
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as fd:
                file_content = fd.read()
            fd.close()
            if filepath.startswith(directory):
                filepath = filepath[len(directory):]
            tracked_files[filepath] = file_content
    return tracked_files

def constructFtree(directory):
    dir = {

    }

    cur_dir = dir

    tracked_files = iterate(directory)
    for filename, content in tracked_files.items():
        dirs = filename.split('/')
        for idx in range(len(dirs)):
            if dirs[idx] not in cur_dir.keys():
                cur_dir[str(dirs[idx])] = {

                }
                dir = copy.deepcopy(dir)
                cur_dir = 


tracked_files = iterate(
    directory="folder/"
)

print(tracked_files)