---
title: "chapter 5-3. Set-Associative Cache"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-11-23
last_modified_at: 2025-11-24
---

Measuring and Improving Cache Performance
=====

# 캐시 성능 측정 & 향상 방법

&ensp;캐시 성능을 향상시키는 두 가지 기술<br/>
&ensp;(1) Using Associativity<br/>
* Direct-mapped cache는 conflict miss가 많다.
* Associative(2-way, 4-way …)로 올리면 같은 set 안에서 여러 block을 저장할 수 있으므로 → Conflict miss가 감소함.
* BUT, associativity가 높아지면 하드웨어 복잡도 증가 & hit time이 약간 증가.

&ensp;(2) Multilevel Caching<br/>
* L1은 작고 빠름 (hit는 빠르지만 miss penalty는 큼 → DRAM 접근)
* L2, L3는 크고 느림
* 여러 계층이 존재하면 L1 miss penalty를 줄일 수 있음 (L1 miss → L2 hit이면 DRAM까지 안 가도 됨)

&ensp;CPU time with cache<br/>
&ensp;공식<br/>
```math
CPU time=(CPU execution cycles+Memory-stall cycles)×Clock cycle time
```

* CPU execution cycles: 캐시 hit일 때 정상적으로 실행되는 사이클
* Memory-stall cycles: 캐시 miss 때문에 기다리며 낭비한 사이클

&ensp;메모리 스톨의 주요 원인: Cache miss<br/>

# Memory Stalls

&ensp;1) Memory-stall clock cycles<br/>
```math
Memory-stall clock cycles = read-stall cycles+write-stall cycles
```

&ensp;CPU는 read/write 모두에서 미스가 발생하면 기다린다.<br/>

&ensp;2) Read-stall cycles<br/>
```math
Read-stall cycles = (reads/program)×read miss rate×read miss penalty
```

* 프로그램 전체에서 read 몇 번 하는지
* 그 중 몇 %가 miss인지
* miss가 발생하면 penalty(= miss 처리 시간)

&ensp;읽기(read)는 보통 CPU 수행에 직접적인 영향을 주므로 더 중요한 부분<br/>

&ensp;3) Write-stall cycles<br/>
```math
Write-stall cycles = (writes/program)×write miss rate×write miss penalty+write buffer stalls
```

&ensp;왜 write는 항이 더 많을까?<br/>
&ensp;Write buffer stalls<br/>
* Store 명령을 모두 메모리에 직접 쓰면 느리기 때문에 → CPU는 write buffer를 사용하여 임시 저장
* buffer가 꽉 차면 CPU는 stall 발생

&ensp;Simplification (단순화)<br/>
&ensp;Assumptions (암기)<br/>
1. read miss penalty = write miss penalty
2. read miss rate = write miss rate
3. write buffer stall 무시 가능

&ensp;→ read와 write를 동일 취급해 계산을 단순화<br/>

&ensp;Memory-stall clock cycles 단순화 과정<br/>
&ensp;전체 식<br/>

$ Memory-stall cycles = \frac{Memory accesses}{Program} \times \frac{Misses}{Memory access} \times Miss penalty$

&ensp;이를 다시:<br/>

$= \frac{Instructions}{Program} \times \frac{Memory accesses}{Instruction} \times \frac{Misses}{Memory access} \times Miss penalty$


## 최종 정리

$= IC\times \frac{Memory accesses}{Instruction} \times Miss rate \times Miss penalty$

# Harvard Architecture RISC 캐시 스톨 계산

&ensp;Harvard 구조 = Instruction cache와 Data cache가 분리되어 있음.<br/>

$IC \times (Instruction miss cycles + Data miss cycles) \times Miss penalty$

&ensp;자세히<br/>

$IC \times (1 \times I-miss rate + frequency of mem instructions \times D-miss rate) \times Miss penalty$

* 명령어 fetch는 매 instruction마다 1번 발생
* 메모리 참조 load/store 명령은 전체 중 일부 비율만 사용됨

&ensp;그래서<br/>

$IC \times (1 \times I-miss rate + frequency of mem instructions \times freq of mem ref) \times Miss penalty$ 

## Example – Cache Performance 계산

&ensp;문제 조건<br/>
* I-cache miss rate = 2%
* D-cache miss rate = 4%
* Load/store 비율 = 36%
* Miss penalty = 100 cycles
* Base CPI = 2

