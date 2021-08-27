import cv2
import numpy as np

def main():
    # 이미지 원본

    img_src = "C:/Users/wsChoe/customDataset/labelImg/data/original_img/1.jpg"
    img_source = cv2.imread(img_src)

    # 이미지 축소

    img = cv2.resize(img_source, None, fx=0.15, fy=0.15, interpolation = cv2.INTER_AREA)

    rows,cols = img.shape[0:2]  # 영상의 크기

    dx, dy = 100, 50            # 이동할 픽셀 거리

    # ---① 변환 행렬 생성 
    mtrx = np.float32([[1, 0, dx],
                    [0, 1, dy]])  
    # ---② 단순 이동
    dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))   

    # ---③ 탈락된 외곽 픽셀을 파랑색으로 보정
    dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, \
                            cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255,0,0) )

    # ---④ 탈락된 외곽 픽셀을 원본을 반사 시켜서 보정
    dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, \
                                    cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

    cv2.imshow('original', img)
    cv2.imshow('trans',dst)
    cv2.imshow('BORDER_CONSTATNT', dst2)
    cv2.imshow('BORDER_FEFLECT', dst3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()