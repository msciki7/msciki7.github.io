---
title: "chapter 4-3. Pipelining"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-10-25
last_modified_at: 2025-10-25
---

파이프라이닝(Pipelining) 개요
=====

&ensp;파이프라이닝은 여러 명령어를 겹쳐서 실행하는 기술이다. 즉 하나의 명령어가 끝날 때까지 기다리지 않고 다음 명령어를 동시에 처리한다.<br/>
&ensp;마치 공장에서 조립 → 검사 → 포장 을 동시에 진행하는 것처럼 각 단계가 병렬로 실행되기 때문에 전체 작업 속도가 빨라진다.<br/>

&ensp;파이프라이닝의 특징<br/>
* 여러 명령어를 동시에 실행하여 처리 효율을 높인다.
* **순차적인 명령어 흐름 안에서 병렬성(parallelism)**을 이끌어낸다.
* 한 명령어의 실행 속도(execution time) 자체는 그대로지만 **전체 처리량(throughput)**이 향상된다.

&ensp;세탁소 비유 (Laundry Analogy)<br/>
&ensp;파이프라이닝을 쉽게 이해하기 위해 세탁 과정을 예를 들어볼 수 있다.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-1.png" width="500"></p>

| 구분                  | 설명                                                                  |
| ------------------- | ------------------------------------------------------------------- |
| **단일 처리 방식(위 그림)**  | A의 세탁이 완전히 끝난 후 B를 시작함 → 4개의 작업에 **8시간** 소요                         |
| **파이프라인 방식(아래 그림)** | A가 세탁 중일 때 B의 세탁물을 넣고, A가 건조 중일 때 C의 세탁 시작 → 4개의 작업에 **3.5시간**만에 완료 |

&ensp;속도 향상 (Speedup) = 8 / 3.5 = 약 2.3배<br/>
&ensp;파이프라이닝은 작업 단계까 겹치도록 만들어 전체 시간을 줄이는 방식이다.<br/>



&ensp;명령어 실행의 5단계 (5 Stages of Instruction Execution)<br/>

&ensp;파이프라이닝은 하나의 명령어를 5단계로 나누어 처리한다. 각 단계는 서로 다른 하드웨어 부품에서 동시에 수행된다.<br/>

| 단계                                              |설명                           |
| ----------------------------------------------- | ---------------------------- |
| **1️⃣ IF (Instruction Fetch)**                  | 명령어를 메모리에서 가져옵니다.            |
| **2️⃣ ID (Instruction Decode / Register Read)** | 명령어를 해석하고, 필요한 레지스터 값을 읽습니다. |
| **3️⃣ EX (Execute / Address Calculation)**      | 연산을 수행하거나 주소를 계산합니다.         |
| **4️⃣ MEM (Memory Access)**                     | 필요한 데이터를 메모리에서 읽거나 씁니다.      |
| **5️⃣ WB (Write Back)**                         | 결과를 레지스터에 저장합니다.             |


&ensp;이 다섯 단계를 파이프라인처럼 연결해두면 한 명령어가 3단계에 있을 때 다음 명령어는 2단계, 그 다음은 1단계에 있게 된다.<br/>

A Pipelined MIPS Processor
=====

* 현재 명령어가 끝나기 전에 다음 명령어를 시작한다.
* 그 결과 **처리량(throughput)**은 좋아지지만, **개별 명령어 지연(latency)**은 줄지 않는다.

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-2.png" width="500"></p>

&ensp;5단계 복습<br/>
&ensp;`IF → ID → EX → MEM → WB` <br/>
&ensp;각 단계가 서로 겹쳐서(오버랩)진행된다. 파이프라인의 클록 주기는 가장 느린 단계가 걸리는 시간에 의해 결정된다.<br/>

&ensp;Single-Cycle vs. Pipelined<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-3.png" width="500"></p>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-4.png" width="500"></p>

* 메모리 접근: 200 ps
* ALU 연산: 200 ps
* 레지스터 파일 읽기/쓰기: 100 ps

&ensp;1) 단일 사이클 구현 (Single-Cycle)<br/>
* 한 명령어가 한 번의 매우 긴 클록 안에 전 단계를 끝냄
* 클록 주기는 가장 오래 걸리는 명령어의 전체 경로로 정해짐
* 각 명령어별 총 시간(표 요약):
    - lw: 200(IF)+100(ID)+200(EX)+200(MEM)+100(WB)= 800 ps
    - sw: 200+100+200+200= 700 ps (WB 없음)
    - R-type: 200+100+200+100= 600 ps
    - beq: 200+100+200= 500 ps
* 하지만 클록은 하나이므로 결국 모든 명령어가 800 ps짜리 클록을 함께 사용(가장 긴 lw 기준) → 처리량: 800 ps당 1개

&ensp;파이프라인 구현 (Pipelined)<br/>
* 각 단계가 독립적으로 동작. 클록 주기 = 가장 긴 단계 시간 = 200 ps (EX, MEM이 200 ps로 가장 김)
* 이상적이라면 CPI ≈ 1 (파이프라인이 가득 찬 뒤엔 매 사이클마다 1개 완료)

&ensp;연속된 lw 3개<br/>
* Single-cycle: 3개 × 800 ps = 2400 ps
* Pipelined: 총 사이클 수 = k + (n−1) = 5 + (3−1) = 7 사이클 시간 = 7 × 200 ps = 1400 ps
* 속도 향상 = 2400 / 1400 ≈ 1.71배

&ensp;공식 요약<br/>
* 단일 사이클: T = IC × (LongestInstructionTime)
* 파이프라인: T = (k + (IC−1)) × StageTime (연속 실행 시) 평균적으로는 T ≈ IC × 1 × StageTime (충분히 길고 이상적일 때)

Pipeline Performance (파이프라인 성능)
=====

&ensp;클록 사이클의 기준: 파이프라인에서 **한 사이클의 길이(clock cycle time)**는 가장 오래 걸리는 단계(stage)에 맞춰 설정된다.<br/>

* IF: 180ps
* ID: 200ps
* EX: 150ps

&ensp;라면, 전체 클록은 200ps로 설정해야 한다.<br/>

