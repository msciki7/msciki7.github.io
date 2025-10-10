---
title: "chapter 4. The Processor-Datapath Design"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-10-10
last_modified_at: 2025-10-10
---

Building a Datapath
=====

&ensp;<b>Instruction Fetch 블록</b><br/>
&ensp;구성요소<br/>
* PC: 다음 명령의 주소 저장
* Instruction Memory: PC가 가리키는 명령어를 읽음
* Adder(PC+4): 다음 순차 명령 주소 계산

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-1.png" width="600"></p>

&ensp;동작<br/>
1. Instruction ← IMem[PC] (명령어 읽기)
2. PC_next_seq ← PC + 4 (순차 실행 주소)
3. 이후 분기/점프가 없으면 PC ← PC_next_seq로 갱신

&ensp;포인트: fetch 시점에는 항상 PC+4를 준비해 두고 뒤에서 branch/jump가 결정되면 덮어씀<br/>

&ensp;<b>R-format 실행</b><br/>
&ensp;대상: `add/sub/and/or/slt` (R-type)<br/>
&ensp;주요선<br/>
* Register file: Read register 1=rs, Read register 2=rt → Read data1,2
* ALU: 두 입력(레지스터 값)과 ALU operation으로 결과/Zero

&ensp;컨트롤<br/>
* RegWrite=1 (결과를 레지스터에 씀)
* RegDst=1 (쓰기 대상=rd)
* ALUSrc=0 (ALU 2번째 입력=rt 값)
* MemRead=0, MemWrite=0, MemtoReg=0
* ALUOp=Rype (funct로 세부연산 결정)

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-2.png" width="600"></p>

&ensp;마이크로-오퍼레이션<br/>
```css
A ← R[rs]
B ← R[rt]
ALU_result ← f(A,B)           // add, sub, and, or, slt …
R[rd] ← ALU_result
```

&ensp;<b>Memory Reference 실행 공통</b><br/>
&ensp;대상: `lw rt, imm(rs)` / `sw rt, imm(rs)` <br/>
&ensp;step 3(공통): 주소 계산<br/>
```css
base ← R[rs]
off  ← signext(imm)           // 16→32 부호확장
Addr ← base + off             // ALU로 계산
```

* 해야 할 일: 메모리 접근 주소(EA, effective address) 만들기 EA = R\[rs\] + signext(imm)
* 왜 sign-extend? 오프셋 imm는 16비트 부호 있는 값이라 +/- 둘 다 가능해야 함
* 데이터패스 흐름
1. Register File에서 R[rs](base)와 R[rt](데이터용)을 동시에 읽음
2. imm는 Sign-Extend(16→32) 를 거쳐 ALU로 감
3. ALU가 R[rs] + signext(imm) 수행 → EA 출력

* 컨트롤 신호(공통): ALUSrc=1 (ALU의 두 번째 입력을 즉시수로)

&ensp;정렬 주의: lw/sw는 워드 정렬 주소(주소 % 4 = 0) 여야 함.<br/>
&ensp;→ 여기까지는 lw와 sw 동일 (ALU의 2번째 입력을 immediate로 쓰므로 ALUSrc=1)<br/>

&ensp;`sw` (store) — 레지스터 → 메모리<br/>
&ensp;의미: R[rt] 값을 EA 주소의 메모리에 써라<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-4.png" width="600"></p>

&ensp;데이터패스<br/>
1. R[rs] + signext(imm) → ALU → EA
2. **Register File의 Read data 2 (= R[rt])**가 Data Memory의 Write Data로 감
3. Data Memory에서 MemWrite=1일 때, Mem[EA] ← R[rt]

&ensp;컨트롤 신호<br/>
* ALUSrc=1, MemWrite=1, MemRead=0
* RegWrite=0 (레지스터에 되돌려 쓰지 않음)
* MemtoReg=x, RegDst=x (사용 안 함)

&ensp;한 줄식 마이크로-오퍼레이션<br/>
```scss
Addr ← R[rs] + signext(imm)
Mem[Addr] ← R[rt]
```

&ensp;`lw` (load) — 메모리 → 레지스터<br/>
&ensp;의미: EA 주소의 메모리 값을 R[rt] 에 써라<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-5.png" width="600"></p>

