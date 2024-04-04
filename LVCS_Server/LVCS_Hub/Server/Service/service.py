import os
import uuid
import json
import copy
import glob
import difflib
import shutil
from datetime import datetime
class LVCS:

    def __init__(self):
        self.path = None

    def pull(self, path):

        self.path = path

        previous_commits = glob.glob(
            os.path.join(self.path + '.lvcs/', "*")
        )

        commits = glob.glob(
            os.path.join(self.path + '.commits/', "*")
        )

        commits = list(set(commits) - set(previous_commits))
        sorted_commits = sorted(commits, key=os.path.getctime)

        for commit_path in sorted_commits:
            commit = str()
            with open(self.path + commit_path, 'r') as fd:
                commit = fd.read()
            fd.close()
            for file_path in commit['deleted_files']:
                os.remove(self.path + file_path)

            for file_path in commit['created_files']:
                with open(self.path + file_path, 'w') as fd:
                    diff = str()
                    diff += '--- \n'
                    diff += '+++ \n'
                    diff == f'@@{commit["changes"][file_path]}@@\n'
                    diff = commit['data'][file_path]
                    new_content = ''.join(list(difflib.restore(diff, 2)))
                    fd.write(
                        new_content = new_content
                    )

            for file_path in commit['modified_files']:
                with open(self.path + file_path, 'w') as fd:
                    diff = str()
                    diff += '--- \n'
                    diff += '+++ \n'
                    diff == f'@@{commit["changes"][file_path]}@@\n'
                    diff = commit['data'][file_path]
                    new_content = ''.join(list(difflib.restore(diff, 2)))
                    fd.write(
                        new_content = new_content
                    )

            shutil.rmtree(self.path + '.lvcs/')
            os.rename(self.path + '.commits', self.path + './lvcs')

            

            