&ensp;완벽히 균형 잡힌 파이프라인(perfectly balanced pipeline)<br/>
&ensp;모든 단계가 같은 시간(t)만큼 걸린다고 가정<br/>
&ensp;이때 파이프라인의 이점은 작업을 겹쳐서 실행할 수 있다는 것<br/>

* 비파이프라인(non-pipelined): 한 명령어가 끝나야 다음 명령어를 시작 → 명령어 사이 간격 = 전체 실행 시간 = k × t
* 파이프라인(pipelined): 각 단계가 겹쳐 실행됨 → 명령어 사이 간격 = t (즉 매 사이클마다 하나씩 결과가 나옴)

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-5.png" width="500"></p>

&ensp;파이프라인을 k단계로 나누면 명령어 간격이 k배 짧아진다는 뜻이다.<br/>

&ensp;속도 향상(Speedup)<br/>
&ensp;이제 수식으로 비교<br/>
&ensp;비파이프라인 (non-pipelined)<br/>
* 명령어 n개 실행 시간 = n × (k × t)

&ensp;파이프라인 (pipelined)<br/>
* 첫 번째 명령어가 끝나기까지: k사이클
* 나머지 n−1개의 명령어는 매 사이클마다 하나씩 끝남<br/>
&ensp;→ 총 사이클 수 = (k − 1) + n<br/>
&ensp;→ 총 실행 시간 = ((k − 1) + n) × t<br/>

&ensp;따라서, 속도 향상 비율(speedup):<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-6.png" width="500"></p>

&ensp;t가 공통이므로 단순화하면<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-7.png" width="500"></p>

&ensp;무한히 많은 명령어라면 (n → ∞)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-8.png" width="500"></p>

&ensp;명령어가 아주 많을수록 최대 속도 향상은 파이프라인 단계수(k)에 가까워진다.<br/>


&ensp;왜 실제 속도 향상은 이상적 값 k보다 작나?<br/>
&ensp;이론상 k단계 파이프라인이면 최대 k배 빨라질 수 있지만, 현실은 다음 이유로 감소한다.<br/>
1. 채우기/비우기 시간(Fill/Drain): 처음 k사이클 동안은 파이프라인을 채우느라 완성되는 명령어가 없음
2. Hazard(충돌): 데이터 해저드, 제어 해저드(분기), 구조적 해저드로 인해 stall(대기) 발생
3. 단계 불균형: 단계별 처리 시간이 다르면 전체 클록은 가장 느린 단계에 맞춰야 함
4. 오버헤드: 단계 사이 파이프라인 레지스터 지연(setup + propagation)이 클록에 추가됨

&ensp;3판 예제(수정 버전)로 보는 큰 그림<br/>
* 메모리 10 ps, ALU 9 ps, 레지스터 파일 8 ps, 그 외 0 ps
* 명령어 비율: lw 25%, sw 10%, R-type 45%, beq 15%, j 5%
* 총 명령어 수 IC = 10¹²

&ensp;(1) 고정 길이 단일 사이클(모든 명령어 1클록, 같은 길이)<br/>
* 클록 = 최악 경로 총합 = IF(10)+ID(8)+EX(9)+MEM(10)+WB(8) = 45 ps
* 실행시간 = 10¹² × 45 ps = **45 s**

&ensp;(2) 가변 길이 단일 사이클(모든 명령어 1클록이지만, 명령어별 클록 길이가 다름)<br/>
* 각 명령어가 자신의 실제 경로 길이만큼만 사용 → 평균 35.25 ps (슬라이드 결과)
* 실행시간 = 10¹² × 35.25 ps = **35.25 s**

&ensp;(3) 고정 길이 다중 사이클(여러 클록 사용, 클록 길이는 고정)<br/>
* 단계 원자 시간의 최댓값으로 클록 설정: 10 ps
* 명령어마다 필요한 **사이클 수(CPI)**의 평균 = 3.95 (슬라이드 결과)
* 실행시간 = 10¹² × 3.95 × 10 ps = **39.5 s**

&ensp;(4) 파이프라인<br/>
* 파이프라인 클록 = 10 ps (가장 느린 단계: 메모리 10 ps)
* 이상적 CPI ≈ 1
* 실행시간 = (k + IC) × 1 × 10 ps ≈ 10¹² × 10 ps = **10 s** (처음 k=5 사이클의 채우기 시간은 10¹²에 비하면 무시 가능)

&ensp;한 줄 결론: 같은 부품을 쓰더라도, 파이프라인은 처리량 관점에서 압도적으로 유리하다. 다만 실제 속도 향상은 Hazard/오버헤드/불균형 때문에 이론치보다 줄어든다.<br/>

Pipeline Hazards (파이프라인 해저드)
=====

&ensp;파이프라인에서 다음 명령어가 바로 실행되지 못하는 상황을 **파이프라인 해저드(hazard)**라고 한다. 즉 한 클록 주기 동안 어떤 명령어가 필요한 자원(resource)이나 데이터를 아직 사용할 수 없을 때 생기는 문제이다.<br/>

&ensp;1. Structural Hazard (구조적 해저드)<br/>
&ensp;원인: 여러 명령어가 동싣에 같은 하드웨어 자원을 사용하려고 할 때 발생한다.<br/>

&ensp;예를 들어: 한 명령어가 데이터 메모리 접근(MEM) 단계에 있고 다른 명령어가 명령어 메모리 접근(IF) 단계에 있을 때 → 두 명령어가 같은 메모리를 동시에 사용하려 함<br/>

&ensp;해결방법<br/>
* 자원(resource)을 늘린다.(예: 명령어와 데이터 메모리를 분리(Harvard Architecture))
* 즉 동시에 접근 가능한 하드웨어 구조로 개선

&ensp;식당에 주방이 하나뿐이면 여러 요리를 동시에 못 하는 것과 같다. 주방(자원)을 늘리면 해결된다.<br/>

&ensp;2. Data Hazard (데이터 해저드)<br/>
&ensp;원인<br/>
&ensp;다음 명령어가 이전 명령어의 결과값을 필요로 하지만 그 값이 아직 계산되지 않았을 때 발생한다.<br/>

&ens해결방법<br/>
* Pipeline Stall (파이프라인 멈춤) → 필요한 데이터가 준비될 때까지 대기
* Code Reordering (명령어 재배치) → 의존성이 없는 명령어를 사이에 넣어 기다림 시간 줄이기
* Forwarding (데이터 전달) → 레지스터에 저장되기 전, ALU 결과를 바로 다음 단계로 전달

