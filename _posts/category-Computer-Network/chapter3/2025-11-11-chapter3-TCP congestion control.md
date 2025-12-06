---
title: "chapter3. Transport Layer(소단원 7~8)"
excerpt: ""

wirter: sohee Kim
categories:
  - Computer Network
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-11-11
last_modified_at: 2025-11-14
---

TCP congestion control
=====

TCP Congestion Control: AIMD
----

&ensp;TCP는 혼잡이 감지될 때까지 전송 속도를 점점 늘리고 혼잡이 발생하면 전송 속도를 급격히 줄이는 방식을 사용한다. 이를 AIMD(Addition Increases / Multiplicative Decrease) 라고 부른다.<br/>

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-67.png" width="500"></p>

1. Additive Increase (선형 증가)
* 송신자는 매 RTT마다(즉, ACK가 한 바퀴 돌 때마다) 전송 속도(cwnd: congestion window) 를 조금씩 증가시킨다.
* 증가량: 1 MSS (Maximum Segment Size) → 즉, "매 RTT마다 1세그먼트씩 더 보내본다"
* 이 과정을 통해 네트워크 용량을 탐색(probing for bandwidth) 한다.

&ensp;그래프의 왼쪽 위로 완만하게 올라가는 부분이 바로 "Additive Increase"이다. 시간이 지날수록 cwnd가 점점 커진다.<br/>

&ensp;2. Multiplicative Decrease (지수 감소)<br/>
* 패킷 손실(loss)이 발생하면 → 네트워크가 혼잡하다고 판단
* 송신자는 즉시 전송 속도를 절반으로 감소시킨다.
* cwnd = cwnd / 2

&ensp;그래프가 위로 올라가다가 급격히 떨어지는 부분이 손실(혼잡) 이후 속도를 줄이는 단계이다. 이런 형태가 반복되면서 “톱니 모양(Sawtooth)” 패턴이 생긴다.<br/>

| 구분                      | 방식                 | 의미             |
| ----------------------- | ------------------ | -------------- |
| Additive Increase       | 매 RTT마다 cwnd 1씩 증가 | 점진적으로 대역폭 탐색   |
| Multiplicative Decrease | 손실 발생 시 cwnd 절반 감소 | 혼잡 발생 시 빠르게 반응 |
| 결과                      | 톱니형(sawtooth) 패턴   | 네트워크의 안정적인 활용  |

&ensp;TCP AIMD: 세부 동작<br/>
1. Triple Duplicate ACK (TCP Reno 방식)
* 같은 ACK가 3번 연속 수신되면 → 패킷 하나가 유실되었다고 판단
* 전송 속도(=cwnd)를 절반으로 감소시킨다. → cwnd = cwnd / 2
2. Timeout 발생 (TCP Tahoe 방식)
* ACK가 너무 오랫동안 도착하지 않으면 → 심각한 혼잡으로 판단
* 전송 속도를 1 MSS로 초기화 (거의 처음부터 다시 시작) → cwnd = 1 MSS

&ensp;Why AIMD?<br/>
&ensp;AIMD는 단순히 알고리즘이지만 이점이 많다.<br/>
* 분산적(distributed): 각 TCP 송신자가 독립적으로 실행 가능
* 비동기적(asynchronous): 동시에 시작하지 않아도 안정적
* 효율적(optimized): 네트워크 전체의 대역폭을 공정하게 나눔
* 안정적(stable): 너무 빠르게 변화하지 않아 전체 네트워크에 진동(oscillation)을 유발하지 않음

&ensp;AIMD는 네트워크 전체의 효율과 공정성을 모두 만족시키는 알고리즘<br/>

&ensp;TCP Congestion Control: Details<br/>
* TCP의 전송 제어 단위: cwnd (Congestion Window)
    - 송신자는 한 번에 전송할 수 있는 데이터 양을 cwnd로 제한한다.
    - cwnd는 네트워크 상태에 따라 AIMD 방식으로 실시간 조절된다.

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-68.png" width="500"></p>

| 구간      | 의미                               |
| ------- | -------------------------------- |
| **초록색** | 이미 ACK 받은 데이터 (확인 완료)            |
| **노란색** | 보냈지만 아직 ACK 안 받은 데이터 (in-flight) |
| **파란색** | 아직 보내지 않은 데이터 (전송 대기 중)          |

&ensp;cwnd는 이 in-flight 데이터의 총량(즉, 미확인 상태인 바이트 수)을 제한<br/>
&ensp;`LastByteSent - LastByteAcked ≤ cwnd` 가 항상 성립한다. → 이 조건이 혼잡 제어의 핵심 규칙<br/>

&ensp;전송 속도 계산<br/>
&ensp;TCP 전송 속도는 대략 다음과 같이 계산된다.<br/>
&ensp;`TCP rate ≈ cwnd / RTT  (bytes/sec)` <br/>
* cwnd가 크면: 더 많은 데이터를 한 번에 보냄 → 전송 속도 ↑
* RTT가 크면: 왕복 시간이 길어져 ACK 회신이 느림 → 전송 속도 ↓

| 항목            | 설명                                |
| ------------- | --------------------------------- |
| **cwnd**      | 혼잡 윈도우 크기, 현재 네트워크 상황에 따라 동적으로 변화 |
| **RTT**       | 왕복 지연 시간, 속도 계산에 직접 영향            |
| **패킷 손실**     | 혼잡 신호 → cwnd 감소                   |
| **ACK 정상 수신** | 혼잡 완화 → cwnd 증가                   |

