# 🧾 Midterm Review Sheet — 문제 1~3 통합 요약 (Java 중간고사 대비)

> 🎯 **이 한 장으로 문제 1~3 완벽 커버**
> 
> 🧠 핵심 키워드: `equals()` · `Math.random()` · `Math.sqrt()` · 상속/오버라이드 · 연료계산 · 방향 전환

---

## 🧩 문제 1 — PrintShop (문자 패턴 출력)

### 📘 핵심 구조
```java
class PrintShop {
    private boolean direction = true;
    private String pChar;
    private int maxNum = 3;
    final private int maxIter = 2;

    PrintShop() { pChar = "*"; }

    PrintShop(String direct, String pC, int mN) {
        if (direct.equals("forward")) direction = true;
        if (direct.equals("reverse")) direction = false;
        pChar = pC;
        maxNum = mN;
    }

    void printForward() {
        int i, j, k;
        for (i = 1; i <= maxNum; i++) {
            for (j = 0; j < i; j++) System.out.print(pChar);
            System.out.println();
        }
    }

    void printReverse() {
        int j, k;
        for (j = maxNum; j >= 1; j--) {
            for (k = 0; k < j; k++) System.out.print(pChar);
            System.out.println();
        }
    }

    void myPrint() {
        boolean printDirection = direction;
        for (int i = 0; i < maxIter; i++) {
            if (printDirection) printForward();
            else printReverse();
            printDirection = !printDirection; // 방향 반전
        }
        System.out.println("--------------------");
    }
}
```

### 📂 입력 (`num1.txt`)
```
forward # 3
reverse @ 5
forward $ 4
```

### 📈 출력 예시
```
*
**
***
***
**
*
--------------------
@@@@@
@@@@
@@@
@@
@
@
@@
@@@
@@@@
@@@@@
--------------------
$
$$
$$$
$$$$
$$$$
$$$
$$
$
--------------------
```

### 🧠 암기 포인트

| 항목 | 내용 |
|------|------|
| 방향 | `direction = true` → forward |
| 전환 | `printDirection = !printDirection;` |
| 출력 | `print`(줄 유지) / `println`(줄바꿈) |
| 반복 | forward: `i=1→maxNum`, reverse: `j=maxNum→1` |

---

## 🧩 문제 2 — PointArray (랜덤 좌표 & 거리 계산)

### 📘 핵심 구조
```java
class Point {
    private double x, y;
    Point(double x, double y) { this.x = x; this.y = y; }

    double getX() { return x; }
    double getY() { return y; }
    protected void move(double x, double y) { this.x = x; this.y = y; }

    void printPoint() { System.out.printf("(%4.2f , %4.2f)", x, y); }

    double getDistance(Point p2) {
        return Math.sqrt(Math.pow(x - p2.x, 2) + Math.pow(y - p2.y, 2));
    }
}

class PointArray {
    int row, column;
    Point mA[][];

    PointArray(int r, int c) {
        row = r; column = c;
        mA = new Point[row][column];
        for (int i = 0; i < row; i++)
            for (int j = 0; j < column; j++)
                mA[i][j] = new Point(Math.random()*10, Math.random()*10);
    }

    void reset() {
        for (int i = 0; i < row; i++)
            for (int j = 0; j < column; j++)
                mA[i][j].move(Math.random()*10, Math.random()*10);
    }

    void showAll() {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                mA[i][j].printPoint();
                System.out.print(" ");
            }
            System.out.println();
        }
    }

    Point getPoint(int r, int c) { return mA[r][c]; }
}
```

### 📂 입력 (`num2.txt`)
```
5 5
0 0
4 4
```

### 📈 출력 예시
```
(2.47 , 6.33) (8.52 , 0.40) ...
Distance between (2.47 , 6.33) and (7.55 , 4.66) = 5.39
```

### 🧠 암기 포인트

| 항목 | 내용 |
|------|------|
| `Math.random()` | 0 ≤ x < 1 → *10 → 0~10 미만 실수 |
| 거리 공식 | `sqrt((x1−x2)^2 + (y1−y2)^2)` |
| 2D 배열 | `Point[][] mA = new Point[row][col]` |
| `reset()` | 모든 좌표 새 랜덤값으로 변경 |

---

## 🧩 문제 3 — Automobile (상속 및 연비 시뮬레이션)

### 📘 상속 구조
```
Automobile (abstract)
   ↑
  Sedan
   ↑
  Sports
```