&ensp;비유하자면 첫 번째 요리가 끝나야 두 번째 요리가 시작되는데 첫 번째 요리의 재료를 미리 옆으로 전달해주는 게 forwarding이다.<br/>

&ensp;3. Control Hazard (제어 해저드)<br/>
&ensp;원인<br/>
&ensp;분기나 점프(jump)명령어처럼 다음에 실행할 명령어의 주소를 결정해야 하는 상황에서 발생한다.<br/>

&ensp;해결방법<br/>
* Pipeline Stall: 결과가 나올 때까지 잠시 멈춤
* Branch Prediction(분기 예측): 다음에 갈 명령어를 미리 예측해서 실행(맞으면 빠르고 틀리면 되돌아감)
* Delayed Brach(지연 분기): 분기 명령어 바로 다음 명령어 1개는 무조건 실행하도록 설계 → pipeline 낭비를 줄이는 기법

&ensp;비유하자면 네비게이션이 다음 길을 아직 계산 중인데 운전자가 이미 움직이고 있는 상황이다. 미리 예측(Brach Prediction)하거나 잠시 정지(스톨)시켜야 한다.<br/>

| 해저드 종류         | 원인                 | 해결 방법                                    |
| -------------- | ------------------ | ---------------------------------------- |
| **Structural** | 하드웨어 자원 충돌         | 자원 늘리기, 메모리 분리                           |
| **Data**       | 이전 결과값이 아직 준비 안 됨  | Stall, Reordering, Forwarding            |
| **Control**    | 분기 결과에 따라 다음 주소 미정 | Stall, Branch Prediction, Delayed Branch |

Pipelined Datapath and Control
=====

&ensp;5단계 파이프라인, 한 줄 정의<br/>

| 단계                                     | 축약      | 단계에서 하는 일                                      | 대표 하드웨어                             |
| -------------------------------------- | ------- | ---------------------------------------------- | ----------------------------------- |
| **Instruction Fetch**                  | **IF**  | PC가 가리키는 **명령어**를 메모리에서 읽어옴, PC+4 계산           | PC, 명령어 메모리, **Adder(PC+4)**        |
| **Instruction Decode / Register Read** | **ID**  | 명령어 해석, **레지스터 파일**에서 피연산자 읽기, 즉시값 sign-extend | Control, Register File, Sign-Extend |
| **Execute / Address Calculation**      | **EX**  | **ALU 연산** 수행 또는 lw/sw를 위한 **유효주소 계산**         | ALU, MUX(연산 입력 선택)                  |
| **Memory Access**                      | **MEM** | lw는 **데이터 메모리 읽기**, sw는 **쓰기**                 | Data Memory                         |
| **Write Back**                         | **WB**  | 결과를 **레지스터 파일**에 기록                            | MUX(결과 선택), Register File           |

&ensp;포인트: EX는 계산, MEM은 메모리 접근, WB는 결과 저장이라고 외우면 깔끔하다.<br/>

&ensp;도식 읽는 법 (5 Steps of MIPS Datapath)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-9.png" width="500"></p>

* IF
    - PC ➜ Instruction Memory에서 명령어를 읽음
    - 동시에 PC+4를 Adder로 계산(다음 기본 PC)
* ID
    - 명령어의 필드(opcode, rs, rt, rd, imm)를 Control이 해석
    - Refister File에서 rs, rt 값을 읽어옴
    - I-형식이면 Sign-Extend로 즉시값(imm) 16→32비트
* EX
    - ALU가 두 입력 (source1, source2)을 받아 연산
    - R-type: 16 ⊕ rt → 결과
    - lw/sw: `ALU = rs + sign-extended imm` (유효 주소)
    - Branch: `ALU 비교` (예: beq 동일 여부), 분기 목적지 = `PC+4 + (imm<<2)`
* MEM
    - lw: Data Memory 읽기
    - sw: Data Memory 쓰기
    - Branch: 분기 여부 결정(파이프라인에선 보통 EX/MEM 경계나 MEM에서 결정하도록 설계하는 버전도 있음 → 제어 해저드 원인)
* WB
    - MUX로 선택: R-type/alu결과 vs lw/메모리데이터
    - 선택된 값을 Register File에 써 넣음

&ensp;도식의 MUX는 “이번 명령어가 어떤 타입인가?”에 따라 데이터 경로를 바꿔 주는 스위치다.<br/>

&ensp;Pipelined Execution: 왼쪽 → 오른 흐름의 두 가지 예외
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-10.png" width="500"></p>

&ensp;왼쪽에서 오른쪽으로만 흐르는 건 아니다는 두 지점: <br/>
1. WB → Register File(되돌림)
* WB에서 나온 결과가 레지스터 파일에 다시 입력된다.
* 바로 뒤 명령이 그 레지스터를 쓰면 Data Hazard가 생김
* 해결: Forwarding(ALU/MEM 결과를 바로 EX로 우회 전달) 또는 Stall
2. Next PC 선택(분기/점프)
* 다음 PC는 보통 PC+4지만, 분기 성립 시 분기목적지로 변경
* 이 정보가 EX/MEM 쪽에서 늦게 나오면, 이미 IF/ID 단계에 들어온 명령을 **플러시(flush)**해야 함
* 해결: Branch Prediction, Delayed Branch, Stall

&ensp;결과의 피드백(데이터)과 다음 주소 결정(제어)이 왼쪽→오른쪽 단방향 흐름을 깨뜨리는 예외이다.<br/>

# 파이프라인 레지스터 (IF/ID, ID/EX, EX/MEM, MEM/WB)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-11.png" width="500"></p>

&ensp;역할 두 가지<br/>
1. 단계 분리: 각 단계의 결과를 “다음 사이클”까지 붙잡아 둔다.
2. 제어·데이터 묶음 전달: 데이터뿐 아니라 Control 신호도 함께 넘긴다.

