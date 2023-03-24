from PIL import Image
import os

# directory where the images are located
dir_path = 'Images\Text Images 4 Map'

# loop through all files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # open the image
        img_path = os.path.join(dir_path, filename)
        img = Image.open(img_path)
        
        # get the bounding box
        bbox = img.getbbox()
        
        # crop the image to the size of the bbox
        cropped_img = img.crop(bbox)
        
        # save the cropped image
        cropped_img.save(os.path.join(dir_path, filename))