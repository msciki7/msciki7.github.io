---
title: "Chap 3-0. The Digital Image"
excerpt: ""

wirter: sohee Kim
categories:
  - Digital Image Processing
tags:
  - 영상처리

toc: true
toc_sticky: true
math: true

date: 2026-03-22
last_modified_at: 2026-03-31
---

# Digital Image Review

&ensp;1) Continuous-tone image vs digital image<br/>
* Continous-tone image: 밝기가 끊기지 않고 연속적으로 변하는 영상
* Digital image: M x N개의 픽셀로 이루어진 영상

&ensp;디지털 영상은 화면 전체가 아주 작은 칸들로 나뉘어 있고 각 칸이 숫자로 하나를 갖는 구조<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-1.png" width="600"></p>

&ensp;2) Pixel<br/>
* picture element
* gray/color level
* 화면에서의 크기

&ensp;픽셀은 그냥 점이 아니라 위치 정보 + 밝기/색 정보를 함께 가진 디지털 영상의 최소 단위<br/>

&ensp;3) Image digitization<br/>
&ensp;영상의 디지털화는 두 단계로 이해하면 된다.<br/>

&ensp;(1) Sampling<br/>
&ensp;연속 공간을 몇 개의 점으로 나눌지 정하는 과정 -> M, N이 결정됨<br/>
* 가로로 몇 칸?
* 세로로 몇 칸?

&ensp;을 정하는 것<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-2.png" width="600"></p>

&ensp;(2) Quantizaton<br/>
&ensp;각 픽셀이 가질 수 있는 밝기값의 단계 수를 정하는 과정 -> number of levels가 결정됨<br/>
* 2비트면 4단계
* 8비트면 256단계
* 10비트면 1024단계

&ensp;4) 세 가지 해상도<br/>
* spatial resolution: 공간 해상도
* brightness(color) resolutuion: 밝기/색 해상도
* temporal resolution: 시간 해상도

&ensp;공간 해상도<br/>
&ensp;픽셀이 얼마나 촘촘한가 -> 세밀한 모양 표현 능력<br/>

&ensp;밝기 해상도<br/>
&ensp;밝기 단계가 얼마나 세분화되었는가 -> 부드러운 명암 표현 능력<br/>

&ensp;시간 해상도<br/>
&ensp;1초에 몇 장 보여주는가 -> 움직임이 얼마나 자연스러운가<br/>

&ensp;5) 좌표계<br/>
* x: 세로 방향, row, line
* y: 가로 방향, colume
* f(x, y): 해당 위치의 픽셀값

&ensp;영상은 단순 그림이 아니라 좌표 위에 정의된 2차원 함수로 볼 수 있다.<br/>

# Nyquist Sampling Theorem

&ensp;어떤 신호 x(t)가 최대 주파수 $f_{max}$ 까지만 에너지를 가진다면, 샘플링 주파수 $f_{s}$ 가 2f_{max}$ 보다 크면 원래 신호를 완전히 복원할 수 있다.<br/>

$$f_{s} > 2f_{max}$$

&ensp;이 조건을 Nyquist rate라고 한다.<br/>

&ensp;신호 안에 빠르게 변하는 성분이 많을수록 더 자주 측정해야 한다는 뜻<br/>
&ensp;예를 들어<br/>
* 천천히 변하는 파형은 듬성듬성 찍어도 됨
* 빠르게 진동하는 파형은 촘촘히 찍어야 함

&ensp;너무 띄엄띄엄 찍으면 원래 파형의 변화를 놓쳐버리기 때문<br/>

## 샘플링 단계

&ensp;Sampling step<br/>
1. LPF(low-pass filter)로 원 신호를 $f_{max}$ 안에 제한
2. 2f_{max}$ 보다 큰 속도로 샘플링

&ensp;즉 실제 시스템에서는 샘플링 전에 너무 높은 주파수 성분을 먼저 잘라내는 anti-aliasing filter가 필요하다.<br/>

&ensp;Reconstruction step<br/>
&ensp;이산 데이터로부터 다시 연속 신호를 만드는 과정<br/>

&ensp;hold circuit을 언급하지만 뒤 페이지에서 이상적인 복원은 sinc 보간으로 설명한다. 즉 샘플만 잘 찍으면 원래 신호를 다시 만들 수 있다.는 것이 핵심<br/>

&ensp;Over-sampling<br/>
&ensp;실제로는 이론 최소값보다 더 촘촘하게 샘플링하는 경우가 많다.<br/>

&ensp;그 이유는:<br/>
* 측정 오차 감소
* 특징 추출 정확도 향상
* 복원 품질 향상