&ensp;기본 용어<br/>
* cwnd(congestion window): 송신자가 동시에 네트워크로 날려 둘 수 있는 바이트 수 (미확인 in-flight 데이터 한도). 전송 속도는 대략 rate ≈ cwnd / RTT
* MSS: TCP 세그먼트 페이로드 최대 크기
* ssthresh(slow-start threshold): slow start를 그만두고 선형 증가로 바꾸는 경계 값
* loss 감지 방법
    - timeout: 타이머 만료(심각한 손실로 간주)
    - 중복 ACK 3개(Triple dupACK): 특정 세그먼트가 빠졌음을 암시(경미한 손실로 간주)

Slow start
-----

&ensp;목표: 초기 전송률을 빠르게(지수적으로) 끌어올리되 첫 손실 직전까지만<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-69.png" width="500"></p>

* 시작: cwnd = 1 MSS
* 매 RTT마다 cwnd가 2배: 매 ACK 수신 시 `cwnd += MSS` → 한 RTT 동안 대략 `+(#ACK ≈ cwnd/MSS)`. 즉 배가 됨
* 종료 트리거:
    - 손실 발생(timeout 또는 dupACK 3개) 또는
    - cwnd ≥ ssthresh(임계 도달) → 선형 증가 단계로 전환

&ensp;요약: 초기는 느리지만 곧바로 지수 증가로 매우 빠르게 치고 올라간다.<br/>

&ensp;Congestion avoidance 전환<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-70.png" width="500"></p>

* 언제 전환? 첫 손실 직전 cwnd 값의 절반을 `ssthresh` 로 두고 그 이후는 선형 증가로 운용
* 구현 규칙:
    - 손실 이벤트가 나면 `ssthresh = cwnd / 2 (직전 값의 반)` 로 설정

&ensp;혼잡 회피(AIMD) + 손실 처리 규칙<br/>
&ensp;AIMD 동작(평상시)<br/>
* Additive Increase(가볍 증가): 혼잡 없으면 매 RTT마다 cwnd를 1 MSS씩 증가 → 선형 톱니("sawtooth")
* Multiplicative Decrease(곱절 감소): 손실 감지 시 cwnd를 절반으로 감소

&ensp;손실별 세부 처치<br/>
&ensp;Triple dupACK (TCP Reno 가정)<br/>
&ensp;네트워크는 살아있고 일부 세그먼트만 빠졌다로 판단<br/>
1. `ssthresh = cwnd / 2`
2. cwnd = ssthresh + 3*MMSH (dupACK 3개 보정)
3. 빠진 세그먼트를 즉시 재전송 → Fast Recovery 진입
4. 새로운 정상 ACK(누락분까지 커버)가 오면 cwnd = ssthresh 로 놓고 Congestion Avoidance로 복귀(선형 증가 재개)

&ensp;Timeout (TCP Tahoe/Reno 공통 처리)<br/>
&ensp;더 심각한 혼잡으로 판단<br/>
1. `ssthresh = cwnd / 2`
2. cwnd = 1 MSS 로 리셋
3. 누락 세그먼트 재전송 후 Slow Start 로 재진입 → `cwnd` 가 `ssthresh` 에 도달하면 다시 Congestion Avoidance로 전환

&ensp;TCP 혼잡 제어 전체 흐름의 핵심 요약도<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-71.png" width="500"></p>

&ensp;전체 구조 한눈에 보기<br/>
&ensp;TCP는 혼잡 제어를 위해 3가지 주요 상태(state)를 둔다.<br/>

| 상태                          | 역할                         | 증가 방식                       |
| --------------------------- | -------------------------- | --------------------------- |
| 🟢 **Slow Start**           | 처음 연결 시 or timeout 후 빠른 증가 | **지수적 증가**                  |
| 🔵 **Congestion Avoidance** | 네트워크 안정 상태에서 조심스러운 증가      | **선형 증가 (AIMD)**            |
| 🟠 **Fast Recovery**        | 중복 ACK 발생 시 빠른 복구          | **빠진 세그먼트만 재전송하고 선형 증가 복귀** |

&ensp;TCP는 ACK, duplicate ACK, timeout을 이벤트로 삼아 이 상태들 사이를 전이한다.<br/>

&ensp;각 상태별 동작과 이벤트<br/>
&ensp;(1) Slow Start 단계<br/>
&ensp;특징<br/>
* 연결 시작 시 또는 타임아웃 이후 진입
* `cwnd`(congestion window)가 작기 때문에 아주 천천히 시작
* 하지만 매 RTT마다 2배씩 빠르게 증가(지수적 증가)
* `ssthresh` (slow-start threshold)를 넘어가면 Congestion Avoidance로 전환

&ensp;;공식<br/>
```makefile
cwnd = 1 MSS  (처음)
→ ACK 하나 받을 때마다 cwnd += 1 MSS
→ RTT 한 번 돌면 cwnd가 2배가 됨
```

&ensp;전환 조건<br/>
* `cwnd ≥ ssthresh` → Congestion Avoidance로 이동
* 손실(timeout or 3 duplicate ACK)발생 → `ssthresh = cwnd/2` 후 복구 절차로

