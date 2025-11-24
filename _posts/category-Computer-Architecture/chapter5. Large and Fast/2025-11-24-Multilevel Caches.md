---
title: "chapter 5-4. Multilevel Caches"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: trues
use_math: true 
toc_sticky: true

date: 2025-11-24
last_modified_at: 2025-11-24
---

Choosing Which Block to Replace
====

&ensp;1. Replacement Algorithms (교체 알고리즘)<br/>
&ensp;Direct-mapped cache<br/>
* "선택"이라는 개념 없음
* block address → 특정 1개 index로 고정

&ensp;→ 그 index에 이미 있는 블록이 있으면 무조건 교체, Replacement policy 필요 없음<br/>

&ensp;Set-associative cache<br/>
* 한 set 안에 여러 block(ways)이 있으므로
* Miss 발생 시 그 set 안에서 어떤 block을 버릴지 선택해야 함

&ensp;→ Replacement algorithm 사용됨<br/>

&ensp;Fully associative cache<br/>
* 캐시 전체가 하나의 set
* 즉, 모든 block 중에서 하나를 선택해서 교체

&ensp;→ Replacement 정책 필요함<br/>

&ensp;2. LRU (Least Recently Used)<br/>
&ensp;정의: 가장 오래 사용되지 않은 block을 교체한다. (최근에 사용된 block은 남기도 오래된 block을 제거)<br/>

&ensp;왜 LRU를 사용할까?<br/>
&ensp;공간 지역성(Locality) 원리 때문<br/>
* 최근에 사용된 데이터는 앞으로도 다시 사용될 가능성이 높음 → 최근 사용된 block은 유지, 오래 안 쓴 block만 제거 = miss 감소

&ensp;LRU 구현 난이도<br/>
* 2-way set associative: 매우 간단
    - 1-bit reference bit(누가 더 최근인지)만 있으면 됨
* Associativity가 커질수록
    - 각 way의 "최근 사용 시간"을 기록해야 함 → 하드웨어 복잡, 비용 증가, 구현 어려움

# Example: Tag Size vs. Associativity

&ensp;문제 조건<br/>
* 주소 = 32비트
* 캐시 크기 = 4096 bytes = 2¹² bytes
* block size = 1 byte → offset = 0 bits (block 내부에 1byte 뿐)

&ensp;전체 block 수<br/>
&ensp;4096B / 1B = 4096 blocks = 4Ki blocks<br/>

&ensp;Direct mapped<br/>
* set = block = 4096
* index = log₂(4096) = 12 bits

&ensp;tag = 32 - 12 = 20 bits<br/>
&ensp;전체 tag 저장 공간 = 20 bits × 4096 = 80 Ki bits<br/>

&ensp;2-way associative<br/>
* set 수 = 4096 / 2 = 2048 = 2Ki sets
* index = log₂(2048) = 11 bits

&ensp;tag = 32 - 11 = 21 bits<br/>
&ensp;tag bits 총합 = 21 × 2048 = 84 Ki bits<br/>

&ensp;4-way associative<br/>
* set 수 = 4096 / 4 = 1024 = 1Ki sets
* index = log₂(1024) = 10 bits
* tag = 32 - 10 = 22 bits
* tag 저장 공간 = 22 bits × 1024 × 4 ways = 88 Ki bits

&ensp;Fully associative<br/>
* set = 1
* index = 0 bits
* tag = 32 bits 
    - tag 저장 공간 = 32 bits × 4096 blocks × 1 = 128 Ki bits

# Example: Tag Size vs. Associativity (2)

&ensp;block size = 16 bytes → offset = log₂(16) = 4 bits<br/>
&ensp;캐시 크기 = 4096 bytes = 4KiB<br/>
&ensp;block 수 = 4096 / 16 = 256 blocks<br/>

&ensp;1. Direct-mapped<br/>
&ensp;block = 256<br/>
&ensp;index = log₂(256) = 8 bits<br/>
&ensp;tag = 28 bits<br/>
&ensp;tag total bits = 28 × 256 = ≈5 Ki bits<br/>

