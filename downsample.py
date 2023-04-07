import os
import argparse
import cv2

# Parse args
parser = argparse.ArgumentParser(description='Downsize images at 2x, 3x, and 4x\
    using bicubic interpolation.')
parser.add_argument("hr_img_dir", help="path to high resolution image dir")
parser.add_argument("lr_img_dir", help="path to desired output dir for\
    downsampled images")
parser.add_argument("-k", "--keepdims", help="keep original image dimensions in\
    downsampled images", action="store_true")
args = parser.parse_args()

hr_image_path = args.hr_img_dir
lr_image_dir = args.lr_img_dir

# Downsample HR images
# Read HR image
hr_img = cv2.imread(hr_image_path)
hr_img_dims = (hr_img.shape[1], hr_img.shape[0])

# Blur with Gaussian kernel of width sigma=1
hr_img = cv2.GaussianBlur(hr_img, (0, 0), 1, 1)

# Downsample image 4x
lr_img_4x = cv2.resize(hr_img, (0, 0), fx=0.25, fy=0.25,
                           interpolation=cv2.INTER_CUBIC)
if args.keepdims:
    lr_img_4x = cv2.resize(lr_img_4x, hr_img_dims,
                               interpolation=cv2.INTER_CUBIC)
        
words = hr_image_path.split("/")
filename = words[len(words)-1].split('.')[0] + "downsampled.jpg"
cv2.imwrite(os.path.join(lr_image_dir, filename), lr_img_4x)
