---
title: "2장 Time domain representation of LTI Systems"
excerpt: "선형 시불변(linear time invariant: LTI) 시스템의 입력과 출력 사이의 관계를 설명하는 여러 방법들을 검토한다. "

wirter: sohee Kim
categories:
  - Signals and Systems
tags:
  - singal
  - system
toc: true
use_math: true 
toc_sticky: true

date: 2025-03-26
last_modified_at: 2025-03-26
---


1\. 서론
======

&ensp;LTI 시스템의 특성은 먼저 임펄스 응답(impulse response)을 이용하여 설명한다. 임펄스 응답은 t = 0 또는 n = 0에서 임펄스 신호가 입력으로 인가될 때 이에 대응해서 나타나는 LTI 시스템의 출력으로 정의된다. 임펄스 응답은 시스템의 구성과 동적 특성에 관한 지식으로부터 결정되거나 시스템을 모를 경우에는 근사 임펄스를 입력에 인가하여 측정된다. 이산시간 시스템의 임펄스 응답은 입력을 δ[n]으로 설정하여 보편적으로 쉽게 얻는다. 이산시간 시스템의 임펄스 응답은 입력을 δ[n]으로 설정하여 보편적으로 쉽게 얻는다. 연속시간인 경우 임펄스 함수는 시간폭이 0이고 크기는 ∞이므로 실제적으로 얻을 수 없고 아주 짧은 시간폭과 아주 큰 크기를 갖는 펄스를 근사적으로 사용한다. 그러므로 임펄스 응답은 극히 짧은 시간폭과 큰 에너지를 가진 입력에 대응하는 시스템 동작이라고 해석할 수 있다. 임펄스 응답이 주어졌을 때 임의의 입력에 대응하는 출력은 입력을 시간이 이동된 임펄스의 가중합으로 표현함으로써 계산된다. 선형성과 시불변성에 의하면 시스템의 출력은 시간 이동된 임펄스 응답의 가중합이어야 한다. 이러한 가중합을 이산시간 시스템에서는 콘벌루션 합(convolution sum)이라 부르고 연속시간 시스템에서는 콘벌루션 적분(convolution integral)이라고 부른다. <br/>

&ensp;LTI 시스템의 입출력 동작을 설명할 두 번째 방법은 선형 상수계수 미분 또는 차분 방정식(linear constant-coefficient differential or difference equation)이다. 미분 방정식은 연속시간 시스템을 표현하기 위해 이용되고 차분 방정식은 이산시간 시스템을 표현하기 위해 이용된다. 시스템 표현의 세 번째 방법은 블록 다이어그램(block diagram)이다. 블록록 다이어그램이란 세 개의 기본 연산의 상호 접속으로 표현된 시스템을 말한다. 이산시간 시스템의 기본 연산은 스칼라 곱셈, 덧셈 및 시간이동(시간지연)이고 연속시간 시스템의 기본 연산은 스칼라 곱셈, 덧셈 및 적분이다. 시스템 표현의 마지막 방법은 상태변수(state variable)방법이다. 상태변수 방법은 시스템의 상태의 거동을 나타내는 연립 1계 미분 또는 차분 방정식과 시스템의 상태들을 시스템의 출력에 관련시키는 한 개의 출력 방정식으로 이루어진다. 시스템을 구성하는 에너지 저장소이자 기억소자와 관계되는 변수들의 집합을 시스템의 상태로 정의한다. <br/>


2\. Convolution Sum
======

