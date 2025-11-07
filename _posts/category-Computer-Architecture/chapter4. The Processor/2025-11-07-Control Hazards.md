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
&ensp;아래 회로는 Control Hazard 대응이 추가된 최종 MIPS 파이프라인이다.<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-5.png" width="500"></p>

&ensp;추가된 주요 요소<br/>
1. IF.Flush 제어선
* Branch misprediction 시 IF/ID 파이프라인 레지스터를 초기화
2. Branch Adder(Shift Left + Adder)
* ID 단계에서 Branch Target 계산
3. Comparator(=)
* 레지스터 두 값을 비교하여 분기 조건 판단

&ensp;이 3가지 함께 작동하여 지연을 최소화하는 파이프라인 구조를 만든다.<br/>

&ensp;Example: Stall on Branch 성능 영향 (CPI 계산)<br/>
&ensp;분기 명령어가 프로그램 전체에서 차지하는 비율이 17% (SPECint2006 기준) 일 때 Stall on Branch 방식이 평균 CPI에 미치는 영향을 계산해보면<br/>

&ensp;조건<br/>
* Branch 명령의 빈도 = 17%
* Branch 명령의 CPI = 1 (기본) + 1 (stall)
* 다른 명령어의 CPI = 1

&ensp;계산<br/>
&ensp;Average CPI=1+0.17×(1)=1.17<br/>
&ensp;분기 지연으로 인해 전체 CPI가 약 17% 증가한다.<br/>

| 항목        | 내용                                 | 효과                |
| --------- | ---------------------------------- | ----------------- |
| **문제**    | Control Hazard (분기 결과 대기)          | Pipeline 정지       |
| **기본 해결** | Stall on Branch                    | 3~1 cycle penalty |
| **개선 방법** | Branch 실행을 ID 단계로 이동               | penalty 감소        |
| **추가 요소** | Branch Adder, Comparator, IF.Flush | 잘못된 명령 제거         |
| **결과**    | Branch 지연 최소화, 평균 CPI 개선           | 효율적 파이프라인         |

Solution 2 – Branch Prediction
=====

&ensp;파이프라인이 길어질수록 분기 결과를 빨리 알기 어렵다. 즉 분기 명령이 어디로 갈지를 기다리며 멈춰야 하는 시간이 길어져 stall penalty(지연 페널티)가 커진다. 그래서 제안된 방식이 Branch Prediction(분기 예측)이다.<br/>

&ensp;Branch Prediction<br/>
&ensp;분기가 일어날지 아닐지를 미리 예측하고 그 예측을 기반으로 파이프라인을 계속 진행하는 기법<br/>

&ensp;분기 결과를 기다리지 않고 일단 예측대로 실행한 후 나중에 실제 결과가 다를 경우 잘못된 명령어들을 flush한다.<br/>

&ensp;핵심 아이디어<br/>
* 분기 명령의 결과를 예측(Predict outcome of branch)
* 예측이 맞으면 → 정상 진행 (stall 없음)
* 예측이 틀리면 → 잘못된 명령어 flush (지연 발생)

# Static vs Dynamic Branch Prediction

| 구분    | Static Branch Prediction | Dynamic Branch Prediction |
| ----- | ------------------------ | ------------------------- |
| 예측 시점 | 프로그램 실행 전 (compile-time) | 프로그램 실행 중 (run-time)      |
| 예측 근거 | 코드 구조, 명령어 종류, 방향        | 실제 실행 결과(히스토리)            |
| 구현 방식 | 소프트웨어 기반                 | 하드웨어 기반                   |
| 장점    | 단순, 구현 쉬움                | 높은 정확도                    |
| 단점    | 정확도 낮음                   | 하드웨어 복잡도 증가               |

