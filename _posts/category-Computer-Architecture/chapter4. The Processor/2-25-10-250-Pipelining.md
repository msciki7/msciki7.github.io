---
title: "chapter 4-3. Ptpelining"
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
&ensp;🧩 비파이프라인 (non-pipelined)<br/>
* 명령어 n개 실행 시간 = n × (k × t)

&ensp;🧩 파이프라인 (pipelined)<br/>
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

&ensp;파이프라인 레지스터 (IF/ID, ID/EX, EX/MEM, MEM/WB)<br/>
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

Multiple-clock-cycle pipeline diagram(자원 사용도)
======

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

Single-Cycle Pipeline Diagram (데이터패스와 단계 연결)
====

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-3-14.png" width="500"></p>

&ensp;세로 파란 기둥 4개: IF/ID, ID/EX, EX/MEM, MEM/WB<br/>
&ensp;이게 바로 파이프라인 레지스터(각 단계 사이의 경계)<br/>
&ensp;역할:<br/>
1. 단계 분리: 한 단계에서 만든 결과를 다음 사이클까지 보관<br/>
2. 제어·데이터 동반 이동: 데이터뿐 아닌 제어 신호(RegWrite, MemRead, MemtoReg 등)도 함께 넘긴다.

&ensp;그림의 위쪽 타이틀(Instruction fetch / decode / execution / memory / write-back)은 해당 구간에서 실제 데이터가 어떤 블록을 통과하는지 보여준다.<br/>
&ensp;해당 구간에서 실제 데이터가 어떤 블록을 통과하는지 보여준다. 즉 단계 이름 ↔ 실제 회로 경로를 1:1로 매핑하는 도식<br/>

Extended Single-Cycle Pipeline Diagram (표로 쓰는 타이밍)
=====

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