&ensp;시간 이동된 임펄스의 가중합으로 임의의 신호를 표현하고 그 다음으로 표현된 신호를 LTI 시스템에 입력으로 인가하면 콘벌루션 합을 얻는다. 이와 비슷한 과정을 적용하여 연속시간 시스템에 대한 콘벌루션 적분을 얻는다.<br/>
&ensp;x[n]δ[n] = x[0]δ[n]<br/>
&ensp;x[n]δ[n-k] = x[k]δ[n-k]<br/>
&ensp;n은 시간 지표이고 x[n]은 전체 신호를 나타내고 x[k]는 시간 n = k에서의 신호값을 나타낸다. 시간 이동된 임펄스와 신호를 곱한 결과는 시간 이동된 임펄스와 그 임펄스가 발생된 시간에서의 신호값의 크기의 곱으로 나타난다. 다음과 같이 시간 이동된 임펄스의 가중합으로 신호 x[n]을 표현할 수 있다. <br/>

$x[n] = .....+ x[-2]δ[n + 2] + x[-1]δ[n + 1] + x[0]δ[n] + x[1]δ[n - 1]+ x[2]δ[n - 2] ...... =  \sum_{k = -\infty }^{\infty }x[k]\delta [n-k]$

<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-1.jpg" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-2.jpg" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-9.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-10.JPEG" width="600"></p>

&ensp;$x[n] = \sum_{k=-\infty }^{\infty }x[k]\delta [n-k]$ (x[n] = a weighted sum of time-shifted impulses)<br/>
&ensp;정의 : 임펄스 응답 h[n]은 입력이 $\delta [n]$ 일 때 시스템의 output이다.<br/>

&ensp;신호 x[n]이 인가된 시스템을 연산자 H로 표현한다. 입력 x[n]이 인가된 시스템 H에 식을 적용하면 출력은 다음과 같다.<br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-3.jpg" width="600"></p>

&ensp;linear : 
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-4.jpg" width="600"></p>

&ensp;T.I :
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-5.jpg" width="600"></p>

&ensp;이 관계는 시간 이동된 임펄스 입력에 관한 출력이 임펄스에 대한 응답을 시간 이동 시킨 것과 같음을 의미한다. <br/>
$H\begin{Bmatrix}\delta [n-k]\end{Bmatrix} = h[n-k]$ <br/>

&ensp;LTI 시스템의 출력은 시간 이동된 임펄스 응답의 가중합으로 계산된다. 이러한 식은 입력 신호를 시간 이동된 임펄스의 가중합으로 표현한 것으로부터 직접 이끌어낸 결과이다.<br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-6.jpg" width="600"></p>

&ensp;하나의 n에 대한 출력은 k만큼 시간 이동되어 가중된 임펄스 입력에 대응하는 응답을 k = -∞부터 k = ∞까지 합산한 것이다. <br/>

* 문제 1
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-7.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-11.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-39.JPEG" width="600"></p>



3\. 콘벌루션 합: 계산 과정
======

&ensp;입력신호의 지속기산이 아주 길어지면 위은 과정이 지루한 계산이 되므로 콘벌루션 합을 계산하는 다른 방법으로 출력을 찾는다. <br/>
&ensp;콘벌루션 합의 표현은 
$y[n] = \sum_{k=-\infty }^{\infty }x[k]h[n-k]$ <br/>
&ensp;cf. $w_{n}[k]$ 는 중간 신호로서 다음과 같이 x[k]와 h[n-k]의 곱으로 정의한다. <br>
$w_{n}[k] = x[k]h[n-k]$ <br/> 

* 문제 2
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-8.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-12.JPEG" width="600"></p>

<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-13.JPEG" width="600"></p>

* 문제 3
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-14.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-15.JPEG" width="600"></p>

* 문제 4
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-16.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-17.JPEG" width="600"></p>


4\. 콘벌루션 적분(The Convolution Integral)
======

