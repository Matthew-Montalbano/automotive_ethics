import cv2
import numpy as np

# Converts image to black and white
def thresholding(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([80, 0, 0])
    upperWhite = np.array([255, 160, 255])
    maskWhite = cv2.inRange(imgHsv, lowerWhite, upperWhite)
    return maskWhite


def warpImg(img, points, w, h):
    pts1 = np.float32(points)
    #Anchors the rectangular points
    pts2 = np.float32([[0, 0], [w, 0],[0, h], [w, h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    # matrix converts images, warps.
    imgWarp = cv2.warpPerspective(img, matrix, (w, h))
    return imgWarp


def nothing(a):
    pass

#Instantiate the values of the Trackbars, returning a float 32 array of the anchor points of the warping
def valTrackbars(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT - widthTop, heightTop), (widthBottom, heightBottom),
                         (wT - widthBottom, heightBottom)])
    return points


def initializeTrackbars(initialTrackbarVals, wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", initialTrackbarVals[0], wT // 2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", initialTrackbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", initialTrackbarVals[2], wT // 2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", initialTrackbarVals[3], hT, nothing)


#img: want to draw the points #points: the points we want to draw
# have to draw the points one by one, circle method.
def drawPoints(img, points):
    for x in range(4):
        #draw circles in four corners, size 15, color = RED, fill the thickness of the circle
        cv2.circle(img,(int (points[x][0]), int(points[x][1])), 15, (0,0,255), cv2.FILLED)
    return img