&ensp;각 레지스터에 보통 담기느 것(대표적 필드):<br/>
* IF/ID: `PC+4`, `Instruction`
* ID/EX: `RegRsVal`, `RegRtVal`, `SignExtImm`, 목적 레지스터 후보(rt/rd), 분기용 PC+4, 그리고 ALUOp, MemRead, MemWrite, RegWrite, MemtoReg 등 제어신호
* EX/MEM: `ALUResult`, `RtVal(메모리 쓰기 데이터)`, 선택된 목적 레지스터 번호, MemRead/Write, RegWrite, MemtoReg
* MEM/WB: `ReadData(메모리에서 읽은 값)`, `ALUResult`, 목적 레지스터 번호, RegWrite, MemtoReg

&ensp;시험 포인트: 제어신호도 레지스터를 타고 흘러간다.(데이터만 흐르는 게 아님)<br/>

&ensp;명령어별 실제 경로<br/>
* R-type (add, sub, …)<br/>
&ensp;`IF → ID(레지스터 읽기) → EX(ALU연산) → MEM(통과) → WB(ALU결과 쓰기)`<br/>
* lw<br/>
&ensp;`IF → ID → EX(주소=rs+imm) → MEM(읽기) → WB(메모리값 쓰기)`<br/>
* sw<br/>
&ensp;`IF → ID → EX(주소=rs+imm) → MEM(쓰기) → WB(통과)`<br/>
* beq<br/>
&ensp;`IF → ID(비교 레지스터 읽기) → EX(비교·분기타겟) → MEM/EX에서 분기판정(설계따라) → 이후 IF 플러시/유지`<br/>

&ensp;파이프라인에서 꼭 생기는 이슈 연결<br/>
* 데이터 해저드: WB 결과를 다음 명령 EX에서 미리 써야 하므로 ➜ Forwarding 경로가 도식에 추가됨(ALU 결과/메모리 결과를 EX의 입력으로 우회) ➜ 그래도 안 되는 경우(load-use)엔 한 사이클 Stall + bubble 삽입
* 제어 해저드: 분기 결과가 늦음 ➜ Flush(잘못 가져온 명령 제거), Predict taken/not-taken, Delayed branch 슬롯 활용


# Multiple-clock-cycle pipeline diagram(자원 사용도)


<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-12.png" width="500"></p>

* IM: Instruction Memory (명령어 메모리, IF 단계)
* Reg: Register File (ID 단계에서 읽고, WB에서 씀)
* ALU: 산술논리연산(또는 주소 계산, EX 단계)
* DM: Data Memory (MEM 단계: lw/read, sw/write)

&ensp;왼쪽에 명령어 목록(예: lw $10,20($1), sub $11,$2,$3 …), 위쪽에 시간축(CC1, CC2 …)<br/>
&ensp;각 명령어가 시간축을 따라 IM→Reg→ALU→DM→Reg 순으로 자원을 차례로 잡아먹는 모습을 보여준다.<br/>

&ensp;핵심 포인터<br/>
* 한 사이클에 **같은 자원(같은 블록)**을 두 명령어가 동시에 쓰지 않으면 충돌 없음
(교재 기본 가정: I-메모리와 D-메모리 분리라서 IF와 MEM은 구조 충돌이 없다.)
* lw는 IM→Reg→ALU→DM→Reg를 모두 사용하고
* R-type(add/sub)은 IM→Reg→ALU→Reg(DM은 통과)
* sw는 IM→Reg→ALU→DM(WB는 없음)

&ensp;Traditional multi-cycle pipeline diagram (단계 상자형)<br/>
&ensp;같은 실행을 단계이름(IF/ID/EX/MEM/WB) 상자로 나타낸 버전<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-13.png" width="500"></p>

&ensp;읽는 법은 간단해<br/>
* 가로축 = 사이클 번호(CC)
* 세로축 = 명령어 순서
* 각 명령어가 어떤 사이클에 어떤 단계에 있는지 만을 보여준다.
* 자원 충돌 여부는 직접 보이지 않지만 단계가 겹친다 = 파이프라인이 겹쳐 돈다는 걸 직관적으로 파악하기 쉽다.

&ensp;둘의 차이<br/>
* 자원 사용도: IM/ALU/DM/Reg 같은 하드웨어 사용을 강조
* 전통적 단계도: IF/ID/EX/MEM/WB 같은 추상 단계를 강조

# Single-Cycle Pipeline Diagram (데이터패스와 단계 연결)


<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-14.png" width="500"></p>

&ensp;세로 파란 기둥 4개: IF/ID, ID/EX, EX/MEM, MEM/WB<br/>
&ensp;이게 바로 파이프라인 레지스터(각 단계 사이의 경계)<br/>
&ensp;역할:<br/>
1. 단계 분리: 한 단계에서 만든 결과를 다음 사이클까지 보관<br/>
2. 제어·데이터 동반 이동: 데이터뿐 아닌 제어 신호(RegWrite, MemRead, MemtoReg 등)도 함께 넘긴다.

&ensp;그림의 위쪽 타이틀(Instruction fetch / decode / execution / memory / write-back)은 해당 구간에서 실제 데이터가 어떤 블록을 통과하는지 보여준다.<br/>
&ensp;해당 구간에서 실제 데이터가 어떤 블록을 통과하는지 보여준다. 즉 단계 이름 ↔ 실제 회로 경로를 1:1로 매핑하는 도식<br/>

# Extended Single-Cycle Pipeline Diagram (표로 쓰는 타이밍)

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-15.png" width="500"></p>

&ensp;마지막 표는 사이클별로 어느 명령어가 어느 단계에 있냐를 글자로 정리한 버전<br/>
&ensp;규칙(이상적인 5단계 파이프라인, 해저드/스톨 없음 가정):<br/>

1. I1은 clock1에 IF를 시작하고, 매 사이클 단계가 하나씩 오른쪽으로 이동한다. → clock1: IF(I1), clock2: ID(I1), clock3: EX(I1), clock4: MEM(I1), clock5: WB(I1)
2. I2는 I1의 다음 사이클에 IF를 시작한다. → clock2: IF(I2), clock3: ID(I2) …
3. n개의 명령을 처리하는 총 사이클 수(이상적)는 n + (k − 1), 여기서 k=5단계 → 충분히 길어지면 CPI ≈ 1

&ensp;표 해석 예시(슬라이드와 같은 패턴):<br/>
* clock1: IF에 I1
* clock2: IF에 I2, ID에 I1
* clock3: IF에 I3, ID에 I2, EX에 I1

