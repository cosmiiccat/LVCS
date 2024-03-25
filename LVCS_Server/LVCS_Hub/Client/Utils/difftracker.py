
import difflib

class DiffTracking:

    def __init__(self):
        pass

    def diff(self, old_content, new_content):
        old_lines = old_content.splitlines()
        new_lines = new_content.splitlines()
        changes = list()

        for line in difflib.unified_diff(old_lines, new_lines, lineterm=''):
            changes.append(line)

        return '\n'.join(changes)
    

# tracker = DiffTracking()
# changes = tracker.diff(
#     old_content="Hello, World!\nThis is the old file.\nThis is EOF.",
#     new_content="Hello, World!\nThis is the old file.\n I am adding content to this file.\nThis is EOF.",
# )
# print(changes)