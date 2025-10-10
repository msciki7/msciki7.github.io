---
title: "chapter 4. The Processor-MIPS Processor"
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

Introduction
=====

&ensp;A Basic MIPS Implementation<br/>
* 메모리 참조: lw, sw
* 산술/논리: add, sub, and, or, slt
* 분기/점프: beq, j

&ensp;컴퓨터 구성요소<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-1.png" width="600"></p>


&ensp;PC(Program Counter): 다음에 가져올(fetch) 명령어의 주소. MIPS는 바이트 주소이므로 보통 PC = PC + 4(명령어 길이 4바이트)<br/>
&ensp;IR(Instruction Register): 메모리에서 읽어온 명령어 자체를 잠시 보관<br/>
&ensp;MAR/MBR (개념적 레지스터): 메모리 주소/데이터 버퍼. 단일사이클 MIPS 교과서 구현에서는 Instruction memory / Data memory로 나눠 그 역할을 대신함<br/>
&ensp;Register File: 32개의 범용 레지스터(`$0~$31`). 동시에 2개 읽기 + 1개 쓰기 지원
&ensp;ALU: 산술, 논리 연산, 주소 계산, 비교 수행<br/>
&ensp;Control: 명령어 필드(opcode,, funct)를 해석해 데이터패스 스위치를 제어(Mux 선택, 레지스터 쓰기 여부, 메모리 읽기/쓰기, ALU 연산코드 등)<br/>

&ensp;모든 명령어가 공통으로 거치는 4단계<br/>
1. Instruction Fetch
* InstructionMemory[PC]를 읽어 IR ← instr
* PC ← PC + 4 (분기/점프가 있으면 뒤에서 덮어씀)
2. Decode & Register Read
* opcode로 명령 종류 판별, 필요 시 funct로 세부 연산 결정
* 레지스터 피치(프리페치): rs, rt를 Register File에서 동시에 읽음
* 즉시수(immediate)라면 부호 확장(sign-extend) 준비
3. Execute (명령 종류별로 ALU 사용)
* 메모리 참조: 유효 주소 = ALU = R[rs] + signext(imm)
* 산술/논리: ALU = f(R[rs], R[rt]/imm)
* brach: ALU = R[rs] − R[rt]로 비교(Zero 여부), brach 타겟 = (PC+4) + (signext(imm) << 2)
4. Memory / Write-Back / PC Update (최종 단계)
* load word: M[주소] 읽어와 레지스터에 씀
* store word: R[rt]를 메모리 주소에 저장
* 산술/논리: ALU 결과를 목적지 레지스터에 씀
* 분기/점프: 조건 성립 시 PC ← 타겟, 아니면 그대로(이미 PC+4)

&ensp;명령어별 단계<br/>
&ensp;각 명령어가 4단계를 어떻게 쓰는지 정리:<br/>
&ensp;1) 메모리 참조<br/>
&ensp;`lw rt, imm(rs)` <br/>
1. Fetch: IR←Mem[PC], PC←PC+4
2. Decode: A←R[rs], Imm←signext(imm)
3. Execute: Addr←A + Imm
4. Memory/Write-Back: MDR←Mem[Addr], R[rt]←MDR

&ensp;`sw rt, imm(rs)` <br/>
1. Fetch: IR←Mem[PC], PC←PC+4
2. Decode: A←R[rs], Imm←signext(imm)
3. Execute: Addr←A + Imm
4. Memory: Mem[Addr]←R[rt] (쓰기)

&ensp;주의: 정렬(Alignment)-ls/sw는 워드(4바이트)정렬 주소여야 함(주소 % 4 == 0) 아니면 하드웨어/시뮬레이터에서 예외<br/>

&ensp;2) 산술/논리 <br/>
&ensp;`add rd, rs, rt (R-type)` <br/>
1. Fetch
2. Decode: A←R[rs], B←R[rt]
3. Execute: ALU←A + B
4. Write-Back: R[rd]←ALU

&ensp;`addi rt, rs, imm (I-type)` <br/>
1. Fetch
2. Decode: A←R[rs], Imm←signext(imm)
3. Execute: ALU←A + Imm
4. Write-Back: R[rt]←ALU

&ensp;다른 연산(sub/and/or/slt)도 ③에서 ALU 함수만 교체<br/>

&ensp;3) 분기/점프<br/>
&ensp;`beq rs, rt, offset` <br/>
1. Fetch
2. Decode: A←R[rs], B←R[rt], Off←signext(offset)
3. Execute: ALU←A − B (Zero 플래그 확인), Target ← (PC+4) + (Off << 2)
4. PC 갱신: Zero=1이면 PC←Target, 아니면 그대로

&ensp;`j target26` <br/>
* 타겟 계산: PC[31:28] ◦ target26 ◦ 00 (상위 4비트는 PC+4 에서 가져오고 26비트 필드는 왼쪽로 2비트 시프트해 하위 2비트 00)

&ensp;포인트 정리<br/>
* 왜 PC는 기본적으로 +4? MIPS 명령어는 항상 32비트(4바이트) 고 바이트 주소를 쓰기 때문
* 즉시수는 왜 부호 확장? addi, 분기 오프셋 등은 음수/양수 모두 가능하므로 16→32로 sign-extend
* 분기 타겟에 << 2를 왜 붙여? 명령어는 4바이트 단위 정렬이므로, 워드 주소 ×4로 바꾸는 셈(하위 2비트는 항상 0)
* 점프는 왜 상위 4비트를 PC에서? MIPS는 가까운(동일 256MB 블록) 안에서 점프하도록 설계. 상위 4비트는 컨텍스트 유지