&ensp;원래 신호의 가장 빠른 변화 속도의 최소 2배보다 더 빠르게 샘플링해야 원래 모습을 잃지 않는다.<br/>

## 1D Frequency-domain representation

&ensp;샘플링하면 주파수 영역에서 원래 스펙트럼이 반복 복제된다는 사실을 수학적으로 보이는 페이지<br/>

&ensp;시작식<br/>

$$x(t) = Acos(\Omega t)$$

&ensp;를 샘플링해서<br/>

$$x[n] = x(nT_s) = Acos(\Omega nT_s) = Acos(\hat{w}n)$$

&ensp;로 바꾼다.<br/>

&ensp;여기서<br/>
* $\Omega$ : 아날로그 각주파수
* $T_{s}$ : 샘플링 주기
* $\hat{w} = T_s \Omega$ : 디지털 각주파수

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-3.png" width="600"></p>

&ensp;이다.<br/>

&ensp;중요한 이유<br/>
&ensp;연속시간 신호가 이산시간 신호로 바뀌면 주파수도 그대로 남는 게 아니라 디지털 주파수 축으로 변환된다.<br/>
* 아날로그 세계의 주파수 표현
* 디지털 세계의  주파수 표현

&ensp;이 서로 대응된다는 걸 보여주는 단계<br/>

&ensp;큰 흐름<br/>
* CTFT(continuous-time Fourier transform)
* DTFT(discrete-time Fourier transform)

&ensp;사이 관계를 유도하는 과정이다.<br/>

&ensp;샘플링된 신호의 주파수 스펙트럼은 원래 아날로그 스펙트럼이 샘플링 주파수 간격으로 반복된 형태가 된다.<br/>

&ensp;반복 스펙트럼의 의미<br/>

$$X(e^{j\hat{w}}) = \frac{1}{T_s}\sum_{\infty }^{r = -\infty }X_a(j(\Omega + \frac{2\pi r}{T_{s})})$$

&ensp;이 식의 의미는 다음과 같다<br/>

&ensp;핵심 의미<br/>
&ensp;디지털 주파수 스펙트럼 $X(e^{j\hat{w}})$ 는 아날로그 스펙트럼 $X_a(j\Omega)$ 가 $\frac{2\pi}{T_s}$ 간격으로 계속 복제되어 더해진 형태라는 뜻이다.<br/>

&ensp;중요한 이유<br/>
&ensp;복제된 스펙트럼들이 서로 안 겹치면 원래 신호를 복원할 수 있다.<br/>
&ensp;반대로 겹치면 aliasing이 발생한다.<br/>

&ensp;이 식은 사실상 Nyquist 조건을 안 지키면 왜 문제가 생기는가? 를 설명하는 수학적 근거다.<br/>

&ensp;샘플링 후 주파수 영역에서는 원 신호 스펙트럼이 반복 복사된다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-4.png" width="600"></p>

&ensp;왼쪽의 원래 아날로그 스펙트럼 $X_a(j\Omega )$ 가 샘플링 후 오른쪽에서 주기적으로 반복된다. 그 반복 간격은 $\frac{2\pi }{T_s}$ 이다.<br/>

&ensp;Nyquist 조건의 그림 해석<br/>

$$\frac{\pi}{T_s} > \Omega _{N} -> f_s > 2f_{max}$$

&ensp;반복된 스펙트럼이 겹치지 않으려면 원래 신호의 최대 주파수가 $\frac{\pi}{T_s}$ 보다 작아야 하고 결국 샘플링 주파수는 샘플링 주파수는 $2f_{max}$ 보다 커야 한다는 것이다.<br/>

* 샘플링이 충분히 빠름 -> 복제 스펙트럼 안 겹침
* 샘플링 부족함 -> 복제 스펙트럼 겹침
* 겹치면 원래 성분을 분리할 수 없음 -> aliasing

&ensp;영상은 1차원 신호가 아니라 2차원 신호이다.<br/>
&ensp;따라서 샘플링도<br/>
* x 방향 샘플링
* y방향 샘플링

&ensp;을 각각 생각해야 한다.<br/>
&ensp;즉 Nyquist 조건도 두 방향에 대해 각각 만족해야 한다.<br/>

&ensp;$f_{s, x} > 2f_{max. x}, f_{x, y} > 2f_{max, y}$ <br/>

&ensp;2D에서 복잡해지는 이유<br/>
&ensp;이미지에는<br/>
* 가로 방향으로 빨리 변하는 무늬
* 세로 방향으로 빨리 변하는 무늬
* 대각선 방향 패턴

&ensp;등이 모두 존재한다.<br/>