&ensp;Static Branch Prediction (정적 예측)<br/>
&ensp;정적 예측은 프로그램 실행 전에 분기 방향을 고정적으로 예측한다.<br/>
&ensp;대표적인 방법<br/>
1. Assume Branch Taken → 항상 분기가 발생한다고 가정 (예: 루프 문에서 자주 맞음)
2. Assume Branch Not Taken → 항상 분기가 발생하지 않는다고 가정 (예: if문에서 자주 맞음)
3. Prediction by Opcode → 명령어의 종류(opcode)에 따라 미리 판단
4. Prediction by Direction → 점프 방향이 "뒤로(backward)"면 반복문이라 taken, "앞으로(forward)"면 not taken으로 예측

&ensp;Dynamic Branch Prediction (동적 예측)<br/>
&ensp;동적 예측은 프로그램 실행 중에 과거 분기 결과를 기록하고 학습하여 예측한다.<br/>
&ensp;주요 방식<br/>
1. Branch Prediction Buffer (BHT, Branch History Table)
* 분기 명령어별로 과거의 결과(Taken / Not Taken)를 저장
* 1-bit predictor: 최근 한 번의 결과만 반영
* 2-bit predictor: “실수 한 번”으로 예측이 바뀌지 않음 (더 안정적)
2. Correlating Branch Predictor
* 최근 여러 분기들의 패턴을 고려하여 예측
3. Tournament Branch Predictor
* 여러 예측기를 동시에 사용하고, 더 잘 맞는 예측기를 선택
4. Branch Target Buffer (BTB)
* 분기 명령어의 목적지 주소를 캐싱해 빠르게 점프할 수 있도록 함

&ensp;Example: Assume Branch Not Taken<br/>
&ensp;분기가 일어나지 않는다고 가정하고 그냥 다음 명령어를 순차적으로 실행한다.<br/>
```text
if (branch not taken)
    → 정상 실행 계속
if (branch taken)
    → 잘못된 명령어를 flush
```

&ensp;잘못된 예측 시 처리<br/>
* 잘못된 명령어의 control signal을 0으로 변경
* IF, ID, EX 단계에 있는 3개의 명령어 flush (MEM 단계에서 결과 확정 시)
* 혹은, 1개의 명령어만 flush (ID 단계에서 결과 확정 시)

&ensp;Misprediction Penalty (잘못된 예측의 대가)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-6.png" width="500"></p>

&ensp;(1) 예측이 맞을 경우<br/>
&ensp;파이프라인은 중단 없이 연속적으로 실행된다.<br/>
```bash
add $4, $5, $6
beq $1, $2, 40
lw  $3, 300($0)
```

&ensp;→ beq가 not taken이라고 예측했고, 실제로도 not taken이라면 다음 명령어(lw)가 그대로 실행됨<br/>

&ensp;(2) 예측이 틀릴 경우<br/>
&ensp;예를 들어 실제로는 branch taken인데 예측은 not taken이라면 이미 가져온 명령어들이 잘못된 것임<br/>
&ensp;→ 따라서 flush 발생<br/>
&ensp;→ 파이프라인이 다시 채워질 때까지 bubble (공백 사이클) 이 생김<br/>
&ensp;즉 branch misprediction penalt는 예측 실패 시 발생하는 stall 사이클을 의미한다.<br/>

&ensp;정리요약<br/>

| 항목                    | 설명                        |
| --------------------- | ------------------------- |
| 문제                    | Control Hazard로 인한 stall  |
| 해결                    | Branch Prediction (분기 예측) |
| Static                | 실행 전 고정 예측 (단순, 정확도 낮음)   |
| Dynamic               | 실행 중 학습 기반 예측 (복잡하지만 정확)  |
| Assume Not Taken      | 기본적으로 순차 실행, 틀리면 flush    |
| Misprediction Penalty | 예측 실패 시 bubble 발생         |

* Branch Prediction은 stall을 완전히 제거하지는 않지만 예측 성공 시 stall 없이 실행 가능
* 예측 실패 시 flush 비용이 있지만 현대 CPU는 동족 예측기(Dynamic Predictor)로 예측률을 90% 이상까지 끌어올림

# Example: Pipelined Branch

&ensp;"Assume branch not taken"(분기 발생 X 가정) 방식을 기반으로 분기가 일어났을 때 (taken) 와 일어나지 않았을 때 (not taken)의 파이프라인 동작을 비교하는 예제이다.<br/>

