import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import re

from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

def add_watermark():

    image_path = re.sub('"','',image_input.get())
    watermark = watermark_input.get()

    opened_image = PIL.Image.open(image_path)


    image_width, image_height = opened_image.size

    draw = PIL.ImageDraw.Draw(opened_image)

    font_size = int(image_width / 8)

    font = PIL.ImageFont.truetype('arial.ttf', font_size)

    x, y = int(image_width / 2), int(image_height / 2)

    draw.text((x, y), watermark, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    opened_image.show()

    if messagebox.askyesno("Wanna Save?","Do you wanna save image ?"):
        opened_image.save('C:\\Users\\Pc\\Desktop\\watermark.jpg')
        messagebox.showinfo("Saved","Image saved on desktop.")

window = Tk()
window.title("Add a watermark to image")
window.config(pady=20, padx=20)

image_input = Entry(width=70)
image_input.grid(column=1, row=0)

image_label = Label(text="Please provide file path here:")
image_label.grid(column=0, row=0)


watermark_text = Label(text="What text would you like to add as watermark?")
watermark_text.grid(column=0, row=1)

watermark_input = Entry(width=70)
watermark_input.grid(column=1, row=1)

add_watermark_button = Button(text="Add watermark", command=add_watermark)
add_watermark_button.grid(column=1, row=2)




window.mainloop()
print(image_input.get())

#add_watermark(filename, 'website.com')