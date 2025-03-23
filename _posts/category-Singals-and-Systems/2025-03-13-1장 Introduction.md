---
title: "1장 Introduction"
excerpt: "Classification of Signals."

wirter: sohee Kim
categories:
  - Signals and Systems
tags:
  - singal
  - system

toc: true
use_math: true
toc_sticky: true

date: 2025-03-13
last_modified_at: 2025-03-13
---

&ensp;1. 연속시간 신호와 이산시간 신호(Continuous-time and discrete-time singals)</br>
==========

&ensp;continuous-time -> sampling -> discrete-time
<p align="center"><img src="/assets/img/Singals and Systems//1장 Introduction/1-1.png" width="600"></p>

&ensp;Periodic 과 aperiodic singal의 차이점<br/>
&ensp;주기적 신호는 일정한 간격 T마다 동일한 패턴이 반복되는 신호. <br/>
&ensp;-연속신호 : $x(t) = x(t + T)$ (T: 기본주기), 주파수 : $f = 1/T (T = 2π/ω)$<br/>
&ensp;-이산신호 : $x[n] = x[n + N]$ (N: 기본 주기기) , 주파수 : $ω = 2πf = 2π/N$<br/>
이산시간 신호는 연속시간 신호를 일정한 비율로 샘플링하여 얻는다. (샘플링(sampling): 메시지 신호를 특정 순간에서 그 진폭을 나타내는 일련의 수로 변환)<br/>

&ensp;2. 우함수 신호와 기함수 신호(Even and Odd signals)<br/>
======

&ensp;우함수 신호 : $x(-t) = x(t)$<br/>
기함수 신호: $x(-t) = -x(t)$<br/>
&ensp;우함수 신호는 수직축에 대하여 수직, 기함수 신호는 원점에 대하여 대칭<br/>
&ensp;All signals can be represented by sum of odd signal and even signal.<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-2.jpg" width="600"></p>

&ensp;컬레 대칭(conjugate symmetry)<br/>
<center>$x(-t) = x*(t)$</center><br/>
<center>$x(t) = a(t) + ib(t)$</center><br/>
<center>$x*(t) = a(t) - ib(t)$</center><br/>
<center>$a(-t) + ib(-t) = a(t) - ib(t)$</center><br/>
&ensp;its real part is even, its imaginary part is odd(실수부 - 우함수 신호, 허수부 - 기함수 신호)<br/>


&ensp;3. 주기 신호와 비주기 신호(Periodic and aperiodic signals)<br/>
======

&ensp;$x(t) = x(t + T)$ (모든 t에 대하여)<br/> 
T는 x(t)의 기본주기(fundamental period); x(t)의 기본 주파수<br/>
$f = 1/T$ (주파수 f의 단위: 헤르츠(Hz))<br/>
단위가 rad/sec인 각주파수(angular frequency) -> $ω = 2\pi f = 2\pi / T$<br/>

&ensp;비주기적 신호는 만족하는 T가 존재하지 않는 <br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-3.jpg" width="600"></p>


&ensp;cf. 주파수의 기본 개념 : 신호가 주기적으로 변할 때 그 변동 속도를 나타내는 게 주파수. 시간 축에서 신호가 얼마나 빨리 반복된느지 나타내는 척도<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-4.png" width="600"></p>


&ensp;f : 일반적인 주파수 -> 신호가 1초에 몇 번 반복되는지 나타냄, 단위: Hz(헤르츠)= cycles per second(초당 싸이클 수), 주기 T와의 관계 : f = 1/T <br/> 
ω : 각주파수 -> 주파수를 라디안 단위로 변환한 것, 단위는 rad/s(라디안/초), 일반 주파수와의 관계 : ω = 2πf <br/> 
Ω : 이산 주파수 -> 이산 신호에서 사용하는 주파수, 샘플링 주파수 Fs에 대한 상대적인 주파수를 나타냄, 단위는 라디안, 연속 주파수와의 관계 : Ω =  ω/Fs = 2πf/Fs
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-5.png" width="600"></p>

​&ensp;주기 이산 신호(Periodic discrete signal)<br/> 
$x[n] = x[n+N]$ (n이 정수일 경우), $Ω = 2π/N$ (단위 : rad/smple)<br/>
 
&ensp;4. 결정적 신호, 랜덤신호(deterministic signal, random signal)<br/>
======