```assembly
36  sub  $10, $4, $8
40  beq  $1, $3, 7       # PC-relative branch
                         # target = 40 + 4 + (7 * 4) = 72
44  and  $12, $2, $5
48  or   $13, $2, $6
52  add  $14, $4, $2
56  slt  $15, $6, $7
...
72  lw   $4, 50($7)
```

&ensp;해석<br/>
* `beq $1, $3, 7` : 만약 `$1 == $3` 이면 분기 발생 → 주소 72로 점프
* 아니라면 → 그냥 다음 명령어(44 and) 로 진행

&ensp;Case 1. Branch Not Taken<br/>
* 파이프라인은 분기가 발생하지 않다고 가정하고 다음 명령어들을 그래도 순차적으로 가져옴

```bash
Cycle 1: sub 실행
Cycle 2: beq 읽기
Cycle 3: and 읽기
Cycle 4: or 읽기
Cycle 5: add 읽기 ...
```

&ensp;실제로 $1 != $3이라면 그래도 AND → OR → ADD 순으로 문제없이 실행된다. 즉 flush 없음, stall 없음<br/>

&ensp;Case 2. Branch Taken<br/>
&ensp;$1 == $3인 상황을 보면 분기가 실제로 발생해 주소 72로 점프해야 한다. 그런데 파이프라인은 이미 분기가 없다고 가정하고 and, or 등을 미리 fetch 해버린 상태이다. 이 때문에 flush가 필요하다.<br/>

&ensp;Clock-by-Clock 동작 분석<br/>
&ensp;Clock 3 (분기 명령의 ID 단계)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-7.png" width="500"></p>

&ensp;상황 설명<br/>

&ensp;상황 설명<br/>
* `beq $1, $3, 7` 이 ID 단계에서 실행 중
* $1과 $3의 값을 비교하는 Comparator(=) 가 동작
* 결과가 "같음(equal)" → Branch Taken 신호 발생
* 동시에 Hazard Detection Unit이 이를 감지

&ensp;IF.Flush 동작<br/>
* 이미 IF 단계에서 읽은 명령어(and)는 잘못된 명령어임
* 따라서 IF.Flush 신호가 1로 설정되어 IF/ID 레지스터의 명령어가 NOP(0000 0000)로 대체됨

&ensp;and 명령이 버려짐(flush)<br/>

&ensp;Clock 4 (분기 명령의 EX 단계)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-8.png" width="500"></p>

&ensp;상황 설명<br/>
* Branch 명령(beq)이 EX 단계로 진입
* Branch Target Address 계산 (40 + 4 + 7×4 = 72)
* IF 단계에서는 새로운 명령어(`lw $4, 50($7)`)가 올바른 분기 주소(72)에서 다시 fetcg 시작

&ensp;Bubble 발생<br/>
* Flush로 인해 파이프라인이 일시적으로 비어 있음
* 따라서 1 사이클 동안 bubble (NOP) 이 존재

&ensp;전체 요약: Taken vs Not Taken 비교<br/>

| 구분       | Not Taken        | Taken                       |
| -------- | ---------------- | --------------------------- |
| 예측       | 분기 없음 가정         | 분기 없음 가정 (실제로는 발생)          |
| IF 단계 동작 | 다음 명령어 그대로 fetch | 잘못된 명령어 fetch 후 flush       |
| ID 단계    | 정상 진행            | 비교 결과 “equal” → IF.Flush 발생 |
| 결과       | Flush 없음         | Flush + 1-cycle bubble      |
| 성능 영향    | 없음               | 1 사이클 지연 (penalty)          |

&ensp;핵심 요약 포인트<br/>

| 개념                     | 설명                               |
| ---------------------- | -------------------------------- |
| **Branch Prediction**  | “분기 없음(Not Taken)” 가정            |
| **Branch Taken 시 문제점** | 잘못된 명령어들이 이미 파이프라인에 들어옴          |
| **해결 방법**              | IF.Flush 신호로 잘못된 명령어 제거          |
| **결과**                 | Branch Taken 시 1-cycle bubble 발생 |

