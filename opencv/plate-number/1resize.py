# 调整大小，并获取灰度图 

import cv2
 
if __name__ == '__main__':
    img = cv2.imread('2.jpeg')
    # 调整图片大小
    img = cv2.resize(img, (620, 480))
    # 灰度图，将彩色图转化为单通道图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
 
    # 显示效果， original 按照原先的尺寸 
    cv2.imshow('original', img)

    # 退出，按任意键关闭窗口
    cv2.waitKey(0)
    # 窗口显示图像
    cv2.destroyAllWindows()

