import argparse
from PIL import Image
import os

# Функция за преоразмеряване на изображение до желания размер
# Function to rescale an image to the desired size
def rescale_image(input_path, output_path, new_width, new_height):
    try:
        # Отваряне на изображението
        # Open the image
        img = Image.open(input_path)

        # Преоразмеряване на изображението до новия размер
        # Rescale the image to the new size
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # Запазване на преоразмереното изображение
        # Save the resized image
        img.save(output_path)

        print(f"Преоразмерено {input_path} до {new_width}x{new_height}")
        # Print a message to indicate successful resizing
    except Exception as e:
        print(f"Грешка: {e} - Неуспешно преоразмеряване на {input_path}")
        # Print an error message if resizing fails

# Функция за преоразмеряване на всички изображения в дадена папка
# Function to rescale all images in a folder
def rescale_images_in_folder(input_folder, output_folder, new_width, new_height):
    # Създаване на изходната папка, ако не съществува
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Изброяване на всички файлове във входната папка
    # List all files in the input folder
    files = os.listdir(input_folder)

    # Обхождане на файловете и преоразмеряване на изображенията
    # Iterate through the files and rescale images
    for file in files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)
        if os.path.isfile(input_path):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                rescale_image(input_path, output_path, new_width, new_height)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Преоразмеряване на изображения в папка.')
    # Command line arguments parser with a description in Bulgarian
    parser.add_argument('input_folder', help='Входна папка, съдържаща изображения')
    # Input folder argument with help message in Bulgarian
    parser.add_argument('output_folder', help='Изходна папка за преоразмерените изображения')
    # Output folder argument with help message in Bulgarian
    parser.add_argument('new_width', type=int, help='Нова ширина в пиксели')
    # New width argument with help message in Bulgarian
    parser.add_argument('new_height', type=int, help='Нова височина в пиксели')
    # New height argument with help message in Bulgarian

    args = parser.parse_args()

    rescale_images_in_folder(args.input_folder, args.output_folder, args.new_width, args.new_height)