&ensp;정리<br/>
* beq 명령이 ID 단계에서 조건 비교
* 같음(equal) → Branch Taken → IF.Flush 발생
* 잘못된 명령어(and, or)는 모두 NOP으로 대체
* 파이프라인은 다음 사이클부터 새로운 주소(72) 에서 실행 재개
* 이로 인해 1-cycle penalty 발생

# Dynamic Branch Prediction (동적 분기 예측)

&ensp;정적 예측(Static Prediction)은 단순하지만 정확도가 낮다. 그래서 CPU는 실행 중(Runtime)에 분기 패턴을 학습하며 더 똑똑하게 예측하는 방식을 사용한다. 이것이 바로 Dynamic Branch Prediction이다.<br/>

&ensp;핵심 아이디어<br/>
&ensp;이전에 어떤 분기에서 어떤 결과(Taken/Not Taken)가 나왔는지를 기억하고 이번에도 그 결과가 반복될 것이라 예측한다.<br/>

* 과거 분기 결과를 기록
* 다음에 같은 명령어가 등작했을 때 이전과 같은 결과를 예상

&ensp;작동 과정<br/>
1. 분기 명령어의 주소(Branch PC) 를 테이블에서 조회
2. 해당 주소에 저장된 비트(0 또는 1)를 확인
* 0 → 이전에 not taken
* 1 → 이전에 taken
3. 예측 결과에 따라 파이프라인이 다음 명령어를 fetch
4. 실제 결과가 다를 경우
* 파이프라인을 flush
* 예측 결과를 반전(flip) 시켜 저장

# Branch Prediction Buffer (BHT)

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-9.png" width="500"></p>

&ensp;BHT(Branch History Table)는 각 분기 명령어의 과거 실행 결과를 저장하는 테이블이다.<br/>

&ensp;특징<br/>
* 주소의 하위 비트(즉, branch 명령어의 일부 주소값)를 index로 사용
* 각 엔트리에는 1-bit or 2-bit 예측 비트가 존재
* 파이프라인 초기에 접근하여 예측 수행
* 실제 실행 결과가 나오면 업데이트

| Branch PC | Prediction Bit | 의미        |
| --------- | -------------- | --------- |
| 0x0040    | 0              | Not taken |
| 0x0044    | 1              | Taken     |
| 0x0048    | 1              | Taken     |

&ensp;작동 흐름<br/>
```text
1. Branch 명령이 들어오면 → 해당 PC로 BHT를 조회
2. 저장된 bit 값이 1이면 → taken 예측 / 0이면 not taken 예측
3. 예측 결과에 따라 instruction fetch 진행
4. 실제 실행 결과가 다를 경우 → flush + 예측 비트 반전
```

&ensp;BHT는 최근의 결과를 반복한다. 는 통계적 가정에 기반한다.<br/>

&ensp;Example: Loops and Prediction<br/>
&ensp;루프(loop)는 분기 예측의 대표적 활용 예시이다.<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-10.png" width="500"></p>

&ensp;상황<br/>
* 루프는 보통 반복 중엔 taken 마지막 한 번만 not taken
* 예를 들어 10번 중 9번 taken, 마지막 1번만 not taken이라면 예측 정확도는?

&ensp;결과<br/>
* 루프의 끝에서 한 번 틀림(not taken)
* 다음 루프 첫 진입 시 또 한 번 틀림(처음엔 taken으로 예측)
* 따라서 10번 중 2번은 틀림 → 예측 정확도 약 80%

# 2-bit Branch Prediction Scheme

&ensp;문제점 (1-bit predictor의 한계)<br/>
&ensp;1-bit predictor는 한 번의 오예측에도 바로 예측을 반전시켜버린다. → 반복문처럼 대부분이 taken인 경우 정확도가 낮아짐<br/>

&ensp;해결책: 2-bit Saturating Counter<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-11.png" width="500"></p>