# Pipelined Version of the Datapath

&ensp;lw Instruction<br/>
&ensp;의미: $t1 ← Memory[$t2 + 0]<br/>
&ensp;즉, 메모리에서 값 읽기(load)<br/>
* $t2: 베이스 주소 레지스터
* 0: 오프셋(immediate)
* $t1: 읽은 값을 저장할 목적 레지스터

&ensp;1단계: IF (Instruction Fetch Stage)<br/>
&ensp;하는 일
1. **PC(Program Counter)**가 가리키는 주소에서 명령어를 읽음 → Instruction Memory[PC]
2. 동시에 PC + 4 계산 (다음 명령어 주소)

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-16.png" width="500"></p>

&ensp;데이터 흐름<br/>
* PC → Instruction Memory로 주소 전송
* 명령어 → IF/ID 파이프라인 레지스터로 저장
* **Adder(PC+4)**의 결과도 IF/ID에 함께 저장

&ensp;그림 해석<br/>
* 왼쪽 위의 PC → Instruction Memory 화살표 = 명령어 읽기
* 오른쪽 PC+4 화살표 = 다음 명령어 주소 계산
* 결과는 세로 블록(IF/ID)에 임시 저장

&ensp;2단계: ID (Instruction Decode / Register Read Stage)<br/>
&ensp;하는 일<br/>
1. 명령어 해석 (Instruction Decode) → opcode가 lw임을 인식
2. 레지스터 파일 접근
* $t2(rs 필드) 값 읽기
* 목적지 $t1(rt 필드)을 식별 (나중에 쓸 예정)
3. 즉시값(immediate) sign-extend (16비트 → 32비트)

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-17.png" width="500"></p>

&ensp;데이터 흐름<br/>
* IF/ID 레지스터에서 꺼낸 opcode, rs, rt, imm를 이용
* Register File → rs 값 읽음 (Reg[rs])
* Sign-Extend 블록이 imm(16bit)을 32bit로 확장
* 모든 정보(Reg[rs], SignExtImm, rt)가 ID/EX 레지스터로 이동

&ensp;그림 해석<br/>
* 중앙 Register File에서 두 값이 빠져나가는 선이 보임
* 아래쪽 "Sign-Extend"에서 즉시값 확장
* ID/EX 레지스터로 전달됨

&ensp;3단계: EX (Execute / Address Calculation Stage)<br/>
&ensp;하는 일<br/>
1. 유효 주소 계산: ALUResult = Reg[rs] + SignExtImm → 즉, 메모리 접근할 실제 주소를 계산
2. lw/sw에서는 ALU가 덧셈기 역할

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-18.png" width="500"></p>

&ensp;데이터 흐름<br/>
* ALU의 두 입력:
    - 첫 번째: ID/EX에서 온 Reg[rs]
    - 두 번째: Sign-Extended Immediate
* ALU 결과(Address)가 EX/MEM 레지스터로 전달

&ensp;그림 해석:<br/>
* ALU 입력 두 개가 선으로 연결돼 있음
* ALU 출력(유효 주소)이 EX/MEM으로 들어감
* 위쪽의 작은 Add(PC+4+s*hift) 부분은 branch 계산용, lw에서는 무시됨

&ensp;4단계: MEM (Memory Access Stage)<br/>
&ensp;하는 일<br/>
1. 데이터 메모리 접근: ReadData = DataMemory[ALUResult] → EX 단계에서 계산된 주소를 이용해 메모리에서 값 읽기
2. lw → 읽기(Read) / sw → 쓰기(Write) 로 구분됨.

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-19.png" width="500"></p>

&ensp;데이터 흐름<br/>
* ALUResult(주소) → Data Memory의 Address 입력으로 전달
* Data Memory → MEM/WB 파이프라인 레지스터로 읽은 데이터 전달

&ensp;그림 해석
* 오른쪽의 Data Memory 블록이 하이라이트되어 있음
* 주소 입력은 EX/MEM 레지스터에서, 출력(Read data)은 MEM/WB로 들어감

&ensp;5단계: WB (Write Back Stage)<br/>
&ensp;하는 일<br/>
1. 읽은 데이터를 레지스터 파일에 저장: Reg[rt] = ReadData
2. 어떤 값을 쓸지 선택하는 MUX(멀티플렉서)가 사용됨:
    - lw: Data Memory에서 읽은 값 선택
    - R-type: ALU 결과 선택

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-20.png" width="500"></p>

&ensp;데이터 흐름<br/>
* MEM/WB 레지스터 → MUX → Register File 입력으로 연결
* RegWrite 신호가 1이 되어 `$t1`(rt)에 값 저장

&ensp;그림 해석<br/>
* 오른쪽 아래 MUX에서 "메모리 값"이 선택되어 Register File로 돌아가는 선이 표시됨
* $t1 레지스터(목적지)에 쓰기 동작이 일어남 (빨간 원 표시 부분)

&ensp;전체 흐름 요약<br/>

| 단계      | 주요 동작           | 핵심 하드웨어                             | 전달 정보               |
| ------- | --------------- | ----------------------------------- | ------------------- |
| **IF**  | 명령어 읽기          | PC, Instruction Memory, Adder(PC+4) | Instruction, PC+4   |
| **ID**  | 명령어 해석, 레지스터 읽기 | Control, Register File, Sign-Extend | Reg[rs], SignExtImm |
| **EX**  | 주소 계산           | ALU                                 | Address             |
| **MEM** | 메모리에서 데이터 읽기    | Data Memory                         | ReadData            |
| **WB**  | 읽은 데이터 레지스터에 쓰기 | MUX, Register File                  | Reg[rt] ← ReadData  |

* Control signal 흐름:
    - RegWrite = 1
    - MemRead = 1
    - MemtoReg = 1
    - ALUSrc = 1 (두 번째 피연산자에 imm 사용)


# Corrected Pipelined Datapath

&ensp;문제: `lw` 는 결과를 WB단계에서 레지스터 파일에 쓴다. 따라서 어느 레지스터에 쓸지(rt)정보가 IF→ID→EX→MEM→WB까지 사이클을 건너 이동해야 한다. 초기 데이터패스 그림에서 이 **목적 레지스터 번호(rt)**를 중간에 잃어버리면 WB에서 어디에 써야 하는지 알 수 없다.<br/>
&ensp;해결: 목적 레지스터 번호를 각 파이프라인 레지스터에 함께 저장/전달한다.<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-21.png" width="500"></p>

