---
title: "chapter 5-2. The Baics of Cache"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-11-22
last_modified_at: 2025-11-22
---

Simple Cache Scenario
=====

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-1.png" width="500"></p>

1. 캐시?
* CPU가 반복적으로 접근하는 데이터를 빠르게 가져오기 위한 작은 메모리
2. 여기서 중요한 질문 2개
* Q1: 캐시에 데이터가 있는지(= Hit or Miss) 어떻게 판단하는가?
* Q2: 있다면 어디에서 찾는가?
3. 그림 설명은 단순한 예시
* Xₙ 접근 전: 캐시에 없음 → Miss
* Xₙ 접근 후: 캐시에 채워짐 → 이후엔 Hit 가능

Direct Mapped Cache
=====

&ensp;Direct-Mapped: 메모리의 각 위치가 캐시의 단 하나의 위치에만 매핑된다.<br/>
&ensp;문제<br/>
* 캐시는 작고 메모리는 크기 때문에 → 서로 다른 메모리 주소가 같은 캐시 위치를 공유하게 됨 → Conflict Miss(충돌 미스) 발생<br/>
&ensp;캐시 주소(Index) 계산식<br/>
```matlab
캐시 주소 = (Memory address) mod (cache size)
```

&ensp;캐시 라인 구성 요소 3개<br/>
* Valid bit — 이 라인에 값이 있는지
* Tag — 원래 주소 정보(누구인지 구분하는 용도)
* Data — 실제 메모리 블록 내용

Accessing a Cache (Example)
-----

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-2.png" width="500"></p>

&ensp;주소를 어떻게 나누는가가 핵심<br/>
* 예시 캐시: 8-byte direct mapped cache = 8개의 캐시 라인 → Index 비트 = 3비트 (왜냐면 2³ = 8)

&ensp;주소가 캐시에 들어올 때 수행되는 과정<br/>
1. Memory address → Binary 변환
2. 하위 3비트는 Index
3. 나머지 상위 비트는 Tag
4. Index에 해당하는 캐시 라인 접근
5. Valid + Tag 비교 → Hit or Miss

* Index가 같으면 서로 다른 주소도 같은 캐시 라인을 사용한다. → Direct-Mapped의 가장 큰 특징 → Conflict Miss의 원인

States of the Cache
-----

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-3.png" width="500"></p>

* Index = 캐시 라인 번호
* Valid=1이면 이 라인에 데이터가 존재
* Tag가 적혀 있음 → 어떤 메모리 블록인지 식별
* Data는 M[address] 형태로 표현됨

&ensp;예시<br/>
```pgsql
Index 010  
Valid 1  
Tag 10  
Data M[26]
```

&ensp;26번 메모리의 내용이 캐시 index=2인 곳에 저장되어 있음<br/>

&ensp;Example Sequence of References<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-4.png" width="500"></p>

&ensp;시쿼스가 다음과 같이 주어지면<br/>
* 주소 22 (10110)
* 주소 26 (11010)
* 주소 22 (10110)
* 주소 16 (10000)
* ...

&ensp;해야 하는 것:<br/>
1. binary 변환
2. Index 계산(하위 3비트)
3. Tag 계산
4. 캐시의 해당 Index 라인에서
    - Valid=1이고
    - Tag가 같으면 Hit
    - 아니면 Miss
5. Miss라면 캐시 라인을 교체 (Tag+Data 갱신)

&ensp;표가 나오면 딱 3 단계로 읽는다.<br/>
&ensp;표를 읽으려면 먼저 메모리 주소가 어떤 캐시 라인(index)으로 가는지 알아야 한다.<br/>
&ensp;예<br/>
* 메모리 주소 = `10110`
* 캐시 크기 = 8 entries → index 비트 = 

&ensp;그러면<br/>
```nginx
Tag | Index
10  | 110
```

* Index = 110 (2진수 6) → 6번 캐시 라인
* Tag = 10

