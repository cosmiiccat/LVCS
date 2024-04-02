import os
import uuid
import json
import copy
import glob
from datetime import datetime
from ..Utils.__init__ import (
    lvcs_hasher,
    lvcs_diff
)

class LVCS:

    def __init__(self):
        self.path = None

    def init(self, path):
            
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
                    "changes": '',
                    "datetime": dt_string
                }

                state = {

                }

                # print(content)

                for file_path in snap.keys():
                    with open(self.path + file_path, 'r') as fd:
                        data = fd.read()
                        state[file_path] = copy.deepcopy(data)
                        changes, data = lvcs_diff.diff(old_content="", new_content=data).split('@@\n')
                        changes = changes.split('@@')[-1]
                        content['changes'] = changes
                        content['data'][file_path] = copy.deepcopy(
                            data
                        )
                    fd.close()

                with open(self.path + '.lvcs/' + 'state.json', 'w') as file:
                    json.dump(
                        state, 
                        file, 
                        indent=4
                    )
                file.close()

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
    
    
    def commit(self, path, commit = False):

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
                "changes": '',
                "datetime": dt_string
            }

            state = {

            }

            with open(self.path + '.lvcs/' + 'state.json', 'rb') as file:
                last_state = json.load(
                    file
                )
            file.close()

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

            for file_name in created_files:
                
                with open(self.path + file_name, 'r') as f:
                    data = f.read()
                    state[file_name] = copy.deepcopy(data)
                    changes, data = lvcs_diff.diff(
                        old_content="",
                        new_content=data
                    ).split('@@\n')
                    changes = changes.split('@@')[-1]
                    content['changes'] = changes
                    content['data'][file_name] = data
                f.close()

            for file_name in modified_files:
                
                with open(self.path + file_name, 'r') as f:
                    data = f.read()
                    state[file_name] = copy.deepcopy(data)
                    changes, data = lvcs_diff.diff(
                        old_content=last_state[file_name],
                        new_content=data
                    ).split('@@\n')
                    changes = changes.split('@@')[-1]
                    content['changes'] = changes
                    content['data'][file_name] = data
                f.close()

            if isChanged:
                if not commit:
                    return {
                        "status": "True",
                        "data": {
                            "created_files": created_files,
                            "modified_files": modified_files,
                            "deleted_files": deleted_files,
                            "changes": content['changes']
                        }
                    }
                
                with open(self.path + '.lvcs/' + 'state.json', 'w') as file:
                    json.dump(
                        state, 
                        file, 
                        indent=4
                    )
                file.close()

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