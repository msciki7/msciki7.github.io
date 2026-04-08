---
title: "Chap 4. Filtering in the Frequency Domain"
excerpt: ""

wirter: sohee Kim
categories:
  - Digital Image Processing
tags:
  - 영상처리

toc: true
toc_sticky: true
math: true

date: 2026-04-08
last_modified_at: 2026-04-08
---

# Fourier series와 Fourier transform

&ensp;주기적인 함수는 여러 개의 사인파와 코사인파의 합으로 표현할 수 있고 이것이 Fourier series이다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-2.png" width="600"></p>

&ensp;주기적이지 않은 함수도 마찬가지로 여러 주파수 성분의 적분 형태로 표현할 수 있는데 이것이 Fourier transform이다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-2.png" width="600"></p>

<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-1.png" width="600"></p>

* 저주파: 천천히 변하는 성분 -> 영상에서는 밝기가 완만하게 변하는 부분, 전체적인 유곽
* 고주파: 급격히 변하는 성분 -> 영상에서는 경계선, 에지, 잡음

&ensp;그래서<br/>
* 저주파를 남기면 부드러워짐
* 고주파를 남기면 경계가 강조됨

# 1차원 Fourier Transform과 역변환

&ensp;**정방향 변환**<br/>
&ensp;원래 함수 f(x)를 주파수 성분 F(u)로 바꾼다.<br/>

$$ F(u)= \int_{-\infty }^{\infty }f(x)e^{-j2\pi ux}dx$$

&ensp;이 식은 "원래 신호 f(x) 안에 주파수 u 성분이 얼마나 들어 있는가?"를 측정하는 식이다.<br/>

&ensp;예<br/>
&ensp;시간 영역 신호 x(t)를 주파수 영역 표현 X(jw)로 바꾸는 식<br/>
&ensp;즉 "신호 x(t) 안에 각 주파수 w 성분이 얼마나 들어 있나?"를 계산하는 식<br/>

$$X(jw) = \int_{-\infty }^{\infty }x(t)e^{-jwt}dt$$


&ensp;**역변환**<br/>
&ensp;주파수 성분 F(u)를 다시 원래 신호로 복원한다.<br/>

$$f(x)= \int_{-\infty }^{\infty }F(x)e^{-j2\pi ux}dxu$$

* 정변환: 공간 -> 주파수
* 역변환: 주파수 -> 공간

&ensp;예<br/>

$$x(t) = \frac{1}{2\pi }\int_{-\infty }^{\infty }X(jw)e^{jwt}dw$$

&ensp;$w = 2\pi u$<br/>
&ensp;이건 반대로 주파수 영역에 있는 X(jw)를 다시 모아서 원래 신호 x(t)로 복원하는 식<br/>

&ensp;추가: 두 변수로 transforms<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-4.png" width="600"></p>

# Convolution

&ensp;공간 영역에서 convolution하면 주파수 영역에서는 multiplication이 된다.<br/>

$$f(t) \ast h(t) \leftrightarrow F(u)H(u)$$

&ensp;convolution 정리 증명<br/>

$$\Im \{ f(t) \ast h(t) \} = F(u)H(u)$$

<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-5.png" width="600"></p>

&ensp;원래 공간에서 colvolution은 계산량이 많다. 하지만 주파수 영역으로 가면 그냥 곱셈이다.<br/>

&ensp;그래서 영상 필터링을 할 때<br/>
1. 영상 DFT 구함
2. 필터 DFT와 곱함
3. inverse DFT 수행

&ensp;이렇게 된다.<br/>


# Discrete Space(Time) Fourier Transform(DSFT / DTFT)

&ensp;입력 신호는 이산적이지만 주파수 변수는 연속인 경우이다.<br/>
* 입력 : $x(n_1, n_2)$
* 출력: $X(\hat{w}_1, \hat{w}_2)$ 

1. 출력은 일반적으로 복소수
2. 주기성을 가진다.
3. magnitude 와 phase로 나눠 볼 수 있다.

&ensp;DSFT 정의<br/>

