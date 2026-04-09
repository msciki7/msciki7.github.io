---
title: "Chap 3-1. Intensity Transformation and Spatial Filtering"
excerpt: ""

wirter: sohee Kim
categories:
  - Digital Image Processing
tags:
  - 영상처리

toc: true
toc_sticky: true
math: true

date: 2026-04-03
last_modified_at: 2026-04-03
---

# 1. 개요

&ensp;영상처리는 크게 다음처럼 나뉜다.<br/>
&ensp;1) Pixel-point processing<br/>
&ensp;한 픽셀씩 독립적으로 처리하는 방법이다.<br/>
&ensp;예<br/>
* histogram sliding
* histogram stretching
* thresholding
* brightness slicing
* photometric correction

&ensp;핵심은 현재 픽셀 하나의 값만 보고 바꾼다는 점이다.<br/>

&ensp;2) Pixel group processing<br/>
&ensp;주변 픽셀도 함께 보는 방식이다.<br/>
&ensp;예<br/>
* spatial filtering
* edge detection
* nonlinear spatial filtering

&ensp;핵심은 주변 이웃(neighborhood) 이 중요하다.<br/>

&ensp;3) Frequency domain processing<br/>
&ensp;푸리에 변환, DCT 같은 변환 후 처리한다.<br/>

&ensp;4) Geometric transformation<br/>
&ensp;이동, 회전, 크기 조절, 리샘플링 같은 기하학적 처리다.<br/>

&ensp;5) Multiple-image pixel-point processing<br/>
&ensp;두 장 이상의 영상을 픽셀 단위로 결합한다.<br/>
&ensp;예<br/>
* image differencing
* spectral rationing
* temporal noise reduction

&ensp;Spatial domain<br/>
&ensp;영상 평면 자체에서 바로 픽셀을 조작하는 것 즉, 우리가 지금 배우는 대부분의 내용은 공간영역 처리다.<br/>

&ensp;Transform domain<br/>
&ensp;영상을 어떤 변환(예: 푸리에 변환)으로 다른 영역으로 바꾼 뒤 처리하고, 다시 inverse transform으로 돌아오는 방식이다.<br/>

&ensp;즉<br/>
* 공간영역: 픽셀에 직접 손대기
* 변환영역: 변환 후 간접적으로 손대기

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-1.png" width="600"></p>

# 2. Spatial domain processing의 기본식

&ensp;공간영역 처리는 다음 식으로 표현한다.<br/>

$$g(x, y) = T[f(x, y)]$$

&ensp;수식 의미<br/>
* f(x, y): 입력 영상
* g(x, y): 출력 영상
* T: 입력 영상을 바꾸는 연산자(operator)

&ensp;여기서 핵심은 T가 어떤 방식으로 픽셀을 변환하느냐이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-2.png" width="600"></p>

&ensp;(x, y) 주변의 3x3 neighborhood가 있는데 출력 픽셀 하나를 만들 때 입력 픽셀 하나만 보는 게 아니라 그 주변도 볼 수 있다는 뜻이다.<br/>
* 1 x 1이면 픽셀 단독 처리
* 3 x 3, 5 x 5 면 주변 포함 처리

&ensp;라고 이해하면 된다.<br/>

&ensp;이웃 크기가 1 x 1이면 가장 단순한 형태가 된다.<br/>

$$s = T(r)$$

&ensp;수식 의미<br/>
* r: 입력 영상의 한 픽셀 밝기값
* s: 출력 영상의 대응 픽셀 밝기값
* T: gray-level transformation function

&ensp;이 식은 "입력 밝기 r를 어떤 함수 T에 넣어서 출력 밝기 s를 얻는다" 라는 뜻이다.<br/>
&ensp;이게 바로 point processing의 핵심 공식이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-3.png" width="600"></p>

# 3. Pixel Point Processing: 한 픽셀씩 밝기 변환

&ensp;1. 기본 개념<br/>

$$s = T[r]$$

&ensp;각 픽셀의 gray level을 새로운 값으로 바꾸는 것이다.<br/>

&ensp;1) Complementing<br/>
&ensp;입력이 밝으면 출력은 어둡고, 입력이 어두우면 출력은 밝다. 즉 반전(negative) 이다.<br/>

&ensp;2) Histogram slide-mapping<br/>
&ensp;전체 히스토그램을 한쪽으로 민다. 예를 들어 전체가 너무 어두운 영상을 오른쪽으로 밀면 더 밝아진다.<br/>

&ensp;3) Histogram stretch-mapping<br/>
&ensp;좁게 몰려 있는 밝기 범위를 넓게 늘린다. 즉 대비(contrast) 를 크게 만든다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-4.png" width="600"></p>

&ensp;2. Thresholding / Brightness Slicing / Photometric Correction<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-5.png" width="600"></p>

&ensp;1) Thresholding<br/>
&ensp;입력값이 임계값보다 작으면 0, 크면 255 같은 식으로 바꾼다.<br/>
&ensp;그래프 모양은 계단 함수다.<br/>

