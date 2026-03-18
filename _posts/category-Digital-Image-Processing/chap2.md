---
title: "Chap 2. Digital Image Fundamentals"
excerpt: ""

wirter: sohee Kim
categories:
  - Digital Image Processing
tags:
  - 영상처리

toc: true
toc_sticky: true
math: true

date: 2026-03-16
last_modified_at: 2026-03-16
---

# Human Eye

&ensp;1) 사람 눈의 기본 구조<br/>
&ensp;사람의 눈은 카메라처럼 빛을 받아 영상을 형성한다. 눈의 주요 구성요소로 각막(cornea), 공막(sclera), 맥락막(choroid), 망막(retina), 홍채(iris), 동공(pupil), 수정체(lens), 중심와(fovea), 시신경(optic nerve)를 설명한다. 특히 망막에는 빛을 감지하는 rod와 cone이 있다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-1.png" width="600"></p>

&ensp;2) Rod와 Cone<br/>
* Cone(추상세포): 색을 구분함, 중심와 쪽에 많음, 해상도가 좋음
* Rod(간상세포): 어두운 곳에서 민감함, 색 구분은 못함

&ensp;즉<br/>
* 밝은 때 + 색 인식 -> cone
* 어두울 때 + 밝기 감지 -> rod

&ensp;3) 중심와와 맹점<br/>
* 중심와(fovea): 시력이 가장 좋은 부분
* 맹점(blind spot): 수용기가 없는 부분이라 영상이 안 보이는 부분

&ensp;4) 밝기 인식 특성<br/>
&ensp;사람 눈을 밝기를 선형적으로 느끼지 않고 로그 함수처럼 느낀다. 그래서 실제 빛의 세기가 2배, 3배 늘어난다고 해서 밝기가 똑같이 2배, 3배로 느껴지지 않는다.<br/>

&ensp;5) HVS(Human Visual System)의 특징<br/>
&ensp;사람 시각계는<br/>
* 절대 밝기보다 상대적 차이(contrast) 에 민감하고 너무 높은 주팧수 세부 정보에는 둔감하며 경계(edge)부분을 더 또렷하게 느낀다.

&ensp;그래서 Mach band effect, simultaneous contrast, optical illusion 같은 현상이 생긴다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-2.png" width="600"></p>

# Temporal Properties of Vision 1 

&ensp;시간에 따라 변하는 빛에 눈이 어떻게 반응하는지 다룬다.<br/>
&ensp;핵심 주제<br/>
* Bloch Law
* Critical Fusion Frequency (CFF)
* Spatial vs. Temporal effects

&ensp;1) 왜 중요할까?<br/>
&ensp;이 내용은 그냥 생리학이 아니라<br/>
* 동영상 처리
* 디스플레이 설계
* 모니터 주사율
* TV 영상 표시

&ensp;같은 것들과 직접 연결된다.<br/>

&ensp;2) Bloch Law<br/>
&ensp;아주 짧은 시간 동안 강한 빛을 비추는 것과 조금 더 긴 시간 동안 약한 빛을 비추는 것이 **총 에너지(빛의 양)가 같으면 눈에는 비슷하게 느껴질 수 있다**는 뜻<br/>

&ensp;3) Critical duration<br/>
* 보통 조명에서는 약 30ms
* 더 어두운 환경에서는 30ms보다 더 길어짐

&ensp;즉 어더운 곳일수록 눈이 빛을 더 오래 모아서 인식하려고 한다고 이해한다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-3.png" width="600"></p>

&ensp;시험 포인트<br/>
* Bloch Law는 빛의 지속시간과 에너지의 관계
* 임계시간보다 짧은 경우, 눈은 둘을 잘 구분 못함
* 어두운 환경일수록 임계시간이 길다

&ensp;시간적 시각 특성의 핵심인 CFF(Critical Fusion Frequency)를 설명한다.<br/>

&ensp;1) CFF란?<br/>
&ensp;천천히 깜빡이는 빛은 깜빡깜빡 하는 것이 구별된다.<br/>
&ensp;그런데 깜빡이는 속도가 점점 빨라지면 어느 순간부터는 개별 깜빡임이 안 보이고 계속 켜져 있는 것처럼 느껴진다.<br/>
&ensp;그 경계가 바로 CFF이다.<br/>