$$X(\hat{w}_1, \hat{w}_2) = \sum_{n_1 = -\infty }^{\infty }\sum_{n_2 = -\infty }^{\infty }x(n_1, n_2)e^{-j\hat{w}_1n_1}e^{-j\hat{w}_2n_2}$$

&ensp;이걸 보면 사실 1차원 DTFT를 두 번 한 것과 같다.<br/>
&ensp;1차원에서는<br/>

$$X(\hat{w}) = \sum_{n= -\infty }^{\infty }x[n]e^{-j\hat{w}n}$$

&ensp;였고 2차원에서는 축이 두 개니까 $n_1, n_2$에 대해 각각 지수항이 붙는다.<br/>

&ensp;역변환<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-7.png" width="600"></p>

&ensp;이 식은 위에서 구한 주파수 표현을 다시 모두 합쳐서 원래 신호를 복원하는 식이다.<br/>

$\hat{w} = 2\pi u$

* u: cycle/sample 같은 느낌의 주파수
* $\hat{w}$ : rad/sample

&ensp;둘이 단위만 다르고 본질적으로 같은 주파수 정보<br/>

&ensp;적분 구간이 −π부터 π까지인 이유<br/>
&ensp;이건 이산 신호의 푸리에 변환이 주기적이기 때문이다. 즉 전 주파수축 전체를 적분할 필요가 없고 한 주기만 적분하면 된다.<br/>
&ensp;그래서 한 주기인 $−π ≤ \hat{ω}_1 ≤ π, −π ≤ \hat{ω}_2 ≤ π $ 만 적분하는 것<br/>

&ensp;결론: $X(\hat{w}_1, \hat{w}_2)$ 는일반적으로 복소수이고 연속 변수이며 주기적이다.<br/>
&ensp;$x(n_1, n_2)$ 가 stable이면 존재한다.<br/>

&ensp;Magnitude와 Phase<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-8.png" width="600"></p>

&ensp;정리<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-9.png" width="600"></p>

&ensp;간단한 연속시간 함수의 Fourier Transform 예제<br/>
&ensp;직사각형 함수의 푸리에 변환 결과가 sinc 형태가 되는 예제이다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-6.png" width="600"></p>

* 직각형(rectangle) <-> sinc
* 공간에서 폭이 넓어지면 주파수에서는 폭이 좁아짐
* 공간에서 폭이 좁아지면 주파수에서는 폭이 넓어짐

&ensp;높이가 A, 폭이 W인 직사각형 함수<br/>

