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
toc_sticky: true

date: 2025-03-26
last_modified_at: 2025-03-26
---


&ensp;1. 서론<br/>
======

&ensp;LTI 시스템의 특성은 먼저 임펄스 응답(impulse response)을 이용하여 설명한다. 임펄스 응답은 t = 0 또는 n = 0에서 임펄스 신호가 입력으로 인가될 때 이에 대응해서 나타나는 LTI 시스템의 출력으로 정의된다. 임펄스 응답은 시스템의 구성과 동적 특성에 관한 지식으로부터 결정되거나 시스템을 모를 경우에는 근사 임펄스를 입력에 인가하여 측정된다. 이산시간 시스템의 임펄스 응답은 입력을 δ[n]으로 설정하여 보편적으로 쉽게 얻는다. 이산시간 시스템의 임펄스 응답은 입력을 δ[n]으로 설정하여 보편적으로 쉽게 얻는다. 연속시간인 경우 임펄스 함수는 시간폭이 0이고 크기는 ∞이므로 실제적으로 얻을 수 없고 아주 짧은 시간폭과 아주 큰 크기를 갖는 펄스를 근사적으로 사용한다. 그러므로 임펄스 응답은 극히 짧은 시간폭과 큰 에너지를 가진 입력에 대응하는 시스템 동작이라고 해석할 수 있다. 임펄스 응답이 주어졌을 때 임의의 입력에 대응하는 출력은 입력을 시간이 이동된 임펄스의 가중합으로 표현함으로써 계산된다. 선형성과 시불변성에 의하면 시스템의 출력은 시간 이동된 임펄스 응답의 가중합이어야 한다. 이러한 가중합을 이산시간 시스템에서는 콘벌루션 합(convolution sum)이라 부르고 연속시간 시스템에서는 콘벌루션 적분(convolution integral)이라고 부른다. <br/>

&ensp;LTI 시스템의 입출력 동작을 설명할 두 번째 방법은 선형 상수계수 미분 또는 차분 방정식(linear constant-coefficient differential or difference equation)이다. 미분 방정식은 연속시간 시스템을 표현하기 위해 이용되고 차분 방정식은 이산시간 시스템을 표현하기 위해 이용된다. 시스템 표현의 세 번째 방법은 블록 다이어그램(block diagram)이다. 블록록 다이어그램이란 세 개의 기본 연산의 상호 접속으로 표현된 시스템을 말한다. 이산시간 시스템의 기본 연산은 스칼라 곱셈, 덧셈 및 시간이동(시간지연)이고 연속시간 시스템의 기본 연산은 스칼라 곱셈, 덧셈 및 적분이다. 시스템 표현의 마지막 방법은 상태변수(state variable)방법이다. 상태변수 방법은 시스템의 상태의 거동을 나타내는 연립 1계 미분 또는 차분 방정식과 시스템의 상태들을 시스템의 출력에 관련시키는 한 개의 출력 방정식으로 이루어진다. 시스템을 구성하는 에너지 저장소이자 기억소자와 관계되는 변수들의 집합을 시스템의 상태로 정의한다. <br/>


&ensp;2. Convolution Sum<br/>
======

&ensp;시간 이동된 임펄스의 가중합으로 임의의 신호를 표현하고 그 다음으로 표현된 신호를 LTI 시스템에 입력으로 인가하면 콘벌루션 합을 얻는다. 이와 비슷한 과정을 적용하여 연속시간 시스템에 대한 콘벌루션 적분을 얻는다.<br/>
&ensp;x[n]δ[n] = x[0]δ[n]<br/>
&ensp;x[n]δ[n-k] = x[k]δ[n-k]<br/>
&ensp;n은 시간 지표이고 x[n]은 전체 신호를 나타내고 x[k]는 시간 n = k에서의 신호값을 나타낸다. 시간 이동된 임펄스와 신호를 곱한 결과는 시간 이동된 임펄스와 그 임펄스가 발생된 시간에서의 신호값의 크기의 곱으로 나타난다. 다음과 같이 시간 이동된 임펄스의 가중합으로 신호 x[n]을 표현할 수 있다. <br/>
&ensp;x[n] = .....+ x[-2]δ[n + 2] + x[-1]δ[n + 1] + x[0]δ[n] + x[1]δ[n - 1]+ x[2]δ[n - 2] ...... =  $\sum_{k = -\infty }^{\infty }x[k]\delta [n-k]$
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-1.jpg" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-2.jpg" width="600"></p>
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
<p align="center"><img src="/assets/img/Singals and Systems/2장 LTI System/2-7.jpg" width="600"></p>


&ensp;3. 콘벌루션 합: 계산 과정<br/>
======

&ensp;