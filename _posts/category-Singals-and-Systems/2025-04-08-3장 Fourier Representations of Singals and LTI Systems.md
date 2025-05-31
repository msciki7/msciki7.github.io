---
title: "3장 Fourier Representation of Signals and LTI Systems"
excerpt: "LTI 시스템의 직교 함수 집합을 이해한다."

wirter: sohee Kim
categories:
  - Signals and Systems
tags:
  - singal
  - system
toc: true
use_math: true 
toc_sticky: true

date: 2025-04-08
last_modified_at: 2025-04-08
---

Fourier's idea
======

&ensp;푸리에 표현의 5가지 경우:<br/>
* DTFS(이산시간 푸리에 급수)<br/>
* CTFS(연속시간 푸리에 급수)<br/>
* DTFT(이산시간 푸리에 급수)<br/>
* DFT(이산 푸리에 변환)<br/>

&ensp;주기적인 함수는 여러 개의 사인/코사인 함수를 더한 형태로 표현 가능 -> Fourier 급수<br/>

&ensp;비주기 함수는 사인/코사인의 적분으로 표현 가능 -> Fouier 변환<br/>

&ensp;Basis(기저 벡터)<br/>
* Orthogonal vector: 서로 직교(내적이 0)
* Orthonormal vector: 직교 + 크기가 1 (직교정규)
* 벡터공간에서 모든 벡터는 직교 기저 벡터의 가중합으로 표현 가능하다.<br/>
* $ a_{1}v_{1} + a_{2}v_{2} + \cdot \cdot \cdot + a_{n}v_{n} = 0$ 인 식을 만족할 때 선형종속(linearly dependent)이라고 하며 그렇지 않은 경우를 선형독립(linearly independent)이라고 한다. 위의 식을 만족하는 상수 값 $a_{1} = a_{2} = ...= a_{n} = 0$ 일 때  v1, v2, ..., vn이 선형독립이 된다. <br/>
* 벡터공간의 모든 벡터들을 V상의 벡터 v1,v2,...,vn의 선형결합으로 나타낼 수 있을 경우, 벡터 v1, v2, ..., vn이 벡터공간 V를 **생성**한다고 한다. $ a_{1}v_{1} + a_{2}v_{2} + \cdot \cdot \cdot + a_{n}v_{n} = v$ 가 되는 스칼라 a1, a2,..., an이 존재할 경우를 말한다.  <br/>

&ensp;LTI 시스템의 고유 함수 성질<br/>
* 입력: 𝑥(𝑡) = 𝜙(𝑡) = 𝑒^{𝑗𝜔𝑡} → 출력: 𝑦(𝑡) = H{𝜙(𝑡)} = λ𝜙(𝑡)<br/>
* 고유 함수(eigenfunction)는 지수함수 𝑒^{𝑗𝜔𝑡}, 고유값(eigenvalue, λ)은 주파수 응답 H(jω)<br/>
* 이산시간 시스템에서도 동일한 성질이 성립(DTFT)<br/>

&ensp;직교성(Orthogonality)<br/>
* 직교(orthogonal) : 서로 내적(inner product)이 0이다. -> 영향을 안 줌, 독립적인 방향<br/> 
* 비주기 함수: 두 함수의 내적이 0이면 직교<br/>
* 주기 함수: 주기 T 또는 N인 함수들 간의 내적 조건<br/>
* 복소지수 함수 𝜙ₖ[n] = 𝑒^{𝑗kΩ₀n} 들이 서로 직교함을 증명<br/>
* 마찬가지로 연속 시간 복소지수 함수 𝜙ₖ(t) = 𝑒^{𝑗kω₀t}도 직교
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-1.JPEG" width="600"></p>

&ensp;1_비주기 함수의 직교 조건<br/>
* 이산 시간 함수<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-2.png" width="600"></p>

* 연속 시간 함수<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-3.png" width="600"></p>

&ensp;-> 두 함수가 무한한 시간 축에서 내적이 0이면 직교<br/>

&ensp;2_주기 함수의 직교 조건<br/>
* 연속 시간(주기 T)<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-4.png" width="600"></p>

* 이산 시간(주기 N)<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-5.png" width="600"></p>

&ensp;-> 주기 N, T 구간만 계산해도 직교 여부 판단 가능<br/>

&ensp;예) 이산 지수 함수의 직교성 증명<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-6.png" width="600"></p>

&ensp;예) 연속 복소 지수 함수의 직교성 증명<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-7.png" width="600"></p>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-8.png" width="600"></p>

