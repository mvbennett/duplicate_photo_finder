#!/usr/bin/env python
import os
import sys
import re

def check_ext(filename):
    jpg = re.compile(r"\.jpg$", re.IGNORECASE)
    dng = re.compile(r"\.dng$", re.IGNORECASE)
    arw = re.compile(r"\.arw$", re.IGNORECASE)
    tif = re.compile(r"\.tif$", re.IGNORECASE)
    extensions = [jpg, dng, arw, tif]
    for ext in extensions:
        if ext.search(filename):
            return True

    return False

def isnt_dirs(dirname, dirs = []):
    for dir in dirs:
        if dirname == dir:
            return False

    return True

def main(path, skip_dirs = []):
    if len(skip_dirs) >= 1:
        print(f"Script will skip these directories: {skip_dirs}")
    results = os.scandir(path)
    files = {}
    duplicates = []

    def get_files(results):
        directories = []
        for file in results:
            if file.is_dir() and isnt_dirs(file.name, skip_dirs):
                directories.append(file.path)
            elif ({'name': file.name, 'size': file.stat().st_size} in files.values()):
                original_path = list(files.keys())[list(files.values()).index({'name': file.name, 'size': file.stat().st_size})]
                print(f"duplicate found: {original_path} --> {file.path}")
                duplicates.append((original_path, file.path))
            elif file.is_file() and check_ext(file.name):
                files[file.path] = {'name': file.name, 'size': file.stat().st_size}

        for dir_path in directories:
            results = os.scandir(dir_path)
            get_files(results)

    get_files(results)

    result_file = open('./duplicates.txt', 'w+')
    for original, duplicate in duplicates:
        result_file.write(f"{original}  -->  {duplicate}\n")

    result_file.close()

if __name__ == "__main__":
    if len(sys.argv) > 2:
        skip_dirs = sys.argv[2:]
        main(sys.argv[1], skip_dirs)
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main('.')