* IF/ID: Instruction(= rt 필드 포함), PC+4
* ID/EX: `Reg[rs]`, `Reg[rt]`, `SignExtImm`, rt(목적지 후보), 제어신호(ALUSrc, MemRead, MemWrite, RegWrite, MemtoReg …)
* EX/MEM: `ALUResult(주소/연산결과)`, rt(목적지/또는 DM 쓰기 데이터의 원본 번호), `WriteData(=Reg[rt] 값)`
* MEM/WB: `ReadData(lw)`, `ALUResult`(R-type), DestReg(최종 목적 레지스터 번호), `RegWrite`, `MemtoReg`

&ensp;sw in EX / MEM / WB – 단계별 차이<br/>
&ensp;sw – EX 단계<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-22.png" width="500"></p>

* 주소 계산: `ALU = Reg[rs] + SignExtImm`
* 동시에 메모리에 쓸 데이터는 Reg[rt]값이므로 ID단계에서 읽어온 `Reg[rt]`를 EX/MEM 레지스터의 `WriteData` 필드로 넘겨둔다.

&ensp;주의: sw는 목적 레지스터가 없지만, **쓰기 데이터(Reg[rt])**를 다음 단계까지 값 그대로 들고 가야 한다.<br/>

&ensp;sw – MEM 단계<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-23.png" width="500"></p>

* Data Memory Write: `DataMem[ALUResult] ← WriteData`
* 제어 신호: `MemWrite=1`, `MemRead=0`, `RegWrite=0`

&ensp;의존성 주의: 이전 명령의 결과를 sw가 바로 써야 하는 경우, WriteData에 forwarding이 필요할 수 있다.(예: add $t0,...; sw $t0, 0($s1))<br/>

&ensp;sw – WB 단계<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-24.png" width="500"></p>

* 아무 것도 안 함. (레지스터에 쓸 것이 없으므로 RegWrite=0)
* 파이프라인은 WB를 지나만 간다.

&ensp;sw 제어 신호 패턴: `ALUSrc=1, MemRead=0, MemWrite=1, RegWrite=0, MemtoReg=X(사용 안 함)`<br/>

&ensp;lw vs sw - 데이터 경로 비교 표<br/>

| 항목           | `lw rt, imm(rs)`                                                  | `sw rt, imm(rs)`                            |
| ------------ | ----------------------------------------------------------------- | ------------------------------------------- |
| EX           | 주소 = `Reg[rs] + imm`                                              | 주소 = `Reg[rs] + imm`                        |
| MEM          | **Read** `DataMem[addr]`                                          | **Write** `DataMem[addr] ← Reg[rt]`         |
| WB           | **`Reg[rt] ← ReadData`** (RegWrite=1, MemtoReg=1)                 | 없음 (RegWrite=0)                             |
| 필요 신호        | ALUSrc=1, MemRead=1, MemWrite=0, RegWrite=1, MemtoReg=1, RegDst=0 | ALUSrc=1, MemRead=0, MemWrite=1, RegWrite=0 |
| 파이프라인에 보존할 것 | **목적지 번호(rt)**, 제어신호, ALUResult, ReadData                         | **WriteData(=Reg[rt])**, 제어신호, ALUResult    |

Pipelined Control
====

&ensp;제어는 한 번 생성, 단계별로 전달<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-25.png" width="500"></p>

* 제어신호는 ID 단계(명령어 해독 시)에서 한 번 생성된다.(Control Unit이 opcode/funct를 보고 결정)
* 생성된 제어신호는 파이프라인 레지스터를 타고 해당 단계까지 운반된다.
    - EX에서 필요한 신호 → ID/EX에 저장
    - MEM에서 필요한 신호 → ID/EX → EX/MEM으로 전달
    - WB에서 필요한 신호 → ID/EX → EX/MEM → MEM/WB로 전달
* 이렇게 해야, 각 사이클에 올바른 단계가 자기 차례에 맞는 제어를 정확히 받는다.

&ensp;단계별로 실제 필요한 제어신호<br/>

| 단계      | 필요한 제어                                       | 역할(대표)                                               |
| ------- | -------------------------------------------- | ---------------------------------------------------- |
| **IF**  | (고정 동작)                                      | PC+4 계산, 명령어 메모리 읽기 — *ID에서 별도 제어 없음*                |
| **ID**  | (제어 생성)                                      | opcode/funct 해석 → **아래 신호들을 생성**                     |
| **EX**  | `RegDst`, `ALUOp(1:0)`, `ALUSrc`             | 목적 레지스터 선택(rd/rt), ALU 연산 종류, ALU 입력 선택(레지스터 vs 즉시값) |
| **MEM** | `Branch`(beq), `MemRead`(lw), `MemWrite`(sw) | 분기 판단·타겟 선택, 데이터 메모리 접근                              |
| **WB**  | `RegWrite`, `MemtoReg`                       | 레지스터 파일에 쓸지/무시할지, 쓰는 값이 ALU결과인지 메모리데이터인지             |

&ensp;F/ID에서 아무것도 안 한다는 말은 별도 제어가 필요 없다는 뜻(항상 동일 동작) 진짜 제어는 ID에서 만들어, 각 단계에 필요한 시점에 도착하게 해주면 된다.<br/>

&ensp;명령어별 제어신호 패턴<br/>

| Instruction                         | RegDst | ALUOp1 | ALUOp0 | ALUSrc | Branch | MemRead | MemWrite | RegWrite | MemtoReg |
| ----------------------------------- | :----: | :----: | :----: | :----: | :----: | :-----: | :------: | :------: | :------: |
| **R-format** (`add/sub/and/or/slt`) |    1   |    1   |    0   |    0   |    0   |    0    |     0    |     1    |     0    |
| **lw**                              |    0   |    0   |    0   |    1   |    0   |    1    |     0    |     1    |     1    |
| **sw**                              |    X   |    0   |    0   |    1   |    0   |    0    |     1    |     0    |     X    |
| **beq**                             |    X   |    0   |    1   |    0   |    1   |    0    |     0    |     0    |     X    |

