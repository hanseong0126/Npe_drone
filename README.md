2021 자율주행 드론 대회
======================
 
**차례** 
- 대회진행전략
- 알고리즘 설명
- 소스코드 설명 


**대회진행 전략**  
-----------------
 본 대회는 영상처리를 활용하여 드론을 제어하는 대회로, 영상처리의 속도/정확성 , 드론제어 수준 등이 중요하다.     
NPE팀은 영상처리의 정확성에 초점을 맞추어 알고리즘을 구축하였다.   

진행해야할 경기장의 경우 사전에 공지되었기 때문에 공지된 규격에 맞추어 빠르게 드론을 이동시킬수 있도록 할 것이다.  

>영상처리의 경우 **RGB to HSV**로 활용하여 색인지를 진행한다.  
그 이유는 RGB는 R,G,B 세가지의 속성을 모두 고려하여 색을 표현하지만,    
HSV의 경우 **H(Hue)** 가 일정한 범위를 가지는 색 정보를 가지고있기에 RGB보다 쉽게 색을 분류 할 수 있다. 

**알고리즘 설명**
-----------------
1. 링의 중점찾기     
  	1. 파란색 사각형의 중점찾기  
  	2. 원의 중점 찾기
  	3. 화면상에 원이 제대로 보이지 않을 때
  	4. 드론 화면상의 중점과 비교   
  		1. 원의 중점좌표에 따른 드론제어 
  
2. 이동을 한 후 상황판단  
  	1. 표식이 안보일 경우 
		1. 표식이 보일때 까지 천천히 직진
		2. 표식이 일정크기보다 크게 보일 시 
  	2. 보라색을 판단  
     
```
정확한 드론제어를 위해 링의 중점을 확인 하는 과정 2번을 거친다.   
첫번째는 파란색 사각형의 중점을 찾고, 두번째로 원의 중점을 찾는다.
```

**소스코드 설명**
-----------------

*RGB to HSV (RED)*  
1. RGB이미지를 HSV로 변환한다. 
2. th_low/high를 임계값으로 설정하고   
 open cv의 inRange함수를 통해 Red만이 검출된 이미지를 얻는다. 
```python
def red_hsv(image):  
	image_hsv = cvtColor(image, COLOR_BGR2HSV)  
	th_low = (160, 100, 70)  
	th_high = (255, 255, 255)  
	img_th = inRange(image_hsv, th_low, th_high)  
	return img_th  

```
파란색 사각형의 중점 찾기 

```python

bi_blue = blue_hsv(image)
	value_th = np.where(bi_blue[:, :] == 255)   #검출된 파란색의 좌표들을 불러온다. 

	min_x1 = np.min(value_th[1])
	max_x1 = np.max(value_th[1])
	min_y1 = np.min(value_th[0])
	max_y1 = np.max(value_th[0])

	center_x1 = int((min_x1 + max_x1) / 2)
	center_y1 = int((min_y1 + max_y1) / 2)
```
사각형의 중점을 찾은 모습    
<img width="300" height="300" alt="33443" src="https://user-images.githubusercontent.com/54049385/125278881-37ea7a80-e34e-11eb-97d7-7fdd60633c5d.jpg">
<img width="300" height="300" alt="33443" src="https://user-images.githubusercontent.com/54049385/125278642-f1951b80-e34d-11eb-96d0-64c201d2cae5.PNG">


사각형의 중점을 찾았지만 더 정확히 계산하고자, 한번 더 연산을 진행한다. 
```python

center_min_x = 640
center_max_x = 0
center_min_y = 480
center_max_y = 0

#사각형의 중점에서 이동하면서 원의 경계에서 멈춘다.
for i in range(center_x1, max_x1):
if bi_blue[center_y1][i] == 255 and i > center_max_x:
    center_max_x = i
    break              
#원의 경계부분의 연산을 통해 더 정확한 중점을 찾는다. 
center_x2 = int((center_min_x + center_max_x) / 2)
center_y2 = int((center_min_y + center_max_y) / 2)
```
원의 중점에서 나아가 경계에서 선이 멈춘것을 확인 할 수 있다.  
<img width="300" height="300" alt="123123" src="https://user-images.githubusercontent.com/54049385/125280065-9bc17300-e34f-11eb-8a85-52ebd1c74d77.PNG">




 
