from PIL import Image, ImageDraw, ImageFont

# Set image size
image_width = 600
image_height = 300

# Set text to be written
text = "Crystal Cliffs"

# Set font size and font style
font_path = "Macro-to-create-txt-images/FFF-Tusj/FFF_Tusj.ttf"
font_size = 50
font = ImageFont.truetype(font_path, font_size)

# Create a blank image
image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))

# Create a drawing context
draw = ImageDraw.Draw(image)

# Set stroke width and color
stroke_width = 1
stroke_color = (0, 0, 0)

# Get text dimensions
text_width, text_height = draw.textsize(text, font)

# Calculate text position
x = (image_width - text_width) // 2
y = (image_height - text_height) // 2

# Draw text with stroke
draw.text((x-stroke_width, y-stroke_width), text, font=font, fill=stroke_color)
draw.text((x+stroke_width, y-stroke_width), text, font=font, fill=stroke_color)
draw.text((x-stroke_width, y+stroke_width), text, font=font, fill=stroke_color)
draw.text((x+stroke_width, y+stroke_width), text, font=font, fill=stroke_color)

# Draw text
draw.text((x, y), text, font=font, fill=(0, 0, 0, 255))

# Save image
image.save("Images\Text Images 4 Map\crystalcliffs.png")