| 상태 | 의미                 | 다음 상태 (조건) |
| -- | ------------------ | ---------- |
| 00 | Strongly Taken     | 틀릴 경우 → 01 |
| 01 | Weakly Taken       | 틀릴 경우 → 10 |
| 10 | Weakly Not Taken   | 틀릴 경우 → 11 |
| 11 | Strongly Not Taken | 틀릴 경우 → 10 |

&ensp;특징<br/>
* 두 번 연속 오예측할 때만 상태 반전
* 일시적 분기 변화에 휘둘리지 않음
* 루프 같은 패턴에서 훨씬 안정적인 예측

# Accuracy of Different Schemes

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-12.png" width="500"></p>

| Predictor Type                    | 설명        | 오예측률   |
| --------------------------------- | --------- | ------ |
| **4096 Entries 2-bit BHT (Red)**  | 보통의 캐시 크기 | 낮음     |
| **Unlimited 2-bit BHT (Green)**   | 이상적 상황    | 가장 정확  |
| **1024 Entries (2,2) BHT (Blue)** | 두 계층 예측기  | 효율적 타협 |

&ensp;평균 오예측률은 약 1~6%, 가장 복잡한 프로그램에서도 약 18%이하. 동적 분기 예측은 실제 CPU에서 매우 높은 예측 정확도(>90%) 를 달성한다.<br/>

| 항목                             | 설명                                      |
| ------------------------------ | --------------------------------------- |
| **BHT (Branch History Table)** | 분기 결과(Taken/Not Taken)를 저장하는 테이블        |
| **1-bit predictor**            | 단순하지만 불안정 (한 번 틀리면 바로 반전)               |
| **2-bit predictor**            | 안정적, 두 번 틀릴 때만 반전                       |
| **Loop 예시**                    | 루프 구조는 taken이 반복 → 2-bit predictor가 효과적 |
| **정확도**                        | 실험적으로 약 90% 이상의 예측률 달성                  |

Solution 3 – Delayed Branch (지연 분기)
=====

&ensp;Delayed Branch는 분기 명령어를 실행할 때 그 다음 순차 명령어를 무조건 한 번 더 실행한 뒤 분기가 이뤄지는 기법이다. 분기 명령어 뒤의 1개 명령어는 항상 실행된다. 분기가 발생하더라도 그 1 명령어 이후에 분기 주소로 점프한다.<br/>

&ensp;Branch Delay Slot<br/>
* 분기 명령어 뒤의 한 칸(slot)이 Branch Delay Slot이다.
* 이 공간은 항상 실행되는 명령어이므로 부작용 없는 안전한 명령어(Safe Instruction)로 채워야 한다.

&ensp;예시코드 (Delay Slot 없을 때 vs 있을 때):<br/>
```assembly
# 일반 분기
beq $1, $3, target
add $4, $5, $6   # 실행되지 않을 수도 있음

# Delayed branch 적용
beq $1, $3, target
add $4, $5, $6   # delay slot → 무조건 실행
```

&ensp;Delayed Branch vs Dynamic Branch Prediction<br/>

| 구분         | Delayed Branch          | Dynamic Branch Prediction  |
| ---------- | ----------------------- | -------------------------- |
| **방식**     | 분기 뒤 1 명령어를 항상 실행       | 분기 결과를 예측 후 실행             |
| **장점**     | 단순, 예측 하드웨어 필요 없음       | 높은 정확도, 지속적 학습             |
| **단점**     | 컴파일러가 delay slot 채워야 함  | 하드웨어 복잡 및 비용 증가            |
| **적합한 환경** | 단일 파이프라인 (5-stage MIPS) | superscalar, deep pipeline |
| **현황**     | 현재는 거의 사용 안 함           | 현대 CPU의 주류 기법              |

&ensp;지연 분기는 한때 간단하고 효과적인 해법이었지만 파이프라인이 길어지고 동시에 여러 명령을 발행하는 CPU에서는 단 1칸의 delay slot로는 부족하기 때문에 지금은 거의 사라졌다.<br/>

Branch Target Buffer (BTB)
=====