&ensp;2) 수치<br/>
&ensp;약 50~60Hz<br/>

&ensp;즉 1초에 50~60번 이상 깜빡이면 사람 눈은 그걸 하나의 연속된 빛처럼 볼 가능성이 높다.<br/>

&ensp;3) 응용<br/>
* TV raster scan: 50/60Hz
* 컴퓨터 모니터: 60Hz 이상 refresh 권장

&ensp;즉 디스플레이가 너무 낮은 주사율이면 깜빡이는 것처럼 느껴질 수 있다.<br/>

&ensp;4) Spatial vs. Temporal Effects<br/>
&ensp;눈은 low spatial frequency보다 high spatial frequency field에서 더 민감하다<br/>

&ensp;핵심<br/>
* 깜빡임을 느끼는 정도는 패턴의 공간적 구조와도 관련된다.
* 화면에 넓게 퍼진 단순한 패턴과 세밀한 무늬가 있는 패턴은 같은 깜빡임이라도 다르게 느껴질 수 있다.

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-4.png" width="600"></p>

# Image sensing and acquisition

&ensp;영상은 물제에서 나오는 에너지를 센서가 받아서 생성한다.<br/>
&ensp;그 에너지는 두 가지 방식이 가능하다.<br/>
* 반사(reflected): 물체 표면에서 빛이 반사됨
* 투과(transmitted): 물체를 통과한 에너지를 측정함

&ensp;예시<br/>
* 일반 사진: 물체 표면에서 반사된 빛
* X-ray: 인체를 통과한 에너지

&ensp;영상은 눈으로 보는 가시광만이 아니라 센서가 받아들일 수 있는 에너지를 통해 만들어질 수 있다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-5.png" width="600"></p>

&ensp;CCD array<br/>
* CCD는 디지털 카메라에서 대표적인 센서
* 입력 빛을 일정 시간 동안 적분(integration)해서 신호를 모은다.
* 오래 적분하면 노이즈를 줄이는 데 도움이 된다.

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-6.png" width="600"></p>

# A simple image for formation model

&ensp;영상의 밝기값을 수학적으로 아주 기본적으로 표현하는 모델<br/>

$$f(x, y) = i(x, y)r(x, y)$$

* f(x, y): 최종 영상 밝기
* i(x, y): illumination, 조명
* r(x, y): reflectance, 반사율

&ensp;의미<br/>
&ensp;같은 물체라도<br/>
* 조명이 밝으면 밝게 보이고
* 조명이 어두우면 어둡게 보인다.

&ensp;또 같은 조명 아래에서도<br/>
* 흰 물제는 많이 반사하고
* 검은 물체는 적게 반사한다.

&ensp;영상의 밝기는 조명 x 반사율로 나타낸다.<br/>

&ensp;조건<br/>
* 0 < f(x, y) < ∞
* 0 < i(x, y) < ∞
* 0 < r(x, y) < 1

&ensp;반사율은 비율이므로 보통 0과 1사이이다.<br/>

&ensp;gray scale<br/>
&ensp;$L_{min}$ 부터 $L_{max}$ 까지의 회색조 범위를 말하면서<br/>
* l = 0 : black
* l = L - 1: white

&ensp;라고 정리한다.<br/>
&ensp;즉 디지털 영상에서는 밝기를 유한한 단계의 숫자로 표현한다<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-7.png" width="600"></p>

# Image sampling and quantization

&ensp;현실의 영상은 연속적이지만 컴퓨터는 연속값을 그대로 다룰 수 없어서 디지털화가 필요하다.<br/>

&ensp;두 단계<br/>
* Sampling
* Quantization

&ensp;1) Sampling<br/>
&ensp;좌표 (x, y)를 디지털화하는 것. 즉 위치를 픽셀 격자로 끊는 과정<br/>

&ensp;2) Quantization<br/>
&ensp;밝기(amplitude) 값을 디지털화하는 것. 즉 명암을 몇 단게로 나눌지 정하는 과정<br/>

