---
title: "11주차 Support Vector Machine"
excerpt: "Support Vector Machine(SVM)이 왜 최대 마진 분류기라고 불리는지 이해하고 마진(margin)의 수학적 의미와 성능에 미치는 영향을 배운다."

wirter: sohee kim
categories:
  - Machine Learning
tags:
  - Machine Learning

toc: true
toc_sticky: true
use_math: true
  
date: 2025-06-19
last_modified_at: 2025-06-19
---


SVM의 최적화 목적 함수와 최대 마진 분류
=======

&ensp;1. SVM 문제<br/>
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-1.png" width="600"></p>

* 두 부류의 데이터를 잘 나누는 선(분류 경계선)을 찾는 것
* "가장 Margin(여백)"이 넓은 선을 고르는 것 → 이것이 바로 SVM의 아이디어

&ensp;2. 로지스틱 회귀 복습<br/>
&ensp;로지스틱 회귀의 예측 함수: 
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-2.png" width="600"></p>

* y = 1이면, wᵀx가 클수록 좋음 → h(x) → 1
* y = 0이면 wᵀx가 작을수록 좋음 → h(x) → 0

&ensp;로지스틱 회귀의 비용 함수 (Cost Function):<br/>
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-3.png" width="600"></p>

* y = 1이면: $-log h(x) = -log\frac{1}{1+ e^{-wTx}}$
* y = 0 이면: -log(1-h(x))

&ensp;결과적으로 wᵀx 값이 클수록 오차가 줄고 작으면 오차가 커짐<br/>

&ensp;3. SVM은 cost를 다르게 생각한다.<br/>
*  로지스틱 회귀는 부드러운 커브(cos 곡선)를 사용하지만 SWM은 직선 두 개로 근사함 -> 단순하고 계산 효율적

<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-4.png" width="600"></p>

* 이 함수는 간단하면서도 **"margin이 얼마나 안전한지를 판단"**하는 데 유리함

&ensp;로지스틱 회귀 vs SVM
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-5.png" width="600"></p>

&ensp;4. SVM의 비용 함수 구조<br/>
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-6.png" width="600"></p>

&ensp;로지스틱 회귀 비용 함수: <br/>
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-7.png" width="600"></p>

&ensp;계산을 더 쉽게 하기 위해 몇 가지 변형을 함<br/>

&ensp;Modification 1: m을 곱함<br/>
* 전체 비용 함수에서 $\frac{1}{m}$ 을 없애고 m을 정규화 항 분모에서 제거
* 결과는 동일하지만 계산이 쉬움

&ensp;Modification 2: λ 대신 C 사용<br/>
* λ는 정규화 계수 -> 오차를 얼마나 줄일지 제어
* C = $\frac{1}{λ}$ 로 두면 더 직관적임:
    - C가 크면 오차 허용 안 함 (엄격)
    - C가 작으면 오차 조금 허용함(느긋)

&ensp;5. 최종 정리: SVM의 목적 함수와 가설(Hypothesis)<br/>
&ensp;최적화 목적 함수<br/>
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-8.png" width="600"></p>

&ensp;C는 오차에 대한 민감도, 요차항은 $cost_1$ , $cost_0$ 두 개로 구성<br/>

&ensp;최종 모델: <br/>

<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-9.png" width="600"></p>

&ensp;즉 선형 결정 경계를 기준으로 데이터를 분류함<br/>

최대 마진 개념
======

&ensp;1. 왜 SVM은 최대 마진 분류기인가?<br/>
&ensp;Support Vector Machine(SVM)은 **"마진을 최대화하는 분류기"**라고 부른다. <br/>
* 마진(margin): 분류 경계선(decision boundary)와 각 클래스의 데이터 사이 거리
* 이 마진을 최대한 넓게 설정하면 새로운 데이터가 와도 잘 분류할 수 있는 일반화 성능이 좋아짐

