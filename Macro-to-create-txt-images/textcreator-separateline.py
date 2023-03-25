from PIL import Image, ImageDraw, ImageFont

def draw_text(text, font_path, font_size, canvas_size):
    # create blank image
    img = Image.new('RGBA', canvas_size, (0, 0, 0, 0))

    # create draw object and set font
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    # split the text into two lines
    words = text.split(' ')
    first_line = words[0]
    second_line = ' '.join(words[1:])

    # get size of first line
    w, h = draw.textsize(first_line, font=font)

    # calculate x,y coordinates of first line to be centered horizontally and vertically
    x = (canvas_size[0] - w) / 2
    y = (canvas_size[1] - h) / 2 - h/2

    # draw first line
    draw.text((x, y), first_line, font=font, fill=(255, 255, 255, 255))

    # get size of second line
    w, h = draw.textsize(second_line, font=font)

    # calculate x,y coordinates of second line to be centered horizontally and below the first line
    x = (canvas_size[0] - w) / 2
    y += h  # move y-coordinate down to center second line below the first line

    # draw second line
    draw.text((x, y), second_line, font=font, fill=(255, 255, 255, 255))

    return img

# example usage
font_path = "Macro-to-create-txt-images/FFF-Tusj/FFF_Tusj.ttf"
text = ""
font_size = 48
canvas_size = (600, 300)
img = draw_text(text, font_path, font_size, canvas_size)
# Save image
img.save('Images/Text Images 4 Map/.png')
