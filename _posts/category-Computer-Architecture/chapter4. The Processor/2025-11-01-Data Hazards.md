---
title: "chapter 4-4. Data Hazards"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-11-01
last_modified_at: 2025-11-01
---

Data Hazards
====

&ensp;Data Dependence란?<br/>
&ensp;Data Dependence(데이터 의존성)은 어떤 명령어가 이전 명령어의 결과값을 사용해야 하는 관계를 말한다. 앞선 명령어가 결과를 만들어내기 전에는 그 값을 필요로 하는 다음 명령어가 완전하게 실행될 수 없다.<br/>

```bash
sub $2, $1, $3      # $2 = $1 - $3
and $12, $2, $5     # $2의 결과를 바로 사용
or  $13, $6, $2     # $2의 결과를 또 사용
add $14, $2, $2     # $2를 두 번 입력으로 사용
sw  $15, 100($2)    # $2를 주소 계산에 사용
```

&ensp;$2 레지스터가 핵심<br/>
* 첫 번째 명령어 `sub`가 `$2`에 결과를 저장한다.
* 그리고 그 뒤의 모든 명령어들이 $2의 값을 사용하고 있다.

&ensp;즉 모든 명령어가 sub 명령어에 의존하고 있는 구조이다.<br/>

&ensp;Data Dependence Graph (데이터 의존 그래프)<br/>
&ensp;오른쪽 그림이 바로 그 관계를 시각적으로 표현한 그래프이다.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-1.png" width="500"></p>


&ensp;노드(Node): 명령어 (sub, and, or, add, sw)<br/>
&ensp;화살표(Edge): 데이터 의존 관계<br/>

&ensp;문제가 되는 이유<br>
&ensp;파이프라인에서는 여러 명령어가 동시에 실행된다.<br/>
* sub이 ALU에서 계산 중인데 바로 다음 명령어 and는 $2의 값을 읽으려고 할 수 있다.

&ensp;그런데 $2는 아직 계산 결과가 안 나왔으니 CPU는 잘못된 값을 읽을 위험이 있다. 이게 바로 Data Hazard(데이터 위험)이다.<br/>

Pipelined Dependence
-----

&ensp;파이프라인(Pipeline)이란?<br/>
&ensp;파이프라인은 CPU가 여러 명령어를 동시에 처리하는 기술이다. 예를 들어 한 명령어가 계산(Ex)단계에 있을 때 다음 명령어는 이미 명령어를 해석(ID) 중일 수 있다.<br/>
&ensp;이렇게 하면 한 번에 하나씩 처리하는 것보다 훨씬 빠르게 프로그램을 실행할 수 있다.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-2.png" width="500"></p>

&ensp;파이프라인 5단계<br/>

| 단계  | 이름                 | 역할                        |
| --- | ------------------ | ------------------------- |
| IF  | Instruction Fetch  | 명령어를 메모리에서 가져옴            |
| ID  | Instruction Decode | 명령어를 해석하고 레지스터를 읽음        |
| EX  | Execute            | 연산 수행 (ALU 계산 등)          |
| MEM | Memory             | 메모리 접근 (load/store 명령어 등) |
| WB  | Write Back         | 연산 결과를 레지스터에 기록           |

&ensp;Clock Cycle별 실행 흐름<br/>

&ensp;Clock Cycle 1<br/>

| 단계 | 명령어              |
| -- | ---------------- |
| IF | `sub $2, $1, $3` |

&ensp;→ 첫 번째 명령어만 메모리에서 가져오고 있는 상태이다.<br/>

&ensp;Clock Cycle 2<br/>

| 단계 | 명령어               |
| -- | ----------------- |
| IF | `and $12, $2, $5` |
| ID | `sub $2, $1, $3`  |

&ensp;→ `and` 명령어는 `$2`를 읽으려 하지만 아직 sub 명령어가 $2 값을 계산하기 전이다. 즉 데이터 의존성이 발생한다.<br/>

&ensp;Clock Cycle 3<br/>

| 단계 | 명령어               |
| -- | ----------------- |
| IF | `or $13, $6, $2`  |
| ID | `and $12, $2, $5` |
| EX | `sub $2, $1, $3`  |

&ensp;→ `sub`은 이제 계산(EX) 단계에서 $2 값을 만들고 있지만 아직 결과가 레지스터에 기록되지 않았기 때문에 뒤 명령어들은 그 값을 쓸 수 없다.<br/>

&ensp;Clock Cycle 4 (문제 발생!)<br/>

| 단계  | 명령어               |
| --- | ----------------- |
| IF  | `add $14, $2, $2` |
| ID  | `or $13, $6, $2`  |
| EX  | `and $12, $2, $5` |
| MEM | `sub $2, $1, $3`  |

&ensp;→ `and`명령어의 EX 단계에서 `$2`를 사용해야 하지만 아직 `sub`의 결과가 나오지 않는다.<br/>
&ensp;이 시점이 바로 파이프라인 해저드(Pipeline Harzard)이다.<br/>

# Data Hazard

&ensp;Data Harzard는 파이프라인에서 명령어 간의 데이터 의존성(Data Dependence)때문에 발생하는 문제이다. 즉 뒤의 명령어가 앞의 명령어 결과를 필요로 하는데 그 결과가 아직 계산되지 않은 상태일 때 생기는 충돌이다.<br/>

&ensp;이럴 때 파이프라인을 일시적으로 멈추거나(Stall) 데이터를 바로 전달(Forwarding)하는 방법으로 해결한다.<br/>

Data Harzard 해결 방안
=====

Stalling
----

&ensp;파이프라인을 멈춰서(Data Stall) 데이터가 준비될 때까지 기다리게 하는 방법이다. 이 때 파이프라인 내부에 버블(bubble)이라는 빈 슬롯을 삽입한다. (버블은 실제로 아무 일도 하지 않는 빈 사이클이다. 마치 공장 라인에서 잠깐 작업을 멈추는 것과 같다.)<br/>

&ensp;명령어 순서<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-2.png" width="500"></p>

```bash
sub $2, $1, $3
and $12, $2, $5
or  $13, $6, $2
add $14, $2, $2
sw  $15, 100($2)
```

&ensp;여기서도 `$s2` 가 계속 반복적으로 사용된다. `sub`가 `$2` 에 결과를 저장하기 전에 `and` `$2` 를 읽으려 하니까 Data Harzardd 발생<br/>