&ensp;2단계: 표에서 해당 Index 라인을 찾기<br/>
```less
Index | V | Tag | Data
-------------------------
000   | 1 | 10  | M[16]
001   |   |     |
010   | 1 | 10  | M[26]
011   | 1 | 00  | M[3]
100   |   |     |
101   |   |     |
110   | 1 | 10  | M[22]
111   |   |     |
```

&ensp;예를 들어<br/>
* Index = 110 을 찾는다 → 즉, 표에서 110 줄을 본다.

&ensp;3단계: Valid + Tag 비교 → Hit/Miss 판단<br/>
&ensp;해당 Index 줄을 찾았으면:<br/>
1. Valid bit(V)=1인가? → 0이면 무조건 Miss → 1이면 다음 단계 진행
2. Tag가 우리가 구한 Tag와 같나? → 같으면 Hit, 다르면 Miss

&ensp;예시<br/>
&ensp;주소 22(`10110`)<br/>
* Index = 110
* Tag = 10

&ensp;표에서 Index 110 줄은:<br/>
```less
110 | 1 | 10 | M[22]
```

* V=1
* Tag=10 <br/>
&ensp;→ Hit!<br/>

&ensp;Example Sequence 표는 어떻게 읽을까?<br/>
```scss
Decimal | Binary | Hit/Miss | Assigned block
22      | 10110  | miss      | 110 = 6
26      | 11010  | miss      | 010 = 2
22      | 10110  | hit       | 110 = 6
...
```

&ensp;Binary addr: 주소를 2진수로 변환한 것<br/>
&ensp;Assigned cache block= Binary address의 하위 3비트(Index)<br/>
&ensp;예: <br/>
&ensp;26의 binary는 11010 → 하위 3비트는 010 → 캐시 2번 라인 사용<br/>
&ensp;Hit or Miss<br/>
&ensp;표를 읽는 순서<br/>
1. Assigned cache block(=Index)을 찾고
2. 그 캐시 라인에 저장된 Tag가 같으면 Hit
3. 아니면 Miss, 그리고 캐시 라인 업데이트

# 4-Block Cache with 4-Byte Blocks

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-5.png" width="500"></p>

&ensp;개념 1) 블록이 4바이트 → Byte offset = 2비트<br/>
* 4바이트 = 2² → “이 블록 안에서 몇 번째 바이트인가?”를 나타내기 위해 필요한 비트 = 2비트 → 주소의 **가장 낮은 2비트(LSB)**는 “바이트 위치”이므로 캐시에 저장되지 않음

```pgsql
주소 = [ Tag | Index | Byte offset(2) ]
```

&ensp;개념 2) 캐시에 저장되는 것은 “블록 단위”<br/>
* 메모리는 4바이트씩 잘려 있음(block)
* 캐시는 메모리 블록 단위로 가져와 저장함
* Byte offset은 캐시가 신경 쓸 필요가 없음 → 캐시는 "블록"만 저장하고 "블록 안 세부 바이트"는 신경 안 씀


# Cache with 1-Word Blocks<br/>
&ensp;1-word = 4바이트<br/>
&ensp;32-bit 주소일 때 구성<br/>
```pqsql
| Tag | Index | Byte offset(2bit) |
```

&ensp;Cache size = 2ⁿ words → Index = n비트<br/>
&ensp;Tag bit 수 계산<br/>
&ensp;주소 전체 = 32비트<br/>
&ensp;Byte offset = 2비트<br/>
&ensp;Index = n비트<br/>

&ensp;따라서 Tag = 32 – (n + 2)<br/>

&ensp;Total number of bits 공식<br/>
&ensp;공식<br/>
```matlab
2ⁿ × (1 + tag + block size)
```

&ensp;여기서 block size = 4 bytes = 32 bits<br/>
&ensp;이 식을 변형해서 다음처럼 외우기 쉽게 만든 것<br/>
```scss
2ⁿ × (63 - n)
```