* 좌표값의 디지털화 -> sampling = 공간 해상도와 관련
* 진폭값의 디지털화 -> quantization = 밝기 단계와 관련

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-8.png" width="600"></p>

&ensp;샘플링을 적게 하면<br/>
* 픽셀이 커지고
* 경계가 거칠어지고
* 세부 정보가 사라진다.

&ensp;즉 공간적으로 얼마나 촘촘하게 측정하느냐가 영상 선명도를 결정한다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-9.png" width="600"></p>

&ensp;양자화 단계 수가 적으면<br/>
* 밝기 변화가 부드럽지 않고 계단처럼 끊겨 보인다.

&ensp;예를 들어 256단계 회색조는 자연스럽지만 4단계 회색조는 밴딩 현상이 심해질 수 있다.<br/>

* sampling 부족 -> 모양이 거칠다
* quantization 부족 -> 밝기 계조가 거칠다.

# Spatial and intensity resolution

&ensp;1) Spatial resolution<br/>
&ensp;공간 해상도 즉 픽셀을 얼마나 촘촘히 배치했는가<br/>
&ensp;표현 방식:<br/>
* line pairs per unit distance
* pixels per unit distance
* dpi

&ensp;2) Intensity resolution<br/>
&ensp;명암 해상도. 즉 픽셀 밝기를 몇 단계로 표현하는가<br/>
&ensp;보통 비트 수로 표현한다.<br/>

&ensp;예<br/>
* 1 bit -> 2단계
* 8bit -> 256단계

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-10.png" width="600"></p>

&ensp;같은 장면이라도<br/>
* 픽셀 수가 적으면 뭉개져 보이고
* 픽셀 수가 많으면 디테일이 살아난다.

&ensp;즉 spatial resolution이 높을수록<br/>
* 경계가 더 선명하고
* 작은 구조를 더 잘 구별한다.

&ensp;같은 해상도라도<br/>
* 비트 수가 적으면 명암이 단순하고 뚝뚝 끊겨 보이고
* 비트 수가 많으면 자연스럽다

&ensp;즉 intensity resolution은 몇 단계 회색을 표현할 수 있는가의 문제<br/>

&ensp;사람들이 여러 영상을 주관적 품질을 평가한 결과를 바탕으로 isopreference curves(등가 선호 곡선)을 설명한다.<br/>

&ensp;핵심 내용<br/>
* N: spatial resolution
* k: bit depth
* N-k 평면에서 비슷한 화질로 느켜지는 조합들이 존재한다.

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-11.png" width="600"></p>

&ensp;영상 디테일이 많을수록 등가 선호 극선이 더 수직에 가까워진다. 즉 디테일이 많은 영상에서는 bit depth를 조금 줄여도 spatial resolution이 높으면 화질이 괜찮게 느껴질 수 있다.<br/>

# Image interpolation

&ensp;interpolation<br/>
&ensp;알고 있는 위치의 값을 이용해서 모르는 위치의 값을 추정하는 과정<br/>
&ensp;영상 확대 시 원래 없던 픽셀을 새로 채워야 하므로 필요하다.<br/>

&ensp;1) Nearest neighbor interpolation<br/>
&ensp;새 픽셀에 가장 가까운 원래 픽셀 값을 그래로 복사<br/>
&ensp;장점<br/>
* 빠름
* 구현 쉬움

&ensp;단점<br/>
* 블록처럼 거칠다
* 계단 현상이 생김

&ensp;2) Bilinear interpolation<br/>
&ensp;주변 픽셀 값을 이용해 더 부드럽게 추정<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-12.png" width="600"></p>

&ensp;네 개의 주변 픽셀을 사용한다.<br/>
&ensp;단위 사각형이 네 꼭짓점 값이 주어졌을 때 그 사이 값을 선형적으로 추정하는 방식이다.<br/>

$$f(x,y)≈f(0,0)(1−x)(1−y)+f(1,0)x(1−y)+f(0,1)(1−x)y+f(1,1)xy$$

&ensp;직관<br/>
* 가로로 한 번 평균
* 세로로 한 번 평균

&ensp;Bicubic interpolation<br/>
&ensp;가까운 16개 이웃 픽셀을 사용한다.<br/>