&ensp;연속시간 LTI 시스템의 출력도 역시 입력과 시스템의 임펄스 응답에 관한 지식으로부터 완벽하게 결정될 수 있다. 이에 관한 접근방식과 결과는 이산시간의 경우와 아주 유사하다. <br/>
$ x(t) = \int_{-\infty }^{\infty } x(\tau )\delta (t - \tau )d\tau$ <br/>
&ensp;중첩 계산은 합산 대신 적분이 이용되고 시간 이동은 연속변수 $\tau$ 로 표시되어 있다. 가중값 x(t)dt는 각 임펄스가 발생되는 시간 $\tau$ 에서의 신호 x(t)의 값으로부터 얻는다. 입력 x(t)가 인가된 시스템을 연산자 H로 표기한다. 가중 중첩으로 표현되는 일반적인 입력에 대응하여 응답하는 시스템 출력은 다음과 같다.<br/>
$y(t) = H{x(t)} = H\begin{Bmatrix}\int_{-\infty }^{\infty }x(\tau )\delta (t - \tau )d\tau \end{Bmatrix}$ <br/>

&ensp;시스템의 선형성을 이용하고 연산자 H와 적분의 순서를 교환하면<br/>
$y(t) = \int_{-\infty }^{\infty }x(\tau )H{\delta (t - \tau )}d\tau $<br/>
&ensp;이산시간 시스템의 경우와 같이 시간 이동된 임펄스들에 대한 연속시간 선형 시스템의 응답은 시스템의 입출력 특성으로부터 완벽하게 얻어진다. 그 다음으로 단위 임펄스 입력에 대한 응답인 시스템 출력을 시스템의 임펄스 응답 $h(t) = H{\delta(t)}$ 이라고 정의한다. 시스템템이 시불변이면 $H{\delta(t-\tau )} = h(t-\tau )$. 시불변이란 시간 이동된 임펄스 입력은 시간 이동된 임펄스 응답을 출력으로 생성한다는 의미를 내포하고 있다. 입력에 대한 LTI 시스템의 출력은 다음과 같이 표현된다. <br/>
$y(t) = x(t) \ast h(t) = \int_{-\infty }^{\infty }x(\tau )h(t - \tau )d\tau $<br/>

* 문제 5
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-18.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-19.JPEG" width="600"></p>

* 문제 6
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-20.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-21.JPEG" width="600"></p>

* 문제 7
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-22.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-23.JPEG" width="600"></p>


5\. 콘벌루션 적분: 계산과정
======

* 문제 8
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-24.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-25.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-26.JPEG" width="600"></p>

6\.LTI 시스템의 접속(Interconnections of LTI Systems)
=======

&ensp;상호 접속된 LTI 시스템의 전체 임펄스 응답과 각 시스템의 임펄스 응답 사이의 관계를 알아본다. <br/>

&ensp;1_LTI 시스템의 병렬 접속(Parallel connection of LTI Systems)<br/>
&ensp;임펄스 응답이 각각 h1(t)와 h2(t)인 두 시스템을 병렬로 접속한다. 전체 시스템의 출력 y(t)는, <br/>

$y(t) = y_{1}(t) + y_{2}(t) = x(t)\ast h_{1}(t) + (t) \ast h_{2}(t)$<br/>
$y(t) = \int_{-\infty }^{\infty }x(\tau )h_{1}(t - \tau ) +\int_{-\infty }^{\infty }x(\tau )h_{2}(t - \tau )d\tau$<br/>
$ y(t) = \int_{-\infty }^{\infty }x(\tau)\begin{Bmatrix}h_{1}(t - \tau ) + h_{2}(t - \tau ) \end{Bmatrix}d\tau = \int_{-\infty }^{\infty }x(\tau )h(t - \tau )d\tau  = x(t)\ast h(t)$<br/>

<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-27.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-28.JPEG" width="600"></p>

&ensp;2_시스템의 종속접속(Cascaded Connection of LTI Systems)<br/>