&ensp;주요 용도<br/>
* binary contrast enhancement
* binarization
* 문서 영상
* 지도 영상
* adaptive thresholding

&ensp;검정/흰색으로 나누는 작업이다.<br/>

&ensp;2) Brightness slicing<br/>
&ensp;특정 밝기 구간만 강조한다. 예를 들어 혈관 영상에서 특정 회색 범위가 혈관이라면 그 구간만 밝게 해서 잘 보이게 할 수 있다.<br/>
&ensp;즉 thresholding이 "한 기준으로 자르는 것"이라면 brightness slicing은 어떤 범위 [A, B]만 살리는 것에 가깝다.<br/>

&ensp;3) Photometric correction<br/>
&ensp;대표적으로 gamma correction<br/>
&ensp;센서 응답(sensor response)이 이상적인 직선이 아닐 수 있으므로 mapping function을 써서 사람이 보기 좋은 형태로 보정한다.<br/>

* 카메라/디스플레이/센서는 선형 응답이 아닐 수 있다.
* 그래서 밝기를 수학적으로 다시 매핑해 준다.

&ensp;3. Histogram slide와 stretch 예시<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-6.png" width="600"></p>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-7.png" width="600"></p>

&ensp;slide-mapping<br/>
* 원래 low-contrast 영상의 히스토그램이 좁은 구간에 몰려 있음
* 그것을 통째로 옮기면 전체가 더 밝아지거나 더 어두워진다

&ensp;stretch-mapping<br/>
* 좁은 히스토그램을 전체 구간으로 넓게 늘린다
* 결과 영상의 대비가 확실히 증가한다

&ensp;즉 실제 영상에서는<br/>
* slide = 밝기 이동
* stretch = 대비 확장

&ensp;4. 여러 영상에 대한 픽셀 단위 처리<br/>
&ensp;여러 영상을 픽셀 단위로 처리할 때의 기본식<br/>

$$O(x, y) = I_1 (x, y) # I_2 (x, y)$$

&ensp;기호 의미<br/>
* $I_1(x, y)$ : 첫 번째 입력 영상의 (x, y) 픽셀
* $I_2(x, y)$ : 두 번째 입력 영상의 (x, y) 픽셀
* O(x, y): 출력 영상
* #: 연산자

&ensp;여기서 #는<br/>
* \+
* −
* ∗
* div
* AND
* OR

&ensp;등이 될 수 있다.<br/>

&ensp;두 가지 경우<br/>
1. image combination: 같은 장면의 비슷한 영상들을 섞는 것
2. image composition: 서로 관련 없는 영상을 합쳐 새로운 이미지를 만드는 것

&ensp;즉 이 식은 "같은 위치의 픽셀끼리 연산한다."는 뜻이다.<br/>

&ensp;여러 영상 처리의 대표 예시<br/>
&ensp;1) Image differencing<br/>

$$O(x, y) = I_1(x, y) - I_2(x, y)$$

&ensp;용도<br/>
* motion/change detection
* background removal
* illumination equalization

&ensp;즉 두 장면의 차이만 남긴다. 움직인 물체나 변환 부분을 찾는 데 아주 유용하다.<br/>

&ensp;2) Image rationing<br/>

$$O(x, y) = I_1(x, y) / I_2(x, y)$$

&ensp;특히 다중분광 영상(multispectral image)에서 사용된다.<br/>

&ensp;3) Image averaging<br/>

$$O(x, y) = \frac{I_1(x, y) + I_2(x, y)}{2}$$

&ensp;같은 장면을 여러 번 찍었을 때 평균을 내면 랜덤 노이즈가 줄어든다. 즉 temporal noise reduction이다.<br/>

&ensp;rationing 예시를 실제 위성영상으로 보여준다.<br/>
* infrared 영상
* red filter 영상
* infrared / red 결과 영상

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-8.png" width="600"></p>

&ensp;결과에서 live vegetation이 훨씬 강조된다. 즉 ratio 연산이 단순 수학이 아니라 실제 물체 특성 차이를 드러내는 데 쓰인다는 것을 보여주는 페이지다.<br/>

# 4. Basic intensity transformation functions

&ensp;1. 세 가지 기본 함수 종류<br/>
&ensp;1) Linear<br/>
* identity transformation
* negative transformation

&ensp;2) Logarithmic<br/>
* log transformation
* inverse-log transformation

&ensp;3) Power-law<br/>
* nth power
* nth root

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-9.png" width="600"></p>

&ensp;그래프에서 입력 r, 출력 s의 관계를 비교해 보여준다.<br/>

&ensp;여기서 중요한 건 함수 모양이 달라지면 어느 밝기 구간이 강조되는지가 달라진다는 점이다.<br/>

&ensp;2. Image negative (Complementing)<br/>
&ensp;negative는 밝기를 뒤집는 변환이다.<br/>
&ensp;8비트 영상이라면 보통<br/>

$$s = 255 - r$$

&ensp;또는 일반적으로 L 단계 영상이면<br/>

$$s = L - 1 - r$$

&ensp;라고 쓴다.<br/>

&ensp;수식의미<br/>
* r: 입력 밝기
* s: 출력 밝기
* L - 1: 최대 밝기값