&ensp;(2) Congestion Avoidance 단계<br/>
&ensp;특징<br/>
* 네트워크가 포화 상태에 가까워지면 더 이상 지수적으로 증가하면 안 됨
* 그래서 선형 증가(Additive Increase)방식으로 천천히 늘려감

&ensp;공식<br/>
```makefile
매 RTT마다 cwnd += 1 MSS
(ACK 1개당 cwnd += MSS*(MSS/cwnd))
```

&ensp;전환 조건<br/>
* 손실 발생
    - dupACK × 3 → Fast Recovery로 이동
    - timeout 발생 → Slow Start로 이동

&ensp;(3) Fast Recovery 단계<br/>
&ensp;트리거<br/>
* 중복 ACK 3개(dupACK == 3)발생 시 진입
* 이건 패킷이 1개 빠졌지만 그 뒤로는 도착 중이야 라는 신호 → 즉, 네트워크는 살아있고 전체 혼잡은 아님

&ensp;동작 순서<br/>
1. `ssthresh = cwnd / 2`
2. `cwnd = ssthresh + 3*MSS` ← 이미 3개의 dupACK 받았기 때문
3. 빠진 세그먼트 재전송 (retransmit missing segment)
4. 새 ACK 수신 시 → cwnd = `ssthresh` 로 맞추고 Congestion Avoidance 상태로 복귀

&ensp;의미<br/>
* 완전히 slow start로 돌아가지 않고 빠진 부분만 빠르게 복구하자는 개념 (성능 향상)

&ensp;Timeout (타임아웃) 발생 시 처리<br/>
* 가장 심각한 혼잡 상황으로 간주
* 모든 상태에서 timeout 발생 시 Slow Start로 돌아감

&ensp;동작<br/>
```makefile
ssthresh = cwnd / 2
cwnd = 1 MSS
dupACKcount = 0
(누락 세그먼트 재전송)
```

&ensp;네트워크가 거의 마비 상태라고 판단하고 다시 처음부터 천천히 시작<br/>

&ensp;전체 동작 흐름 정리<br/>

| 이벤트                                | 변화                                    | 다음 상태                |
| ---------------------------------- | ------------------------------------- | -------------------- |
| **새 ACK 수신**                       | cwnd 증가                               | 현재 상태 유지             |
| **dupACK (3 미만)**                  | 누락 가능성 체크 (카운트만 증가)                   | 현재 상태 유지             |
| **dupACK == 3**                    | 빠진 세그먼트 재전송                           | Fast Recovery        |
| **timeout 발생**                     | cwnd ↓ (1 MSS로 리셋), ssthresh = cwnd/2 | Slow Start           |
| **cwnd ≥ ssthresh (slow start 중)** | 증가 방식 변경                              | Congestion Avoidance |

&ensp;핵심 키워드<br/>

| 이벤트                                | 변화                                    | 다음 상태                |
| ---------------------------------- | ------------------------------------- | -------------------- |
| **새 ACK 수신**                       | cwnd 증가                               | 현재 상태 유지             |
| **dupACK (3 미만)**                  | 누락 가능성 체크 (카운트만 증가)                   | 현재 상태 유지             |
| **dupACK == 3**                    | 빠진 세그먼트 재전송                           | Fast Recovery        |
| **timeout 발생**                     | cwnd ↓ (1 MSS로 리셋), ssthresh = cwnd/2 | Slow Start           |
| **cwnd ≥ ssthresh (slow start 중)** | 증가 방식 변경                              | Congestion Avoidance |

&ensp;TCP 혼잡 제어는 초기엔 빠르게 (지수 증가) 안정기엔 천천히 (선형 증가) 혼잡 시 빠르게 반응 (감소 및 복구)하는 AIMD 기반 적응 제어 시스템이다.<br/>

TCP CUBIC
-----

&ensp;TCP CUBIC 개요<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-72.png" width="500"></p>

&ensp;AIMD보다 더 똑똑하게 대역폭을 탐색할 수 없을까?<br/>
* AIMD는 항상 선형 증가 → 손실 → 반감 패턴이라 대역폭을 “톱니형(sawtooth)”으로 탐색함
* 이 과정에서 손실 직전 속도(Wₘₐₓ) 를 매번 잊고, 다시 그 근처까지 “기어올라가는” 비효율이 있음

&ensp;CUBIC의 핵심 직관<br/>
* `Wₘₐₓ`: 손실이 일어난 당시의 윈도 크기 (그때의 대역폭)
* 병목 구간의 상황이 크게 변하지 않았다면 다음 혼잡 제어 주기에서 그 Wₘₐₓ 근처가 여전히 한계점일 가능성이 높음

| 단계          | 설명                                                  |
| ----------- | --------------------------------------------------- |
| 1. 손실 발생 시 | cwnd(혼잡 윈도)를 ½로 줄임 (`Wₘₐₓ/2`)                       |
| 2. 그 후     | **초반엔 빠르게 증가**, **Wₘₐₓ에 가까워질수록 천천히 증가**             |
| 3. 이유      | 네트워크 혼잡을 최소화하면서, **이전의 최대 대역폭(Wₘₐₓ)을 기준으로 탐색**하기 위해 |

