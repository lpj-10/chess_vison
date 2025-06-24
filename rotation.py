import cv2
import numpy as np

def rotate_img(img, angel):
    h, w = img.shape[:2]

    center = (w//2, h//2)
    scale = 1.0

    M = cv2.getRotationMatrix2D(center, angel, scale)

    return cv2.warpAffine(img, M, (w, h))

def rotate_point(img, point, angel):
    h, w = img.shape[:2]

    center = (w // 2, h // 2)
    scale = 1.0

    M = cv2.getRotationMatrix2D(center, angel, scale)

    point_np = np.array([point[0], point[1], 1])

    return np.dot(M, point_np)