&ensp;Clock Cycle별 동작 (Stalling 과정)<br/>

&ensp;Clock Cycle 3<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-4.png" width="500"></p>

&ensp;sub이 $2를 계산 중 (EX 단계)<br/>
&ensp;and는 $2 값을 필요로 하지만, 아직 결과가 안 나옴<br/>
&ensp;따라서 hazard 감지<br/>

&ensp;Clock Cycle 4<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-5.png" width="500"></p>

&ensp;하드웨어가 의존성을 감지해서 파이프라인을 멈춤<br/>
&ensp;Ex 단계에 Bubble 삽입<br/>
&ensp;이걸 Pipeline Interlock 이라고 한다.<br/>

&ensp;Clock Cycle 5<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-6.png" width="500"></p>

&ensp;sub이 이제 결과를 레지스터에 저장(WB 단계)<br/>
&ensp;이제 $2 값이 준비됨<br/>
&ensp;다음 사이클부터 and 명령어가 실행 가능<br/>

&ensp;Clock Cycle 6<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-7.png" width="500"></p>

&ensp;and가 드디어 실행 가능(EX 단계 진입)<br/>
&ensp;버블은 사라지고 정상적으로 명령어가 이어짐<br/>

&ensp;Solution 1 – Stalling 요약표<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-3.png" width="500"></p>

Insert nop Instructions (NOP 명령어 삽입)
----

&ensp;개념<br/>
&ensp;`nop` 은 No operation, 아무 일도 하지 않는 명령어이다. 파이프라인이 데이터를 기다리는 동안 CPU가 멈추지 않게 하기 위해 의도적으로 빈 명령어를 삽입하는 방법이다.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-8.png" width="500"></p>

&ensp;동작 방식<br/>
1. `sub`이 $2를 계산하고 결과를 레지스터에 저장하기까지 시간이 걸림
2. `and`는 $2가 필요하지만 결과가 아직 준비되지 않음
3. 따라서 그 사이에 `nop` 2개를 삽입해 시간을 벌어줌
4. 그동안 CPU는 그냥 아무 일도 안 하는 사이클을 보냄

&ensp;단점<br/>
* 성능 저하 → 불필요한 사이클이 생겨 파이프라인이 효율적으로 동작하지 못함
* 유지보수 어려움 → 코드 안에 nop이 많으면 읽기 힘들고 비효율적임

Code Reordering (코드 재배치)
-----

&ensp;이 방법은 컴파일러나 프로그래머가 직접 명령어 순서를 바꿔서 의존성을 피하는 방법이다. 결과를 기다리는 동안 독립적인 명령어를 먼저 실행하는 것이다.<br/>

&ensp;예시 비교<br/>
&ensp;Before(문제 있는 코드)<br/>
```assembly
sub $2, $1, $3
and $12, $2, $5   # $2 결과 필요
or  $13, $6, $7
add $14, $4, $8
sw  $15, 100($9)
```

&ensp;After(Reordered Code)<br/>
```assembly
sub $2, $1, $3
or  $13, $6, $7   # $2 사용 안 함
add $14, $4, $8   # $2 사용 안 함
and $12, $2, $5   # 이제 $2 결과 준비됨
sw  $15, 100($9)
```

&ensp;동작 방식<br/>
* `$2`가 준비될 때까지 $2를 사용하지 않는 다른 명령어(or, add)를 먼저 실행
* 이렇게 하면 Stall이나 NOP 없이 파이프라인이 계속 움직임

&ensp;장점<br/>
* CPU가 멈추지 않음(no stall)
* 속도 향상, 효율적인 명령어 실행

&ensp;단점<br/>
* 모든 코드에서 항상 가능하지는 않음 → 의존성이 복잡하면 재배치가 어려움
* 컴파일러가 자동 최적화를 해줘야 하는 경우가 많음

Forwarding(aka Bypassing)
-----

&ensp;결과를 레지스터에 쓰기 전에 바로 명령어에 전달한다. 결과값이 ALU에서 계산된 즉시 그 값을 기다리는 명령어(EX 단계)에 바로 넘겨준다.<br/>

&ensp;결과를 레지스터에 저장될 때까지 기다리지 않고 ALU 내부 버퍼에서 바로 꺼내 쓰는 방법이다.

```assembly
add $s0, $t0, $t1   # $s0 계산 중
sub $t2, $s0, $t3   # $s0 필요
```
&ensp;보통이라면 `add` 가 끝나고 `$s0` 이 WB(Write Back) 단계에 들어가야 `sub` 가 `$s0` 을 쓸 수 있다.<br/>
&ensp;하지만 Forwarding이 있다면?<br/>
&ensp;`add`의 EX 단계에서 계산된 결과를 바로 `sub`의 EX 단계 입력으로 전달할 수 있다.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-9.png" width="500"></p>

* 위쪽 `add` 명령어가 EX 단계에서 $s0 결과 생성
* 아래쪽 `sub` 명령어는 아직 ID 단계
* 하드웨어가 결과선을 연결해 `$s0` 값을 바로 전달 (파란 화살표)

&ensp;장점<br/>
* 파이프라인 중단 없이 실행 가능
* 성능 향상: NOP나 Bubble이 필요 없음
* 하드웨어 자동 처리

&ensp;단점<br/>
* 회로 복잡도 증가 (추가 연결선 필요)
* 하드웨어 설계가 더 어려워짐

&ensp;세 가지 해결법 비교<br/>

| 방법                  | 원리                    | 장점      | 단점          |
| ------------------- | --------------------- | ------- | ----------- |
| **Stalling (버블)**   | 결과 나올 때까지 멈춤          | 구현 간단   | 느림          |
| **NOP 삽입**          | 명시적으로 기다리는 명령어 삽입     | 쉬운 구현   | 비효율적, 코드 복잡 |
| **Code Reordering** | 의존 없는 명령어 순서 변경       | 빠름, 효율적 | 항상 적용 불가    |
| **Forwarding**      | ALU 결과를 즉시 다음 명령어에 전달 | 매우 빠름   | 하드웨어 복잡     |

