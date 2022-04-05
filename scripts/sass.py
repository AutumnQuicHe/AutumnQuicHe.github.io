#!/usr/bin/python3

import os

LOAD_PATH = "sass/"

SASS_TASKS = (
    {"SRC_PATH": "sass/fangqiuhang.scss", "DES_PATH": "static/css/fangqiuhang.css"},
    {"SRC_PATH": "content/RFC8999_Chinese_Translation/sass/RFC8999.scss",
        "DES_PATH": "content/RFC8999_Chinese_Translation/css/RFC8999.css"},
    {"SRC_PATH": "content/RFC9000_Chinese_Translation/sass/RFC9000.scss",
        "DES_PATH": "content/RFC9000_Chinese_Translation/css/RFC9000.css"},
    {"SRC_PATH": "content/RFC9001_Chinese_Translation/sass/RFC9001.scss",
        "DES_PATH": "content/RFC9001_Chinese_Translation/css/RFC9001.css"},
)

if __name__ == "__main__":
    for sass in SASS_TASKS:
        cmd = "sass --load-path=" + LOAD_PATH + " " + \
            sass["SRC_PATH"] + " " + sass["DES_PATH"]
        print(cmd)
        os.system(cmd)