&ensp;Delayed Branch가 소프트웨어적 해결이라면 BTB는 하드웨어 레벨에서 분기 속도를 높이는 방법이다.<br/>

&ensp;개념<br/>
&ensp;BTB = Branch Target Buffer<br/>
* 분기 예측기 + 분기 목적지 주소를 함께 저장하는 테이블
* 분기 명령어의 PC로 index → 이전 분기 결과와 목적지 주소 조회
* 파이프라인 초기단계(IF)에서 이미 목적지 주소를 가져올 수 있음

&ensp;동작 흐름<br/>
1. Instruction Fetch 시 PC를 BTB에서 조회
2. 이전 기록이 있다면 → 예측된 PC로 즉시 점프
3. 기록이 없다면 → 일반 순차 명령 fetch
4. 결과 틀리면 → flush 후 BTB 내용 갱신

&ensp;Example 1 – Assume Branch Not Taken<br/>
&ensp;조건<br/>
* 분기 예측: Not Taken
* 분기 명령이 EX 단계에서 결정
* 파이프라인: MIPS 5단계 → IF → ID → EX → MEM → WB

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-13.png" width="500"></p>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-14.png" width="500"></p>

&ensp;분기 결과가 EX 단계에서 늦게 결정되므로 잘못 가져온 명령어들은 flush되어 여러 bubble이 발생<br/>

&ensp;기본 동작<br/>
&ensp;파이프라인은 항상 다음 명령어를 미리 가져오면서(fetch) 실행된다.<br/>
```text
CC1: sub
CC2: and
CC3: lw
CC4: add
CC5: beq
```

&ensp;이렇게 차례로 들어가는데 40번 명령어인 `beq` 가 분기 발생 명령이다. 이때 CPU는 분기 결과를 아직 모른 상태에서 다음 명령어(sw, slt, and,...)를 이미 가져와 실행하고 있다.<br/>

&ensp;문제: beq 명령의 분기 조건은 ID 단계에서 판단됨<br/>
* beq 명령어는 ID 단계에서 두 레지스터 값을 비교해 taken / not taken 을 판단한다.
* 이 시점에 CPU는 이미 다음 명령어(sw)를 IF 단계에서 가져옴. → 그런데 “taken”이니까 그 sw는 잘못된 명령어
* 따라서 “EX 단계”부터는 실행을 멈춰야 함. → EX 칸에 bubble 삽입.

```yaml
CC5 : beq - IF
CC6 : beq - ID (여기서 branch taken 판정!) → Flush 발생
CC6 : EX 칸부터 bubble 삽입 시작
CC7 : bubble 유지, beq는 EX 이동
CC8 : bubble 유지, 다음 명령어 재시작 준비
CC9 : branch target에서 정상 재시작
```

&ensp;그 동안 가져온 명령어들(CC6~CC8에 fetch된 것들)은 전부 잘못된 거다.<br/>

&ensp;그래서 생기는 일: Flush + Bubble<br/>
&ensp;CPU는 이 잘못된 명령어들은 취소(flush)해야 한다. 하지만 이미 파이프라인 단계에 들어와 있기 때문에 즉시 삭제할 수 없고 빈 칸(bubble)으로 남게 된다.<br/>

&ensp;단계별로 보면<br/>

