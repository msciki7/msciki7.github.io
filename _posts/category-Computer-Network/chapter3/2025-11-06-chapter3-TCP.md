---
title: "chapter3. Transport Layer(소단원 5~6)"
excerpt: ""

wirter: sohee Kim
categories:
  - Computer Network
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-11-06
last_modified_at: 2025-11-06
---

Connection-oriented transport: TCP
====

&ensp;TCP Overview<br/>

| 개념                                 | 설명                                                   |
| ---------------------------------- | ---------------------------------------------------- |
| **point-to-point**                 | 한 번의 TCP 연결은 정확히 **1:1 (sender ↔ receiver)** 통신만 지원  |
| **reliable, in-order byte stream** | 데이터 손실 없이, 순서대로 전달 (메시지 경계가 없음 — 스트림 형태)             |
| **full duplex**                    | 양방향 전송 (A↔B 동시에 가능)                                  |
| **cumulative ACKs**                | 여러 세그먼트를 한 번에 ACK (누적 확인 응답)                         |
| **pipelining**                     | 여러 패킷을 동시에 전송 가능 (Go-Back-N/Selective Repeat 개념과 유사) |
| **connection-oriented**            | 연결 수립 (3-way handshake) 후 전송 시작                      |
| **flow controlled**                | 수신자의 처리 속도를 고려해서 전송량 조절                              |

&ensp;TCP는 신뢰적이고 순서가 보장된 양방향 바이트 스트림 전송을 제공하는 프로토콜이다.<br/>

&ensp;TCP Segment Structure<br/>
&ensp;TCP는 IP 위에서 동작하며, 데이터 단위를 세그먼트(segment) 라고 부른다.<br/>

&ensp;주요 필드 정리<br/>

| 필드                                     | 설명                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------ |
| **Source Port # / Destination Port #** | 송신자와 수신자 애플리케이션 식별                                                                   |
| **Sequence Number**                    | 세그먼트 내 **첫 번째 바이트의 번호**                                                              |
| **Acknowledgement Number**             | 상대방으로부터 다음에 기대하는 바이트 번호                                                              |
| **Header Length**                      | TCP 헤더의 길이                                                                           |
| **Flags (C, E, U, A, P, R, S, F)**     | 제어 비트들<br>**SYN**: 연결 요청<br>**FIN**: 연결 종료<br>**ACK**: 응답 확인<br>**RST**: 비정상 연결 종료 등 |
| **Receive Window (rwnd)**              | 수신자가 한 번에 받을 수 있는 **버퍼 크기** (→ 흐름 제어)                                                |
| **Checksum**                           | 오류 검출용                                                                               |
| **Options**                            | MSS(Max Segment Size), Timestamp 등 부가 정보                                             |
| **Data**                               | 실제 전송되는 애플리케이션 데이터                                                                   |

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-38.png" width="500"></p>

&ensp;TCP는 세그먼트 단위로 데이터를 주고받지만 각 세그먼트의 sequence number는 바이트 단위로 번호를 매긴다.<br/>

&ensp;TCP Sequence Numbers & ACKs<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-39.png" width="500"></p>

&ensp;Sequence Number<br/>
* 세그먼트 내 첫 번째 데이터 바이트의 번호
* 예를 들어 1000~1999바이트를 보냈다면 다음 세그먼트의 시퀀스 번호는 2000이 됨

&ensp;ACK Number<br/>
* 다음에 기대하는 바이트 번호
    - 이전까지의 모든 데이터를 받았으니 다음 번호부터 보내라는 의미
* TCP는 누적 ACK(cumulative ACK) 방식 사용 → 연속된 데이터가 모두 수신되면 한 번에 ACK 보냄

&ensp;Out-of-order 처리<br/>
* TCP 표준에서는 순서가 뒤바뀐 세그먼트 처리 방식을 명시하지 않음 → OS나 구현 방식에 따라 다름 (ex. 버퍼링 가능 or 무시)

&ensp;Simple Tenlnet Scenario<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-40.png" width="500"></p>

&ensp;흐름 설명<br/>

| 단계 | 송신자 (Host A)             | 수신자 (Host B)                        |
| -- | ------------------------ | ----------------------------------- |
| ①  | 사용자 입력 ‘C’               |                                     |
| ②  | Seq=42, ACK=79, data=‘C’ | ‘C’ 수신 후 ACK=43 응답 및 ‘C’ 반사(echo)   |
| ③  | Seq=79, ACK=43, data=‘C’ | Host A가 ‘C’를 받았다는 것을 다시 ACK=80으로 회신 |

&ensp;결과적으로 TCP는 양방향 통신이기 때문에 각 방향마다 별도의 시퀀스/ACK 번호 흐름이 유지된다.<br/>

&ensp;정리 요약<br/>

| 개념            | 설명                                                   |
| ------------- | ---------------------------------------------------- |
| **TCP의 목적**   | 신뢰적, 순서보장, 양방향 전송                                    |
| **핵심 기능**     | 오류검출, 흐름제어, 혼잡제어, 연결관리                               |
| **데이터 단위**    | 세그먼트 (segment)                                       |
| **시퀀스 번호 단위** | 바이트 단위 (byte-based numbering)                        |
| **ACK 방식**    | 누적 ACK (Cumulative)                                  |
| **연결 특성**     | 1:1 연결, 양방향(Full Duplex), 연결지향형(Connection-Oriented) |

