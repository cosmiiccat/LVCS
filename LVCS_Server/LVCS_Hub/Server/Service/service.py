import os
import uuid
import json
import copy
import glob
from datetime import datetime
class LVCS:

    def __init__(self):
        pass

    def pull(self, commits):

        previous_commits = glob.glob(
            os.path.join(self.path + '.lvcs/', "*")
        )

        commits = list(set(commits) - set(previous_commits))
        sorted_commits = sorted(commits, key=os.path.getctime)

        for commit in sorted_commits:
            pass



