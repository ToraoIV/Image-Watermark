from PIL import Image, ImageDraw, ImageFont
import tkinter
from tkinter import filedialog

window = tkinter.Tk()
window.withdraw()
file_name = tkinter.filedialog.askopenfilename(initialdir="/Users/milat", title="Select image")


def add_watermark(image, text):
    selected_image = Image.open(image)
    width, height = selected_image.size
    draw = ImageDraw.Draw(selected_image)
    font_size = int(width/8)
    font1 = ImageFont.truetype("Arial.ttf", font_size)
    x, y = int(width/2), int(height/2)
    draw.text((x,y),text,font=font1, fill="#ffffff", stroke_width=10, stroke_fill="#000000", anchor="ms")
    selected_image.show()

add_watermark(file_name, "Your_Text")
