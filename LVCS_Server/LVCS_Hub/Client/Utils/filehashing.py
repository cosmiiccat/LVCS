
import os
import hashlib

class FileHashing:

    def __init__(self):
        pass

    def compute_file_hash(self, filepath):
        with open(filepath, 'rb') as f:
            return hashlib.sha1(f.read()).hexdigest()
        
    def take_snap(self, directory):
        tracked_files = dict()
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                file_hash = self.compute_file_hash(filepath)
                tracked_files[filepath] = file_hash
        return tracked_files
    
# filehasher = FileHashing()
# snap = filehasher.take_snap(
#     directory=r"/home/preetam/Desktop/Projects/LVCS/LVCS_Server/LVCS_Hub/"
# )
# print(snap)