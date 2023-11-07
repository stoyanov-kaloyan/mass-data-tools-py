# Mass Data Tools

This repository contains Python scripts for mass data manipulations. These tools allow you to perform batch operations on files within a specified folder, such as renaming multiple files with an index or resizing a batch of images.

## 1. File Renamer with Index

### Description

The `rename_files.py` script renames all files in a specified folder with a given base name and appends an index to each filename. This is useful for quickly organizing and numbering a large number of files.

### Usage

```shell
python rename_files.py /path/to/folder new_name
```

- `/path/to/folder`: The path to the folder containing the files you want to rename.
- `new_name`: The new base name for the renamed files.

Example:
```shell
python rename_files.py /my_folder documents
```

This command will rename files in the specified folder to `documents_1`, `documents_2`, and so on.

## 2. Image Resizer

### Description

The `resize_images.py` script uses the Pillow (PIL) library to rescale all images in a folder to the desired width and height. It's helpful for resizing a batch of images to a consistent size.

### Usage

```shell
python resize_images.py /path/to/folder output_folder width height
```

- `/path/to/folder`: The path to the folder containing the images you want to resize.
- `output_folder`: The folder where the resized images will be saved.
- `width`: The new width in pixels for the resized images.
- `height`: The new height in pixels for the resized images.

Example:
```shell
python resize_images.py /image_folder /output_folder 800 600
```

This command will resize images in the specified folder to 800x600 pixels and save the resized images in the output folder.

## Contributing

Feel free to contribute to this repository by adding more mass data manipulation tools or improving existing scripts. Create a pull request to share your enhancements with the community.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
