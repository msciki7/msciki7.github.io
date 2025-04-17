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

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-14.png" width="600"></p>

&ensp;주기 신호는 복소 지수 함수의 가중합으로 표현될 수 있다. 이러한 가중합을 통해 입력 신호와 출력 신호가 같은 주기를 갖고 동일한 주파수 성분으로 구성된다. 이 특성은 시스템이 주파수 성분을 그대로 유지하며 각 성분에 대해 스칼라 계수만 곱해주는 형태로 작동한다는 것을 의미한다.<br/>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-10.png" width="600"></p>

* 이때 $v_k{t}$ 는 보통 $e^{jkw_{0} t}$ 또는 $cos(kw_{0}t)$ , $sin(kw_{0}t)$ <br/>
* 계수 $F_{k}$ 는 f(t)와 기지 함수 $v_{k}(t)$ 사이의 내적<br/>

2\. 복소 지수 함수와 LTI 시스템(Complex Sinusoids and LTI Systems)
======

&ensp;이산 시간 시스템에서 임퍽스 응답이 h[n]인 LTI 시스템의 출력 y[n]은 다음과 같이 정의된다.<br/>

&ensp; $y[n] = \sum_{k= -\infty }^{\infty }h[k]x[n-k]$ <br/>

&ensp;여기서 입력 x[n]이 복소 지수 함수 x[n] = $e^{jkwt}$ 인 경우 출력은 다음과 같다.<br/>

&ensp; $y[n] = H(e^{jkw})e^{jkwn}$<br/>

&ensp;이때 주파수 응답 $H(e^{jkw})$ 는 시스템의 임펄스 응답 h[n]을 통해 다음과 같이 정의된다.<br/>

&ensp; $H(e^{jkw}) = \sum_{k = -\infty }^{\infty }h[k]e^{-jwk}$ <br/>

&ensp;복소 지수 입력 $e^{jkwn}$ 은 LTI 시스템에 대해 고유 함수(eigenfunction)이다. 출력은 입력과 같은 형태를 가지고 스칼라 값 $H(e^{jw})$ 에 의해 크기 및 위상만 변한다. <br/>

&ensp;이산시간 시스템 예: 
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

* 주기적 신호는 Fourier 급수를 사용한다.<br/>
* 비주기적 신호는 Fourier 변환을 사용한다.<br/>

* DTFS(Discrete-Time Fourier Series): 이산 시간 주기 신호
* DTFT(Discrete-Time Fourier Transform): 이산 시간 비주기 신호

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-15.png" width="600"></p>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-16.png" width="600"></p>

&ensp;1_Periodic Singals<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-17.png" width="600"></p>

&ensp;DTFS의 주파수 인덱스도 주기적이다.<br/>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-18.png" width="600"></p>


&ensp;Fourier transform<br/>
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-19.png" width="600"></p>


&ensp;2_Non-periodic Singals<br/>
&ensp;주기 없는 신호들이 포함되며 이들을 표현하기 위해서는 푸리에 급수 대신 푸리에 변환을 사용한다. <br/>
* 푸리에 변환은 복소 지수 함수를 연속적인 주파수 스펙트럼으로 구성된 신호로 표현한다. 
* 주파수 축은 더 이상 이산적인 정수 배가 아니라 연속적인 값을 가진다. 

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-20.png" width="600"></p>

<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-21.png" width="600"></p>