&ensp;결정적 신호 : 어느 시간에서의 값이 불확실성이 없는 신호<br/>
&ensp;랜덤신호 : 발생 이전에 불확실성이 있는 신호, 그룹에 있는 각 신호는 특정한 발생 확률(probability of occurrence)을 가짐, 그러한 신호의 전체를 랜덤 프로세스(random process)라고 함.<br/>

--------

&ensp;에너지 신호, 전력신호(Energe signal, power signal)<br/>
&ensp;순시전력 : $p(t) = \nu ^{2}(t)/R or p(t) = R\imath ^{2}(t)$<br/>
&ensp;순시 전력 p(t)는 신호의 진폭의 제곱에 비례 특히 1\Omega저항인 경우 위에 식 같은 형태가 됨<br/>
&ensp;normalized power($R = 1\Omega$) : $p(t) = x ^{2}(t)$<br/>
&ensp;연속시간 신호 x(t)의 전체 에너지<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-6.jpg" width="600"></p>
&ensp;평균전력 기본주기가 T인 주기신호 $x(t) : P = \frac{1}{T}\int_{T/2}^{-T/2}x^{2}(t)dt$<br/>
&ensp;평균전력 P의 제곱근 = 신호 x(t)의 실효값(root-mean-square, rms)<br/>
&ensp;이산신호 x[n]의 전체 에너지 $E = \sum_{n=-\infty }^{\infty }x^{2}[n]$<br/>
&ensp;기본주기 가 N인 주기 신호 x[n]의 평균 전력 $P = \frac{1}{N}\sum_{n=-N}^{N}x^{2}[n]$<br/>
0<E<∞를 만족시키면 에너지 신호, 0<P<∞를 만족시키면 전력신호<br/>

&ensp;신호에 대한 기본적인 연산<br/>
&ensp;진폭 스케일링(amplitude scaling) : $y(t) = cx(t), y[n] = cx[n]$<br/>
&ensp;덧셈(addition) :$ y(t) = x₁(t) + x₂(t),  y[t] = x₁[t] + x₂[t]$<br/>
&ensp;곱셈(multiplication) : $y(t) = x₁(t)x₂(t),  y[t] = x₁[t]x₂[t]$<br/>
&ensp;미분(differentiation) : $y(t) =\frac{\mathrm{d} }{\mathrm{d} x}x(t)$<br/>
&ensp;시간 스케일링(time scaling) : $y(t) = x(at), y[n] = x[kn]$<br/>
&ensp;시간 이동(time shifting) : $y(t) = x(t - t₀)$ (t₀는 시간 이동된 간격, t₀>0 -> 시간축에 대하여 오른쪽, t₀<0 -> 왼쪽으로 이동)<br/>

&ensp;5. 기본 신호(Elementary Signals) <br/>
======

&ensp; 지수함수, 삼각함수, 계단함수, 임펄스 함수, 램프 함수 등<br/>

&ensp;1. 지수 신호(exponential signals) : $x(t) = B = e^{at}$ (B, a는 실수)<br/>

&ensp;2. 정현파 신호(sinsoidal signals)<br/>
&ensp;$x(t) = A\cos(\omega t + \phi)$ (A: 진폭, $\omega$: 단위가 rad/sec인 주파수, $\phi$: 단위가 라디안인 위상각)<br/>
&ensp;정현파 신호의 주기 : $T/2\pi/\omega$<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-7.jpg" width="600"></p><br/>
&ensp;이산시간 정현파 신호 : $x[n] = A\cos(\Omega n + \phi)$ -> $x[n + N] = A\cos(\Omega n + \Omega N + \phi)$ ($\Omega N = 2\pi m$  radians 또는 $\Omega = \frac{2\pi m}{N} radians/cycle$ , integer m, N)<br/>

&ensp;3. 정한파 신호와 복소 지수 신호와의 관계<br/>
&ensp;$e^{\iota \theta } = cos\theta + j sin\theta$<br/>
$Be^{j\omega t} = Acos(\omega t + \phi ) + jAsin(\omega t + \phi )$<br/>
$Acos(\Omega n + \phi ) = Re{Be^{j\Omega n}}$<br/>
$Asin(\omega n + \phi ) = Im{Be^{j\omega n}}$<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-8.jpg" width="600"></p>

&ensp;4. 지수적 감쇠 정현파 신호(Exponential Damped Sinusoidal SIgnals)<br/>
&ensp; $x(t) = Ae^{-\alpha t}sin(\omega t + \phi ), \alpha > 0$<br/>
&ensp;A: real number
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-9.jpg" width="600"></p>