# TCP RTT와 Timeout 개념

&ensp;RTT(Round Trip Time)<br/>
* 송신자가 세그먼트를 보낸 뒤 ACK(응답)을 받기까지 걸리는 왕복 시간
* 네트워크 상태(혼잡, 거리, 라우팅 등)에 따라 계속 변함

&ensp;Timeout이란?<br/>
* 송신자가 보낸 세그먼트의 ACK이 일정 시간 내에 안 오면 재전송하기 위한 기준 시간
* 네트워크 상태(혼잡, 거리, 라우팅 등)에 따라 계속 변함

&ensp;Timeout이란?
* 송신자가 보낸 세그먼트의 AKC이 일정 시간 내에 안 오면 재전송하기 위한 기준 시간

&ensp;그럼 Timeout 값을 어떻게 설정해야 할까?<br/>

| 경우               | 문제점                                                |
| ---------------- | -------------------------------------------------- |
| ⏱️ **너무 짧게 설정**  | 실제 세그먼트가 도착하기 전에 재전송 시작 → **불필요한 재전송 증가 (중복 트래픽)** |
| 🕰️ **너무 길게 설정** | 손실된 세그먼트에 대한 **대응이 너무 늦어짐** → 성능 저하                |

&ensp;따라서 TCP는 RTT보다 약간 긴 시간으로 timeout을 잡되 RTT가 변동하는 것을 고려해서 동적으로 조정해야 한다.<br/>

&ensp;RTT 측정 방법<br/>

&ensp;SampleRTT<br/>
* 실제 한 세그먼트 전송 → ACK 수신까지의 시간
* 재전송된 세그먼트는 무시(왜냐면 어떤 세그먼트의 ACK인지 헥살릴 수 있으니까)

&ensp;Estimated RTT<br/>
* RTT는 매번 다르기 때문에 최근 측정값 여러 개를 평균 내어 부드럽게 추정

&ensp;Estimated RTT 계산식<br/>
&ensp;EstimatedRTT = (1 - α) × EstimatedRTT + α × SampleRTT<br/>

* α(알파) : 최근 측정값에 얼마나 가중치를 둘지 결정
    - 일반적으로 α = 0.125 (1/8)
* 과거 값의 영향은 지수적으로 감소(Exponential Weighted Moving Average, EWMA)

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-41.png" width="500"></p>

* 파란색: 실제 SampleRTT(불안정, 들쭉날쭉)
* 분홍색: EstimateRTT(평균된 안정적 추세)

&ensp;TCP는 RTT를 실시간으로 학습하고 네트워크 상태에 따라 timeout을 조정하는 적응형 프로토콜이다.<br/>

&ensp;Timeout Interval 계산<br/>
&ensp;TimeoutInterval = EstimatedRTT + 4 × DevRTT<br/>

&ensp;구성 요소 설명<br/>
* EstimatedRTT : RTT의 평균값
* DevRTT (Deviation RTT) : RTT가 얼마나 변동되는지를 나타내는 표준편차
    - RTT의 "흔들림"이 크면 timeout에 더 여유를 둠

&ensp;DevRTT 계산식<br/>
&ensp;DevRTT = (1 - β) × DevRTT + β × |SampleRTT - EstimatedRTT|<br/>
* β(베타) : 보통 0.25 (1/4)
* SampleRTT가 예측보다 너무 높거나 낮을수록 DevRTT가 커짐 → 즉, RTT의 불안정성이 커진다는 뜻

&ensp;TimeoutInterval 의미<br/>

| 상황                   | 결과                                |
| -------------------- | --------------------------------- |
| RTT가 안정적 (DevRTT 작음) | TimeoutInterval이 작아짐 → 빠른 재전송 가능  |
| RTT가 불안정 (DevRTT 큼)  | TimeoutInterval이 커짐 → 불필요한 재전송 방지 |

&ensp;TCP는 RTT의 평균(EstimatedRTT)과 변동폭(DevRTT)을 함께 고려해 유연한 TimeoutInterval 을 설정함으로써 빠른 복구와 불필요한 방지를 동시에 달성한다.<br/>

# TCP Sender 동작

&ensp;TCP 송신자(sender)는 3가지 이벤트(event)에 반응한다.<br/>

