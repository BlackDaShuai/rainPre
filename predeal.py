import cv2 as cv
import numpy as np

# 加载两张图片
# image = cv.imread('dataSet/0.PNG')
background = cv.imread('dataSet/background.PNG')
output_folder = 'overDataSet/'


# 检查图片是否成功加载
if background is None:
    print("Error: 图片加载失败，请检查路径是否正确！")
else:
    # 确保两幅图像大小相同
    for i in range(241):
        image_path = f'dataSet/{i}.PNG'
        image = cv.imread(image_path)

        if image.shape == background.shape:
            # 执行图像减法
            difference = cv.absdiff(image, background)

            # 将差异图像转换为灰度图像
            gray_difference = cv.cvtColor(difference, cv.COLOR_BGR2GRAY)

            # 使用阈值处理创建二值图像
            _, mask = cv.threshold(gray_difference, 30, 255, cv.THRESH_BINARY)

            # 创建一个与原图相同大小的白色背景（白色）
            white_background = np.ones_like(image) * 255
            # （黑色）
            black_background = np.zeros_like(image)

            # 使用掩码将背景部分替换为白色，保留前景部分
            result = np.where(mask[:, :, None] == 255, image, white_background)

            # 显示结果
            cv.imshow('Subtracted Image', result)

            output_path = f'{output_folder}/{i}.PNG'
            cv.imwrite(output_path, result)
        else:
            print("Error: 图像尺寸不匹配，无法执行减法操作！")