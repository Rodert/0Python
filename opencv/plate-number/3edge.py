# 边缘检测 cv2.Canny（image，threshold1，threshold2）

import cv2
 
if __name__ == '__main__':
    img = cv2.imread('2.jpeg')
    # 调整图片大小
    img = cv2.resize(img, (620, 480))
    # 灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 双边滤波
    gray = cv2.bilateralFilter(gray, 13, 15, 15)
    # 边缘检测
    edged = cv2.Canny(gray, 30, 200)
 
 
 
 
    # 显示效果
    cv2.imshow('gray', gray)
    cv2.imshow('edged', edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()