&ensp;2. 2-way associative<br/>
&ensp;set = 128<br/>
&ensp;index = 7 bits<br/>
&ensp;tag = 32 − (7+4) = 21 bits<br/>
&ensp;총 tag bits = 21 × 128 × 2 = ≈5.25 Ki bits<br/>

&ensp;3. 4-way associative<br/>
&ensp;set = 64<br/>
&ensp;index = 6 bits<br/>
&ensp;tag = 32 − (6+4) = 22 bits<br/>
&ensp;총 tag bits = 22 × 64 × 4 = ≈5.5 Ki bits<br/>

&ensp;4. Fully associative<br/>
&ensp;index = 0 bits<br>
&ensp;tag = 32 − 4 = 28 bits<br/>
&ensp;tag bits = 28 × 256 × 1 = ≈7 Ki bits<br/>

&ensp;핵심 패턴<br/>
&ensp;Associativity 올릴수록<br/>
* set ↓
* index bits ↓
* tag bits ↑
* 저장해야 할 tag bits 전체 크기도 ↑ (fully가 가장 큼)

# Example: Tag Size vs. Associativity (3)

&ensp;Cache of 4096 blocks (= 2¹² blocks )<Br/>
* 여기서 4096 = block 개수를 의미함
* block size는 "4 words"
* word = 4 bytes → block size = 4 words × 4 bytes = 16 bytes

&ensp;Block offset 계산<br/>
&ensp;block size = 16 bytes → offset bits = log₂(16) = 4 bits<br/>
&ensp;주소에서 마지막 4비트는 block 내부 주소용(offset)<br/>

&ensp;1. Direct mapped (1-way)<br/>
* set 수 = block 수 = 4096 = 4Ki
* index bits = log₂(4096) = 12 bits
* tag bits: 32(주소 길이) − index(12) − offset(4) = 16 bits
* Tag 저장 공간: tag bits × block 수 = 16 bits × 4096 ≈ 66 Kbits

&ensp;2. 2-way set associative<br/>
* set 수: 4096 blocks / 2 ways = 2048 sets = 2Ki sets
* index bits = log₂(2048) = 11 bits
* tag bits: 28 − 11 = 17 bits
* tag 저장 공간: 2 ways × 2048 sets × 17 bits = 68K bits ≈ 70K bits

&ensp;3. 4-way set associative<br/>
* set 수: 4096 blocks / 4 = 1024 sets = 1Ki set
* index bits = log₂(1024) = 10 bits
* tag bits: 28 − 10 = 18 bits
* tag 저장 공간: 4 ways × 1024 sets × 18 bits = 72K bits ≈ 74K bits

&ensp;4. Fully associative<br/>
* set = 1개
* index bits = 0
* tag = address bits − offset bits = 32 − 4 = 28 bits

```
tag = 28 × 4Ki × 1 = 112Ki bits = 115K bits
```

* fully associative일 때 "blocks = ways"
* 4096개의 ways가 있으므로 → tag storage = 4096 × 28 bits <br/>
&ensp;= 114688 bits ≈ 112 Ki bits = 115 Kbits<br/>

| Associativity | Sets | Index bits | Tag bits | Tag storage |
| ------------- | ---- | ---------- | -------- | ----------- |
| 1-way         | 4096 | 12         | 16       | 66 Kbits    |
| 2-way         | 2048 | 11         | 17       | 70 Kbits    |
| 4-way         | 1024 | 10         | 18       | 74 Kbits    |
| Fully         | 1    | 0          | 28       | 115 Kbits   |

&ensp;핵심 개념<br/>
&ensp;Associativity ↑<br/>
* → set 개수 ↓
* → index bits ↓
* → tag bits ↑
* → 전체 tag 저장 공간 ↑ (fully associative가 가장 큼)

&ensp;block size가 커질수록<br/>
* → offset bits ↑
* → tag bits ↓

Multilevel Cache
=====

&ensp;개념<br/>
&ensp;Primary cache (L1)<br/>
* CPU 바로 옆 (on-chip)
* 목표: hit time 최소화
* 작고 빠름
* block size도 작음 → miss penalty 작게 유지

