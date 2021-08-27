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

    # 이미지 대칭

    dst2 = cv2.flip(img_result, 0) # x축 대칭
    dst3 = cv2.flip(img_result,-1) # xy축 대칭
    dst4 = cv2.flip(img_result,1) # y축 대칭

    cv2.imshow("src", img_result)
    cv2.imshow("dst2", dst2)
    cv2.imshow("dst3", dst3)
    cv2.imshow("dst4", dst4)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()