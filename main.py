import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    _, frame = camera.read()

    #cv.imshow("camera",frame)

    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow("Laplacian", laplacian)

    "the lower the more details the more noise ! "
    edges = cv.Canny(frame, 50, 50)
    cv.imshow("Canny", edges)




    if cv.waitKey(5) == ord("x"):
        break


camera.release()
cv.destroyAllWindows()