&ensp;특징<br/>
* bilinear보다 더 부드럽고 자연스러움
* 계산량은 더 큼

# Bicubic interpolation

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-13.png" width="600"></p>

* bicubic은 주변 16개 값을 고려한다.
* 단순한 선형 보간보다 더 부드럽고 정교하다
* 고품질 확대에 자주 쓰인다.

# Some basic relationships between pixels

&ensp;1) 4-neighbors<br/>
* (x+1, y)
* (x-1, y)
* (x, y+1)
* (x, y-1)

&ensp;이를 $N_4(p)$ 라고 한다.<br/>

&ensp;2) diagonal neighbors<br/>
&ensp;대각선 네 이웃<br/>
* (x+1, y+1)
* (x+1, y-1)
* (x-1, y+1)
* (x-1, y-1)

&ensp;이를 $N_D(p)$ 라고 한다.<br/>

&ensp;3) 8-neighbors<br/>

$$ N_8(p) = N_4(p)\cup N_D(p)$$

&ensp;상하좌우 + 대각선 전체 8개<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-14.png" width="600"></p>

* N, E, W, S -> 4-neighbor
* NE, SE, NW, SW -> diagornal neighbor
* 전체 합치면 8-neighbor

* $N_4(p) = {N, E, W, S}$
* $N_D(p) = {NE, SE, NW, SW}$
* $N_8(p) = N_4(p)\cup N_D(p)$

# Adjacency

&ensp;1) 4-adjacency<br/>
&ensp;q가 p의 $N_4(p)$ 안에 있으면 4-인접<br/>
&ensp;2) 8-adjacency<br/>
&ensp;q가 p의 $N_8(p)$ 안에 있으면 8-인접<br/>
&ensp;3) m-adjacency (mixed adjacency)<br/>
&ensp;혼합 인접성<br/>
&ensp;8-adjacency가 만들 수 있는 애매함을 없애기 위해 도입<br/>

# Path, Connectivity, Regions, Edge

&ensp;1) Path<br/>
&ensp;픽셀 p에서 q까지 이어지는 인접 픽셀들의 집합<br/>
&ensp;2) Path length<br/>
&ensp;그 경로를 구성하는 픽셀 개수로 길이를 생각한다.<br/>
&ensp;3) Closed path<br/>
&ensp;시작점과 끝점이 같으면 닫힌 경로<br/>
&ensp;4) Connected<br/>
&ensp;두 픽셀 사이에 path가 있으면 connected<br/>
&ensp;5) Connected component<br/>
&ensp;어떤 픽셀 p와 연결된 모든 픽셀들의 집합<br/>
&ensp;6) Connected set<br/>
&ensp;연결 성분이 하나뿐이면 connected set<br/>

&ensp;Region<br/>
&ensp;영역 R이 하나의 connected component만 가지면 region이라고 본다.<br/>
&ensp;즉 하나의 덩어리로 연결된 픽셀 집합<br/>

&ensp;Boundary<br/>
&ensp;영역 R안에 있으면서 이웃 중 하나 이상이 R 밖에 있는 픽셀들의 집합<br/>
&ensp;즉 경계선 픽셀들<br/>

&ensp;Edge<br/>
&ensp;gray level discontinuity<br/>
&ensp;밝기값이 갑자기 변하는 지점<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-15.png" width="600"></p>
<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-16.png" width="600"></p>

# Distance measures

&ensp;거리 함수 D의 조건<br/>
* 음수가 아님
* 자기 자신과의 거리는 0
* 대칭
* 삼각부등식을 만족

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-17.png" width="600"></p>

&ensp;1) Euclidean distance<br/>
&ensp;보통의 직선거리<br/>

$$D_E(p) = \sqrt{(x - s)^2 + (y - t)^2}$$

&ensp;2) D4 distance (city-block distance)<br/>
&ensp;상하좌우만 허용하는 거리<br/>

$$D_4(p) = \left\| x-s\right\| + \left\| y-t\right\|$$

&ensp;3) D8 distance (chessboard distance)<br/>
&ensp;대각선도 허용하는 거리<br/>

$$D_8(p, q) = max(\left\| x-s\right\|, \left\| y-t\right\|)$$