&ensp;Secondary cache (L2)<br/>
* L1보다 조금 멀리, 그래도 on-chip/next to chip
* 목표: L1 miss penalty 줄이기
* L1이 miss 날 때만 접근
* 크고 느리고 associative 높음 → miss rate 낮음

&ensp;예제: Multilevel Cache 성능 계산<br/>
&ensp;CPU, Memory 정보<br/>
* Clock rate = 4 GHz
* 1 cycle = 1 / 4 GHz = 0.25 ns
* CPI(base) = 1.0
* Memory access time = 100 ns (L1 miss → 메모리 접근 비용)
* L1 miss rate = 2%
* L2 miss rate = 0.5%
* L2 access time = 5 ns

&ensp;1-level cache만 사용할 때<br/>
&ensp;L1 miss penalty = 메인 메모리 접근 비용<br/>

$Miss penalty = \frac{100ns}{0.25ns} = 400 cycles$

&ensp;Total CPI<br/>

$CPI = 1 + (0.02 \times 400) = 1 + 8 = 9.0$ 

&ensp;L1 + L2 (2-level cache) 사용할 때<br/>
&ensp;1. L1 miss → L2 access (5 ns)<br/>

$L1 miss penalty = \frac{5ns}{0.25ns} = 20 cycles$

&ensp;→ 이것은 "L1 miss인데 L2 hit"인 경우만 적용됨<br/>
&ensp;2. L2 miss → Memory access (100 ns)<br/>
&ensp;400cycles<br/>
&ensp;3. 총 CPI 구성<br/>

$CPI = 1 + Primary stalls + Secondary stalls$

&ensp;Primary stalls (L1 miss → L2 hit)<br/>

$2\% \times 20 = 0.4$

&ensp;Secondary stalls (L2 miss → memory)<br/>
&ensp;전체 miss rate = global miss rate = 0.5%<br/>

$0.5\% \times 400 = 2.0$

&ensp;Total CPI<br/>

$CPI = 1 + 0.4 + 2.0 = 3.4$

&ensp;Speedup<br/>
&ensp;원래 1-level → CPI = 9.0<br/>
&ensp;2-level → CPI = 3.4<br/>

$Speedup = \frac{9.0}{3.4} \approx 2.6$

&ensp;Primary vs Secondary Cache 설계 철학<br/>

| Cache        | 무엇을 목표로?      | 왜?                                    |
| ------------ | ------------- | ------------------------------------- |
| **L1 cache** | hit time 최소화  | L1은 CPU가 바로 접근 → 1 cycle 늘어나도 성능 저하 큼 |
| **L2 cache** | miss rate 최소화 | L1 miss penalty가 수십~수백 cycle이라 치명적    |

# Design Details

&ensp;L1 cache 특징<br/>
* 작고 빠름
* associativity 낮음 (2~4-way)
* block size 작음 → miss penalty 줄임

&ensp;L2 cache 특징<br/>
* 큼 (수백 KB ~ 수 MB)
* associativity 크고 block size 큼 → miss rate 낮추기
* hit time 커도 상관 없음 (CPU와 pipeline 영향 적음)

# 실제 머신의 캐시 구조

| 레벨 | Intel Nehalem  | AMD Barcelona  | 특징                  |
| -- | -------------- | -------------- | ------------------- |
| L1 | 32KB I, 32KB D | 64KB I, 64KB D | 매우 빠르며 4~8-way      |
| L2 | 256KB          | 512KB          | 중간 크기, 8~16 way     |
| L3 | 8MB            | 2MB            | 공유 cache, 16~32 way |

&ensp;공통점<br/>
* L1: 작고 빠름, hit time 최적화
* L2/L3: 크고 느림, miss rate 최적화
* Write policy: 대부분 write-back + write-allocate

&ensp;공식 정리<br/>
&ensp;L1 miss penalty: $L1 MP = \frac{L2 access time}{cycle time}$ <br/>
&ensp;Global miss penalty: $L2 MP = \frac{Memory access time}{cycle time}$ <br/>
&ensp;Total CPI: $CPI = Base CPI + (L1 miss rate \times L1 MP) + (L2 miss rate \times L2MP)$  <br/>

