import os
import uuid
import json
import copy
import glob
import shutil
import difflib
from datetime import datetime

class LVCS:

    def __init__(self):
        self.path = None
        self.global_path = None
    
    def pull(self, path):

        self.path = path

        if os.path.exists(self.path + '.lvcs/'):
            
            previous_commits = glob.glob(
                os.path.join(self.path + '.lvcs/', "*")
            )
        else:
            previous_commits=[]

        commits = glob.glob(
            os.path.join(self.path + '.commits/', "*")
        )

        for idx in range(len(commits)):
            commits[idx] = commits[idx].split(self.path + '.commits/')[-1]

        for idx in range(len(previous_commits)):
            previous_commits[idx] = previous_commits[idx].split(self.path + '.lvcs/')[-1]

        commits = list(set(commits) - set(previous_commits))
        
        for id in range(len(commits)):
            commits[id] = self.path + '.commits/' + commits[id]
        
        # sorted_commits = sorted(commits, key=os.path.getctime)
        sorted_commits = sorted(commits, key=os.path.basename)
        print(sorted_commits)
        
        for id in range(len(sorted_commits)):
            sorted_commits[id] = sorted_commits[id].split(self.path + '.commits/')[-1]

        for commit_path in sorted_commits:
            commit = str()
            with open(self.path + '.commits/' + commit_path, 'r') as fd:
                commit = fd.read()
            fd.close()
            # print(commit)
            commit = json.loads(commit)
            # print(commit)
            for file_path in commit['deleted_files']:
                os.remove(self.path + file_path)

            for file_path in commit['created_files']:

                dirs = file_path.split('/')
                dirs.pop()
                cur_path = self.path
                for dir in dirs:
                    cur_path += (dir + '/')
                    if not os.path.exists(cur_path):
                        os.makedirs(cur_path)

                with open(self.path + file_path, 'w') as fd:
                    diff = str()
                    # diff += '--- \n'
                    # diff += '+++ \n'
                    # diff == f'@@{commit["changes"][file_path]}@@\n'
                    # print("Creating File")
                    diff = commit['data'][file_path].splitlines()
                    augmented_diff = list()
                    for id in range(len(diff)):
                        line = diff[id]
                        if '+' in line:
                            line = '+ ' + line[1:]
                        elif '-' in line:
                            line = '- ' + line[1:]
                        else:
                            line = ' ' + line
                        augmented_diff.append(line)
                        if(id != len(diff) - 1):
                            augmented_diff.append('')
                    
                    new_content_list = list(difflib.restore(augmented_diff, 2))
                    new_content = ''
                    for line in new_content_list:
                        new_content += line
                        new_content += '\n'
                    # new_content = ''.join(list(difflib.restore(diff, 2)))
                    # print("\n\n\n" + new_content)
                    fd.write (
                        new_content
                    )

            for file_path in commit['modified_files']:
                with open(self.path + file_path, 'w') as fd:
                    diff = str()
                    # diff += '--- \n'
                    # diff += '+++ \n'
                    # diff == f"@@{commit['changes'][file_path]}@@\n"
                    # diff = commit['data'][file_path].splitlines()
                    diff = commit['data'][file_path].splitlines()
                    augmented_diff = list()
                    for id in range(len(diff)):
                        line = diff[id]
                        if '+' in line:
                            line = '+ ' + line[1:]
                        elif '-' in line:
                            line = '- ' + line[1:]
                        else:
                            line = ' ' + line
                        augmented_diff.append(line)
                        if(id != len(diff) - 1):
                            augmented_diff.append('')
                    
                    # print(augmented_diff)
                    new_content_list = list(difflib.restore(augmented_diff, 2))
                    new_content = ''
                    for line in new_content_list:
                        new_content += line
                        new_content += '\n'
                    # new_content = ''.join(list(difflib.restore(diff, 2)))
                    # print(new_content)
                    fd.write(
                        new_content
                    )
        if os.path.exists(self.path + '.lvcs/'):
            shutil.rmtree(self.path + '.lvcs/')
        os.rename(self.path + '.commits', self.path + '.lvcs')

        return {
            "status": "True",
            "data": "Pushed successfully!" 
        }
    
if __name__=="__main__":
    LVCS_PULL = LVCS()
    LVCS_PULL.pull("/home/abhik/Desktop/LVCS_test/server/testing2/")