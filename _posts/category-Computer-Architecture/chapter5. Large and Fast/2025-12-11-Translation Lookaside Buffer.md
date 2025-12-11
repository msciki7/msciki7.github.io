---
title: "chapter 5-6. Translation Lookaside Buffer"
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

TLB가 필요한 이유
====

&ensp;CPU가 virtual address를 사용하면 일반적으로 “메모리를 두 번” 접근해야 한다:<br/>
1. Page table에서 PPN(물리 페이지 번호)을 찾기
2. 실제 데이터를 읽기

&ensp;주소변환 비용이 너무 큼 → 성능↓<br/>

&ensp;해결책: TLB<br/>
&ensp;TLB(Translation Lookaside Buffer)는 ‘주소 변환 캐시’다.<br/>
* 최근 사용된 VPN→PPN 매핑을 저장해둔다
* TLB hit이면 page table까지 갈 필요 없음
* 하드웨어 캐시처럼 동작하지만 페이지 테이블 전용

&ensp;TLB Typical Parameters<br/>

| 항목           | 값              |
| ------------ | -------------- |
| TLB size     | 16–512 entries |
| Hit time     | 0.5–1 cycle    |
| Miss penalty | 10–100 cycles  |
| Miss rate    | 0.01–1%        |

&ensp;TLB miss penalty가 큰 이유? → page table lookup도 메모리 접근이기 때문.<br/>

Address Translation with TLB
====

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-6-1.png" width="500"></p>

&ensp;TLB → Page Table → Physical memory 전체 흐름<br/>

&ensp;주소 변환 흐름 요약<br/>
&ensp;1. CPU가 VA 생성 → VPN 추출<br/>
&ensp;VPN이 TLB에 들어가서 검색됨.<br/>

&ensp;2. TLB Hit ⭢ 가장 빠름<br/>
&ensp;TLB가 바로 PPN을 반환 → physical memory 접근<br/>

&ensp;3. TLB Miss ⭢ Page Table 보기<br/>
&ensp;Page Table에서<br/>
* valid=1 → PPN 찾기 → TLB에 엔트리 추가 (replacement 발생 가능)
* valid=0 → page fault → 디스크에서 페이지 가져와 업데이트

&ensp;TLB Miss는 곧 Page Fault가 아니다. TLB miss → page table에서 valid=1이면 문제 없음. page fault → valid=0일 때 발생<br/>

Intrinsity FastMATH TLB
====

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-6-2.png" width="500"></p>

&ensp;핵심 구성요소<br/>

&ensp;Fully Associative TLB<br/>
&ensp;→ 어떤 VPN도 어떤 TLB 엔트리에 들어갈 수 있음<br/>
&ensp;→ TLB는 캐시보다 크기가 작아서 fully associative가 가능함<br/>

&ensp;각 TLB Entry 구성<br/>
* tag: VPN 상위 비트
* physical page number
* valid bit
* dirty bit
* 기타 metadata (LRU 등)

&ensp;VA → PPN 변환 후 Cache 접근 과정<br/>
1. TLB hit → PPN 가져옴
2. PPN + offset 결합해 physical address 생성
3. L1 cache에 접근
4. cache hit이면 바로 데이터 반환
5. miss면 memory 접근

Integrating Virtual Memory, TLBs, and Caches
====

&ensp;주소 접근 시 발생 가능한 5가지 케이스<br/>

| Case | Cache | TLB  | Virtual Memory(Page Table) | 결과                                 |
| ---- | ----- | ---- | -------------------------- | ---------------------------------- |
| (0)  | Hit   | Hit  | Hit                        | **Best case**. 바로 데이터 읽음           |
| (1)  | Miss  | Hit  | Hit                        | Cache miss만 발생 → 메모리 접근            |
| (2)  | Miss  | Miss | Hit                        | **TLB miss** (페이지는 메모리에 있음)        |
| (3)  | Miss  | Miss | Miss                       | TLB miss + Cache miss + Page fault |
| (4)  | Miss  | Hit  | Miss                       | Page fault                         |

&ensp;TLB miss와 Page fault는 다르다<br/>
* TLB miss = Page Table을 보면 해결됨
* Page fault = Valid=0 → 디스크 접근 필요