$y(t) = z(t)\ast h_{2}(t)$<br/>
$y(t) = \int_{-\infty }^{\infty }z(\tau )h_{2}(t - \tau )d\tau $<br/>
$y(t) = x(t)\ast h_{1}(t)$<br/>
$y(t) = \int_{-\infty }^{\infty }x(\nu )h_{2}(t - \nu )d\nu $<br/>
$y(t) = \int_{-\infty }^{\infty }\int_{-\infty}^{\infty}x(\nu )h_{1}(\tau -\nu )h_{2}(\tau -\nu )d\nu d\tau $<br/>
$\eta = \tau - \nu$ 로 변환하고 적분 순서를 재배열하면<br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-29.JPEG" width="600"></p>
 
 &ensp;$h(t - \nu ) = \int_{-\infty }^{\infty }h_{1}(\eta )h_{2}(t - \nu -\eta )d\eta $<br/>
 &ensp;$y(t) = \int_{-\infty }^{\infty } x(\nu )h(t - \nu )d\nu  = x(t)\ast h(t)$<br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-30.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-31.JPEG" width="600"></p>

$h(t) = h_{1}(t)\ast h_{2}(t)$ 를 적분으로 표현하면<br/>
$h(t) = \int_{-\infty }^{\infty }h_{1}(\tau )h_{2}(t - \tau )d\tau$<br/>
$\nu = t -\tau $ 에 따라 변환하면 <br/>
$h(t) = \int_{-\infty }^{\infty }h_{1}(t - \nu )h_{2}(\nu )d\nu = h_{2}(t)\ast h_{1}(t)$<br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-32.JPEG" width="600"></p>

* 문제 9
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-33.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-34.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-35.JPEG" width="600"></p>

7\. LTI 시스템의 특성과 임펄스 응답의 관계(LTI System properties and the Impulse Response)
======

&ensp;1_무기억 시스템(Memoryless LTI System)<br/>
&ensp;무기억 LTI 시스템의 출력은 현재 입력에만 연관된다. convolution의 교환성을 적용하면 이산시간 시스템의 출력은 다음과 같다.<br/>

$y[n] = h[n]\ast x[n] = \sum_{k = -\infty }^{\infty }h[k]x[n-k]$<br/>
$y[n] = ...+ h[-2]x[n+2] + h[-1]x[n+1] + h[0]x[n] + h[1]x[n-1] + h[2]x[n-2] + ....$<br/>

&ensp;이 시스템이 무기억성이라면 y[n]은 x[n]에만 의존해야 하고 k ≠ 0 인 x[n-k]에는 관계가 없어야 하며 h[0]x[n]인 항을 제외한 모든 항이 0이어야 한다. 이 사실로부터  k ≠ 0일 때 h[0] = 0임이 분명하다. 이산시간 시스템이 무기억성인 경우는 $h[k] = c\delta[k]$ 인 경우뿐이다. <br/>

&ensp;연속시간 LTI 시스템의 출력은 <br/>

$y(t) = \int_{-\infty }^{\infty }h(\tau )x(t - \tau )d\tau $<br/>

&ensp;연속시간 시스템의 임펄스 응답이 다음 조건 $h(\rho) = c\delta(\tau)$ 를 만족하는 경우에만 그 연속시간 시스템의 무기성을 갖는다. <br/>

&ensp;2_인과 LTI 시스템(Causal LTI Systems)<br/>
&ensp;인과성 LTI 시스템은 그의 출력이 과거와 현재에만 의존하는 시스템이다. <br/>
$y[n] = ...+ h[-2]x[n+2] + h[-1]x[n+1] + h[0]x[n] + h[1]x[n-1] + h[2]x[n-2] + ....$<br/>
&ensp;과거와 현재 입력인 x[n], x[n-1], x[n-2].. 등은 k > 0인 임펄스 응답 h[k]에 관련되고 반면에 미래의 입력 x[n+1], x[n+2],..등은 k > 0인 임펄스 응답 h[k]에 관련된다. 그러므로 출력 y[n]이 과거 및 현재 입력에만 의존하려면 k < 0일 때 반드시 h[k] = 0이어야 한다. 이에 따라 이산시간 인과성 LTI시스템에 대해서 임펄스 응답은 **k < 0, h[k] = 0**이어야 하고 그의 콘벌루션 합은 다음과 같이 새로운 형태로 표현된다.<br/>

