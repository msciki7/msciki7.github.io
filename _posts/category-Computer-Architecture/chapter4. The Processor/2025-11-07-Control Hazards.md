---
title: "chapter 4-5. Control Hazards"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-11-07
last_modified_at: 2025-11-07
---

Control Hazard(Branch Hazard)
======

&ensp;파이프라인에서 제어 흐름이 바뀌는 명령어(Branch, Jump 등)가 등장할 때 발생하는 문제를 말한다. 다음에 어떤 명령어를 가져와야 할지 결정되지 않은 상태에서 잘못된 명령을 가져와 실행하게 되는 상황이다.<br/>

&ensp;원인<br/>
* 분기(Branch) 명령의 결과를 계산하기 전까지 다음 명령어의 주소를 확정할 수 없음
* 파이프라인은 항상 명령어를 미리 가져오므로(fetch) 잘못된 명령어를 가져올 가능성이 생김
* 이로 인해 올바른 명령어를 실행하기 전까지 지연(delay) 발생

&ensp;해결 방법(Solutions)<br/>
1. Stall on Branch → 분기 결과가 확정될 때까지 파이프라인을 멈춘다.
2. Branch Prediction (분기 예측) → 분기가 일어날지 예측해서 미리 명령어를 가져온다.
3. Delayed Branch (지연 분기) → 분기 명령어 바로 뒤의 명령어를 항상 실행하도록 스케줄링한다.

&ensp;Impact of Pipeline on Branch<br/>
&ensp;파이프라인에서 분기 결과가 MEM 단계에서 결정되는 경우 이미 여러 개의 명령어가 fetch되어 실행 중일 수 있다.<br/>
&ensp;이 경우 잘못 가져온 명령어들을 Flush(제거)해야 한다.<br/>

&ensp;→ Flush = 파이프라인에 잘못 들어온 명령어의 제어 신호를 0으로 설정해 무효화<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-1.png" width="500"></p>

&ensp;분기 명령어가 MEM 단계에서 결정될 경우 그 사이에 들어온 명령어들이 모두 무효화된다.<br/>

Solution 1 - Stall on Branch
====

* 분기 결과가 결정될 때까지 파이프라인이 멈춘다.
* 다음 명령어를 가져오지 않고 대기(bubble)를 삽입한다.

&ensp;성능 손실(Penalty)<br/>
* Branch가 MEM단계에서 결정될 경우 → 3 cycle penalty
* Branch가 ID단계에서 결정될 경우 → 1 cycle penalty

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-2.png" width="500"></p>

&ensp;분기 명령어(beq)가 실행될 때 다음 명령어들을 bubble로 대체하며 기다림<br/>

# Branch Execution in MEM Stage

&ensp;특징<br/>
* 분기 결과가 MEM 단계에서 계산되므로 3개의 bubble(=3 cycle penalty)이 발생한다.

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-3.png" width="500"></p>

&ensp;→ 3 cycle 동안 파이프라인이 멈춰 있다가 lw 명령이 새로 시작됨<br/>

# Branch Execution in ID Stage

* 분기 결과를 ID 단계에서 미리 결정할 수 있다면 → 대기 시간이 1 cycle로 줄어듦

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-4.png" width="500"></p>

* → 단 1 cycle만 bubble이 생기고 이후 명령어가 바로 실행됨<br/>

| 구분                | Branch 결정 시점 | Penalty  | 비고          |
| ----------------- | ------------ | -------- | ----------- |
| MEM 단계            | 늦게 결정됨       | 3 cycles | Flush 많음    |
| ID 단계             | 빠르게 결정됨      | 1 cycle  | 성능 개선       |
| Branch Prediction | 예측 성공 시      | 0 cycle  | 실패 시 재실행 필요 |
| Delayed Branch    | 컴파일러 최적화     | 0 cycle  | 명령어 재배치 필요  |

&ensp;Reducing the Delay of Branches<br/>
&ensp;분기 명령어(branch)로 인한 지연을 줄이기 위해 Branch Execution Stage를 변경하고 데이터패스(datapath)에 약간의 구조적 변화를 준다.<br/>

&ensp;Branch Execution in ID Stage<br/>
&ensp;기존에는 MEM단계에서 분기 결과를 알 수 있지만 이를 ID 단계에서 판단하도록 개선한다.<br/>

| 구분      | MEM 단계에서 결정   | ID 단계에서 결정    |
| ------- | ------------- | ------------- |
| Flush 수 | 3개의 명령어 Flush | 1개의 명령어 Flush |
| Penalty | 3 cycles      | 1 cycle       |
| 처리속도    | 느림            | 빠름            |

&ensp;Datapath 수정<br/>
&ensp;ID 단계에서 분기를 수행하기 위해 아래 두 가지 수정<br/>
1. Branch Adder 이동
  - 원래 EX 단계에 있는 Branch Target Address 계산기를 → ID 단계로 이동
2. Comparator 삽입
  - 두 레지스터 값을 비교(==)하기 위한 Comparator 회로를  → ID 단계에 추가

&ensp;이렇게 하면 분기 여부를 ID 단계에서 바로 결정할 수 있다.<br/>

* 역할: IF/ID 레지스터의 명령어 필드를 0으로 초기화 (NOP 명령으로 대체)
* 결과: 잘못된 명령어를 무효화(Flush 수행)

&ensp;NOP(No Operation) = 0000 0000₁₆<br/>

&ensp;IF.Flush = "이 명령은 실행하지 말고 버려라!" 신호임<br/>

&ensp;Final Datapath and Control<br/>