Summary: Improving Cache Performance
====

&ensp;1. Reduce the hit time(= hit 되는 경우를 더 빠르게 만들기)<br/>
&ensp;Smaller cache (작은 캐시)<br/>
* 캐시가 작으면 index도 작고 탐색도 빠름
* L1은 hit time이 가장 중요 → 작게 만드는 것이 일반적

&ensp;Direct-mapped cache<br/>
* set associative보다 비교해야 하는 tag 수가 적다
* 병렬 비교 회로(Comparator) 적음 → 더욱 빠름
* 그래서 L1 cache 는 거의 항상 direct-mapped 또는 low-way

&ensp;Smaller blocks<br/>
* block size가 작으면 캐시 라인 읽기 시간도 짧음
* miss penalty 관점에서는 클 수도 좋지만, hit time만 보면 작을수록 빠름

&ensp;2. Reduce the miss rate(= miss가 덜 나도록 만들기)<br/>
&ensp;Bigger cache<br/>
* 용량이 크면 더 많은 working set을 담을 수 있음
* capacity miss 감소

&ensp;More flexible placement (higher associativity)<br/>
* direct → set associative → fully associative 순으로 유연
* conflict miss 감소
* 특히 2-way 이상이면 ping-pong conflict 크게 줄어듦

&ensp;Larger blocks (16~64 bytes typical)<br/>
* spatial locality 활용
* 한 번 읽을 때 주변 데이터 많이 가져오므로 miss rate 감소
* 단 너무 크면 conflict miss가 증가할 수 있음 → trade-off

&ensp;Victim cache<br/>
* 최근 교체된 block을 잠시 보관하는 작은 캐시
* conflict miss를 dramatic하게 줄여줌
* AMD Opteron L1 데이터 캐시에 실제 사용 (8 blocks)

&ensp;3. Reduce the miss penalty(= miss가 나더라도 덜 아프게 하기)<br/>
&ensp;Smaller blocks<br/>
* block size가 크면 메모리에서 가져오는 데 시간이 오래 걸림
* 작게 하면 penalty 감소

&ensp;Write buffer 사용<br/>
* write-back인 경우 더티 블록을 evict할 때 바로 메모리에 쓰지 않고 write buffer에 넣어서 쓰기 완료 기다리는 시간을 줄임
* write로 인한 stall 제거

&ensp;Read miss 시 write buffer/victim cache 확인<br/>
* 혹시 needed block이 write buffer나 victim cache에 있을 수도 있다.
* 존재하면 memory까지 안가도 되므로 penalty 절감

&ensp;Critical word first (large blocks일 때)<br/>
* 큰 block을 메모리에서 가져올 때 CPU가 당장 필요로 하는 word 먼제 전송
* CPU stall 최소화

&ensp;Use multiple cache levels (L2 cache)<br/>
* L1 miss penalty → L2 접근 비용(수 ns)
* 없으면 memory(100ns) 접근해서 penalty 엄청 커짐
* L2는 CPU clock rate와 분리해서 더 큰 block 사용 가능

&ensp;Faster backing store (memory bandwidth 향상)<br/>
* wider bus(더 넓은 버스 → 많은 byte 동시 전송 가능)
* memory interleaving
* DDR SCREAM 기술로 병렬 접근

Dependable Memory Hierarchy
=====

&ensp;1. Dependable Memory Hierarchy란?<br/>
&ensp;RAS (Reliability, Availability, Serviceability) 메모리나 시스템이 고장 없이, 오래, 쉽게 복구되도록 만드는 기술들을 뜻한다.<br/>


&ensp;Dependablity 정의<br/>
> a measure of a system’s availability, reliability, and its maintainability

* 얼마나 오래 정상 동작하는지
* 얼마나 고장이 적은지
* 고장 시 얼마나 쉽게 복구 가능한지<br/>
&ensp;를 모두 포함한 개념<br/>

