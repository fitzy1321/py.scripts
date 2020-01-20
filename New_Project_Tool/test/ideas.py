# ideas.py
# a sandbox script for trying out new ideas, or to make a note of something
# import os


# _file_name = "creator.json"
# _path = os.path.expanduser("~")
# _prefix = "/." if os.name != "nt" else "\\"
# _full_path = _path + _prefix + _file_name

# print(_full_path)
# print(os.path.isfile(_full_path))

# print(platform.system())

# __path = expanduser("~")
# print(__path)

# print("Testing something")

# dict = {"obj1": {"foo": 12, "bar": 32}, 24: ""}

# if "obj1" in dict:
#     print("derp")
#     if ("whiz", "fuzz") in dict["obj1"]:
#         print("you're an idiot")
#     elif "bar" in dict["obj1"]:
#         print("FUCK YES!")
# else:
#     print("you dun goofed")

import sys

if (sys.version_info.major, sys.version_info.minor) != (3, 7):
    print("You need to use python 3.7 or greater to run this app.")
