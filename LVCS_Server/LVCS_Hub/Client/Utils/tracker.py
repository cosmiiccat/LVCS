import os
import uuid
import json
import glob
from datetime import datetime
from __init__ import (
    lvcs_hasher,
    lvcs_diff
)

# TBD - Tracking from root, to be changed to tracking from cur

class Tracker:

    def __init__(self):
        self.path = None

    def track(self, path):

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

            with open(self.path + '.lvcs/' + latest_snap_filename, 'rb') as file:
                last_snap = json.load(file)

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
                "datetime": dt_string, 
                "data": {
                    
                }
            }

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
                
                with open(file_name, 'r') as f:
                    data = file.read()
                    content['data'][file_name] = data
                f.close()

            for file_name in modified_files:
                
                with open(file_name, 'r') as f:
                    data = file.read()
                    content['data'][file_name] = data
                f.close()


            

            
  
lvcsTrack = Tracker()
lvcsTrack.track(path = '/home/preetam/Desktop/Projects/LVCS/LVCS_Server/LVCS_Hub/Client/Utils/')

