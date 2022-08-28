#!/usr/bin/python3

import os

LOAD_PATH = "sass/"

SASS_TASKS = (
    {"SRC_PATH": "sass/AutumnQuic.scss", "DES_PATH": "static/css/AutumnQuic.css"},
    {"SRC_PATH": "content/RFC8999_Chinese_Simplified/sass/RFC8999.scss",
        "DES_PATH": "content/RFC8999_Chinese_Simplified/css/RFC8999.css"},
    {"SRC_PATH": "content/RFC9000_Chinese_Simplified/sass/RFC9000.scss",
        "DES_PATH": "content/RFC9000_Chinese_Simplified/css/RFC9000.css"},
    {"SRC_PATH": "content/RFC9001_Chinese_Simplified/sass/RFC9001.scss",
        "DES_PATH": "content/RFC9001_Chinese_Simplified/css/RFC9001.css"},
    {"SRC_PATH": "content/RFC9002_Chinese_Simplified/sass/RFC9002.scss",
        "DES_PATH": "content/RFC9002_Chinese_Simplified/css/RFC9002.css"},
    {"SRC_PATH": "content/RFC9114_Chinese_Simplified/sass/RFC9114.scss",
        "DES_PATH": "content/RFC9114_Chinese_Simplified/css/RFC9114.css"},
    {"SRC_PATH": "content/RFC9204_Chinese_Simplified/sass/RFC9204.scss",
        "DES_PATH": "content/RFC9204_Chinese_Simplified/css/RFC9204.css"},
    {"SRC_PATH": "content/RFC9221_Chinese_Simplified/sass/RFC9221.scss",
        "DES_PATH": "content/RFC9221_Chinese_Simplified/css/RFC9221.css"},
    {"SRC_PATH": "content/RFC9250_Chinese_Simplified/sass/RFC9250.scss",
        "DES_PATH": "content/RFC9250_Chinese_Simplified/css/RFC9250.css"},
)

if __name__ == "__main__":
    for sass in SASS_TASKS:
        cmd = "sass --load-path=" + LOAD_PATH + " " + \
            sass["SRC_PATH"] + " " + sass["DES_PATH"]
        print(cmd)
        os.system(cmd)