&ensp;TCP CUBIC의 수학적 개념<br/>
&ensp;개념적 변수 "K" <br/>
* K: TCP 윈도우 크기가 Wₘₐₓ에 도달할 시간 시점(time point)
    - 이번 주기에서 언제 Wₘₐₓ에 닿을까?”를 미리 계산
    - K 값은 조정 가능(tuneable)

&ensp;CUBIC의 증가 함수<br/>
* CUBIC은 W(t) (현재 윈도우 크기)를 시간과 K의 차이의 3제곱(cube)함수로 <br/>

```mathematica
W(t) = C * (t - K)^3 + Wₘₐₓ
```

&ensp;여기서 C는 상수 (증가 속도 조정 파라미터)<br/>

&ensp;동작 방식<br/>

| 구간         | 특징                                          |
| ---------- | ------------------------------------------- |
| K에서 멀리 떨어짐 | (t가 K보다 훨씬 작을 때) → (t−K)³ 커짐 → 빠르게 증가       |
| K 근처 접근    | (t가 K에 가까울 때) → 증가량 작아짐 → 천천히 증가 (조심스럽게 접근) |
| Wₘₐₓ 도달 후  | 잠시 정체 → 안정화 후 새로운 손실 시 반감                   |

&ensp;그래프 해석<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-73.png" width="500"></p>

* 빨간선: TCP Reno (AIMD) - 직선 증가, 손실 시 반감
* 파란선: TCP CUBIC - 곡선 증가, 초반 급상승 → 후반 완만 → 손실 후 재시도
* 결과: 손실 구간 사이의 평균 cwnd가 Reno보다 큼 → 더 높은 전송 효율

&ensp;정리<br/>
* TCP CUBIC은 “시간 기반(window vs time)” 방식의 혼잡 제어
* 오늘날 Linux의 기본 TCP 알고리즘(default) 이며 대부분의 웹 서버(Nginx, Apache,Google 등)가 기본적으로 CUBIC을 사용함

&ensp;TCP와 병목 링크(bottleneck link)<br/>
&ensp;혼잡은 네트워크 어딘가의 병목 링크에서 발생<br/>
* TCP는 전송률을 계속 올리며 패킷을 보냄
* 그런데 네트워크의 한 구간(라우터 출력 큐 등)은 항상 가장 느린 구간. 즉 bottleneck link임
* 여기서 버퍼가 꽉 차면 패킷이 손실됨 → 그 시점이 혼잡 발생 시점

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-74.png" width="500"></p>

* 송신측(source)의 TCP는 계속 데이터를 큐에 밀어넣음
* 병목 링크 구간(빨간 부분)은 항상 거의 꽉 찬 상태(almost always busy)
* 큐가 다 차면 일부 손실 → TCP가 이를 혼잡으로 인식

&ensp;결론<br/>
* TCP(클래식, CUBIC 둘 다)는 결국 이 bottleneck link의 용량을 기준으로 조절함
* 혼잡 제어의 핵심은 병목 구간에서 손실이 일어나지 않도록 파이프를 꽉채우되 넘치지 않게 유지 하는 것

&ensp;혼잡 이해의 핵심 목표<br/>
&ensp;네트워크 버퍼에 데이터를 충분히 채워서 대역폭 낭비 없이 사용하면서도 너무 많이 보내서 지연(RTT 증가)나 패킷 손실이 생기지 않게 해야 한다.<br/>

&ensp;추가 인사이트<br/>
* 보내는 속도 증가 → RTT 증가
    - RTT가 커지는 건 큐가 쌓이기 때문 → 혼잡 징후
* 보내는 속도 증가해도 처리량이 늘지 않음 → 이미 병목에 도달한 것

&ensp;TCP의 설계 목표<br/>
* TCP는 이런 병목 구간을 스스로 감지하고 조절함
* AIMD나 CUBIC 모두 기본 목표는 동일: 병목 링크를 100% 활용하되 오버플로우로 손실을 일으키지 말자


| 구분          | Classic TCP (Reno, AIMD)                                 | TCP CUBIC              |
| ----------- | -------------------------------------------------------- | ---------------------- |
| **증가 방식**   | 선형 (Additive Increase)                                   | 시간 기반 3차 함수 (Cube)     |
| **감소 방식**   | 손실 시 cwnd 반감                                             | 동일하게 반감, 이후 곡선 증가      |
| **Wₘₐₓ 활용** | 잊음 (매번 새로 탐색)                                            | 기억함 (그 근처를 기준으로 곡선 탐색) |
| **증가 속도**   | 일정 (선형)                                                  | 초반 빠르고, Wₘₐₓ 근처 느려짐    |
| **효율성**     | 낮음 (톱니형 손실 반복)                                           | 높음 (평균 처리율 ↑)          |
| **기본 OS**   | 옛 TCP                                                    | Linux 기본 (CUBIC)       |
| **공통 목표**   | 병목 링크를 가득 채우되 넘치지 않게 (keep the pipe full but not fuller) |                        |

Delay-based TCP Congestion Control (지연 기반 TCP 혼잡 제어)
-----

&ensp;기존 TCP(Reno, CUBIC)는 패킷이 손실된 후에야 혼잡을 인식했다. 하지만 delay-based TCP는 손실이 일어나기 전에 RTT(왕복 지연 시간)이 늘어나면 혼잡이 시작됐다. 고 판단한다. 즉 손실 발생 없이 RTT 변화를 통해 혼잡을 미리 감지하고 제어하는 방식이다.<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-75.png" width="500"></p>