&ensp;예<br/>
* 입력 0이면 출력은 255
* 입력이 255면 출력은 0
* 입력이 128이면 중간 근처가 된다.

&ensp;그래프가 우하향 직석인 이유가 바로 이것이다.<br/>

&ensp;쓰는 이유<br/>
&ensp;검은 배경이 넓고 그 안에 밝거나 회색인 세부 정보가 숨어 있을 때 negative로 바꾸면 오히려 디테일이 더 잘 보일 수 있다.<br/>

&ensp;3. Log transformation<br/>
&ensp;로그 변환의 일반식<br/>

$$s = clog(1 + r)$$

&ensp;기호의 의미<br/>
* r: 입력 픽셀값
* s: 출력 픽셀값
* c: 스케일 상수
* log(1+r): 로그 변환

&ensp;1 + r -> r = 0 일 때 log0는 정의되지 않으므로 1을 더해서 안전하게 만든다.<br/>

&ensp;낮은 밝기값의 좁은 범위를 출력에서 더 넓게 펄쳐준다.<br/>
* 어두운 영역 디테일 강조
* 밝은 영역은 상대적으로 압축

&ensp;이라고 이해하면 된다.<br/>

&ensp;예를 들어<br/>
* 0~20사이의 값 차이는 크게 벌어지고
* 200~255사이의 값 차이는 압축된다.

&ensp;그래서 어두운 부분 구조를 보기 좋게 만든다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-10.png" width="600"></p>

&ensp;4. Power-law transform<br/>

&ensp;power-law transform의 기본식<br/>

$$s = cr_{γ}$$

&ensp;기호 의미<br/>
* r: 입력 밝기값
* s: 출력 밝기값
* c: 양의 상수
* γ: 감마 값, 양의 상수

&ensp;왜냐하면 감마 하나만 바꿔도 영상이 밝아지거나 어두워지기 때문이다.<br/>

&ensp;감마에 따른 해석<br/>
* γ < 1: 어두운 부분이 더 밝아짐
* γ = 1: 변화 없음 
* γ > 1: 전체가 더 어두워짐

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-11.png" width="600"></p>

&ensp;그래프에서도 γ값에 따라 곡선이 달라진다.<br/>

&ensp;gamma correction<br/>
&ensp;디스플레이나 CRT 모니터는 입력 전압과 실제 밝기가 선형 비례하지 않는다.
즉, 장치가 자체적으로 어떤 power-law response 를 가진다.<br/>
&ensp;예를 들어 장치 특성이 $r^{2.5}$ 처럼 나타나면 화면이 입력보다 더 어둡게 보일 수 있다. 이때 반대쪽 성질의 감마 보정을 적용해 전체 시스템을 선형에 가깝게 만든다.<br/>

&ensp;감마 보정 요약<br/>

$$s \propto r_{\gamma }$$

&ensp;여기서<br/>
* γ < 1: 밝아짐
* γ = 1: 그대로
* γ > 1: 어두워짐

&ensp;"감마가 1보다 작으면 dark region enhancement, 1보다 크면 darkening"<br/>

# 5. Piecewise-linear transformation

&ensp;piecewise-lineaer transformation은 구간별로 다른 직선을 붙여 만든 변환이다.<br/>
&ensp;장점: 함수 모양을 원하는 대로 복잡하게 만들 수 있다.<br/>
&ensp;단점: 사용자가 직접 구간과 기울기를 정해야 하므로 입력이 많다.<br/>

&ensp;대표 예<br/>
* contrast stretching
* gray-level slicing
* bit-plane slicing

&ensp;단일 공식 하나보다 더 유연한 맞춤형 변환이다.<br/>

&ensp;1. Contrast stretching<br/>
&ensp;목적은 gray level의 dynamic range를 넓히는 것이다.<br/>
&ensp;예를 들어 원본 영상의 픽셀들이 80~150 범위에만 몰려 있으면 그걸 0~255 전체로 늘리면 대비가 강해진다.<br/>

&ensp;일반 stretch<br/>

$$(r_1, s_1) = (r_{min}, 0), (r_2, s_2) = (r_{max}, L -1)$$

&ensp;즉 최소 밝기 $r_{min}$ 은 0으로 최대 밝기 $r_{max}$ 는 L - 1로 보낸다.<br/>

&ensp;Binary image용 threshold 형태<br/>

$$(r_1, s_1) = (m, 0), (r_2, s_2) = (m, L - 1)$$

&ensp;여기서 m은 mean value이다.<br/>

&ensp;즉 평균값을 기준으로 이진화하는 식으로도 볼 수 있다.<br/>

&ensp;2. Gray-level slicing<br/>
&ensp;목적은 특정 밝기 범위만 강조하는 것이다.<br/>

&ensp;예들 들어 [A, B]구간이 우리가 찾는 물체의 밝기 범위라고 한다.<br/>
&ensp;그러면 두 가지 방식이 있다.<br/>

&ensp;방식 1<br/>
&ensp;[A, B] 구간만 높게 만들고 나머지는 낮게 만든다. 즉 관심 영역만 두드러지게 한다.<br/>

