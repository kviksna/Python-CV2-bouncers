import cv2
import numpy as np

maxX = 300
maxY = 400
drawing = np.zeros((maxX, maxY, 3), np.uint8)  # image to draw the distance

cnt = 0
posX1 = 20
posY1 = 40
posX2 = 40
posY2 = 20
posX3 = 10
posY3 = 30
stepX1 = 1
stepY1 = 3
stepX2 = 3
stepY2 = 1
stepX3 = 2
stepY3 = 1
while True:
    #drawing[posX, posY] = [0, 0, 0]  # (B, G, R)
    cv2.line(drawing, (posX1, posY1), (posX2, posY2), (0, 0, 0), 1)
    cv2.line(drawing, (posX2, posY2), (posX3, posY3), (0, 0, 0), 1)
    cv2.line(drawing, (posX3, posY3), (posX1, posY1), (0, 0, 0), 1)
    cv2.imshow('bounce_triangle', drawing)

    if posX1+stepX1 >= maxX or posX1+stepX1 < 0:
        stepX1 *= -1
    posX1 += stepX1
    if posX2+stepX2 >= maxX or posX2+stepX2 < 0:
        stepX2 *= -1
    posX2 += stepX2
    if posX3+stepX3 >= maxX or posX3+stepX3 < 0:
        stepX3 *= -1
    posX3 += stepX3

    if posY1+stepY1 >= maxY or posY1+stepY1 < 0:
        stepY1 *= -1
    posY1 += stepY1
    if posY2+stepY2 >= maxY or posY2+stepY2 < 0:
        stepY2 *= -1
    posY2 += stepY2
    if posY3+stepY3 >= maxY or posY3+stepY3 < 0:
        stepY3 *= -1
    posY3 += stepY3

    # print(f'drawing[{posX}, {posY}], stepX={stepX}, stepY={stepY}')
    # drawing[posX, posY] = [0, 255, 0]  # (B, G, R)
    cv2.line(drawing, (posX1, posY1), (posX2, posY2), (0, 255, 0), 1)
    cv2.line(drawing, (posX2, posY2), (posX3, posY3), (0, 255, 0), 1)
    cv2.line(drawing, (posX3, posY3), (posX1, posY1), (0, 255, 0), 1)
    cv2.imshow('bounce_triangle', drawing)

    # Cancellation strategies:
    cnt += 1
    key = cv2.waitKey(1)  # ms
    if key == 27:
        cv2.destroyAllWindows()
        exit(0)
    elif key == ord('s'):
        cv2.imwrite(f'bounce_triangle_{cnt}.jpg', drawing)  # saves image to file
