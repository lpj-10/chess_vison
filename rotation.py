import cv2
import numpy as np

def rotate_img(img, angel):
    """将图片旋转指定角度，正数表示逆时针，负数表示顺时针。"""
    h, w = img.shape[:2]

    center = (w//2, h//2)
    scale = 1.0

    M = cv2.getRotationMatrix2D(center, angel, scale)

    return cv2.warpAffine(img, M, (w, h))

def rotate_point(img, point, angel):
    """将特定的图片里的某个特定的点的坐标旋转指定角度，正数表示逆时针，负数表示顺时针。"""
    h, w = img.shape[:2]

    center = (w // 2, h // 2)
    scale = 1.0

    M = cv2.getRotationMatrix2D(center, angel, scale)

    point_np = np.array([point[0], point[1], 1])

    return np.dot(M, point_np)