&ensp;방식 2<br/>
&ensp;[A, B] 구간을 높게 만들되 나머지 구간은 유지한다. 즉 배경 정보도 어느 정도 보존한다.<br/>

&ensp;3. Bit-plane slicing<br/>
&ensp;8비트 영상은 각 픽셀을 8개의 비트로 표현할 수 있다.<br/>
&ensp;예<br/>

$$pixel value = b_7b_6b_5b_4b_3b_2b_1b_0$$

* 하위 비트(LSB): 작은 밝기 변화 담당
* 상위 비트(MSB): 전체 밝기 구조 담당

&ensp;bit-plane slicing은 특정 비트가 전체 영상 모양에 얼마나 기여하는지 보는 방법이다.<br/>

&ensp;즉<br/>
* bit plane 1: LSB
* bit plane 8: MSB

&ensp;로 나뉜다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-12.png" width="600"></p>

# 6. Histogram Equalization과 Histogram Modification

&ensp;1. Histogram equalizatoin의 목적과 조건<br/>
&ensp;histogram equalization은 출력 영상의 히스토그램이 가능한 균등(uniform)해지도록 하는 변환 함수를 찾는 방법이다.<br/>

&ensp;기본식<br/>

$$s = T(r)$$

&ensp;여기서<br/>
* r: 입력 밝기
* s: 출력 밝기

&ensp;조건<br/>
1. T(r)는 단조 증가(monotonically increasing)
2. 0 ≤ T(r) ≤ L - 1
3. 역함수가 가능해야 함(엄밀히는 strictly monotonic이면 one-to-one)

&ensp;단조 증가여야 하는 이유<br/>
&ensp;밝은 입력이 더 어두운 출력으로 뒤바뀌는 혼란을 줄이기 위해서이다. 즉 밝기 순서를 유지한다.<br/>

&ensp;범위를 유지해야 하는 이유<br/>
&ensp;출력도 여전히 영상의 가능한 밝기 범위 안에 있어야 하기 때문이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-13.png" width="600"></p>

* 단조 증가 -> 출력 밝기 순서 보존
* 출력 범위 유지 -> 입력과 같은 밝기 레벨 범위 사용
* 역함수 존재 -> 서로 다른 입력이 같은 출력으로 무작정 겹치지 않게 함

&ensp;실제로 histogram equalization의 변환 함수는 CDF 누적분포함수를 사용한다.<br/>

&ensp;2. 히스토그램과 확률<br/>
&ensp;히스토그램 정의<br/>

$$h(r_k) = n_k$$

&ensp;의미<br/>
* $r_k$ : k번째 gray level
* $n_k$: 그 gray level을 가진 픽셀 개수

&ensp;정규화된 형태는<br/>

$$p(r_k) = \frac{n_k}{n}, n = MN$$

&ensp;의미<br/>
* M × N: 영상 크기
* n = MN: 전체 픽셀 수
* $p(r_k)$ 밝기 $r_k$ 가 나올 확률

&ensp;즉 히스토그램은 "개수" 정규화 히스토그램은 "확률"이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-14.png" width="600"></p>

&ensp;3. 연속영역에서의 histogram equalization 유도<br/>
&ensp;기본 확률변수 변환 공식:<br/>

$$p_s(s) = p_r(r) \left | \frac{dr}{ds}\right |$$

&ensp;의미<br/>
* $p_r(r)$ : 입력 밝기 r의 pdf
* $p_s(s)$ : 출력 밝기 s의 pdf

&ensp;그리고 변환 함수를<br/>

$$s = T(r) = (L - 1)\int_{0}^{r}p_r(w)dw$$

&ensp;로 둔다.<br/>
&ensp;이 식은 입력 밝기의 CDF에 (L - 1)을 곱한 것이다.<br/>

&ensp;이런 식을 쓰는 이유<br/>
&ensp;히스토그램을 균등하게 만들고 싶기 때문<br/>
&ensp;미분하면<br/>

$$\frac{ds}{dr} = \frac{dT(r)}{dr} = (L - 1)p_r(r)$$

&ensp;따라서<br/>

$$\frac{dr}{ds} = \frac{1}{(L - 1)p_r(r)}$$

&ensp;이걸 처음 식에 대입하면<br/>

$$p_s(s) = p_r(r)\left | \frac{1}{(L - 1)p_r(r)}\right | = \frac{1}{L - 1}$$

&ensp;즉<br/>

$$p_s(s) = \frac{1}{L - 1}, 0 \leq s \leq L-1$$

&ensp;가 된다.<br/>

&ensp;결론<br/>
&ensp;출력 밝기 s는 균일분포(uniform distribution)를 갖는다.<br/>
&ensp;즉 입력의 pdf를 CDF로 누적해서 매핑하면 출력 히스토그램이 평탄해진다.<br/>

&ensp;4. 이산영역에서의 histogram equalization<br/>
&ensp;실제 디지털 영상에서는 적분 대신 합을 쓴다.<br/>

