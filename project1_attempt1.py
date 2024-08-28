import cv2
import numpy as np

# Define the color range for neon pink
color_list = [[140, 50, 100, 179, 255, 255]]  # Adjusted range for neon pink

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 80)

def empty(a):
    pass

def find_color(img, color_list):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in color_list:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow("mask", mask)

while True:
    success, img = cap.read()
    find_color(img, color_list)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
