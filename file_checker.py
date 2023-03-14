import os
import sys
import re

def main(path):
    results = os.scandir(path)
    jpg = re.compile(r"\.jpg$", re.IGNORECASE)
    dng = re.compile(r"\.dng$", re.IGNORECASE)
    arw = re.compile(r"\.arw$", re.IGNORECASE)
    files = {}
    duplicates = []

    def get_files(results):
        for file in results:
            if file.is_dir():
                results = os.scandir(file.path)
                get_files(results)
            elif ({'name': file.name, 'size': file.stat().st_size} in files.values()):
                original_path = list(files.keys())[list(files.values()).index({'name': file.name, 'size': file.stat().st_size})]
                print(f"duplicate found: {original_path} --> {file.path}")
                duplicates.append((original_path, file.path))
            elif file.is_file() and (jpg.search(file.name) or dng.search(file.name) or arw.search(file.name)):
                files[file.path] = {'name': file.name, 'size': file.stat().st_size}

    get_files(results)

    result_file = open('./duplicates.txt', 'w+')
    for original, duplicate in duplicates:
        result_file.write(f"{original}  -->  {duplicate}\n")
        # print(f"{original}  -->  {duplicate}")

    result_file.close()

if __name__ == "__main__":
    main(str(sys.argv[1]))