&ensp;풀이 과정<br/>
1. Instruction miss cycles: $I \times 2\% \times 100 = 2.00I$
2. Data miss cycles: $I \times 36\% \times 4\% \times 100 = 1.44I$
3. Total stall cycles: $2.00I + 1.44I = 3.44I$
4. CPI with stalls: stall cycles를 CPI로 환산 → $CPI = 2 + 3.44 = 5.44$
5. Perfect cache일 때 속도 향상: Perfect cache = stall 없음 → CPI = 2

&ensp;성능 향상률: $\frac{5.44}{2} = 2.72$

&ensp;결론: 캐시 미스가 모두 사라지면 약 2.7배 빨라짐.<br/>

&ensp;When CPI = 1일 때 speedup<br/>

$Speedup = \frac{1 + 3.44}{1} = 4.44$

&ensp;CPI가 1인 CPU에서는 캐시 성능 개선 효과가 훨씬 커진다.<br/>

Reducing Cache Misses by More Flexible Placement of Blocks
======

&ensp;3가지 Placement Scheme 전체 설명<br/>
&ensp;1. Direct Mapping<br/>
* 메모리 특정 block → 캐시의 딱 하나의 위치에만 저장 가능
* 1:1 대응

&ensp;예: block #3 → 캐시 index 3 위치에만 저장됨(다른 곳 절대 못 감)<br/>
&ensp;장점: 빠르고 구조가 단순<br/>
&ensp;conflict miss 많음<br/>

&ensp;2. Set-associative Mapping<br/>
* 블록이 하나의 set으로 매핑되는데 
* 그 set 안에서는 여러(= n-way)위치 중 아무 곳이나 저장 가능

&ensp;예: 4-way set associative = 한 set 안에 block 4개 저장 가능 → 충돌이 발생해도 빈 자리 있으면 넣을 수 있음<br/>

&ensp;3. Fully Associative Mapping<br/>
* 블록이 캐시 어디에나 들어갈 수 있음
* 제한 없음

&ensp;장점: conflict miss = 0<br/>
&ensp;단점: 모든 tag를 동시에 비교해야 함 → CAM 필요 → 하드웨어 복잡 & 비쌈<br/>

&ensp;Direct Mapped Cache 상세<br/>
* 각 메모리 block은 캐시의 단 하나의 idex로만 감
* 빠르지만 miss 많음

&ensp;Fully Associative Cache 상세<br/>
* 어디든 저장 가능한 캐시
* block 배치를 가장 유연하게 함 → conflict miss 거의 없음

&ensp;하지만 단점:<br/>
* 모든 태그를 병렬 비교해야 → CAM(content-addressable memory) 필요
* 구현비용 ↑

# n-Way Set Associative Cache 상세 설명

&ensp;Fully associative와 direct의 중간 단계라고 생각하면 된다.<br/>
&ensp;1) 각 block은 1개의 set으로 매핑되지만, set 안에서는 n개의 위치 중 어느 곳에나 저장 가능<br/>
* set index는 여전히 필요
* set 내부에서는 자유롭게 배치 가능

&ensp;2) Set size = n (ways)<br/>
&ensp;각 set 저장 가능한 블록 수 = n<br/>
&ensp;총 set 개수: $\frac{\text{cache size}}{n}$

&ensp;3) 매핑 방식<br/>
* 메모리 block → index bits를 사용해 단 하나의 set으로 매핑됨
* set 내부(n개의 ways) 중 아무 곳에나 저장됨

&ensp;4) hit 판단<br/>
* 그 set 안의 모든 way(즉 n개의 블록)를 태그 비교해야 함

&ensp;5) Associativity 증가 효과<br/>
* n 증가 → miss rate 감소
* n 증가 → hit time 증가 (비교해야 할 블록 수 증가)
 
# Three Block Placement Policies

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-1.png" width="500"></p>

&ensp;1) Direct mapped<br/>
* block #4만 index 4으로 간다.
* 오로지 한 칸에만 들어갈 수 있음
* Search 회살표도 하나

&ensp;block 4 → cache line 4, miss 나면 덮어씀<br/>