&ensp;2. Failure 정의: 두 가지 상태<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-1.png" width="500"></p>

&ensp;시스템은 항상 두 상태 중 하나이다.<br/>
1. Service accomplishment = 정상 동작 (정상 서비스 제공)
2. Service interruption = 서비스 중단 (고장 발생)

&ensp;상태 전이<br/>
* Failure: state 1 → state 2
* Restoration: state 2 → state 1

&ensp;고장이 나면 Accomplishment → Interruption, 수리하면 Interruption → Accomplishment<br/>

&ensp;3. Reliability (신뢰성)<br/>
&ensp;Reliability는 얼마나 오랫동안 고장 업시 운영되는가의 정도<br/>
&ensp;Reliability = time to failure<br/>
&ensp;특정 시간 동안 fail 하지 않을 확률<br/>

&ensp;MTTF (Mean Time To Failure)<br/>
&ensp;고장까지 걸리는 평균 시간 → 얼마나 오래 갈 수 있는가?<br/>
* 수리가 불가능하거나 전체 교환하는 장치(예: 디스크, SSD)에서 자주 사용

&ensp;AFR (Annual Failure Rate)<br/>
&ensp;1년 동안 고장 날 확률<br/>
* MTTF가 1,000,000시간이면 AFR은 거의 0.876%

&ensp;MTBF (Mean Time Between Failure)<br/>
&ensp;$MTBF = MTTF + MTTR$ <br/>

* MTTR = Mean Time To Repair
* 고장을 포함해 고장 → 수리 → 다음 고장까지의 전체 주기

&ensp;예제: MTTF vs AFR (디스크 고장 예시)<br/
&ensp;100,000개의 디스크 중 1년 동안 몇 개가 고장나는가?<br/>
* MTTF = 1,000,000시간
* 1년 = 8760시간
* AFR = 8760 / 1,000,000 = 0.876%
* 디스크 수 = 100,000개
* 100,000 × 0.876% = 876개 고장
* 하루 평균 고장 디스크 ≈ 2.4개

&ensp;Availability (가용성)<br/>
&ensp;Availability는 정상 서비스 시간 / 전체 시간<br/>
&ensp;시스템이 얼마나 자주 정상 상태인가?<br/>
&ensp;공식:<br/>

$Abailability = \frac{MTTF}{MTTF + MTTR}$

&ensp;Availability 개선 방법<br/>
&ensp;(1) Reduce MTTR (수리 시간 줄이기)<br/>
* 더 좋은 진단 도구
* 자동화된 복구 시스템
* Hot-swapping 가능하게 만들기

&ensp;(2) Improve MTTF (고장까지 평균 시간 늘리기)<br/>
1. Fault avoidance
* 애초에 고장이 나는 설계를 없애기
* 내구성이 좋은 재료, 검증된 제조 공정
2. Fault tolerance
* 고장이 나도 서비스가 중단되지 않도록
* Redundancy(중복) 사용
* 예: RAID, ECC 메모리
3. Fault forecasting
* 언제 고장 날지 예측
* 사전 교체
* 예: 디스크 SMART 정보로 "조만간 고장" 예측


supplement
=====

<details>
<summary>📌 전체 흐름 요약</summary>

&ensp;캐시 미스 발생하면 CPU가 메모리에서 block을 가져와야 함 → 이때 쓰는 통로가 memory bus<br/>
&ensp;문제는 이 bus가 CPU보다 10배 느림.<br/>
&ensp;그래서 miss penalty가 큰 것!<br/>
&ensp;따라서 목표 = 메모리 → 캐시로 전달하는 bandwidth를 늘리는 것<br/>

&ensp;그 방법에는 크게 3개가 있음:<br/>
1. One-word-wide memory (기본구조 = 병렬성 없음, 가장 느림)
2. Wide memory (버스를 넓혀 병렬 전송)
3. Interleaved memory (메모리를 여러 뱅크로 나누어 병렬 접근)

</details>

## One-word-wide Memory

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-2.png" width="500"></p>