| 단계      | 이름                                  | beq에서 하는 일                               | 구체적 내용                                                                                                                                                                                                       |
| ------- | ----------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **IF**  | Instruction Fetch                   | 명령어를 메모리에서 가져옴                           | PC가 가리키는 주소의 명령어(`beq`)를 Instruction Memory에서 읽음                                                                                                                                                             |
| **ID**  | Instruction Decode / Branch Check  | 명령 해독 + 레지스터 읽기 + **분기 조건 판단**           | - 명령어의 opcode를 해석해 ‘branch 명령’임을 인식<br>- `$1`, `$3` 두 피연산자를 Register File에서 읽음<br>- **Comparator(=== 비교기)** 가 ID 단계에 있어서 `$1 == $3`인지 바로 비교 → branch taken 여부 결정<br>- 동시에 branch target 주소 계산(PC + offset×4) |
| **EX**  | Execute / ALU 계산                    | 분기 명령의 경우 **추가 실행은 없음** (조건 이미 ID에서 판정됨) | - 일반 명령어(add, sub 등)는 연산 수행하는 단계지만<br>- **beq는 ID에서 이미 비교 완료했기 때문에** EX 단계에서는 더 이상 할 일이 거의 없음<br>- 다만 “PC 갱신 준비” 정도만 수행                                                                                      |
| **MEM** | Memory Access                       | 메모리 접근 없음                                | beq는 메모리 접근이 없기 때문에, MEM 단계에서는 대기 혹은 pass-through                                                                                                                                                            |
| **WB**  | Write Back                          | 결과 저장 없음                                 | beq는 연산 결과가 없으므로 레지스터에 쓸 것도 없음                                                                                                                                                                               |

* IF 단계 → 단순히 "명령어를 읽어오는" 단계
* ID 단계 → 교수님 버전에서는 여기서 분기 조건 비교 + 분기 목표 주소 계산, $1 == $3 이면 branch taken 즉시 판단 가능. 다음 사이클부터 IF.Flush 신호 발생 (즉, bubble 생성 시작)
* EX 단계 → 이미 분기 여부가 결정되었기 때문에 beq 명령은 EX에서 실질적으로 아무 일도 안 함

&ensp;Bubble은 왜 필요한가?<br/>
&ensp;파이프라인은 항상 “각 단계마다 뭔가” 있어야 시계(tick)가 계속 돈다. 하지만 flush된 명령어 자리는 아무 일도 하지 않으므로 "아무것도 안 함" = bubble(공기) 로 표현한다.<br/>
&ensp;그래서 실제 실행에서는<br/>
* 이 사이클 동안 ALU나 MEM 단계나 놀고 있음(= 성능 손실)
* 하지만 다음 올바른 명령어(`branch target`)가 준비될 때까지는 어쩔 수 없음

| 항목                  | 설명                                                |
| ------------------- | ------------------------------------------------- |
| **bubble의 원인**      | ID 단계에서 분기 결과를 바로 판단(taken) → 이미 가져온 명령어 flush 필요 |
| **bubble이 생기는 시점**  | `beq`가 ID에 들어온 **CC6**의 EX 단계부터                   |
| **bubble의 역할**      | 잘못 가져온 명령어 자리 확보 (파이프라인 동기화 유지)                   |
| **bubble이 사라지는 시점** | 분기 타겟 명령어 fetch가 완료될 때                            |

| 원인                         | 결과                                 |
| -------------------------- | ---------------------------------- |
| 분기 명령의 결과를 EX 단계에서만 알 수 있음 | 그동안 다음 명령들을 미리 가져와버림               |
| 실제 분기 발생 시                 | 잘못된 명령어를 flush                     |
| flush된 구간                  | bubble로 표시 (실행 안 함)                |
| 효과                         | 파이프라인이 몇 사이클 동안 멈춰 있음 (penalty 발생) |

&ensp;분기 동작 해석<br/>
&ensp;beq 명령 분석<br/>
* 명령어: `beq $3, $3, Label`
* 조건: 항상 참 (`$3 == $3`)
* 결과: 분기 발생 (Taken)
* 분기 타겟: Label 주소 (즉, and $4, $5, $1 명령어 위치)

&ensp;beq가 실행되면 프로그램 흐름이 다시 "and" 라벨로 점프한다.<br/>
&ensp;1. CC8 이후의 명령어들은 분기 목표 주소(Label) 에서 가져온 새 명령어들이다.<br/>
* beq 이후 원래 프로그램 순서상에는 sw, slt, or가 있었지만 분기(taken)가 발생했기 때문에 이들은 무효화(Flush) 되었다.
* 대신 PC가 Label (and) 로 점프한다.
* 그래서 CC8부터 다시 and → lw → add 순서로 fetch가 시작된다.