&ensp;Example: 4KiB Cache with 1-Word Blocks<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-6.png" width="500"></p>

&ensp;Byte offset = 2비트?<br/>
&ensp;1 word = 4 bytes → 4바이트 중 어느 바이트인가? → 2비트<br/>
&ensp;Cache size = 4 KiB = 4096 bytes<br/>
&ensp;1024 = 2¹⁰ → Index = 10비트<br/>

&ensp;Tag bit 수<br/>
&ensp;전체 주소 32비트<br/>
&ensp;Byte offset = 2비트<br/>
&ensp;Index = 10비트<br/>
&ensp;Tag = 32 – (10+2) = 20비트<br/>

&ensp;내부 흐름 해석<br/>
&ensp;메모리 주소 →<br/>
1. Byte offset(2bit) 제거
2. 다음 10비트로 캐시 인덱스 찾음
3. 남은 20비트로 Tag 비교
4. Valid=1이고 Tag 일치하면 Hit
5. Data(32bit word) 반환

# Cache with 2ᵐ-Word Blocks

&ensp;구조<br/>
```pgsql
| Tag | Index | Block offset | Byte offset |
```

&ensp;Byte offset = 2비트 (word는 항상 4byte이므로)<br/>
&ensp;Block offset = m비트 (block 내부에서 몇 번째 word인가?) → block size = 2ᵐ words니까 block 안에는 2ᵐ개의 word 존재 → block offset = m bit<br/>
&ensp;Index = n bits (block 개수가 2ⁿ일 때)<br/>
&ensp;Tag = 32 - (n + m + 2)<br/>

&ensp;Direct Mapped Cache with 4-Word Blocks<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-7.png" width="500"></p>

&ensp;Byte offset = 2비트 (block 내부에서 몇 번째 byte?)<br/>
&ensp;Block offset = 2비트 (block 내부에서 몇 번째 word?)<br/>

&ensp;왜냐하면 4-word block → 4 = 2² → block offset=2bit<br/>

&ensp;주소 구조<br/>
```pgsql
| Tag(20) | Index(8) | Block offset(2) | Byte offset(2) |
```

&ensp;Another Implementation<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-8.png" width="500"></p>

&ensp;핵심 흐름은 같음<br/>
1. Address → Byte offset(2비트) 제거, Block offset(m비트) 제거, Index(n비트)로 캐시 라인 선택
2. 선택된 캐시 라인의 Tag와 Address의 Tag 비교
3. 같으면 Hit
4. Block offset을 이용해 block 내부에서 원하는 word 선택

# Direct Mapped Cache (Block Size = 1)

&ensp;Reference string: `0 1 2 3 4 3 4 15` <br/>
&ensp;Block size = 1 word → 한 블록은 데이터 하나(Mem(x))만 가짐<br/>
&ensp;캐시 구조<br/>
* Index 00
* Index 01
* Index 10
* Index 11

&ensp;→ 총 4개의 캐시 라인<br/>
&ensp;Index 계산<br/>
```ini
index = address mod 4   (block size = 1일 때)
```

&ensp;주소별 동작 이해하기<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-9.png" width="500"></p>

| 접근값 | index | Hit/Miss     | 캐시 변화                 |
| --- | ----- | ------------ | --------------------- |
| 0   | 0     | miss         | Mem(0) 저장             |
| 1   | 1     | miss         | Mem(1) 저장             |
| 2   | 2     | miss         | Mem(2) 저장             |
| 3   | 3     | miss         | Mem(3) 저장             |
| 4   | 0     | miss (0과 충돌) | Mem(4) 저장, Mem(0) 사라짐 |
| 3   | 3     | hit          | Mem(3) 유지             |
| 4   | 0     | hit          | Mem(4) 유지             |
| 15  | 3     | miss (3과 충돌) | Mem(15) 저장            |

&ensp;→ 8번 요청에서 6 misses<br/>

