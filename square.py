import cv2
from rotation import *

def getPoints(img):
    #rotate clockwise a little bit. The findChessboardCorners() will always find the correct starting point
    img = rotate_img(img, -10)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (7, 7), None)

    if not ret:
        raise ValueError("The input image must be a empty chess board. No such thing is detected.")

    ls = [tuple(pt[0]) for pt in corners]

    points = [[None for _ in range(9)] for _ in range(9)]

    n = 48
    for i in range(1, 8):
        for j in range(7, 0, -1):
            #rotate back
            points[i][j] = rotate_point(img, ls[n], 10);
            n = n-1

    points[0][0] = (2 * points[1][1][0] - points[2][2][0], 2 * points[1][1][1] - points[2][2][1])
    points[0][8] = (2 * points[1][7][0] - points[2][6][0], 2 * points[1][7][1] - points[2][6][1])
    points[8][0] = (2 * points[7][1][0] - points[6][2][0], 2 * points[7][1][1] - points[6][2][1])
    points[8][8] = (2 * points[7][7][0] - points[6][6][0], 2 * points[7][7][1] - points[6][6][1])

    for i in range(1, 8):
        points[0][i] = (2 * points[1][i][0] - points[2][i][0], 2 * points[1][i][1] - points[2][i][1])
        points[i][0] = (2 * points[i][1][0] - points[i][2][0], 2 * points[i][1][1] - points[i][2][1])
        points[i][8] = (2 * points[i][7][0] - points[i][6][0], 2 * points[i][7][1] - points[i][6][1])
        points[8][i] = (2 * points[7][i][0] - points[6][i][0], 2 * points[7][i][1] - points[6][i][1])

    return points

def getSqure(points, x, y):
    for i in range(0, 8):
        for j in range(0, 8):
            if points[i][j][0] < x < points[i][j+1][0] and points[i][j][1] < y < points[i+1][j][1]:
                return i, j

img = cv2.imread(r"test/empty.jpg")
points = getPoints(img)

for i in range(0, 9):
    for j in range(0, 9):
        cv2.circle(img, (int(points[i][j][0]), int(points[i][j][1])), radius=5, color=(0, 0, 255), thickness=-1)
        cv2.putText(img, f"{i}, {j}", (int(points[i][j][0]), int(points[i][j][1])+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

# cv2.drawChessboardCorners(img, (7, 7), corners, True)

cv2.imwrite("test/output.jpg", img)

print(f"\n{points}")
