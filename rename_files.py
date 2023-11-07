import os
import argparse

def rename_files_with_index(folder_path, base_name):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    files = os.listdir(folder_path)

    for index, file_name in enumerate(files):
        # Get the file extension (if any)
        file_name, file_extension = os.path.splitext(file_name)

        # Generate the new filename with the base name and index
        new_file_name = f"{base_name}_{index + 1}{file_extension}"

        # Construct the full paths for the old and new filenames
        old_file_path = os.path.join(folder_path, file_name + file_extension)
        new_file_path = os.path.join(folder_path, new_file_name)

        try:
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file_name}' to '{new_file_name}'")
        except Exception as e:
            print(f"Failed to rename '{file_name}': {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename files in a folder with an index.')
    parser.add_argument('folder_path', help='Path to the folder containing files to rename')
    parser.add_argument('base_name', help='Base name for the renamed files')

    args = parser.parse_args()

    rename_files_with_index(args.folder_path, args.base_name)
