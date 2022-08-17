from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import cv2
import pytesseract
from gingerit.gingerit import GingerIt
import language_tool_python
import pyttsx3


def cam():
    img_counter = 0
    cam = cv2.VideoCapture(0)

    while img_counter != 1:
        success, frame = cam.read()
        cv2.imshow("Image", frame)
        k = cv2.waitKey(1)

        if k % 256 == 32:
            img_name = 'img2.png'
            cv2.imwrite(img_name, frame)
            img_counter += 1


def click():
    cam()

    print("Working")

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)

    def speak(text):
        print("working")
        engine.say(text)
        engine.runAndWait()

    def ocr_core(img):
        text = pytesseract.image_to_string(img)
        return text

    img2 = cv2.imread("img2.png")
    img = cv2.resize(img2, (0, 0), fx=10, fy=10)

    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def remove_noise(image):
        return cv2.medianBlur(image, 5)

    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    img = get_grayscale(img)
    img = thresholding(img)
    img = remove_noise(img)
    print("working")

    text = str(ocr_core(img))

    print("Working")

    my_tool = language_tool_python.LanguageTool('en-US')
    correct_text = my_tool.correct(text)
    print(correct_text)
    print("working")
    speak(correct_text)

root = Tk()
root.title("Blind Dictator")
root.geometry("854x440")

logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoLabel = Button(root, image = logo, command = click )
logoLabel.pack()

root.mainloop()


