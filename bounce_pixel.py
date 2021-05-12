import cv2
import numpy as np

maxX = 300
maxY = 400
drawing = np.zeros((maxX, maxY, 3), np.uint8)  # image to draw the distance

cnt = 0
posX = 20
posY = 40
stepX = 1
stepY = 3
while True:
    drawing[posX, posY] = [0, 0, 0]  # (B, G, R)
    cv2.imshow('bounce_pixel', drawing)

    if posX+stepX >= maxX or posX+stepX < 0:
        stepX *= -1
    posX += stepX

    if posY+stepY >= maxY or posY+stepY < 0:
        stepY *= -1
    posY += stepY

    # print(f'drawing[{posX}, {posY}], stepX={stepX}, stepY={stepY}')
    drawing[posX, posY] = [0, 255, 0]  # (B, G, R)
    cv2.imshow('bounce_pixel', drawing)

    # Cancellation strategies:
    cnt += 1
    key = cv2.waitKey(1)  # ms
    if key == 27:
        cv2.destroyAllWindows()
        exit(0)
    elif key == ord('s'):
        cv2.imwrite(f'bounce_pixel_{cnt}.jpg', drawing)  # saves image to file
