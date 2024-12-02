from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import glob
from PIL import Image, ImageOps, UnidentifiedImageError


# --------------- Select and individual file ---------------- #
class Converter():
    def __init__(self):
        self.watermark = Image.open("watermark.png")
        self.images =[]


    def open_file(self):
        Tk().withdraw()

        filename = askopenfilename()
        if filename != "":
            try:
                im = Image.open(filename)
                self.images.append(im)
            except UnidentifiedImageError:
                no_img_warning = messagebox.showerror(title="Invalid Image Selection", message=f"{filename}, is not a valid image.")
            except PermissionError:
                no_img_warning = messagebox.showerror(title="Invalid Image Selection", message=f"{filename}, is not a valid image.")
            self.output()
            if self.images != []:
                self.success_alert()
            self.images = []


    def open_watermark_file(self):
        Tk().withdraw()

        filename = askopenfilename()
        if filename != "":
            try:
                im = Image.open(filename)
                self.watermark = im
            except UnidentifiedImageError:
                no_img_warning = messagebox.showerror(title="Invalid Image Selection", message=f"{filename}, is not a valid image.")
            except PermissionError:
                no_img_warning = messagebox.showerror(title="Invalid Image Selection", message=f"{filename}, is not a valid image.")

    def convert_all(self):
        for n in glob.iglob("input/*"):
            try:
                im = Image.open(n)
                self.images.append(im)
            except UnidentifiedImageError:
                print(f"{n[6:]} is not a valid image. Skipping...")
                no_img_warning = messagebox.showwarning(title="Invalid Image Selection",
                                                        message=f"{n[6:]}, is not a valid image.\nSkipping file.")
            except PermissionError:
                print(f"{n[6:]} folder cannot be accessed. Skipping...")
                no_img_warning = messagebox.showwarning(title="Invalid Image Selection",
                                                        message=f"{n[6:]}, is not a valid image.\nSkipping file.")
        self.output()
        if self.images != []:
            self.success_alert()
        self.images = []



    def merge(self, size, im1, watermark):
        w = size[0]
        h = size[1]
        im = Image.new("RGBA", (w, h))

        im.paste(im1)
        im.paste(watermark, (0, int(h / 2)), watermark)
        return im


    def output(self):
        for image in self.images:
            size = image.size
            resized_watermark = ImageOps.contain(self.watermark, size)
            im = self.merge(size, image, resized_watermark)
            im.save(f"output/image {self.images.index(image) + 1}.png")

    def success_alert(self):
            success_alert = messagebox.showinfo(title="Watermarking Complete",
                                                message=f"Success! {len(self.images)} image(s) watermarked successfully.")

