import os

def main():
    results = os.scandir('./images')
    files = []
    # print(results)

    def get_files(results):
        files = []
        for file in results:
            if file.is_dir():
                results = os.scandir(file.path)
                files += get_files(results)
            elif file.is_file():
                files.append({'name': file.name, 'size': file.stat().st_size})

        return files

    files += get_files(results)

    print(files)

    # print(os.stat(f"./images/{file1}").st_size)

if __name__ == "__main__":
    main()
