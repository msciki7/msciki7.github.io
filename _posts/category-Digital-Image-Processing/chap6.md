---
title: "Chap 6. Color"
excerpt: ""

wirter: sohee Kim
categories:
  - Digital Image Processing
tags:
  - 영상처리

toc: true
toc_sticky: true
math: true

date: 2026-03-31
last_modified_at: 2026-03-31
---

# 색의 기본 개념: 빛, 파장, 사람의 눈

&ensp;1. 색은 어디서 시작되는가<br/>
&ensp;흰빛을 프리즘에 통과시키면 흰색이 유지되는 것이 아니라, 보라에서 빨강까지 이어지는 연속적인 색 스펙트럼으로 분해된다. 즉 흰빛은 “색이 없는 빛”이 아니라 여러 파장의 빛이 섞인 결과다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-1.png" width="600"></p>

&ensp;2. 가시광선은 전자기 스펙트럼의 일부<br/>
&ensp;대략<br/>
* 자외선
* 가시광선
* 적외선

&ensp;중에서 사람이 보는 것은 중간의 가시광선 영역뿐이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-2.png" width="600"></p>

$$\lambda = \frac{c}{\nu }$$

* λ: 파장
* c: 빛의 속도
* ν: 주파수

&ensp;즉 파장과 주파수는 반비례한다. 파장이 짧을수록 주파수는 높다.<br/>

&ensp;3. 사람은 왜 RGB로 색을 느끼는가<br/>
&ensp;cones(원추세포)<br/>
* 65%: red 쪽에 민감
* 33%: green 쪽에 민감
* 2%: blue 쪽에 민감

# 색 해상도와 RGB / CMY 시스템

&ensp;1. Additive color system<br/>
&ensp;기본 색은<br/>
* Red
* Green
* Blue

&ensp;즉 RGB다.<br/>
&ensp;이건 빛을 직접 내는 시스템. 즉 emissive color에 해당한다.<br/>

&ensp;대표 예시는<br/>
* TV
* LCD
* 모니터

&ensp;같은 디스플레이다.<br/>

&ensp;가산 혼합에서는<br/>
* R + G = Yellow
* G + B = Cyan
* R + B = Magenta
* R + G + B = White

&ensp;가 된다.<br/>
&ensp;즉 빛은 더할수록 밝아지고, 세 기본색을 모두 합치면 흰색이 된다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-3.png" width="600"></p>

&ensp;2. Subtractive color system<br/>
&ensp;반대로 인쇄에서는 감산 색 시스템을 쓴다.<br/>
&ensp;기본 색은<br/>
* Cyan
* Magenta
* Yellow

&ensp;즉 CMY다.<br/>
&ensp;이건 반사형 색 시스템이다. 즉 빛을 직접 내는 게 아니라, 들어온 흰빛에서 일부 성분을 빼는 방식이다.<br/>
&ensp;예를 들어 cyan은 red를 포함하지 않는다. 즉 흰빛에서 red를 빼고 green + blue만 남긴 결과라고 볼 수 있다.<br/>
&ensp;즉 CMY는 RGB의 보색 관계다.<br/>

&ensp;3. RGB Color Space와 gamut<br/>
&ensp;gamut은 어떤 장치가 표현할 수 있는 색의 범위다. 즉 RGB라고 해서 모든 장치가 같은 색을 내는 건 아니다. 모니터마다, 프린터마다, 필름마다 표현 가능한 색 범위가 다르다.<br/>

&ensp;4. Trichromacy theory<br/>
&ensp;사람의 망막은 기본적으로 세 종류의 색 자극 조합으로 색을 인식하므로, 색은 결국 세 기본 자극값으로 표현할 수 있다.<br/>
&ensp;즉 특정 색을 만들기 위해 필요한 세 기본 자극량을 수치로 표현한 것이 XYZ 계열 개념이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-4.png" width="600"></p>

&ensp;white balancing<br/>
* 세 기본색 비율을 조정해서
* 색 치우침 없이
* 순수한 흰색처럼 보이게 만드는 것

&ensp;이게 화이트 밸런싱이다.<br/>

&ensp;5. Subtractive Color Space 자세히<br/>