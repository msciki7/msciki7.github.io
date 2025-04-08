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
* 비주기 함수: 두 함수의 내적이 0이면 직교<br/>
* 주기 함수: 주기 T 또는 N인 함수들 간의 내적 조건<br/>
* 복소지수 함수 𝜙ₖ[n] = 𝑒^{𝑗kΩ₀n} 들이 서로 직교함을 증명<br/>
* 마찬가지로 연속 시간 복소지수 함수 𝜙ₖ(t) = 𝑒^{𝑗kω₀t}도 직교
<p align="center"><img src="/assets/img/Singals and Systems/3장 Fourier Representation of Singals and LTI Systems/3-1.JPEG" width="600"></p>


