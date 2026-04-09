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
* C = G + B
* M = R + B
* Y = R + G

&ensp;즉 CMY는 RGB의 반대편 개념이다.<br/>
&ensp;또 black balancing도 나온다.<br/>
&ensp;이건 감산형 기본색을 조정해서 검정이 다른 색으로 치우치치 않도록 맞추는 것이다.<br/>


# 색도도(chromaticity)와 color gamut

&ensp;1. chromaticity란?<br/>
&ensp;색의 세 요소 중에서<br/>
* Hue(색조)
* Saturation(채도)

&ensp;를 together 묶은 개념이 chromaticity(색도)다.<br/>

&ensp;즉 chromaticity는 이 색이 어떤 계열 색이고 얼마나 순수한가를 나타낸다.<br/>
&ensp;밝기(Intensity)는 별도로 생각한다.<br/>

&ensp;2. x, y, z 관계<br/>

$$x = \frac{X}{X + Y + Z}, y = \frac{Y}{X + Y + Z}, z = \frac{Z}{X + Y + Z}$$

&ensp;그리고 $x + y + z = 1$ 이므로 $z = 1 - x - y$ 가 된다.<br/>

&ensp;즉 실제로는 x와 y만 알면 z는 자동으로 결정된다. 그래서 색도도는 2차원 평면으로 그릴 수 있다.<br/>

&ensp;3. CIE Chromaticity Diagram<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-5.png" width="600"></p>

* 바깥 경계 쪽일수록 순수한 스펙트럼 색
* 안쪽일수록 여러 색이 섞인 색
* 가운데 근처는 흰색 계열

&ensp;4. color gamut<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-6.png" width="600"></p>

* RGB 모니터가 표현 가능한 색 영역
* 고급 프린터가 표현 가능한 색 영역

&ensp;이 서로 다르다.<br/>
&ensp;즉 어떤 색은 모니터에서는 표현되지만 프린터에서는 잘 안 되고 반대로 인쇄에 강한 영역이 따로 있을 수 있다.<br/>

&ensp;gamut은 장치가 실제로 낼 수 있는 색의 영토라고 생각하면 된다.<br/>

# HSI 색 공간

&ensp;1. HSI가 필요한 이유<br/>
&ensp;RGB는 장치 입장에서는 편하지만 사람이 색을 느끼고 방식과는 약간 다르다.<br/>

&ensp;사람은 보통 색을 생각할 때<br/>
* 무슨 색인가
* 얼마나 진한가
* 얼마나 밝은가

&ensp;로 구분한다.<br/>
&ensp;이 직관에 더 가까운 모델이 HSI이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-7.png" width="600"></p>

&ensp;2. H, S, I의 의미<br/>
&ensp;Hue(H)<br/>
&ensp;색조<br/>
&ensp;어떤 파장 계열의 색이 중심이 되는가를 나타낸다.<br/>
* R = 0.0
* G = 0.333
* B = 0.666

&ensp;처럼 각도로 표현할 수 있다.<br/>

&ensp;Saturation(S)<br/>
&ensp;채도<br/>
&ensp;색의 순도<br/>
* S = 0 이면 회색
* S = 1 이면 매우 진한 색

&ensp;Intensity(I)<br/>
&ensp;밝기<br/>
&ensp;전체 빛의 양이다.<br/>
* I = 0 이면 black
* I = 1 이면 white

&ensp;즉 HSI는 사람이 느끼는 색 개념과 더 가깝다.<br/>

&ensp;3. RGB → HSI 변환<br/>
&ensp;RGB를 HSI로 바꾸는 식<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-8.png" width="600"></p>

* I: RGB 평균으로 계산
* S: 최소값을 이용해 색의 순도를 계산
* H: 세 색의 상대적 관계로 각도를 계산

&ensp;HSI는 결국 RGB 값을 재해석해서 사람 친화적인 표현으로 옮긴 것이다.<br/>

&ensp;4. HSI -> RGB 변환<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-9.png" width="600"></p>

&ensp;Hue 영역을 세 구간으로 나눠서 계산한다.<br/>
* RG sector
* GB sector
* BR sector

&ensp;즉 생상각이 어느 구간에 있는지에 따라 RGB 성분 계산식이 달라진다.<br/>

# YCbCr와 다양한 색 공간 변환

&ensp;1. 왜 RGB 대신 YCbCr를 쓰는가<br/>
&ensp;영상 시스템에서는 저장/전송/압축을 위해 RGB 대신 YCbCr를 자주 쓴다.<br/>
&ensp;이유는 사람 눈이 밝기 변화에는 민감하고 색차에는 상대적으로 덜 민감하기 때문이다.<br/>
&ensp;그래서 밝기와 색차를 분리하면 압축 효율을 높이기 좋다.<br/>

&ensp;2. YCbCr의 의미<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap6/6-10.png" width="600"></p>

* Y: 밝기(luma)
* Cb: blue 차이 성분
* Cr: red 차이 성분

&ensp;밝기 Y는 RGB를 동일하게 더하는 게 아니라 사람 눈이 green에 더 민감하다는 점을 반영해 가중합으로 계산한다.<br/>

&ensp;또<br/>
* B−Y
* R−Y

&ensp;를 기반으로 색차 성분을 만든 뒤 Cb, Cr로 스케일링한다.<br/>

# 시간 해상도와 시간적 aliasing

&ensp;1. Temporal resolution<br/>
&ensp;예를 들어<br/>
* film: 24Hz
* TV: 30/25Hz → 60/50Hz

&ensp;즉 1초에 몇 장의 화면을 보여주는가가 시간 해상<br/>

&ensp;2. Temporal aliasing<br/>
&ensp;시간 해상도가 부족하면 움직이 이상하게 보인다.<br/>

# 화질 평가(Image Fidelity Criteria)

&ensp;영상처리에서는 필터링, 압축, 복원 같은 작업을 한 뒤 결과가 얼마나 좋은가를 수치로 평가해야 한다.<br/>
&ensp;그래서 다음과 같은 기준이 필요하다.<br/>
* image quality measurement
* processing system performance evluation

&ensp;좋은지 나쁜지를 느낌이 아니라 수치로 비교하려는 것이다.<br/>

&ensp;1. Mean Square Error<br/>
&ensp;원본 영상 u(m, n)과 처리 결과 u'(m, n)의 차이를 제곱해서 평균낸 값이다.<br/>

$$\sigma ^{2}_{ms} = \frac{1}{MN}\sum \sum (u(m, n) - u'(m, n))^2$$

&ensp;값이 작을수록 원본과 비슷하다.<br/>

&ensp;2. SNR<br/>
&ensp;신호 대 잡음비다.<br/>
&ensp;원래 신호의 에너지에 비해 오차가 얼마나 작은지를 보는 지표이다.<br/>
&ensp;값이 클수록 좋다.<br/>

&ensp;4. PSNR<br/>
&ensp;Peak signal-to-noise ratio다. 영상 품질 비교에서 아주 자주 쓰는 지표다.<br/>
&ensp;역시 일반적으로 값이 클수록 품질이 좋다고 본다.<br/>