* RegDst: 목적 레지스터가 rd(1)인지 rt(0)인지
* ALUOp: ALU에 연산 종류 힌트를 제공 (10=R형, 00=add, 01=sub/beq)
* ALUSrc: 두 번째 ALU 입력을 레지스터(0) vs 즉시값(1) 중 선택
* Branch: beq에서 분기 비교·PC 선택에 사용
* MemRead / MemWrite: 데이터 메모리 접근
* RegWrite: 레지스터 파일 쓰기 활성화
* MemtoReg: WB에서 쓰는 값 선택(ALU(0) vs 메모리(1))

&ensp;X는 "상관없음" — 해당 명령에서는 그 신호를 사용하지 않는다.<br/>

&ensp;신호의 이동 경로<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-26.png" width="500"></p>

* ID 단계의 Control이 명령어를 보고 세 묶음으로 신호를 뽑아낸다:
    - EX 묶음(예: RegDst, ALUOp, ALUSrc) → ID/EX에 저장
    - MEM 묶음(예: Branch, MemRead, MemWrite) → ID/EX → EX/MEM으로 전달
    - WB 묶음(예: RegWrite, MemtoReg) → ID/EX → EX/MEM → MEM/WB로 전달
* 따라서 EX·MEM·WB 단계는 자기 차례가 되었을 때 해당 신호를 정확히 받는다.

&ensp;완성형 파이프라인에서 보는 신호 흐름<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-27.png" width="500"></p>

* 파란 선(또는 블록)으로 표시된 경로가 제어신호의 운바로
* 데이터 경로(검은 선)와 제어 경로(파란 선)가 각 단계 레지스터에서 함께 이동한다.
* PCSrc(다음 PC 선택)은 보통 Branch & Zero 결과로 만들며, 분기 성립 시 분기목적지를 선택하고 IF/ID 플러시가 동반될 수 있다(제어 해저드 처리)

&ensp;예시<br/>
&ensp;1000: lw $1,81($2)<br/>
&ensp;1004: add $3,$4,$5<br/>
&ensp;1008: sub $6,$7,$8<br/>
&ensp;1012: slt $9,$10,$11<br/>
&ensp;1016: beq $12,$13, XX<br/>

&ensp;$r = r+1<br/>
&ensp;M[x] = x*2<br/>

&ensp;1) 큰 틀부터 잡기: 5단계와 경계선<br/>
1. IF (Instruction Fetch)
* PC, Instruction Memory, PC+4 Adder
2. ID (Instruction Decode / Register Read)
* Control Unit, Register File(레지스터 읽기/쓰기), Sign-Extend
3. EX (Execute / Address Calculation)
* ALU, ALU control, Shift-left-2, Branch target adder, MUX들
4. MEM (Data Memory Access)
* Data Memory, MemRead/MemWrite
5. WB (Write Back)
* MUX(결과 선택) → Register File(쓰기)

&ensp;각 단계 사이의 세로 파란 기둥(IF/ID, ID/EX, EX/MEM, MEM/WB)이 파이프라인 레지스터 → 이전 사이클에서 만든 값 + 제어신호를 다음 사이클까지 보존하고 넘겨준다.<br/>

&ensp;선/블록의 의미 익히기<br/>
* 굵은 검은 선: 데이터가 흐르는 길
* 파란 선/라벨: 제어신호(어디서 만들고 어디로 가는지)
* 삼각형 모양(MUX): 여러 입력 중 하나를 선택(예: ALUSrc, MemtoReg, RegDst, PCSrc)
* ALU: 산술/논리 연산, `Zero` 출력으로 beq 판단에 사용
* Adder 2개
    - 왼쪽 위 Adder: PC+4
    - EX 영역 Adder: Branch Target = (PC+4) + (Sign-extended imm << 2)
* Register File 포트
    - Read reg1/2 → Read data1/2
    - Write reg + Write data (WB 단계에서 RegWrite=1일 때만 기록)

&ensp;3) 명령 하나를 따라가며 읽는 법<br/>
&ensp;예시 첫 줄: `1000: lw $1, 81($2)` <br/>
&ensp;(A) IF<br/>
* PC가 1000 → **InstrMem[1000]**에서 lw 명령을 읽음
* 동시에 PC+4(=1004) 계산
* 읽은 명령과 `PC+4`는 IF/ID 레지스터에 저장

&ensp;(B) ID<br/>
* Control이 opcode를 보고 lw용 제어신호 생성
    - `ALUSrc=1, MemRead=1, MemWrite=0, RegWrite=1, MemtoReg=1, RegDst=0`
* Register File에서 $2 값 읽음, 즉시값 81을 sign-extend
* 목적지 **레지스터 번호(rt=$1)**도 함께 ID/EX 레지스터로 보관

&ensp;(C) EX<br/>
* ALU: 주소 = $2 + 81 (오른쪽 MUX가 ALUSrc=1로 즉시값을 선택)
* 주소/제어신호/쓰기 레지스터 번호가 EX/MEM으로 이동

&ensp;(D) MEM<br/>
* MemRead=1 → **DataMemory[주소]**에서 값 읽기
* 읽은 데이터는 MEM/WB로 이동

&ensp;(E) WB<br/>
* MUX에서 MemtoReg=1 → 메모리 데이터 선택
* RegWrite=1이므로 $1(rt)에 기록

&ensp;다음 명령(`add $3, $4, $5`)도 같은 회로 위를 한 칸씩 오른쪽으로 이동하며 진행한다. 즉 파이프라인 레지스터가 현재 명령의 상태를 단계별로 운반해 주는 것<br/>

&ensp;분기/비교/연산을 볼 때의 포인트<br/>
* R-type (add/sub/and/or/slt):
    - RegDst=1 → 목적지 rd 선택, ALUSrc=0(두 번째 피연산자=레지스터)
    - ALUOp + funct → ALU연산 결정
    - MemtoReg=0 → ALU 결과를 WB로 써준다.
* beq:
    - ALU가 **두 레지스터를 뺀 결과의 Zero**를 사용
    - Branch=1 AND Zero=1 → PCSrc=1이 되어 다음 PC를 Branch Target으로 바꿈
    - 일반적으로 RegWrite=0 (레지스터 쓰지 않음)