&ensp;2) Set associative<br/>
&ensp;예시는 2-way set associative라고 보면 됨<br/>
* block들은 특정 set으로 매핑됨
* 예: block X는 set 1로 매핑
* set 1에는 두 칸(way 0, way 1)이 있음
* 둘 중 어느 곳이든 갈 수 있음
* 검색 시 → set 1 안의 두 태그를 모두 비교함 (화살표 2개)

&ensp;3) Fully associative<br/>
* Tag 비교 화살표가 모든 칸으로 향함
* 캐시 전체를 뒤져서 match 찾음
* 가장 유연하지만 가장 복잡

&ensp;8-Block Cache Example<br/>
&ensp;8개의 블록으로 구성된 캐시를 associativity 별로 어떻게 표현하는지 보여주는 예시이다.<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-2.png" width="500"></p>

&ensp;Case 1 — Direct-mapped (1-way)<br/>
* cache = 8 blocks
* set 수 = 8
* 각 set(=index)은 block 1개만 저장 → associativity = 1 (1-way)<br/>
&ensp;그림 설명:<br/>
* Block 0, 1, 2 … 7이 각각 1칸씩 갖고 있음
* Tag + Data 형식

&ensp;Case 2 — 2-way set associative<br/>
* set당 2개 block(way)
* 총 block 수가 8개 → set 수 = 8 / 2 = 4 → sets = 0, 1, 2, 3

&ensp;그림 설명:<br/>
* 각 set 안에 “Tag, Data”가 2개씩
* set 0 안에 block 2개 저장 가능

&ensp;Case 3 — 4-way set associative<br/>
* set당 4개 block
* 총 8 blocks → set 수 = 8 / 4 = 2 → sets = 0, 1

&ensp;그림 설명:<br/>
* set당 4개의 tag/data pair

&ensp;Case 4 — 8-way (Fully associative)<br/>
* set당 8 blocks
* set 수 = 1

&ensp;fully associative = 전체 캐시를 1개의 set으로 본 것과 동일<br/>

| Mapping 방식            | Block이 배치될 수 있는 위치 | Miss rate | Hardware cost |
| --------------------- | ------------------ | --------- | ------------- |
| Direct mapped         | 단 1개의 위치           | ❌ 가장 높음   | ✅ 가장 저렴       |
| n-way set associative | 특정 set 안의 n개 위치    | 중간        | 중간            |
| Fully associative     | 모든 위치              | ✅ 가장 낮음   | ❌ 가장 비쌈       |

# Conflict Misses (충돌 미스)

&ensp;Conflict Misses & Ping-Pong Effect<br/>
&ensp;Reference string: 0,4,0,4,0,4,0,4<br/>
&ensp;총 8번 메모리 접근 → 모두 miss (8 misses)<br/>

&ensp;왜 이런 일이 벌어질까?<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-3.png" width="500"></p>

&ensp;Direct-mapped cache는 메모리 블록 → 캐시의 “단 하나의” 위치(index)에만 매핑됨<br/>
&ensp;예를 들어<br/>
* 주소 0 → index 0
* 주소 4 → index 0 (같은 index!)

&ensp;메모리 주소 0과 4가 같은 index에 매핑됨 → 서로 덮어씀<br/>

&ensp;3) 그림 해석<br/>
&ensp;각 작은 상자는 캐시에 단 하나의 line(index)이 있는 direct-mapped 캐시라고 보면 됨<br/>
1. 0 접근 → 비어있음 → miss → 캐시에 Mem(0) 저장
2. 4 접근 → index 동일 → 기존 Mem(0) 강제로 삭제 → miss → Mem(4) 저장
3. 0 접근 → Mem(4) 때문에 없어짐 → miss → Mem(0) 저장
4. 4 접근 → Mem(0) 삭제됨 → miss → Mem(4) 저장

&ensp;이게 무한 반복 = Ping-Pong Effect<br/>

&ensp;4) Ping-pong effect 정의<br/>
>두 메모리 블록이 같은 캐시 블록에 매핑될 때 하나가 저장되면 다른 하나가 반드시 쫒겨나가는 현상

&ensp;Direct mapping에서만 발생, Set-associative에서는 해결됨.<br/>

# 2-Way Set-Associative Cache 구조

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-4.png" width="500"></p>