&ensp;컴포넌트별 역할<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-2.png" width="600"></p>


&ensp;큰 그림: 한 사이클에 한 명령 데이터패스<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-3.png" width="600"></p>

&ensp;PC: 다음 명령의 주소, 기본적으로 `PC ← PC + 4` <br/>
&ensp;Instruction memory: PC가 가리키는 명령어를 읽어 IR(암시)에 전달<br/>
&ensp;Register file(Regs): 32개 레지스터. 동시에 2개 읽기(rs, rt) + 1개 쓰기(rd/rt)<br/>
&ensp;Sign-extend: 16비트 immediate/Branch Offset → 32비트 부호확장<br/>
&ensp;ALU: 산술/논리, 주소계산, 비교(Zero) 수행<br/>
&ensp;Data memory: lw/sw용 데이터 메모리<br/>
&ensp;Adder x2: 
* PC+4 계산
* branch target = (PC+4) + (signext(imm) << 2) 계산

&ensp;MUX(멀티플렉서): 한 선로에 여러 후보가 올 수 있으니 선택 신호로 하나만 통과시킴<br/>
&ensp;Control: opcode/funct를 해석해 모든 선택/쓰기/읽기 신호를 생성<br/>

&ensp;MUX가 필요한 이유<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-4.png" width="600"></p>

&ensp;그림의 빨간 동그라미 지점들은 두 개 이상의 소스가 한 목적지로 모이는 곳<br/>
&ensp;선을 그냥 합치면 단략이므로 반드시 MUX로 하나만 골라야 한다.<br/>

&ensp;주요 MUX들<br/>
* PCSrc MUX: 다음 PC가
    - PC+4(순차 실행)인지
    - 분기 타겟인지(beq 성립 시)를 선택
* RegDst MUX: 결과를 쓸 레지스터가
    - rt(I-type: lw/addi)인지
    - rd(R-type: add/sub/and…)인지 선택
* ALUSrc MUX: ALU의 두 번째 피연산자가
    - 레지스터 rt인지(R-type/beq)
    - 즉시수(sign-extended imm) 인지(lw/sw/addi) 선택.
* MemtoReg MUX: 레지스터에 쓸 값이
    - ALU 결과(R-type, sw는 쓰기없음)
    - Data memory에서 읽은 값(lw) 중 무엇인지 선택

&ensp;Basic Implementation of the MIPS Subset<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-5.png" width="600"></p>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-6.png" width="600"></p>

&ensp;branch는 Branch와 ALU Zero의 AND로 PCSrc를 결정: `(Branch & Zero) ? Target : PC+4` <br/>

&ensp;명령어별 "선 따라가기"<br/>
&ensp;(1) `lw rt, imm(rs)` — 메모리→레지스터<br/>
1. Fetch: PC→IMEM, 명령 획득, PC+4 계산
2. Decode: rs, rt 읽기, imm 부호확장
3. Execute: ALUSrc=1 ⇒ Addr = R[rs] + signext(imm)
4. Memory: MemRead=1 ⇒ DataMem[Addr] 읽기
5. Write-back: MemtoReg=1, RegDst=0, RegWrite=1 ⇒ R[rt] ← DataMem[Addr]

&ensp;(2) `sw rt, imm(rs)` — 레지스터 → 메모리<br/>
&ensp;1~3 동일 (주소 계산)<br/>
&ensp;4. Memory: MemWrite=1 ⇒ DataMem[Addr] ← R[rt] (레지스터 쓰기 없음)<br/>

&ensp;(3) R-type `add rd, rs, rt` <br/>
* ALUSrc=0, RegDst=1, MemtoReg=0, RegWrite=1
* ALU = R[rs] + R[rt], R[rd] ← ALU

&ensp;(4) `beq rs, rt, off` — 조건분기<br/>
* ALUSrc=0, ALUOp=SUB로 비교 → Zero 생성
* Branch=1이면 PCSrc = Branch & Zero 참이면 PC ← (PC+4) + (signext(off)<<2), 거짓이면 PC+4

Logic Design Conventions
=====

* edge triggered 방식: 
1. 사이클 시작 시 상태요소(PC, 레지스터, 메모리) 값을 읽고
2. 그 값이 조합논리(ALU/MUX/Adder) 를 거쳐
3. 사이클 끝 에지에서 다음 상태요소에 기록

&ensp;그래서 레지스터 파일은 동시에 2읽기/1쓰기 가 가능한 구조를 씀:<br/>
* 읽기는 조합 논리처럼 즉시 출력
* 쓰기는 클록 에지에서만 반영

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-7.png" width="600"></p>

&ensp;Register file 내부<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-8.png" width="600"></p>
<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-9.png" width="600"></p>

&ensp;출력(읽기) 경로<br/>
* 각 레지스터의 값들이 2개의 큰 MUX로 들어감
* Read register number 1/2 신호가 각각 하나를 선택 → Read data 1/2로 출력

<p align="center"><img src="/assets/img/Computer Architecture/chapter4. The processor/4-1-10.png" width="600"></p>

&ensp;입력(쓰기) 경로<br/>
* Write register 번호를 n→2ⁿ 디코더에 넣으면 선택된 한 레지스터 라인만 활성
* 그 레지스터의 D FF에 쓰기 데이터가 들어가고, Write(RegWrite)가 1일 때 클록 에지에서 저장

&ensp;핵심: 읽기=멀티플렉싱, 쓰기=디코딩<br/>