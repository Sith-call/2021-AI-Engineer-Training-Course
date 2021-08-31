# 2021-AI-Engineer-Training-Course

## Darknet & Yolov4

Darknet : Neural networks framework

Yolov4 : Object dection algorithm

Dataset : [Kaggle](https://www.kaggle.com/choemarco/mouse-book) (labeled using labelImg)

Weights : [Google Drive](https://drive.google.com/file/d/1Jy4jGshzCzajSByDK6k0YIDVVXi-z3lt/view?usp=sharing)

## Data Processing and aggregation by python

파이썬을 이용해서 각기 다른 데이터의 이름, 크기를 맞춰주었습니다.
 
opencv-python을 이용해서 데이터셋의 크기를 키웠습니다.

## Review

데이터셋을 사용하려는 목적에 맞게 형성해야 합니다.
즉, 물체를 인식해야하는 특정 각도가 주어진 상황이라면 그 각도에 특화된 데이터셋을 생성해야 합니다.
학습된 각도에선 이미지를 잘 인식하지만 학습하지 못한 각도에선 잘 인식해내지 못합니다.
또한 학습시키지 않은 물건인데도 인식을 하기도 합니다. 여기서 문제는 책을 교육시켰을 때,
다른 책도 인식해내지만 책과 비슷한 물건도 책으로 인식해버립니다. 이런 경우를 방지하기 위해서
데이터셋을 보강할 필요가 있습니다. 

데이터셋의 크기를 키우기 위해서 opencv를 이용해서 이미지에 회전 및 대칭의 효과를 줄 수도 있습니다.
그리고 이미지의 색도 바꾸어줄 수 있는데 이땐 색온도를 고려하여 이미지를 처리해야 합니다. 이미지에 필터 처리를 한다고 생각하면 됩니다.

### Chart

![chart (1)](https://user-images.githubusercontent.com/57928967/131431793-955a92bd-9a3d-418d-ba17-6c2a5d682dca.png)

### Dection Image

![KakaoTalk_20210826_235308156](https://user-images.githubusercontent.com/57928967/131431362-4f15d2fd-5bc7-46ee-8750-077fd5c01d86.png)
![KakaoTalk_20210826_234708969](https://user-images.githubusercontent.com/57928967/131431390-a71f979a-7023-41be-9098-5333860cbd8b.png)
![KakaoTalk_20210826_234651408](https://user-images.githubusercontent.com/57928967/131431419-d533c5f0-2a4d-4f2d-9347-44fb74f2dfb8.png)



