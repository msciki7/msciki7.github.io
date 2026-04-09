---
title: "Chap 0~1 "
excerpt: ""

wirter: sohee Kim
categories:
  - Digital Image Processing
tags:
  - 영상처리

toc: true
toc_sticky: true
math: true

date: 2026-03-13
last_modified_at: 2026-03-13
---

# 디지털 영상처리

&ensp;정의: 디지털 영상처리는 컴퓨터를 이용해 디지털 이미지를 처리하는 기술<br/>

&ensp;영상은 다음과 같이 표현된다.<br/>

$$f(x, y)$$

* x, y -> 이미지 위치(pixel 좌표)
* f(x, y) -> 밝기값(intensity)

&ensp;이미지는 픽셀(pixel)들의 집합이다.<br/>
* pixel = picture element
* 각 픽셀은 밝기값을 가진다.

# 디지털 영상의 특징

&ensp;디지털 영상은 다음 조건을 만족한다.<br/>
&ensp;1. 좌표가 이산적이다.<br/>
&ensp;(x, y)는 정수<br/>
&ensp;예<br/>

```
(0,0)
(0,1)
(0,2)
```

&ensp;2. 밝기값도 이산적이다.<br/>
&ensp;예<br/>
&ensp;8bit grayscale<br/>
```
0 ~ 255
```

&ensp;좌표 + 밝기값이 모두 discrete<br/>
&ensp;-> 이것이 digital image<br/>

# 수학이 필요한 이유

&ensp;영상처리는 **수학 기반 기술**이다.<br/>

&ensp;Fourier Transform<br/>
&ensp;영상 -> 주파수 영역 변환<br/>

$$H(w_1, w_2)$$

&ensp;사용 목적<br/>
* 필터링
* 압축
* 복원

&ensp;Convolution<br/>

$$f(x, y) \ast h(x, y)$$

&ensp;의미<br/>
* 필터 적용
* blur
* edge detection

&ensp;Entropy<br/>

$$H(S) = -\sum P(S_i)log_2P(S_i)$$

&ensp;의미<br/>
* 정보량
* 압축

&ensp;Mean Square Error<br/>
&ensp;영상 복원에서 사용<br/>

$$error = (f - f\hat{})^2$$

&ensp;정리<br/>
&ensp;영상처리 = 수학 + 알고리즘 + 프로그래밍(C/C++)<br/>

# DCT (영상 압축의 핵심)

&ensp;영상 압축에서 가장 중요한 변환<br/>

&ensp;DCT(Discrete Cosine Transform)<br/>

$$F(u, v) = \alpha (u)\alpha (v)\sum_{x=0}^{N-1}\sum_{y=0}^{N-1}f(x, y)cos(\frac{(2x+1)u\pi }{2N})cos(\frac{(2y+1)v\pi }{2N})$$

&ensp;사용하는 이유<br/>

&ensp;에너지를 저주파에 집중<br/>
&ensp;`고주파 제거 -> 데이터 감소` <br/>

&ensp;결과: 영상 압축 가능<br/>

&ensp;사용되는 곳<br/>
* JPEG
* MPEG
* H.264
* H.265
* 영상 압축

# 영상처리의 응용분야

&ensp;1. 영상 압축<br/>

* 스마트폰
* IPTV
* Netfilx
* Youtube

&ensp;코덱<br/>
```
H.264
H.265
AV1
```

&ensp;2. 사진 처리<br/>

* 디지털 카메라
* Photoshop
* 영상 보정

&ensp;3. 의료 영상<br/>
* X-ray
* CT
* MRI
* PET

&ensp;4. 우주/원격탐사<br/>
* 위성 영상
* 천문학 영상

&ensp;5. 군사/보안<br/>
* 미사일 유도
* 위성 영상 분석
* 얼굴 인식

&ensp;6. AI/컴퓨터 비전<br/>
* 자율주행
* 객체인식
* CNN

# Image Processing vs Computer Vision

&ensp;Low Level<br/>
&ensp;Image -> Image<br/>
&ensp;예<br/>
* noise 제거
* blur 제거
* contrast 향상

&ensp;->Image Processing<br/>

&ensp;High Level<br/>
&ensp;Image -> 의미<br/>
&ensp;예<br/>
* 사람 인식
* 자동차 인식

&ensp;->Computer Vistion/AI<br/>

# 영상처리의 기본 단계

&ensp;영상처리 과정<br/>
```css
Image Acquisition
↓
Image Enhancement
↓
Image Restoration
↓
Segmentation
↓
Representation
↓
Recognition
```

&ensp;1. Image Acquisition<br/>
&ensp;영상 획득<br/>
&ensp;예<br/>
* 카메라
* 센서

&ensp;2. Image Enhancement<br/>
&ensp;영상 개선<br/>
&ensp;예<br/>
* 밝기 조정
* contrast 향상
* sharpening

&ensp;3. Image Restoration<br/>
&ensp;영상 복원<br/>
&ensp;예<br/>
* blur 제거
* noise 제거

&ensp;4. Segmentation<br/>
&ensp;영상 분할<br/>
&ensp;예<br/>
* 배경 / 물체 분리

&ensp;5. Representation<br/>
&ensp;물체 특징 추출<br/>
&ensp;예<br/>
* 크기
* 모양
* texture

&ensp;6. Recognition<br/>
&ensp;물체 인식<br/>
&ensp;예<br/>
* 얼굴 인식
* 자동차 인식

# 영상처리 시스템 구성

```css
Image Acquisition
↓
Storage
↓
Processing
↓
Communication
↓
Display
```

| 단계            | 의미      |
| ------------- | ------- |
| Acquisition   | 카메라 입력  |
| Storage       | 저장      |
| Processing    | 알고리즘 처리 |
| Communication | 전송      |
| Display       | 화면 출력   |