&ensp;파이프라인 이름 짚기<br/>
* ID/EX : 지금 EX로 들어가려는(=막 레지스터 값을 읽은) 소비자 명령어의 입력 보관 레지스터
    - `ID/EX.RegisterRs`, `ID/EX.RegisterRt` : 이 명령어가 읽을 소스 레지스터 번호(Rs, Rt)
* EX/MEM : 방금 EX에서 결과를 만든 생산자가 한 단계 앞에 있을 때의 보관 레지스터
    - `EX/MEM.RegisterRd` : 이 생산자가 쓸 목적지 레지스터 번호(Rd)
* MEM/WB : 생산자가 두 단계 앞에 있을 때(메모리 끝나고 WB 직전)의 보관 레지스터
    - `MEM/WB.RegisterRd` : 이 생산자가 쓸 목적지 레지스터 번호(Rd)

&ensp;요약: 지금 EX로 갈 소비자(ID/EX) 가 읽을 레지스터(Rs/Rt)와, 앞서 가는 생산자(EX/MEM, MEM/WB) 가 쓸 레지스터(Rd)를 번호로 비교해 “의존성이 있나?”를 판단한다.<br/>

&ensp;기본 해저드 판정식(포워딩 필요 후보)<br/>
&ensp;바로 앞 또는 두 칸 앞의 생산자가 내게 필요한 값을 쓰는지 보는 비교식이다.<br/>
* 1a : `EX/MEM.RegisterRd == ID/EX.RegisterRs` → 한 단계 앞의 결과를 ALU 입력 A로 포워딩
* 1b : `EX/MEM.RegisterRd == ID/EX.RegisterRt` → 한 단계 앞의 결과를 ALU 입력 B로 포워딩
* 2a : `MEM/WB.RegisterRd == ID/EX.RegisterRs` → 두 단계 앞의 결과를 ALU 입력 A로 포워딩
* 2b : `MEM/WB.RegisterRd == ID/EX.RegisterRt` → 두 단계 앞의 결과를 ALU 입력 B로 포워딩

&ensp;앞에 있는 누군가가 곧 쓰려는 레지스터(Rd)가 내가 지금 읽어야 할 레지스터(Rs/Rt)와 같으면 그쪽에서 바로 값(결과)을 빼 와서 ALU에 꽂아준다.(포워딩)<br/>

&ensp;예제에 적용해 분류하기<br/>
```assemble
sub $2, $1, $3     # $2를 만듦
and $12, $2, $5    # 첫 번째 피연산자 $2 사용
or  $13, $6, $2    # 두 번째 피연산자 $2 사용
add $14, $2, $2    # 둘 다 $2 사용
sw  $15, 100($2)   # 주소 계산에 $2 사용(Rs)
```

&ensp;(1) `sub` → `and`<br/>
* 타이밍: `and`가 ID/EX에 있을 때 `sub`는 EX/MEM에 있음(한 단계 앞)
* 비교: `EX/MEM.Rd(= $2)` vs `ID/EX.Rs(= $2)` → 같음
* 분류: Type 1a (한 단계 앞 생산자의 결과를 Rs로 포워딩)

&ensp;(2) `sub` → `or`<br/>
* 타이밍: `or`가 ID/EX에 있을 때 `sub`는 MEM/WB에 있음(두 단계 앞)
* 비교: `MEM/WB.Rd(= $2)` vs `ID/EX.Rt(= $2)` → 같음
* 분류: Type 2b (두 단계 앞 생산자의 결과를 Rt로 포워딩)

&ensp;(3) `sub` → `add, sub` → `sw` <br/>
* 이때쯤이면 `sub`는 이미 WB까지 끝나 레지스터 파일에 결과가 정식으로 기록됨.
* 따라서 `add`/`sw`가 ID/EX에 있을 때 앞 레지스터(EX/MEM, MEM/WB)에 `sub`가 존재하지 않음 → 위 네 식에 안 걸림.
* 결과: 데이터 해저드 없음(단순히 레지스터 파일에서 읽으면 충분)

&ensp;의존성은 있지만 타이밍상 이미 값이 레지스터에 써져 있으면 포워딩/스톨이 필요 없는 의존성이라 해저드로 취급하지 않는다.<br/>

&ensp;불필요한 포워딩 피하기<br/>
&ensp;포워딩 유닛이 괜히 선을 켜지 않도록 두 가지 추가 체크를 한다.<br/>
1. 그 생산자 명령어가 실제로 레지스터를 쓰는가?
* 제어 신호 `RegWrite == 1` 인 경우만 포워딩 후보로 인정
* (예: `sw`, `beq` 등은 레지스터에 안 씁니다)
2. 목적지가 `$zero`(0번 레지스터)가 아닌가?
* `$zero`는 언제나 0, “쓰기 무시” 레지스터이므로
* `RegisterRd != 0` 인 경우만 후보

&ensp;확장된 해저드 조건<br/>
&ensp;위 두 가지 필터를 반영해 각 판정식 앞에 조건이 붙는다.<br/>
* 1a. `EX/MEM.RegWrite` and `(EX/MEM.RegisterRd != 0)` and `(EX/MEM.RegisterRd == ID/EX.RegisterRs)`
* 1b. `EX/MEM.RegWrite` and `(EX/MEM.RegisterRd != 0)` and `(EX/MEM.RegisterRd == ID/EX.RegisterRt)`
* 2a. `MEM/WB.RegWrite` and `(MEM/WB.RegisterRd != 0)` and `(MEM/WB.RegisterRd == ID/EX.RegisterRs)`
* 2b
`MEM/WB.RegWrite` and `(MEM/WB.RegisterRd != 0)` and `(MEM/WB.RegisterRd == ID/EX.RegisterRt)`

&ensp;의미: 앞에 있는 생성자가 정말로 레지스터를 쓰는 명령이고 그 목적지가 $zero가 아니며 그 목적지 번호가 내가 지금 읽을 Rs/Rt 랑 같다면 → 포워딩 신호를 켜라<br/>

&ensp;한 눈 정리<br/>
* 해저드 검출은 “소비자(ID/EX)의 Rs/Rt ↔ 앞선 생산자(EX/MEM, MEM/WB)의 Rd 번호 비교”다.
* 1a/1b: 한 단계 앞(EX/MEM)에서 가져올지 결정, 2a/2b: 두 단계 앞(MEM/WB)에서 가져올지 결정
* RegWrite=1, Rd≠$zero(0) 조건을 함께 걸어 불필요한 포워딩을 차단한다.
* 예제 분류: sub→and = 1a, sub→or = 2b, sub→add/sw = 해저드 없음(이미 WB 완료 후라 단순 읽기 가능)

