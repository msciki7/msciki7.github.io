---
title: "chapter 5-5. Virtual Memory"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: trues
use_math: true 
toc_sticky: true

date: 2025-12-11
last_modified_at: 2025-12-11
---

Virtual Memory가 필요한 이유
==== 

&ensp;진짜 RAM(물리 메모리)보다 더 큰 메모리를 프로그램이 쓰는 것처럼 보이게 하는 기술

* 물리 메모리는 작음 → 프로그램이 커도 실행되게 해야 함
* 그래서 “필요한 부분만” RAM에 올리고, 나머지는 디스크에 둠
* CPU는 “가상주소”를 사용하고, OS/하드웨어가 이를 “물리주소”로 바꿔줌 (=주소 변환)

Design Considerations
===

&ensp;**Virtual Memory의 가장 큰 문제: miss penalty가 너무 크다**

&ensp;Virtual Memory의 가장 큰 문제: miss penalty가 너무 크다<br/>

&ensp;그래서 다음을 최적화해야 함<br/>

1. Large Page Size
* 페이지가 너무 작으면 page fault 자주 발생
* 너무 크면 내부 단편화 증가
* 보통: 4KB~16KB, 최근 32KB~64KB
2. Page Fault Rate 줄이기
* 가능하면 페이지들을 메모리 어딘가에 다 넣을 수 있게 해야 함
* fully associative 배치가 이상적(하지만 하드웨어 비용 큼)
3. 똑똑한 소프트웨어 알고리즘 사용
* OS의 페이지 교체 알고리즘(LRU 등)이 성능을 좌우
4. Write-back
* 디스크 쓰기 너무 오래 걸리므로 write-through 절대 못 씀
* write-back 사용 → dirty page만 디스크에 기록

Virtual Address vs Physical Address
====

&ensp;CPU는 가상 주소(VA)를 만든다.<br/>
* 프로그램은 가짜 주소를 사용
* CPU는 이 주소를 내놓음

&ensp;OS + Hardware(TLB + Page Table)가 이를 "물리주소(PA)"로 변환<br/>
* RAM은 실제 물리주소 사용

Address Mapping
=====

&ensp;**CPU 가상주소 = (VPN, offset)**

```sql
| Virtual Page Number | page offset |
        (VPN)             (offset)
```

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-1.png" width="500"></p>

&ensp;변환과정<br/>
1. CPU가 VPN을 Page Table에 전달함
2. Page Table이 그 VPN이 실제 어디(PPN)에 있는지 찾음
3. physical page number(PPN) + 동일 offset을 합쳐서 물리주소 완성

&ensp;Offset은 변하지 않는다<br/>

Virtual Address = VPN || offset
-----

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-2.png" width="500"></p>

&ensp;1. 가상주소(VA)와 물리주소(PA)에서 offset은 항상 동일<br/>
&ensp;페이지 크기는 VA와 PA에서 동일하기 때문 → page offset 비트수는 주소변환과 무관하게 그대로 복사됨<br/>

&ensp;2. VPN만 PPN으로 치환된다<br/>
```sql
Virtual Address  (VPN | offset)
           ↓ Translation
Physical Address (PPN | offset)
```

&ensp;여기서 TLB, Page Table이 VPN → PPN 매핑 담당<br/>

&ensp;주소 변환 문제 나오면 반드시 이 순서로 풀기:<br/>
1. 페이지 크기 구하기 → offset 비트수 계산 (예: page size = 4KB = 2¹² → offset은 12비트)
2. 전체 주소 길이에서 offset을 뺀 나머지가 VPN이다 (예: 32비트 주소 → 32 - 12 = 20비트가 VPN)
3. Page Table/TLB에서 VPN → PPN 찾기
4. 물리주소 = (PPN || offset)

Placing a Page and Finding It Again
----

&ensp;Fully Associative Mapping (완전 연관 매핑) = 어떤 가상 페이지라도 원하는 어떤 물리 프레임에도 넣을 수 있음.

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-3.png" width="500"></p>

&ensp;설명<br/>
* Logical memory
    - 프로세스가 가진 가상 페이지: A, B, C, D, E, F, G, H
    - 번호는 "가상 페이지 번호(VPN)"
* Page Table
    - frame(=PPN): 해당 가상 페이지가 매핑된 물리 프레임 번호
    - valid bit: 1이면 RAM에 존재, 0이면 page fault