&ensp;그래서 주파수 공간도 2차원이 복제 스펙트럼도 평면에서 반복된다.<br/>

## what is aliasing phenomenon?

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-5.png" width="600"></p>

&ensp;예시 이미지<br/>
&ensp;320×240 영상이 있고, 해상도를 계속 낮출수록<br/>
* 160×120
* 80×60
* 40×30
* 20×15

&ensp;처럼 점점 거칠어진다.<br/>
&ensp;그 결과 pixel-blocking effect가 나타난다.<br/>

&ensp;aliasing?<br/>
&ensp;원래 존재하던 고주파 성분을 충분히 샘플링하지 못해서 낮은 주파수이 다른 패턴처럼 잘못 보이는 현상이다.<br/>

&ensp;영상에서는 보통<br/>
* 계단 현상
* 깨짐
* 줄무늬 왜곡
* 블록화

&ensp;같이 나타난다.<br/>

&ensp;왜 해상도가 낮아지면 이런 일이 생기는 이유<br/>
&ensp;야자수 잎처럼 세밀한 구조는 높은 공간 주파수를 가진다. 그런데 픽셀 수를 줄이면 그 세밀한 구조를 표현할 수 없어서<br/>
* 뭉개지거나
* 이상한 무늬처럼 보이거나
* 큰 블록처럼 보이게 된다.

# Reconstruction of $x_{a}(t)$ from x[n]

$$ x(t) = \sum_{k = -\infty }^{\infty }x_a{kT_s}\frac{sin(\frac{\pi }{T_s})((t-kT_s))}{\frac{\pi }{T_s}(t-kT_s)}$$

&ensp;이 식이 바로 sinc interpolation이다.<br/>

&ensp;식의 의미<br/>
&ensp;각 샘플값 x_a(kT_s) 하나하나는 복원할 때 단순한 점이 아니라 하나의 sinc 함수로 퍼져서 전체 신호를 만드는 데 기여한다.<br/>
&ensp;즉 복원 신호는 모든 샘플에서 나온 sinc 함수들을 다 더한 결과이다.<br/>

&ensp;sinc?<br/>
&ensp;이상적인 저역통과 필터의 시간영역 응답이 sinc이기 때문이다.<br/>
&ensp;샘플링 후 복원은 결국<br/>
* 주파수 영역에서는 원래 대역만 남기고
* 시간 영역에서는 sinc 모양으로 보간하는 것

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-6.png" width="600"></p>

* 각 샘플 위치에서는 자기 sinc가 가장 크게 기여
* 다른 샘플 위치에서는 0이 되도록 설계
* 그래서 모든 샘플을 정확히 지나가면서 원래 곡선을 재구성

# interpolation과 실제 복원 방식

&ensp;복원 이론에서는 이상적인 sinc 보간이 가장 정확하지만 실제 시스템에서는 계산량과 구현의 편의 때문에 여러 보간 방법을 쓴다.<br/>

* Zero-order hold interpolation
* Linear interpolation
* Parabolic interpolation
* Ideal pulse (sinc)

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-7.png" width="600"></p>

&ensp;1. Zero-order hold<br/>
&ensp;이전 샘플값을 다음 샘플 전까지 그대로 유지하는 방식<br/>
&ensp;장점은 간단하지만 출력이 부드럽지 않고 계단 현상이 심하다.<br/>

&ensp;2. Linear interpolation<br/>
&ensp;인접한 두 점을 직선으로 잇는 방식이다. Zero-order hold보다 훨씬 자연스럽다.<br/>

&ensp;3. Parabolic interpolation<br/>
&ensp;직선보다 더 부드럽게 연결하려는 방식이다. 곡선 형태로 이어주므로 더 자연스러운 경욱 많다.<br/>

&ensp;4. Ideal interpolation<br/>
&ensp;가장 이상적인 방식은 sinc 보간이다. 이론적으로 원래 신호를 가장 잘 복원한다.<br/>

# 공간 주파수와 공간 해상도

&ensp;1. Spatial frequency?<br/>
&ensp;공간 주파수는 이미지 안에서 밝기나 색이 공간적으로 얼마나 빠르게 변하는가를 뜻한다.<br/>

&ensp;예를 들어<br/>
* 넓은 면이 천천히 변하면 저주파
* 흑백 줄무늬처럼 촘촘히 변하면 고주파

&ensp;가 된다.<br/>

&ensp;즉 영상에서<br/>
* 윤곽선
* 세밀한 텍스처
* 얇은 선
* 반복 무늬

&ensp;는 주로 고주파 성분에 해당한다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-8.png" width="600"></p>