---

### 🚗 Automobile (추상 클래스)
```java
abstract class Automobile {
    private String makerName, modelName;
    private int serialNum;
    private double tankSize, remainingFuel, odometer;
    private static int serialCount = 1000;

    Automobile(String maker, String model, double tank) {
        makerName = maker; modelName = model;
        tankSize = tank; remainingFuel = tank;
        odometer = 0; serialNum = serialCount++;
    }

    void showModelMakerTank() {
        System.out.print(makerName+" "+modelName+" "+serialNum+" ["+tankSize+" liter]");
    }

    void showFuel() {
        System.out.println(" fuel left= "+remainingFuel+" l / "+odometer+" kilo");
    }

    public abstract boolean running(double kM);
}
```

---

### 🚘 Sedan
```java
class Sedan extends Automobile {
    private double kiloPerL;

    public Sedan(String m, String mM, double t, double kP) {
        super(m, mM, t);
        this.kiloPerL = kP;
    }

    public boolean running(double kM) {
        double cF = getFuel(), cK = getKilo();
        double fuelNeeded = kM / kiloPerL;
        if (cF < fuelNeeded) {
            System.out.println("Not enough fuel to drive " + kM + " km!");
            return false;
        } else {
            setFuel(cF - fuelNeeded);
            setKilo(cK + kM);
            return true;
        }
    }

    void showAll() {
        System.out.print("[Sedan] ");
        showModelMakerTank();
        System.out.println(" " + kiloPerL + " km/l");
    }
}
```

---

### 🏎️ Sports
```java
class Sports extends Sedan {
    private double kiloPerL;
    private int numCylinder;

    public Sports(String m, String mM, double t, double kP, int cyl) {
        super(m, mM, t, kP);
        this.kiloPerL = kP;
        this.numCylinder = cyl;
    }

    public boolean running(double kM) {
        double cF = getFuel(), cK = getKilo(), liter;
        double adjustedKPL = kiloPerL - (numCylinder * 0.1);
        if (adjustedKPL <= 0) adjustedKPL = 1;

        liter = kM / adjustedKPL;

        if (cF < liter) {
            System.out.println("Not enough fuel to drive " + kM + " km!");
            return false;
        } else {
            setFuel(cF - liter);
            setKilo(cK + kM);
            return true;
        }
    }

    void showAll() {
        System.out.print("[Sports] ");
        showModelMakerTank();
        System.out.print(" Cylinder= " + numCylinder);
        System.out.println();
    }
}
```

---

### ⚖️ Sedan vs Sports 비교

| 항목 | Sedan | Sports |
|------|--------|---------|
| 연비 계산 | `kM / kiloPerL` | `kM / (kiloPerL - numCylinder*0.1)` |
| 실린더 영향 | X | 연비 감소 (실린더 많을수록 비효율) |
| 상속 관계 | `Automobile` | `Sedan` |
| 출력 형식 | `[Sedan] ...` | `[Sports] ... Cylinder=n` |
| 반환값 | true/false (연료 충분 여부) | 동일 |

---

### 🧠 시험 포인트 총정리

| 개념 | 포인트 |
|------|---------|
| 문자열 비교 | `equals()` |
| print vs println | `print`: 같은 줄 / `println`: 줄바꿈 |
| 난수 생성 | `Math.random()*10` (0~10 미만 실수) |
| 거리 계산 | `Math.sqrt((x−x2)^2+(y−y2)^2)` |
| 연비 계산 | `fuel = km / kiloPerL` |
| Sports 보정 | `kiloPerL - (numCylinder * 0.1)` |
| 추상 메서드 | `public abstract boolean running(double kM)` |
| 상속 순서 | `Automobile → Sedan → Sports` |
| 상태 업데이트 | `setFuel()` / `setKilo()` |
| 출력 메시지 | `"Not enough fuel to drive "+kM+" km!"` |

---

> ✅ **이 시트 한 장이면 문제 1~3 완벽 대비 가능!**  
> 
> 🧩 외워야 할 핵심 흐름:
> - PrintShop: 방향 전환과 중첩 for문  
> - PointArray: 난수 생성 + 거리 계산  
> - Automobile: 상속 + 오버라이드 + 연비 계산  
> 
> 💪 시험장에서는 코드 구조를 떠올리고, 각 for문/공식 패턴만 기억하자!
