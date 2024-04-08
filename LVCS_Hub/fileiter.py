
import os
import copy
import json

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

def convert_to_nested_dict(file_structure):
    result = {}
    for path, content in file_structure.items():
        parts = path.split("/")
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = content
    return result