1\. Introduce
======

&ensp;신호가 선형 시스템에 입력된다면 시스템의 주파수 응답은 각 복소 지수 항에 독립적으로 적용되며 이들은 다시 합쳐져 출력 신호(output signal)를 형성한다. <br/>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-9.png" width="600"></p>

&ensp;1_푸리에 급수 정의<br/>


&ensp;주기 신호는 복소 지수 함수의 가중합으로 표현될 수 있다. 이러한 가중합을 통해 입력 신호와 출력 신호가 같은 주기를 갖고 동일한 주파수 성분으로 구성된다. 이 특성은 시스템이 주파수 성분을 그대로 유지하며 각 성분에 대해 스칼라 계수만 곱해주는 형태로 작동한다는 것을 의미한다.<br/>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-10.png" width="600"></p>

* 이때 $v_k{t}$ 는 보통 $e^{jkw_{0} t}$ 또는 $cos(kw_{0}t)$ , $sin(kw_{0}t)$ <br/>
* 계수 $F_{k}$ 는 f(t)와 기지 함수 $v_{k}(t)$ 사이의 내적<br/>

2\. 복소 정현파 함수와 LTI 시스템의 주파수 응답(Complex Sinusoids and Frequency of LTI Systems)
======

&ensp;임펄스 응답 h[n]과 단위 진폭 복소 정현파 함수 입력 $ x[n] = e^{j\Omega n}$ 을 갖는 이산시간 LTI 시스템을 고려한다. 출력은 다음과 같다.<br/>

&ensp; $ y[n] = \sum_{k= -\infty }^{\infty }h[k]x[n-k] = \sum_{k= -\infty }^{\infty }h[k]e^{j\Omega (n-k)}$ <br/>

&ensp;합으로부터 $e^{j\Omega n}$ 을 분리하여 다음을 구한다.<br/>

&ensp; $y[n] = e^{j\Omega n}\sum_{k= -\infty }^{\infty }h[k]e^{-j\Omega k}=H(e^{j\Omega })e^{j\Omega n}$<br/>

&ensp;여기서 $H(e^{j\Omega})$ 는 다음과 같이 정의된다.<br/>

$H(e^{j\Omega }) = \sum_{k =-\infty }^{\infty }h[k]e^{-j\Omega k}$ <br/>

&ensp;연속시간 LTI 시스템에 대해서도 유사한 결과가 얻어진다. 연속시간 LTI 시스템의 임펄스 응답 h(t) 그리고 입력을 $x(t) = e^{jwt}$ 라고 하자. 그때 콘벌루션 적분에 의한 출력은 다음과 같다. <br/> 

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-14.png" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-22.JPEG" width="600"></p>

&ensp;여기서 H(jw)는 다음과 같이 정의한다.<br/>

$H(jw) = \int_{-\infty }^{\infty } h(\tau )e^{-jw\tau }d\tau $ <br/>

&ensp;정현파 정상 상태 응답의 직관적인 해석은 복소값 주파수 응답 연속시간를 복소 형태로 표기함으로써 구해진다. 만약 c = a+jb가 복소수하면 그때 복소 형태로 C를 다음과 같이 쓸 수 있다.
&ensp;|H(jw)|는 시스템의 크기 응답이고 arg{ {H(jw)} }는 시스템의 위상 응답이다.<br/>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-23.png" width="600"></p>

&ensp;그러므로 시스템은 입력의 잔폭을 |H(jw)|배로 증가시키고 입력의 위상을 $arg\{H(jw)\}$만큼 변형시킨다. <br/>

&ensp;이산시간 시스템 예: <br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-11.png" width="600"></p>

&ensp;이산 LTI 시스템에 $e^{j\Omega n}$ 넣으면 출력은 같은 형태 X $H(e^{j\Omega })e^{j\Omega n}$ <br/>

&ensp;연속시간 시스템도 동일 :

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-12.png" width="600"></p>

&ensp;즉 복소 지수 함수는 LTI 시스템의 고유 함수, 시스템의 주파수 응답 = 고유값<br/>

&ensp;복소 지수들의 가중합 표현<br/>

&ensp;신호 x[n]이 여러 복소 지수 성분의 합으로 표현될 수 있다면 <br/>
$x[n] = \sum_{k= 0}^{N-1} A[k]e^{jw_{k}n}$​ <br/>

&ensp;이 시스템의 통과한 출력 y[n]도 다음과 같은 방식으로 표현<br/>

