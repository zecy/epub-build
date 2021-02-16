#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import zipfile


def epubzip(book_dir, book_title):
    """This Zip Script is used to build the .epub file"""

    list = []

    # book_title = book_title.decode('utf8') # Py2

    # book_title = book_title.encode('gbk') # Py2

    for i in os.walk(book_dir):
        for l in i[2]:
            list.append(os.path.join(i[0], l))

    z = zipfile.ZipFile(book_title + '.epub', 'w')

    for i in list:
        zipdir = i.replace(book_dir + '\\', '')  # On Windows
        # zipdir = i.replace(book_dir + '/', '') # On *nix
        z.write(i, zipdir)
