import cv2
import pytesseract
from gingerit.gingerit import GingerIt
import language_tool_python
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text


img2 = cv2.imread("test.png")
img = cv2.resize(img2, (0,0), fx = 10, fy = 10)


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)


text = str(ocr_core(img))

my_tool = language_tool_python.LanguageTool('en-US')
correct_text = my_tool.correct(text)


speak(correct_text)