$y[n] = \sum_{k =0}^{N-1}H(e^{jw_{k}})A[k]e^{jw_{k}n}$ <br/>

&ensp;즉 입력 성분마다 주파수 응답 $H(e^{jw_{k}})$ 이 곱해져 출력에 반영된다. <br/>


3\. Fourier Representations for Four Classes of singals
======

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-13.png" width="600"></p>

&ensp;서로 다른 종류의 적용이 가능한 4종류의 푸리에 표현이 존재한다. 이들 4종류는 신호의 주기성과 시간의 연속성 또는 불연속성에 의해서 정의된다. 푸리에 급수(FS)는 연속시간 주기 신호에 적용되며 이산시간 푸리에 급수(DTFS)는 이산시간 주기 신호에 적용된다. 비주기 신호는 푸리에 변환 표현을 갖는다. 푸리에 변환(FT)은 연속시간 비주기 신호에 적용된다. 이산시간 푸리에 변환(DTFT)은 이산시간 비주기 신호에 적용된다. <br/>

* 주기적 신호는 Fourier 급수를 사용한다.<br/>
* 비주기적 신호는 Fourier 변환을 사용한다.<br/>

* DTFS(Discrete-Time Fourier Series): 이산 시간 주기 신호
* DTFT(Discrete-Time Fourier Transform): 이산 시간 비주기 신호

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-15.png" width="600"></p>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-16.png" width="600"></p>

&ensp;1_Periodic Singals<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-17.png" width="600"></p>

&ensp;중첩에서 k번째 정현파 함수의 주파수는 $kw_{o}$ 이다. 이러한 정현파 함수의 각각의 공통 주기 N를 갖는다. <br/>

&ensp;2_Non-periodic Singals<br/>
&ensp;주기 신호와는 달리 비주기 신호를 표현하는 정현파 함수들의 주기에 대한 제한은 없다. 그러므로 푸리에 변환 표현은 연속적인 주파수값을 갖는 복소 정현파 함수를 사용한다. 연속시간 비주기 신호는 복소 정현파 함수들의 가중된 적분으로 표현되며 여기서 적분 변수는 신호의 주파수이다. FT에서 연속시간 정현파 함수가 연속시간 비주기 신호를 표현하기 위하여 사용하는 데 반하여 DTFT에서는 이산시간 정현파 함수가 이산시간 비주기 신호를 표현하기 위하여 사용된다. 구별되는 주파수를 갖는 연속시간 정현파 함수는 서로 구별되며 따라서 FT는 범위 $-\infty$ 에서 $\infty$ 의 정현파 주파수와 연관된다. <br/>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-20.png" width="600"></p>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-21.png" width="600"></p>

&ensp;정리<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-19.png" width="600"></p>

4\. 이산시간 주기 신호: 이산시간 푸리에 급수(DTFS)
======

&ensp;기본 주기 N과 기본 주파수 
$\Omega _{o} = 2\Pi /N$ 

를 갖는 주기 신호 x[n]에 대한 DTFS 표현은 다음과 같이 주어진다.<br/>

&ensp;$x[n] = \sum_{k = 0}^{N-1}X[k]e^{jk\Omega _{o}n}$ <br/>

&ensp;여기서 X[k]의 정의는 <br/>

&ensp;$X[k] = \frac{1}{N}\sum_{n=0}^{N-1}x[n]e^{-jk\Omega _{o}n}$ <br/>

&ensp;이며, 신호 x[n]의 DTFS 계수이다. x[n]과 X[k]를 DTFS쌍이라고 하고 이 관계를 <br/>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-18.png" width="600"></p>

&ensp;X[k] 또는 x[n]은 신호에 대한 완전한 표현을 제공한다. DTFS 계수 X[k]는 x[n]에 대한 주파수 영역 표현이라고도 불린다. 왜냐하면 각 계수는 서로 다른 주파수의 복소 정현파 함수와 관계되기 때문이다. 변수 k는 X[k]를 갖는 정현파 함수의 주파수를 결정한다. 그래서 X[k]는 주파수의 함수이다. <br/>

* 문제 1
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-24.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-25.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-26.JPEG" width="600"></p>

* 문제 2
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-27.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-28.JPEG" width="600"></p>

* 문제3
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-29.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-30.JPEG" width="600"></p>

* 문제 4
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-31.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-32.JPEG" width="600"></p>

* 문제 5
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-33.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-34.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-35.JPEG" width="600"></p>

