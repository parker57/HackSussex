#!/usr/bin/python

import os
import imghdr


def disk_images(dir):
    if dir[-1] is not '/':
        dir += '/'

    image_extensions = ['jpeg', 'bmp', 'jpg', 'png']
    # traverse root directory, and list directories as dirs and files as files
    all_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            all_files.append(root +'/'+ file)

    images = []
    for f in all_files:
        try:
            if str(imghdr.what(f)).lower() in image_extensions:
                images.append(f)
        except:
            continue

    return images