&ensp;동작원리<br/>
1. RTT 측정: 송신자는 매번 패킷의 RTT(왕복 시간)를 측정한다.
    - `RTT_measured` : 현재 측정된 RTT
    - `RTT_min`: 지금까지 관찰된 가장 짧은 RTT(비혼잡 상태의 RTT)
2. 기준 설정: RTT가 `RTT_min` 보다 길어지면 → 큐에 데이터가 쌓이고 있다는 뜻 → 혼잡이 시작된 것
3. throughput(처리율) 계산: measured throughput = (보낸 데이터 양) / (RTT_measured)
    - 만약 `RTT_measured`가 커지면 → 처리율이 낮아짐.
4. 제어 규칙:

```makefile
if measured throughput ≈ uncongested throughput
    → cwnd 선형 증가 (더 보내도 혼잡 아님)
else if measured throughput << uncongested throughput
    → cwnd 선형 감소 (혼잡 상태)
```

&ensp;파이프를 꽉 채우되 넘치지 않게 링크는 계속 바쁘게 유지하되 대기 지연(buffering delay)은 최소화하는 것<br/>


&ensp;주요 특징<br/>

| 항목          | 설명                                                           |
| ----------- | ------------------------------------------------------------ |
| **핵심 아이디어** | 손실(loss)을 기다리지 않고 **RTT 증가로 혼잡 감지**                          |
| **장점**      | 패킷 손실 발생 X → 지연 적고 안정적                                       |
| **단점**      | 다른 loss-based TCP와 함께 있을 때 **공평성(fairness)** 문제              |
| **목표**      | 처리율 최대화 + 지연 최소화                                             |
| **예시 프로토콜** | **BBR (Bottleneck Bandwidth and RTT)** — Google 내부 네트워크에서 사용 |

Explicit Congestion Notification (ECN) - "명시적 혼잡 알림"
-----

&ensp;Network-assisted 방식이다. 단말(TCP 송신자/수신자)끼리 혼자 추측하지 않고 네트워크 라우터가 직접 혼잡 상태를 알려주는 방식이다.<br/>

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-76.png" width="500"></p>

&ensp;동작 과정<br/>
1. 혼잡 감지 (라우터)
* 라우터는 큐가 꽉 차기 전에 곧 혼잡이 될 것 같다고 판단
* 패킷을 버리지 않고 IP 헤더의 ECN 비트를 세팅한다.
    - ECN 비트는 IP 헤더의 ToS(서비스 유형)필드에 있음
    - 2비트를 사용 (예: 10 또는 11)
2. 수신자에게 알림
    - 혼잡 비트가 표시된 IP 패킷을 받은 수신자(destination)는 ACK 세그먼트를 보낼 때 TCP 헤더의 ECE(ECN Echo)비트를 1로 설정해서 송신자에게 보냄
3. 송신자 반응
    - 송신자는 ECE = 1 ACK 를 받으면 "네트워크가 혼잡하구나" 라고 판단 → cwnd를 줄여 전송 속도를 낮춤

| 단계 | 담당       | 동작                                         |
| -- | -------- | ------------------------------------------ |
| ①  | Router   | 혼잡 감지 후 IP 헤더에 **ECN=10** 또는 **ECN=11** 마킹 |
| ②  | Receiver | ACK의 TCP 헤더에 **ECE=1** 설정                  |
| ③  | Sender   | ECE 수신 → 혼잡 판단 후 cwnd 감소                   |

&ensp;ECN의 장점<br/>

| 장점              | 설명                           |
| --------------- | ---------------------------- |
| **손실 없는 혼잡 제어** | 패킷을 버리지 않고, 단지 비트 마킹으로 혼잡 알림 |
| **지연 감소**       | 큐가 꽉 차기 전에 미리 제어             |
| **네트워크 효율 향상**  | 손실 복구(재전송) 부담 감소             |


TCP Fairness
----

&ensp;여러 개의 TCP 세션이 동일한 병목 링크(bottlenect link)를 공유할 때 각 세션은 그 링크의 총 용량 R을 공평하게 나누어 사용해야 한다.<br/>

* 병목 링크의 전체 대역폭이 R Mbps
* 동시에 K개의 TCP 세션이 존재한다면 → 각 세션은 평균 R/K의 전송률을 가져야 한다.

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-77.png" width="500"></p>

* 두 개의 TCP 연결(Connection 1, Connection 2)이 하나의 라우터의 병목 링크 (capacity R)를 공유 중
* 두 연결이 서로 경쟁하지만 TCP의 혼잡 제어(AIMD) 덕분에 결과적으로 두 연결의 평균 속도는 R/2에 수렴하게 됨

&ensp;TCP는 공정할까?<br/>

&ensp;가정<br/>
* 두 개의 TCP 세션이 하나의 병목 링크를 공유
* TCP는 AIMD(Additive Increase, Multiplicative Decrease)를 사용함

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-78.png" width="500"></p>

* X축: 연결 1의 처리율 (Throughput)
* Y축: 연결 2의 처리율 (Throughput)
* 파란 선: X + Y = R → 두 연결의 합이 링크 용량을 초과하지 않음.
* 점선 대각선: X = Y → 두 연결이 공평하게 나눠 쓰는 상태.

