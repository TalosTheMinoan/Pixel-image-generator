import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk
import time

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Generator")

        # Entry for user input
        self.pixel_entry = tk.Entry(root)
        self.pixel_entry.pack(pady=10)
        self.pixel_entry.insert(0, "200")

        # Button to select an image
        select_image_button = tk.Button(root, text="Select Image", command=self.load_image)
        select_image_button.pack(pady=10)

        # Button to generate and display the image
        generate_button = tk.Button(root, text="Generate Image", command=self.generate_and_display_image)
        generate_button.pack(pady=10)

        # Canvas to display the image
        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        # Variables for image and pixel display
        self.image = None
        self.pixels_to_show = None
        self.current_pixel_index = 0

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = Image.open(file_path).convert("RGB")
            self.pixels_to_show = self.image.getdata()

    def generate_and_display_image(self):
        num_pixels_to_show = int(self.pixel_entry.get())

        if self.image is not None:
            # Generate and display pixels gradually
            self.current_pixel_index = 0
            self.display_pixels_slowly(num_pixels_to_show)

    def display_pixels_slowly(self, num_pixels_to_show):
        if self.current_pixel_index < len(self.pixels_to_show):
            # Get the next pixel
            current_pixel = self.pixels_to_show[self.current_pixel_index]
            self.current_pixel_index += 1

            # Update the canvas with the new pixel
            x, y = self.current_pixel_index % self.image.width, self.current_pixel_index // self.image.width
            self.canvas.create_rectangle(x, y, x + 1, y + 1, fill="#%02x%02x%02x" % current_pixel)

            # Call the method again after a delay
            self.root.after(1, lambda: self.display_pixels_slowly(num_pixels_to_show))
        else:
            print("Pixel display completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()
