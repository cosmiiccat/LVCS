
from .service import LVCS

lvcs = LVCS()
# lvcs.config(
#     username="Preetam",
#     email="preetamOfficial@gmail.com",
#     path = "/home/preetam/Desktop/folder/"
# )
lvcs.init(
    path = "/home/preetam/Desktop/folder/"
)

# lvcs.commit(
#     path="/home/preetam/Desktop/folder/",
# )

# lvcs.commit(
#     path = "/home/preetam/Desktop/folder/",
#     commit=True,
#     commit_message="Modified python_files"
# )

# lvcs.pull(
#     path = "/home/preetam/Desktop/folder1/"
# )