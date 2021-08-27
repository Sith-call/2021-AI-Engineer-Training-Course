import cv2
import numpy as np

def main():

    # 이미지 원본

    img_src = "C:/Users/wsChoe/customDataset/labelImg/data/original_img/1.jpg"
    img_source = cv2.imread(img_src)

    # 이미지 축소

    img_result = cv2.resize(img_source, None, fx=0.15, fy=0.15, interpolation = cv2.INTER_AREA)
    cv2.imshow("x0.5 INTER_AREA", img_result)
    cv2.waitKey(0)

    # 이미지 회전

    height, width, channel = img_result.shape
    matrix = cv2.getRotationMatrix2D((width/2, height/2), 36, 1) # 36도 회전, 1배율
    dst = cv2.warpAffine(img_result, matrix, (width, height)) # 객체형성

    cv2.imwrite("C:/Users/wsChoe/customDataset/temp_img/rotate.jpg",dst)

    cv2.imshow("src", img_result)
    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()