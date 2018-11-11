#!/usr/bin/python3
import sys
from clarifairy import *
from file_crawler import *

images = disk_images(sys.argv[1])
#print(images)

tags = sys.argv[2:]

matches = []

for image in images:
    if len([c for c in list_concepts(image) if c in tags]):
        if image not in matches:
            matches.append(image)
            print(image)