$$f(t) = \left\{\begin{matrix}
A , -\frac{W}{2} \leq t \leq \frac{w}{2} \\  0, otherwise
\end{matrix}\right.$$

&ensp;원점 중심으로 가로폭이 W이고 함수값은 A인 상자 모양<br/>

&ensp;구하고 싶은 것<br/>
&ensp;연속시간 푸리에 변환 정의를 사용하면<br/>

$$F(u) = \int_{-\infty }^{\infty }f(t)e^{-j2\pi ut}dt$$

&ensp;f(t)는 -W/2 부터 W/2까지만 A이고 나머지는 0이므로 적분구간이 줄어든다.<br/>

$$F(u) = \int_{-\frac{W}{2} }^{\frac{W}{2} }Ae^{-j2\pi ut}dt$$

&ensp;수학적 증명 과정<br/>
&ensp;step1. 상수 A를 밖으로 뺀다.<br/>

$$F(u) = A\int_{-\frac{W}{2}}^{\frac{W}{2}}e^{-j2\pi ut}dt$$

&ensp;step2. 지수함수를 적분한다.<br/>

$$\int e^{-j2\pi ut}dt$$

&ensp;를 적분해야 한다.<br/>
&ensp;지수함수 적분 공식에 의해<br/>

$$\int e^{at} dt = \frac{1}{a}e^{at}$$

&ensp;이므로 여기서는 $a = -j2\pi u$ 이다.<br/>

&ensp;따라서<br/>

$$\int e^{-j2\pi ut}dt = \frac{e^{-j\pi ut}}{-j2\pi u}$$

&ensp;그래서<br/>

$$F(u)= A\begin{bmatrix}\frac{e^{-j2\pi ut}}{-j2\pi u} \end{bmatrix}_{-W/2}^{W/2}$$

&ensp;step3. 구간 대입<br/>
&ensp;상한 $t = \frac{W}{2}$, 하한 $t = -\frac{W}{2}$ 를 넣으면<br/>

$$F(u) = A\begin{pmatrix}\frac{e^{-j2\pi u(W/2)}- e^{-j2\pi u(-W/2)}}{-j2\pi u}\end{pmatrix}$$

&ensp;정리하면<br/>

$$F(u) = A\begin{pmatrix}\frac{e^{-j\pi uW} - e^{j\pi uW}}{-j2\pi u}\end{pmatrix}$$

&ensp;step4. 오일러 공식 사용<br/>

$$e^{j\theta} - e^{-j\theta } = 2jsin\theta$$

&ensp;여기서 $\theta = \pi uW$ 이므로<br/>

$$F(u) = A \cdot \frac{-2jsin(\pi uW)}{-j2\pi u} = A\frac{sin(\pi uW)}{\pi u}$$

&ensp;step 5. sinc 형태로 정리<br/>
&ensp;이 식을 보통 W를 묶어서 정리한다.<br/>

$$F(u) = AW\frac{sin(\pi uW)}{\pi uW}$$

&ensp;그리고 sinc를<br/>

$$sinc(x) = \frac{sin(\pi x)}{\pi x}$$

&ensp;로 정의하면<br/>

$$F(u) = AWsinc(uW)$$

&ensp;가 된다.<br/>

&ensp;u = 0 에서는 어떻게 될까?<br/>
&ensp;방금 얻은 식<br/>

$$F(u) = A\frac{sin(\pi uW)}{\pi u}$$

&ensp;은 u = 0을 대입하면 분모가 0이라서 바로 넣기 곤란하다. 그런데 실제로는 극한을 보면 된다.<br/>

$$F(0) = \displaystyle \lim_{u \to 0}A\frac{sin(\pi uW)}{\pi u} = AW\displaystyle \lim_{u \to 0}\frac{sin(\pi uW)}{\pi uW} = AW$$

&ensp;zero crossing은 어떻게 나올까?<br/>
&ensp;분자가 0이 될 때<br/>
&ensp;$sin(\pi uW) = 0$ 이어야 한다.<br/>
&ensp;사인 함수가 0이 되는 조건은 $\pi uW = l\pi (l: integer)$ 이다.<br/>
&ensp;양변을 π로 나누면<br/>

$$u = \frac{1}{W}$$

&ensp;단, l = 0이면 원점이라 zero crossing이 아니라 peak이므로 보통 l ≠ 0 이라고 둔다.<br/>

&ensp;W가 커질 때<br/>
&ensp;공간 영역에서 폭이 넓어지면 주파수 영역에서는 스펙트럼이 더 좁고 더 높아진다.<br/>

&ensp;W가 작아질 때<br/>
&ensp;공간 영역에서 폭이 좁아지면 주파수 영역에서는 스펙트럼이 넓게 퍼진다.<br/>

&ensp;시험에 나올 수 있는 부분 체크<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-10.png" width="600"></p>

<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-11.png" width="600"></p>

## Properties of DSFT

&ensp;1. Linearity<br/>

$$ax + by <-> aX + bY$$

&ensp;입력의 선형결합은 출력에서도 선형결합이 된다.<br/>

&ensp;2. Convolution<br/>

$$ x ** y <-> XY$$

&ensp;공간에서 convolution은 주파수에서 곱셈이다.<br/>

&ensp;3. Separable sequence<br/>

$$x(n_1, n_2) = x_1(n_1)x_2(n_1)$$

&ensp;이면<br/>

$$X(w_1, w_2) = X_1(w_1)X_2(w_2)$$

&ensp;가 된다.<br/>
&ensp;2차원 문제를 1차원 두개로 분해할 수 있다.<br/>

&ensp;4. Parseval’s theorem<br/>
&ensp;공간(또는 시간) 영역에서의 전체 에너지 = 주파수 영역에서의 전체 에너지<br/>
&ensp;신호를 원래 영역에서 보든 푸리에 변환한 뒤 보든 전체 에너지는 보존된다는 뚯이다.<br/>

&ensp;2차원 DSFT<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-12.png" width="600"></p>

* 왼쪽: 원래 신호 $x(n_1, n_2)$ 의 총 에너지
* 오른쪽: 주파수 표현 $X(\hat{w}_1, \hat{w}_2)$ 의 총 에너지

&ensp;1차 형태부터 이해<br/>
&ensp;1차원 DTFT의 Parseval 정리<br/>

$$\sum_{n= -\infty }^{\infty }\begin{vmatrix}x(n)\end{vmatrix}^2  = \frac{1}{2\pi }\int_{-\pi }^{\pi }\begin{vmatrix}X(\hat{w})\end{vmatrix}^2d\hat{w}$$

&ensp;이걸 풀어서 쓰면<br/>

$$\sum_{n= -\infty }^{\infty }x(n)x^{*}(n) = \frac{1}{2\pi }\int_{-\pi }^{\pi }X(\hat{w})X^* (\hat{w})d\hat{w}$$

&ensp;*는 complex conjugate, 즉 켤레복소수이다.<br/>

&ensp;1차원 Parseval 정리 증명<br/>
&ensp;Step 1. 시작식<br/>
&ensp;에너지 정의부터 시작<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-13.png" width="600"></p>

&ensp;Step2. $x^* (n)$ 에 inverse DTFT를 대입<br/>
&ensp;DTFT의 역변환은<br/>

$$x(n) = \frac{1}{2\pi }\int_{-\pi }^{\pi }X(\hat{w})e^{j\hat{w}n}d\hat{w}$$

&ensp;그럼 컬레를 취하면<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-14.png" width="600"></p>

&ensp;Step 3. 다시 원래 식에 대입<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-15.png" width="600"></p>

&ensp;Step 4. 합과 적분 순서를 바꾼다<br/>

$$= \frac{1}{2\pi }\int_{\-\pi }^{\pi }X^* (\hat{w})\begin{bmatrix} \sum_{n=-\infty }^{\infty }x(n)e^{-j\hat{w}n} \end{bmatrix}d\hat{w}$$

$$X(\hat{w}) = \sum_{n=-\infty }^{\infty }x(n)e^{-j\hat{w}n}$$

&ensp;이므로<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-16.png" width="600"></p>

&ensp;시험에 나올 수 있는 부분 체크<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-17.png" width="600"></p>

<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-18.png" width="600"></p>

## Example 1 of DSFT

&ensp;마스크 모양을 보면 중심이 2이고 상하좌우가 1인 형태이다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-19.png" width="600"></p>

&ensp;결과는<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-20.png" width="600"></p>

<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-21.png" width="600"></p>

&ensp;이 응답은 원점 근처에서 값이 크고 멀어질수록 작아지는 형태이므로 Low Pass Filter이다.<br/>

## Example 2 of Fourier Transform

&ensp;마스크는<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-22.png" width="600"></p>

&ensp;separable하다고 설명<br/>
&ensp;즉 $h(n_1, n_2) = h_1(n_1)h_2(n_2)$ 로 나눌 수 있다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-23.png" width="600"></p>

&ensp;결과<br/>

$$H_1(w_1) = 3 - 2cos(w_1), H_2(w_2) = 3 - 2cos(w_2)$$

&ensp;이므로<br/>

$$H(w_1, w_2) = H_1(w_1)H_2(w_2)$$

<p align="center"><img src="/assets/img/Digital Image Processing/chap4/4-23\4.png" width="600"></p>

&ensp;이 응답은 고주파 쪽이 강하므로 HPF이다. 즉 샤프닝이나 에지 강조에 쓰이는 형태다.<br/>