1. Direct-mapped는 하나의 주소가 딱 하나의 캐시 라인에만 갈 수 있음 → 그래서 index 충돌이 많음
2. Block size=1이면 Conflict Miss가 매우 많이 발생함
3. Repeated accesses to 3 or 4 → Hit이지만 → 15는 index 3을 써서 Mem(3)을 날려버리고 Miss 발생

&ensp;index 충돌이 Miss의 주 원인이다.<br/>

# Direct Mapped Cache (Block Size = 2)

&ensp;Reference string: `0 1 2 3 4 3 4 15` <br/>
&ensp;Block size = 2 → 한 블록에 두 개의 word 저장됨<br/>
&ensp;예<br/>
```scss
Mem(0), Mem(1)
Mem(2), Mem(3)
Mem(4), Mem(5)
...
```

&ensp;즉 한 번 불러오면 두 개의 데이터가 함께 올라옴 → Spatial locality 활용<br/>

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-10.png" width="500"></p>

&ensp;Block size=2일 때 index 계산<br/>
&ensp;전체 주소 0~15를 Block Size=2로 나누면:<br/>

| address | block number = addr / 2 | index = block num mod 4 |
| ------- | ----------------------- | ----------------------- |
| 0,1     | block 0                 | index=0                 |
| 2,3     | block 1                 | index=1                 |
| 4,5     | block 2                 | index=2                 |
| 6,7     | block 3                 | index=3                 |
| …       | …                       | …                       |

&ensp;Reference string 전체 분석<br/>
* 0 접근: block 0 → miss
* 1 접근: block 0 → 같은 block이 이미 있음 → hit
* 2 접근: block 1 → miss
* 3 접근: block 1 → hit
* 4 접근: block 2 → miss
* 3 접근: block 1 → hit
* 4 접근: block 2 → hit
* 15 접근: block 7 → miss

&ensp;→ 8 요청 중 miss = 4<br/>
&ensp;Block size=1보다 miss가 줄었다.<br/>

1. Block size가 크면 spatial locality 때문에 miss 줄어듦
2. 1 →hit, 3→hit, 4→hit 되는 이유가 같은 block이기 때문
3. block size=2는 block size=1보다 더 효율적임
4. 하지만 너무 크면 문제 발생

# Bits in a Cache

&ensp;문제:<br/>
```text
Direct-mapped
16 KiB of data
4-word blocks
32-bit address
```

&ensp;이걸 가지고 캐시 전체 크기(비트)를 계산해라<br/>

&ensp;Step 1) Block 수 계산<br/>
&ensp;캐시에 저장된 데이터 크기 = 16KiB<br/>
&ensp;Block size = 4 words<br/>
&ensp;1 word = 4 bytes → 4 words = 16 bytes<br/>

&ensp;Block 수 = (캐시 데이터 크기) / (block size)<br/>
```mathlab
16 KiB = 16 × 1024 bytes = 16384 bytes
block size = 16 bytes
16384 / 16 = 1024 blocks = 2^10 blocks
```

&ensp;→ Index bit = 10 비트<br/>

&ensp;Step 2) Block 안에서 바이트 위치 (Byte offset)<br/>
&ensp;Block = 4 words = 16 bytes 어떤 byte인지 지정하려면?<br/>
```mathlab
16 bytes = 2^4 → Byte offset = 4 bits
```

&ensp;주소 맨 뒤 4비트는 캐시에서 사용하지 않음<br/>
```ini
addr = [ Tag | Index | Byte offset(4 bits) ]
```

&ensp;Step 3) Tag bit 계산<br/>
&ensp;주소 전체 = 32bits<br/>
&ensp;Index = 10 bits<br/>
&ensp;Byte offset = 4 bits<br/>

&ensp;그러면 Tag는<br/>
```ini
Tag = 32 - 10 - 4 = 18 bits
```

&ensp;Step 4) 캐시에 저장되는 한 block당 비트 수<br/>
&ensp;한 캐시 라인은 다음으로 구성됨<br/>
1. Valid bit: 1 bit
2. Tag: 18 bits
3. Data: block size = 4 words = 4 × 32bits = 128 bits