&ensp;데이터패스<br/>
1. R[rs] + signext(imm) → ALU → EA
2. Data Memory가 MemRead=1이면 Read Data = Mem[EA] 출력
3. 그 값이 Register File의 Write Data로 들어가고 RegWrite=1, RegDst=0, MemtoReg=1이면 R[rt] ← Read Data

&ensp;컨트롤 신호<br/>
* ALUSrc=1, MemRead=1, MemWrite=0
* RegWrite=1, RegDst=0(대상=rt), MemtoReg=1(메모리값을 레지스터에)

&ensp;한 줄식 마이크로-오퍼레이션<br/>
```scss
Addr ← R[rs] + signext(imm)
R[rt] ← Mem[Addr]
```

&ensp;두 명령을 헷갈리지 않는 요령<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-6.png" width="600"></p>

&ensp;마음 속 그림:<br/>
* sw는 레지스터 값을 밖으로 밀어 넣기
* lw는 밖의 값을 안으로 끌어오기

&ensp;`sw $t0, 32($s1)`<br/>
```scss
Addr = R[$s1] + 32
Mem[Addr] = R[$t0]
```

&ensp;`lw $t0, -4($sp)`<br/>
```scss
Addr = R[$sp] + (-4)
R[$t0] = Mem[Addr]
```

&ensp;<b>Branch 명령의 기본 개념 (beq rs, rt, offset)</b><br/>
&ensp;의미: `if (R[rs] == R[rt]) then PC ← PC + 4 + (signext(offset) << 2)`<br/>
&ensp;(그렇지 않으면 PC ← PC + 4)<br/>

* 두 레지스터 값이 같으면 분기 성공(PC 점프)
* 다르면 다음 명령으로 이동

&ensp;step 3 — ALU로 비교 & 분기 주소 계산<br/>
&ensp;1. ALU 비교 (Equality Check)<br/>
* ALU 입력 1: R[rs]
* ALU 입력 2: R[rt]
* ALU 연산: subtraction (R[rs] - R[rt])
* 결과:
    - 결과가 0 → Zero 플래그 = 1 → 두 값이 같음
    - 결과가 ≠0 → Zero = 0 → 다름

&ensp;ALU는 단순히 “0인지 아닌지”를 확인하는 데 쓰인다.<br/>

&ensp;Branch Target Address 계산<br/>
* 기본 PC는 PC + 4 (다음 명령)
* 여기에 offset을 더해야 함

&ensp;offset은 16비트 부호 있는 값<br/>
&ensp;→ Sign Extend로 32비트로 확장<br/>
&ensp;→ Shift Left 2 (왜냐면 명령어는 항상 4바이트 정렬되기 때문!)<br/>

&ensp;$Branch Target = (PC+4)+(signext(offset)<<2)$ <br/>

&ensp;Step4 — 비교 결과에 따라 PC 변경<br/>
&ensp;조건:<br/>
&ensp;Zero == 1 (즉, R[rs] == R[rt])<br/>
&ensp;그리고 Branch 신호(=beq opcode)가 활성화일 때만 → PC ← Branch Target<br/>

&ensp;그 외에는 PC ← PC + 4 (다음 명령 실행)<br/>

&ensp;데이터패스 흐름<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-7.png" width="600"></p>

&ensp;주요 블록별 역할<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-8.png" width="600"></p>

&ensp;데이터 흐름 요약<br/>
1. PC → (Instruction Memory) → 명령 fetch
2. Register File → R[rs], R[rt] 값 ALU로
3. ALU: R[rs] - R[rt] → Zero 출력
4. offset → Sign-Extend → Shift-Left-2 → Adder
5. Adder: (PC+4) + (offset<<2) → Branch target
6. Branch & Zero = 1이면 MUX 통해 PC ← Target

&ensp;예제<br/>
&ensp;`beq $t0, $t1, 4` <br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-9.png" width="600"></p>

&ensp;Shift Left 2 & Sign Extend<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-10.png" width="600"></p>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-12.png" width="600"></p>


&ensp;이유: 모든 MIPS 명령어는 4바이트(=1워드) 단위 정렬이라 offset은 워드 기준, 주소 계산 시 ×4 해야 함<br/>

&ensp;핵심 요약<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-11.png" width="600"></p>

&ensp;<b>Single-Cycle Datapath</b><br/>
&ensp;모든 명령어를 하나의 클록 사이클 안에서 완전히 실행한다.<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-13.png" width="600"></p>

