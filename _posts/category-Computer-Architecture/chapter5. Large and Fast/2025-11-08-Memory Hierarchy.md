---
title: "chapter 5-1. Memory Hierarchy"
excerpt: ""

writer: sohee Kim
categories:
  - Computer Architecture
tags:
  - CS

toc: true
use_math: true 
toc_sticky: true

date: 2025-11-08
last_modified_at: 2025-11-08
---

Introduction
====

# Processor–Memory Performance Gap

<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-1-1.png" width="500"></p>

&ensp;현상: 1980~2010 사이 CPU 성능 향상 속도(대략 1.52배/년 → 이후 1.20배/년)가 메모리 성능 향상 속도(대략 1.25배/년 → 1.07배/년)보다 훨씬 빨랐다. ⇒ CPU는 더 빠른데 메모리는 상대적으로 느려서 메모리 접근이 병목이 된다.<br/>
&ensp;예시: Apple II(1977) 기준: CPU ≈ 1000ns, 메모리 ≈ 400ns. 시간이 갈수록 CPU가 훨씬 앞서 나가며 격차가 벌어짐<br/>
&ensp;의미: 캐시 없이 메모리에 자주 접근하면 CPU가 대기(stall) 하므로 전체 성능이 크게 떨어진다. ➜ 해결책: 빠른 소용량 메모리(캐시) 를 여러 단계로 두고, 프로그램의 지역성(locality) 을 이용한다.<br/>

# Memory Hierarchy

* 엔지니어링 문제: 최소 비용으로 최대 성능
    - 빠른 메모리 = 비싸고 작음 (SRAM)
    - 느린 메모리 = 싸고 큼 (DRAM, SSD/HDD)
* 목표: 아주 큰 메모리를 아주 빠르게 쓰는 착시를 제공하기 → 실제로는 여러 레벨(L1/L2/L3 캐시 → 메인 메모리 → 스토리지)을 두고 자주 쓰는 데이터만 위쪽(빠른 곳)에 올려둠
* 핵심 원리 – 지역성(Principle of Locality)
    1. 시간적 지역성(Temporal): 방금 쓴 것을 곧 또 쓴다
    - 예: 루프에서 같은 변수/코드 반복 사용
    2. 공간적 지역성(Spatial): 가까이 있는 것을 연달아 쓴다
    - 예: 배열을 i=0→N-1 순서로 순차 접근

&ensp;메모리 계층의 기본 구조(위→아래로 갈수록 느리지만 큼)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-1-2.png" width="500"></p>

| 레벨         | 기술            | 특징                          |
| ---------- | ------------- | --------------------------- |
| **L1 캐시**  | SRAM          | 가장 빠름, 가장 작음(수십 KB), 코어에 붙음 |
| **L2 캐시**  | SRAM          | 빠름, 수백 KB~수 MB              |
| **L3 캐시**  | SRAM          | 코어들 **공유**, 수 MB~수십 MB      |
| **메인 메모리** | DRAM          | 수 GB 이상, 캐시보다 훨씬 큼/느림       |
| **스토리지**   | SSD/HDD/Flash | 가장 큼, 가장 느림                 |

* 블록(=라인): 캐시가 가져오는 최소 단위(보통 64B)
* 히트(Hit): 필요한 데이터가 캐시에 있음
* 미스(Miss): 캐시에 없음 → 아래 레벨에서 블록 단위로 가져옴(미스 페널티)
* AMAT (평균 메모리 접근 시간): AMAT = Hit time + Miss rate × Miss penalty → 히트 타임을 줄이고, 미스율/미스 페널티를 낮추는 게 목표

&ensp;멀티코어 칩의 캐시 계층 (예: Intel Core i7)<br/>
<p align="center"><img src="/assets/img/Computer Architecture/chapter5. Large and Fast/5-1-3.png" width="500"></p>

* 코어별 개인 캐시
    - L1 I-cache + L1 D-cache: 각 32KB, 보통 4-way, ~4사이클
    - L2 (Unified): 약 256KB, 보통 8-way, ~11사이클
* 코어 간 공유 캐시
    - L3 (Unified, Shared): 예 8MB, 16-way, ~30–40사이클
* 블록 크기: 64B (모든 캐시 공통인 경우가 많음)

&ensp;공유 L3가 필요한 이유<br/>
* 코어들이 같은 데이터를 볼 때 중복 로드 감소
* 캐시 일관성(coherence) 유지에 유리(프로토콜: MESI/MOESI 등 필요)

&ensp;메모리 접근 과정<br/>
1. 명령/데이터 접근 발생
2. L1에서 찾음? → 히트면 수 사이클 내 완료
3. 미스면 L2 조회 → 또 미스면 L3 → 또 미스면 DRAM
4. 미스 시 64B 블록을 상위 캐시에 올려두고, 원하던 바이트/워드를 사용
5. 다음 접근에서 시간·공간적 지역성 덕분에 히트 확률 상승

&ensp;Hit & Miss<br/>

| 용어                         | 설명                                                                    |
| -------------------------- | --------------------------------------------------------------------- |
| **Block (= Line)**         | 상위 계층과 하위 계층 간 데이터 전송의 최소 단위.<br>보통 한 블록은 **64B** 정도.                 |
| **Hit**                    | CPU가 요청한 데이터가 **상위 계층**(예: 캐시)에 **이미 존재**하는 경우.                       |
| **Miss**                   | 요청한 데이터가 상위 계층에 **없어서**, 하위 계층에서 **불러와야** 하는 경우.                      |
| **Hit rate (= hit ratio)** | 전체 접근 중 **Hit된 비율** → 높을수록 좋음.<br>💡 `Hit rate = (Hit 횟수 / 전체 접근 횟수)` |
| **Miss rate**              | `1 - Hit rate`                                                        |

