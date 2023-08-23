from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import os

path = './Images'
pathOut = './editedImages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('RGB').rotate(180)

    draw = ImageDraw.Draw(edit)
    draw.line((10, 10, 150, 150), fill="red", width=5)
    
    font = ImageFont.truetype("arial.ttf", 55)
    draw.text((650,860), "Hello Me!", fill = "red", font = font)

    factor = 1.8
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    

    clean_name = os.path.splitext(filename)[0]

    edited_filename = f'{clean_name}_edited.jpg'
    edited_filepath = os.path.join(pathOut, edited_filename)
    edit.save(edited_filepath)

    print(f"Saved edited image: {edited_filepath}")

