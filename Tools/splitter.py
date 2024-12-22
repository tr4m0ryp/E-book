import os
from tkinter import Tk, filedialog
from PIL import Image

def split_image(image_path, output_folder, start_number):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if width < 2:
                print(f"Image {image_path} is too narrow to split.")
                return start_number

            left_box = (0, 0, width // 2, height)
            right_box = (width // 2, 0, width, height)

            left_image = img.crop(left_box)
            right_image = img.crop(right_box)

            left_image.save(os.path.join(output_folder, f"screenshot_{start_number}.png"))
            right_image.save(os.path.join(output_folder, f"screenshot_{start_number + 1}.png"))

            print(f"Split images saved: screenshot_{start_number}.png and screenshot_{start_number + 1}.png")

            return start_number + 2
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return start_number

def main():
    Tk().withdraw()
    input_folder = filedialog.askdirectory(title="Select a folder with images")

    if not input_folder:
        print("No folder selected. Exiting script.")
        return

    output_folder = os.path.join(input_folder, "split")
    os.makedirs(output_folder, exist_ok=True)

    image_files = sorted(
        [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))],
        key=lambda x: os.path.getmtime(os.path.join(input_folder, x))
    )

    if not image_files:
        print("No images found in the selected folder.")
        return

    counter = 2
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        counter = split_image(image_path, output_folder, counter)

    print(f"All images processed. Split files are in: {output_folder}")

if __name__ == "__main__":
    main()
