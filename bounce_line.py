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
stepX1 = 1
stepY1 = 3
stepX2 = 3
stepY2 = 1
while True:
    #drawing[posX, posY] = [0, 0, 0]  # (B, G, R)
    cv2.line(drawing, (posX1, posY1), (posX2, posY2), (0, 0, 0), 1)
    cv2.imshow('bounce_line', drawing)

    if posX1+stepX1 >= maxX or posX1+stepX1 < 0:
        stepX1 *= -1
    posX1 += stepX1
    if posX2+stepX2 >= maxX or posX2+stepX2 < 0:
        stepX2 *= -1
    posX2 += stepX2

    if posY1+stepY1 >= maxY or posY1+stepY1 < 0:
        stepY1 *= -1
    posY1 += stepY1
    if posY2+stepY2 >= maxY or posY2+stepY2 < 0:
        stepY2 *= -1
    posY2 += stepY2

    # print(f'drawing[{posX}, {posY}], stepX={stepX}, stepY={stepY}')
    # drawing[posX, posY] = [0, 255, 0]  # (B, G, R)
    cv2.line(drawing, (posX1, posY1), (posX2, posY2), (0, 255, 0), 1)
    cv2.imshow('bounce_line', drawing)

    # Cancellation strategies:
    cnt += 1
    key = cv2.waitKey(1)  # ms
    if key == 27:
        cv2.destroyAllWindows()
        exit(0)
    elif key == ord('s'):
        cv2.imwrite(f'bounce_line_{cnt}.jpg', drawing)  # saves image to file