$$P_r(r_k) = \frac{n_k}{MN}, k = 0, 1, ..., L - 1$$

&ensp;그리고 변환은<br/>

$$s_k = T(r_k) = (L - 1) \sum_{j = 0}^{k}p_r(r_j)$$

&ensp;또는<br/>

$$s_k = \frac{L - 1}{MN}\sum_{j = 0}^{k}n_j$$

&ensp;의미<br/>
* 현재 gray level $r_k$ 까지의 누적확률을 구한다.
* 거기에 L−1 을 곱해 출력 gray level로 바꾼다.

&ensp;즉 디지털 구현에서는 CDF를 누적합으로 계산한다고 이해하면 된다.<br/>

&ensp;각 gray level의 확률을 구하고 누적해서 $s_k$를 계산한다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-15.png" width="600"></p>

&ensp;1. 각 gray level의 개수 $n_k$ 정리<br/>
&ensp;2. 확률 $p_r(r_k) = n_k/(MN)$ 계산<br/>
&ensp;3. 누적합 $\sum_{j = 0}^{k}p_r(r_j)$ 계산<br/>
&ensp;4. (L - 1)을 곱해서 $s_k$ 계산<br/>
&ensp;5. 원래 픽셀값들을 새 값으로 치환<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-16.png" width="600"></p>

&ensp;5. Histogram equalization 요약<br/>
&ensp;핵심 요약:<br/>

$$s = F_r(r) = \int_{0}^{r}p_r(w)dw$$

&ensp;여기서 $F_r(r)$ 는 입력 밝기 r의 CDF이다.<br/>

&ensp;실제 영상 범위를 고려하면<br/>

$$s = (L - 1) = \int_{0}^{r}p_r(w)dw$$

&ensp;를 사용한다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-17.png" width="600"></p>

&ensp;핵심 의미<br/>
* 히스토그램 = 밝기값의 상대적 빈도
* 목표 = 출력 히스토그램을 균일하게 만듦
* 방법 = 입력 밝기의 CDF로 매핑

&ensp;즉 "히스토그램 평활화"라는 말은 결국 CDF 매핑이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-18.png" width="600"></p>

&ensp;6. Histogram modification<br/>
&ensp;Histogram equalization은 uniform distribution을 목표로 했지만 histogram modification은 원하는 출력 분포를 직접 정하는 방법이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-19.png" width="600"></p>

&ensp;기본 아이디어는 입력 누적확률과 출력 누적확률을 맞추는 것이다.<br/>
&ensp;예시 구현: $s[i] = F(i)$ <br/>
&ensp;그리고 모든 픽셀에 대해<br/>

$$output[i][j] = (uchar)s(input[i][j])$$

&ensp;즉 미리 매핑 테이블을 만든 뒤 각 픽셀에 적용하는 방식이다.<br/>

&ensp;이번에는 출력 pdf를 지수분포(exponential distribution)로 두는 예시<br/>
&ensp;핵심<br/>
* 원하는 $p_s(s)$ 를 정한다.
* 누적해서 $F_s(s)$를 만든다.
* 입력 CDF와 연결해 매핑을 구한다.

&ensp;즉 equalization이 “uniform만 목표”였다면, modification은 “원하는 분포로 바꾸기”라고 이해하면 된다.<br/>

# 7. Local Enhancement

&ensp;전역 히스토그램이 아니라 국소 통계(local statistics) 를 이용해 enhancement하는 방법이다.<br/>

&ensp;전역 평균<br/>

$$m = \sum_{i = 0}^{L-1}r_ip(r_i)$$

&ensp;전역 분산<br/>

$$\sigma ^2 = \sum_{i=0}^{L-1}(r_i - m)^2p(r_i)$$

&ensp;국소 평균<br/>

$$m_{S_{xy}}$$

&ensp;국소 분산<br/>

$$\sigma ^2_{s_{xy}}$$

&ensp;즉 전체 영상의 평균/분산과 특정 작은 영역 $S_{xy}$ 안의 평균/분산을 비교한다.<br/>
&ensp;그 다음 enhancement rule:<br/>