* 문제 6
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-36.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-37.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-38.JPEG" width="600"></p>


5\. 연속시간 주기 신호: 푸리에 급수(FS)
======

&ensp;모든 연속시간 주기 함수 x(t)는 기저 주기 함수들(복소 지수 $e^{-jk\omega _{o}t}$ ) 의 가중합으로 표현 가능하다. 

* 주기적인 아날로그 신호 x(t)는 복소지수 $e^{-jk\omega _{o}t}$ 들의 조합으로 표현할 수 있고 각각의 주파수 성분 $k\omega _{o}$ 에 대응하는 계수 X[k]가 존재한다.

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-39.png" width="600"></p>

&ensp;연속시간 주기 신호는 FS로 표현된다. 기본 주기 T와 기본 주파수 
$\omega _{o} = 2\Pi /T$ 를 갖는 신호 x(t)의 FS는 다음과 같다. <br/>

&ensp;$x(t) = \sum_{k = -\infty }^{\infty }X[k]e^{jk\omega _{o}t}$ <br/>

* 주기적 연속시간 신호 x(t)를 기본 주파수 $\omega _{o} = 2\Pi /T$ 의 정수배 복소지수로 구성
* X[k] : 각 주파수 성분에 해당하는 푸리에 계수
* x(t) : 실수이거나 복소수일 수 있음
* 이 합은 신호의 스펙트럼 재조합

&ensp;$X[k] = \frac{1}{T}\int_{0}^{T}x(t)e^{-jk\omega _{o}t}dt$ <br/>
* 주기 T 내에서 x(t)와 $e^{-jk\omega _{o}t}$ 의 내적
* 이 수식은 X[k]를 구하는 방법이자 직교성의 결과

* 문제 7
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-40.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-41.JPEG" width="600"></p>

* 문제 8
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-42.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-43.JPEG" width="600"></p>

* 문제 9
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-44.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-45.JPEG" width="600"></p>

* 문제 10
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-46.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-47.JPEG" width="600"></p>

* 문제 11
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-48.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-49.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-50.JPEG" width="600"></p>


&ensp;푸리에 급수의 또 다른 표현 방식은 삼각형 푸리에 급수(Trigonometric Fourier Series)이다. 특히 사각파처럼 짝대칭이 없는 실수 신호에서 유용하게 사용된다.<br/>

&ensp;지수형 푸리에 급수 (기존 표현)<br/>
&ensp;$ x(t) = \sum_{k=-\infty }^{\infty }X[k]e^{jkw_{o}t}$

&ensp;삼각형(삼각함수) 표현: Trigonometric FS<br/>
&ensp;$ x(t) = B[0] + \sum_{k = 1}^{\infty }(B[k]cos(kw_{O}t) + A[k]sin(kw_{o}t))$
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-51.png" width="600"></p>


* cos, sin 항의 진폭만 계산
* 복소수 표현이 필요 없음
* 특히 x(t)가 실수함수일 때 유용

&ensp;계수 계산 방법<br/>
* $B[0] = X[0] = \frac{1}{T}\int_{0}^{T}x(t)dt$
* $B[k] = \frac{2}{T}\int_{0}^{T}x(t)cos(kw_{o}t)dt$
* $A[k] = \frac{2}{T}\int_{0}^{T}sin(kw_{o}t)dt$

&ensp;복소수 FS와 삼각형 FS의 관계<br/>
* B[k] = X[k] + X[-k] (k != 0)
* A[k] = j(X[k] - X[-k]) (k != 0)

&ensp;사각파의 특별한 경우<br/>
&ensp;문제 3.13 
&ensp;$X[k] = \frac{sin(k2\Pi T_{o}/T)}{k\Pi }$ -> 우함수
* A[k] = 0
* B[k] = X[k] + X[-k] = 2X[k], k != 0
* $B[0] = X[0] = 2T_{o}/T$ , k = 0
* $x(t) = \sum_{k = 0}^{\infty }B[k]cos(kw_{o}t)$

* 문제 12
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-52.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-53.JPEG" width="600"></p>

6\. 이산시간 비주기 신호: 이산시간 푸리에 변환(DTFTS)
======

&ensp;DTFT는 이산시간 비주기 신호를 복소 정현파 함수의 중첩으로 표현하기 위해 사용된다. DTFT는 범위 $ -\Pi \leq \Omega \leq \Pi $ 의 주파수의 연속을 포함한다. <br/>