$y[n] = \sum_{k = 0}^{\infty }h[k]x[n-k]$<br/>

&ensp;일반적인 연속시간 시스템의 출력에 관한 콘벌루션 적분을 다시 쓰면 <br/>
&ensp;$y(t) = \int_{-\infty }^{\infty }h(\tau )x(t - \tau )d\tau $<br/>
&ensp;$\tau < 0$ 일 때 $h(\tau) = 0$ 이므로 일반적인 연속시간 시스템의 콘벌루션 적분에 인과성을 적용하면 인과성 시스템에 대한 다음과 같은 새로운 형태의 콘벌루션 적분을 얻는다.<br/>
&ensp;$y(t) = \int_{0 }^{\infty }h(\tau )x(t - \tau )d\tau $<br/>

&ensp;3\_안정 LTI 시스템(Stable LTI System)<br/>
&ensp;어떤 시스템의 입력이 유한 크기일 때 그 시스템의 출력도 유한 크기이면 그 시스템은 BIBO 안정성을 갖는다고 정의하였다. 안정한 이산 시스템에서 
$\begin{vmatrix}x[n]\end{vmatrix} \leq M_{x} \leq \infty$ 
이면 그 시스템의 출력도 $\begin{vmatrix}y[n]\end{vmatrix} \leq M_{x} \leq \infty$ 을 만족해야 한다. 
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-36.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-37.JPEG" width="600"></p>

&ensp;4\_가역성 시스템과 역콘벌루션<br/>
&ensp;어떤 시스템의 입력 신호가 배율 상수를 제외하고 그 시스템의 출력 신호로부터 복원될 수 있으면 이 시스템을 가역성 시스템(invertible system)이라고 부른다. 시스템의 출력을 입력으로 받아들여서 원래 시스템의 입력을 출력 신호로 발생시키는 시스템이 존재한다는 뜻이다. 이러한 새로운 시스템을 원래 시스템의 역시스템(inverse system)이라고 부른다. $h(t)\ast x(t)$ 로부터 x(t)를 복원하는 과정은 콘벌루션을 수행하는 과정을 반대로 수행하는 것이므로 역콘벌루션(deconvolution)이라고 부른다.<br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-38.JPEG" width="600"></p>

* 문제 10
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-40.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-64.JPEG" width="600"></p>

8\. 계단 응답<br/>
&ensp;입력 신호의 갑작스런 변동에 대한 LTI 시스템의 응답을 관찰하기 위해서 계단 입력 신호가 자주 사용된다. 계단 응답(step response)은 단위 계단 입력 신호에 대한 시스템의 출력으로 정의된다. 이산시간 LTI시스템에서 임펄스 응답을 h[n]으로 표현하고 계단 응답을 s[n]으로 표현한다. <br/>

$s[n] = h[n] \ast u[n] = \sum_{k=-\infty }^{\infty }h[k]u[n - k]$

&ensp;k > n이면 u[n - k] = 0이고 k ≦ n이면 u[n-k] = 1이므로 위의 식은 다음과 같이 정리된다.<br/>
$s[n] = \sum_{k = -\infty }^{\infty }h[k]$

&ensp;이와 같이 LTI시스템의 계단 응답은 임펄스 응답을 누산하여 얻을 수 있다. 같은 방법으로 연속시간 시스템의 계단 응답은 임펄스 응답의 적분으로 다음과 같이 얻을 수 있다. <br/>

$s(t) = \int_{-\infty }^{t}h(\tau )d\tau$

&ensp;이 관계들을 거꾸로 적용하면 임펄스 응답을 계단 응답으로 표현하는 식을 다음과 같이 얻는다. 이산시간 시스템에 관한 결과는 
$h[n] = s[n] - s[n-1]$ 이고 연속시간 시스템에 대한 결과는 $h(t) = \frac{d}{dt}s(t)$

