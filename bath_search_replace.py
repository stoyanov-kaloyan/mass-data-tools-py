import os
import argparse
import fileinput
import shutil

def batch_search_replace(folder_path, file_extension, search_string, replace_string):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    backup_folder = os.path.join(folder_path, "backup")
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                backup_path = os.path.join(backup_folder, file)
                shutil.copy(file_path, backup_path)
                with fileinput.FileInput(file_path, inplace=True) as file:
                    for line in file:
                        print(line.replace(search_string, replace_string), end='')

                print(f"Replaced text in '{file}'")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Batch search and replace in text files.')
    parser.add_argument('folder_path', help='Path to the folder containing text files')
    parser.add_argument('file_extension', help='File extension to target (e.g., .txt)')
    parser.add_argument('search_string', help='Text to search for')
    parser.add_argument('replace_string', help='Text to replace found text')

    args = parser.parse_args()

    batch_search_replace(args.folder_path, args.file_extension, args.search_string, args.replace_string)

    # python batch_search_replace.py /path/to/folder file_extension search_string replace_string
