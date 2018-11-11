#!/usr/bin/python3
import sys
from clarifairy import *
from file_crawler import *

images = disk_images(sys.argv[1])

tags = sys.argv[2:]

matches = []

for image in images:
    if len([c for c in list_concepts(image) if c in tags]):
        matches.append(image)

print(list(set(matches)))