&ensp;캐시 한 라인의 총 비트 수:<br/>
```
1 + 18 + 128 = 147 bits
```

&ensp;Step 5) 전체 캐시 비트 수<br/>
&ensp;Block 수 = 2^10<br/>
&ensp;Block당 비트 = 147 bits<br/>

&ensp;따라서<br/>
```ini
Total = 2^10 × 147 bits
```

&ensp;= 147 × 1024 bits = 147 Kibits = 147/8 KiBytes ≈ 18.4 KiBytes<br/>

&ensp;Miss rate vs. Block size<br/>
&ensp;Block size가 커지면<br/>
* Spatial locality 때문에 Miss rate 감소

&ensp;하지만 지나치게 크면 오히려 증가<br/>
* block이 커질수록 한 block이 캐시에서 차지하는 공간이 커짐 → 저장 가능한 block 수 감소, conflict miss 증가, miss rate 다시 증가

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-11.png" width="500"></p>

&ensp;Block Size vs. Performance<br/>
&ensp;문제점 1) Too large blocks<br/>
* 캐시에 들어갈 block 수 감소 
* Miss rate 증가

&ensp;문제점 2) Miss penalty 증가<br/>
&ensp;Miss penalty = block을 메모리에서 캐시에 가져오는 시간<br/>

&ensp;Block fetch time =<br/>
```scss
Latency(첫 word까지 걸리는 시간)  +  
Transfer time(나머지 word 전송 시간)
```

&ensp;Block size가 커질수록:<br/>
* Latency는 동일
* Transfer time ↑ → Miss penalty ↑

&ensp;결론: Block size에는 적절한 최적값이 존재함<br/>

Handling Cache Misses(캐시 미스 처리)
=====

&ensp;1) Instruction Cache Miss (명령 캐시 미스)<br/>
&ensp;Instruction cache miss는 프로그램 카운터(PC)가 가리키는 명령어를 캐시에서 못 찾았을 때 발생하는 상황<br/>
&ensp;(1) PC–4를 메모리에 보냄<br/>
&ensp;PC는 다음 명령어의 주소이므로 PC–4는 방금 실행하려던 instruction의 주소<br/>
&ensp;이 명령어 블록을 메모리에서 가져와라는 의미<br/>

&ensp;(2) 메모리에 read 요청 → 메모리 응답을 기다림<br/>
&ensp;CPU는 메모리가 블록을 읽어 올 때까지 기다림.<br/>
&ensp;Instruction fetch는 반드시 순서적으로 진행되므로 stall 발생<br/>

&ensp;(3) 캐시에 가져온 데이터 저장<br/>
* 캐시 라인의 data 갱신
* tag 갱신
* valid bit = 1로 설정

&ensp;Data Cache Miss (데이터 캐시 미스)<br/>
&ensp;데이터 캐시 miss가 일어나면:<br/>
* CPU는 데이터가 필요함
* 캐시에 없음 → memory에서 불러와야 함
* 메모리 read가 끝날 때까지 CPU는 멈춤

```
Data miss → CPU 멈춤 → memory read → 캐시에 저장 → 다시 실행
```

&ensp;Instruction miss와 매우 비슷하지만 Instruction miss는 명령어 pipeline 흐름이 다시 시작하는 것이고 Data miss는 단순히 stall하고 다시 실행<br/>

&ensp;Handling Writes (쓰기 정책)<br/>
&ensp;캐시의 write 정책은 두 가지:<br/>
&ensp;(1) Write-through (항상 둘 다 씀)<br/>
&ensp;Write-through policy란?<br/>
* 캐시에 쓰기 발생 → 캐시에도 쓰고
* 동시에 메모리에도 작성

```
Cache = Memory (완벽히 일치)
```

