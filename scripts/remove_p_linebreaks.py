#!/usr/bin/python3

'''
WARNNING: python3 please!!!

You should install requirements before by executing:
> pip3 install beautifulsoup4 lxml html5lib
'''

import os

from bs4 import BeautifulSoup
from bs4.element import Tag as bs4elementTag
from bs4.element import NavigableString as bs4elementNavigableString


public_path = os.getcwd() + "/public"


def RemoveLineBreaks(element):
    if isinstance(element, bs4elementTag):
        #print("Before parsing:", element)
        c = element.contents
        for i in range(element.contents.__len__()):
            if isinstance(c[i], bs4elementNavigableString):
                #print("before", x, "after", x.replace("\n", ""))
                #print("Before:", element.contents[i])
                element.contents[i].replace_with(c[i].replace("\n", ""))
                #print("After:", element.contents[i])
            elif isinstance(c[i], bs4elementTag):
                RemoveLineBreaks(element.contents[i])
            else:
                print("Invalid sub element:", c[i])

        #print("After parsing:", element)
    else:
        print("Invalid element:", element, ", type ", type(element))

def ParseHtml(filepath):
    soup = BeautifulSoup(open(filepath), "html.parser")
    ps = soup.find_all('p')
    for x in ps:
        #print(x)
        RemoveLineBreaks(x)

    with open(filepath, 'w') as f:
        #f.write(soup.__str__())
        f.write(str(soup))

def ParseXml(filepath):
    soup = BeautifulSoup(open(filepath), "xml")
    ds = soup.find_all('description')
    for x in ds:
        #print(x, type(x))
        if isinstance(x, bs4elementTag) and isinstance(x.string, bs4elementNavigableString):
            #x.string = x.string.replace("\n", "")
            x.text.replace('\n', '')
            #print("new ", x, type(x.string))
        else:
            #print(filepath, x, type(x), type(x.string))
            pass
    with open(filepath, 'w') as f:
        #f.write(soup.prettify())
        #f.write(soup.__str__())
        f.write(str(soup))

def WalkPath(path="./public"):
    for root, _, files in os.walk(path, followlinks=True):
        for filename in files:
            if filename.endswith(".html"):
                filepath = os.path.join(root, filename)
                #print(filepath)
                ParseHtml(filepath=filepath)
            elif filename.endswith(".xml"):
                filepath = os.path.join(root, filename)
                #print(filepath)
                #ParseXml(filepath=filepath)


if __name__ == "__main__":
    WalkPath(public_path)
    #ParseHtml("/home/sad/fangqiuhang.github.io/public/RFC9114_Chinese_Simplified/index.html")
    #ParseXml("/home/sad/fangqiuhang.github.io/public/RFC9002_Chinese_Translation/Relevant_Differences_between_QUIC_and_TCP/index.xml")