* Physical Memory
    - 프레임 번호 0~15
    - 그 안에 A, C, F 등이 올라가 있는 상태
    - 나머지는 디스크에 있음

&ensp;Fully associative mapping에서는 VPN이 어떤 PPN에도 배치될 수 있으며,
이 매핑 정보는 Page Table을 통해 검색한다.<br/>

&ensp;Page Table<br/>
&ensp;VPN → PPN 매핑을 저장하는 ‘큰 배열’<br/>
&ensp;각 프로세스는 자신만의 Page Table을 갖는다.<br/>

&ensp;PTE(Page Table Entry) 구성<br/>

| 항목                            | 설명                                    |
| ----------------------------- | ------------------------------------- |
| **PPN(physical page number)** | 가상 페이지가 실제 RAM에서 있는 위치                |
| **Valid bit**                 | 1이면 메모리에 존재, 0이면 디스크에 있음 → page fault |

&ensp;Page Table Register (PTR)<br/>
* CPU가 Page Table을 참조할 때 시작 주소(Base address)를 저장
* 모든 주소 변환 과정에서 PTR + VPN 으로 PTE 위치를 찾는다.

Address Translation Hardware
----

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-4.png" width="500"></p>

&ensp;핵심 값들<br/>
* Virtual address space = 2³² bytes
* Physical address space = 2³⁰ bytes
* Page size = 2¹² bytes → offset = 12비트

&ensp;변환 과정<br/>
&ensp;1. 가상주소(VA)를 VPN과 offset으로 나눈다<br/>
```sql
| VPN (상위 비트) | offset (하위 12비트) |
```

&ensp;2. Page Table에서 VPN을 인덱스로 사용<br/>
&ensp;PTR(VPN) → PTE를 찾음<br/>

&ensp;3. Valid bit 확인<br/>
* 0 → page fault
* 1 → 변환 계속

&ensp;4. PPN을 읽어옴<br/>
&ensp;5. 물리주소 구성<br/>
```scss
Physical Address = (PPN || offset)
```

Example: Page Table
----

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-5.png" width="500"></p>

&ensp;주어진 조건 정리<br/>
* Virtual Address Space = 64KiB = 2¹⁶ → 가상 페이지 개수 = 64KiB / 8KiB = 8개 → VPN = 3비트
* Physical Address Space = 32KiB = 2¹⁵ → 물리 페이지 개수 = 32KiB / 8KiB = 4개 → PPN = 2비트

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-6.png" width="500"></p>

* VPN 001 → 물리 프레임 11
* VPN 010 → 물리 프레임 00
* VPN 000 → valid=0이므로 page fault

Example: Address Translation
----

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-7.png" width="500"></p>

&ensp;Step 1: Virtual Address → 분해<br/>
```scss
Virtual Address bit = [VPN = 3비트] [Offset = 13비트]
```

&ensp;Step 2: VPN을 Page Table <index로 사용<br/>
&ensp;VPN = 101 이라고 하면 Page Table의 101번째 엔트리를 읽음<br/>

&ensp;Step 3: Valid bit 확인<br/>
* valid=1 → 변환 계속
* valid=0 → page fault

&ensp;Step 4: PPN을 가져온다<br/>
&ensp;예: PPN = 01<br/>

&ensp;Step 5: Physical Address = (PPN || offset)<br/>
&ensp;VPN은 쓰지 않고, PPN + offset을 합친다.<br/>

Example: Reference String
-----

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-8.png" width="500"></p>

1. 가상주소 → VPN, offset 분리
2. Page Table에서 VPN의 valid bit 확인
3. valid=1이면 PPN 가져와서 물리주소 생성
4. valid=0이면 page fault → 새 PPN 할당, Page Table 업데이트

&ensp;기본 구조<br/>
* VPN은 3비트
* PPN도 2비트 (물리 메모리 페이지 4개)
* page size는 2¹² = 4096B → offset은 12비트

```scss
[ 3-bit VPN ][ 12-bit page offset ]
```

&ensp;eference String 하나씩 분석<br/>
&ensp;1. 4010<br/>
&ensp;Step 1: VPN 추출<br/>
&ensp;4010(hex) → 이진 → VPN = 010<br/>

