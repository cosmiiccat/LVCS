import os
import uuid
import json
import copy
import glob
import shutil
import difflib
from datetime import datetime
from ..Utils.__init__ import (
    lvcs_hasher,
    lvcs_diff
)

class LVCS:

    def __init__(self):
        self.path = None
        self.global_path = None

    def config(self, path, username, email):

        dirs = path.split('/')
        cur_path = '/'
        for dir in dirs:
            cur_path += (dir + '/')
            if dir == "Desktop":
                self.global_path = copy.deepcopy(cur_path)
                break

        if not os.path.exists(self.global_path + 'lvcs.config'):
            with open(self.global_path + 'lvcs.config', 'w') as file:
                json.dump(
                    {
                        "username": username,
                        "email": email
                    },
                    file,
                    indent=4
                )

            return {
                "status": "True",
                "data": f"LVCS is configured with username:{username} and email:{email}"
            }
        return {
            "status": "False",
            "data": "LVCS is already configured"
        }
    
    def reconfig(self, username, email):

        with open(self.global_path + 'lvcs.config', 'w') as file:
            json.dump(
                {
                    "username": username,
                    "email": email
                },
                file,
                indent=4
            )

        return {
            "status": "True",
            "data": "LVCS is re configured with username:{username} and email:{email}"
        }


    def init(self, path):

        dirs = path.split('/')
        cur_path = '/'
        for dir in dirs:
            cur_path += (dir + '/')
            if dir == "Desktop":
                self.global_path = copy.deepcopy(cur_path)
                break

        if not os.path.exists(self.global_path + 'lvcs.config'):
            return {
                "status": "False",
                "data": "LVCS is not yet configured"
            }
        
        dirs = path.split('/')
        cur_path = '/'
        for dir in dirs:
            cur_path += (dir + '/')
            if dir == "Desktop":
                self.global_path = copy.deepcopy(cur_path)
                break
        
        with open(self.global_path + 'lvcs.config', 'r') as file:
            details = json.loads(
                file.read()
            )
        file.close()
        
        dirs = path.split('/')
        status = True
        cur_path = ''
        for dir in dirs:
            cur_path += (dir + '/')
            if os.path.exists(cur_path + '.lvcs'):
                status = False
                break
        if status:
            
            # Check for circular .lvcs folder tree traversal ---> TBD

            os.makedirs(path + '.lvcs', exist_ok=True)
            self.path = path

            snap = lvcs_hasher.take_snap(
                directory=self.path
            )

            now = datetime.now()
            _id = str(uuid.uuid4())
            dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
            commit_name = f"{dt_string}_commit.json"

            content = {
                "_id": _id, 
                "snap": snap, 
                "data": {
                    
                },
                "created_files": [],
                "modified_files": [],
                "deleted_files": [],
                "changes": {

                },
                "username": details['username'],
                "email": details['email'],
                "commit_message": "Initial Commit",
                "datetime": dt_string
            }

            # state = {

            # }

            # print(content)

            for file_path in snap.keys():
                with open(self.path + file_path, 'r') as fd:
                    data = fd.read()
                    content['created_files'].append(file_path)
                    # state[file_path] = copy.deepcopy(data)
                    changes, data = lvcs_diff.diff(old_content="", new_content=data).split('@@\n')
                    changes = changes.split('@@')[-1]
                    content['changes'][file_path] = changes
                    content['data'][file_path] = copy.deepcopy(
                        data
                    )
                fd.close()

            # with open(self.path + '.lvcs/' + 'state.json', 'w') as file:
            #     json.dump(
            #         state, 
            #         file, 
            #         indent=4
            #     )
            # file.close()

            with open(self.path + '.lvcs/' + commit_name, 'w') as file:
                json.dump(
                    content, 
                    file, 
                    indent=4
                )
            file.close()

            

            return {
                "status": "True",
                "data": "This folder is now being tracked by LVCS"
            }
    
        return {
            "status": "False",
            "data": "This folder is already being tracked by LVCS"
        }

    
    def commit(self, path, commit = False, commit_message=""):

        dirs = path.split('/')
        cur_path = '/'
        for dir in dirs:
            cur_path += (dir + '/')
            if dir == "Desktop":
                self.global_path = copy.deepcopy(cur_path)
                break

        with open(self.global_path + 'lvcs.config', 'r') as file:
            details = json.loads(
                file.read()
            )
        file.close()


        dirs = path.split('/')
        status = True
        cur_path = ''
        for dir in dirs:
            cur_path += (dir + '/')
            if os.path.exists(cur_path + '.lvcs'):
                self.path = cur_path
                status = False
                break

        if not status:
            snap = lvcs_hasher.take_snap(
                directory=self.path
            )

            previous_snaps = glob.glob(
                os.path.join(self.path + '.lvcs/', "*")
            )
            latest_snap = max(previous_snaps, key=os.path.getctime)
            latest_snap_filename = os.path.basename(
                latest_snap
            )
            if latest_snap_filename == 'state.json':
                sorted_snaps = sorted(previous_snaps, key=os.path.getctime, reverse=True)
                latest_snap = sorted_snaps[1]
                latest_snap_filename = os.path.basename(
                    latest_snap
                )

            with open(self.path + '.lvcs/' + latest_snap_filename, 'rb') as file:
                last_snap = json.load(file)
            file.close()

            deleted_files = list()
            created_files = list()
            modified_files = list()

            isChanged = False

            now = datetime.now()
            _id = str(uuid.uuid4())
            dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
            commit_name = f"{dt_string}_commit.json"

            content = {
                "_id": _id, 
                "snap": snap, 
                "data": {
                    
                },
                "created_files": [],
                "modified_files": [],
                "deleted_files": [],
                "changes": {

                },
                "username": details['username'],
                "email": details['email'],
                "commit_message": commit_message,
                "datetime": dt_string
            }

            # state = {

            # }

            # with open(self.path + '.lvcs/' + 'state.json', 'rb') as file:
            #     last_state = json.load(
            #         file
            #     )
            # file.close()

            for file in last_snap['snap'].keys():
                if file not in snap.keys():
                    deleted_files.append(
                        file
                    )
                    isChanged = True

            for file in snap.keys():
                if file not in last_snap['snap'].keys():
                    created_files.append(
                        file
                    )
                    # store new content
                    isChanged = True
                
            for file in snap.keys():
                if file in last_snap['snap'].keys():
                    if snap[file] != last_snap['snap'][file]:
                        modified_files.append(
                            file
                        )
                        # store changes 
                        isChanged = True

            content["created_files"] = copy.deepcopy(created_files)
            content["modified_files"] = copy.deepcopy(modified_files)
            content["deleted_files"] = copy.deepcopy(deleted_files)

            for file_name in created_files:
                
                with open(self.path + file_name, 'r') as f:
                    data = f.read()
                    # state[file_name] = copy.deepcopy(data)
                    changes, data = lvcs_diff.diff(
                        old_content="",
                        new_content=data
                    ).split('@@\n')
                    changes = changes.split('@@')[-1]
                    content['changes'][file_name] = changes
                    content['data'][file_name] = data
                f.close()

            for file_name in modified_files:
                
                with open(self.path + file_name, 'r') as f:
                    data = f.read()
                    diff = str()
                    # diff += '--- \n'
                    # diff += '+++ \n'
                    # diff += f"@@{last_snap['changes'][file_name]}@@\n"
                    diff = last_snap['data'][file_name].splitlines()
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
                    
                    old_content_list = list(difflib.restore(augmented_diff, 2))
                    old_content = ''
                    for line in old_content_list:
                        old_content += line
                        old_content += '\n'
                    # state[file_name] = copy.deepcopy(data)
                    changes, data = lvcs_diff.diff(
                        old_content=old_content,
                        new_content=data
                    ).split('@@\n')
                    changes = changes.split('@@')[-1]
                    content['changes']['file_name'] = changes
                    content['data'][file_name] = data
                f.close()

            # print({
            #     "created_files": created_files,
            #     "modified_files": modified_files,
            #     "deleted_files": deleted_files,
            #     "changes": content['changes']
            # })

            if isChanged:
                if not commit:
                    print({
                        "status": "True",
                        "data": {
                            "created_files": created_files,
                            "modified_files": modified_files,
                            "deleted_files": deleted_files,
                            "changes": content['changes']
                        }})

                    return {
                        "status": "True",
                        "data": {
                            "created_files": created_files,
                            "modified_files": modified_files,
                            "deleted_files": deleted_files,
                            "changes": content['changes']
                        }
                    }
                
                # with open(self.path + '.lvcs/' + 'state.json', 'w') as file:
                #     json.dump(
                #         state, 
                #         file, 
                #         indent=4
                #     )
                # file.close()

                with open(self.path + '.lvcs/' + commit_name, 'w') as file:
                    json.dump(
                        content, 
                        file, 
                        indent=4
                    )
                file.close()

                return {
                    "status": "True",
                    "data": {
                        "created_files": created_files,
                        "modified_files": modified_files,
                        "deleted_files": deleted_files,
                        "changes": content['changes'],
                        "commit_status": "True"
                    }
                }
            
            else:
                return {
                    "status": "True",
                    "data": "No changes in the current working directory"
                }
        
        return {
            "status": "False",
            "data": "LVCS not initiated in this directory."
        }
    
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
            "data": "Pulled successfully!" 
        }