1. DTFT 정의
&ensp;$X(e^{j\Omega }) = \sum_{n = -\infty }^{\infty }x[n]e^{-j\Omega n}$ <br/>

* 이것은 시간영역의 이산신호 x[n]를 주파수 영역의 연속 주기 함수 $X(e^{j\Omega })$ 로 변환하는 공식

* 이산 신호 -> 주파수축에서 2π 주기적인 연속 함수
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-54.png" width="600"></p>


2. 역확산 공식(IDTFT)
&ensp;$x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\Omega}) e^{j\Omega n} \, d\Omega$  <br/>
* 주파수 영역의 함수로부터 원래의 x[n]을 복원하는 공식
* 푸리에 급수와 유사하지만 여긴 적분이 포함되어 있음 -> 비주기성

3. 왜 $X(e^{j\Omega })$ 는 2π 주기 함수인가?
&ensp;푸리에 변환 결과인 $X(e^{j\Omega })$ 는 다음과 같은 성질을 가짐 : <br/>
&ensp;$X(e^{j\Omega}) = X(e^{j(\Omega + 2\pi)}$ <br/>
* 이건 지수함수 $e^{j\Omega n}$ 이 2π 주기이기 때문에 자동으로 생긴다.
* 따라서 DTFT는 주파수축이 무한대가 아니라 [-π,π] 구간이면 충분

4. DTFT가 존재하려면? (조건)
&ensp;$\sum_{n=-\infty}^{\infty} |x[n]| < \infty$ <br/>
* 절대수렴해야 한다.
* 이는 푸리에 변환이 수학적으로 유효하려면 반드시 만족해야 할 조건이다.

&ensp;또는 에너지 기준:<br/>
&ensp;$\sum_{n=-\infty}^{\infty} |x[n]|^2 < \infty$ <br/>
* 이건 유한 에너지 신호에 대한 기준
* 이 경우에도 DTFT는 존재

&ensp;Parseval’s Theorem <br/>
&ensp;$\sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\Omega})|^2 \, d\Omega$ <br/>
* 시간 영역에서의 에너지 = 주파수 영역에서의 에너지
* 신호의 총 에너지는 DTFT의 제곱 적분값과 동일
* 에너지 보존 법칙이라고 보면 된다. 

* 문제 13
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-55.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-56.JPEG" width="600"></p>

* 문제 14
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-57.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-58.JPEG" width="600"></p>

* 문제 15
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-59.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-60.JPEG" width="600"></p>

* 문제 16
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-61.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-62.JPEG" width="600"></p>

* 문제 17
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-63.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-64.JPEG" width="600"></p>

* 문제 18
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-65.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-66.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-67.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-68.JPEG" width="600"></p>

7\. 연속시간 비주기 신호: 푸리에 변환
======

&ensp;전체 구조<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-69.png" width="600"></p>

* 시간 영역 x(t): 연속시간, 비주기 신호
* 주차수 영역 X(jw): 연속 주파수 성분의 스펙트럼
* 변환 방향: 푸리에 변환(CTFT)
* 역변환: inverse CTFT

&ensp;CTFT 정의<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-70.png" width="600"></p>

* X(jw): 주파수 영역에서의 복소수 함수
* $w = 2\Pi f$ : 각 주파수 (rad/s)
* 이 수식은 시간 영역의 함수 x(t)를 주파수 영역으로 변환하는 공식

&ensp;Iverse CTFT (역변환)<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-71.png" width="600"></p>

* 주파수 도메인의 X(jw)로부터 원래의 시간 신호 x(t)를 복원하는 식
* 앞의 CTFT와 복소지수의 부호가 반대이며 보정 계수 $1/2\Pi$ 가 있음

&ensp;푸리에 쌍 요약<br/>
* x(t) <-> X(jw)
* CTFT: 시간 -> 주파수
* Inverse CTFT: 주파수 -> 시간

&ensp;존재 조건 (Fourier Transform 이 존재하기 위한 조건)<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-71.png" width="600"></p>

&ensp;즉 시간 영역 함수 x(t)가 절대적 적분 가능해야 푸리에 변환이 정의된다. <br/>
* 신호가 무한 에너지는 가질 수 있지만 전체 면적은 유한해야 한다. 

&ensp;요약<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-73.png" width="600"></p>


* 문제 19
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-74.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-75.JPEG" width="600"></p>

* 문제 20
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-76.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-77.JPEG" width="600"></p>

* 문제 21
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-78.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-79.JPEG" width="600"></p>

