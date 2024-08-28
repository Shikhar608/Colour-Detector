import cv2
import numpy as np
color_list = [[140, 50, 100, 179, 255, 255],
              [35,100,100,80,255,255]]  
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
        #cv2.imshow("mask", mask)
        get_contours(mask)
def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            color_name(imgResult, cnt)
def color_name(img, cnt):
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.putText(img, "Pink", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
while True:
    success, img = cap.read()
    imgResult = img.copy()
    find_color(img, color_list)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