&ensp;2. SVM의 비용 함수 구성<br/>
&ensp;비용 함수 J(w)는 두 부분으로 나눈다.<br/>
* 첫째: 모델이 데이터를 잘 분류했는지를 확인하는 항(예츨이 정확할수록 작아짐)
* 둘째: 너무 복잡한 모델을 피하기 위한 정규화 항 $\frac{1}{2}\left\| w\right\|^2$ -> 이것이 과접합을 막는 역할을 한다. 

<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-10.png" width="600"></p>

&ensp;3. Logistic 회귀와 SVM의 차이<br/>
&ensp;Logistic Regression에서는 다음을 원한다.<br/>
* y = 1 일 때 $w^Tw > 0$
* y = 0 일 때 $w^Tw < 0$

&ensp;VM에서는 더 확실한 구분을 위해 아래처럼 바꾼다.<br/>
* y = 1 일 때 $w^Tw > 1$
* y = 0 일 때 $w^Tw \leq -1$

&ensp;즉 0이 아니라 +1, -1을 기준으로 안전 여백(safety margin)을 둬서 애매한 분류를 피함<br/>

&ensp;4. 비용 함수에서의 마진 적용<br/>
&ensp;비용함수 안에서:<br/>
* $w^Tw \geq 1$ 이면 $cost_1 = 0$
* $w^Tw \leq -1$ 이면 $cost_0 = 0$

&ensp;즉 마진 안쪽 (1이상 -1이하)의 값만 신경 쓰고 그 외는 비용 없음 -> 간단한 비용 함수 가능<br/>

&ensp;5. 수학적으로 마진이란?<br/>
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-11.png" width="600"></p>

1. Decision Boundary는 $w^Tw = 0$ 형태의 직선이다.
2. 어떤 점 x에서 이 직선까지의 수직 거리 r은: $r = \frac{w^Tx}{\left\| w\right\|}$
3. 클래스 1과 0사이 가장 가까운 데이터로부터 이 거리의 합은 마진 $Margin = \frac{2}{\left\| w\right\|}$ -> 따라서 마진을 최대화하려면 $\left\| w\right\|$ 를 최소화해야 함

<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-12.png" width="600"></p>

&ensp;6. 최적화 문제로 표현하기<br/>
&ensp;최대 마진을 찾는 문제는 이렇게 바뀜<br/>
* 목표: $min\frac{1}{2}\left\| w\right\|^2$
* 조건: 
    - $w^Tx_i \geq 1$ (if y = 1)
    - $w^Tx_i \leq -1$ (if y = 0)

&ensp;7. 결정 경계선(Decision Boundary)의 일반화 능력<br/>
* 아래 두 선이 모두 데이터를 잘 나누고 있지만  

<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-13.png" width="600"></p>

* 어떤 선은 데이터와 너무 가까움 -> 새로운 데이터에 취약
* 어떤 선은 마진이 넓음 -> 새로운 데이터에도 안정적

* 따라서 SVM은 마진이 가장 넓은 경계선을 하나만 선택함 -> 최고의 일반화 성능

<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-14.png" width="600"></p>

&ensp;8. Outlier가 있을 경우는?<br/>
* C 값이 클수록 (오차 허용 안함) → 이상치(outlier)에 민감함 → 잘못된 경계
* C 값이 적당하면 → 일부 오차 허용 → 안정적인 분류 가능

&ensp;정리: SVM의 핵심<br/>
* "확실히" 구분할 수 있는 여백을 만들자!
* 마진을 최대화하면 일반화 성능이 높아진다.
* 비용 함수는 간단하고 직관적으로 구성되어 있다.

최대 마진 분류(Maximum Margin Classifier)의 수학적 개념
=======

&ensp;1. 벡터 내적(inner product)의 의미<br/>
* $u^Tv= \left\| u\right\| \times projection$ -> 벡터 v가 벡터 u에 만든 그림자의 길이(projection) x u의 길이
* 기하적 의미:
    - 내적은 각도에 따라 부호가 달라짐 
        + 90도보다 크면 음수
        + 90도보다 작으면 양수