* 문제 22, 23
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-80.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-81.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-82.JPEG" width="600"></p>

9\. 선형성과 대칭성(Linearity and Symmetry Properies of FT)
======

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-83.png" width="600"></p>

&ensp;선형성(Linearity)<br/>
&ensp;푸리에 변환(FT, CTFT, DTFT, DTFS, etc)은 선형 연산이다. 시간 영역에서 선형 결합한 함수는 주파수 영역에서도 선형 결합이 된다.<br/>
&ensp;$z(t)=ax(t)+by(t) -> Z(jω)=aX(jω)+bY(jω)$ <br/>

&ensp;위 식은 CTFT 기준이며, 다른 모든 푸리에 계열에서도 동일하게 적용된다. 선형성은 이미 알고 있는 신호 표현의 합으로 구성된 신호의 푸리에 표현을 구하기 위해 사용된다.<br/>

* 문제 24
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-84.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-85.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-86.JPEG" width="600"></p>

1_Symmetry Properties: Real and Imaginary Signals
------

1. 핵심 개념: 실수 신호 x(t)의 대칭성
&ensp;푸리에 변환 정의는 다음과 같다<br/>
&ensp;$X(jw) = \int_{-\infty }^{\infty }x(t)e^{-jwt}dt$ <br/>
&ensp;이를 복소컬레 취하면:<br/>
&ensp;$ X^{*}(jw) = (\int_{-\infty }^{\infty }x(t)e^{-jwt}dt)^{*} = \int_{-\infty }^{\infty }x^{*}(t)e^{jwt}dt$ <br/>

2. 실수(real) 신호의 대칭성
&ensp;실수 함수하면:<br/>
&ensp;$ X^{*}(jw) = x(t) -> X^{*}(jw) = \int x(t)e^{jwt}dt = X(-jw)$ <br/>
&ensp;즉<br/>
&ensp;$X^{*}(jw) = X(-jw)$ (복소컬레 대칭, conjugate symmetry)<br/>

&ensp;크기: $|X(jw)| = |X(-jw)| -> even(짝함수)<br/>
&ensp;위상: $arg X(jw) = - arg X(-jw)$ -> odd(홀함수)<br/>

&ensp;💡 예시<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-87.png" width="600"></p>

3. DTFS(이산 푸리에 급수)에서도 동일
&ensp;DTFS정의:<br/>
&ensp;$X[k] = \frac{1}{N}\sum_{n =0}^{N-1}x[n]e^{-jk\Omega _{0}n}$ <br/>
&ensp;만약 x[n]이 실수면: <br/>
&ensp;$X^{*}[k] = X[-k] = X[N-k]$ (복소컬레 대칭)<br/>

4. 만약 x(t)가 허수 신호라면?
&ensp;$x(t)^{*} = -x(t) -> X^{*}(jw) = -X(-jw)$ <br/>
&ensp;이건 반대칭 성질(odd symmetry)이라고 부른다.<br/>

&ensp;크기: $|X(jw)| = |X(-jw)|$ -> even<br/>
&ensp;위상: $arg X(jw) = arg X(-jw)$ -> even<br/>

&ensp;💡 예시<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-88.png" width="600"></p>

2_Symmetry Propeties: Even/Odd signals
------

&ensp;💡 먼저, 복습! 푸리에 변환이란?<br/>
&ensp;푸리에 변환은 시간 영역의 신호 x(t)를 주파수 영역으로 바꾸는 도구이다. <br/>
&ensp;$X(jw) = \int_{-\infty }^{\infty }x(t)e^{-jwt}dt$ <br/>

* x(t): 시간에 따라 바뀌는 신호
* X(jw): 이 신호가 주파수 영역에서 얼마나 각 주파수 성분을 포함하는지 보여주는 표현

&ensp;대칭성(Symmetry) 성질: 짝수(even)/홀수(odd) 신호의 경우<br/>

1. x(t)가 **실수(real)**이고 **짝수 함수(even)**일 때
&ensp;짝수 함수란? -> x(-t) = x(t) <br/>

&ensp;푸리에 변환 결과: X(jw)는 실수(real)함수가 된다.<br/>
&ensp;왜냐하면 계산하면 <br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-89.png" width="600"></p>
&ensp;-> 실수 값이면 컬레가 같다. 그래서 실수 + 짝수 신호는 푸리에 변환 결과도 실수 함수가 된다. <br/>

2. x(t)가 **실수이고 홀수 함수(odd)**일 때
&ensp;홀수 함수란? -> x(-t) = -x(t) <br/>