&ensp;2. CC9에서 beq 뒤의 (bubble) (bubble)는 Flush 효과이다.<br/>
* beq가 MEM 단계로 이동하는 동안 분기 타겟에서 새로 가져온 명령들이 아직 IF, ID에 있음.
* EX~MEM 라인은 "빈 칸"이기 때문에 bubble이 보인다. (기존 파이프라인이 비워지고 새로운 흐름이 들어오는 중)

&ensp;3. CC10의 lw는 분기 이후 Label에서 이어진 정상 명령어이다.<br/>
* Label: 바로 뒤에 있는 lw $6, 100($7) 가 다시 실행되고 있는 것이다.
* CC10의 lw는 "beq 다음 명령"이 아니라 "Label로 점프한 뒤의 첫 번째 lw"이다.

&ensp;Example 2 – Delayed Branch 적용<br/>
&ensp;분기 명령(beq 등)을 만나면 분기 바로 다음 명령(Delay Slot)은 분기가 일어나더라도 무조건 한 번은 실행되는 구조이다.<br/>

* 분기 명령 뒤 1 칸(delay slot)에 다른 명령어 삽입
* 분기가 ID 단계에서 결정
* 분기 명령어가 실행되어도 바로 다음 한 줄(sw)은 이미 pipeline에 들어와 있으니까 그냥 실행
* 그 이후에 branch target으로 점프

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-15.png" width="500"></p>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-5-16.png" width="500"></p>

&ensp;bubble이 들어가는 이유<br/>
&ensp;1. CC6<br/>
* `beq` 가 ID 단계에서 조건을 비교함 (branch taken 판단)
* 하지만 pipeline에는 이미 그 다음 명령어 `sw` 가 IF 단계에 들어와 있음 → delay slot으로 인정되어 실행 허용
* 다만 beq 이후의 명령들이 잘못된 fetch를 막기 위해 EX 단계부터 bubble을 하나 삽입 (이건 파이프라인이 한 사이클 멈추는 효과)

&ensp;2. CC7<br/>
* `sw` 가 delay slot 명령으로 정상 실행 중
* `beq` 는 여전히 pipeline 안에서 흐르지만 다음 명령(fetch)은 이미 Label로 점프 준비
* flush가 sw 이후부터만 적용됨
* 그래서 이 시점까지 bubble이 유지됨 (EX 칸)

&ensp;3. CC8 이후<br/>
* `sw` 실행 완료 후 branch target(Label)의 명령(`and`, `lw`, `add`)이 다시 fetch됨
* bubble 사리자고 파이프라인 정상 복귀

&ensp;정리<br/>

| 구분                | 이유                                       | 결과           |
| ----------------- | ---------------------------------------- | ------------ |
| **CC6 bubble 발생** | ID 단계에서 branch taken 판단 → pipeline 잠깐 멈춤 | EX 칸에 bubble |
| **CC7 유지**        | delay slot(`sw`) 실행 중                    | bubble 유지    |
| **CC8 이후**        | branch target(`and`, `lw` …)으로 점프        | bubble 제거    |

&ensp;Delayed Branch에서는 `beq`가 taken 되어도 바로 다음 명령(`sw`)은 delay slot으로 실행되고 그 동안 pipeline flush가 잠시 보류된다. flush가 완료되면 다음 사이클부터 branch target(Label)로 점프하면서 bubble이 사라진다.<br/>

&ensp;비교<br/>

| 항목               | 일반 Branch (No Delay Slot) | Delayed Branch     |
| ---------------- | ------------------------- | ------------------ |
| **분기 판단 시점**     | ID 단계                     | ID 단계              |
| **다음 명령어 실행 여부** | Flush로 무효화됨               | Delay slot으로 실행됨   |
| **bubble 수**     | 2~3개                      | 1개 이하              |
| **성능**           | 느림 (더 많은 stall)           | 빠름 (delay slot 덕분) |

&ensp;bubble은 여전히 생기지만 그게 분기 조건 판단으로 pipeline이 살짝 멈춘 결과이고 delay slot(sw)덕분에 branch penalty가 최소화된다.<br/>