&ensp;동작 과정<br/>
* TCP는 다음 규칙을 따름
1. Additive Increase: 각 연결이 조금씩 선형으로 속도를 증가 → 화살표가 대각선 방향(오른쪽 위)으로 이동
2. Multiplicative Decrease: 손실 발생 시 속도를 절반으로 감소 → 화살표가 왼쪽 아래로 이동

&ensp;이 과정을 반복하다 보면 두 연결은 결국 공평한 대각선(equal bandwidth share line) 근처로 수렴하게 된다.<br/>

&ensp;결론<br/>
&ensp;두 연결의 RTT가 동일하고 모두 congestion avoidance 단계에 있을 때 TCP는 이상적인 상황에서는 공평한 대역폭 분배를 자동으로 이뤄낸다.<br/>

&ensp;현실에서는 TCP가 항상 공정하지 않다.<br/>
&ensp;(1) Fairness and UDP<br/>
&ensp;문제점<br/>
* UDP는 혼잡 제어를 하지 않음
    - 멀티미디어(영상, 음성) 앱은 전송 속도를 일정하게 유지해야 하므로 TCP처럼 스스로 속도를 줄이지 않음
    - 대신 일부 손실을 감수하면서 지속 전송

&ensp;결과<br/>
* UDP는 혼잡 시에도 계속 보냄 → TCP 세션이 손해를 봄.
* 즉 UDP는 "비공평(fairness-unfriendly)" 프로토콜.
* 인터넷에는 "혼잡 제어 경찰(Internet police)" 같은 게 없기 때문에 누가 혼잡 제어를 무시하더라도 강제할 방법이 없음.

&ensp;(2) Fairness and Parallel TCP Connections<br/>
&ensp;문제점<br/>
* 어떤 앱은 한 세션이 아닌 여러 개의 TCP 연결을 동시에 열어 대역폭을 더 차지함

&ensp;예를 들어 웹브라우저(Chrome, Edge 등)는 한 웹페이지를 불러올 때 여러 파일을 동시에 받기 위해 여러 TCP 연결을 생성한다.<br/>

&ensp;예시<br/>
* 병목 링크 용량: R
* 기존 9개의 TCP 연결이 있음 → 각자 R/9 속도로 사용 중.
* 새 앱이 한 개의 TCP 연결만 연다면 → R/10.
* 그런데 어떤 앱이 11개의 병렬 연결을 연다면? → 그 앱의 총 전송률은 R/2에 달함.

&ensp;병렬 TCP 연결은 일종의 불공평한 꼼수가 됨<br/>

Evolution of transport-layer functionality
======

&ensp;개념: TC다.P와 UDP는 지난 40년간 인터넷의 핵심 전송 계층 프로토콜이었지만, 인터넷 환경이 복잡해지면서 “기존 TCP만으로는 부족”한 상황들이 생겼다. 그래서 여러 특화된 버전의 TCP(flavors of TCP)가 만들어졌다.<br/>

&ensp;시나리오별 문제점 정리<br/>

| 시나리오                                    | 주요 문제(Challenge)                                                 |
| --------------------------------------- | ---------------------------------------------------------------- |
| **Long, fat pipes (대용량 데이터 전송)**        | 한 번에 “in flight” 패킷이 많아서 손실이 발생하면 전체 전송이 중단됨 (ex: 위성 통신, 고속 백본망) |
| **Wireless networks (무선망)**             | 전파 잡음, 이동성으로 인한 손실 → TCP는 이걸 혼잡으로 오해하고 속도를 줄여버림                  |
| **Long-delay links (장거리 링크)**           | RTT가 매우 커서 전송 속도 회복이 느림                                          |
| **Data center networks (데이터센터 내부)**     | 지연(latency)에 매우 민감함 (마이크로초 단위 지연도 문제)                            |
| **Background traffic flows (백그라운드 전송)** | 낮은 우선순위, 다른 트래픽에 영향 최소화해야 함                                      |


&ensp;그래서 생긴 변화<br/>
&ensp;최신엔 TCP의 한계를 보완하기 위해 전송 계층의 일부 기능을 애플리케이션 계층으로 옮김<br/>

QUIC
----

&ensp;Quick UDP Internet Connections<br/>
&ensp;핵심 개념<br/>
* QUIC은 UDP 기반의 애플리케이션 계층 프로토콜이다.
* TCP를 완전히 대체하지 않고 UDP 위에서 TCP의 기능을 구현한 형태이다.

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-79.png" width="500"></p>

&ensp;목적<br/>
1. HTTP 성능 향상 (특히 HTTP/3에서)
2. TCP보다 더 빠른 연결 설정, 더 나은 병렬 전송

&ensp;비교 구조<br/>

| 계층          | HTTP/2 | HTTP/3                |
| ----------- | ------ | --------------------- |
| Application | HTTP/2 | **HTTP/3**            |
| Security    | TLS    | **TLS 내장 (QUIC에 포함)** |
| Transport   | TCP    | **UDP 기반 QUIC**       |
| Network     | IP     | IP                    |

&ensp;HTTP/2 over TCP → HTTP/3 over QUIC (UDP) 로 진화한 셈<br/>