9\. LTI시스템에 대한 미분-차분 방정식 표현
=======

&ensp;선형 상수 계수 차분 또는 미분 방정식은 LTI 시스템의 입출력 특성에 관한 또 다른 표현이다. 차분 방정식은 이산시간 시스템을 표현하기 위해 이용되고 미분 방정식은 연속시간 시스템을 표현한다. 선형 상수 계수 미분 방정식의 일반적인 형태는<br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-41.JPEG" width="600"></p>

&ensp;차분 방정식을 재배열해서 입력 신호와 과거 출력으로부터 현재 출력을 계산할 수 있는 재귀 방정식을 얻을 수 있다. <br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-42.JPEG" width="600"></p>

10\. 미분 및 차분 방정식의 해법
======

&ensp;미분 또는 차분 방정식으로 표현되는 시스템의 출력은 2가지 성분의 합으로 이루어진다. 제 1성분은 미분 또는 차분 방정식의 동차형의 해로서 일반적으로 동차해(homogeneous solution)라 부르고 $y^{(h)}$ 로 나타낸다. 제 2 성분은 입력 신호에 따른 본래의 미분 또는 차분 방정식의 해로서 특수해(particular solution)라고 부르고 $y^{(p)}$ 로 나타낸다. 그러므로 방정식의 완전 해(complete solution) y는 $ y = y^{(h)}  + y^{(p)}$ 이다. <br/>

&ensp;1\_동차해(homogeneous solution)<br/>
&ensp;미분 또는 차분 방정식의 동차형은 방정식에서 모든 입력을 0으로 놓는 것이다.연속시간 시스템에 대해서 $y^{(h)}(t)$ 는 다음 동차 방정식의 해이다.<br/>

$sum_{k = 0}^{N}a_{k}\frac{d^{k}}{dt^{k}}y^{(h)}(t) = 0$ <br/>
&ensp;연속시간 시스템에 관한 동차해는 다음의 형태로 나타난다.<br/>

$y^{(h)}(t) = \sum_{i = 1}^{N}c_{i}e^{r_{i}t}$<br/>
&ensp;$c_{i}$ 는 임의의 상수이고  $r_{i}$ 는 다음 식으로 정의되는 시스템의 특성 방정식(characteristic equation)이 갖는 N개의 해이다.<br/>
$\sum_{k = 0}^{N} a_{k}r^{k} = 0$
&ensp;이산시간 시스템에서 동차 방정식은 <br/>
$\sum_{k = 0}^{N} a_{k}y^{(h)}[n - k] = 0$ 이고 동차해의 형태는 $y^{(h)}[n] = \sum_{i = 1}^{N}c_{i}r_{i}^{n}$ 이다. <br/>
&ensp;$c_{i}$ 는 임의의 상수이고  $r_{i}$ 는 다음 식으로 정의되는 시스템의 특성 방정식(characteristic equation)이 갖는 N개의 해이다.<br/>
$\sum_{k = 0}^{N}a_{k}r^{N-k} = 0$ <br/>

* 문제 11
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-43.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-44.JPEG" width="600"></p>

* 문제 12
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-45.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-46.JPEG" width="600"></p>

&ensp;2_특수해(Particular solution)<br/>
&ensp;특수해 $y^{(p)}$ 는 미분 또는 차분 방정식에서 주어진 입력에 대응하는 해로 정의하며 시스템에 관한 유일성을 갖지 않는다. 특수해는 입력과 같은 형태의 해를 가정하여 얻는 것이 보통이다. 특수해 관련 이런 해법은 입력 신호가 동차해의 성분과 동일한 경우이면 수정되어야 한다. 그러한 경우 특수해는 동차해의 모든 성분과 독립적이라고 가정한다. 이러한 과정은 특성 방정식의 근이 중복근인 경우에 독립적인 항을 찾는 과정과 동일하다. 특히 특수해의 형태에 t 또는 n의 제일 낮은 차의 거듭제곱 항을 곱해서 그 결과가 동차해와 독립적으로 만들어 새로운 특수해의 형태를 얻는다. 이 결과를 본래의 미분 또는 차분 방정식에 대입하여 상수를 결정함으로써 시스템에 맞는 특수해를 확정한다. 
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-47.JPEG" width="600"></p>

