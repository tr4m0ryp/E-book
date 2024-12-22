import os
from tkinter import Tk, filedialog
from PIL import Image

def images_to_pdf(input_folder, output_pdf):
    try:
        image_files = sorted(
            [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))],
            key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else x
        )

        if not image_files:
            print("No images found in the selected folder.")
            return

        images = []
        for idx, image_file in enumerate(image_files):
            image_path = os.path.join(input_folder, image_file)
            with Image.open(image_path) as img:
                img = img.convert('RGB')
                if idx == 0:
                    first_image = img
                else:
                    images.append(img)

        first_image.save(output_pdf, save_all=True, append_images=images)
        print(f"PDF successfully created: {output_pdf}")

    except Exception as e:
        print(f"Error creating the PDF: {e}")

def main():
    Tk().withdraw()
    input_folder = filedialog.askdirectory(title="Select a folder with images")

    if not input_folder:
        print("No folder selected. Exiting script.")
        return

    output_pdf = filedialog.asksaveasfilename(
        title="Save the PDF file as",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not output_pdf:
        print("No output file specified. Exiting script.")
        return

    images_to_pdf(input_folder, output_pdf)

if __name__ == "__main__":
    main()