&ensp;Datapath 만들기 예시<br/>
&ensp;Arithmetic/Logic 명령어 데이터패스 + Memory 명령어 데이터패스를 결합<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-14.png" width="600"></p>

&ensp;구성요소<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-15.png" width="600"></p>

&ensp;동작별 흐름<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-16.png" width="600"></p>

&ensp;두 개의 Datapath 결합<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-17.png" width="600"></p>

&ensp;이 그림은 R-type(검정선)과 Memory 명령어(빨간선)의 데이터 흐름을 하나의 그림으로 합친 것이다.
* 빨간선: `lw/sw` 용 경로
    - Sign Extend, ALUSrc = 1, MemRead/MemWrite 사용
* 검정선: R-type용 경로
    - 두 레지스터 값 → ALU → 결과 다시 Register File로

&ensp;이제 공통 부분은 공유하고 명령어마다 MUX로 제어한다.<br/>

&ensp;최종 Single-Cycle Datapath<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-18.png" width="600"></p>

&ensp;주요 구성요소 정리<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-19.png" width="600"></p>

&ensp;명령별 데이터 흐름 요약<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-20.png" width="600"></p>

&ensp;정리 요약<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-21.png" width="600"></p>

Simple Implementation Scheme
=====

&ensp;<b>ALU Control의 역할</b><br/>
&ensp;목적: ALU가 해야 할 연산을 결정하는 것(ALU는 add, sub, and, or, slt 등 여러 일을 할 수 있음)<br/>

&ensp;구조 요약<br/>
&ensp;MIPS 명령어는 두 단계로 제어된다.<br/>
1. Main Control Unit → ALU에 **대략적인 지시(ALUOp)**를 줌(예: "이건 R-type이다", "이건 branch다", "이건 load/store다")
2. ALU Control Unit → ALUOp와 R-type의 function field를 조합해서 정확한 ALU 동작을 결정함

&ensp;The ALU Control<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-22.png" width="600"></p>

&ensp;<b>Main Control + ALU Control 연결</b><br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-23.png" width="600"></p>

&ensp;이 그림은 명령어 비트들이 제어신호로 해석되는 전체 구조를 보여준다.<br/>

&ensp;흐름 요약<br/>
&ensp;1. Instruction Memory에서 명령어를 가져옴<br/>
```css
[31-26] → opcode  
[25-21] → rs  
[20-16] → rt  
[15-11] → rd  
[5-0] → funct
```

&ensp;2. Main Control Unit<br/>
* opcode(6비트)를 입력으로 받아 다음 제어신호를 출력

```css
RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, ALUOp(2비트)
```

&ensp;3. ALU Control Unit<br/>
* ALUOp(2비트) + funct(6비트)를 입력으로 받아 → ALU operation code(4비트)를 출력(즉 실제 ALU 동작: add/sub/and/or/slt 등)

&ensp;4. ALU<br/>
* ALU control로부터 받은 4비트 신호에 따라 실제 연산 수행

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-24.png" width="600"></p>

* 파란색: ALU 제어 관련 경로(ALUOp, function, ALU control)
* 파란 박스: Main Control
* 작은 파란 원: ALU control
* 파란선이 ALU 입력까지 이어짐 (즉, 이 제어 신호가 ALU 동작을 결정)

&ensp;Truth Table<br/>
&ensp;ALUOp + funct 조합에 따른 ALU Operation 출력 진리표<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-25.png" width="600"></p>

&ensp;ALU Control 논리식<br/>
&ensp;진리표를 논리회로로 단순화한 결과이다.<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-26.png" width="600"></p>

* Operation2, Operation1, Operation0은 ALU 제어 비트 3개
* ALUOp은 Main Control에서 주는 두 비트
* F0~F5는 Function 필드의 하위 비트들

&ensp;이 회로 덕분에 ALU가 명령어 종류(opcode)와 연산 종류(function)에 따라 정확히 맞는 연산을 자동으로 선택할 수 있다.<br/>

&ensp;요약 정리<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-2-27.png" width="600"></p>

* Main Control은 이 명령이 어떤 종류인지만 결정
* ALU Control은 그 종류 안에서 정확히 어떤 연상르 할지 결정
* 이 두 개가 함께 MIPS 데이터패스의 핵심 제어 구조를 완성한다.