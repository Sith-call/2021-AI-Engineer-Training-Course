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

![cha](https://user-images.githubusercontent.com/57928967/131076694-0d0118f8-9e41-43b7-913d-08d9aca46905.png)

### Dection Image

![KakaoTalk_20210826_235308156](https://user-images.githubusercontent.com/57928967/131076509-914342f4-5d42-4e26-a232-4721793ace9d.png)
![제목 없음](https://user-images.githubusercontent.com/57928967/131076559-3594e545-fb8e-4af5-991c-6756ed8db5e0.png)
![제목 없음2](https://user-images.githubusercontent.com/57928967/131076582-4ba750db-eb38-4157-bd84-fa3e3c3e07b2.png)