```assembly
sub $2, $1, $3
and $12, $2, $5
or  $13, $6, $2
add $14, $2, $2
sw  $15, 100($2)
```

&ensp;여기서 `$2` 는 첫 번째 `sub` 가 만든 결과를 뒤 명령어들이 계속 사용한다. 보통 `sub`의 결과는 WEB(Write Back) 단계에서야 레지스터에 저장되지만 `and` 는 이미 그 전에 EX 단계에서 `$2` 값을 필요로 한다.<br/> 
&ensp;→ 그래서 Forwarding이 없으면 Stall이 발생하지만 Forwarding을 사용하면 Stall 없이 연속 실행이 가능하다.<br/>

&ensp;Forwarding 타이밍 이해<br/>
&ensp;이 그림은 파이프라인 단계별로 결과가 어떻게 전달되는지(화살표) 보여준다.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-10.png" width="500"></p>

| Clock Cycle | 설명                                                                                 |
| ----------- | ---------------------------------------------------------------------------------- |
| **CC3**     | `sub`이 EX 단계에서 `$2 = 10 - 20 = -10` 계산                                             |
| **CC4**     | `and` 명령어가 `$2`를 필요로 하는데, 아직 레지스터에 저장되지 않음 → **Forwarding**으로 `sub`의 ALU 결과를 직접 전달 |
| **CC5**     | `or` 명령어가 `$2`를 필요로 하는데, 이때는 MEM/WB 단계에 있는 `sub` 결과를 **다시 전달**                     |
| **CC6 이후**  | 이후 명령어들도 `$2` 값을 필요할 때마다 **적절한 단계(EX/MEM 또는 MEM/WB)** 에서 바로 가져옴                    |

&ensp;`sub` 결과는 레지스터를 거치지 않고 ALU → ALU 또는 ALU → MEM → ALU 경로로 직접 전달된다.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-11.png" width="500"></p>

&ensp;왼쪽 그림 - NO Forwarding<br/>
&ensp;Forwarding이 없는 기본 파이프라인 구조이다.<br/>
* ID/EX → EX/MEM → MEM/WB 순서로 순차 이동
* 결과는 레지스터 파일에 저장된 후에야 다음 명령어가 읽을 수 있음
* 따라서 Data Hazard 발생 → Stall(버블) 필요

&ensp;오른쪽 그림 — With Forwarding<br/>
&ensp;Forwarding Unit이 추가된 구조이다. 하드웨어가 자동으로 데이터 흐름을 감지하고 ALU 입력으로 바로 보내준다.<br/>

&ensp;주요 구성<br/>

| 구성 요소                 | 역할                                                                   |
| --------------------- | -------------------------------------------------------------------- |
| **Forwarding Unit**   | 현재 EX 단계 명령어(ID/EX)가 필요한 레지스터와, 앞선 명령어(EX/MEM, MEM/WB)의 목적지 레지스터를 비교 |
| **MUX A / MUX B**     | ALU의 두 입력값(A, B)이 어디서 오는지를 선택                                        |
| **EX/MEM.RegisterRd** | 한 단계 앞 명령어의 결과                                                       |
| **MEM/WB.RegisterRd** | 두 단계 앞 명령어의 결과                                                       |

&ensp;데이터 흐름 요약<br/>
* ForwardA, ForwardB 신호는 MUX 제어선입니다. ALU의 두 입력이 각각 레지스터에서 올지, EX/MEM, MEM/WB에서 올지를 정합니다.

&ensp;Forwarding Unit은 “어디서 값을 가져올까?”를 판단하는 뇌 역할, MUX는 실제로 그 경로를 선택하는 손 역할을 합니다.<br/>

Multiplexor Control Signals
====

&ensp;Forwarding이 필요한 상황별로 MUX 제어 신호 값(00, 10, 01) 이 어떻게 되는지를 정리한 표이다.<br/>

&ensp;표 해석<br/>

| Hazard        | MUX 제어 (ForwardA / ForwardB) | Source | 설명                                        |
| :------------ | :--------------------------- | :----- | :---------------------------------------- |
| **No Hazard** | 00                           | ID/EX  | 그냥 레지스터 파일에서 읽음 (Forwarding 필요 없음)        |
| **1a**        | 10                           | EX/MEM | 한 단계 앞(ALU 결과)을 바로 전달 → 첫 번째 ALU 피연산자     |
| **2a**        | 01                           | MEM/WB | 두 단계 앞 결과(MEM/WB 단계)에서 전달 → 첫 번째 ALU 피연산자 |
| **No Hazard** | 00                           | ID/EX  | 두 번째 ALU 피연산자도 그대로 레지스터에서 읽음              |
| **1b**        | 10                           | EX/MEM | 한 단계 앞의 ALU 결과를 두 번째 피연산자로 전달             |
| **2b**        | 01                           | MEM/WB | 두 단계 앞의 ALU 결과를 두 번째 피연산자로 전달             |

* ForwardA, ForwardB = 00 → 레지스터에서 읽기 (정상)
* ForwardA, ForwardB = 10 → 바로 앞(EX/MEM) 결과를 사용
* ForwardA, ForwardB = 01 → 두 단계 앞(MEM/WB) 결과를 사용

&ensp;orwardA는 ALU의 왼쪽 입력(Rs), ForwardB는 ALU의 “오른쪽 입력(Rt)” 에 대응한다.<br/>

&ensp;전체 동작 흐름 요약<br/>
1. Forwarding Unit이 두 레지스터 ID를 비교
2. 필요하면 ForwardA / ForwardB 신호를 설정 (10 또는 01)
3. ALU 입력 MUX가 신호에 따라 가장 최신 데이터를 선택
4. 명령어가 멈추지 않고(EX 단계에서 바로 계산 수행) 진행

&ensp;Forwarding은 "레지스터에 쓰기 전에 결과를 바로 다음 명령어에 전달하는" 기술로 MUX 제어 신호(ForwardA, ForwardB) 를 통해 ALU 입력 경로를 바꾼다. 덕분에 Stall 없이 파이프라인이 매끄럽게 돌아간다.<br/>