&ensp;목적: Consistency 유지<br/>
&ensp;이 정책의 장점은<br/>
* 캐시와 메모리의 값이 항상 동일
* coherence 유지 쉬움

&ensp;On write-hit<br/>
&ensp;캐시에 데이터가 존재(hit)하면?<br/>
1. 캐시 block에 word를 덮어 씀
2. 동일 word를 main memory에도 씀

&ensp;On write-miss<br/>
&ensp;캐시에 데이터 없음(miss) → memory에만 있다면:<br/>
1. 메모리에서 해당 block 가져옴
2. 캐시 block에 word 저장
3. 메모리에도 word 저장

&ensp;항상 두 군데를 갱신한다 → 이게 write-through의 본질<br/>

&ensp;Problems of Write-through<br/>
&ensp;가장 큰 문제: 성능 저하(Performance degradation)<br/>
&ensp;모든 write가 memory까지 내려감<br/>
&ensp;메모리는 캐시보다 수백 배 느림 → CPU가 빈번히 stall<br/>

&ensp;SPEC2000 예시<br/>
* 전체 명령 중 10%가 store
* write-thru 때문에 store마다 100 cycles 추가 → CPI = 1.0 + (100 × 10%) = 11 (속도가 11배 느려짐)

&ensp;해결책: Write Buffer<br/>
* 캐시에서 write 발생 → write buffer에 넣음
* CPU는 즉시 다음 작업 진행
* buffer가 백그라운드로 memory에 천천히 씀

&ensp;CPU는 stall 안 하고 바로 다음 명령 실행 가능<br/>
&ensp;단점: write buffer가 꽉 차면 stall 발생<br/>

&ensp;Write-Back<br/>
&ensp;쓰기 시 캐시에만 저장하고, 메모리는 나중에 저장한다.<br/>
```
Cache에만 씀
Memory는 한참 뒤에 씀
```

&ensp;이게 write-through와 가장 큰 차이<br/>

&ensp;Dirty bit(= Modified bit)<br/>
&ensp;캐시 블록이 변경되었음을 나타내는 flag<br/>
```
Dirty bit = 1 → 메모리보다 더 최신 데이터가 캐시에 있음
```

&ensp;메모리에 언제 쓰는가?<br/>
&ensp;Block이 캐시에서 **evict(교체)**될 때: dirty bit = 1 → 메모리에 write, dirty bit = 0 → 메모리에 write 불필요<br/>

&ensp;장점<br/>
* 성능 훨씬 좋음
* 메모리에 자주 쓰지 않음 (write-through의 단점 해소)

&ensp;단점<br/>
* 구조가 더 복잡
* coherence 유지가 어려움

&ensp;Write Allocate vs No Write Allocate<br/>
&ensp;Write allocate (대부분 write-back + write-through 일부)<br/>
1. 블록을 캐시에 불러오고
2. 그 블록에 write 수행

&ensp;No write allocate<br/>
1. 캐시에 불러오지 않고
2. 그냥 메모리만 쓴다 → write-through에서 자주 사용

Intrinsity FastMATH Processor
====

&ensp;Embedded microprocessor<br/>
&ensp;→ 저전력, 작은 장치용 CPU (스마트폰, IoT 같은 곳)<br/>
&ensp;MIPS architecture<br/>
&ensp;→ 수업에서 배우는 구조와 동일 (Pipeline, Cache 구조 이해에 좋은 예시)<br/>
&ensp;12-stage pipeline<br/>
&ensp;→ 명령어를 12단계로 쪼개서 처리 (파이프라인이 깊을수록 고클럭 가능)<br/>
&ensp;Split caches (Instruction cache / Data cache 분리됨)<br/>
* 각각의 cache 크기: 16 KiB
* 블록 크기: 16-word block
* block count: 256 blocks

&ensp;Cache Structure in FastMATH<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-12.png" width="500"></p>

&ensp;Address Breakdown (32-bit)<br/>
```
| Tag (18 bits) | Index (8 bits) | Byte offset (4 bits) |
```