* sw:
    - 주소 rs + imm 계산은 lw와 동일(EX)
    - MemWrite=1, RegWrite=0 → WB 없음
    - 쓰기 데이터는 ID에서 읽어온 rt 값이 EX/MEM을 거쳐 MEM으로 들어간다.

&ensp;회로 읽기 체크리스트<br/>
1. 어느 단계인가? (IF/ID/EX/MEM/WB)
2. 데이터는 어디서 와서 어디로 가는가?
    - PC/Instr, 레지스터 값, 즉시값, ALU 결과, 메모리 데이터
3. 어떤 MUX가 무엇을 선택하는가?
    - ALUSrc, MemtoReg, RegDst, PCSrc
4. 제어신호는 이미 도착했나?
   - ID에서 만들어져 파이프라인 레지스터를 통해 필요한 단계에 도착해야 함
5. 목적 레지스터 번호/쓰기 데이터가 끝까지 보존되나?
    - lw: rt 번호가 MEM/WB까지 가야 함
    - sw: **WriteData(rt 값)**이 EX/MEM→MEM으로 전달
6. 분기면 PC 경로 확인
    - Branch & Zero → PCSrc → 상단의 PC MUX로 되돌아감

&ensp;예시 시퀀스를 회로 위에서 빠르게 추적하는 팁<br/>
```markdown
1000: lw  $1, 81($2)
1004: add $3,$4,$5
1008: sub $6,$7,$8
1012: slt $9,$10,$11
1016: beq $12,$13, XX
```

* 각 명령은 매 사이클 오른쪽 단계로 한 칸씩 이동한다.
* 의존성이 없다고 가정하면(슬라이드 의도), stall 없이 표준 5단계 타임라인으로 흘러간다.
* beq가 도착하면 EX에서 비교 → PCSrc로 상단 PC MUX가 분기목적지를 고르고, IF/ID에 들어와 있던 오염된 명령은 flush(NOP)될 수 있다.(교재 정책에 따라 1~2 사이클 낭비)

&ensp;사이클별 파이프라인 표<br/>

| Clock | IF     | ID     | EX     | MEM    | WB     |
| ----: | ------ | ------ | ------ | ------ | ------ |
|     1 | **I1** |        |        |        |        |
|     2 | **I2** | **I1** |        |        |        |
|     3 | **I3** | **I2** | **I1** |        |        |
|     4 | **I4** | **I3** | **I2** | **I1** |        |
|     5 | **I5** | **I4** | **I3** | **I2** | **I1** |
|     6 | (다음)   | **I5** | **I4** | **I3** | **I2** |
|     7 |        | (다음)   | **I5** | **I4** | **I3** |
|     8 |        |        |        | **I5** | **I4** |
|     9 |        |        |        |        | **I5** |

* 총 사이클 = n + (k−1) = 5 + 4 = 9
* 분기(beq) 판정 시점: I5가 EX에 들어가는 Clock 7
    - taken이면, Clock 6~7에 IF/ID에 들어온 “다음 명령어들”을 flush(NOP) 해야 함
    - not-taken이면 위 표 그대로 진행

&ensp;명령어별 제어신호(정석 값)<br/>

&ensp;ID 단계에서 생성되어, 필요한 단계까지 파이프라인 레지스터(ID/EX, EX/MEM, MEM/WB) 를 통해 전달된다.<br/>
| Instr      | RegDst | ALUOp1 | ALUOp0 | ALUSrc | Branch | MemRead | MemWrite | RegWrite | MemtoReg |
| ---------- | :----: | :----: | :----: | :----: | :----: | :-----: | :------: | :------: | :------: |
| **lw**     |    0   |    0   |    0   |    1   |    0   |    1    |     0    |     1    |     1    |
| **add**(R) |    1   |    1   |    0   |    0   |    0   |    0    |     0    |     1    |     0    |
| **sub**(R) |    1   |    1   |    0   |    0   |    0   |    0    |     0    |     1    |     0    |
| **slt**(R) |    1   |    1   |    0   |    0   |    0   |    0    |     0    |     1    |     0    |
| **beq**    |    X   |    0   |    1   |    0   |    1   |    0    |     0    |     0    |     X    |

* EX 단계에서 쓰는 신호: RegDst, ALUOp(1:0), ALUSrc
* MEM 단계에서 쓰는 신호: Branch, MemRead, MemWrite
* WB 단계에서 쓰는 신호: RegWrite, MemtoReg
* R-type의 실제 ALU 연산(add/sub/slt)은 ALUOp=10과 funct 필드로 ALU Control이 결정


Structural Hazard (구조적 해저드)
====

&ensp;정의: 하드웨어 자원을 동시에 쓰려는 명령어들이 충돌하는 상황<br/>
&ensp;파이프라인은 여러 명령어를 동시에 실행 단계별로 겹쳐서 수행한다. 그런데 이 명령어들이 같은 하드웨어(자원)를 동시에 쓰려고 하면 충돌(conflict)이 발생한다.<br/>

&ensp;결과 — Stall(멈춤)과 Bubble(빈칸)<br/>
* 한 명령어가 메모리를 사용하는 동안, 다른 명령어는 기다려야(stall) 함.
* 기다리는 동안 파이프라인이 멈춰서 빈칸이 생김 → 이것을 bubble(버블) 이라고 부른다.

&ensp;예를 들어:<br/>
```sql
Cycle 1: IF   (명령어1)
Cycle 2: ID   (명령어1), IF (명령어2)
Cycle 3: EX   (명령어1), ID (명령어2), IF (명령어3)
Cycle 4: MEM  (명령어1), ID (명령어3) ❌ (충돌 발생)
```

&ensp;→ 명령어 3은 stall 해야 하므로, IF 단계에서 멈춤<br/>

&ensp;해결 방법 — 분리된 메모리 구조<br/>
&ensp;두 개의 메모리(or 캐시)를 사용<br/>
* Instruction Memory (명령어 메모리) → IF 단계 전용
* Data Memory (데이터 메모리) → MEM 단계 전용

&ensp;이렇게 하면 명령어를 가져오는 명령과 데이터를 읽는 명령이 서로 다른 메모리 공간을 쓰기 때문에 충돌이 사라진다.<br/>