&ensp;1) Set은 2개 (set 0, set 1)<br/>
&ensp;각 세트는 2개의 ways(=2개의 line)를 가짐<br/>
&ensp;set마다 2개의 저장공간이 존재<br/>

```yaml
set 0: [way 0] [way 1]
set 1: [way 0] [way 1]
```

&ensp;2) 주소의 index bits에 따라 set이 결정됨<br/>
&ensp;오른쪽 주소들(000, 001, 010...)에서<br/>
* 파란색 박스 = index bits
* 빨간색/초록색 박스 = 각 블록이 어느 set에 들어갈 수 있는지 보여주는 것

* 어떤 주소는 set 0으로
* 어떤 주소는 set 1으로 두 set 안에서 여러 block이 공존할 수 있음

&ensp;Direct mapping처럼 무조건 "하나의 위치"만 가능하지 않고, 2개의 선택지가 생긴다.<br/>

# Removing Conflict Misses

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-5.png" width="500"></p>

&ensp;1) 첫 번째 접근: 0 → miss<br/>
* set = 0
* tag = 000
* way 0에 저장

&ensp;2) 다음 접근: 4 → miss<br/>
* set = 0
* tag = 010
* way 1에 저장

&ensp;2-way이므로 비어있는 장소가 존재<br/>

&ensp;이제 캐시는 다음처럼 됨:<br/>
```yaml
set 0:
  way0: tag=000 → Mem(0)
  way1: tag=010 → Mem(4)
```

&ensp;0과 4가 같은 set에 매핑되지만 두 개의 ways가 있으므로 둘 다 공존 가능<br/>

&ensp;3) 세 번째 접근: 0 → hit<br/>
&ensp;Mem(0)이 그대로 있을 것 → hit<br/>
&ensp;4) 네 번째 접근: 4 → hit<br/>
&ensp;Mem(4)도 그대로 존재 → hit<br/>
&ensp;최종 결과<br/>

| 방식                        | 총 miss 수                             |
| ------------------------- | ------------------------------------ |
| Direct-mapped             | 8 misses                             |
| **2-way set associative** | **2 misses (처음 0,4만 miss, 나머지 hit)** |

&ensp;2-way set associative는 충돌 미스(conflict miss)를 획기적으로 줄인다.<br/>
&ensp;이유:<br/>
* 같은 index로 매핑되는 블록들이
* 서로 다른 ways 안에서 공존할 수 있기 때문.

&ensp;따라서 ping-pong effect 해결됨<br/>

# Example: Misses and Associativity in Caches

&ensp;캐시 구성<br/>
* 총 블록 수 = 4개
* 비교할 캐시 3가지
1. Direct-mapped
2. 2-way set associative
3. Fully associative
* Replacement policy = LRU
* Access sequence = (0, 8, 0, 6, 8)

&ensp;목표: 각 캐시 구조별 miss 개수를 계산<br/>

## Direct Mapped (5 misses)

&ensp;매핑 방식<br/>
&ensp;direct-mapped → index = (block address mod 4)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-6.png" width="500"></p>

&ensp;0, 4, 8 모두 index 0으로 가는 게 중요 → conflict 잔치 남<br/>

&ensp;전체 추적 테이블<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-7.png" width="500"></p>

&ensp;결론<br/>
* block 0 ↔ 8가 계속 같은 index 0에 매핑 → Ping-Pong 발생
* 총 5 misses
* hit가 단 1번도 없음

## 2-Way Set Associative (4 misses)

&ensp;set 개수<br/>
* 총 block = 4
* associativity = 2-way → set 수 = 4 / 2 = 2 → set index = (block address mod 2)

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-8.png" width="500"></p>

&ensp;모든 주소(0, 4, 6, 8)가 다 set 0에 몰린다.<br/>
&ensp;단, set 0 안에는 way가 2개 있으므로 두 블록까지는 공존 가능 → 하지만 3번째 블록부터는 LRU로 하나씩 쫓겨남<br/>

&ensp;추적 테이블<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-9.png" width="500"></p>

&ensp;결론<br/>
* hits: 1
* misses: 4

&ensp;Direct-mapped보다 좋아졌지만 set 0 안에 모든 block이 몰려서 conflict가 여전히 일부 존재.<br/>

## Fully Associative (3 misses)

&ensp;Fully associative → 모든 블록을 캐시 어디에나 저장 가능<br/>
&ensp;conflict miss 없음, 오직 capacity 제한 + LRU만 고려하면 됨.<br/>

