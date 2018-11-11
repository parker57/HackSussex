#!/usr/bin/python3
import os
import imghdr


def disk_images(start):
    if start[-1] is not '/':
        start += '/'

    image_extensions = ['jpeg', 'bmp', 'jpg', 'png']
    # traverse root directory, and list directories as dirs and files as files
    all_files = []
    for root, dirs, files in os.walk(start):
        for file in files:
            if root[-1] is not '/':
                all_files.append(root + '/' + file) #Might need to add dash if looking in current directory
            else:
                all_files.append(root + file)

    images = []
    for f in all_files:
        try:
            if str(imghdr.what(f)).lower() in image_extensions:
                images.append(f)
        except FileNotFoundError:
            continue
        except OSError:
            continue

    return images