# Linear operation

&ensp;선형 시스템의 조건<br/>
&ensp;연산자 H가 선형이려면<br/>

$$H[a_if_i(x, y) + a_if_i(x, y)] = a_iH[f_i(x, y)] + a_iH[f_i(x, y)]$$

&ensp;를 만족해야 한다.<br/>

* 덧셈 보존
* 상수배 보존

&ensp;두 영상을 더한 뒤 처리한 결과가 각 영상을 따로 처리한 후 더한 결과와 같아야 한다.<br/>

# Arithmetic operation

&ensp;기본 연산<br/>
* 덧셈: s(x, y) = f(x, y) + g(x, y)
* 뺄셈: d(x, y) = f(x, y) - g(x, y)
* 곱셈: p(x, y)  = f(x, y) × g(x, y)
* 나눗셈: v(x, y) = f(x, y) / g(x, y)

&ensp;잡음은 평균이 0. 서로 uncorrelated. 이때 여러 noisy image를 평균내면 잡음이 줄어든다.<br/>

# Image averaging의 수식 전개

&ensp;평균 영상의 기대값은 원래 영상:<br/>

$$E[\bar{g}(x, y)] = f(x, y)$$

&ensp;즉 평균을 많이 내도 신호 자체는 유지된다.<br/>

&ensp;평균 영상의 분산은<br/>

$$\sigma ^2_{\bar{g}} = \frac{1}{K}\sigma ^2_n$$

&ensp;즉 이미지를 K장 평균내면 잡음 분산이 1/K로 줄어든다.<br/>
&ensp;의미: 많은 noisy image를 평균하면 신호는 유지되고 잡음은 감소한다.<br/>

# Image multiplication

&ensp;1) shading correction<br/>
&ensp;조명 불균일 때문에 어떤 부분은 어둡고 밝을 수 있는데 곱셈/나눗셈으로 이를 보정할 수 있다.<br/>

&ensp;2) masking / ROI<br/>
&ensp;마스크 영상과 곱해서 관심 영역(ROI)만 살리고 나머지는 없애는 데 사용<br/>

# Image representation

&ensp;실제로 대부분의 영상은 8bit, 즉 0~255범위로 표시한다.<br/>

&ensp;그런데 연산 결과는<br/>
* 음수가 되거나
* 255보다 커질 수 있다.

$$f_m = f - min(f)$$
$$f_s = K \times \frac{f_m}{max(f_m)}$$

&ensp;의미<br/>
1. 최소값을 빼서 바닥을 0으로 맞춤
2. 최대값 기준으로 전체를 비례 확대/축소
3. 결과를 [0, K] 범위에 넣음

&ensp;8bit면 K = 255<br/>

# Spatial operations

&ensp;Spatial operationsa 종류<br/>
* Single-pixel opetations
* Neighborhood operations
* Geometric spatial transforms

&ensp;1) Single-pixel operations<br/>
&ensp;각 픽샐을 독립적으로 바꾸는 연산<br/>

$$s = T(z)$$

&ensp;즉 입력 픽셀값 z를 함수 T로 바꿔 출력 s로 만든다.<br/>
&ensp;예<br/>
* 발기 증가
* 대비 조절
* 음영 반전

# Neighborhood operations

&ensp;출력 영상의 한 픽셀 g(x, y)는 입력 영상에서 (x, y) 주변 이웃 집합 $S_{x, y}$ 의 값들로 결정된다.<br/>
&ensp;즉 현재 픽셀만 보는 게 아니라 주변 픽셀을 함께 본다.<br/>

&ensp;예시: Local averaging<br/>
&ensp;주변 m x n 영역 평균을 내어 현재 픽셀값으로 사용하는 방식<br/>

&ensp;효과<br/>
* 블러
* 잡음 완화
* 세부 정보는 조금 희생

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-18.png" width="600"></p>

# 2D Image transformation

&ensp;기본 변환<br/>
* Translation: 이동
* Scaling: 확대/축소
* Rotation: 회전

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-19.png" width="600"></p>

&ensp;Affine transformation<br/>
&ensp;이 기본 변한들을 결함한 일반 형태<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-20.png" width="600"></p>