&ensp;5. 계단 함수 신호<br/>
======

&ensp;이산시간 계단 함수 신호 -> <p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-10.jpg" width="600"></p>
&ensp;연속시간 계단 함수 신호 -> <p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-11.jpg" width="600"></p>

&ensp;6. 임펄스 신호(Impulse Function)<br/>
======

&ensp;이산시간 임펄스 신호는 다음과 같이 정의된다.<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-12.jpg" width="600"></p>
&ensp;임펄스 신호는 두 개의 식으로 정의된다. <br/>
&ensp;$\delta (t) = 0, t \neq 0 $<br/>
&ensp;$\int_{\infty }^{\infty }\delta (t)dt = 1$<br/>
&ensp;$\delta (t)$가 원점을 제외한 모든 곳에서 0임을 나타낸다. 밑에 있는 식은 단위 임펄스 신호 아래의 전체 면적이 1임을 나타낸다. 임펄스 신호가 계단 함수 신호 $u(t)$의 시간에 대한 미분이라는 것이다. 단위 연속시간 임펄스 신호를 그림으로 나타내는 방법은 펄스 면적이 1을 유지하면서 펄스 폭을 감소시키고 진폭을 증가시킨다. 폭이 감소됨에 따라 구형파 펄스는 임펄스에 근사화된다. 이 결과의 일반화는 
$\delta (t) = \lim_{\Delta \to 0}x_\Delta (t)$ 
이다. 임펄스의 면적은 임펄스 신호의 세기로 정의한다. <br/>
&ensp;$u(t) = \int_{-\infty }^{t} \delta (\tau )d\tau$
&ensp;임펄스와 단위 계단 함수는 특별한 관계를 가지고 있으며 둘 중 하나를 알고 있으면 다른 하나도 표현할 수 있게 된다. <br/>
&ensp;$\delta (t) = \frac{\mathrm{d} }{\mathrm{d} t}u(t)$  $u(t) = \int_{-\infty }^{t} \delta (\tau )d\tau$

&ensp;continuous time impluse functions<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-13.jpg" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-14.jpg" width="600"></p>

&ensp;7. 램프함수(Ramp Function)<br/>
======

&ensp;임펄스 함숭 신호 δ(t)는 계단 함수 신호 u(t)의 도함수이다. 계단 함수 신호의 적분은 기울기가 1인 램프 함수 신호이다.<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-15.jpg" width="600"></p>
&ensp;연속 시간 : δ(t) -> 적분 -> u(t)  / δ(t) <- 미분 <- u(t)<br/>
&ensp;이산 시간 : δ[t] -> 덧셈 -> u[t]  / δ[t] <-뺄셈 <- u[n] - u[n-1]<br/>
&ensp;수학적으로 시스템은 입력 신호를 입력 신호와 다른 특성을 가진 출력 신호로 변환하는 어려 연산의 접속으로 볼 수 있다. 
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-16.jpg" width="600"></p>

&ensp;8. 시스템의 특성<br/>
=====

&ensp;1. 안정성(Stability)<br/>
&ensp;유한 입력에 대하여 출력이 유한이면 시스템이 안정하다고 정의한다. 안정한 시스템의 경우에는 입력이 발산하지 않는다면 출력도 발산하지 않는다. <br/>
&ensp;$\left\| x(t)\right\| \leq M_{x} < \infty$ (모두 t일 경우)<br/>
&ensp;$\left\| y(t)\right\| \leq M_{y} < \infty$ (모두 t일 경우)<br/>

&ensp;2. 기억(memory)<br/>
&ensp;출력 신호가 입력 신호의 과거값의 영향을 받는다면 시스템은 기억이 있다고 한다. 출력에 영향을 주는 과거 시간으이 양은 시스템이 얼마나 많은 과거의 값을 기억하는지를 나타낸다. 반대로 출력 신호가 입력 신호의 현재값에만 의존한다면 무기억 시스템(memory-less)라고 한다. <br/>
&ensp;무기억 : $\imath (t) = \frac{1}{R}\nu (t)$, $y[n] = x^{2}[n]$  (y[n]은 오직 현재의 값 x[n]만 필요하다)<br/>
&ensp; 기억: ex) $y[n] = \frac{1}{3}(x[n] + x[n-1] + x[n-2])$ y[n]은 현재 x[n]과 두 과거 값 x[n-1]과 x[n-2]가 필요하다. <br/>