&ensp;푸리에 변환 결과: X(jw)는 순허수(imaginary)함수가 된다.<br/>
&ensp;왜냐하면 푸리에 변환을 수행하면 다음과 같은 대칭성을 갖기 때문이다.<br/>
&ensp;$X^{*}(jw) = -X(jw)$<br/>
&ensp;-> 실수 부분이 0이고 허수만 남는 구조이다.<br/>

&ensp;🎯 요약<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-90.png" width="600"></p>


10\. Convolution Property(컨볼루션 성질)
======

Convolution of non-periodic signals(비주기 신호의 컨볼루션)
------

&ensp;🔶 요약: 컨볼루션 <-> 곱셈<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-91.png" width="600"></p>

&ensp;두 개의 비주기 연속시간 신호들 x(t)와 h(t)의 콘볼루션이다.<br/>
&ensp;즉 시간 영역에서의 컨볼루션 연산은 주파수 영역에서의 곱셈으로 바뀌고 반대로 주파수 영역에서의 곱셈은 시간 영역의 컨볼루션으로 바뀐다.<br/>

&ensp;🔍 자세한 수식 풀이<br/>

1. 시간 영역: 컨볼루션 정의
&ensp;$y(t) = h(t) * x(t) = \int_{-\infty}^{\infty} h(\tau)\, x(t - \tau)\, d\tau$ <br/>

&ensp;이는 h(t)필터가 x(t) 신호에 영향을 주는 방식(예: 시스템 응답)을 설명하는 기본 연산이다.<br/>

2. 주파수 영역으로 푸리에 변환
&ensp;푸리에 변환의 기본 성질:<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-92.png" width="600"></p>

3. 시간 영역의 컨볼루션을 푸리에 변환하면?
&ensp;$y(t) = h(t)*x(t) = \int_{-\infty }^{\infty }h(\tau )x(t-\tau )d\tau $ <br/>
&ensp;이걸 주파수 영역으로 변환하면: <br/>
&ensp;$Y(jw) = H(jw)X(jw)$ <br/>

&ensp;📌 결론: 컨볼루션 정리<br/>
&ensp;$y(t) = h(t)\ast x(t) \overset{FT}{\rightarrow} Y(jw) = H(jw)X(jw)$ <br/>

&ensp;시간 영역의 곱셈이 어려우면 -> 주파수 영역에서 곱셈으로 계산하자!<br/>

* 문제 25
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-93.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-94.JPEG" width="600"></p>

* 문제 26
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-95.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-96.JPEG" width="600"></p>


Filtering
------

1. 필터가 뭐야?
&ensp;필터는 마치 소리 골라내는 체 같은 거다. 우리가 듣는 음악에는 높은 소리(고음), 낮은 소리(저음), 중간 소리(중음)가 섞여 있다. 필터는 이 소리들 중에서 특정한 소리만 통과시키고 나머지는 막아주는 역할을 한다. 

&ensp;🎵 예시<br/>
* 엄가가 “TV 소리 너무 크다~!” 하면, 소리 중에서 시끄러운 고음만 줄이고 싶을 때, <br/>
  - 👉 Low Pass Filter (LPF): 낮은 소리만 통과!
* 친구가 "베이스만 더 듣고 싶어!" 하면,
  - 👉 High Pass Filter (HPF): 높은 소리만 통과!
* 특정한 중간 소리만 듣고 싶으면
  - 👉 Band Pass Filter (BPF): 중간 대역 소리만 통과!

2. 그림 설명
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-97.png" width="600"></p>

* LPF(Low Pass): 낮은 주파수(소리)는 통과, 높은 주파수는 잘라냄
* HPF(High Pass): 낮은 주파수는 자르고, 높은 주파수는 통과
* BPF(Band Pass): 중간 주파수만 통과하고 양끝은 자름

3. dB 단위란?
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-98.png" width="600"></p>

* 왼쪽 그래프는 실제 크기, 오른쪽은 dB로 표현한 그래프이다.
* 예를 들어 크기 1의 소리는 $20log_{10}(1) = 0 dB$
* 크기가 1/√2 일 때는 $20log_{10}(1/ √2) = -3 dB$ -> 여기서부터 소리를 지르기 시작한다.
&ensp;그래서 이걸 컷오프 주파수(cutoff frequency)라고 부른다. <br/>

* 문제 27
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-99.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-100.JPEG" width="600"></p>

* 문제 28
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-101.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-102.JPEG" width="600"></p>

