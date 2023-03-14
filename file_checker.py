import os
import sys
import re

def main(path):
    results = os.scandir(path)
    jpg = re.compile(r"\.jpg$", re.IGNORECASE)
    dng = re.compile(r"\.dng$", re.IGNORECASE)
    arw = re.compile(r"\.arw$", re.IGNORECASE)
    files = []
    duplicates = []

    def get_files(results):
        for file in results:
            if file.is_dir():
                results = os.scandir(file.path)
                get_files(results)
            elif ({'name': file.name, 'size': file.stat().st_size} in files):
                # print(f"{file.name} is a duplicate!")
                duplicates.append(file.path)
            elif file.is_file() and (jpg.search(file.name) or dng.search(file.name) or arw.search(file.name)):
                files.append({'name': file.name, 'size': file.stat().st_size})

    get_files(results)

    result_file = open('./duplicates.txt', 'w+')
    for file in duplicates:
        result_file.write(f"{file}\n")

    # print(duplicates)

if __name__ == "__main__":
    main(str(sys.argv[1]))