* 메모리에서 한 번에 1 word만 전송할 수 있음
* Cache block = 4 words → 4번 전송해야 함

&ensp;Assumptions (기본 가정)<br/>
* 주소를 bus로 보내는 데: 1 cycle
* DRAM 내부 접근 지연: 15 cycles
* 한 word 전송: 1 cycle
* block size = 4 words

&ensp;Miss Penalty 계산<br/>

$1 + 4 \times 15 + 4 \times 1 = 65 cycles$

1. 주소 전송 = 1
2. 각 word DRAM access = 15 × 4
3. 각 word 전송 = 1 × 4

&ensp;Bandwidth 계산<br/>
&ensp;한 miss 당 총 데이터 = 4 words = 16 bytes<br/>

$Bandwidth = \frac{16 bytes}{64 cycles} = 0.25 B/cycle$

&ensp;→ 아주 느림 (기본 baseline)<br/>

## Wide Memory (Bus를 넓혀 병렬 전송)

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-3.png" width="500"></p>

&ensp;개념<br/>
* 메모리 폭(width)을 늘려, 한 번에 여러 word 읽기
* 버스도 더 넓혀야 함
* block 전체를 거의 한 번에 가져올 수 있음

&ensp;Case 1: memory width = 2 words<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-4.png" width="500"></p>

&ensp;Miss penalty:<br/>
$1 + 2 × 15 + 2 × 1 = 33$

* 주소 = 1
* DRAM access 2번 필요 (2 word씩 읽기 때문)
* 전송도 2번

&ensp;Bandwidth<br/>
$\frac{16}{33} = 0.48 B/cycle$

&ensp;Case 2: memory width = 4 words<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-5.png" width="500"></p>

&ensp;Miss penalty:<br/>
$1 + 1 × 15 + 1 × 1 = 17$

&ensp;Bandwidth<br/>
$\frac{16}{17} = 0.94 B/cycle$

## Interleaved Memory (메모리는 넓히지 않고 은행(bank)만 분리)

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-6.png" width="500"></p>

* 메모리는 여러 뱅크(bank)로 나누어 독립적으로 동작
* bus 폭은 그대로 (narrow)
* 하지만 DRAM access latency(15 cycles)를 동시에 겪을 수 있음

&ensp;폭은 그대로지만 병렬로 동시에 읽음<br/>

&ensp;4-way interleaving<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-7.png" width="500"></p>

&ensp;Miss penalty:<br/>
$1 + 1 \times 15 + 4 \times 1 = 20$

* 주소 = 1
* 첫 DRAM latency = 15
* word 4개는 각 bank에서 병렬로 얻어오므로 전송만 4 cycles

&ensp;Bandwidth<br/>
$\frac{16}{20} = 0.8.0 B/cycles$

&ensp;Wide memory(4 words = 0.94)에는 못 미치지만 Wide memory(2 words = 0.48)보다 훨씬 좋음. One-word(0.25)보다는 압도적으로 빠름.<br/>

## The Hamming SEC/DED Code (해밍 코드)

&ensp;Richard Hamming<br/>
* 메모리에서 발생하는 비트 에러를 자동으로 검출·수정하기 위한 코드를 고안한 사람.
* 이 업적으로 튜링상 수상(1968).

&ensp;Hamming Distance(해밍 거리)<br/>
&ensp;해밍 거리: 두 비트 패턴 간에 서로 다른 비트의 개수<br/>

&ensp;해밍 거리와 오류 검출·수정 능력의 관계<br/>

| 해밍 거리 | 기능                                         |
| ----- | ------------------------------------------ |
| **2** | 단일 비트 오류 **검출** 가능 (예: parity code)        |
| **3** | 단일 비트 **수정** + 두 비트 **검출** 가능 (SEC/DED 기반) |

&ensp;해밍 거리를 3 이상으로 늘려야 에러 수정 가능<br/>

&ensp;Parity Code (패리티 코드)<br/>
&ensp;Even/Odd Parity<br/>
* Even parity: 전체 1의 개수를 짝수로 맞춤
* Odd parity: 전체 1의 개수를 홀수로 맞춤