$$g(x, y) = \left\{\begin{matrix}
E \cdot f(x, y), & if m_{S_{xy}} \leq k_0m_G and k_1\sigma _{S_{xy}} \leq k_2\sigma _G \\
 f(x, y),& otherwise \\
\end{matrix}\right.$$

&ensp;의미<br/>
&ensp;특정 지역이<br/>
* 전체보다 어둡고
* 분산도 특정 범위 안에 있으면

&ensp;그 픽셀을 E배 밝게 만든다.<br/>
&ensp;영상 전체를 무조건 밝게 하는 게 아니라 어둡고, 디테일이 적당한 지역만 골라서 국소적으로 강화하는 방법이다.<br/>

# Spatial Filtering의 기초

&ensp;1. Spatial filtering<br/>
&ensp;spatial filtering은 영상처리에서 매우 중요한 도구다.<br/>
&ensp;주파수 영역의 LPF, HPF 개념을 공간영역에서도 비슷하게 구현할 수 있다.<br/>
* LPF: 부드럽게, 블러
* HPF: 경계 강조, 선명화

&ensp;여기서 mask, kernel, template, window 라는 말이 거의 비슷하게 쓰인다.<br/>

&ensp;spatial filter는<br/>
* 작은 neighborhood
* 그 위에서 수행할 predefined operation

&ensp;으로 구성된다.<br/>
&ensp;출력 픽셀은 보통 그 neighborhood의 중심 위치에 기록된다.<br/>
&ensp;또한 필터는<br/>
* linear spatial filter
* nonlinear spatial filter

&ensp;로 나뉜다.<br/>
&ensp;선형이면 sum of products 형태로 계산된다.<br/>

&ensp;2. Spatial filtering 수식<br/>

$$g(x, y) = \sum_{s=-a}^{a}\sum_{t=-b}^{b}w(s, t)f(x+s, y+t)$$

&ensp;기호 의미<br/>
* f(x+s, y+t): 입력 영상의 주별 픽셀
* w(s, t): 커널(마스크) 계수
* g(x, y): 출력 픽셀
* a, b: 커널 반크기

&ensp;예를 들어 3×3 마스크면 a = b = 1 이다.<br/>

&ensp;의미<br/>
&ensp;각 주변 픽셀에 가중치 w를 곱해서 모두 더한 값을 출력으로 만든다. 즉 공간 필터링은 weighted average /weighted sum이다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-20.png" width="600"></p>

&ensp;3. Correlation과 Convolution<br/>
&ensp;Correlation<br/>
&ensp;마스크를 그대로 밀면서 sum of products를 계산<br/>

&ensp;Convolution<br/>
&ensp;마스크를 180도 회전시킨 뒤 sum of products를 계산<br/>
&ensp;즉 둘의 차이는 필터를 뒤집느냐 안 뒤집느냐이다.<br/>

&ensp;1차원 예시<br/>
&ensp;convolution<br/>

$$y[n] = w[n] \ast x[n] = \sum_{k} w[k]x[n-k]$$

&ensp;correlation<br/>

$$\sum_{k} w[k]x[n+k]$$

&ensp;즉 correlation은 x[n+k], convolution은 x[n-k]를 쓴다.<br/>
&ensp;그래서 correlation은 일반적으로 교환법칙이 없지만 convolution은 교환법칙을 가진다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-21.png" width="600"></p>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-22.png" width="600"></p>

&ensp;2차원 식<br/>
&ensp;2D correlation<br/>

$$w(x, y) \circ f(x, y) = \sum_{s = -a}^{a}\sum_{t=-b}^{b}w(s, t)f(x+s, y+t)$$

&ensp;2D convolution<br/>

$$w(x, y) \ast  f(x, y) = \sum_{s = -a}^{a}\sum_{t=-b}^{b}w(s, t)f(x-s, y-t)$$

&ensp;여기서 마이너스 부호가 바로 180도 뒤집기 효과이다.<br/>
&ensp;또 correlation은 이미지 매칭(template matching)에도 쓸 수 있다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-23.png" width="600"></p>

# Convolution의 의미

&ensp;필터 h(n)의 성질을 DTFT로 분석<br/>
&ensp;예<br/>
* {1,−1}
* {1,2,1}
* {1,1,1}
* {−1,2,−1}

&ensp;DTFT:<br/>

$$H(e^{j\hat{w}}) = \sum_{k=-\infty }^{\infty }h[k]e^{-j\hat{w}k}$$

&ensp;이 필터들이 LPF인지 HPF인지 magnitude를 보고 판단하라<br/>
&ensp;즉 공간영역 필턴도 결국 주파수 응답으로 해석할 수 있다는 점을 보여준다.<br/>

# 10. Low-pass / High-pass filtering

&ensp;대표 커널 두 개<br/>

&ensp;Box filter(LPF)<br/>

$$Boxfilter kernel = \frac{1}{9}\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1 \\
\end{bmatrix}$$

&ensp;왜 1/9인가?<br/>
&ensp;3x3에 1이 9개 있으므로 총합 9이다. 이걸 9로 나누면 주변 9개 픽셀의 평균값이 된다.<br/>
&ensp;평균을 내면 급격한 변화가 줄어드니 blur가 생긴다. 따라서 LPF는 영상 블러링을 일으킨다.<br/>

&ensp;HPF kernel<br/>

$$\begin{bmatrix}
-1 & -1 & -1 \\
-1 & 8 & -1 \\
-1 & -1 & -1 \\
\end{bmatrix}$$

&ensp;이 커널은 중심 픽셀을 크게 보고 주변을 빼 버린다. 즉 주변과 차이가 큰 부분, 곧 고주파 성분(에지)이 강조된다.<br/>
&ensp;그래서 HPF는 sharpening 효과를 낸다.<br/>

&ensp;선형 필터링을 벡터로 표현한다.<br/>

$$R = w_1z_1 + w_2z_2 + ...+ w_{mn}Z_{mn}$$

&ensp;또는<br/>

$$R = \sum_{k=1}^{mn}w_kz_k = w^Tz$$

&ensp;의미<br/>
* w: 커널 계수 벡터
* z: 이웃 픽셀 벡터

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-24.png" width="600"></p>

&ensp;즉 필터링은 결국 벡터 내적(dot product)이다. 이 관점은 계산 구현이나 선형대수 해석에서 중요하다.<br/>

&ensp;평균 intensity를 만드는 경우<br/>

$$R = \frac{1}{9}\sum_{i=1}^{9}z_i$4$$

&ensp;즉 3x3 neighborhood의 평균을 내는 것이다. 이게 가장 기본적인 smoothing mask이다.<br/>

&ensp;Gaussian mask를 만드는 연속 함수가 나온다.<br/>

$$h(x, y) = e^{-\frac{x^2 + y^2}{2\sigma ^2}}$$

&ensp;또는 1차원 가우시안과 연결한다.<br/>

&ensp;의미<br/>
* $\sigma$ : 표준편차
* 중심에 가까울수록 큰 값
* 멀수록 작은 값

&ensp;즉 box filter처럼 모두 같은 비중이 아니라 중심 픽셀에 더 큰 가중치를 주는 smoothing filter를 만들 수 있다.<br/>
&ensp;3x3 마스크면 중심 주변의 정수 좌표에서 샘플링해 계수를 만든다.<br/>

# 11. Smoothing spatial filters

&ensp;smoothing filter의 목적은<br/>
* blurring
* noise reduction

&ensp;이다.<br/>

&ensp;선형 smoothing filter의 출력은 neighborhood 안 픽셀들의 평균이다. 그래서 averaging filter라고도 부른다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-25.png" width="600"></p>

&ensp;하지만 단점도 있다.<br/>
* 랜덤 노이즈도 줄어들지만
* edge 역시 sharp transition이라 함께 흐려진다.

&ensp;즉 smoothing은 항상 노이즈 감소와 에지 손실의 trade-off가 있다.<br/>

&ensp;weighted average<br/>
&ensp;픽셀마다 다른 계수를 곱해 평균을 낸다.<br/>
&ensp;즉 어떤 픽셀은 더 중요하게 어떤 픽셀은 덜 중요하게 반영한다.<br/>
&ensp;일반식:<br/>

$$g(x, y) = \frac{\sum \sum w(s, t)f(x+s, y+t)}{\sum \sum w(s, t)}$$

&ensp;형태로 이해하면 된다.<br/>
&ensp;또 3x3, 7x7등 mask 크기가 커질수록 blur 효과가 강해진다.<br/>

&ensp;같은 크기의 검은 사각형이라도 필터 크기와 비슷한 작은 구조는 훨씬 크게 blur된다는 점을 보여준다. 즉 smoothing은 작은 세부를 지워 버리기 쉽다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-26.png" width="600"></p>

&ensp;블러링의 중요한 응용은 **관심 물체의 거친 현상(gross representation)을 얻는 것**이다.<br/>
&ensp;작은 물체들은 배경과 섞이고 큰 물체는 blob처럼 남는다. 그 다음 thresholding을 하면 큰 구조만 쉽게 분리할 수 있다.<br/>
&ensp;즉 smoothing은 단독 목적만이 아니라 전처리(preprocessing)로 매우 중요하다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-27.png" width="600"></p>


# 12. Order-statistic / Nonlinear filter

&ensp;Order-statistic filter는 **비선형 필터**다.<br/>
&ensp;과정<br/>
1. neighborhood 안 픽셀값들을 정렬한다.
2. 순서(rank)를 기준으로 특정 값을 고른다.
3. 중심 픽셀을 그 값으로 대체한다.

&ensp;대표가 median filter이다.<br/>

&ensp;Median filter: 중앙값으로 바꾼다.<br/>
&ensp;장점<br/>
* impulse noise 제거에 매우 강함
* linear smoothing보다 edge blur가 덜함

&ensp;특히 slat-and-pepper noise에 효과적이다.<br/>

&ensp;왜냐하면 이상치(outlier) 하나가 있어도 평균도 크게 흔들리지만 중앙값은 덜 흔들리기 때문이다.<br/>

&ensp;이 외에도<br/>
* max filter
* min filter

&ensp;가 있다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-28.png" width="600"></p>

&ensp;3x3 median filter 예시<br/>
&ensp;주변 9개의 값을 정렬해서 가운데 5번째 값을 출력으로 사용한다는 식으로 이해하면 된다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-29.png" width="600"></p>

&ensp;order-statistic filter 관련 예시<br/>
&ensp;핵심: nonlinear filtering은 sum-of-products가 아니라 정렬과 선택 기반이라는 점<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-30.png" width="600"></p>

# 13. Sharpening spatial filters

&ensp;1. 미분과 샤프닝<br/>
&ensp;샤프닝은 **밝기 변화가 급격한 부분**을 강조하는 것이다.<br/>
&ensp;평균화가 적분과 비슷하므로 샤프닝은 미분으로 생각할 수 있다.<br/>
&ensp;디지털에서는 연속미분 대신 차분을 사용한다.<br/>

&ensp;1차 미분<br/>

$$\frac{\partial f}{\partial x} = f(x+1)-f(x)$$

&ensp;2차 미분<br/>

$$\frac{\partial ^2f}{\partial x^2} = f(x+1)-2f(x)+f(x-1)$$

&ensp;의미<br/>
* 1차 미분: 변화율
* 2차 미분: 변화율의 변화

&ensp;즉 에지처럼 갑자기 바뀌는 부분에서 큰 값을 만든다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-31.png" width="600"></p>

&ensp;1차 미분은 현재값과 다음값 차이, 2차 미분은 이전/현재/다음값을 함께 쓴다.<br/>
&ensp;또 2차 미분의 zero crossing property가 에지 검출에 유용하다고 설명한다. 즉 2차 미분이 부호를 바꾸는 지점이 경계일 수 있다.<br/>

&ensp;2. Laplacian<br/>
&ensp;2차 미분을 2D로 확장하면 Laplacian이 된다.<br/>
&ensp;대표 mask 예시는 보통<br/>

$$\begin{bmatrix}
0 & 1 & 0 \\
1 & -4 & 1 \\
0 & 1 & 0 \\
\end{bmatrix}$$

&ensp;또는 대각선까지 포함한 형태를 쓸 수 있다.<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-32.png" width="600"></p>

&ensp;핵심은 주변과 현재값의 차이의 합으로 생각하면 된다. 급격한 변화가 있는 부분이 크게 튀어나온다.<br/>

&ensp;3. Unsharp masking/Highboost filtering<br/>
&ensp;unsharp masking 절차<br/>
&ensp;1. 원본을 blur한다.<br/>
&ensp;2. 원본에서 blur 버전을 뺀다.<br/>

$$g_{mask}(x, y) = f(x, y) - f_{blur}(x, y)$$

&ensp;3. 이 mask를 원본에 더한다.<br/>

$$g(x, y)= f(x, y) + k\cdot g_{mask}(x, y)$$

&ensp;의미<br/>
* blur된 버전은 저주파만 남는다
* 원본 - blur = 고주파 성분(에지/세부)
* 그걸 다시 더하면 샤프해진다

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-33.png" width="600"></p>

&ensp;k > 1 이면 highboost filtering이라고 한다.<br/>
&ensp;즉 에지 강조량을 더 크게 만든 것이다. k가 클수록 더 샤프하지만 과하면 노이즈도 강조될 수 있다.<br/>

&ensp;4. Gradient와 edge operator<br/>
&ensp;gradient 정의:<br/>

$$\bigtriangledown f = \begin{bmatrix}
g_x \\ g_y
\end{bmatrix} = \begin{bmatrix}
\frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y}
\end{bmatrix}$$