&ensp;Step 2: Page Table 확인<br/>
&ensp;VPN 010의 valid bit = 1<br/>
&ensp;PPN = 00<br/>

&ensp;Step 3: PA 생성<br/>
&ensp;PPN 00 + offset 01000010000 = → 0x0010

&ensp;page fault 없음<br/>

&ensp;2. 5100<br/>
&ensp;VPN = 010<br/>
&ensp;이미 PPN = 00 로 매핑됨.<br/>
&ensp;PA = 1100<br/>

&ensp;page fault 없음

&ensp;3. 0048<br/>
&ensp;VPN = 000<br/>
&ensp;Page Table에서 VPN=000 의 valid = 0<br/>
&ensp;→ page fault 발생<br/>
&ensp;Page Fault 처리:<br/>
* 새 physical frame 할당 (예: PPN = 10)
* Page Table 업데이트:

```
VPN 000 : valid=1, PPN=10
```

&ensp;4. 6F08<br/>
&ensp;VPN = 011<br/>
&ensp;valid = 0 → page fault<br/>
&ensp;새 PPN = 01 (예제에서 부여한 것)<br/>

```
VPN 011 : valid=1, PPN=01
```

&ensp;5. 33B4<br/>
&ensp;VPN = 011 (다시 접근)<br/>
&ensp;이제 valid=1 (앞에서 fault 처리됨)<br/>
&ensp;PPN = 01<br/>
&ensp;PA = 7384 (표에 그대로 있음)<br/>

&ensp;NOT page fault

&ensp;6. 1084<br/>
&ensp;VPN = 010<br/>
&ensp;이미 매핑된 페이지<br/>
&ensp;PPN = 00 → 5084<br/>

&ensp;NOT page fault

&ensp;7. AAB0<br/>
&ensp;VPN = 101<br/>
&ensp;valid=0 → page fault<br/>
&ensp;새 PPN = 01<br/>

```
VPN 101: valid=1, PPN=01
```

&ensp;8. 2770<br/>
&ensp;VPN = 001<br/>
&ensp;valid = 1<br/>
&ensp;PPN = 11<br/>
&ensp;PA = 6770<br/>

&ensp;NOT page fault<br/>

&ensp;Final Page Tabel<br/>

| VPN | Valid | PPN |                                       |
| --- | ----- | --- | ------------------------------------- |
| 000 | 1     | 10  |                                       |
| 001 | 1     | 11  |                                       |
| 010 | 1     | 00  |                                       |
| 011 | 0     | 01  | ← valid가 0인데 PPN 값이 있는 이유는 “과거의 값 유지” |
| 100 | 0     | 11  |                                       |
| 101 | 1     | 01  |                                       |
| 110 | 0     | 10  |                                       |
| 111 | 0     | 01  |                                       |

&ensp;1) Valid bit가 0이어도 PPN칸에 값이 남아있을 수 있다<br/>
&ensp;이건 하드웨어 구현 편의 때문이다.<br/>
&ensp;중요한 것은 valid bit가 0이면 PPN은 절대 사용하지 않는다는 것.<br/>

&ensp;2) valid bit만 보고 page fault 여부가 결정됨<br/>
&ensp;PPN이 뭔지는 중요하지 않다.<br/>

Page Fault Handling
=====

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-5-9.png" width="500"></p>

&ensp;Page Fault 발생 시 동작 순서<br/>
&ensp;Step 1. CPU가 메모리 접근 → Page Table valid bit = 0 발견<br/>
&ensp;page fault trap 발생 → OS에게 제어권 넘김<br/<>
&ensp;Step 2. OS는 “해당 페이지가 디스크 어디에 있는지” 찾음<br/>
&ensp;Step 3. 디스크에서 페이지를 읽어옴 (이 과정이 가장 느림)<br/>
&ensp;Step 4. 물리 메모리에서 “빈 프레임”을 찾음<br/>
* 빈 프레임 없으면 → page replacement 알고리즘 실행(LRU 등)

&ensp;Step 5. Page Table 업데이트<br/>
```scss
valid=1  
PPN = 새로 할당된 frame 번호
```

&ensp;Step 6. 문제가 일어난 명령어를 재시작(restart instruction)<br/>
&ensp;OS는 항상 그 명령을 다시 실행할 수 있어야 함.<br/>