* Miss가 발생하면 어떤 일이 일어나는가? → 하위 계층 접근 + 블록 단위 교체
* Miss rate = ? 계산 문제 출제 가능

# 성능 측정 – AMAT (Average Memory Access Time)

&ensp;Hit time: 상위 계층(예: 캐시)에서 블록을 찾는 데 걸리는 시간 = `블록 접근 시간 + Hit/Miss 판별 시간` <br/>
&ensp;Miss penalty: Miss 시 하위 계층에서 블록을 가져와 CPU로 전달하기까지 걸리는 시간 = 하위 계층 접근 시간<br/>
* 전송 시간
* 상위 계층에 삽입 시간
* CPU로 전달 시간

&ensp;AMAT 공식: AMAT = Hit time + (Miss rate × Miss penalty)<br/>

# The BIG Picture

&ensp;Temporal Locality (시간적 지역성)
* 최근에 접근한 데이터는 곧 다시 접근된다. → 최근에 접근한 데이터를 상위 계층(캐시) 에 두면 효율적.
* 예: 반복문(loop) 내 변수 재사용

&ensp;Spatial Locality (공간적 지역성)<br/>
* 가까운 주소의 데이터가 곧 접근된다. → 여러 연속된 단어(예: 배열)를 한 번에 블록 단위로 불러옴
* 예: 배열 순차 접근, 함수 코드 순서 실행

&ensp;Memory Hierarchy의 목표<br/>
* Hit rate를 높여서 평균 접근 시간(AMAT)을 줄인다.
* 최적의 구조 =
    - Access time ≈ 가장 빠른 레벨
    - Size ≈ 가장 느린(가장 큰) 레벨

&ensp;Multi-level Inclusion / Exclusion Property<br/>

| 속성                     | 의미                            | 예시                        |
| ---------------------- | ----------------------------- | ------------------------- |
| **Inclusion Property** | 하위 캐시에 있는 데이터는 항상 상위 캐시에도 존재. | Level(i) ⊂ Level(i+1)     |
| **Exclusion Property** | 두 캐시에 같은 블록이 **중복 저장되지 않음.**  | Level(i) ∩ Level(i+1) = ∅ |

Memory Technologies
====

&ensp;주요 메모리 종류 및 특성 비교<br/>

| Memory technology      | Typical access time     | $ per GiB (2020) | 특징                     |
| ---------------------- | ----------------------- | ---------------- | ---------------------- |
| **SRAM** (Static RAM)  | 0.5–2.5 ns              | $500–$1000       | 빠름, 비쌈, 캐시에 사용    |
| **DRAM** (Dynamic RAM) | 50–70 ns                | $3–$6            | 느림, 쌈, 메인 메모리에 사용 |
| **Flash Memory**       | 5,000–50,000 ns         | $0.06–$0.12      | 비휘발성 저장 (SSD 등)        |
| **Magnetic Disk**      | 5,000,000–20,000,000 ns | $0.01–$0.02      | 가장 느림, 대용량 HDD에 사용     |

&ensp;SRAM (Static Random Access Memory)<br/>
&ensp;"캐시 메모리에 사용되는 빠른 메모리"<br/>
&ensp;구조 및 특징<br/>
* 각 비트 저장에 6~8개의 트랜지스터 사용 → 안정적이지만 면적 큼
* 전하 유지(refresh) 불필요 → "Static"
* 읽기/쓰기 속도 일정 (고정 접근 시간)
* 비휘발성 아님 (전원 끄면 데이터 사라짐)

&ensp;장점<br/>
* 빠름 (CPU 속도와 비슷)
* 간단한 제어, refresh 불필요

&ensp;단점<br/>
* 집적도 낮음 (트랜지스터 수 많음)
* 가격 비쌈 → 대용량으로 사용 불가능

&ensp;DRAM (Dynamic Random Access Memory)<br/>
&ensp;"메인 메모리(RAM)에 사용되는 느리지만 싸고 큰 메모리"<br/>
&ensp;구조 및 특징<br/>
* 각 비트는 1개의 트랜지스터 + 1개의 캐패시터로 저장
* 캐패시터의 전하가 시간이 지나면 누설됨 → 주기적으로 Refresh 필요 (~8ms)
* Refresh가 전체 동작의 1~2% 시간을 차지
* Dynamic이라 부르는 이유 = 저장된 값이 계속 변동(누설)하기 때문

&ensp;장점<br/>
* 트랜지스터 1개/비트 → 집적도 높음
* 저렴하고 대용량 가능

&ensp;단점<br/>
* Refresh 필요 → 속도 저하
* 접근 시간 길고 회로 복잡

&ensp;SRAM vs DRAM 비교 요약<br/>

| 항목      | SRAM             | DRAM            |
| ------- | ---------------- | --------------- |
| 저장 방식   | 플립플롭(트랜지스터 6~8개) | 캐패시터 + 트랜지스터 1개 |
| 속도      | 빠름               | 느림              |
| 크기      | 작음               | 큼               |
| 가격      | 비쌈               | 저렴              |
| Refresh | 불필요              | 필요              |
| 용도      | Cache (L1/L2/L3) | Main Memory     |
| 소비 전력   | 높음               | 낮음              |
| 집적도     | 낮음               | 높음              |
