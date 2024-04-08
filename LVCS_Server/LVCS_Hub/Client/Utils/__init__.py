
# To be treated as a common entry point for all functionalities 

from .filehashing import FileHashing
from .difftracker import DiffTracking


lvcs_hasher = FileHashing()
lvcs_diff = DiffTracking()