&ensp;추적 테이블<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-10.png" width="500"></p>

&ensp;결론<br/>
* misses: 3
* Direct → 2-way → Fully 순서대로 miss가 감소함

&ensp;Direct-mapped<br/>
* 위치가 1개라 충돌 많음
* block 0/8이 같은 index를 두고 계속 싸워서 전부 miss → 가장 성능 낮음

&ensp;2-way set associative<br/>
* 같은 set 안에서 2개의 공간이 있어 일부 공존 가능
* 하지만 block 0,8,6,4 모두 set 0에 몰리는 경우에는 여전히 conflict 발생 → miss 감소하지만 완벽하지는 않음

&ensp;Fully associative<br/>
* 어디든 들어갈 수 있으므로 conflict miss 0
* 오직 capacity가 문제가 됨 → miss 가장 적음

Large Degree of Associativity
====

&ensp;1) Associativity 증가 → miss rate 감소<br/>
* Direct-mapped에서는 conflict miss가 심함
* Associativity가 커질수록 같은 set 안에 여러 block이 공존 가능 → conflict miss 줄어듬, miss rate 감소

&ensp;2) 그러나 associativity를 크게 늘릴수록 "효과는 점점 작아짐"<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-11.png" width="500"></p>

&ensp;1→2-way 변화는 매우 큼(10.3→8.6%) 하지만 4→8-way 변화는 거의 없음(8.3→8.1%)<br/>

&ensp;Miss Rate vs Associativity<br/>
&ensp;그래프는 캐시 크기(1KiB, 2KiB, 4KiB, 8KiB…)와 associativity(1-way, 2-way, 4-way, 8-way)를 비교한 것<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-12.png" width="500"></p>

&ensp;모든 선의 공통점<br/>
&ensp;(1) 캐시 크기 증가 → miss rate 크게 감소<br/>
&ensp;(2) associativity 증가 → miss rate 감소<br/>

&ensp;핵심<br/>
* 캐시 크기를 늘리는 것이 miss rate 감소에 가장 효과적
* 그다음으로 associativity 증가가 효과 있음
* 하지만 associativity 증가의 효과는 크기가 커질수록 더 작아진다

# Locating a Block in the Cache

&ensp;주소 = (tag, index, offset)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-13.png" width="500"></p>

&ensp;Index<br/>
* 어느 set을 선택할지 결정
* 캐시의 "행 번호"에 해당

&ensp;Tag<br/>
* set 내부 n개의 way 중 어느 block이 맞는지 비교하는 용도
* 모든 ways와 병렬 비교

&ensp;Associativity를 2배로 늘리면?<br/> 
&ensp;n → 2n way 증가<br/>
1. 한 set에 block이 2배 들어감 → 비교해야 할 tag comparator 수도 2배 증가, 하드웨어 복잡도 증가
2. set 수가 절반으로 줄어듬 → 전체 캐시 크기는 동일하니까

&ensp;index 길이가 1bit 줄어듬, 대신 tag 길이가 1bit 길어짐<br/>

# 4-Way Set-Associative Cache (하드웨어 구조)

&ensp;구성 요소<br/>
1. 4개의 ways 각각
* Valid bit
* Tag
* Data 를 가지고 있음
2. index
* index로 하나의 set 선택 → 그 set의 4개 ways가 활성화됨
3. parallel tag compare
* 4개의 tag를 동시에 비교 → 하나라도 맞으면 Hit → 해당 way의 data 선택
4. 4-to-1 multiplexer
* 어떤 way에서 hit가 났는지를 결정해 데이터를 최종 출력

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-14.png" width="500"></p>

# Set-Associative Cache with 2ᵐ-Word Blocks

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-3-15.png" width="500"></p>

&ensp;Block offset<br/>
* block 안에서 어떤 word를 선택하는지
* offset bits 필요
    - word offset
    - byte offset

&ensp;index<br/>
* set 선택

&ensp;tag<br/>
* set 안에서 block을 식별

&ensp;핵심 구조<br/>
* 두 개의 words를 출력하는 예시
* 모든 word들을 읽고 multiplexers로 필요한 word 선택
* associativity가 있으므로 tag 비교는 n개 ways에서 동시에 수행됨