&ensp;gradient magnitude<br/>

$$M(x, y) = \sqrt{g^2_x + g^2_y}$$

&ensp;근사식<br/>

$$M(x, y) \approx \begin{vmatrix} g_x\end{vmatrix} + \begin{vmatrix} g_y \end{vmatrix}$$

&ensp;의미<br/>
* $g_x$ : x방향 변화량
* $g_y$ : y방향 변화량
* magnitude: 전체 에지 강도

&ensp;즉 gradient는 "어느 방향으로 얼마나 급하게 변하는가"를 나타낸다.<br/>

&ensp;Roberts operator<br/>

$$g_x = z_9 - z_5, g_y = z_8 - z_6$$

&ensp;gradient mangnitude<br/>

$$M(x, y) = \sqrt{(z_9 + z_5)^2  + (z_8 - z_6)^2}$$

&ensp;또는 근사형도 사용요한다.<br/>

&ensp;Sobel operator<br/>
&ensp;$z_1 ~ z_9$ 로 neighboorhood를 두고 x방향/y방향 기울기를 계산한다.<br/>

<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-34.png" width="600"></p>

&ensp;Sobel은 Roberts보다 노이즈에 더 강하고 실전에서 많이 쓴다.<br/>

&ensp;edge transition profile과 1차/2차 미분 관계를 설명<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-35.png" width="600"></p>

* 1차 미분: 에지 위치에서 peak
* 2차 미분: 에지 전후에서 부호가 바뀜
* Laplacian: 방향성 없이 omni-directional

&ensp;Prewitt edge direction과 magnitude 예시<br/>
<p align="center"><img src="/assets/img/Digital Image Processing/chap3-1/3-36.png" width="600"></p>
&ensp;Sobel과 비슷한 계열의 1차 미분 기반 에지 연산자라고 보면 된다. 즉 방향과 크기를 함께 해석할 수 있음을 보여준다.<br/>

&ensp;5. Line Segment Enhancement<br/>
&ensp;에지 강화 후 끊어진 선분을 정리하는 내용이다.<br/>
&ensp;즉 edge connection, gap filling 같은 후처리 역할을 한다.<br/>
* vertical
* horizontal
* 45도
* 135도

&ensp;등 방향성 마스크를 제시한다.<br/>
&ensp;핵심은 특정 방향의 선분에 잘 반응하는 mask를 써서 끊긴 선을 이어 주거나 더 강조하는 것이다.<br/>