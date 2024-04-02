
from .service import LVCS

lvcs = LVCS()
# lvcs.init(
#     path = "/home/preetam/Desktop/Projects/LVCS/LVCS_Server/LVCS_Hub/Client/Test/"
# )

lvcs.commit(
    path = "/home/preetam/Desktop/Projects/LVCS/LVCS_Server/LVCS_Hub/Client/Test/",
    commit=True
)