&ensp;포워딩이 필요한 두 상황<br/>
&ensp;forwarding의 목적: 지금 EX에 들어갈 명령어(ID/EX)의 ALU 입력(Rs, Rt)에 가장 최신 결과를 꽂아 주는 것<br/>

&ensp;(1) EX hazard = Type 1a/1b<br/>
&ensp;바로 한 단계 앞(EX/MEM)에 있는 생산자의 결과가 필요할 때<br/>
&ensp;조건 A (왼쪽 입력, Rs)<br/>
```swift
EX/MEM.RegWrite = 1
∧ EX/MEM.RegisterRd ≠ 0
∧ EX/MEM.RegisterRd = ID/EX.RegisterRs
→ ForwardA = 10
```

&ensp;조건 B (오른쪽 입력, Rt)<br/>
```swift
EX/MEM.RegWrite = 1
∧ EX/MEM.RegisterRd ≠ 0
∧ EX/MEM.RegisterRd = ID/EX.RegisterRt
→ ForwardB = 10
```

&ensp;의미: "바로 앞 명령어의 결과(방금 ALU가 만든 값)를 ALU 입력으로 직접 가져와!"<br/>

&ensp;(2) MEM hazard = Type 2a/2b<br/>
&ensp;두 단계 앞(MEM/WB)에 있는 생산자의 결과가 필요할 때<br/>
&ensp;조건 C (왼쪽 입력, Rs)<br/>
```swift
MEM/WB.RegWrite = 1
∧ MEM/WB.RegisterRd ≠ 0
∧ MEM/WB.RegisterRd = ID/EX.RegisterRs
→ ForwardA = 01
```

&ensp;조건 D (오른쪽 입력, Rt)<br/>
```swift
MEM/WB.RegWrite = 1
∧ MEM/WB.RegisterRd ≠ 0
∧ MEM/WB.RegisterRd = ID/EX.RegisterRt
→ ForwardB = 01
```

&ensp;의미: 두 칸 앞(WB 직전)에 있는 결과를 가져와<br/>
&ensp;RegWrite=1과 Rd≠$zero(0) 체크는 불필요한 포워딩 방지용(레지스터를 실제로 쓰는 명령만 대상)<br/>

Double Data Hazard
====

```bash
add $1, $1, $2   # ① $1 갱신
add $1, $1, $3   # ② $1 다시 갱신 (가장 최신)
add $1, $1, $4   # ③가 EX에서 읽을 $1은 '②의 결과'여야 함
```

* 같은 ALU 입력에 대해 type1(앞 단계)과 type2(두 단계 앞)가 동시에 참일 수 있다.
* 이때는 가장 최신 결과를 써야 하므로 type1(=EX/MEM) 우선
* 따라서 포워딩 우선순위: `EX/MEM(10) > MEM/WB(01) > 레지스터(00)`

&ensp;Revised Control for Type 2 Hazards<br/>
&ensp;핵심 개념<br/>
* MEM 단계에서 결과를 전달하는 Type 2 포워딩(Forward = 01) 은 앞 단계(EX/MEM)에서 이미 포워딩할 게 없을 때만 수행해야 한다.
* 그래서 조건문에 `not (EX/MEM ... )` 이 붙었다.

&ensp;공식 해석<br/>
&ensp;ForwardA (왼쪽 ALU 입력 Rs 용)<br/>
```c
If (MEM/WB.RegWrite
    and (MEM/WB.RegisterRd != 0)
    and not (EX/MEM.RegWrite
             and (EX/MEM.RegisterRd != 0)
             and (EX/MEM.RegisterRd = ID/EX.RegisterRs))
    and (MEM/WB.RegisterRd = ID/EX.RegisterRs))
        ForwardA = 01
```

&ensp;ForwardB (오른쪽 ALU 입력 Rt 용)<br/>
```c
If (MEM/WB.RegWrite
    and (MEM/WB.RegisterRd != 0)
    and not (EX/MEM.RegWrite
             and (EX/MEM.RegisterRd != 0)
             and (EX/MEM.RegisterRd = ID/EX.RegisterRt))
    and (MEM/WB.RegisterRd = ID/EX.RegisterRt))
        ForwardB = 01
```

&ensp;두 단계 앞(MEM/WB)의 결과를 포워딩하려면 그보다 한 단계 앞(EX/MEM)에서 이미 포워딩해야 할 값이 없을 때만 한다.<br/>
* EX/MEM 매치가 있으면 → `ForwardA/B = 10` (Type 1 우선)
* 그게 없을 때만 MEM/WB 매치 → `ForwardA/B = 01`

&ensp;최종 우선순위 로직 - ForwardA<br/>
```bash
if (EX/MEM.RegWrite
    ∧ EX/MEM.RegisterRd ≠ 0
    ∧ EX/MEM.RegisterRd = ID/EX.RegisterRs)
    ForwardA = 10             # type 1a가 참이면 이것이 최우선

else if (MEM/WB.RegWrite
         ∧ MEM/WB.RegisterRd ≠ 0
         ∧ MEM/WB.RegisterRd = ID/EX.RegisterRs)
    ForwardA = 01             # type 2a는 그 다음

else
    ForwardA = 00             # 포워딩 필요 없음(레지스터에서 읽기)
```

&ensp;핵심: EX/MEM 매치가 보이면 무조건 10을 선택하고 아니라면 그 다음(01)을 고려한다. 이렇게 해야 가장 최신 값을 보장한다.<br/>

&ensp;한 눈 정리 표<br/>

| 상황            | 비교 대상                  | 조건 충족 시 MUX       | 의미                |
| ------------- | ---------------------- | ----------------- | ----------------- |
| **No hazard** | —                      | `ForwardA/B = 00` | 레지스터 파일에서 읽기      |
| **Type 1a**   | `EX/MEM.Rd = ID/EX.Rs` | `ForwardA = 10`   | 한 단계 앞 결과 → ALU A |
| **Type 1b**   | `EX/MEM.Rd = ID/EX.Rt` | `ForwardB = 10`   | 한 단계 앞 결과 → ALU B |
| **Type 2a**   | `MEM/WB.Rd = ID/EX.Rs` | `ForwardA = 01`   | 두 단계 앞 결과 → ALU A |
| **Type 2b**   | `MEM/WB.Rd = ID/EX.Rt` | `ForwardB = 01`   | 두 단계 앞 결과 → ALU B |
| **우선순위**      | —                      | `10 > 01 > 00`    | 최신값 우선(EX/MEM 우선) |