&ensp;3. 인과성(Causality)<br/>
&ensp;현재의 출력 신호 값이 현재 또는 과거의 입력 신호 값에만 의존한다면 시스템은 인과적(causal)라고 한다. 반대로 비인과적 시스템의 출력 신호는 미래의 입력 신호 값에도 의존한다. <br/>
&ensp; ex) 인과적 : $y[n] = \frac{1}{3}(x[n] + x[n-1] + x[n-2])$ <br/>
&ensp; ex) 비인과적: $y[n] = \frac{1}{3}(x[n+1] + x[n] + x[n-1])$ <br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-17.jpg" width="600"></p>
&ensp;4. 가역성(Invertibility)<br/>
&ensp;입력을 구하기 위해서 주어진 시스템에 종속으로 연결되어 주어진 시스템의 입력과 동일한 신호를 출력하는 2치 시스템이 필요하다.<br/>
&ensp;2차 시스템의 출력 신호 : <br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-18.jpg" width="600"></p>
&ensp;출력 신호가 본래의 입력신호 x(t)와 같기 위해서는 
$$H^{inv}H = I$를 만족해야 한다. 여기서 I는 항등연산자를 표시한다. 항등 연산자로 나타낸 시스템의 출력은 입력과 똑같다.<br/>

&ensp; 4. 시불변(invariance)<br/>
&ensp;입력 신호를 시간 이동시켜서 인가한 경우의 출력 신호가 원래 입력 신호에 대한 출력을 시간 이동시킨 것과 동일하면 시스템이 시불변이라고 한다. 이것은 시불변 시스템의 응답은 입력이 가해지는 순간에 관계 없이 동일하다는 것을 의미한다. 달리 설명하면 시불변 시스템의 특성은 시간에 따라 변하지 않는다는 것이다. 그렇지 않으면 시스템은 시변(time variant)이라고 한다. <br/>
&ensp;time-invariant: y[n] = x[n] + ax[n-1] 
&ensp;어떤 시스템 T가 시불변성을 가지려면 입력 신호 x[n]에 대해 $y[n] = T[x[n]]$ 을 성립해야 한다. 입력 신호 d 만큼 지연(shift)되었을 때 $x[n-d]$ 출력 신호도 같은 방식으로 지연되어야 한다. $T[x[n-d]] = y[n-d]$ <br/>
즉 입력이 이동하면 출력도 동일하게 이동해야 시불변 시스템이라고 할 수 있다.<br/>

&ensp;5. 선형성(linear)<br/>
&ensp;시스템이 아래에 나오는 동차성(homogeneity)과 중첩성(superposition)을 만족한다면 입력 신호 x(t)와 출력 신호 y(t)의 관계는 선형성(linear)이 있다고 말한다. <br/>
&ensp;5-1. 중첩성(susperposition): 초기에 작동하지 않는 시스템에 입력으로 x(t) = x1(t)가 주어지면 출력으로 y(t) = y1(t)가 나온다고 가정한다. 또 같은 시스템에 x(t) = x2(t)인 입력을 인가하면 출력으로 y(t) = y2(t)인 값이 나온다고 가정한다. 이 시스템이 선형성을 가지기 위해서는 입력으로 x(t) = x1(t) + x2(t)를 인가하면 출력으로 y(t) = y1(t) + y2(t)인 값을 출력해야 한다. <br/>
&ensp;5-2. 동차성(homogeneity): 초기에 작동하지 않고 입력으로 x(t)가 인가되면 출려구 y(t)가 출력되는 시스템으로 가정하면 이 시스템이 동차성을 보인다고 말하기 위해서는 입력 x(t)의 크기가 a배로 스케일되면 출력 y(t)의 크기도 a배로 스케일되어야 한다. <br/>
&ensp;$y_{1}(t) = H{x_{1}(t)}$, $y_{2}(t) = H{x_{2}(t)}$ 라면<br/>
&ensp;$a_{1}y_{1}(t) + a_{2}y_{2}(t) = H{a_{1}x_{1}(t) + a_{2}x_{2}(t) }$ 가 성립해야 한다. <br/>
&ensp;입력 x(t)가 여러 개 존재할 경우 다음과 같이 일반화된다. 
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-19.png" width="600"></p>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-20.jpg" width="600"></p>
&ensp;선형성(linearity) 핵심 조건:
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-21.jpg" width="600"></p>






