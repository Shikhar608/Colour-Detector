import cv2
import numpy as np
color_list = [[140, 50, 100, 179, 255, 255],
              [35, 100, 100, 80, 255, 255],
              [100,100,100,140,255,255],
              [20,150,150,40,255,255],]  

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
        get_contours(mask, color)

def get_contours(img, color):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 255, 255), 2)
            color_name(imgResult, cnt, color)

def color_name(img, cnt, color):
    x, y, w, h = cv2.boundingRect(cnt)
    if color == [140, 50, 100, 179, 255, 255]:
        cv2.putText(img, "Pink", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (193, 203, 255), 2)
    elif color == [35, 100, 100, 80, 255, 255]:
        cv2.putText(img, "Green", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    elif color == [100,100,100,140,255,255]:
        cv2.putText(img, "Blue", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    elif color == [20,150,150,40,255,255]:
        cv2.putText(img, "Yellow", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    

while True:
    success, img = cap.read()
    imgResult = img.copy()
    find_color(img, color_list)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
