import cv2
from rotation import *

def getPoints(img):
    """
        识别图像，获取棋盘的格点。
        :param img: 输入的图像。是已经用openCV的cv2.imread()读取好的图像，不是路径。从上到下正着拍，误差<10度。
        :return:以二位数组表示的，格点的位置。
        """

    # 因为cv2.findChessboardCorners()是从左上角开始搜索第一个格点的，因此将图片顺时针旋转10度，保证（如果棋盘是从上到下正着拍，误差<10度）棋盘的左上角一定是第一个被搜索到
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
            #将结果逆时针旋转10度，转回来。
            points[i][j] = rotate_point(img, ls[n], 10);
            n = n-1


    #从findChessboardCorners()识别出的7*7格点，推测出周围一圈的格点，得到9*9的完整格点。
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

def getSqureNum(points, x, y):
    """以数字形式返回某个点的坐标对应的格子坐标，以(0, 0)开始。"""
    for i in range(0, 8):
        for j in range(0, 8):
            if (points[i+1][j][0] < x < points[i][j+1][0]) and (points[i+1][j][1] < y < points[i][j+1][1]):
                return i, j

def getSqure(points, x, y):
    """以字母形式返回某个点的坐标对应的格子坐标，以a1开始。"""
    i, j = getSqureNum(points, x, y)
    return f"{chr(ord('a') + j)}{1 + i}"

# img = cv2.imread(r"test/empty.jpg")
# points = getPoints(img)
#
# for i in range(0, 9):
#     for j in range(0, 9):
#         cv2.circle(img, (int(points[i][j][0]), int(points[i][j][1])), radius=5, color=(0, 0, 255), thickness=-1)
#         cv2.putText(img, f"{i}, {j}", (int(points[i][j][0]), int(points[i][j][1])+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
#
# cv2.drawChessboardCorners(img, (7, 7), corners, True)
#
# cv2.imwrite("test/output.jpg", img)
#
# print(getSqure(points, 775, 710))