| 이벤트                              | 동작                                                                                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 📩 **데이터 수신 (from application)** | - 애플리케이션이 보낸 데이터를 TCP 세그먼트로 만듦<br>- 세그먼트에 **시퀀스 번호(seq #)** 부여 (바이트 단위)<br>- **타이머 시작** (만약 아직 안 돌고 있으면)<br> → 타이머는 “가장 오래된 unACKed(미확인) 세그먼트” 기준 |
| ⏰ **타임아웃 발생 (timeout)**          | - 해당 세그먼트를 **재전송(retransmit)**<br>- 타이머 **재시작** (TimeoutInterval 기준으로)                                                                            |
| ✅ **ACK 수신 (acknowledgement)**   | - 이전에 보내서 아직 확인 안 된 세그먼트 중, ACK가 도착한 부분은 “확인됨”으로 표시<br>- 아직 남아있는 unACKed 세그먼트가 있으면 타이머 유지                                                         |

&ensp;TCP는 타이머와 ACK를 함께 이용해 손실 감지 + 재전송 관리를 자동으로 수행한다.<br/>

# TCP Receiver 동작

&ensp;수신자는 세그먼트 도착 상태에 따라 ACK 생성 방법이 달라진다.<br/>

| 이벤트                                           | 수신자의 동작                                                                                                 |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| ✅ **순서대로(in-order)** 세그먼트 도착, 모든 데이터는 이미 ACK됨 | - **지연 ACK (Delayed ACK)**: 최대 500ms 동안 다음 세그먼트를 기다림<br>- 다음 세그먼트가 오면 한 번에 ACK<br>- 안 오면 500ms 뒤 ACK 전송 |
| ✅ **순서대로(in-order)** 세그먼트 도착, 하나의 ACK가 대기 중   | - **즉시 ACK 전송 (immediate cumulative ACK)**<br>- 이전 세그먼트 + 이번 세그먼트를 한 번에 ACK                             |
| ⚠️ **순서가 어긋난(out-of-order)** 세그먼트 도착 (Gap 발생) | - **즉시 duplicate ACK 전송**<br>- “다음에 기대하는 시퀀스 번호”를 명시 (즉, 아직 빠진 세그먼트를 요청하는 의미)                           |

&ensp;수신자는 누락된 부분을 즉시 알리기 위해 duplicate ACK를 보낸다.<br/>

# TCP 재전송 시나리오 (Retransmission Scenarios)

&ensp;(1) Lost ACK Scenario<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-42.png" width="500"></p>

* ACK 손실: 송신자는 ACK을 못 받았다고 생각해 타임아웃 → 같은 데이터 재전송
* 하지만 수신자는 이미 데이터 받았음 → 중복 ACK 발생 가능

&ensp;결국 중복 전송이 일어나지만 TCP는 데이터 중복 수신 시 자동으로 제거함<br/>

&ensp;(2) Premature Timeout (조기 타임아웃)<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-43.png" width="500"></p>

* 실제 데이터는 잘 도착했지만 ACK이 조금 늦게 옴 → 송신자는 timeout이 너무 짧아서 "손실로 오판"하고 재전송함
* 수신자는 중복된 데이터지만 또 ACK 보냄 → 나중에 누적 ACK(cumulative ACK)가 중복 ACK 문제를 해결함

&ensp;(3) Cumulative ACK<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-44.png" width="500"></p>

* 여러 세그먼트를 받았을 때 중간 ACK이 손실돼도 누적 ACK(cumulative ACK)이 그 이전 모든 데이터를 포함함 → 손실된 ACK은 자연스럽게 복구됨

# TCP Fast Retransmit (빠른 재전송)

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-45.png" width="500"></p>

&ensp;동작 원리<br/>
* 송신자가 같은 데이터에 대한 duplicate ACK 3개를 연속으로 받으면 → "이건 타임아웃 기다릴 필요 없이 세그먼트가 진짜 손실된 것 같다"고 판단
* 즉시 가장 작은 시퀀스 번호의 세그먼트를 재전송

&ensp;예시<br/>
* 송신자가 Seq=100 세그먼트를 보냄(중간에 손실)
* 이후 세그먼트(Seq=120, 140...)들은 잘 도착
* 수신자는 빠진 부분(Seq=100)을 계속 요구하며 ACK=100을 3번 이상 연속 보냄 → "Triple Duplicate ACKs"

&ensp;송신자는 timeout 없이 즉시 Seq=100 재전송.<br/>

| 개념                  | 설명                                             |
| ------------------- | ---------------------------------------------- |
| **Timer 기반 재전송**    | ACK이 안 오면 timeout → 세그먼트 재전송                   |
| **ACK 기반 업데이트**     | ACK 도착 시, 수신된 데이터 범위 업데이트                      |
| **Duplicate ACK**   | 순서 어긋남 감지 → 빠진 세그먼트 재요청                        |
| **Cumulative ACK**  | 누락된 ACK 자동 복구                                  |
| **Fast Retransmit** | 3회 duplicate ACK 감지 시 즉시 재전송 (timeout 기다리지 않음) |


TCP flow control
=====

&ensp;문제 상황: 송신 속도가 너무 빠를 때<br/>
&ensp;만약 네트워크 계층이 데이터를 너무 빨리 전달하고 애플리케이션 계층이 그 데이터를 버퍼에서 천천히 꺼내면 어떻게 될까?<br/>

&ensp;TCP 수신 버피(receiver buffer)가 꽉 차게 된다.<br/>
&ensp;TCP의 데이터 흐름 구조는 다음과 같다.<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-46.png" width="500"></p>

```scss
Application Process (상위 계층)
      ↑
TCP Socket Receiver Buffer  ← (여기서 대기)
      ↑
TCP Layer (세그먼트 처리)
      ↑
IP Layer (데이터그램 수신)
      ↑
Sender (송신자)
```

&ensp;즉 네트워크(IP)가 계속 데이터를 넣고 있는데 응용 프로그램이 천천히 읽으면 → 버퍼 overflow 위험 발생<br/>

&ensp;Flow Control(흐름 제어)의 개념<br/>
&ensp;Flow Control = "수신자가 송신자에게 속도를 조절하라고 신호를 보내는 메커니즘"<br/>

&ensp;Receiver controls sender so sender won’t overflow receiver’s buffer by transmitting too much, too fast.<br/>

&ensp;수신자가 버퍼 상황을 감시하면서 이만큼만 보내라고 송신자에게 알려주는 방식이다.<br/>

# rwnd (Receive Window) — TCP의 핵심 필드

&ensp;TCP는 헤더(header)에 rwnd(receive window)라는 필드를 둔다. 이 값이 바로 수신자가 현재 수용 가능한 여유 공간(바이트 단위)이다.<br/>
&ensp;구조<br/>
```bash
TCP Header
 ├── source port
 ├── dest port
 ├── seq number
 ├── ack number
 ├── rwnd  ← 여기가 flow control 정보
 └── ...
```

&ensp;수신자는 내 버퍼에 이만큼 공간이 있다라고 rwnd 값을 송신자에게 계속 알려준다.<br/>

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-47.png" width="500"></p>


&ensp;RcvBuffer와 rwnd의 관계<br/>

| 용어                        | 설명                                 |
| ------------------------- | ---------------------------------- |
| **RcvBuffer**             | 수신 버퍼의 총 크기 (예: 4096 bytes)        |
| **rwnd (receive window)** | 현재 남은 **빈 공간 (free buffer space)** |
| **buffered data**         | 이미 TCP가 받아놓은 데이터 (아직 앱이 안 읽은 부분)   |

&ensp;rwnd = RcvBuffer - (buffered data)<br/>

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-48.png" width="500"></p>

&ensp;송신자(sender)의 행동<br/>

&ensp;송신자는 현재 미확인(unACKed) 데이터의 총량이 수신자가 보낸 rwnd 이하가 되도록 전송량을 제한한다.<br/>
&ensp;`송신 가능한 데이터량 ≤ 수신자가 보낸 rwnd` <br/>
&ensp;이렇게 하면 수신자의 버퍼는 절대 overflow 되지 않는다.<br/>

&ensp;동작 흐름 정리<br/>
&ensp;1. 수신자(receiver)<br/>
* TCP 세그먼트를 받음
* 버퍼에 저장
* 현재 남은 버퍼 공간을 계산 → rwnd 필드에 기록
* ACK 패킷에 이 값을 포함해 송신자에게 전송

&ensp;송신자(sendeer)<br/>
* 수신자의 rwnd 값을 읽음
* 그 값보다 많은 데이터를 보내지 않음
* ACK가 도착할 때마다 다시 최신 rwnd 확인

&ensp;예시로 이해<br/>

| 단계        | 수신 버퍼 상태      | rwnd 값     | 송신자의 행동            |
| --------- | ------------- | ---------- | ------------------ |
| 초기        | 비어 있음         | 4096 bytes | 최대 4096 bytes까지 전송 |
| 절반 찼을 때   | 2000 bytes 사용 | 2096 bytes | 속도 절반으로 제한         |
| 거의 가득 참   | 3900 bytes 사용 | 196 bytes  | 아주 조금씩만 전송         |
| 버퍼 가득 참   | 4096 bytes 사용 | 0 bytes    | 전송 중지 (pause)      |
| 앱이 데이터 읽음 | 1024 bytes 해제 | rwnd=1024  | 전송 재개             |

&ensp;결과<br/>
* 송신자가 절대 수신자의 버퍼를 넘치게 하지 않음
* TCP 연결은 안정적으로 유지됨
* 데이터 손실 없이 양방향 흐름 가능

# TCP Connection Management 개요

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-49.png" width="500"></p>

&ensp;TCP는 데이터를 주고받기 전에 송신자(sender)와 수신자(receiver)가 먼저 서로의 의사를 확인해야 한다. 이 과정을 핸드셰이크(handshake)라고 부른다.<br/>
&ensp;목적<br/>
* 서로 연결을 맺을 준비가 되어 있는지 확인
* 통신에 필요한 초기 정보(예: 시퀀스 번호) 교환
* 연결 상태를 동기화(synchronize)시켜 안정적인 통신을 보장

&ensp;연결 전 TCP 소켓 상태<br/>
* 클라이언트(Client): `Socket clientSocket = newSocket("hostname", "port number");` → 서버에 연결을 요청하는 역할
* 서버(Server): `Socket connectionSocket = welcomeSocket.accept();` → 클라이언트의 연결 요청을 수락하는 역할

&ensp;서버는 기본적으로 listen 상태로 대기하다가 클라이언트의 요청을 받으면 새로운 소켓을 만들어 연결을 수립한다.<br/>

&ensp;2-way Handshake (문제 있는 초기 방식)
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-50.png" width="500"></p>

&ensp;1. 클라이언트 → 서버: "연결하자" (req_conn(x))<br/>
&ensp;2. 서버 → 클라이언트: "좋아" (acc_conn(x))<br/>

&ensp;이렇게만 하면 일단 두 노드 모두 ESTABLISHED(연결됨)상태로 보이기 하지만 문제가 생긴다.<br/>

&ensp;2-way Handshake의 문제점<br/>
&emsp;TCP는 네트워크 환경이 불안정할 때<br/>
* 패킷 지연(variable delay)
* 패킷 재전송(retransmission)
* 패킷 순서 바뀜(message reordering)

&ensp;같은 현상이 자주 일어나기 때문에 단순히 요청-응답(2단계)만으로는 신뢰성이 부족하다.<br/>

&ensp;문제 시나리오 1 — 정상 케이스<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-51.png" width="500"></p>

* 클라이언트: `req_conn(x)` 전송
* 서버: `acc_conn(x)` 수학
* 이후 데이터 주고받음 → 정상적인 연결 성립

&ensp;문제 시나리오 2 — "Half-Open Connection"<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-52.png" width="500"></p>

1. 클라이언트가 `req_conn(x)` 보냄
2. 서버가 응답(`acc_conn(x)`) 보냄
3. 그런데 네트워크 오류로 인해 클라이언트는 연결이 끊김(terminate)
4. 서버는 여전히 연결됐다고 착각 → ESTAB 상태 유지

&ensp;서버는 존재하지 않는 클라이언트와 연결된 상태로 남음 → Half-Open Connection<br/>
&ensp;서버는 연결이 유지된다고 생각하지만 클라이언트는 이미 종료됨<br/>

&ensp;문제 시나리오 3 — "중복 데이터 전송"<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-53.png" width="500"></p>

1. 이전 연결 요청(`req_conn(x)`)이 네트워크에 남아있음
2. 새로운 연결 시도가 이루어짐
3. 늦게 도착한 예전 req_conn(x) 때문에 서버가 옛날 연결을 다시 활성화함

&ensp;서버는 이미 끊긴 연결에 대해 중복 데이터(data(x+1))를 수락 → 데이터 중복 문제 발생<br/>

&ensp;TCP 3-Way Handshake (연결 수립 과정)<br/>
&ensp;TCP는 신뢰성 있는 연결을 위해 서로의 상태와 시퀀스 번호를 동기화(synchronize) 해야 한다. 그래서 데이터를 주고받기 전에 3단계 절차를 통해 연결을 설정한다.<br/>

&ensp;전체 과정 요약<br/>

| 단계 | 방향         | 플래그       | 의미                                       | 상태 변화               |
| -- | ---------- | --------- | ---------------------------------------- | ------------------- |
| ①  | 클라이언트 → 서버 | SYN       | “나 연결하고 싶어. 내 초기 시퀀스는 x야.”               | `LISTEN → SYN_SENT` |
| ②  | 서버 → 클라이언트 | SYN + ACK | “좋아. 나도 연결할게. 내 시퀀스는 y야. 네 SYN(x)은 받았어.” | `SYN_RCVD`          |
| ③  | 클라이언트 → 서버 | ACK       | “좋아. 네 SYN(y)도 받았어.”                     | `ESTABLISHED`       |

&ensp;이후 양쪽 모두 `ESTABLISHED` 상태로 전환되어 데이터 전송 시작<br/>

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-54.png" width="500"></p>

&ensp;SYN 단계<br/>
* Client
    - 초기 시퀀스 번호 x 선택
    - `SYNbit=1, Seq=x` 패킷 전송
    - 상태: `SYN_SENT`
* Server
    - 패킷 수신 후 `SYN_RCVD` 상태로 전환

&ensp;SYN + ACK 단계<br/>
* Server
    - 자신의 시퀀스 번호 y 선택
    - `SYNbit=1, Seq=y, ACKbit=1, ACKnum=x+1` 전송
    - 너의 요청은 받았고 나도 준비됐어
* Client
    - 이 메시지 받으면 "서버가 살아 있네!" 확인
    - `ESTABLISHED` 상태로 진입

&ensp;ACK 단계<br/>
* Client
    - `ACKbit=1, ACKnum=y+1` 전송
    - 이때 이 세 번째 세그먼트는 데이터를 포함할 수도 있음
* Server
    - ACK 수신 → `ESTABLISHED` 상태로 전환

&ensp;TCP 연결 종료 (Closing a TCP Connection)<br/>
&ensp;연결을 끊을 때는 양쪽이 각각 자신의 방향의 통신을 닫는다. 한쪽이 보내는 걸 끝냈다는 신호를 보내고 다른 쪽이 그것을 확인한 자신의 쪽도 닫는다.<br/>

&ensp;절차 요약 (4-way handshake)<br/>

| 단계 | 방향         | 플래그 | 의미                | 상태                 |
| -- | ---------- | --- | ----------------- | ------------------ |
| ①  | 클라이언트 → 서버 | FIN | “더 이상 보낼 데이터 없어.” | FIN_WAIT_1         |
| ②  | 서버 → 클라이언트 | ACK | “알겠어. 네 FIN 받았어.” | CLOSE_WAIT         |
| ③  | 서버 → 클라이언트 | FIN | “나도 이제 끝낼게.”      | LAST_ACK           |
| ④  | 클라이언트 → 서버 | ACK | “확인했어. 완전히 닫자.”   | TIME_WAIT → CLOSED |

&ensp;세부 설명<br/>
1. FIN
* 한쪽이 `FIN` 플래그를 보냄 (보내는 데이터가 더 이상 없음)
2. ACK
* 상대방은 `ACK` 으로 알겠어 응답
* 하지만 여전히 받는 쪽 방향의 통신은 열려 있음
3. 상대방도 FIN 전송
* 양쪽 모두 전송 종료 신호 보냄
4. 마지막 ACK
* 최종적으로 ACK 교환 후 연결 완전히 종료

| 구분     | Handshake 단계                               | 특징                    |
| ------ | ------------------------------------------ | --------------------- |
| 연결 수립  | **3-way handshake**                        | SYN → SYN+ACK → ACK   |
| 연결 종료  | **4-way handshake**                        | FIN → ACK → FIN → ACK |
| 동기화 정보 | 시퀀스 번호(seq), ACK 번호(ack), 플래그(SYN/ACK/FIN) |                       |
| 역할     | 신뢰성 보장, 중복 연결 방지, 양방향 종료 처리                |                       |

Principles of congestion control
=====

&ensp;혼잡: 너무 많은 송신자들이 너무 빠른 속도로 데이터를 보내서 네트워크(특히 라우터)가 처리할 수 없는 상태<br/>

&ensp;혼잡의 결과<br/>
1. 지연(Delay)
* 라우터 큐(buffer)에 패킷이 너무 많이 쌓임 → 대기시간 길어짐
* 네트워크 교통 체증처럼 데이터가 막힘
2. 패킷 손실(Packet Loss)
* 라우터의 버퍼가 꽉 차면 새로운 패킷이 버려짐(drop)
* 전송 계층(TCP)은 재전송을 수행하게 됨 → 오히려 혼잡 더 악화 가능

&ensp;Flow Control vs Congestion Control 차이<br/>

| 구분                     | 대상            | 설명                                                |
| ---------------------- | ------------- | ------------------------------------------------- |
| **Flow Control**       | 송신자 ↔ 수신자 간   | 수신자가 너무 느릴 때 송신자가 너무 빨리 보내지 않도록 제어 (1:1 문제)       |
| **Congestion Control** | 송신자 ↔ 네트워크 전체 | 여러 송신자들이 동시에 너무 많이 보낼 때 네트워크가 막히지 않도록 제어 (N:1 문제) |

&ensp;비유<br/>
* Flow Control: 개 한 마리에게 너무 많은 물을 뿌림
* Congestion Control: 고속도로에 차가 너무 많아 막힘

# Scenario 1: Simplest Case

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-55.png" width="500"></p>

&ensp;설정<br/>
* 라우터 1개, 무한 버퍼(infinite buffer)
* 입출력 링크 용량: R
* 2개의 호스트(Host A, Host B) → 두 흐름이 동시에 전송
* 재전송 없음 (즉 손실은 고려하지 않음)

&ensp;개념 정리<br/>
* 입력 속도: `λ_in` (호스트가 보내는 속도)
* 출력 속도: `λ_out` (라우터가 내보내는 속도)

&ensp;라우터의 출력 링크 용량은 R 두 호스트가 나눠 쓰르모 각 호스트의 최대 처리량은 R/2<br/>

&ensp;그래프 해석<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-56.png" width="500"></p>

&ensp;왼쪽 그래프 — 처리량(throughput)<br/>
* `λ_in` < `R/2`: 입력 속도와 출력 속도가 같음
* `λ_in` → `R/2`: 처리량이 R/2로 수렴
* 최대 per-connection throughput = R/2

&ensp;오른쪽 그래프 — 지연(delay)<br/>
* `λ_in`이 R/2에 가까워질수록 라우터 큐가 길어짐
* → 지연이 급격히 증가(폭발적으로 큼)
* 현실에서도 RTT가 커지고 응답 느려짐

&ensp;결론: 입력 속도가 링크 용량에 가까워지면 → 지연 폭발(delay explosion) 즉 네트워크가 막히기 시작함.<br/>

# Scenario 2: Finite Buffers (현실적 상황)

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-57.png" width="500"></p>

&ensp;설정<br/>
* 이번엔 라우터 버퍼 크기가 제한됨(finite buffer)
* 패킷 손실 발생 가능 → 송신자는 재전송 수행

&ensp;중요한 포인터<br/>
* 애플리케이션이 보내는 속도: `λ_in`
* 실제 전송 계층(TCP)에서 보내는 속도: `λ'_in` (원본 + 재전송 포함)

&ensp;`λ'_in ≥ λ_in` (재전송 때문에 더 많아짐)<br/>

&ensp;결과<br/>
* 네트워크 부하 증가
* 혼잡 심화
* 불필요한 중복 전송으로 효율 저하

&ensp;Idealization: Perfect Knowledge (이상적 가정)<br/>
&ensp;가정: 송신자가 라우터의 버퍼 상태를 완벽히 알고 있음 → "버퍼에 여유 공간이 있을 때만 보냄"<br/>

&ensp;결과<br/>
* 손실 없음
* 재전송 불필요
* 전체 처리율은 이상적으로 R/2에 도달

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-58.png" width="500"></p>

* 입력 속도(`λ_in`)와 출력 속도(`λ_out`)가 1:1로 증가
* `λ_in = R/2`일 때 최대 처리량

&ensp;Some Perfect Knowledge (현실적 시나리오)<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-59.png" width="500"></p>

&ensp;가정: 송신자가 어느 정도만 네트워크 상태를 앎<br/>
* 라우터 버퍼가 꽉차면 → 패킷 손실 발생
* 송신자는 손실을 "알게 되면"에만 재전송 수행

&ensp;특징<br/>
* 손실 발생 가능
* 라우터 버퍼 overflow → 패킷 drop
* 송신자는 손실된 것만 재전송(known to be lost)

&ensp;하지만 여전히 네트워크 자원 낭비 발생:<br/>
* 패킷 손실 시 재전송 → 중복 트래픽
* 전체 네트워크 부하 증가

&ensp;Scenario 2 (계속): 비용 발생<br/>
&ensp;핵심 문제: 낭비된 용량(wasted capacity)<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-60.png" width="500"></p>

* 입력 속도 `λ'_in`을 R/2까지 높이면 일부 패킷은 재전송이 필요해짐 → 용량 일부가 낭비됨
* 송신자는 열심히 보내지만 일부는 라우터에서 손실되어 다시 보냄

&ensp;결과적으로<br/>
* 실제 유효 처리량(`λ_ou`) < 송신 속도(`λ'_in`)
* 그래프의 파란 원 부분 = 손실로 인한 재전송 낭비

| 구분                             | 설명                      | 특징                            |
| ------------------------------ | ----------------------- | ----------------------------- |
| **혼잡(Congestion)**             | 네트워크 내에 너무 많은 트래픽       | 지연↑, 손실↑                      |
| **Scenario 1**                 | 무한 버퍼 → 손실 없음, 지연만 증가   | `λ_in → R/2` 시 delay 폭증       |
| **Scenario 2 (finite buffer)** | 버퍼 한정 → 손실 발생 + 재전송     | 비효율 증가                        |
| **Perfect Knowledge**          | 버퍼 상태를 완벽히 앎            | 이상적, 손실 없음                    |
| **Some Knowledge**             | 손실을 알면 재전송              | 실제 TCP에 가까움                   |
| **결론**                         | 재전송 + 손실 → 용량 낭비, 혼잡 심화 | TCP가 Congestion Control 수행 이유 |

&ensp;Scenario 2: Realistic scenario (Un-needed duplicates)<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-61.png" width="500"></p>

&ensp;현실에는 라우터 버퍼가 꽉 차거나 패킷 손실이 발생하면 재전송이 필요하다. 하지만 송신자(sender)가 너무 일찍 timeout 되는 경우 아직 살아있는 패킷도 손실된 줄 알고 다시 보냄<br/>
&ensp;그 결과 같은 패킷이 2번 도착하는 문제(Unneeded duplicates) 발생한다.<br/>

* 빨간 선 `λ_in`: 원래 전송된 데이터 속도
* 빨간 굵은 선 `λ'_in`: 재전송 포함된 실제 전송 속도 → `λ'_in ≥ λ_in`
* 라우터는 `finite buffer` 를 가짐 → 일부 패킷이 버려짐
* 송신자는 `timeout` 발생 → 같은 패킷을 재전송 (둘 다 도착함)

&ensp;하나의 유효 패킷을 위해 2개의 복사본이 네트워크를 타게 됨 → 네트워크 용량 낭비 + 혼잡 악화<br/>

&ensp;그래프 설명<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-62.png" width="500"></p>

* x축: 입력 속도(λ′_in)
* y축: 실제 처리량(λ_out)
* 회색 점선: 이론적 최대치
* 빨간 곡선: 실제 처리량 (낭비 포함)

&ensp;혼잡으로 인해 발생한 재전송 때문에 <br/>
* 처리량은 포화 상태에 도달(R/2 부근) 후 오히려 떨어짐
* "Wasted capacity due to unneeded retransmissions" 발생

&ensp;Costs of Congestion (혼잡의 비용)<br/>
&ensp;혼잡이 초래하는 비용 정리<br/>

| 종류                                          | 설명                                  |
| ------------------------------------------- | ----------------------------------- |
| 1. **재전송 증가**                              | 손실된 패킷을 재전송해야 하므로 송신자는 더 많은 일을 함    |
| 2. **불필요한 재전송 (Unneeded retransmissions)** | 같은 패킷이 두 번 이상 전송되어 링크 용량 낭비         |
| 3. **유효 처리량(Throughput) 감소**               | 링크가 여러 복사본을 전달하느라 진짜 새 데이터 전송 속도 감소 |

&ensp;결국 혼잡은 "더 많은 데이터 전송 시도"가 "더 적은 처리량"으로 이어지는 역설을 초래한다.<br/>

# Scenario 3: Multi-sender (다중 송신자 환경)

<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-63.png" width="500"></p>

&ensp;설정<br/>
* 4개의 송신자 (Host A, B, C, D)
* Multi-hop 경로 (여러 라우터를 거침)
* Timeout + Retransmission 포함

&ensp;중요 포인터<br/>
1. 각 송신자는 자신만의 `λ_in` (원래 속도)과 `λ'_in` (재전송 포함 속도)을 가짐
2. 네트워크 중간 라우터는 finite shared buffer (제한된 용량 공유)
3. 일부 링크에 트래픽 집중 → 특정 라우터 혼잡 발생

&ensp;결과적으로 빨간 흐름(λ'_in) 이 너무 커지면 → 파란 흐름(다른 송신자의 패킷)이 큐에서 모두 버려짐 → blue throughput → 0 (한쪽이 완전히 굶음)<br/>

&ensp;λ_in 과 λ′_in 이 모두 증가하면 무슨 일이 일어날까?<br/>
&ensp;빨간 송신자(λ′_in)가 너무 빨라지면 라우터가 가득 차서 → 파란 송신자의 패킷은 도착 즉시 버려짐(drop) → 일부 송신자는 throughput 0이 됨<br/>
&ensp;혼잡은 불공정한 대역폭 분배와 전체 효율 저하를 유발<br/>

&ensp;Another Cost of Congestion<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-64.png" width="500"></p>

&ensp;또 다른 비용: 낭비된 상류 자원 (upstream cost)<br/>
&ensp;라우터에서 패킷이 버려질 때 그 패킷이 여기 도착하기까지 사용된 모든 이전 링크 용량과 버퍼 공간이 낭비된다.<br/>

* 패킷이 최종 목적지에 도달하기 전에 버려지면 이전 단계의 전송, 저장 모두 헛수고

&ensp;네트워크 효율은 더 떨어지고 혼잡이 누적될수록 낭비가 체계적으로 커진다.<br/>
&ensp;λ′_in 증가 시 throughput(λ_out)은 한 번 정점에 도달한 후 급격히 감소함 → “과도한 재전송 + 낭비된 자원”이 원인<br/>

&ensp;혼잡의 핵심 인사이트 정리<br/>

| 요약                                  | 설명                                            |
| ----------------------------------- | --------------------------------------------- |
| **1. 처리량 한계 존재**                    | Throughput은 절대 링크 용량(capacity)을 초과할 수 없음      |
| **2. 지연 증가**                        | 입력 속도(λ_in)가 용량에 가까워질수록 delay가 폭발적으로 증가       |
| **3. 손실/재전송의 영향**                   | 재전송은 실제 유효 처리량을 감소시킴                          |
| **4. 불필요한 중복(Unneeded duplicates)** | 동일 패킷이 여러 번 전송되어 낭비된 대역폭 발생                   |
| **5. 상류 낭비(Upstream waste)**        | 아래 단계에서 패킷이 drop되면, 그 위 단계에서 사용한 용량·버퍼가 모두 헛됨 |

# 혼잡 제어(Congestion Control)의 두 가지 접근 방식

&ensp;End-to-End Congestion Control (종단 간 혼잡 제어)<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-65.png" width="500"></p>

&ensp;개념<br/>
* **네트워크 내부(라우터)**에서 피드백을 직접 받지 않는다.
* 즉, 라우터가 혼잡하다는 걸 알려주지 않는다.
* 대신 **송신자(Sender)**가 스스로 네트워크 상황을 추론해야 한다.

&ensp;어떻게 혼잡을 "추론(inferred)"하나?<br/>
* 패킷 손실(loss) → 라우터가 버퍼 오버플로우로 데이터를 버렸다고 판단
* 지연(delay) 증가 → 큐잉(queueing)이 많아져 혼잡이 발생했다고 판단

&ensp;송신자는 ACK(응답)가 늦게 오거나 안 오면 → 네트워크가 막혀 있다고 추측한다.<br/>

| 특징       | 설명                  |
| -------- | ------------------- |
| 네트워크 피드백 | ❌ 없음                |
| 혼잡 판단 기준 | 손실(loss), 지연(delay) |
| 대표 프로토콜  | TCP                 |
| 장점       | 라우터 수정 없이 동작 가능     |
| 단점       | 반응이 느림, 부정확할 수 있음   |

&ensp;Network-Assisted Congestion Control (네트워크 지원 혼잡 제어)<br/>
<p align="center"><img src="/assets/img/Computer Network/chapter3. Transport-layer services/3-66.png" width="500"></p>

&ensp;개념<br/>
* 라우터가 직접 송신자에게 피드백을 줌
* 네트워크 내부에서 혼잡이 감지되면 명시적(explicit)으로 알림을 보냄

&ensp;방식<br/>
* 혼잡이 발생한 라우터가 explicit congestion info를 송신자나 수신자에게 전달
* 이 피드백은 지금 혼잡해 또는 전송 속도를 줄여라 같은 정보를 포함할 수 있다.

&ensp;예시<br/>
* TCP ECN (Explicit Congestion Notification) → IP 헤더의 ECN 비트를 사용해 혼잡을 표시
* ATM (Asynchronous Transfer Mode), DECbit 등도 같은 목적의 프로토콜이다.

| 특징       | 설명                        |
| -------- | ------------------------- |
| 네트워크 피드백 | 있음 (라우터 → 송신자)          |
| 혼잡 판단 기준 | 라우터의 직접 정보                |
| 대표 프로토콜  | ECN, ATM, DECbit          |
| 장점       | 빠르고 정확한 대응 가능             |
| 단점       | 라우터에 추가 기능 필요 (비용↑, 복잡도↑) |

&ensp;비교<br>

| 구분       | End-to-End   | Network-Assisted |
| -------- | ------------ | ---------------- |
| 피드백 제공자  | 송신자 스스로 추론   | 라우터가 직접 전달       |
| 혼잡 감지 기준 | 손실, 지연       | 네트워크 내부 상태       |
| 대표 예시    | TCP          | ECN, ATM         |
| 장점       | 구현 간단, 범용적   | 빠르고 효율적          |
| 단점       | 반응 느림, 오차 가능 | 라우터 수정 필요        |