&ensp;요약<br/>

| 우선순위 | 포워딩 경로          | 제어값  | 설명                     |
| ---- | --------------- | ---- | ---------------------- |
| 1.  | EX/MEM (Type 1) | `10` | 가장 최신 결과 → ALU로 직접 전달  |
| 2. | MEM/WB (Type 2) | `01` | EX/MEM이 없을 때만 WB 결과 사용 |
| 3.  | 없음              | `00` | 그냥 레지스터 파일에서 읽음        |

Forwarding unit이 들어간 5-단계 MIPS 파이프라인 데이터패스
====

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-12.png" width="500"></p>

&ensp;림을 볼 때는 왼→오른쪽, 앞→뒤 순서로 레이어를 잡으면 쉽게 읽힌다.<br/>
1. IF 단계
* PC → Instruction memory → IF/ID 레지스터 (다음 사이클에 ID가 읽어갈 명령어와 필드를 임시 보관)
2. ID 단계
* Register File(레지스터 묶음)에서 `Rs`, `Rt` 값을 읽음
* 제어기(Control)가 명령어 필드로부터 RegWrite, MemRead, MemWrite, ALUSrc, MemtoReg 등을 생성
3. EX 단계
* ALU가 연산
* 여기서 포워딩 경로와 ALU 입력 MUX가 핵심 (그림의 파란/하늘색 선)
4. MEM 단계
* Data memory 접근 (lw/sw)
* 제어 신호 MemRead/Write 사용
5. WB 단계
* 최종 결과를 레지스터 파일에 쓰기(RegWrite, MemtoReg)

&ensp;각 단계 사이에 있는 굵은 세로 블록이 파이프라인 레지스터(IF/ID, ID/EX, EX/MEM, MEM/WB)이다.<br/>
&ensp;사이클 경계이자 데이터를 다음 단계로 딱 한 사이클 지연시킨다고 생각하면 된다.<br/>

&ensp;포워딩이 붙으면서 생긴 3가지 ‘읽는 포인트’<br/>
1. ALU 입력 MUX 2개 (ForwardA, ForwardB)
* ALU의 왼쪽 입력(A : 보통 Rs), 오른쪽 입력(B : 보통 Rt) 앞에 MUX가 한 개씩
* 이 MUX의 3가지 선택지:
    - `00` : ID/EX에서 온 원래 레지스터 값(레지스터 파일에서 읽은 값)
    - `10` : EX/MEM의 결과(한 단계 앞) ← Type 1 포워딩
    - `01` : MEM/WB의 결과(두 단계 앞) ← Type 2 포워딩
2. ALUSrc MUX (오른쪽 피연산자 선택)
    * R-형(연산)면 Rt/포워딩된 값, I-형(즉시수)면 즉시값(imm) 을 선택
    * ForwardB가 선택돼도 ALUSrc가 1이면 즉시값이 우선(즉시값 사용 명령에는 포워딩이 필요 없음)
3. Forwarding Unit(비교기 + 제어 생성기)
    * 내부에서 ID/EX.Rs/Rt ↔ EX/MEM.Rd, MEM/WB.Rd를 비교
    * 그리고 `RegWrite=1` · `Rd≠$zero` 조건을 확인한 뒤 ForwardA/B = 10/01/00 제어 신호를 만들어 MUX에 보냄

&ensp;클로즈업을 읽는 요령<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-13.png" width="500"></p>

* 위쪽 작은 MUX : 보통 shamt/PC+4 같은 특수 입력 선택
* 가운데 큰 MUX(두 개) : 바로 ForwardA/B가 제어하는 ALU 입력 선택기
* ALUSrc: 오른쪽 입력(ForwardB의 결과 vs 즉시값) 최종 선택
* 아래의 Forwarding unit: 비교/판정 블록, EX/MEM.Rd·MEM/WB.Rd·ID/EX.Rs/Rt 신호선이 들어오고 `ForwardA/B` 가 나감
* 오른쪽 세로 블록(EX/MEM, MEM/WB) : 앞선 명령의 결과값과 목적지 번호를 한 사이클씩 보관하는 레지스터

&ensp;자주 헷갈리는 포인트 정리<br/>
* 왜 Type1(10)이 Type2(01)보다 우선? → 같은 레지스터 이름이라도 가장 최신 결과가 맞아야 하니까. 방금 EX를 통과한 값(EX/MEM)이 WB 직전 값(MEM/WB)보다 최신
* RegWrite=0 이면? → 그 명령은 레지스터를 쓰지 않음(예: sw, beq). 포워딩 후보에서 제외
* $zero(0번)으로 쓰는 경우는? → 쓰더라도 실제로는 무시이므로 포워딩 불필요. Rd≠0 체크가 들어가는 이유
* Load-use 해저드(바로 뒤가 lw 결과를 쓰는 경우)→ lw의 결과는 MEM 단계에서야 생김 바로 뒤 명령이 EX에서 필요로 하면 한 사이클 스톨이 필요(포워딩만으로는 한 틱 모자람)
→ 흔한 패턴: lw r1, 0(r2) 다음에 add r3, r1, r4 → 1-cycle bubble 삽입 또는 스케줄링/재배치 필요

&ensp;회로 읽기 체크리스트<br/>
1. 파이프라인 레지스터 위치(IF/ID, ID/EX, EX/MEM, MEM/WB)를 먼저 표시한다.
2. ALU 입력 MUX 2개를 찾고 각각의 3가지 입력(레지스터/EXMEM/MEMWB)을 확인한다.
3. Forwarding Unit의 입력(두 Rd, Rs/Rt)과 출력(ForwardA/B)을 따라간다.
4. ALUSrc가 1인 명령(I-형)은 즉시값 경로가 최종 선택됨을 체크한다.
5. 제어 신호(RegWrite, MemRead/Write, MemtoReg)가 어디서 생성되고 어디에 쓰이는지 확인한다.
6. 예제 명령열을 사이클별로 놓고, EX에 들어가는 순간에 ForwardA/B 값을 표로 적어본다.
7. lw 바로 다음 사용(load-use)처럼 포워딩으로 안 되는 한계가 있는지 평가한다.