&ensp;2. Viewing Geometry<br/>
&ensp;관찰자와 이미지 사이의 거리가 두 배가 되거나 이미지 크기가 절반으로 줄어들면 공간 해상도도 절반으로 줄여도 디테일 손실을 크게 느끼지 않을 수 있다.<br/>

&ensp;즉 해상도는 절대적인 숫자만이 아니라 얼마나 가까이서, 얼마나 크게 보느냐와 연결된다.<br/>

&ensp;그래서 같은 4K 영상도<br/>
* 큰 TV를 가까이서 볼 때
* 작은 화면을 멀리서 볼 때

&ensp;느낌이 달라진다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-9.png" width="600"></p>

&ensp;HD, SD, UHD<br/>
&ensp;TV/영상 포맷의 해상도<br/>
* 1080i
* 720p
* 480p
* 480i
* UHD

&ensp;여기서 중요한 것은 i와 p의 차이이다.<br/>

&ensp;3. Interlaced vs Progressive<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-10.png" width="600"></p>

&ensp;Progressive<br/>
&ensp;한 프레임의 모든 라인을 순서대로 한 번에 표시한다.<br/>
* 더 자연스럽고
* 선명하며
* 움직임 표현이 좋다

&ensp;Interlaced<br/>
&ensp;홀수 줄, 짝수 줄을 나눠 번갈아 표시한다.<br/>
* 한 번에 모든 줄을 보내지 않아도 되므로 과거 방송 시스템에서 유리했다
* 대신 움직이는 장면에서 줄 갈라짐 같은 문제가 생길 수 있다

&ensp;4. Scanning(Display)<br/>
* Object
* Color video camera
* RGB → YCbCr 변환
* 영상 압축
* YCbCr → RGB 복원
* Display scanning

&ensp;즉 영상 시스템 전체는<br/>
1. 빛을 카메라가 RGB로 받아들이고
2. 전송/압축에 유리한 YCbCr로 바꾸고
3. 다시 화면에 맞게 RGB로 복원한 다음
4. 디스플레이가 스캔 방식으로 보여주는 과정

<p align="center"><img src="/assets/img/Digital Image Processing/chap3/3-11.png" width="600"></p>

&ensp;5. Aliasing과 Moire Pattern<br/>
&ensp;moire pattern은 두 개의 반복 패턴이 미세하게 어긋치면서 생기는 간섭 무늬다. 촘촘한 줄무늬 옷을 촬영할 때 이상한 물결무늬가 보이는 게 대표적이다. 즉 aliasing은 단순히 “깨진다”에서 끝나는 게 아니라 없는 무늬가 새로 생겨 보일 수도 있다는 점이 중요하다.<br/>

&ensp;6. Aspect Ratio<br/>

$$Aspect Ratio = \frac{가로 폭}{세로 높이}$$

&ensp;대표적으로<br/>
* 4:3
* 16:9

&ensp;특히 square-pixel 개념이 중요하다. 픽셀이 정사각형이면 계산이 단순하지만, 직사각형 픽셀을 쓰는 시스템도 있을 수 있다. 즉 화면비는 단순히 모니터 모양이 아니라, 영상 신호가 어떻게 보일지를 결정하는 중요한 파라미터다.<br/>

# 밝기 해상도와 양자화

&ensp;1. Brightness Resolution이란?<br/>
&ensp;한 픽셀이 가질 수 있는 밝기 단계 수를 의미한다. 즉 양자화 수준이 높을수록 더 부드러운 명암 표현이 가능하다.<br/>

&ensp;2. Quantization<br/>
&ensp;연속적인 밝기값을 유한한 단계의 숫자로 바꾸는 과정이다. 예를 들어 실제 밝기가 연속적이어도,
컴퓨터는 0~255 같은 정수로 저장한다.<br/>

&ensp;3. contouring effect<br/>
&ensp;밝기 단계 수가 너무 적으면 부드러운 그라데이션이 끊겨 보인다. 이걸 contouring effect 또는 banding처럼 이해할 수 있다. 즉 하늘 사진에서 원래는 부드럽게 변해야 하는 부분이 층층이 나뉘어 보이면 밝기 해상도가 부족한 것이다.<br/>

&ensp;4. bit depth 예시<br/>
* 일반 소비자용 영상 시스템: 8-bit = 256 levels
* 의료용 X-ray 시스템: 12-bit = 4096 levels

&ensp;5. 거리와 contouring<br/>
&ensp;관찰 거리가 멀어질수록 contouring effect는 덜 눈에 띈다. 이것도 결국 viewing geometry와 연결된다.<br/>