&ensp;(1) Byte Offset = 4 bits<br/>
&ensp;Block size = 16 words<br/>
&ensp;1 word = 4 bytes<br/>
&ensp;→ 16 words = 64 bytes<br/>
&ensp;→ block 내부에서 몇 번째 byte인가?를 나타내기 위해 6 bits 필요가 맞지만<br/>
&ensp;FastMATH는 word 단위 접근이라<br/>
* Byte offset: 2 bits
* Block offset: 4 bits

&ensp;그림에서는 byte offset만 4bit로 나타냄 → word offset이 그 안에 포함됨.<br/>
* Byte offset = 2 bits
* Word offset = 4 bits → 그림에서 합쳐서 6bit 중에 4bit만 표기한 것

&ensp;(2) Index = 8 bits<br/>
&ensp;256 blocks → log₂(256) = 8bit<br/>
&ensp;따라서 주소의 중간 8bit는 캐시의 어느 block인지 결정<br/>

&ensp;(3) Tag = 18 bits<br/>
&ensp;32 - (8 + 4 + 나머지 offset) = 18 bits → CPU가 그 block이 진짜 맞는지 확인할 때 사용<br/>

보충
=====

# Direct-Mapped Cache (Block size = 8 bytes)

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-14.png" width="500"></p>

&ensp;Block size = 8 bytes<br/>
&ensp;8 bytes = 2³ → offset = 3 bits<br/>

&ensp;Cache는 index=2 bits (총 4개의 block)<br/>
```
Index bits = 2
Blocks = 4
```

&ensp;주소 전체를 4 + 2 + 3 = 9bit 으로 가정하고 예제를 만든 것<br/>

&ensp;Initial cache content<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-13.png" width="500"></p>

&ensp;각 index 블록이 저장하고 있는 메모리 범위<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-15.png" width="500"></p>

* Block 00: 0100 00 xxx → 0x80 ~ 0x87
* Block 01: 0100 01 xxx → 0x88 ~ 0x8F
* Block 10: 0001 10 xxx → 0x30 ~ 0x37
* Block 11: 1010 11 xxx → 0x158 ~ 0x15F

&ensp;이렇게 되는 이유<br/>
&ensp;주소 형식: \[ tag(4) \] \[ index(2) \] \[ offset(3) \] <br/>
&ensp;예: tag = 0100, index = 00 → 0100 00 xxx <br/>
&ensp;xxx = 000 ~ 111 = 0~7<br/>
&ensp;16진수<br/>
```yaml
0100 0000₂ = 0x80
0100 0111₂ = 0x87
```

&ensp;block 00에는 0x80~0x87이 들어있다<br/>

&ensp;Access sequence example<br/>
&ensp;주어진 주소 시퀀스: `083, 007, 034, 15F, 002, 080, 1A8, 038, 001, 1AF` <br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-2-16.png" width="500"></p>

&ensp;Step 1: 주소 → binary → tag + index<br/>
&ensp;예: `083` <br/>
&ensp;hex → binary:<br/>
```yaml
083₁₆ = 0 1000 0011₂
```

* tag = 0100
* index = 00
* offset = 011

&ensp;Hit or Miss 판단<br/>
&ensp;Block 00의 tag = 0100 → 같은 tag → Hit<br/>

&ensp;또 다른 예: `007`<br/>
&ensp;007₁₆ = 0000 0111₂<br/>
* tag=0000
* index=00
* offset=111

&ensp;block00의 tag=0100 → 다름 → Miss → 0x00~0x07 블록을 block00에 로드, 기존 M[080]~M[087] 버려짐<br/>

&ensp;전체 처리 순서 요약<br/>
1) 주소를 2진수로 바꾼다
2) tag/index/offset으로 나눈다
3) index로 캐시 블록 선택
4) tag 비교해서 hit/miss
5) miss면 해당 block 메모리 범위를 계산하여 캐시에 저장
6) 다음 주소로 넘어감