&ensp;QUIC: 내부 동작 구조<br/>
&ensp;QUIC은 사실 TCP의 기능을 거의 모두 재구현했다.<br/>
1. Error & Congestion Control
* 손실 감지, 혼잡 제어 알고리즘은 TCP와 유사하게 동작
* 다만 UDP 기반이라 더 빠르고 유연하게 동작 가능
2. Connection Establishment(연결 설정)
* TCP의 신뢰성, 혼잡 제어, 암호화(TLS 기능)을 모두 포함한 하나의 통합 핸드셰이크(one RTT handshake) 구조
3. Multiplexing Streams
* 하나의 QUIC 연결 안에서 여러 데이터 스트림(Streams)을 병렬로 전송 가능
* 각 스트림의 별도의 신뢰성/보안 관리를 하면서 공통의 혼잡 제어(cwnd)를 공유

&ensp;다중 스트림 + 낮은 지연 + 보안 내장형 전송 프로토콜<br/>

&ensp;Connection Establishment<br/>
&ensp;기존 TCP + TLS의 문제<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-80.png" width="500"></p>

1. TCP Handshake (2-way handshake)
2. TLS Handshake (보안 인증, 암호화 키 교환) → 순차적으로 이루어져야 해서 총 2개의 왕복 지연(RTT) 필요

&ensp;실제 데이터 전송이 시작되기 전까지 느림<br/>

&ensp;QUIC의 개선점<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-81.png" width="500"></p>

* QUIC은 위 두 과정을 하나로 합침 (1 RTT handshake)
* 신뢰성, 혼잡 제어, 인증, 암호화 모두 한 번에 수행
* 1 handshake = 보안 + 전송 동시에 확립

&ensp;결과: 페이지 로딩 속도 등 실사용 체감이 매우 빨라짐<br/>

&ensp;Streams & No HOL Blocking<br/>
&ensp;HOL Blocking (Head-Of-Line Blocking) 문제<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-82.png" width="500"></p>

&ensp;TCP는 순서 보장(Reliable, In-order) 때문에 한 패킷이라도 손실되면 그 뒤 패킷 전부 대기 상태가 됨<br/>
&ensp;여러 개의 요청(HTTP GET)을 동시에 보내도 하나가 손실되면 전체가 멈추는 문제 발생(특히 HTTP/1.1, HTTP/2)<br/>

&ensp;QUIC의 해결책<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-83.png" width="500"></p>

&ensp;QUIC은 Stream 단위의 독립적 신뢰성 보장을 함.<br/>
* 여러 Stream이 하나의 연결을 공유하지만 각 Stream의 손실과 상관없이 동작 가능
* 따라서 병령성(parallelism) 확보 + HOL blocking 없음

&ensp;전체 요약표<br/>

| 구분                | TCP              | QUIC                         |
| ----------------- | ---------------- | ---------------------------- |
| **기반 프로토콜**       | IP 위의 TCP        | **UDP 위의 QUIC**              |
| **계층**            | 전송 계층            | **애플리케이션 계층 (UDP 기반)**       |
| **핸드셰이크**         | 2회 (TCP + TLS)   | **1회 (통합)**                  |
| **혼잡 제어 / 오류 제어** | 있음               | 있음 (TCP 유사)                  |
| **보안 (TLS)**      | 별도               | **내장형**                      |
| **병렬 전송**         | HOL blocking 있음  | **Stream 병렬 전송, HOL 없음**     |
| **대표 사용**         | HTTP/1.1, HTTP/2 | **HTTP/3 (Chrome, YouTube)** |

추가 개념
=====

Go-Back-N
-----

&ensp;Sender FSM<br/>
&ensp;핵심 개념<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-84.png" width="500"></p>

* Go-Back-N (GBN) 은 파이프라이닝 방식의 신뢰성 전송 프로토콜
* 한 번에 여러 패킷(최대 N개)을 보낼 수 있고 손실이 나면 그 이후의 모든 패킷을 재전송함.

&ensp;주요 변수<br/>
* `base` : 아직 ACK를 받지 않은 가장 오래된 패킷의 번호
* `nextseqnum` : 다음에 보낼 패킷 번호
* `N` : 윈도우 크기 (동시에 보낼 수 있는 최대 패킷 수)

&ensp;주요 동작<br/>
1. 데이터 전송 요청 (rdt_send(data))
* 아직 윈도우가 꽉 차지 않았다면 (`nextseqnum < base + N`)
    - 새 패킷 생성 후 전송
    - 첫 번째 패킷이면 타이머 시작
    - `nextseqnum++`
* 윈도우가 꽉 찼으면 → `refuse_data()` (보내지 않음)
2. ACK 수신 (rdt_rcv(rcvpkt))
* 손상되지 않았으면 (`notcorrupt(rcvpkt)`)
    - `base = getacknum(rcvpkt) + 1`
    - 모두 패킷 ACK 받았으면 타이머 멈춤 아니면 다시 타이머 시작
3. 타임아웃 발생 (timeout)
* `base` 부터 아직 ACK 안 받은 패킷까지 전부 재전송
* 다시 타이머 시작

&ensp;Receiver FSM<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-85.png" width="500"></p>

&ensp;핵심 개념<br/>
* GBN 수신자는 순서대로 (in-order) 온 패킷만 수용하고 순서가 어긋난(out-of-order) 패킷은 버린다.

&ensp;주요 변수<br/>
* `expectedseqnum` : 다음에 올 것으로 기대되는 패킷 번호