&ensp;Impossible 상태가 있는 이유<br/>
&ensp;예: TLB hit인데 virtual memory miss? → TLB는 valid 매핑만 가지고 있으므로 절대 불가능<br/>
&ensp;그래서 아래 조합이 불가능:<br/>
* cache hit + TLB miss + VM miss
* cache hit + TLB hit + VM miss

Example: Virtual Memory with TLB
=====

&ensp;조건 정리<br/>
&ensp;1) Virtual / Physical Address Space<br/>
* Virtual address space = 2¹¹ bytes
* Physical address space = 2¹⁰ bytes
* Page size = 2⁸ = 256 bytes → offset = 8bits → VPN = (11 - 8) = 3bits

&ensp;즉 VA = [3비트 VPN | 8비트 offset]<br/>

&ensp;2) Page Table<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-6-3.png" width="500"></p>

&ensp;Valid bit 1이면 메모리에 존재 → PPN 사용 가능<br/>
&ensp;Valid bit 0이면 page fault<br/>

&ensp;3) 초기 TLB 상태<br/>
&ensp;TLB는 fully associative (어디든 저장 가능)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-6-4.png" width="500"></p>

&ensp;현재 TLB에는 VPN = 7만 저장되어 있음<br/>

&ensp;답<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-6-5.png" width="500"></p>

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-6-6.png" width="500"></p>

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-6-7.png" width="500"></p>

&ensp;**VA 6A8**<br/>
&ensp;Step 1. VPN 추출<br/>
&ensp;6A8(hex) → binary → VPN = 6<br/>

&ensp;Step 2. TLB hit?<br/>
&ensp;TLB에는 tag=7만 존재 → VPN=6은 없음 → TLB miss<br/>

&ensp;Step 3. Page Table 확인<br/>
&ensp;VPN=6 → valid=0 → Page Fault<br/>

&ensp;Step 4. Page Fault 처리<br/>
* 새로운 PPN 배정 (LRU physical page 순서에 따라 PPN=2 사용)
* Page Table 업데이트
* TLB 업데이트 (tag=6, PPN=2)

&ensp;Step 5. PA 생성<br/>
&ensp;PPN(2) | offset(A8) → 2A8<br/>

&ensp;**VA 700 → VPN=7**<br/>
&ensp;Step 1. TLB hit 여부<br/>
&ensp;TLB에 tag=7 있음 → TLB hit<br/>

&ensp;Step 2. Page fault?<br/>
&ensp;Page Table에서 VPN=7은 valid=1 → page fault 없음<br/>

&ensp;Step 3. PA<br/>
&ensp;PPN=3<br/>
&ensp;PA = 0x300<br/>

&ensp;**VA 3F4 → VPN=3**<br/>
&ensp;TLB miss<br/>
&ensp;TLB에 3 없음<br/>

&ensp;Page Table<br/>
&ensp;VPN 3 → valid=0 → page fault<br/>

&ensp;새 PPN=1 할당<br/>
&ensp;PA = 1F4<br/>

&ensp;**VA 4E0 → VPN=4**<br/>
&ensp;TLB miss<br/>
&ensp;Page Table valid=1 → resident page → TLB miss지만 page fault 아님<br/>

&ensp;PPN=0<br/>
&ensp;PA=0E0<br/>

&ensp;**VA 76C → VPN=7**<br/>
&ensp;TLB hit (tag=7 있음)<br/>
&ensp;PA = (PPN=3)6C → 36C<br/>

&ensp;**VA 008 → VPN=0**<br/>
&ensp;TLB miss<br/>
&ensp;Page table valid=0 → page fault<br/>

&ensp;PPN=2<br/>
&ensp;PA=208<br/>

Handling TLB Misses and Page Faults
====

&ensp;핵심 두 가지 상황<br/>
&ensp;1. TLB miss<br/>
* resident page(=Page Table valid=1)이면 → TLB entry 생성 후 재시도
* non-resident page(valid=0)이면 → page fault exception 발생

&ensp;Page Fault<br/>
* OS 개입 필요
* 디스크에서 페이지 읽어옴
* Page Table 업데이트
* TLB도 업데이트
* faulting instruction 재실행

Page Fault Handling 과정
-----

1. Page Table에서 디스크 위치 확인
2. Victim frame 선택 (LRU 등) Dirty면 디스크로 write-back
3. 디스크에서 새 페이지 읽기
4. Page Table 업데이트 (valid=1, PPN=frame번호)
5. ERET 실행 → kernel에서 user mode로 복귀
6. faulting instruction 재실행

