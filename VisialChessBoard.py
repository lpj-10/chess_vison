import cv2
import square


class VisialChessBoard:

    def __init__(self, empty):
        img = cv2.imread("empty.jpg")
        self.points = square.getPoints(img)

    def getSqure(self, x, y):
        square.getSqure(self.points, x, y)