&ensp;주요 동작<br/>
1. 올바른 패킷 수신(정상 수신 + 올바른 seqnum)
* 데이터 추출(extract) 후 애플리케이션에 전달
* `expectedseqnum++`
* 새로운 ACK 생성 후 전송
2. 패킷 손상 or 순서 어긋남
* 그냥 버림(discard)
* 대신 마지막으로 정상 수신된 패킷 번호에 대해 중복 ACK 재전송

&ensp;특징<br/>
* 버퍼링 없음(out-of-order 패킷 저장 안 함)
* 항상 가장 최신 정상 패킷에 대해 ACK만 전송
* 손실이나 순서 오류가 나면 송신자는 Go-Back-N 재전송

TCP
-----

&ensp;TCP Sender (Simplified FSM)<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-86.png" width="500"></p>

&ensp;상태 설명<br/>
1. 데이터 수신 (application → TCP)
* 세그먼트 생성, `NextSeqNum` 증가
* 타이머가 꺼져 있으면 시작
2. 타임아웃 발생
* 아직 ACK 안 받은 가장 작은 seq# 세그먼트 재전송
3. ACK 수신
* `SendBase` 업데이트 (마지막 누적 ACK 바이트)
* 모든 데이터가 ACK되면 타이머 중지 아니면 계속 유지

&ensp;TCP는 GBN과 유사하게 동작하지만 패킷 단위가 아니라 바이트 단위(window 단위)로 관리한다.<br/>

&ensp;TCP 3-Way Handshake<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-87.png" width="500"></p>

&ensp;개념<br/>
&ensp;TCP는 신뢰성 있는 연결을 만들기 위해 3단계 핸드셰이크(3-way handshake)를 수행한다.<br/>

&ensp;과정<br/>

| 단계 | 방향         | 내용                         | 설명         |
| -- | ---------- | -------------------------- | ---------- |
| ①  | 클라이언트 → 서버 | **SYN(seq=x)**             | 연결 요청      |
| ②  | 서버 → 클라이언트 | **SYNACK(seq=y, ACK=x+1)** | 요청 수락 및 확인 |
| ③  | 클라이언트 → 서버 | **ACK(ACK=y+1)**           | 최종 확인      |

&ensp;이후 ESTABLISHED 상태에서 데이터 전송 시작 가능<br/>

&ensp;Closing a TCP Connection<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-88.png" width="500"></p>

&ensp;TCP는 종료도 신중하게 처리한다. 4단계 종료(4-way handshake) 방식으로 양쪽이 각각 닫음<br/>

&ensp;과정<br/>

| 단계 | 클라이언트 상태           | 서버 상태      | 동작                   |
| -- | ------------------ | ---------- | -------------------- |
| 1  | ESTAB → FIN_WAIT_1 | ESTAB      | 클라이언트가 종료 요청 (FIN=1) |
| 2  | FIN_WAIT_2         | CLOSE_WAIT | 서버가 ACK 보내고 잠시 대기    |
| 3  | TIMED_WAIT         | LAST_ACK   | 서버도 FIN 보냄           |
| 4  | CLOSED             | CLOSED     | 클라이언트가 마지막 ACK 보냄    |

&ensp;TIMED_WAIT 이유<br/>
* 혹시 마지막 ACK이 손실될 경우 재전송 대비
* 2x 최대 세그먼트 수명(MSL) 동안 대기 후 완전 종료

&ensp;TCP Throughput<br/>
&ensp;개념<br/>
&ensp;TCP의 평균 처리율(throughput)은 혼잡 제어에서의 윈도우 크기(W) 와 RTT에 의해 결정된다.<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-89.png" width="500"></p>

&ensp;계산식<br/>
&ensp;평균 윈도우 크기 ≈ 3/4W<br/>
&ensp;$Avg TCP Throughput = \frac{3}{4}\cdot \frac{W}{RTT}$ <br/>
* W: 윈도우 크기
* RTT: 왕복 지연 시간

&ensp;예시<br/>
&ensp;TCP가 혼잡 회피 중일 때 cwnd가 선형 증가하다 손실 시 절반으로 감소하는 패턴이 삼각형 파형처럼 반복됨(그래프의 톱니 형태)<br/>

&ensp;TCP over Long, Fat Pipes<br/>
&ensp;문제 상황<br/>
* 대용량("fat"), 장거리("long") 링크에서는 RTT가 길고 대역폭이 매우 커서 손실 하나로도 큰 손실이 발생함

&ensp;예시<br/>
* 1500바이트 세그먼트, RTT = 100ms, 목표 10Gbps
* 필요한 in-flight 세그먼트 수 W = 83,333개
* 즉, 창(window)이 매우 커야 함

&ensp;수식<br/>
&ensp;$TCP Throughput = \frac{1.22 \times MSS}{RTT \times \sqrt{L}}$ <br/>

* MSS: 최대 세그먼트 크기
* L: 세그먼트 손실 확률

&ensp;의미<br/>
* Throughput은 손실 확률의 제곱근에 반비례
* 10Gbps 유지하려면 $L = 2 \times 10^{-10}$ → 매우 낮은 손실률 필요
* 이런 환경에서는 일반 TCP보다 더 효율적인 고속 TCP 변형(CUBIC, BBR) 등이 필요함