<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-15.png" width="600"></p>

&ensp;2. SVM 비용 함수 (복습)<br/>
* 비용 함수: $min \left\| w\right\|^2$
* 제약 조건:
    - y = 1 -> wᵀx ≥ 1
    - y = 0 -> wᵀx ≤ -1
* 여기서 wᵀx는 결국 데이터 x를 w에 projection한 길이 p⁽ⁱ⁾ x \|\|w\|\| 와 같음

&ensp;3. 마진을 projection으로 표현<br/>
* projection 길이: $w^Tx = p^{(i)}\cdot \left\| w\right\|$

* 이를 통해 제약 조건 다시 쓰기: 
    - y = 1 -> $p^{(i)}\left\| w\right\| \geq 1$
    - y = 0 -> $p^{(i)}\left\| w\right\| \leq -1$

* 마진(Margin)은: $Margin = \frac{2}{\left\| w\right\|}$ 
* 따라서 비용함수를 최소화하는 건 -> 마진을 최대화하는 것과 같다.

&ensp;4. 예시를 통한 이해<br/>
&ensp;마진이 작은 경우<br/>
* 데이터들이 결정 경계(decision boundary)와 가까워서
* → projection p⁽ⁱ⁾가 작음 → w가 커져야 조건 만족
* → \|\|w\|\| 커지면 비용 함수 ↑ → 바람직하지 않음

&ensp;마진이 큰 경우<br/>
* 데이터들이 결정 경계에서 멀리 떨어져 있음
* → p⁽ⁱ⁾가 크므로 w가 작아도 조건 만족
* → \|\|w\|\| 작음 → 비용 함수 ↓ → 바람직함

&ensp; 5. 결론<br/>
* SVM은 마진을 최대화하는 방향으로 학습됨
    - 마진이 클수록 새로운 데이터도 잘 분류함 (→ 일반화 성능이 우수함)
* 따라서 support vector machine은 이상적인 분류 경계선을 찾는 데 효과적임!

커널의 개념
=======

&ensp;1. 복잡한 데이터와 분류 문제<br/>
&ensp;SVM은 주로 직선으로 데이터를 나누는 방법이다. 그런데 실제 세상에는 복잡하게 얽힌 데이터가 많아서 직선으로는 구분이 안되는 경우가 많다. 이런 경우 비선형적인(직선이 아닌 곡선 등의) 분류 경계선이 필요하다.<br/>

&ensp;2. 그럼 어떻게 비선형 경계를 만들까?<br/>
&ensp;이런 경우에는 입력 데이터 자체는 그대로 두고 특징(feature)을 변형해서 차원을 바꿔보는 아이디어를 쓴다.<br/> 
&ensp;예를 들어 x₁, x₂라는 두 개의 특징을 사용했지만 새로운 특징을 만들어서:<br/>
* x₁²
* x₂²
* x₁ * x₂
* x₁³, x₂³, …

&ensp;이렇게 고차원 다항식 형태로 특징을 확장하면 이 변형된 공간에서는 직선으로 나뉠 수 있다. -> 즉 원래 데이터는 곡선으로 나뉘지만 고차원 공간에선 직선으로 나뉜다.<br/>

&ensp;3. 그런데 이 방식의 문제점은?<br/>
&ensp;다항식을 계속 추가하면 특징이 너무 많아지고 특히 픽셀이 수천 개인 데이터에서는 계산이 폭발적으로 증가한다. -> 비슷한 결과를 내면서도 효율적인 방법을 찾아야 한다.<br/>

