---
title: "Chap 3. The Digital Image"
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
last_modified_at: 2026-03-22
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

