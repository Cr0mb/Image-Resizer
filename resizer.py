from PIL import Image
import os

def resize_image(image_path, output_path, size):
    try:
        with Image.open(image_path) as img:
            img = img.resize(size)
            img.save(output_path)
            print(f"Image saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    output_path = input("Enter the output path: ")
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))

    resize_image(image_path, output_path, (width, height))
