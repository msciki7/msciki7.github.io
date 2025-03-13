---
title: "1장 Introduction"
excerpt: "Classification of Singals."

wirter: sohee Kim
categories:
  - Singals and Systems
tags:
  - singal, system

toc: true
use_math: true
toc_sticky: true

date: 2025-03-13
last_modified_at: 2025-03-13
---

Classification of Signals
======

&ensp;1. Continuous-time and discrete-time singals</br>
&ensp;continuous-time -> sampling -> discrete-time
<p align="center"><img src="/assets/img/Singals and Systems//1장 Introduction/1-1.png" width="600"></p>

&ensp;All signals can be represented by sum of odd signal and even signal.
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-2.jpg" width="600"></p>

<center>$x(-t) = x*(t)$</center><br/>
<center>$x(t) = a(t) + ib(t)$</center><br/>
<center>$x*(t) = a(t) - ib(t)$</center><br/>
<center>$a(-t) + ib(-t) = a(t) - ib(t)$</center><br/>
its real part is even, its imaginary part is odd
&ensp;Periodic 과 aperiodic singal의 차이점
&ensp;주기적 신호는 일정한 간격 T마다 동일한 패턴이 반복되는 신호. 
&ensp;-연속신호 : x(t) = x(t + T) (T: 기본주기), 주파수 : f = 1/T
&ensp;-이산신호 : x[n] = x[n + N] (N: 기본 주기기) , 주파수 : ω = 2πf = 2π/N

&ensp;주기적 신호 예시 : 1. 사인/코사인 함수 -> x(t) = cos(2πt) : 기본 주기 T = 1, 항상 같은 형태가 반복됨. <br/> 2. 사각파(Square Wave) : 정해진 주기마다 1과 -1이 반복되는 신호.<br/> 3. 펄스열(Impulse Train) : 일정한 간격으로 샘플 값이 존재하는 신호
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-3.jpg" width="600"></p>

&ensp;비주기적 신호는 어떤 주기 T를 찾아도 반복되지 않는 신호. 어떤 T를 넣어도 다음 관계를 만족하는 값이 존재하지 않으면 비주기적 $x(t) \neq x(t+T) $ <br/> 비주기적 신호 예제 <br/> 1. 지수 감쇠 신호 <br/> 2. 랜덤 신호 <br/> 3. 임의의 오디오 신호(사람의 음성 신호는 특정 주기가 없어서 비주기적)<br/> 4. $(-1)^{n^2}$같은 비정형적인 이산 신호(주기가 일정하지 않아 반복되지 않음)

&ensp;cf. 주파수의 기본 개념 : 신호가 주기적으로 변할 때 그 변동 속도를 나타내는 게 주파수. 시간 축에서 신호가 얼마나 빨리 반복된느지 나타내는 척도
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-4.png" width="600"></p>


&ensp;f : 일반적인 주파수 -> 신호가 1초에 몇 번 반복되는지 나타냄, 단위: Hz(헤르츠)= cycles per second(초당 싸이클 수), 주기 T와의 관계 : f = 1/T <br/> ω : 각주파수 -> 주파수를 라디안 단위로 변환한 것, 단위는 rad/s(라디안/초), 일반 주파수와의 관계 : ω = 2πf <br/> Ω : 이산 주파수 -> 이산 신호에서 사용하는 주파수, 샘플링 주파수 Fs에 대한 상대적인 주파수를 나타냄, 단위는 라디안, 연속 주파수와의 관계 : Ω =  ω/Fs = 2πf/Fs
<p align="center"><img src="/assets/img/Singals and Systems/1장 Introduction/1-5.png" width="600"></p>

​&ensp;Periodic discrete signal<br/> 
$x[n] = x[n+N] for integer n, Ω = 2π/N
 
 


실습 문제
======

문제 1
------

`문제`


`코드`
```cpp
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define SEC_PER_MINUTE 60


int main(void) {
	
	printf("222222\n");
	printf("2    2\n");
	printf("2    2\n");
	printf("222222");

	return 0;
}
```

`결과`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-2-실습문제1-실행결과.png"></p>

문제 2
------

`문제`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-3-실습문제2.png" width="600"></p>

`코드`
```cpp
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define SEC_PER_MINUTE 60


int main(void) {
	
	printf("   A\n");
	printf("  A A\n");
	printf(" A   A\n");
	printf("A A A A");
	

	return 0;
}

```

`결과`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-4-실습문제2-실행결과.png"></p>

문제 3
------

`문제`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-5-실습문제3.png" width="600"></p>

`코드`
```cpp
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define SEC_PER_MINUTE 60


int main(void) {
	
	int a;
	scanf("%d", &a);

	printf("%d%d%d%d%d%d\n", a, a, a, a, a, a);
	printf("%d    %d\n", a, a);
	printf("%d    %d\n", a, a);
	printf("%d%d%d%d%d%d\n", a, a, a, a, a, a);

	return 0;
}

```

`결과`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-6-실습문제3-실행결과.png"></p>

문제 4
------

`문제`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-7-실습문제4.png" width="600"></p>

`코드`
```cpp
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define SEC_PER_MINUTE 60


int main(void) {
	
	printf("My birthday is month 3 date 5");

	return 0;
}


```

`결과`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-8-실습문제4-실행결과.png"></p>

문제 5
------

`문제`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-9-실습문제5.png" width="600"></p>

`코드`
```cpp
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define SEC_PER_MINUTE 60


int main(void) {
	
	int month;
	int date;

	scanf("%d\n", &month);
	scanf("%d", &date);

	printf("My birthday is month %d date %d.", month, date);



	return 0;
}


```

`결과`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-10-실습문제5-실행결과.png"></p>

문제 6
------

`문제`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-11-실습문제6.png" width="600"></p>

`코드`
```cpp
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#define SEC_PER_MINUTE 60


int main(void) {
	
	int month;
	int date;

	scanf("%d", &month);
	scanf("%d", &date);

	printf("My birthday is month %d date %d.", month, date);



	return 0;
}

```

`결과`
<p align="center"><img src="/assets/img/C Progrmming and Lab/1장 C 프로그래밍 시작하기/1-12-실습문제6-실행결과.png"></p>