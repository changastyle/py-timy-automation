import pyautogui
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\e107580\AppData\Local\Programs\Tesseract-OCR2\pytesseract.exe'

img = cv2.imread("img3.png")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

data = pytesseract.image_to_data(img)

# print("RES:" + str(find_coordinates_text("Oficina")))