&ensp;포워딩 데이터패스는 Forwarding Unit(비교/판정) → ForwardA/B(제어선) → ALU 입력 MUX(경로 선택) 의 3단 구조로 읽는다. 우선순위는 EX/MEM(10) > MEM/WB(01) > 레지스터(00), ALUSrc가 즉시값을 고르면 오른쪽 입력은 즉시값이 우선된다.<br/>

Load-Use Data Hazard
=====

&ensp;Load-Use-Hazard는 로드(load) 명령어의 결과를 바로 다음 명령어가 사용하려 할 때 발생하는 데이터 의존성 문제이다.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-14.png" width="500"></p>

* 파이프라인 타이밍을 보면, 빨간 원 부분이 충돌 지점
* lw가 MEM 단계에 있을 때 데이터가 막 메모리에서 나오는 중인데 and는 이미 EX에서 그 값을 쓰려 함
* 이때 하드웨어가 자동으로 1 사이클 멈춤(버블 삽입)

```assemble
lw   $2, 20($1)    # 메모리에서 $2로 값을 로드 (결과는 MEM 단계에서 나옴)
and  $4, $2, $5    # 바로 다음 명령에서 $2 사용
```

* lw의 결과($2)는 MEM 단계가 끝나야 준비됨.
* 하지만 and는 그 다음 사이클의 EX 단계에서 $2가 필요함
* 데이터가 아직 메모리에서 나오지 않았기 때문에 Forwarding으로도 해결할 수 없음

&ensp;→ 해결책: 1사이클 Stall(버블) 삽입. and 명령을 한 사이클 늦게 실행시켜 데이터를 기다림<br/>

Hazard Detection Unit
====

&ensp;파이프라인이 이런 Load-Use 상황을 자동으로 감지하고 Stall을 발생시키는 하드웨어이다.<br/>

&ensp;작동 조건<br/>
&ensp;ID 단계에서 아래 조건을 검사한다.<br/>
```c
if (ID/EX.MemRead = 1)        // 현재 EX로 가는 명령이 lw임
  and ((ID/EX.RegisterRt = IF/ID.RegisterRs)   // 다음 명령이 그 레지스터를 읽거나
        or (ID/EX.RegisterRt = IF/ID.RegisterRt))
then
    stall the pipeline (1-cycle)
```

| Clock | IF             | ID             | EX             | MEM            | WB             |
| ----- | -------------- | -------------- | -------------- | -------------- | -------------- |
| 3     | `or $8,$2,$6`  | `and $4,$2,$5` | `lw $2,20($1)` |                |                |
| 4     | `or $8,$2,$6`  | `and $4,$2,$5` | **(bubble)**   | `lw $2,20($1)` |                |
| 5     | `add $9,$4,$2` | `or $8,$2,$6`  | `and $4,$2,$5` | **(bubble)**   | `lw $2,20($1)` |

* clock 4: Hazard Detection Unit이 스톨을 검출 → and 명령이 EX로 진입하지 않고, 버블이 삽입됨 → lw는 정상 진행 (MEM 단계로)
* clock 5: and가 EX로 이동 (이제 lw의 결과 사용 가능)

&ensp;결국 ID/Ex 단계에서 스톨을 검출하고 IF/ID 레지스터와 PC 업데이터를 1사이클 멈춰준다.<br/>

Hazard Detection Unit + Forwarding Unit
=====

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-4-15.png" width="500"></p>

&ensp;이 회로는 기존 5단계 MIPS 파이프라인에 Forwarding Unit(데이터 전달)과 Hazard Detection Unit(데이터 충돌 감지) 두 개의 보조 하드웨어가 추가된 형태이다.<br/>
* Forwarding Unit → ALU 입력에서 일어나는 대부분의 데이터 의존성 해결
* Hazard Detection Unit → Forwarding으로 안 되는 load-use 해저드 감지 및 Stall 삽입

&ensp;기본 데이터 경로(Data Path) 읽는 법<br/>

| 블록                            | 설명                       |
| ----------------------------- | ------------------------ |
| **PC & Instruction Memory**   | 다음 명령어를 가져옴 (IF 단계)      |
| **IF/ID 레지스터**                | 가져온 명령어를 ID 단계로 전달       |
| **Register File (Registers)** | ID 단계에서 `Rs`, `Rt` 값을 읽음 |
| **ID/EX 레지스터**                | 읽은 값 + 제어 신호들을 EX 단계로 전달 |
| **ALU**                       | 연산 수행 (EX 단계)            |
| **Data Memory**               | Load/Store 수행 (MEM 단계)   |
| **WB MUX**                    | 결과를 레지스터로 되돌려줌 (WB 단계)   |

&ensp;Forwarding Unit 읽기<br/>
&ensp;Forwarding Unit은 ALU 바로 앞(EX 단계)에 붙어 있다. 이 유닛은 EX 단계의 두 입력(Rs, Rt)이 최신 값을 쓰는지 판단한다.<br/>

&ensp;입력선 (왼쪽에서 들어오는 신호들)<br/>

| 신호 이름                                  | 의미                             |
| -------------------------------------- | ------------------------------ |
| **ID/EX.RegisterRs, ID/EX.RegisterRt** | 지금 EX로 들어가는 명령의 입력 레지스터 번호     |
| **EX/MEM.RegisterRd**                  | 한 단계 앞(EX→MEM) 명령의 목적지 레지스터 번호 |
| **MEM/WB.RegisterRd**                  | 두 단계 앞(MEM→WB) 명령의 목적지 레지스터 번호 |
| **EX/MEM.RegWrite, MEM/WB.RegWrite**   | 해당 명령이 레지스터에 값을 쓰는 명령인지 여부     |

&ensp;이 다섯 신호가 Forwarding Unit으로 들어간다. Forwarding Unit은 이들을 비교해서 누가 지금 필요한 값을 가지고 있는가를 결정한다.<br/>

&ensp;출력선 (오른쪽으로 나가는 신호들)<br/>

| 신호 이름        | 의미                    | 값                             |
| ------------ | --------------------- | ----------------------------- |
| **ForwardA** | ALU 왼쪽 입력(Rs)의 선택 제어  | 00:레지스터, 10:EX/MEM, 01:MEM/WB |
| **ForwardB** | ALU 오른쪽 입력(Rt)의 선택 제어 | 00:레지스터, 10:EX/MEM, 01:MEM/WB |