&ensp;4. 랜드마크와 커널의 아이디어<br/>
&ensp;랜드마크: 데이터 공간 위에 지정한 기준점이다. 예를 들어 2차원 평면 위에 점 3개를 무작위로 찍는거다. 그리고 어떤 데이터 x가 있을 때 그 x가 각 랜드마크와 얼마나 가까운지(=유사한지)를 측정하는 함수를 사용한다. 이 함수가 커널 함수이다.<br/>
* 예를 들어, x가 랜드마크 1에 가까우면 f₁ = 1에 가깝고, 멀면 0에 가까운 값을 가지게 된다. 
* 이것을 특징으로 사용하면, 복잡한 분류 경계도 만들 수 있다.

&ensp;5. 가장 많이 쓰는 커널: Gaussian Kernel<br/>

&ensp;Gaussian kernel 수식: $f_i = similarity(x, \l ^{(i)}) = exp(\frac{\left\| x-\l^{(i)} \right\|^2}{2\sigma ^2}) , i = 1, 2, 3$ <br/>

* x: 현재 데이터
* lᵢ: i번째 랜드마크
* \|\|x - lᵢ\|\|²: x와 랜드마크 사이 거리의 제곱
* σ²: 커널의 “폭”을 조절하는 값

&ensp;핵심 직관:<br/>
* x가 lᵢ와 가까우면 → 거리는 작음 → 분자는 작음 → fᵢ ≈ 1
* x가 lᵢ와 멀면 → 거리는 큼 → 분자는 큼 → fᵢ ≈ 0

&ensp;즉 fᵢ는 x가 해당 랜드마크와 얼마나 가까운지를 숫자로 나타낸다. 가깝다 -> 유사도 높음 -> 특징 값 큼, 멀다 -> 유사도 낮음 -> 특징 값 작음<br/>

&ensp;6. 커널로 만든 예측 함수는 어떻게 생겼나?<br/>
&ensp;SVM에서는 예측함수: 예측 = w₀ + w₁*f₁ + w₂*f₂ + w₃*f₃<br/>
&ensp;즉 각 커널 특징 (f₁, f₂, f₃)을 가중치(w)로 더하고 그 합이 0보다 크면 -> 1로 분류, 작으면 0으로 분류한다.<br/>

&ensp;예를 들어:<br/>
* x가 l¹에 가까우면 f₁ = 1, 나머지는 0 → 예측값이 0보다 크면 → y = 1
* x가 모든 랜드마크에서 멀면 → 모든 f = 0 → 예측값 < 0 → y = 0

&ensp;이렇게 비선형 경계선을 커널 특징을 통해 만들 수 있다.<br/>

&ensp;7. 랜드마크는 어떻게 정할까?<br/>
&ensp;학습 데이터의 위치 자체를 랜드마크로 사용한다. 즉 데이터가  x¹, x², ..., xᵐ개가 있다면 그걸 전부 랜드마크로 사용한다.<br/>
* 각 데이터는 m개의 랜드마크에 대해 f₁ ~ fₘ까지 특징을 가짐
* 그러면 특징 벡터는 m+1차원 (f₀ = bias 포함)

&ensp;이 방법은 정확하긴 하지만 계산량이 많아질 수 있다.<br/>

&ensp;8. 정리된 예측과 비용 함수<br/>
&ensp;이렇게 특징 벡터를 m+1차원으로 확장한 다음, SVM에서 사용하는 예측함수와 비용함수도 그대로 적용한다. <br/>
* 예측: y = 1 (if wᵀf(x) > 0 else 0)
* 비용함수: 이전과 같은 hinge loss + regularization

&ensp;단, 이제는 w의 차원이 m+1로 늘어나서 계산량이 많아질 수 있다.<br/>

&ensp;9. 파라미터 C와 σ²의 영향<br/>
1. C (정규화 파라미터)
* C가 크면 → 제약조건을 더 중요하게 봄 → 오버피팅 위험
* C가 작으면 → 더 부드러운 결정경계 → 언더피팅 위험
2. σ² (Gaussian 폭)
* σ² 작으면 → 커널이 국소적 → 결정 경계가 매우 정밀하지만 민감
* σ² 크면 → 커널이 넓게 퍼짐 → 덜 민감하고 부드러운 경계

