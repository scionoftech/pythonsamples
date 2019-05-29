import numpy as np
from PIL import Image
import pytesseract
import cv2
from skimage.io import MultiImage

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def gettextFrom_image():
    img = cv2.imread('What-is-Lorem-Ipsum.tiff')
    img_str = pytesseract.image_to_string(Image.fromarray(img))
    print(img_str)


def gettextFrom_tiff_Image(file):
    qq = MultiImage(file, plugin='pil')
    for i, frame in enumerate(qq, start=1):
        pil_img = Image.fromarray(frame)
        img_str = pytesseract.image_to_string(pil_img)
        print(img_str)


if __name__ == '__main__':
    gettextFrom_image()
    gettextFrom_tiff_Image()