* 문제 13
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-48.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-49.JPEG" width="600"></p>

&ensp;3_완전해<br/>
&ensp;미분 또는 차분 방정식으로부터 얻은 특수해와 동차해를 합산하여 새로운 해를 구성하고 새로운 해가 주어진 초기조건을 만족하도록 동차해 성분에 포함되어 있는 상수들을 결정한다. 입력이 t = 0 또는 n = 0에서 인가되어서 특수해 각각 t > 0 또는 n >= 0 에 대해서 적용된다고 가정한다. 완전해는 이 시간 영역에 대해서만 성립한다. 그러므로 이산시간 시승템에서 초기조건 y[-N], y{-N + 1}, ...., y[-1]은 제 3 단계를 시작하기 이전에 y[0], y[1], y[N-1]의 조건ㅇ으로 변환되어야 한다.<br/>
&ensp;연속시간 시스템의 경우 $t = 0^{-}$ 의 값으로 주어진 초기조건은 t = 0에서 입력을 인가하는 효과를 반영할 수 있도록 t = 0^{+}의 초기값으로 변화되어야 한다. 
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-50.JPEG" width="600"></p>

* 문제 14
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-51.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-52.JPEG" width="600"></p>

* 문제 15
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-53.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-54.JPEG" width="600"></p>

* 문제 16
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-55.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-56.JPEG" width="600"></p>


11\. 블록 다이어그램 표현
======

&ensp;이제 미분 또는 차분 방정식으로 표현되는 LTI 시스템을 블록 다이러그램으로 표현하는 방법을 알아본다. 블록 다이어그램(block diagram)은 입력 신호에 가해지는 기본 연산들의 상호 접속으로 정의한다. 블록 다이어그램은 시스템의 내부 계산이나 연산이 어떤 순서로 이루어지는가를 나타내주기 때문에 시스템에 관해 임펄스 응답이나 미분 또는 차분 방정식들보다 블록 다이어그램이 더 상세한 표현이다. 임펄스 응답이나 미분 또는 차분 방정식들은 시스템의 입력과 출력에 관한 동작만을 나타내는 표현이다. 입출력의 관계가 주어진 한 개의 시스템이 서로 다른 블록 다이어그램으로 표현됨을 알게 될 것이다. 각각의 블록 다이어그램은 시스템의 출력을 계산하기 위해 사용하는 계산과정이 서로 다른 것을 나타낸다. <br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-57.JPEG" width="600"></p>

&ensp;블록 다이어그램에서 사용되는 연산에 관한 각각의 기호이다. 적분으로 연속시간 LTI 시스템을 나타내려면 미분 방정식을 적분 방정식으로 변환해야 한다. 대부분의 연속시간 시스템의 블록 다이어그램 표현에서 미분 대신 적분 연산이 이용된다. 이와 더불어 적분기 시스템에서 잡음을 감소시키는 효과를 갖는 데 반해 미분기는 잡음을 강조하는 효과를 갖고 있기 때문이다.<br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-58.JPEG" width="600"></p>


&ensp;시스템 동작에 관한 적분 또는 미분 방정식은 블록 다이어그램에 의해 표현된 일련의 연산작용을 방정식의 형태로 나타냄으로써 얻을 수 있다. <br/>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-59.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-60.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-61.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-62.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-63.JPEG" width="600"></p>

































