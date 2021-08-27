import cv2
import numpy as np

# 이미지 원본

img_src = "C:/Users/wsChoe/customDataset/labelImg/data/original_img/1.jpg"
img_source = cv2.imread(img_src)

# 이미지 크기 확인
# height width channel = imgae.shape
print(img_source.shape)

# 절대 크기 스케일링
dst = cv2.resize(img_source, dsize=(640, 480), interpolation=cv2.INTER_AREA)
cv2.imshow("absolute scaling", dst)
cv2.waitKey(0)

# 이미지 축소(배율)

# img_result = cv2.resize(img_source, None, fx=0.2, fy=0.2, interpolation = cv2.INTER_AREA)
# print(img_result.shape)
# cv2.imshow("x0.5 INTER_AREA", img_result)
# cv2.waitKey(0)

# 이미지 확대

# img_result = cv2.resize(img_source, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
# cv2.imshow("x2", img_result)
# cv2.waitKey(0)