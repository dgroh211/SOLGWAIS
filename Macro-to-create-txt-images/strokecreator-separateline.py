from PIL import Image, ImageDraw, ImageFont

# Set image size
image_width = 600
image_height = 300

# Set text to be written
text_line1 = "Solgwai"
text_line2 = "Village"

# Set font size and font style
font_path = "Macro-to-create-txt-images/blackchancery/BLKCHCRY.TTF"
font_size = 50
font = ImageFont.truetype(font_path, font_size)

# Create a blank image
image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))

# Create a drawing context
draw = ImageDraw.Draw(image)

# Set stroke width and color
stroke_width = 1
stroke_color = (255, 255, 0, 255)

# Get text dimensions for each line
text_line1_width, text_line1_height = draw.textsize(text_line1, font)
text_line2_width, text_line2_height = draw.textsize(text_line2, font)

# Calculate text positions
x_line1 = (image_width - text_line1_width) // 2
y_line1 = (image_height - text_line1_height - text_line2_height) // 2
x_line2 = (image_width - text_line2_width) // 2
y_line2 = y_line1 + text_line1_height

# # Draw text with stroke for line 1
# draw.text((x_line1-stroke_width, y_line1-stroke_width), text_line1, font=font, fill=stroke_color)
# draw.text((x_line1+stroke_width, y_line1-stroke_width), text_line1, font=font, fill=stroke_color)
# draw.text((x_line1-stroke_width, y_line1+stroke_width), text_line1, font=font, fill=stroke_color)
# draw.text((x_line1+stroke_width, y_line1+stroke_width), text_line1, font=font, fill=stroke_color)

# # Draw text with stroke for line 2
# draw.text((x_line2-stroke_width, y_line2-stroke_width), text_line2, font=font, fill=stroke_color)
# draw.text((x_line2+stroke_width, y_line2-stroke_width), text_line2, font=font, fill=stroke_color)
# draw.text((x_line2-stroke_width, y_line2+stroke_width), text_line2, font=font, fill=stroke_color)
# draw.text((x_line2+stroke_width, y_line2+stroke_width), text_line2, font=font, fill=stroke_color)

# Draw text
draw.text((x_line1, y_line1), text_line1, font=font, fill=(0, 0, 0, 255))
draw.text((x_line2, y_line2), text_line2, font=font, fill=(0, 0, 0, 255))

# Save image
image.save("Images/Text Images 4 Map/villagename.png")
