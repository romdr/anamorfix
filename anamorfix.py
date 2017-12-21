""" Command line utility to desqueeze anamorphic images from a given folder, and using stretch ratio. """

import os
import sys
try:
    from PIL import Image
except Exception:
    print 'Error: Pillow doesn\'t seem installed.\nInstall it with: pip install pillow'
    sys.exit(1)

def desqueeze_images_in_folder(img_path, stretch_ratio):
    """ Create a `resized` folder in specified path, and place dequeezed images in it. """

    dst_path = os.path.join(img_path, "resized")
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    for filename in os.listdir(img_path):
        file_path = os.path.join(img_path, filename)
        if not os.path.isfile(file_path):
            continue

        print 'Desqueezing %s at %.3fx' % (filename, stretch_ratio)
        img = Image.open(file_path)
        width, height = img.size
        new_img = img.resize((width, int(height * (1.0 / stretch_ratio))))
        new_img.save(os.path.join(dst_path, filename))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'usage: anamorfix.py "C:\\Path\\To\\Images" <stretch-ratio>'
        sys.exit(1)
    desqueeze_images_in_folder(img_path=sys.argv[1], stretch_ratio=float(sys.argv[2]))