&ensp;결국 이 두 값은 bias-variance trade-off에 영향을 준다.(오버피팅 vs 언더피팅 조절)<br/>

SVM 적용하기
======

&ensp;1. SVM을 구현하는 방법은?<br/>
&ensp;Support Vector Machine, 줄여서 SVM을 직접 수학적으로 계산하려면 어렵지만, 다행히도 실제로는 소프트웨어 패키지를 사용해서 쉽게 구현할 수 있다.<br/>
* liblinear: 선형 SVM 전용
* libsvm: 커널 SVM까지 포함
* MATLAB의 fitcsvm(): 다양한 커널 지원

&ensp;이 도구들은 주어진 데이터를 기반으로 최적의 피라미터 w를 찾아주고 그걸 사용해서 예측할 수 있다.<br/>

&ensp;2. SVM에서 미리 설정해야 할 것들<br/>
* 정규화 계수 C
    - $C = \frac{1}{\lambda }$ 
    - 오버비팅(모델이 너무 훈련 데이터에만 잘 맞음)과 언더피팅(모델이 너무 단순해서 데이터에 못 맞춤)을 조절하기 위해 사용된다.

* 커널 함수 (Kernel Function)
    - 커널 함수는 데이터를 고차원으로 매핑해서 복잡한 분류가 가능하게 해 줘.
    - 우리가 지난 시간에 배운 Gaussian 커널이 대표적인 예

&ensp;3. 커널의 종류<br/>
&ensp;(1) Linear Kernel (선형 커널)<br/>
* 커널 없이 사용하는 경우, 즉 f(x) = x 자체를 사용하는 경우
* 선형 결정 경계 (직선, 평면 등)만 가능
* 특징 수가 많고, 데이터 수가 적은 경우에 적합

&ensp;(2) Gaussian Kernel (RBF 커널)<br/>
* 비선형 분류 가능
* $exp(-\frac{\left\| x - \l \right\|^2}{2\sigma ^2})$ 형태
* 특징 수가 작고 데이터 수가 많은 경우에 적합
* 하이퍼파라미터인 $\sigma ^2$ 값을 적절히 설정해야 함

&ensp;(3) Polynomial Kernel<br/>
* $\left ( x^T\l + c \right )^d$ 형태
* 차수 d, 상수 c를 조절해야 함
* 커널이 될 수 있는 조건인 Mercer 조건을 만족해야 함

&ensp;4. 커널 사용 시 주의사항: 특징 값 스케일링<br/>
&ensp;SVM에서 유클리드 거리를 쓰기 때문에, 서로 다른 범위의 특징 값들이 섞여 있으면 문제가 생긴다.<br/>
&ensp;예시:<br/>
* 실린더 수: 4 ~ 8
* 최고 RPM: 4000 ~ 8000

&ensp;→ 이 경우 RPM의 영향력이 너무 커지므로, 모든 특징을 0~1 또는 평균 0, 표준편차 1로 스케일링하는 게 좋음.<br/>

&ensp;5. 멀티클래스 분류에도 SVM 사용 가능할까?<br/>
&ensp;SVM은 원래 이진 분류용이지만 One-vs-All방식으로 확장 가능하다.<br/>

&ensp;One-vs-All 방식<br/>
* 클래스가 k개라면 SVM을 k개 만든다.
* 예: 클래스 1 vs 나머지, 클래스 2 vs 나머지, ..., 클래스 k vs 나머지
* 새 데이터에 대해 각 SVM의 점수를 계산해서 가장 높은 점수를 선택!

&ensp;6. SVM vs 로지스틱 회귀 비교<br/>
<p align="center"><img src="/assets/img/Machine Learning/11. Spport Vector machine/11-16.png" width="600"></p>

