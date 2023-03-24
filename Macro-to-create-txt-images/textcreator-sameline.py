from PIL import Image, ImageDraw, ImageFont

# set the font file and size
font_path = "Macro-to-create-txt-images/FFF-Tusj/FFF_Tusj.ttf"
font_size = 60
font = ImageFont.truetype(font_path, font_size)

# Create new image
width, height = 650, 200
image = Image.new('RGBA', (width, height), (0, 0, 0, 0))

# Add text to image using custom font
draw = ImageDraw.Draw(image)
text = 'Silver Sands Beach'
x, y = 50, 50
draw.text((x, y), text, fill=(0, 0, 0), font=font)

image.save("Images/silversands.png")