&ensp;픽셀값만 바꾸는 게 아니라 픽셀이 놓인 위치를 바꾸는 것<br/>

## Geometric spatial transformations

&ensp;기하 변환은 영상 내 픽셀들의 공간적 관계를 바꾼다.<br/>
&ensp;좌표 변환을<br/>

$$(x, y) = T{(v, w)}$$

&ensp;로 표현한다.<br/>

&ensp;Affine transform<br/>
&ensp;Affine transform은 여러 기하 연산을 하나의 행렬 형태로 통합해서 다룰 수 있게 해준다.<br/>
* translation
* scaling
* rotation
* shear

&ensp;로 따로따로 계산하지 않고 행렬 곱으로 묶어 표현 가능하다.<br/>

# Forward mapping and inverse mapping

&ensp;1) Forward mapping<br/>
&ensp;입력 영상의 픽셀을 출력 영상 위치로 보냄<br/>

&ensp;문제점<br/>
* 여러 입력 픽셀이 같은 출력 위치로 갈 수 있음
* 어떤 출력 위치는 비어버릴 수 있음

&ensp;즉 hole이 생길 수 있음<br/>

&ensp;2) Inverse mapping<br/>
&ensp;출력 영상의 각 위치에 대해 그 값이 원래 입력 영상 어디에서 왔는지 역으로 계산<br/>

$$(v, w) = T^{-1}(x, y)$$

&ensp;장점<br/>
&ensp;출력의 모든 픽셀을 빠짐없이 채우기 쉬움<br/>

&ensp;Image registration<br/>
&ensp;같은 장면의 둘 이상의 영상을 서로 맞추는 작업<br/>

&ensp;예시<br/>
* 의료영상 정합
* 위성영상 겹치기
* 여러 프레임 정렬

&ensp;방법<br/>
&ensp;두 영상에서 서로 대응하는 특징점들을 찾고 그 점들을 맞추는 변환 함수를 추정한다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-21.png" width="600"></p>

# Vector and matrix operations

&ensp;핵심<br/>
&ensp;RGB 영상의 한 픽셀은<br/>
* R
* G
* B

&ensp;세 성분을 가지므로 3차원 벡터로 볼 수 있다.<br/>

&ensp;벡터의 선형변환<br/>

$$w = A(z - a)$$

* A: 행렬
* z, a: 벡터
* w: 변환된 결과

&ensp;RGB 같은 다차원 픽셀 데이터를 행렬 곱으로 다른 공간으로 변환할 수 있다.<br/>
&ensp;예를 들어 색공간 변환, 특성 추출 등에 쓰일 수 있다.<br/>

# Image transforms

&ensp;어떤 영상처리 문제는 1. 입력 영상을 변환하고 2. 변환 영역에서 처리한 뒤 3. 다시 역변환하는 것이 더 좋다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-22.png" width="600"></p>

&ensp;푸리에 변환은 영상을 공간 정보 대신 주파수 정보로 표현하게 해준다.<br/>

&ensp;영상 안이 천천히 변하는 부분 -> 저주파<br/>
&ensp;급격히 변하는 경계/세부 -> 고주파로 나눠서 볼 수 있다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap2/2-23.png" width="600"></p>

# Probabilistic methods

&ensp;영상의 intensity 값을 확률 변수처럼 본다.<br/>
&ensp;가능한 intensity 값들을<br/>

$$z_i, i = 0, 1, ..., L-1$$

&ensp;라고 두고 각 값이 등장하는 확률 $p(z_k)$를 정의한다.<br/>

&ensp;이걸로 구하는 것<br/>
&ensp;1) 평균 밝기<br/>

$$m = \sum z_kp(z_k)$$

&ensp;2) 분산<br/>

$$\sigma ^2 = \sum (z_k - m)^2p(z_k)$$

&ensp;3) n차 모멘트<br/>

$$\mu _n = \sum (z_k - m)^np(z_k)$$

&ensp;의미<br/>
&ensp;이건 히스토그램 기반 영상 통계의 출발점<br/>
&ensp;즉 영상 전체의 밝기 분포를 수학적으로 분석할 수 있게 된다.<br/>

