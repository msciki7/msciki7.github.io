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

&ensp;Classification of Signals
-------

&ensp;1. 연속시간 신호와 이산시간 신호(Continuous-time and discrete-time singals)</br>
&ensp;continuous-time -> sampling -> discrete-time
<p align="center"><img src="/assets/img/Singals and Systems//1장 Introduction/1-1.png" width="600"></p>

&ensp;Periodic 과 aperiodic singal의 차이점<br/>
&ensp;주기적 신호는 일정한 간격 T마다 동일한 패턴이 반복되는 신호. <br/>
&ensp;-연속신호 : $x(t) = x(t + T)$ (T: 기본주기), 주파수 : $f = 1/T (T = 2π/ω)$<br/>
&ensp;-이산신호 : $x[n] = x[n + N]$ (N: 기본 주기기) , 주파수 : $ω = 2πf = 2π/N$<br/>
이산시간 신호는 연속시간 신호를 일정한 비율로 샘플링하여 얻는다. (샘플링(sampling): 메시지 신호를 특정 순간에서 그 진폭을 나타내는 일련의 수로 변환)<br/>

&ensp;2. 우함수 신호와 기함수 신호(Even and Odd signals)<br/>
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

&ensp;기본 신호(Elementary Signals) <br/>
&ensp; 지수함수, 삼각함수, 계단함수, 임펄스 함수, 램프 함수 등<br/>

&ensp;1. 지수 신호(exponential signals) : $x(t) = B = e^{at}$ (B, a는 실수)<br/>

&ensp;2. 정현파 신호(sinsoidal signals)<br/>
&ensp;$x(t) = A\cos(\omega t + \phi)$ (A: 진폭, $\omega$: 단위가 rad/sec인 주파수, $\phi$: 단위가 라디안인 위상각)<br/>
&ensp;정현파 신호의 주기 : $T/2\pi/\omega$<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-7.jpg" width="600"></p><br/>
&ensp;이산시간 정현파 신호 : $x[n] = A\cos(\Omega n + \phi)$ -> $x[n + N] = A\cos(\Omega n + \Omega N + \phi)$ ($\Omega N = 2\pi m$  radians 또는 $\Omega = \frac{2\pi m}{N} radians/cycle$ , integer m, N)<br/>

&ensp;정한파 신호와 복소 지수 신호와의 관계<br/>
&ensp;$e^{\iota \theta } = cos\theta + j sin\theta$<br/>
$Be^{j\omega t} = Acos(\omega t + \phi ) + jAsin(\omega t + \phi )$<br/>
$Acos(\Omega n + \phi ) = Re{Be^{j\Omega n}}$<br/>
$Asin(\omega n + \phi ) = Im{Be^{j\omega n}}$<br/>
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-8.jpg" width="600"></p>


