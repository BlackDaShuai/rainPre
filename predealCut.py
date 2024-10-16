import shutil
import cv2 as cv
import numpy as np
from datetime import datetime, timedelta
import os
from sympy.physics.units import years

# 加载两张图片
pth_in = 'dataSetTest/'
pth_out = 'overDataSetTest/'

timeStart = datetime(year=2023, month=1, day=6, hour=8, minute=30)

if os.path.exists(pth_out):
    shutil.rmtree(pth_out)
# 不存在，创建文件夹
if not os.path.exists(pth_out):
    os.mkdir(pth_out)

# 检查图片是否成功加载
for i in range(288):
    image_path = pth_in + timeStart.strftime('%Y%m%d_%H%M%S') + '.PNG'
    print(image_path)
    image = cv.imread(image_path)
    if image is not None and image.shape == (630, 920, 3):
        height, width, _ = image.shape
        start_x = (width - 192) // 2
        start_y = (height - 192) // 2
        end_x = start_x + 192
        end_y = start_y + 192

        # 裁剪图片
        cropped_image = image[start_y:end_y, start_x:end_x]
        output_path = f'{pth_out}/{i}.PNG'
        cv.imwrite(output_path, cropped_image)
    else:
        print("Error: 图像尺寸不匹配，无法执行减法操作！")
    timeStart += timedelta(minutes=10)