&ensp;이 두 신호는 ALU 앞의 MUX 두 개로 들어간다.<br/>

&ensp;데이터 흐름<br/>
1. ALU 왼쪽 입력(Rs)에 연결된 MUX는 ForwardA로 제어된다.
* ForwardA=00 → 레지스터 값 사용
* ForwardA=10 → EX/MEM 결과 사용 (Type 1a)
* ForwardA=01 → MEM/WB 결과 사용 (Type 2a)
2. ALU 오른쪽 입력(Rt)에 연결된 MUX는 ForwardB로 제어됩니다.
* ForwardB=00 → 레지스터 값 사용
* ForwardB=10 → EX/MEM 결과 사용 (Type 1b)
* ForwardB=01 → MEM/WB 결과 사용 (Type 2b)

&ensp;Forwarding Unit은 "어디서 값을 가져올지"를 결정하고 ALU 앞 MUX가 "그 경로를 실제로 선택"한다.<br/>

&ensp;Hazard Detection Unit 읽기<br/>
&ensp;이건 Forwarding Unit보다 앞 단계(ID) 에 있다. 이 유닛은 Forwarding으로도 해결이 불가능한 상황, 즉 Load-Use Hazard를 감지한다.<br/>

&ensp;입력선<br/>

| 신호                                     | 설명                        |
| -------------------------------------- | ------------------------- |
| **ID/EX.MemRead**                      | 현재 EX로 들어가는 명령이 load인지 확인 |
| **ID/EX.RegisterRt**                   | load 명령이 결과를 쓸 레지스터 번호    |
| **IF/ID.RegisterRs, IF/ID.RegisterRt** | 다음 명령어가 읽으려는 레지스터 번호      |

&ensp;동작 논리<br/>
```c
if (ID/EX.MemRead == 1) and 
   ((ID/EX.RegisterRt == IF/ID.RegisterRs) or
    (ID/EX.RegisterRt == IF/ID.RegisterRt))
then
   stall pipeline
```

&ensp;현재 명령이 lw이고, 다음 명령이 그 로드한 레지스터를 바로 쓰려 한다면 Stall!<br/>

&ensp;출력선 (제어 신호)<br/>

| 신호                    | 역할                   |
| --------------------- | -------------------- |
| **PCWrite = 0**       | PC 멈춤 (새 명령 가져오지 않음) |
| **IF/ID.Write = 0**   | ID 단계 멈춤 (현재 명령 유지)  |
| **ID/EX.Control = 0** | 다음 EX 단계에 nop(버블) 삽입 |


| 구분 | Forwarding Unit             | Hazard Detection Unit             |
| -- | --------------------------- | --------------------------------- |
| 위치 | **EX 단계 근처 (ALU 앞)**        | **ID 단계 근처 (Register File 앞)**    |
| 입력 | Register ID 비교 (Rs/Rt ↔ Rd) | MemRead, Register ID 비교           |
| 역할 | ALU–ALU 의존성 해결 (포워딩)        | Load–Use 의존성 해결 (스톨)              |
| 출력 | ForwardA, ForwardB          | PCWrite, IF/ID.Write, ID/EX.Flush |
| 결과 | 파이프라인 멈추지 않음                | 파이프라인 1사이클 멈춤 (버블 생성)             |




Inserting Bubbles
=====

&ensp;버블 삽입 방식 2단계<br/>
&ensp;(1) Stall in IF & ID stages
* PC와 IF/ID 레지스터를 멈추면 같은 명령어를 한 사이클 더 유지하게 된다. 새로운 명령을 가져오지 않는다.(fetch stop) → 한 사이클 동안 대기

&ensp;(2) Simulate NOP (in EX, MEM, WB)<br/>
* 다음 단계(EX, MEM, WB)에 들어가는 제어 신호를 0으로 초기화해서
실제로 아무 일도 하지 않도록 함
* 실질적으로 “NOP 명령어”를 실행하는 효과를 만든다.

```text
RegWrite = 0
MemWrite = 0
(나머지는 don't care)
```

&ensp;Inserting Bubble 과정 이해하기<br/>
1. Hazard Detection Unit이 load-use를 감지
2. `PCWrite=0`, `IF/ID.Write=0` 으로 명령 흐름 정지
3. EX 단계에 들어갈 명령의 제어신호를 모두 0으로 만들어 → NOP 삽입
4. 1사이클 후, load 결과가 MEM 단계에서 나오면 다시 정상 실행

Delayed Load
====

&ensp;하드웨어로 Stall을 넣는 대신 컴파일러가 명령 순서를 조정해서 Stall이 생기지 않게 하는 방법이다.<br/>

&ensp;예시<br/>
```assembly
lw  $2, 0($1)
add $9, $4, $5    # (독립적인 명령)
and $3, $2, $6    # 이제 $2 사용 가능
```

* lw 다음에 $2를 사용하지 않는 독립 명령어를 끼워 넣으면 lw가 메모리 접근(MEM)을 끝낼 시간 동안 파이프라인이 멈추지 않음
* 이걸 Delayed Load(지연된 로드) 라고 한다.

&ensp;컴파일러 관점<br/>
&ensp;파이프라인을 효율적으로 활용하려면 컴파일러가 해저드 발생을 미리 예측하고 Stall이 생기지 않게 명령 재배치(Code Scheduling)를 수행해야 한다. 그렇지 않으면 하드웨어 강제로 스톨을 넣어서 성능이 떨어지게 된다.<br/>

&ensp;요약<br/>

| 구분                  | 문제 상황                 | 해결 방법             | 동작 방식                                 |
| ------------------- | --------------------- | ----------------- | ------------------------------------- |
| **일반 Data Hazard**  | ALU → ALU 간 결과 사용     | **Forwarding**    | EX/MEM, MEM/WB → ALU 직접 전달            |
| **Load-Use Hazard** | `lw` 결과를 바로 다음 명령이 사용 | **1-cycle Stall** | Hazard Detection Unit이 감지 후 Bubble 삽입 |
| **Delayed Load**    | 컴파일러 최적화로 Stall 방지    | **명령 재배치**        | 독립 명령을 중간에 삽입                         |