Convolution of periodic signals:Cyclic convolution(주기 신호의 컨볼루션)
------

&ensp;convolution<br/>
* 두 신호가 있을 때
* 하나의 입력신호 x(t), 하나는 시스템의 반응 z(t)
* 이 둘은 합성(convolution)하면 출력신호 y(t)가 된다.

&ensp;주기적이란?<br/>
&ensp;예를 들어 x(t)가 1초마다 반복되고 z(t)도 똑같이 반복된다면 이걸 그냥 쭉 합성하면 계산이 너무 커진다. <br/>

&ensp;그래서 "한 주기만" 합성하면 된다.<br/> -> 이걸 **Cyclic Convolution(순환 합성)** 이라고 한다. <br/>

&ensp;공식<br/>
&ensp;$y(t) = x(t) \otimes z(t) = \int_{0}^{T} x(\tau)\, z(t - \tau)\, d\tau$ <br/>
* 이 수식은 한 주기만 가지고 합성한다는 걸 의미한다.
* 범위가 0부터 T까지인 게 포인터이다. (한 주기만 계산)

&ensp;푸리에 급수로 바꾸면 훨씬 쉬워짐<br/>
&ensp;주기적인 신호 -> 푸리에 급수(FS)로 바꿔준다. 그러면 합성도 그냥 곱하기로 끝남<br/>
&ensp;결과 공식: <br/>
&ensp;$Y[k] = TX[k]Z[k]$ <br/>
* X[k],Z[k]는 각각 x(t), z(t)의 푸리에 계수
* Y[k]: 합성 결과의 푸리에 계수
* 그냥 계수끼리 곱하고 T만 곱해주면 끝

&ensp;컨볼루션 성질<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-103.png" width="600"></p>

* 문제 29
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-104.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-105.JPEG" width="600"></p>


11\. 미분과 적분의 성질
======

1_시간 영역에서 미분 -> 주파수에서의 곱셈
------

&ensp;목표: 시간 영역에서 미분하는 건 주파수 영역에서 jw를 곱하는 것과 같다.<br/>

1. 기본 푸리에 변환 정의 
&ensp;푸리에 변환: <br/>
&ensp;$x(t) \overset{Ft}{\leftarrow}\to X(jw)$ <br/>
&ensp;즉 x(t)가 주어지면 X(jw)로 바꿀 수 있고 그 반대도 가능하다. <br/>

2. 시간에서 미분하면?
&ensp;시간에서 x(t)를 미분하면 이렇게 된다.: <br/>
&ensp;$\frac{d}{dt}x(t)\overset{Ft}{\leftarrow}\rightarrow jwX(jw)$ <br/>
&ensp;즉 미분하는 것은 주파수 스펙트럼에 jw를 곱하는 것과 같다. <br/>
&ensp;미분하면 고주파가 강조된다. <br/>

&ensp;시간 영역에서 비주기 신호 x(t)를 미분하였을 대 효과에 대해 생각해보면: <br/>
 
&ensp;$x(t) = \frac{1}{2\Pi }\int_{-\infty }^{\infty }X(jw)e^{jwt}dw$ <br/>
&ensp;이 식의 양변을 t에 대하여 미분하면 <br/>
&ensp;$\frac{d}{dt}x(t) = \frac{1}{2\Pi }\int_{-\infty }^{\infty }X(jw)e^{jwt}dw$ <br/>

&ensp;즉 시간 영역에서의 미분은 주파수 영역에서 jw를 곱하는 것에 해당한다. <br/>

* 문제 30
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-106.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-107.JPEG" width="600"></p>

* 문제 31
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-108.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-109.JPEG" width="600"></p>

* 문제 32
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-110.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-111.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-112.JPEG" width="600"></p>

&ensp;정리: 시간 미분 -> 주파수 곱셈<br/>
* g(t)를 시간 t로 미분하면 -> 푸리에 변환에서는 주파수에 곱하기 (jw)

&ensp;$\frac{d}{dt}g(t) \leftarrow \overset{FT}{\rightarrow}jwG(jw)$ <br/>

3. 주파수 미분 -> 시간 곱셈

* G(jw)를 주파수 w로 미분하면 -> 시간 신호에 -jt를 곱한 것과 같다.

&ensp;$-jtg(t)\leftarrow \overset{FT}{\rightarrow}\frac{d}{dw}G(jw)$ <br/>

* 문제 33
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-113.JPEG" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-114.JPEG" width="600"></p>