&ensp;한계<br/>
* 1비트 오류는 검출 가능
* 그러나 2비트 오류는 검출 불가
* 어떠한 오류도 수정 불가

&ensp;Hamming Error Correction Code (ECC)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-8.png" width="500"></p>

&ensp;(1) 패리티 비트 위치<br/>
&ensp;위치는 2의 제곱수<br/>
&ensp;1, 2, 4, 8, …<br/>
&ensp;예: 12비트라면<br/>
&ensp;p1 = position 1<br/>
&ensp;p2 = position 2<br/>
&ensp;p4 = position 4<br/>
&ensp;p8 = position 8<br/>

&ensp;(2) 각 패리티 비트가 커버하는 범위 규칙<br/>


&ensp;패리티 비트 p_k는
&ensp;k 비트 간격으로 k개의 bit를 체크하고, 다시 k개 건너뛰는 패턴<br/>

&ensp;예: p1 → 1칸마다 번갈아 체크<br/>
&ensp;p2 → 2칸 체크, 2칸 스킵<br/>
&ensp;p4 → 4칸 체크, 4칸 스킵<br/>
&ensp;p8 → 8칸 체크, 8칸 스킵<br/>

&ensp;그래서 표가 X와 공백으로 구성됨.<br/>

&ensp;(3) Even parity(짝수 패리티) 사용<br/>
&ensp;각 p_k는 자신이 담당하는 영역의 1 개수를 짝수로 맞추도록 0 or 1을 넣음.<br/>

&ensp;Hamming ECC 예제 설명<br/>
&ensp;예제 데이터:<br/>
```ini
9A_hex = 10011010₂
```

&ensp;해밍 위치에 맞춰 d1, d2… 배치 후 각 parity bit을 계산해서 p1, p2, p4, p8을 채움.<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-9.png" width="500"></p>

&ensp;오류 발생 시 디코딩<br/>
&ensp;예: 10번 bit 뒤집힌 경우<br/>
1. 새로 parity 검사
2. p1, p2, p4, p8의 결과를 합쳐서 → 오류 위치의 이진수 주소가 나타남

&ensp;예: p1=1, p2=0, p4=1, p8=0 → 1010₂ = 10, 10번 비트가 에러<br/>
&ensp;따라서 그 비트를 뒤집어서 원복 → 에러 수정 완료<br/>

### SEC/DED Code (Single Error Correcting / Double Error Detecting)

&ensp;SEC(단일 오류 수정)<br/>
&ensp;해밍 코드 기본 구조(거리 3)<br/>

&ensp;DED(이중 오류 검출)<br/>
&ensp;추가 패리티 비트를 하나 더 넣어 전체 코드의 해밍 거리를 4로 만들면 가능.<br/>

&ensp;해밍 코드 + 전체 패리티 1bit 추가 = SEC/DED<br/>

&ensp;예제: data = 1001<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-10.png" width="500"></p>

* case 1: 단일 오류 → 빨간색 하나
* case 4: 이중 오류 → 빨간색 두 개 → "double error" 로 표시

&ensp;SEC+DED는<br/>
* 단일 오류는 수정
* 두 개 오류는 "오류 발생했다"만 탐지 가능

## Fully Associative Cache = CAM(Content Addressable Memory)

&ensp;CAM 이란?<br/>
&ensp;일반 메모리는 주소로 접근<br/>
&ensp;CAM은 내용(data, tag)으로 직접 비교하여 찾음<br/>

&ensp;Fully associative cache가 CAM을 기반으로 작동.<br/>

&ensp;CAM 동작 방식<br/>
1. CPU가 **Argument Register(A)**에 비교할 tag를 넣음
2. CAM의 모든 엔트리와 병렬 비교
3. 일치하는 엔트리의 index만 1(M(i)=1)
4. 그 인덱스의 데이터가 cache hit

&ensp;Key Register(K)<br/>
* 비교할 때 특정 비트만 비교하도록 마스킹하는 기능
* K가 1인 비트만 비교함 (bit mask)

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-4-11.png" width="500"></p>