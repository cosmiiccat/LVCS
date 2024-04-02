import os
import uuid
import json
from datetime import datetime
from __init__ import (
    lvcs_hasher
)

class Initializer:

    def __init__(self):
        self.path = None

    def initiate(self, path):

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
                "datetime": dt_string
            }

            # print(content)

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
    
initiator = Initializer()
initiator.initiate(path = '/home/preetam/Desktop/Projects/LVCS/LVCS_Server/LVCS_Hub/Client/Utils/')

