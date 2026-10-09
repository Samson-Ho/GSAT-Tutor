# 數A Handout Digest — 黑狗 (林信安老師編寫) handout corpus

Source: `files/數A/黑狗_handout/` — 163 PDFs (162 unique; 資優班/三上 第59單元數列極限(1) duplicates 第59單元數列極限), ~3,300 pages, three series by 林信安老師:

| Series | Folder | Content |
|---|---|---|
| 108課綱 | `108課綱/一上 一下 二上 二下` | Current-curriculum textbook-order handouts (10年級必修 + 11年級數A). Closest match to 學測數A scope. |
| 99課綱 | `99課綱/第一冊–第四冊, 數甲上, 數甲下` | Old-curriculum handouts. 第一–四冊 overlap heavily with 108; 數甲上下 cover 機率統計/三角函數/複數/極限/微積分 (12年級 or old 指考數甲 content). |
| 資優班 | `資優班/一上 … 三下` (第1–63單元) | Gifted-class handouts: same topics, more proofs, harder 例題, olympiad-flavoured extras (數論、同餘、反三角、複數極式、圓錐曲線、微積分). |

**How to use this file (agent-facing).** Written in English to save tokens; every 數學名詞、題幹、專有名詞 is kept in 繁體中文 as the handouts print it. Each section gives: scope status (108 學習內容 codes from `scope.md`), definitions/theorems/formulas, 題型 with methods and representative handout 例題 (answers recomputed against the keys; where a key is wrong the correct value is given and the misprint noted inline, e.g. 「the key prints …」), traps, and enrichment. Out-of-scope material is kept (the handouts teach it) but flagged **[超出數A]** — never test it as 學測數A content; use `scope.md` as the authority. Past-exam citations inside the handouts (e.g. 「2014學測」「92學測」「91指定乙」) are reproduced because they show how a concept was examined.

Notation: vectors $\vec{a}$, $\overrightarrow{AB}$; segment length $\overline{AB}$; determinants with `vmatrix`; $\log$ = 常用對數 (base 10).

## Contents
Part A — 10年級必修
1. 實數、數與式、乘法公式、根式、算幾不等式（附：簡單數論）
2. 絕對值、分點公式、絕對值方程式與不等式（附：不等式總整理）
3. 指數與常用對數
4. 直線方程式
5. 二元一次不等式與線性規劃
6. 圓方程式、圓與直線
7. 多項式：運算、除法原理、函數圖形、方程式、不等式
8. 數列、級數、數學歸納法、遞迴
9. 數據分析（一維、二維）
10. 集合、邏輯、計數原理、排列組合、二項式定理
11. 古典機率與期望值
12. 三角比：直角三角比、廣義角、正餘弦定理、三角測量

Part B — 11年級必修數學A
13. 弧度量與三角函數圖形
14. 和差角、倍角半角、疊合（附：反三角函數）
15. 指數函數、對數律、對數函數及應用
16. 平面向量（運算、內積、面積與行列式、柯西）
17. 空間概念
18. 空間坐標、空間向量、內積、外積、三階行列式
19. 平面方程式、空間直線（附：球面）
20. 線性方程組、矩陣運算、矩陣應用、線性變換
21. 條件機率、獨立事件、貝氏定理、主客觀機率

Part C — handout content beyond 學測數A **[超出數A]**
22. 複數與複數極式（棣美弗、n次方根）
23. 圓錐曲線（拋物線、橢圓、雙曲線）
24. 隨機、二項分布、抽樣與信賴區間
25. 函數、數列極限、函數極限
26. 微分與應用
27. 積分與應用

---

# Part A — 10年級必修

## 1. 實數、數與式、乘法公式、根式、算幾不等式

**Scope**: N-10-1 實數 (√2 為無理數的證明★), A-10-1 式的運算, N-10-3 (算幾不等式). **Sources**: 108一上 1-1數與式; 99第一冊 1-1數與數線; 資優 第1單元簡單數論, 第2單元有理數與實數.

### 1.1 有理數 Q
- 有理數: 可表成「整數比 $\frac{m}{n}$」($m,n\in\mathbb Z$, $n\ne0$). Every integer is rational; representation not unique ($\frac13=\frac26$); Q closed under 加減乘除 (除數≠0).
- 有理數 ⇔ 整數、有限小數或循環小數. 直式除法: remainders mod $n$ have at most $n$ values → repeats → 循環小數.
- 最簡分數 $\frac{m}{n}$ 可化為有限小數 ⇔ 分母 $n$ 的質因數只有 2、5 (e.g. $\frac{67}{40}=\frac{67\cdot5^2}{2^3\cdot5^3}=\frac{1675}{10^3}=1.675$).
- 循環小數化分數: $x=3.\overline{12}$ ⇒ $100x-x=309$ ⇒ $x=\frac{309}{99}=\frac{103}{33}$. (Justification is 無窮等比級數.) 題型: 「$\frac{13}{5}$… 小數點後第123位」, 「$\frac{5}{13}$ 第2000位 → 8」: use period length & mod.
- 尺規作圖 $\frac{m}{n}$: draw auxiliary ray from O, mark n equal steps, connect last mark to A(m), draw parallels (平行線截比例線段).
- **稠密性**: $r<s$ rational ⇒ $r<\frac{mr+ns}{m+n}<s$ for $m,n>0$ ⇒ infinitely many rationals between any two. 整數具離散性 ($|p-q|\ge1$).
- 有理數運算律: 交換、結合、分配、消去律; 次序: 三一律、遞移律、加法律、乘法律 (乘負數變號).

### 1.2 無理數與實數
- $\sqrt2$ 不是有理數 (反證法): $\sqrt2=\frac mn$ ⇒ $m^2=2n^2$; exponent of 2 in $m^2$ is even, in $2n^2$ odd → 矛盾. Generalization: 若自然數 $n$ 的標準分解式中有某質因數出現奇數次，則 $\sqrt n$ 為無理數 (e.g. $540=2^2\cdot3^3\cdot5$ ⇒ $\sqrt{540}$ 無理).
- 十分逼近法: $1.414<\sqrt2<1.415$ … each step shrinks interval ×1/10.
- 無理數 = 不循環的無限小數; examples $\sqrt3,\pi,5+\sqrt2,\sqrt[3]2$, e.
- 實數 = 有理數 ∪ 無理數 ↔ 數線上所有點 (一對一). 實數家譜: 實數 ⊃ 有理數 (整數: 正整數/零/負整數; 分數) ∪ 無理數.
- 作圖 $\sqrt n$: (法一) 連續直角三角形螺線 $\sqrt2,\sqrt3,\dots$; (法二) 母子相似: $\overline{AC}=1,\overline{BC}=n$, 以 $\overline{AB}$ 為直徑作半圓, 過 C 作垂線交於 D ⇒ $\overline{CD}=\sqrt n$. Same idea draws $ab$, $\frac ba$ on the 數線 via similar triangles.
- 題型「證明無理」: 已知$\sqrt3$無理 ⇒ $5+\sqrt3$, $5\sqrt3$, $\frac{\sqrt3}{7}$ 無理 (反證). $\sqrt2+\sqrt7$: set $k=\sqrt2+\sqrt7$ rational ⇒ $\sqrt7-k=-\sqrt2$... square ⇒ $\sqrt2=\frac{k^2-5}{2k}$ rational, 矛盾. $\sqrt[3]{3}+2$-type: cube it. $\sqrt{n(n+2)}$ 無理: $n<\sqrt{n(n+2)}<n+1$.
- **有理係數比較**: $a,b\in\mathbb Q$, $a+b\sqrt2=0$ ⇒ $a=b=0$; hence $a+b\sqrt2=c+d\sqrt2$ ⇒ $a=c,b=d$. 例: $(2+\sqrt3)a+(1-\sqrt3)b=7-\sqrt3$ ⇒ $2a+b=7$, $a-b=-1$ ⇒ $a+b=5$. 有理數 $x$ 滿足 $(x^2-1)+(x^2-2x-3)\sqrt5=0$ ⇒ $x=-1$.
- 多選 classics: $a,b,a-b$ 無理 ⇒ $a+b$ 無理 ✗ (反例 $a=3+\sqrt2,b=3-\sqrt2$: $a-b=2\sqrt2$, $a+b=6$); $a,b,\frac ab$ 無理 ⇒ $ab$ 無理 ✗ ($a=3+\sqrt2,b=3-\sqrt2$, $ab=7$); $a,b\in\mathbb Q$, $ab\ne0$ ⇒ $a+b\sqrt3\ne0$ ✓; 可找兩無理數 $a,b$ 使 $\frac ab$ 無理、$ab$ 有理 ✓; $a^3,a^5\in\mathbb Q$ ⇒ $a\in\mathbb Q$ ✓ ($a=\frac{(a^3)^2}{a^5}$) but $a^3,a^6\in\mathbb Q$ ⇏ ($a=\sqrt[3]2$); $a+b\in\mathbb Q, ab\notin\mathbb Q$ ⇒ $a-b\notin\mathbb Q$ ✓. 若 $a,b$ 無理且 $a+b$ 有理 ⇒ $2a+3b=2(a+b)+b$ 必無理 (99 綜合練習); $a+b,b+c,c+a\in\mathbb Q$ ⇒ $a+b+c\in\mathbb Q$ ✓. $a$ 無理, $c$ 有理 ⇒ $a+c$ 無理 ✓; $a+b$, $ab$ 不一定無理; $cb$ 若 $c=0$ 為有理.
- 大小比較 (2014學測): $\sqrt{13}>3.5$ ✓ ($3.5^2=12.25$), $\sqrt{13}<3.6$ ✗ ($3.6^2=12.96<13$), $\sqrt{13}-\sqrt3>\sqrt{10}$ ✗, $\sqrt{13}+\sqrt3>\sqrt{16}$ ✓, $\frac{1}{\sqrt{13}-\sqrt3}>0.6$ ✗ → Ans (1)(4). Method: square both sides when both positive; 有理化.
- $\sqrt{10+n}-\sqrt{10}<\sqrt{10}-\sqrt{10-n}$ (rationalize: $\frac{n}{\sqrt{10+n}+\sqrt{10}}<\frac{n}{\sqrt{10}+\sqrt{10-n}}$). Also $\sqrt6$ 比較接近 $\sqrt7$ (concavity of $\sqrt x$). $\sqrt4+\sqrt5>\sqrt3+\sqrt6$.
- 黃金比例 (維特魯威人): $\frac{AB}{BC}=\frac{BC}{AC}=\varphi$ ⇒ $\varphi=\frac{\sqrt5-1}{2}$ (as ratio <1); height 150 cm, navel 90 cm → 高跟鞋 7 cm.
- 「最簡分數分子分母差 7，四捨五入得 0.5」→ $\frac{6}{13}$ 或 $\frac{8}{15}$; 「和為70，四捨五入0.6」→ $\frac{23}{47}$.

### 1.3 乘法公式與因式分解
- 完全平方 $(a\pm b)^2=a^2\pm2ab+b^2$; 平方差 $(a+b)(a-b)=a^2-b^2$; 完全立方 $(a\pm b)^3=a^3\pm3a^2b+3ab^2\pm b^3$; 立方和 $(a+b)(a^2-ab+b^2)=a^3+b^3$; 立方差 $(a-b)(a^2+ab+b^2)=a^3-b^3$; $(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)$ (代換法 $A=a+b$).
- $a^2+b^2+c^2-ab-bc-ca=\frac12[(a-b)^2+(b-c)^2+(c-a)^2]\ge0$.
- 因式分解 examples: $x^6-y^6=(x+y)(x^2-xy+y^2)(x-y)(x^2+xy+y^2)$; $64a^6-b^6$; $x^4+4=(x^2+2x+2)(x^2-2x+2)$, $x^4+64=(x^2+4x+8)(x^2-4x+8)$ (配方成平方差); $9x^4+11x^2+4=(3x^2+x+2)(3x^2-x+2)$; $a^4+a^2b^2+b^4=(a^2+ab+b^2)(a^2-ab+b^2)$; $x^2-y^2+6yz-9z^2=(x+y-3z)(x-y+3z)$; $x^3+x^2+x+1=(x+1)(x^2+1)$; $x^4+2x^3+2x^2+x+1$… $=(x^2+1)(x^2+x+1)$.
- 對稱式求值: $x+\frac1x=6$ ⇒ $x^2+\frac1{x^2}=34$, $x^3+\frac1{x^3}=6^3-3\cdot6=198$; $x-\frac1x=4$ ⇒ 18, 76. $x=\frac{\sqrt3+\sqrt2}{\sqrt3-\sqrt2}$, $y$ = its reciprocal ⇒ $x+y=10$, $xy=1$, $x^2+y^2=98$, $x^3+y^3=970$. $a+b=5,ab=2$ ⇒ $a^3+b^3=95$; $a-b=-1,a^2+b^2=5$ ⇒ $a^3-b^3=-7$.
- $a=\frac{1+\sqrt5}{2}$ ⇒ $a^2-a-1=0$ ⇒ $a^3=2a+1$, $a^4=3a+2$ (降次). 多選: $x=\frac{\sqrt5+1}{2}$ 與 $\frac1x+1$, $x^2-1$, $\frac1{x-1}$ 相等.
- 分式: 通分、約分, e.g. $\frac{x+1}{x-1}-\frac{x-1}{x+1}=\frac{4x}{(x-1)(x+1)}$.

### 1.4 根式
- $a\ge0$ 的平方根 $\pm\sqrt a$; $\sqrt{ab}=\sqrt a\sqrt b$, $\sqrt{\frac ab}=\frac{\sqrt a}{\sqrt b}$ ($a,b\ge0$, $b>0$); **$\sqrt{a^2}=|a|$** (key trap). 立方根: 被開方數與立方根同號 ($\sqrt[3]{-8}=-2$).
- 最簡根式 $\frac qp\sqrt n$ ($n$ 無平方因數); 同類方根 can be combined.
- 有理化因子: $\sqrt a+\sqrt b\leftrightarrow\sqrt a-\sqrt b$; $\sqrt[3]a\pm\sqrt[3]b\leftrightarrow\sqrt[3]{a^2}\mp\sqrt[3]{ab}+\sqrt[3]{b^2}$.
- **二重根號**: $\sqrt{(p+q)+2\sqrt{pq}}=\sqrt p+\sqrt q$; $\sqrt{(p+q)-2\sqrt{pq}}=|\sqrt p-\sqrt q|$. E.g. $\sqrt{11+2\sqrt{30}}=\sqrt6+\sqrt5$, $\sqrt{6-2\sqrt5}=\sqrt5-1$, $\sqrt{10-\sqrt{84}}=\sqrt7-\sqrt3$, $\sqrt{9+\sqrt{72}}$… $=\sqrt6+\sqrt3$, $\sqrt{2+\sqrt3}=\frac{\sqrt6+\sqrt2}{2}$ (先乘 $\frac{\sqrt4}{\sqrt4}$: $\sqrt{\frac{4+2\sqrt3}{2}}$).
- 化簡 with $\sqrt{a^2}=|a|$: $1<a<3$ ⇒ $\sqrt{(a-1)^2}-\sqrt{(a-3)^2}=2a-4$; $\frac23<x<\frac34$ ⇒ $\sqrt{9x^2-12x+4}+\sqrt{4x^2+4x+1}-\sqrt{16x^2-24x+9}=8x-3$ (99 form).
- 整數部分/小數部分: $\frac1{3-\sqrt5}=\frac{3+\sqrt5}4$ ⇒ 整數部分 $a=1$, 小數部分 $b=\frac{\sqrt5-1}{4}$; $a=\sqrt{41-12\sqrt5}=6-\sqrt5$, 純小數部分 $b=3-\sqrt5$ ⇒ $\frac a4+\frac1b=\frac{6-\sqrt5}4+\frac{3+\sqrt5}4=\frac94$. 小數部分 $b$ 滿足 $0\le b<1$; $a^2+b^2=38$ (a 實數, b 為其小數部分) ⇒ 整數部分 6 ⇒ $a+b=2\sqrt{10}$.
- $a^2+b^2+2a-4b+5=0$ ⇒ $(a+1)^2+(b-2)^2=0$ ⇒ $(a,b)=(-1,2)$ (配方+平方和為0).
- 化簡 $\sqrt{x^2+\frac1{x^2}-2}+\sqrt{x^2+\frac1{x^2}+2}$ ($0<x<1$) $=|x-\frac1x|+|x+\frac1x|=\frac2x$.

### 1.5 算幾不等式 (N-10-3)
- $a,b\ge0$: $\frac{a+b}{2}\ge\sqrt{ab}$, 等號 ⇔ $a=b$. Proof: $\frac{a+b}2-\sqrt{ab}=\frac12(\sqrt a-\sqrt b)^2\ge0$. 幾何: 半圓直徑 $\overline{AB}$ 上點 P, $\overline{AP}=a,\overline{PB}=b$, 垂線 $\overline{PQ}=\sqrt{ab}$ (母子相似) ≤ 半徑 $\frac{a+b}2$. Also 平行四邊形面積 picture.
- 題型 「和定積最大／積定和最小」: 周長20矩形最大面積25 (正方形); $2a+3b=8$ ⇒ $ab\le\frac83$ at $(2,\frac43)$; $xy=6$ ⇒ $3x+2y\ge12$ at $(2,3)$; $3a+4b=12$ ⇒ $ab\le3$ at $(2,\frac32)$; $ab=18$ ⇒ $a+2b\ge12$ ($a=6,b=3$).
- 應用: 66 m 籬笆圍菜園(BC 留 2 m 出入口): $2x+2y-2=66$ ⇒ $x+y=34$ ⇒ 面積 ≤ 289 at $x=y=17$; 半徑8半圓內接矩形最大面積 64; 高5、體積245 長方體盒最省材料 → 長寬各7.
- 注意 equality must be attainable (see §2.4 trap with 算幾 twice).

### 1.6 Enrichment — 簡單數論 (資優 第1單元) [mostly outside 數A; appears embedded in 學測-era problems]
- 除法原理: $a=bq+r$, $0\le r<|b|$ unique (e.g. $-9=5(-2)+1$). 整除 $b|a$; $a|b,b|c\Rightarrow a|c$; $a|b,a|c\Rightarrow a|mb+nc$. Note: $a|b+c$ ⇏ $a|b$ and $a|c$; $a|bc$ ⇏ $a|b$ or $a|c$ (unless $a$ prime).
- 質數 (2 is the only even prime; 無限多), 篩法: 合數 $a$ 必有 $\le\sqrt a$ 的質因數 (check 313, 409 by primes ≤ √). 標準分解式 $n=p_1^{\alpha_1}\cdots p_k^{\alpha_k}$. 正因數個數 $\prod(\alpha_i+1)$, 正因數和 $\prod\frac{p_i^{\alpha_i+1}-1}{p_i-1}$. E.g. $5292=2^2 3^3 7^2$: 36 個, 和 15960; 正因數中完全平方數 8 個. $1260x$ 為完全平方 → $x_{\min}=35$. 含12個正因數的最小自然數 60.
- 倍數判別: 3/9 (digit sum), 4 (末二位), 8 (末三位), 11 (奇偶位和差), 99 (two-digit blocks). E.g. 23ab421 為99倍數 → a=2,b=4; 12a49b 為36倍數 → (0,2),(9,2),(5,6).
- gcd/lcm: $(b,c)$, $[b,c]$; $(a,b)[a,b]=ab$ (not for three numbers); $a=dh,b=dk,(h,k)=1$. 輾轉相除法 $(a,b)=(b,r)$; (38254,60466)=1234; (3431,2397)=47, lcm 174981; 表現定理 $d=am+bn$ (3431·7+2397·(−10)=47). $ax+by=c$ 有整數解 ⇔ $(a,b)|c$ (5克、7克砝碼可稱1克、13克).
- $p$ prime, $p|ab$ ⇒ $p|a$ or $p|b$; $a|bc,(a,b)=1$ ⇒ $a|c$.
- 整除求值: $(2a-1)|(5a+1)$ and $(a+2)|(5-2a)$ ⇒ $a=1$ or $-3$; $\frac{k-15}{2k-3}$ 正整數 → $k=1,0,-3,-12$.
- 整數分類 mod $k$; 完全平方數 mod 4 ∈{0,1}, mod 5 ∈{0,1,4}, mod 6 ∈{0,1,3,4}; $3n+2$ 不是平方數; $11,111,\dots$ 無平方數 (mod 4 ≡3).
- 韓信點兵 / 中國剩餘定理: 除以7,6,5 餘5,1,2 → 最小187. $x\equiv2\ (5),3\ (7),4\ (11)$ → $x\equiv367\pmod{385}$.
- 同餘 $a\equiv b\pmod n$ properties (加減乘、可約條件 $(c,m)=1$). 費馬小定理 $a^p\equiv a$, $(a,p)=1⇒a^{p-1}\equiv1$; Wilson $(p-1)!\equiv-1$; 費馬數 $F_5=641\times6700417$; $2^{11}-1=23\times89$ (Mersenne: $2^k-1$ prime ⇒ k prime, converse false).
- Classic 學測 items: $2^{100}$ 除以10 餘 6 (88學測); $40^{255}$ mod 13 → 1 (85學科); 43569 有 3 個質因數 (94學測); 足球16分/6分可得 28, 82, 284 (90學科); a 92學測 item counting $n$ that make a fraction an integer (reduce to 「$n$ 整除某常數」, Ans 4 個); $(a,b)=(b,r)$ 與 $(a,q)=(q,r)$ 為真 (90學科); 2000/1/1 星期六 → 下次 2005 年; 天干地支 2039=己未; 400 m 跑道相遇第8次 320 秒.
- 質數求值: $n^4-6n^2+25=(n^2+4n+5)(n^2-4n+5)$ 為質數 ⇒ $n=\pm2$, 質數 17; $\sqrt{x^2+21}$ 自然數 ⇒ $x=2,10$.
- 檢查碼: ISBN-10 $\sum i\cdot n_i\equiv0\pmod{11}$; 身分證字號 check digit formula (英文字母轉兩位數，權重 1,9,8,…,1).
- $1+\frac12+\dots+\frac1n$ 不是整數 ($n>1$).

---

## 2. 絕對值、分點公式、絕對值方程式與不等式（附：不等式總整理）

**Scope**: N-10-2 絕對值 (以 $|x-a|\le b$、$|x-a|\ge b$ 為原則，連結誤差範圍; 區間符號含 ∪ 與 ±∞，不做區間集合運算); F-10-1 (分點公式 on 數線); G-11A-4 (實數三角不等式). **Sources**: 108一上 1-2絕對值; 99第一冊 1-2數線上的幾何; 資優 第2單元 (絕對值部分), 第54單元簡單不等式.

### 2.1 定義與幾何意義
- $|a|=a$ ($a\ge0$), $-a$ ($a<0$); $|a|$ = 點 $A(a)$ 到原點距離; $\overline{AB}=|a-b|$ (右減左).
- Properties: $-|a|\le a\le|a|$; $|ab|=|a||b|$; $|\frac ab|=\frac{|a|}{|b|}$; $\sqrt{a^2}=|a|$; $|a|^2=a^2$.
- **三角不等式**: $\big||a|-|b|\big|\le|a\pm b|\le|a|+|b|$; $|a+b|=|a|+|b|$ ⇔ $ab\ge0$.
- $|x|=a\ (a\ge0)$ ⇔ $x=\pm a$; $|x|\le a$ ⇔ $-a\le x\le a$; $|x|\ge a$ ⇔ $x\ge a$ 或 $x\le-a$.
- 情境: 產品標示 39 克 ±9% ⇒ $|W-39|\le39\times0.09$; 尺寸 ±5% ⇒ $|V-V_0|\le0.05V_0$. 「b 代表誤差範圍」.
- 區間符號: $[a,b]$, $(a,b)$, $[a,b)$, $[a,\infty)$, $(-\infty,b]$, $\cup$. E.g. $|x-2|\ge3$ → $[5,\infty)\cup(-\infty,-1]$.

### 2.2 數線分點公式 (F-10-1)
- $P$ 在 $\overline{AB}$ 上, $\overline{AP}:\overline{PB}=m:n$ ⇒ $x=\frac{na+mb}{m+n}$ (內插法原理). 外分點: solve with signed ratio or $|x-a|:|x-b|=m:n$ and $P$ outside.
- 例: $A(-7),B(3)$, $\overline{AP}:\overline{PB}=3:2$ → 內分 $x=\frac{2(-7)+3\cdot3}{5}=-1$; 外分 (P beyond B) $\frac{x+7}{x-3}=\frac32$ ⇒ $x=23$. (Handout answer line prints 「(1)3」; the correct internal point is $-1$.)
- $A(-5),B(11)$, $AP:BP=5:3$ → $x=5$; external $y=35$. $p=\frac{3a+2b}{5}$ ⇒ $AP:BP=2:3$.
- 2014指定乙 多選: $b=\frac45a+\frac15c$ ⇒ $b$ 在 $a,c$ 之間 且 $\overline{AB}:\overline{BC}=1:4$; $d=\frac43a-\frac13c$ 在 $a,c$ 外; $|b|=\frac45|a|+\frac15|c|$ ⇏ $abc>0$ (only same sign: a=−6,b=−5,c=−1 counterexample) → Ans (1)(4).
- 99 多選: $C=\frac{2a+3b}{5}$, $D=\frac{3a+2b}{5}$ with $a<b$: $\overline{AB}=|a-b|$ ✓, D 在 C 左方 ✓, $\overline{AD}=\overline{BC}$ ✓.

### 2.3 絕對值方程式與不等式
- Two viewpoints: 幾何 (distance on 數線) and 代數 (分段討論 by sign).
- $|2x+1|=5$ ⇔ $|x+\frac12|=\frac52$ ⇒ $x=2,-3$. $|x-2|<3$ ⇒ $-1<x<5$. $|2x+3|\le5$ ⇒ $-4\le x\le1$. $|x-1|\ge|x+2|$ ⇒ $x\le-\frac12$ (平方或中點). $|x-1|\ge|2x+3|$ ⇒ $-4\le x\le-\frac23$. $3\le|x+1|<5$ ⇒ $2\le x<4$ 或 $-6<x\le-4$. $5<|2x-1|<33$ ⇒ $3<x<17$ 或 $-16<x<-2$.
- **距離和** $|x-a|+|x-b|$: min $=|a-b|$ attained for $x$ between $a,b$; $=k$ has solutions ⇔ $k\ge|a-b|$. E.g. ants $A(-3),B(2),C(x)$ 距離和14 ⇒ $|x-2|+|x+3|=9$ ⇒ $x=4,-5$; $|x+3|+|x-2|\ge9$ ⇒ $x\le-5$ or $x\ge4$; $|x-1|+|x-5|=8$ ⇒ $x=7,-1$; $\le8$ ⇒ $-1\le x\le7$; $|x+2|+|x-5|=k$ 有解 ⇔ $k\ge7$; 機器人 A(−2),B(4) 距離和 ≤12 ⇒ $-5\le x\le7$.
- **距離差** $|x-a|-|x-b|$ ranges over $[-|a-b|,|a-b|]$: $|x+1|-|x-3|=2,-1$ 有解, $=10$ 無解.
- $|x+5|=2|x-4|$ ⇒ $x=13$ or $1$. $|x+3|+|2x-5|=10$ ⇒ $x=4,-2$. $|4x-12|\le2x$ ⇒ $2\le x\le6$, 區間長 4 (2014學測).
- 反求係數: $|ax+1|\le b$ 解為 $-1\le x\le5$ (i.e. $|x-2|\le3$) ⇒ $-\frac1a=2$, $\frac b{|a|}=3$ ⇒ $a=-\frac12,b=\frac32$; $|ax-2|\ge b$ 解 $x\le0$ 或 $x\ge\frac43$ ⇒ $a=3,b=2$; $|ax+3|\le b$ 解 $[-3,7]$ ⇒ $a=-\frac32,b=\frac{15}2$; $|2x-a|\le b$ 解 $[-2,5]$ ⇒ $a=3,b=7$. Method: midpoint ↔ center, half-length ↔ radius.
- 範圍運算: $|x+1|\le3$, $|y-2|\le1$ ⇒ $-7\le2x+y\le7$, $-12\le xy\le6$, $-13\le x-3y\le-1$, $\frac13\le\frac1y\le1$ (don't subtract ranges naïvely; $xy$ check endpoint products).
- 整數解: $3|a+1|+2|b-3|+|c+4|=2$; $|x+2|+2|y|=3$ (6 組).
- 集合: $A=\{x\,|\,|x-a|\le2\}\subset B=\{x\,|\,|x-3|\le5\}$ ⇒ $0\le a\le6$.
- 證明: $|a|,|b|<1$ ⇒ $|a+b|+|a-b|<2$; $ab+1>a+b$ ($(1-a)(1-b)>0$); $abc+2>a+b+c$. $\frac{|a+b|}{1+|a+b|}\le\frac{|a|}{1+|a|}+\frac{|b|}{1+|b|}$ ($f(x)=\frac x{1+x}$ increasing & subadditive).

### 2.4 不等式總整理 (資優 第54單元; parts beyond 數A flagged)
- **算幾不等式 (n 項)**: $\frac{a_1+\dots+a_n}{n}\ge\sqrt[n]{a_1\cdots a_n}$, 等號 ⇔ 全相等 (proof n=2 → 4 → 2^k → 歸納/backward). n≥3 versions are enrichment; 學測 uses mainly 2-term.
  - $x+y+z=1$ ⇒ $xyz\le\frac1{27}$; $x^2yz\le\frac1{64}$ (split $x=\frac x2+\frac x2$). $3x+2y+z=12$ ⇒ $xyz\le\frac{32}{3}$ at $3x=2y=z=4$; $x^3y^2z\le64$ at $(2,2,2)$ (6 terms $x,x,x,y,y,z$ each 2). $xy^2=2$ ⇒ $2x+y^2\ge4$; $2x+y\ge3$ at $x=\frac12,y=2$. $(2-x)^3(x+3)^2$ on $[-3,2]$ max 108 at $x=-1$. 表面積54長方體最大體積27. $x^3y^2z=576$ ⇒ $x+2y+3z\ge12$. $-\frac12<x<\frac52$: $(2x+1)(5-2x)^2\le32$ (set $a=2x+1,b=5-2x$, $a+b=6$, max $ab^2$ at $a=2,b=4$).
  - **Trap** (例題4 討論): using 算幾 twice and multiplying gives a bound whose equality cases conflict → not the true minimum. Always check equality simultaneously attainable. Correct: $\frac1x+\frac4y+\frac9z\ge36$ when $x+y+z=1$ (柯西), at $(\frac16,\frac13,\frac12)$.
  - $x>-1$: $x+\frac{4}{x+1}=(x+1)+\frac4{x+1}-1\ge3$ at $x=1$. $\cos x+\frac4{\cos x}$ on $(-\frac\pi2,\frac\pi2)$: min not 4 (cos≤1 ⇒ min 5 at x=0) — 多選 trap. 閃黃燈 $f(v)=1+\frac{v}{10}+\frac{90}{v}\ge7$, equality $v=30$; $f(60)=8.5$.
  - $3^x+3^y$ with $x+y=1$, $x,y\ge0$: $2\sqrt3\le\cdot\le4$.
- **柯西不等式**: $(a_1^2+\dots+a_n^2)(b_1^2+\dots+b_n^2)\ge(a_1b_1+\dots+a_nb_n)^2$, 等號 ⇔ $(a_i)\parallel(b_i)$. Proofs: Lagrange identity; 內積 $|\vec a\cdot\vec b|\le|\vec a||\vec b|$; 判別式 of $\sum(a_ix-b_i)^2\ge0$.
  - $x^2+y^2+z^2=9$ ⇒ $2x-y+3z\le3\sqrt{14}$ at $(\frac6{\sqrt{14}},\frac{-3}{\sqrt{14}},\frac9{\sqrt{14}})$; $x+y+kz$ max $3\sqrt6$ ⇒ $k=\pm2$. $a^2+4b^2+9c^2=100$ ⇒ $a+2b-3c\in[-10\sqrt3,10\sqrt3]$. $\frac{x^2}4+y^2=1$ ⇒ $x+2y\le2\sqrt2$. $2x+3y=1$ ⇒ $x^2+y^2\ge\frac1{13}$ (also 幾何: distance from O to line; or 代入配方). $a^2+b^2=4$ ⇒ $(a-3)^2+(b+4)^2\ge9$ (circle to point distance $5-2=3$).
  - $x+y-2z=4$ ⇒ $x^2+y^2+z^2-2x+4y+1=(x-1)^2+(y+2)^2+z^2-4$, with $(x-1)+(y+2)-2z=5$ ⇒ min $\frac{25}6-4=\frac16$. $\sqrt a+\sqrt b+\sqrt c$ with $a+b+c=8$, $a,b,c\ge0$: max $2\sqrt6$, min $2\sqrt2$ (min by expansion, not 柯西 lower bound).
- 代數技巧: 配方 ($x^2+y^2+z^2-2x+6y-10z+50\ge15$ at $(1,-3,5)$; $a^2+b^2+(2a-b-3)^2\ge\frac32$; $x^2+xy+y^2-2x+4y-1$ min at $(\frac83,-\frac{10}3)$), $a^4+b^4+c^4\ge a^2b^2+b^2c^2+c^2a^2$, $(a+b)(b+c)(c+a)\ge8abc$, $\frac c{a+b}+\frac a{b+c}+\frac b{c+a}\ge\frac32$ (Nesbitt), $abc\ge(a+b-c)(b+c-a)(c+a-b)$, 周長固定以正三角形面積最大 (海龍 + 算幾).
- 分式不等式: $\frac{f}{g}>0$ ⇔ $fg>0$; $\frac fg\ge0$ ⇔ $fg>0$ or $f=0$; general $\frac fg>h$ ⇔ $g(f-hg)>0$. E.g. $\frac{x+2}{x-1}>0$ ⇒ $x<-2$ or $x>1$; $\frac3{x-2}>x$ ⇒ $x<-1$ or $2<x<3$; $\frac2x>x+1$ ⇔ $x(x-1)(x+2)<0$.
- 根式不等式 (types): $\sqrt f>\sqrt g$ ⇔ $f>g\ge0$; $\sqrt f>g$ ⇔ ($g<0$ & $f\ge0$) or ($g\ge0$ & $f>g^2$); $\sqrt f<g$ ⇔ $f\ge0$, $g>0$, $f<g^2$. E.g. $\sqrt{x^2-25}>x-1$ ⇒ $x\le-5$ or $x>13$; $x+2<\sqrt{10-x^2}$ ⇒ $-\sqrt{10}\le x<1$.
- 凹凸性 (Jensen form): 凹向上 ⇔ $f(\frac{x_1+x_2}2)\le\frac{f(x_1)+f(x_2)}2$. 多選: $2^{\frac{a+b}2}<\frac{2^a+2^b}2$ ✓, $\log\frac{a+b}2>\frac{\log a+\log b}2$, $\sin$ concave on $[0,\pi]$; $\tan$ convex on $[0,\frac\pi2)$.
- 判別式法求值域: $y=\frac{x^2-x+1}{x^2+x+1}$ ⇒ $\frac13\le y\le3$; $\frac{x^2-4x+5}{x^2+2x+6}$ ⇒ $\frac{15-\sqrt{205}}{10}\le y\le\frac{15+\sqrt{205}}{10}$.
- 「必要條件」多選: $a<b,c<d$ 的必要條件 $a+c<b+d$, $(b-a)(c-d)<0$. $a>b,c>d$ ⇒ $ac>bd$ needs 乙(b>0)與丙(c>0) both (Ans 4). $0<a,b<1$ ⇒ $0<a+b<2$, $0<ab<1$, $|a-b|<1$ (91學測補 Ans 1,2,5).
- 鈍角三角形邊長 $14-x,18-x,22-x$ ⇒ $2<x<10$ (需三角形成立 & 最大邊平方 > 其他平方和).
- (Exponential/log/trig inequalities from this unit are filed in §15 and §14.)

---

## 3. 指數與常用對數

**Scope**: N-10-3 指數 (非負實數之小數或分數次方、實數指數、計算機 $y^x$ 鍵), N-10-4 常用對數 (log 的意義、與科學記號連結、$10^x$/log 鍵; 「任意正數 a 可寫成 $10^{\log a}$」; 不談其他底). N-10-1 科學記號/有效位數 (★). General-base 對數律 is A-11A-4 → see §15. **Sources**: 108一上 1-3指數, 1-4常用對數; 99第一冊 3-1指數, 3-3對數; 資優 第12單元指數, 第13單元對數, 第15單元對數表的應用.

### 3.1 指數的推廣 (principle: 新定義仍須滿足指數律)
- 正整數指數: $a^ma^n=a^{m+n}$, $(a^m)^n=a^{mn}$, $a^nb^n=(ab)^n$; $\frac{a^m}{a^n}=a^{m-n}$.
- 整數指數 ($a\ne0$): $a^0=1$, $a^{-n}=\frac1{a^n}$ — forced by $a^0a^n=a^n$, $a^{-n}a^n=a^0$. 指數律 still hold for integer exponents.
- 有理指數 ($a>0$): $a^{\frac1n}=\sqrt[n]a$ = the unique positive root of $x^n=a$ (exists & unique by 勘根/單調); $a^{\frac mn}=\sqrt[n]{a^m}=(\sqrt[n]a)^m$. Model: 細菌 $2\times3^t$ (3日後54, 5日後486 ⇒ $k=3$, 初始 2, 4日前 $\frac2{81}$); $3^{\frac13}$ = 8小時後倍率.
- **Why $a>0$**: $(-3)^{\frac12}=\sqrt3 i$ but $(-3)^{\frac24}=\sqrt[4]9$ real → 「迷惑一」; $(-16)^{\frac14}$ undefined. Fraction-exponent laws break for negative bases.
- 實數指數: $3^{\sqrt2}=\lim 3^{1.4},3^{1.41},3^{1.414},\dots\approx4.7288$; $2^{\sqrt3}\approx3.3220$. 指數律 hold for real exponents with positive bases.
- **大小**: $a>1$: $p<q⇒a^p<a^q$; $0<a<1$: $p<q⇒a^p>a^q$. Proof for rationals: raise to common power (e.g. compare $(1.6)^{\frac23}$ vs $(1.6)^{\frac34}$ via 12th powers: $1.6^8<1.6^9$).
- 化簡技巧: write as prime-power products (e.g. $3^5\cdot10^9\cdot12^{\dots}=2^x3^y$ → $(x,y)=(20,31)$); $\sqrt[3]4\cdot\sqrt[4]{\dots}$ → common root index ($\sqrt[3]{3}\cdot\sqrt[4]{3}$ etc.; $\sqrt3\cdot\sqrt[3]4=\sqrt[6]{432}$).
- 對稱式: $a^{\frac12}+a^{-\frac12}=6$ ⇒ $a+a^{-1}=34$, $a^2+a^{-2}=1154$; $=3$ ⇒ 7, 47, $a^3+a^{-3}=322$; $=5$ ⇒ $a+a^{-1}=23$, $a^{\frac32}+a^{-\frac32}=5(23-1)=110$, $a^2+a^{-2}=527$. $a^{3x}+a^{-3x}=52$ ⇒ $t=a^x+a^{-x}$: $t^3-3t=52$ ⇒ $t=4$, $a^{2x}+a^{-2x}=14$, $a^x=2\pm\sqrt3$. $x^{\frac12}+x^{-\frac12}=\sqrt6$ ($x>1$) ⇒ $x^{\frac12}-x^{-\frac12}=\sqrt2$, etc.
- $67^x=27$, $603^y=81$ ⇒ $27^{1/x}=67$, $81^{1/y}=603$ ⇒ $3^{\frac3x-\frac4y}=\frac{67}{603}=\frac19$ ⇒ $\frac3x-\frac4y=-2$. Same pattern: $53^x=9$, $477^y=243$ ⇒ $\frac2x-\frac5y=-2$ ($477=9\cdot53$); $333^x=9$, $37^y=27$ ⇒ $\frac2x-\frac3y=2$.
- $2^a=3^b=6^c$ ($c\ne0$) ⇒ $\frac1a+\frac1b=\frac1c$; $a^x=b^y=(ab)^z$ ⇒ $\frac1x+\frac1y=\frac1z$ (take logs / set common value $t$).
- $f(x)=\frac{4^x}{4^x+2}$ ⇒ $f(a)+f(1-a)=1$ ⇒ $\sum_{k=1}^{1999}f(\frac k{2000})=\frac{1999}2$.
- 指數方程 (99/資優): $2^{x+4}=7^{x+4}$ ⇒ $x=-4$; $5^{2x+1}-6\cdot5^x+1=0$ ⇒ $x=0,-1$; $2(4^x+4^{-x})-7(2^x+2^{-x})+10=0$ ⇒ $t=2^x+2^{-x}\ge2$: $2(t^2-2)-7t+10=0$ ⇒ $t=2$ ($t=\frac32<2$ 不合) ⇒ $x=0$; $4(4^x+4^{-x})-12(2^x+2^{-x})+13=0$ ⇒ $x=\pm1$; $(2+\sqrt3)^x+(2-\sqrt3)^x=4$ ⇒ $x=\pm2$ ($(2+\sqrt3)(2-\sqrt3)=1$); $6^x-8\cdot3^x-9\cdot2^x+72=0$ ⇒ $(2^x-8)(3^x-9)=0$ ⇒ $x=3$ or $2$ (分組因式分解); $2^x+3^y=8$, $2^{x+1}+\frac13 3^y=5$ ⇒ $5\cdot3^y-5\cdot2^x=26$.
- 應用 (108): 半衰期6日: $n$ 日後是 $n+3$ 日後的 $\sqrt2$ 倍, 30日後是60日後的 $2^5=32$ 倍, 3個月後量 N → 66 天後量 16N; 止痛藥 $y=(\frac12)^{h/3}$ 達 $\frac1{64}$ ⇒ $\frac h3=6$ ⇒ 18 小時 (handout answer key prints 12 — misprint). 牛頓冷卻 $T=25+169a^t$, 2分鐘125°C ⇒ $a=\frac{10}{13}$, 10分鐘≈37°C. 表面積 $S=kM^{2/3}$ (70 kg, 18600 cm² ⇒ $k\approx1095.1$). 獅子地盤 $T=W^{1.31}$; 議會規模立方根法則 $N=P^{1/3}$ (台灣 ≈ 287). 汙染模型 $P=1000\,t^{5/4}+14000$ (1980 後 t 年): 81 年後 $1000\cdot3^5+14000=257000$; 達 46000 ⇒ $t^{5/4}=32$ ⇒ $t=16$ (1996 年) — a power function, not exponential; 波德法則 $d=\alpha+\beta\cdot2^n$ ($\alpha=0.4,\beta=0.3$; 火星1.6, 天王星19.6, 穀神星 $n=3$, 水星0.4 AU). Logistic 廣告 $P(t)=\frac{100}{1+24(2.71)^{-0.28t}}\%$ ($P(0)=4\%$). 10莫耳米灑地球表面 → 高度 ≈ 總統府 (order of magnitude).

### 3.2 科學記號、位數與有效數字 (N-10-1, N-10-4)
- 正數 $=a\times10^n$, $1\le a<10$, $n\in\mathbb Z$. $n\ge0$ ⇒ 整數部分 $n+1$ 位數; $n=-k$ ⇒ 小數點後第 $k$ 位開始不為0. 「$n$ 位有效數字」: coefficient rounded to $n-1$ decimals (e.g. 23,580,833 → $2.36\times10^7$ to 3 sig. figs; the handout answer prints 2.35, a rounding slip). Software notation `aE+n`.
- $10^{23.4}$ 整數部分 24 位; $10^{-13.7}$ 小數點後第 14 位; $10^{17.3}$ → 18 位; $10^{-14.1}$ → 第15位; $10^{8.91}$ 是 9 位數; $10^{-6.12}$ 第 7 位.
- Voyager 1 距離 $3\times10^8\times(16h23m20s)\approx1.77\times10^{13}$ m (14位數、3位有效). 2.7 μm / 54 nm = 50 倍.

### 3.3 常用對數 (base 10)
- 定義: $p>0$, $p=10^a$ ⇔ $a=\log p$; hence $p=10^{\log p}$, $\log10^n=n$, $\log1=0$. Found by 十分逼近法 on calculator ($10^{0.301}<2<10^{0.302}$ ⇒ $\log2\approx0.301$).
- Values to memorize (printed on 學測 formula sheet): $\log2\approx0.3010$, $\log3\approx0.4771$, $\log7\approx0.8451$ ⇒ $\log4=0.6020$, $\log5=0.6990$, $\log6=0.7781$, $\log8=0.9030$, $\log9=0.9542$.
- 對數律 (proved from 指數律 in 108 1-4 習題18): $\log mn=\log m+\log n$, $\log\frac mn=\log m-\log n$, $\log m^t=t\log m$.
- 落在哪兩整數間: $\log21970\in(4,5)$, $\log0.000357\in(-4,-3)$, $\log1409\in(3,4)$, $\log0.0314\in(-2,-1)$.
- **位數 / 首位數字**: $x=10^{k}$ with $k=n+f$ ($0\le f<1$) ⇒ $x$ has $n+1$ 位 (if $n\ge0$); 首位數字 $d$ where $\log d\le f<\log(d+1)$.
  - $2^{127}-1$: $127\times0.30103\approx38.23$ ⇒ 39 位數 (Lucas 1876); $2^{61}-1$ 19 位; $2^{607}-1$ 183 位; 1TB $=2^{40}$ byte 13 位數.
  - $7^{100}$: $\log=84.51$, $f=0.51\in(\log3,\log4)$ ⇒ 85 位數, 首位數字 **3** (資優 15 prints 2 — misprint since $0.51>\log3=0.4771$).
  - $(\frac23)^{20}$: $\log=-3.522=-4+0.478$ ⇒ 小數點後第4位開始不為0, 該數字 3. $2^{26}\cdot3^{16}$ 16 位數; $2^{26}+3^{16}=110155585$ 9 位數. $25^{16}+16^{25}$: 31 位、首位 1. $47^{100}$ 168 位 ⇒ $1.67\le\log47<1.68$ ⇒ $47^{17}$ 29 位, $\frac1{47^{17}}$ 小數點後第29位. $1+2+\dots+2^{73}=2^{74}-1$: 23 位, 首位 1, 個位 3. $\sum_{k=1}^{100}(\frac12)^k$ 小數點後第31位開始不為9. $2^{6972593}-1$ 列印需 ≈700 張A4 (89學科).
  - 首數/尾數 (99 terminology): $\log x=n+\log a$; 首數 $n$ (integer) decides 位數, 尾數 $\log a\in[0,1)$ decides digits. $\log x=-2.65$ ⇒ 首數 $-3$, 尾數 $0.35$ (not $-0.65$). 尾數相同 ⇔ $x=y\cdot10^n$. 首數為2的正整數 900 個.
- **Applications (formula given in stem; compute with log)**:
  - pH $=-\log[H^+]$: pH 3 與 4 依 1:1 混合 → $[H^+]=5.5\times10^{-4}$, pH≈3.3; 3:2 → 3.2; pH 2 與 4 依 1:4 → ≈2.7. pH 5.1 vs 5.5: $10^{0.4}\approx2.5$ 倍.
  - 分貝 $d=10\log\frac I{I_0}$, $I_0=10^{-12}$: $10^2$ W/m² → 140 dB; 90 dB → $I=10^{-3}$; 一支 70 dB, 百支 → 90 dB (93指定乙). 蚊子 $10^{-12}$ → 0 dB; $10^{-4}$ → 80 dB.
  - 芮氏規模 $\log E=11.8+1.5M_L$: 宮城 9.0 → $E=10^{25.3}$ (26 位), 為集集 7.3 的 $10^{2.55}\approx355$ 倍. (Older form $r=\log I$: 921(7.3) vs 神戶(7.2) → $10^{0.1}\approx1.259$ 倍.)
  - 星等 $m-m_0=-2.5\log\frac F{F_0}$, $M=m+5-5\log d$: 金星(−4.4)/天狼星(−1.45) 亮度比 $10^{1.18}\approx15$; 牛郎星 16 光年 ⇒ 織女星 ≈25 光年; 牛郎星 $d=10^{0.714}$ 秒差距 ≈ 17 光年.
  - 班佛定律 首位數字 $a$ 的比例 $\log(1+\frac1a)$ (a=7 → 0.06). 步行速度 $v=0.26\log p+0.02$. 克利夫蘭 $27^\alpha=10$ ⇒ $\alpha=\frac1{\log27}\approx0.7$; 感覺10倍 → 實際≈27倍 (93指定乙). 對摺 A4 (0.05 cm) 超過101大樓 → 20 次; 0.01 cm 報紙到太陽 → 51 次.
  - 半衰期 / 複利: 碘131 半衰期8天 → 降為 $\frac16$ 需 ≈21 天 ($t=8(1+\frac{\log3}{\log2})$); 鐳 1600 年, 剩 $\frac34$ 需 ≈664 年; 碳14 5770 年, 剩 $\frac23$ ≈3376 年. 年利率 4.8% 每2月複利 5 年 → 10000×1.008^{30}≈12560; 日利率 2% 一年 → ≈1405 萬; 年息7% 20萬→30萬 需 6 年; 12.5% 翻倍需 6 年 (86聯考); 每年調薪 a% 使10年後加倍 → a=8 (91指定乙); 每週虧1%, 超過一半需 69 週 (89自然); 菌A每2小時×2, 菌B每3小時×3, B/A≈10 約117小時 (2007學測); 乙菌×4/日 vs 甲菌×2/日, 千倍需 10 天 (89社會); 「72規則」: 6%, 4%, 3% 符合 (8%, 9% 不符); 貸款100萬 月還1萬 月利0.6% → 13 年 (88大學自); 年金 1200 元 10 年 4% → 14944.8; 1000 元 20 年 5% → 34749.
  - 定位根: $4^x=100\cdot3^x$ ⇒ $x=\frac{2}{\log4-\log3}\approx16.01$ ∈ (16,17).
- 對數表 (資優15, 99-era; calculators replaced it in 108): 直接查表 (1.00–9.99), 表尾差 (4th digit), 反查表, **內插法** (linear: $\log1.346\approx0.1271+0.6\times0.0032=0.1290$; 108 notes 「理解內插法的原理是分點公式」). Product via logs: $\frac{3.67\times4.92\times7.25}{9.75\times8.72}\approx1.54$.

---

## 4. 直線方程式

**Scope**: G-10-2 直線方程式 (斜率及其絕對值的意義、點斜式、點與直線之平移、平行線/垂直線方程式、點到直線的距離、平行線的距離、二元一次不等式; 由 P、Q 坐標計算 △OPQ 面積); G-10-1 坐標圖形的對稱性 (only x軸, y軸, y=x, 原點 — the handouts also do 點對一般直線的對稱/反射 via 投影, which is fine as a distance/垂直 application); F-10-1 (分點公式). **Sources**: 108一上 2-1直線方程式及其圖形, 2-2直線方程式的應用; 99第三冊 2-1直線方程式; 資優 第3單元平面座標.

### 4.1 坐標基本公式
- 距離 $\overline{AB}=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$; 分點 $P$ 於 $\overline{AB}$, $\overline{PA}:\overline{PB}=m:n$ ⇒ $P=\big(\frac{nx_1+mx_2}{m+n},\frac{ny_1+my_2}{m+n}\big)$; 中點; 重心 $G=\big(\frac{x_1+x_2+x_3}3,\frac{y_1+y_2+y_3}3\big)$.
- 例: $P_1(3,-4),P_2(-1,5)$, $\overline{P_1P}:\overline{PP_2}=1:3$ (P 在直線 $P_1P_2$ 上) ⇒ 內分 $(2,-\frac74)$ or 外分 $(5,-\frac{17}2)$. 外心 of $A(1,3),B(4,2),C(5,7)$: $(\frac{13}4,\frac{19}4)$.
- 解析法證幾何: 中線定理 $\overline{AB}^2+\overline{AC}^2=2\overline{AM}^2+\frac12\overline{BC}^2$; 平行四邊形四邊平方和 = 兩對角線平方和; 三高共點; **Euler 線** (垂心H、重心G、外心O 共線; set $A(0,0),B(c,0),C(p,q)$).

### 4.2 斜率
- 定義: $m=\frac{y_2-y_1}{x_2-x_1}$ ($x_1\ne x_2$); 鉛直線斜率不定義. Independent of chosen points (相似三角形).
- 詮釋: 斜率 $k$ ⇒ x 每增加 $a$, y 增加 $ka$. $|m|$ = 傾斜程度; 左下→右上 正, 左上→右下 負, 水平 0. 斜率 ↔ 斜角 $m=\tan\theta$ (§12).
- $\frac{f(b)-f(a)}{b-a}$ for linear $f(x)=2011x+11$ is 2011 (平均變化率).
- **平行** $L_1\parallel L_2$ ⇔ $m_1=m_2$ (或皆鉛直); **垂直** ⇔ $m_1m_2=-1$ (proof by 畢氏 on lines through O meeting $x=1$, or 全等 △OAB≅△CDO). 三點共線 ⇔ 兩斜率相等.
- 例: $A(2,5),B(6,3),C(-a,2),D(10,a),E(11,a+1)$: $AB\parallel CD$ ⇒ $a=-2$; $AB\perp CD$ ⇒ $a=-22$; $A,C,E$ 共線 ⇒ $a=-5$ or $7$. $A(5,16),B(-1,k+7),C(k,0),D(1,-2)$: 平行 $k=3,7$; 垂直 $k=-3$; $A,B,C$ 共線 $k=-3,17$.
- 圖形判讀多選: 正五邊形 (EA∥x軸) 斜率大小 $m_{AB}>m_{CD}>m_{EA}>m_{BC}>m_{DE}$; 鳶形 ($AB=AD=2$, $BC=CD=4$, $AC=5$) → (B)(C)(E). **2009學測**: $L_1\perp L_3$, $L_3\parallel L_4$, lines $y=m_ix$ relative to $y=x$: true (2) $m_1m_4=-1$, (3) $m_1<-1$, (4) $m_2m_3<-1$.
- **2012學測**: $A(1,1),B(3,5),C(5,3)$, $D(0,-7),E(2,-3),F(8,-6)$; L 與兩三角形各恰一交點 ⇒ L passes through a vertex of each; 斜率最小可能值 $-3$ (line CF).

### 4.3 直線方程式
- 圖形的方程式: (1) 圖形上每點滿足 $f(x,y)=0$, (2) 每個解都在圖形上.
- **點斜式** $y-y_1=m(x-x_1)$; 兩點式; 鉛直線 $x=x_1$; **斜截式** $y=mx+b$; **截距式** $\frac xa+\frac yb=1$ ($ab\ne0$); **一般式** $ax+by+c=0$ (a,b 不全為0): $b=0$ 鉛直, else 斜率 $-\frac ab$, y 截距 $-\frac cb$.
- 平行/垂直於 $ax+by+c=0$: $ax+by=k$ / $bx-ay=k$. 例: 過 $(3,-2)$ 垂直 $5x-4y+1=0$ ⇒ $4x+5y=2$; x截距1 且平行於過 $(3,2),(-5,7)$ 的直線 ⇒ $5x+8y=5$; 垂心 of $A(-1,-10),B(2,-1),C(6,-3)$: $H(3,-2)$.
- 截距題: 過 $(2,6)$, 截距和 1 ⇒ $y-6=2(x-2)$ or $y-6=\frac32(x-2)$; 過 $(-3,1)$ 兩截距絕對值相等 ⇒ $x+y+2=0$, $x-y-4=0$, **$x+3y=0$ (過原點, 截距皆0 — don't forget)**; 過 $(3,-2)$ 截距相等 ⇒ $x+y=1$ 或 $2x+3y=0$; 垂直 $2x-y=3$ 且與兩軸圍面積2 ⇒ $x+2y=\pm2\sqrt2$; 斜率 $-\frac43$, 斜邊長5 ⇒ $4x+3y=\pm12$; 截距和5、面積3 ⇒ four lines $\frac x2+\frac y3=1$, $\frac x3+\frac y2=1$, $\frac x6+\frac y{-1}=1$, $\frac x{-1}+\frac y6=1$.
- **平移**: $L: f(x,y)=0$ 右移 $h$、上移 $k$ ⇒ $f(x-h,y-k)=0$ (e.g. $2x+3y=6$ 右移2: $2(x-2)+3y=6$; 下移3: $2x+3(y+3)=6$).
- △ABC 線: $A(-2,3),B(0,2),C(4,-1)$: AB $x+2y-4=0$; BC 中線 $5x+8y-14=0$, 重心 $(\frac23,\frac43)$; AC 上的高 $3x-2y+4=0$, 垂心 $(22,35)$; AB 中垂線 $4x-2y+9=0$, 外心 $(-10,-\frac{31}2)$.
- 直線族 / 恆過定點: $(3k+5)x+(k-1)y+9k-1=0$ ⇒ $k(3x+y+9)+(5x-y-1)=0$ 恆過 $(-1,-6)$; $\frac{2a}3+\frac b3=1$ ⇒ $2ax+by+1=0$ 恆過 $(-\frac13,-\frac13)$; 過兩直線交點的直線 $L_1+kL_2=0$: through $10x+3y-18=0$ ∩ $11x-12y+18=0$ — 過原點 $7x-3y=0$, 斜率8 $8x-y-6=0$.
- 中點條件: $L_1:x+y=4$, $L_2:2x-y=8$, L 過 $(1,0)$ 且被截線段中點為 $(1,0)$ ⇒ $4x+y=4$. 兩中線 $x+y-5=0$, $x-2y+7=0$, $A(1,7)$ ⇒ 重心 $(1,4)$, A 中線 $x=1$, BC: $x+4y=11$. 垂心 $H(\frac{19}8,\frac74)$, $A(-1,4),B(3,2)$ ⇒ $C(1,-1)$.
- 三直線不能圍成三角形 (some two parallel or all concurrent): $4x+y=4$, $mx+y=0$, $2x-3my=4$ ⇒ $m=\frac23,-1,4,-\frac16$.
- 過 $(2,3)$ 在第一象限與兩軸圍最小面積: $\frac xa+\frac yb=1$, $\frac2a+\frac3b=1\ge2\sqrt{\frac6{ab}}$ ⇒ $ab\ge24$ ⇒ min area 12, line $3x+2y=12$. 過 $(-2,3)$ 且不經過第三象限 ⇒ $-\frac32\le m\le0$.
- 二元一次方程組 ↔ 兩直線: 恰一解 ⇔ 相交 ⇔ $a_1b_2\ne a_2b_1$; 無限多解 ⇔ 重合; 無解 ⇔ 平行. 例: $(2k+1)x+ky-2=0$, $(k-1)x-2y+k=0$: $k\ne-1,-2$ 唯一解; $k=-1$ 無解(平行); $k=-2$ 無限多解(重合). (Determinant/Cramer version → §20.)

### 4.4 點到直線距離、投影、對稱、反射 (108 2-2)
- **點到直線距離** $d(A,L)=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$. Derivations: (法一) solve foot of perpendicular H; (法二) for origin, $\overline{MN}\cdot d=\overline{OM}\cdot\overline{ON}$ ⇒ $d=\frac{|c|}{\sqrt{a^2+b^2}}$, then translate.
- **平行線距離** $ax+by+c_1=0$, $ax+by+c_2=0$: $\frac{|c_1-c_2|}{\sqrt{a^2+b^2}}$ (normalize coefficients first; e.g. $4x-3y+2=0$ & $4x-3y+12=0$ → 2).
- **投影點 / 對稱點**: L 是 $\overline{AA'}$ 的中垂線. $H=A-\frac{ax_0+by_0+c}{a^2+b^2}(a,b)$, $A'=A-2\frac{ax_0+by_0+c}{a^2+b^2}(a,b)$. 例: $A(3,-9)$, $2x+3y-5=0$ ⇒ $H(7,-3)$, $A'(11,3)$, $d=2\sqrt{13}$; $A(-1,2)$, $3x+2y=14$ ⇒ $H(2,4)$, $A'(5,6)$, $d=\sqrt{13}$; $A(3,1)$, $x+2y=0$ ⇒ $H(2,-1)$, $A'(1,-3)$; $A(1,1)$ 對 $4x+2y-1=0$ ⇒ $(-1,0)$.
- 摺紙: 使 $A(0,2)$ 與 $B(4,0)$ 重合 ⇒ 摺痕 = $\overline{AB}$ 中垂線 $2x-y-3=0$; $C(7,3)$ 對應 $D(\frac35,\frac{31}5)$, $m+n=\frac{34}5$.
- 三角形面積: 頂點到對邊距離 × 底/2, e.g. $A(-1,3),B(2,0),C(5,5)$: BC $5x-3y-10=0$, $d=\frac{24}{\sqrt{34}}$, 面積 12; $A(-3,4),B(2,-1),C(6,5)$ → 25. **△OPQ 面積** with $P(m,n),Q(p,q)$: $\frac12|mq-np|$ (G-10-2 備註; e.g. $A(1,2),B(-2,6)$ → 5). (Same as 行列式 formula §16.)
- 圓心 $(-4,6)$ 切 $2x+y=3$ ⇒ 半徑 $=\frac{|-8+6-3|}{\sqrt5}=\sqrt5$ (108 prints 「5」; computed radius is $\sqrt5$).
- **反射/最短路徑**: A, B 在 L 同側, P∈L, $\overline{AP}+\overline{BP}$ 最小 ⇒ 取 A 的對稱點 A′, P = $\overline{A'B}$∩L, min $=\overline{A'B}$ (光走最短路徑/入射角=反射角). 例: 光源 $A(1,4)$, 鏡 $x-2y+2=0$, 經 $B(5,8)$ ⇒ $A'(3,0)$, 反射點 $(\frac{26}7,\frac{20}7)$; $A(3,-9)$ reflect on $2x+3y-5=0$ to $B(-22,12)$ ⇒ $P(-11,9)$; $A(3,-1),B(9,3)$, $2x-3y+4=0$ ⇒ $P(4,4)$, min $2\sqrt{26}$; 撞球 $P(2,6)$ 碰 x 軸到 $B(7,4)$ ⇒ $A(5,0)$, 路徑 $5\sqrt5$; 反射線 from $A(-3,3)$ at $P(15,1)$ on $3x-5y-10=0$ ⇒ $2x-3y-27=0$.
- **差的最大**: A, B 在 L 異側 → reflect one so both same side; $|\overline{QA}-\overline{QB}|\le\overline{AB'}$, equality on line AB′ (handout 練習 on $x-5y-12=0$: key $Q(8,-\frac45)$, max $\sqrt{74}$; the points A, B are not legible in the source text).
- 函數極值化成距離和: $f(x)=\sqrt{(x-13)^2+(2x-1)^2}+\sqrt{(x-2)^2+(2x+1)^2}$ = $\overline{PA}+\overline{PB}$ with $P(x,2x)$, $A(13,1),B(2,-1)$ (同側) ⇒ reflect B → $B'(-2,1)$ ⇒ min 15 at $x_0=\frac12$. △ABC with $A(2,1),B(5,4)$, $C(x,0)$ 周長最小 ⇒ $x=\frac{13}5$.
- 過 $P(-1,16)$ 的直線交 $L_1,L_2$ 於 B, C, 使 P 在 BC 上且 △ABC 面積最小 ⇒ P 為 BC 中點 ⇒ $3x+5y=77$.

---

## 5. 二元一次不等式與線性規劃

**Scope**: G-10-2 「二元一次不等式」 (解區域) is in scope; G-10-4 備註 「搭配不等式，可連結描述式的集合符號；僅限表達不等式的解區域」. Full **線性規劃** optimisation (目標函數、平行線法、頂點法) was a 99課綱 第三冊 unit and an old 指考數乙 favourite; it is not a named 108 數A 學習內容 → treat as **enrichment/情境** (a 學測 item may still ask for a region, lattice points, or a max of a linear expression over a small region). **Sources**: 108一上 2-2 (丙)二元一次不等式的解區域; 99第三冊 2-2線性規劃; 資優 第53單元線性規劃.

### 5.1 半平面 (half-planes)
- $L:px+qy+r=0$ splits the plane into two 半平面; $px+qy+r>0$ on one, $<0$ on the other. Test a point (usually O). ≥/≤ include the line (實線), strict excludes it (虛線).
- **同側/異側判別**: $P(x_1,y_1),Q(x_2,y_2)$ 在 L 異側 ⇔ $(px_1+qy_1+r)(px_2+qy_2+r)<0$; 同側 ⇔ $>0$. Proof: $R=\overline{PQ}\cap L$ with $\overline{PR}:\overline{RQ}=m$ ⇒ $m=-\frac{f(P)}{f(Q)}>0$. (Meaning of $f(A)$: proportional to signed distance $\frac{f(A)}{\sqrt{p^2+q^2}}$.)
- Vertical-line argument: on $x=x_0$, points above the intersection satisfy $x+y-4>0$ etc.
- 題型:
  - 點在某側: $2x-y+12=0$, $A(a,-6)$ 在右半平面 ⇒ $a>-9$; $B(3,b)$ 在下半平面 ⇒ $b<18$.
  - 線段與直線相交 ⇔ endpoint values have product ≤0: $A(3,10),B(-1,2)$, $7x-2y+k=0$ ⇒ $-1\le k\le11$; $P(3,1),Q(-4,6)$, $3x-2y+k=0$ 相交 ⇒ $-7\le k\le24$ (異側 strict). $A(2,1),B(3,4)$ 與 $y=mx+3$ 相交 ⇒ $-1\le m\le\frac13$.
  - **直線族過定點 + 斜率範圍**: $y=mx+\frac32$ 與 △ (sides $2x+y-2=0$, $y=0$, $x-y+1=0$) 相交 ⇒ $m\ge\frac32$ or $m\le-\frac12$ (lines through $(0,\frac32)$; rotate & read slopes to vertices); $y=m(x+2)-1$ 與 $A(1,-2),B(-4,5),C(4,2)$ △ 相交 ⇒ $-3\le m\le-\frac13$; $y=mx-8m-6=m(x-8)-6$ 與 $A(3,3),B(-1,-5),C(6,0)$ △ 相交 ⇒ $-3\le m\le-\frac19$; $y=mx-1$ 恆與 $A(-1,3),B(4,1),C(5,6)$ △ 相交 ⇒ $m\le-4$ or $m\ge\frac12$; $A(3,1),B(-2,0)$ 在 $y=mx+3$ 異側 ⇒ $(-3m-2)(2m-3)<0$ ⇒ $m>\frac32$ or $m<-\frac23$; $A(3,2),B(-1,3)$ 在 $y=mx$ 同側 ⇒ $-3<m<\frac23$.
  - 三角形內部 as 聯立不等式: $A(5,6),B(-2,0),C(1,-2)$ ⇒ $6x-7y+12>0$, $2x+3y+4>0$, $2x-y-4<0$ (each side's inequality signed by the third vertex); $P(k,k-1)$ inside ⇒ $-\frac15<k<3$. 108 例題8: $A(0,2),B(4,0),C(3,6)$ (stem misprints A as (2,0); figure shows (0,2)) 含邊界: $x+2y-4\ge0$, $4x-3y+6\ge0$, $6x+y-24\le0$; $y=mx+2$ passes through A, so it bisects the area iff it passes through the midpoint $(\frac72,3)$ of BC ⇒ $m=\frac27$.
  - 區域面積: find vertices by pairwise intersection, then 鞋帶公式/split into triangles. $(2x+y-8)(x+y-5)\le0$ with the axes → $\frac{11}2$ (product ≤0 ⇒ between the two lines); $6-2x\le y-2\le x\le6$ → 24.
  - Change of variables: $0\le a\le1$, $0\le b\le2$, $x=3a+b$, $y=a-b$ ⇒ region $0\le x+y\le4$, $0\le x-3y\le8$ — a **parallelogram** (not the rectangle $0\le x\le5,-2\le y\le1$), area 8. $p,q,r\ge0$, $p+q+r=1$, $(x,y)=p(1,2)+q(3,1)+r(4,3)$ ⇒ triangle with those vertices, area $\frac52$.
  - 格子點 count: $x\ge0,y\ge0,3x+2y\le6$ → 7 個.
- 非線性 regions (補充): $y\ge|x|$ (above V), $|x|+|y|\le4$ (菱形內部); $|x|\le y\le11-|x-6|$-type polygons (area $\frac{85}2$); $|12x-4|+|6y-3|\le24$ → 菱形 diagonals 4, 8 → area 16; $|x|+|y|\le2$ ∩ $|x|+|y-1|\le2$ → $\frac92$ (2002指定甲); $(x+y-1)(x+y-2)(x+y-3)\le0$-type with $|\cdot|$ → 環狀; $(|x|+|y|-1)(|x|+|y|-\frac12)\cdots$ ⇒ $A_n=\frac85[1-(-\frac14)^n]$.
- $y=||x|-2|$: reflect negative part; $||x|-2|=k$ has 0 (k<0), 2 (k=0 or k>2), 4 (0<k<2), 3 (k=2) solutions; $y=mx+5$ meets it at exactly 2 points ⇔ $|m|\ge1$. $f(x)=|2x-1|$ on [0,1]: $f(f(f(x)))=x$ has 8 solutions.

### 5.2 線性規劃 (enrichment)
- Setup: 變數 → 限制條件 (聯立不等式) → **可行解區域** → **目標函數** $f(x,y)=ax+by$ → **最佳解**.
- **平行線法**: $ax+by=k$ is a family of parallel lines; slide until last contact with the region; compare the objective's slope with edge slopes to know which vertex. **頂點法**: on a bounded convex region the max/min occurs at a vertex (or along an edge if objective ∥ edge → infinitely many optima).
- 原型: 甲原料 (成本1000, 運費500, 產90 kg), 乙 (1500, 400, 100 kg), 預算 6000/2000 ⇒ $10x+15y\le60$, $5x+4y\le20$; vertices $O,(4,0),(0,4),(\frac{12}7,\frac{20}7)$ ⇒ max 440 kg.
- **整數解 (格子點)**: if optimum vertex is non-lattice, search lattice points near it: 木板 $2x+y\ge15$, $x+2y\ge22$, $x+3y\ge27$, min $x+y$ at $B(\frac83,\frac{29}3)$ gives $12\frac13$ ⇒ $x+y=13$ with $(2,11),(3,10),(4,9)$. 維他命 甲(5A,9B,10元) 乙(6A,4B,8元), need 29A,35B ⇒ 各3粒, 54元. 貨車 4噸×7輛, 5噸×4輛, 9名司機, ≥30噸: 10 種調度, 最省 小5大2 = 4100 元.
- 經典應用 (with Ans): 預售屋 $5x+2y\le35$, $3x+5y\le40$ ⇒ 各5棟, 5000萬 (2008指定乙); 營養餐 A,B ⇒ vertices $(0,60),(15,15),(20,10),(40,0)$; 雞飼料 $7x+2y\ge84$, $3x+6y\ge72$, $3x+2y\ge60$, min $5x+4y=102$ at $(18,3)$ (2006指定乙); 中草藥/健康食品 $P=5000x+100y$, $200x+5y\le10000$, $x\le30$, $y\le1800$ ⇒ $(30,800)$ (2004指定乙); 徽章 鐵板 ⇒ $(2,3)$, 1760 元 (2014指定乙); 大小教室 → 大20 小40 (2009指定乙); 稻/花生 → 83200 元; 自行車 新竹/台中 → $x=480,y=220$, 41440 元; 運輸 → 第一廠 30,10; 第二廠 0,30; 890 元; 電視機 甲2日乙4日; 酪梨 1080 粒 25/8 裝 → 2600 元 (89社, Diophantine: $x=8t$, $y=135-25t$).
- 參數題: 目標函數 $kx-y$ at $(4,1)$ 最大 ⇒ $-\frac23\le k\le2$ (feasible triangle (1,3),(4,1),(6,5); compare vertex values); 正六邊形 region, $ax-y$ (or $y-ax$) unique max at A ⇒ $-3<a<0$ (87自) / $-2<a<0$; $z=x+ky$ max at $(2,1)$ ⇒ $-1\le k\le2$; 2010指定乙: 目標 $ax+by+32$ min 18 at boundary interior point $(4,10)$ of CD ⇒ min along whole edge ⇒ $(a,b)=(14,-7)$; 2003指定甲: triangle max 31 at (19,12), min 23 at (13,10); add 4th constraint → vertices (17,13),(16,11) ⇒ max at (17,13) = 30 (A)(C).
- 非線性目標 over a polygon: $x^2+y^2$ (distance² from O; min may be on an edge — foot of perpendicular), $\frac{y+2}{x+1}$ (slope from $(-1,-2)$): region $x,y\ge0$, $3x+2y\le12$, $x+y\ge2$ ⇒ $2x-y+3$ max 11 at $(4,0)$; $x^2+y^2$ max 36, min 2; $\frac{y+2}{x+1}$ max 8, min $\frac25$. $xy$ over $2x+y\le2$, $x+2y\le2$ ⇒ max $\frac49$, min 0.
- 線性變數範圍: $5\le3x-2y\le27$, $-35\le x+3y\le31$ ⇒ $-5\le x\le13$, $-12\le y\le8$, $-5\le3x-y\le33$, $-82\le2x+7y\le70$. $f(x)=ax+b$, $-2<f(1)<6$, $2<f(3)<10$ ⇒ $-3<f(\frac12)<5$, $-12<f(10)<52$ (express target as combination of $f(1),f(3)$).
- 根的位置 → region in $(a,b)$: $x^2-ax+b=0$, $-1\le\alpha\le0$, $1\le\beta\le2$ ⇒ $f(-1)\ge0,f(0)\le0,f(1)\le0,f(2)\ge0$ ⇒ $2a+b$ max 4, min $-1$; $a^2+b^2$ min $\frac12$.

---

## 6. 圓方程式、圓與直線

**Scope**: G-10-3 圓的標準式; G-10-4 直線與圓 (圓的切線，圓與直線關係的代數與幾何判定; **不含兩圓關係**; 可用不等式表示圓內/外區域). 圓系 through two circles, 根軸, 外公切線 are **[超出數A]** (兩圓). **Sources**: 108一上 2-3圓方程式, 2-4圓與直線的關係; 99第三冊 2-3圓與直線的關係; 資優 第33單元圓.

### 6.1 圓的方程式
- **標準式** $(x-h)^2+(y-k)^2=r^2$ (圓心 $(h,k)$, 半徑 $r$). 「求圓 = 求圓心與半徑」.
- **一般式** $x^2+y^2+Cx+Dy+E=0$ ⇒ $(x+\frac C2)^2+(y+\frac D2)^2=\frac{C^2+D^2-4E}4$: $>0$ 圓 (center $(-\frac C2,-\frac D2)$, $r=\frac12\sqrt{C^2+D^2-4E}$); $=0$ 一點; $<0$ 無圖形. Coefficients of $x^2,y^2$ must be equal (divide first: $2x^2+2y^2-4x+6y+1=0$ → center $(1,-\frac32)$, $r=\frac{\sqrt{11}}2$); no $xy$ term.
- **直徑式** (資優): 直徑端點 $A(x_1,y_1),B(x_2,y_2)$ ⇒ $(x-x_1)(x-x_2)+(y-y_1)(y-y_2)=0$ (since $\overrightarrow{AP}\cdot\overrightarrow{BP}=0$; or 畢氏 $AP^2+BP^2=AB^2$). E.g. $A(-1,2),B(3,4)$ ⇒ $(x-1)^2+(y-3)^2=5$; 以拋物線與 x 軸交點 AB 為直徑: $ax^2+ay^2+bx+c=0$.
- 三點定圓: 中垂線交點 (外心) or substitute into 一般式 and solve 3 equations. $P(1,1),Q(4,0),R(5,1)$ ⇒ $(x-3)^2+(y-2)^2=5$; $(0,0),(0,4),(3,3)$ ⇒ $x^2+y^2-2x-4y=0$; $A(3,6),B(8,1),C(11,10)$ ⇒ $x^2+y^2-16x-12y+75=0$.
- 參數討論: $x^2+y^2+2x-2ky+k+3=0$: 圓 ⇔ $k^2-k-2>0$ ($k<-1$ or $k>2$), 點 ⇔ $k=-1,2$, 無圖形 ⇔ $-1<k<2$. $x^2+y^2+2(m+1)x-2my+3m^2-2=0$ 表圓 ⇔ $-1<m<3$, max area $4\pi$ (r²=$-m^2+2m+3$… max at $m=1$). $x^2+y^2+2x-6y+k=0$: 圓 $k<10$, 點 $k=10$.
- Useful facts: 圓心到弦中點連線 ⊥ 弦 (弦心距); 與兩軸相切 ⇒ $|a|=|b|=r$; 切線距離 = 半徑.
  - 弦 $P_1(1,4)P_2(3,-2)$, 弦心距 $\sqrt{10}$ ⇒ $(x+1)^2+y^2=20$ or $(x-5)^2+(y-2)^2=20$ (圓心在中垂線上). 弦 $(2,0)(8,0)$ 弦心距4 ⇒ $(x-5)^2+(y\mp4)^2=25$. 過 $(5,1),(3,1)$, 圓心在 $x+2y-3=0$ ⇒ $(x-4)^2+(y+\frac12)^2=\frac{13}4$. 過 $(2,0),(-4,0)$, 圓心在 $y=4$ ⇒ $(x+1)^2+(y-4)^2=25$. 過 $A(1,4),B(3,-2)$ 切 $x+2y+11=0$ ⇒ $(x+1)^2+y^2=20$ or $(x-23)^2+(y-8)^2=500$. 過 $(1,2)$ 切兩軸 ⇒ $(x-1)^2+(y-1)^2=1$, $(x-5)^2+(y-5)^2=25$. 切 $y=x$ 過 $(2,0),(4,0)$ ⇒ $(x-3)^2+(y+7)^2=50$ or $(x-3)^2+(y-1)^2=2$. 切兩平行線 $x+5y-4=0$, $x+5y-12=0$, 圓心在 $x-2y-1=0$ ⇒ $(x-3)^2+(y-1)^2=\frac{16}{26}$… (r = half the gap $\frac{4}{\sqrt{26}}$). 過A(1,2),B(3,4) 被 x 軸截 6 ⇒ $x^2+y^2+12x-22y+27=0$ or $x^2+y^2-8x+2y+7=0$.
- 「哪些是圓」: $y=\sqrt{9-x^2}$ 半圓 ✗; $x=1+\sqrt{9-y^2}$ 半圓 ✗; $x^2+y^2=2$ ✓; $x^2+y^2-6x+4y+15=0$ (r²<0) ✗; $x^2+y^2+2x-8y+3=0$ ✓.
- 2014學測: 正方形 $(\pm1,\pm1)$ 與 $(x+1)^2+(y+1)^2=1$ (center = a vertex) → 2 個交點.

### 6.2 點與圓、圓的內外部 (G-10-4)
- $P$ 在圓內/上/外 ⇔ $\overline{PQ}<,=,>r$ ⇔ $f(x_0,y_0)=x_0^2+y_0^2+dx_0+ey_0+f<,=,>0$. 圓內部 $f<0$, 外部 $f>0$.
- 環形區域 area $=\pi(r_2^2-r_1^2)$: $5\le(x-1)^2+(y+3)^2\le25$ ⇒ $20\pi$; $11\le\cdot\le35$ ⇒ $24\pi$ (108 answer key prints 16π and 14π — inconsistent with the stems). 108 例題7: annulus centred $Q(4,4)$ through $A(3,1)$ (實線 inner) and $B(5,9)$ (虛線 outer) ⇒ $10\le(x-4)^2+(y-4)^2<26$. 兩圓內部交集 as 聯立不等式 (含邊界 ≤).
- $(x^2+y^2-1)(x^2+y^2-2x-3)\le0$ → region between two circles (one inside the other partially) area $3\pi$ ($4\pi-\pi$, unit circle inside $(x-1)^2+y^2=4$).
- **點到圓上點的最遠/最近距離** $=\overline{PQ}\pm r$: $A(-3,2)$, $(x-4)^2+(y-1)^2=4$ ⇒ $5\sqrt2\pm2$; $A(2,-1)$ 在 $(x+1)^2+(y-3)^2=64$ 內 ⇒ 13, 3; $A(-6,-9)$ & $(x+1)^2+(y-3)^2=100$ ⇒ 23, 3; $P(6,8)$ & $(x-3)^2+(y-4)^2=1$ ⇒ 4 at $(\frac{18}5,\frac{24}5)$, 6 at $(\frac{12}5,\frac{16}5)$ (分點公式 on line through center). 點 $(24,37)$ 到 $x^2+y^2=10y$ 最近點 $(3,9)$.
- 颱風情境: 暴風半徑 250 km, 距恆春 400 km, 15 km/h 直線前進 → 10 小時後進入暴風圈.
- 焚化爐 (Apollonius): $\overline{PA}:\overline{PB}=1:2$ (反比 4萬:2萬噸), A(0,0), B(12,0) → circle; 遠離道路 → 圓的最高點 (A 西 4 km、北 8 km).

### 6.3 圓與直線的關係 (G-10-4)
- 代數: substitute line into circle → 一元二次方程, 判別式 $D$: $D>0$ 相割(2點), $D=0$ 相切, $D<0$ 相離.
- 幾何: $d=d(\text{圓心},L)$ vs $r$: $d<r$ 相割, $d=r$ 相切, $d>r$ 相離.
- 例: $x^2+y^2=4$ vs $3x-4y-2=0$ (割), $3x-4y+10=0$ (切), $3x-4y+15=0$ (離). $(x+1)^2+(y-2)^2=4$ & $x-y+k=0$: 切 $k=3\pm2\sqrt2$, 割 between. $(x+1)^2+y^2=8$ & $y=mx+3$: $D=4(m+1)(7m-1)$ ⇒ 割 $m<-1$ or $m>\frac17$; 切 $m=-1,\frac17$. $kx+y-3=0$ & $x^2+y^2=3$: 相切 $k=\pm\sqrt2$, 相離 $|k|<\sqrt2$, 相割 $|k|>\sqrt2$. $(x-1)^2+(y+2)^2=9$ & $3x-4y+k=0$ 割 ⇔ $-26<k<4$. $x^2+y^2-2x+6y+k=0$ & $x+2y=0$ 相交 ⇔ $k\le5$.
- **弦長** $=2\sqrt{r^2-d^2}$: $x^2+y^2-2x+4y-4=0$ & $4x+3y+7=0$: 弦心距1, 弦長 $4\sqrt2$; $3x-4y+21=0$ on $(x-2)^2+(y-3)^2=25$ → 8; $(x-1)^2+(y+3)^2=169$, $4x+3y+k=0$, 弦長24 ⇒ $d=5$ ⇒ $k=30,-20$; $y=mx$ & $x^2+y^2-4x+2y+1=0$, $AB=\sqrt6$ ⇒ $m=\frac13$ or $-3$; $y=mx+4-m$ & $x^2+y^2=25$, $AB=6$ ⇒ $m=0$ or $-\frac8{15}$; $4x-3y+1=0$ in $x^2+y^2=41$ → $\frac{32}5$; $x^2+y^2+2x+k=0$ & $8x-15y-9=0$, $AB=4$ ⇒ $k=-24$. Chord via 韋達: $|x_1-x_2|\sqrt{1+m^2}$ with $(x_1-x_2)^2=(x_1+x_2)^2-4x_1x_2$.
- 弦中點: $x^2+y^2=5$ ∩ $x-y+1=0$ → 中點 $(-\frac12,\frac12)$ (foot from center). 過圓內點 $P$ 的最短弦 ⊥ $\overline{OP}$: $(x+2)^2+(y-3)^2=16$, $P(-1,2)$ ⇒ 長 $2\sqrt{14}$, 方程 $x-y+3=0$. 兩平行線 $y=x+m$, $y=x+n$ 四等分 $x^2+(y-2)^2=4$ ⇒ $m=4,n=0$.
- **學測 classics**: 2013學測 一圓被 $x-y=1$ 與 $x-y=5$ 所截弦長皆14 ⇒ 圓心在 $x-y=3$, $d=\sqrt2$, $r^2=51$, 面積 $51\pi$. 2019學測 $A(1,0)$ 在單位圓, 圓上另有幾點到 $y=2x$ 距離等於 A 的? → 3 個. 2008學測 $x^2+y^2-10x+9=0$ (center (5,0), r=4): 圓心 ✓; 到 $3x+4y-15=0$ 最遠距離 $0+4=4$ ✓; $3x+4y+15=0$ 不相切 ($d=6$); 與 $3x+4y=0$ 距離2 的點恰2個 ✓ ($d=3$; the two parallel lines at distance 2 are 1 and 5 from the center → 2+0 points); 與 $3x+4y-5=0$ 距離2 恰4個 ✗ ($d=2$; parallels at distance 0 and 4 → 2+1 = 3 points) → (1)(2)(4). 2009學測 到 O 距離1、到 A(3,0) 距離2 的直線 = 兩圓公切線 → 3 條 (circles externally tangent). 2017學測 O 在 Γ 外、(2,6) 在 Γ 內 ⇒ center beyond perpendicular bisector $x+3y=10$ … only (5) 圓心可在第四象限且半徑必>10. 2013指考甲 圓 $x^2+y^2+4x-7y+10=0$ 與 $y=m(x+3)$ 兩交點在不同象限 ⇒ line must cross y-axis between (0,2),(0,5) ⇒ $\frac23<m<\frac53$.
- 圓上格點/整數距離: $P$ on $(x-3)^2+(y-4)^2=3$, $a^2+b^2\in\mathbb Z$ ⇒ $(5\pm\sqrt3)^2$ range 10.68…45.32 ⇒ 35 integer values × 2 = 70 points. $x^2+y^2+2x+6y-10=0$, $A(9,2)$: $\overline{AP}$ 為整數的點 18 個.
- 根的個數 ↔ 圖形: $\sqrt{x(4-x)}=mx+4$ (upper semicircle vs lines through $(0,4)$) 兩相異解 ⇔ $-1\le m<-\frac34$; $y=m(x-3)$… with circle → $\frac{12-2\sqrt{21}}5<m<\frac{12+2\sqrt{21}}5$; 方程組 $x+y+k=0$ & $x^2+y^2+2x-6y-6=0$ … by $d$ vs $r$.

### 6.4 切線 (G-10-4)
- Properties: 圓心與切點連線 ⊥ 切線; 圓心到切線距離 = r. Three types: 過圓上一點、已知斜率、過圓外一點 (two tangents; if slope eq. gives one m, the other is **鉛直線** $x=x_1$).
- **切點式**: $(x_0-h)(x-h)+(y_0-k)(y-k)=r^2$; for $x^2+y^2=r^2$: $x_0x+y_0y=r^2$; general form: $x_0x+y_0y+\frac d2(x+x_0)+\frac e2(y+y_0)+f=0$. E.g. $x^2+y^2=25$ at $(3,4)$: $3x+4y=25$; $x^2+y^2+2x-6y-15=0$ at $(2,7)$: $3x+4y-34=0$; $(x-2)^2+(y+1)^2=5$ at $(3,1)$: $y-1=-\frac12(x-3)$.
- **斜率式**: $x^2+y^2=r^2$, slope m: $y=mx\pm r\sqrt{1+m^2}$; translated: $y-k=m(x-h)\pm r\sqrt{1+m^2}$. 斜率 $-1$ to $x^2+y^2-6x-4y+5=0$: $y=-x+1$, $y=-x+9$; 平行 $x+3y=0$ 切 $(x+2)^2+(y-1)^2=10$: $x+3y=11$, $x+3y=-9$; 平行 $2x+y=1$ 切 $x^2+y^2=5$: $2x+y=\pm5$.
- **過圓外一點**: $A(4,2)$, $x^2+y^2-4x+4y-2=0$ ⇒ slopes $\frac13,-3$; $P(2,1)$, $(x-3)^2+(y-4)^2=5$ ⇒ $2x+y-5=0$, $x-2y=0$; $P(4,5)$, $(x-3)^2+(y-2)^2=1$ ⇒ $4x-3y-1=0$ **and $x=4$**; $A(1,6)$, $(x+2)^2+(y-2)^2=9$ ⇒ $7x-24y=-137$ and $x=1$; $P(2,7)$, $x^2+(y-3)^2=2$ ⇒ $x-y+5=0$, $7x-y-7=0$, 光源 P 投影圓於 x 軸影長 6. $(7,5)$ 光源, $x^2+(y-1)^2=1$ 影長 $\frac{16}3$.
- **切線段長** $\sqrt{f(x_0,y_0)}$ (= $\sqrt{\overline{PO}^2-r^2}$): $(-1,2)$ to $x^2+y^2-2x+4y-3=0$ → $2\sqrt3$; 圓冪 $\overline{PA}\cdot\overline{PQ}=12$. $Q(3,1)$ to $(x-2)^2+(y-9)^2=16$ → 7.
- 切點弦 / 極線: 過圓外 P 兩切線切點 Q,R ⇒ 直線 QR: $x_0x+y_0y+\frac d2(x+x_0)+\frac e2(y+y_0)+f=0$; △PQR 外接圓 = 以 $\overline{P\,\text{圓心}}$ 為直徑的圓. E.g. $P(1,2)$, $x^2+y^2-4x+2y-4=0$ ⇒ 外接圓 $x^2+y^2-3x-y=0$, QR: $x-3y+4=0$, 切線 $y=2$, $y-2=\frac34(x-1)$; $A(-3,0)$, $x^2+y^2-2x+4y+1=0$ ⇒ $x^2+y^2+2x+2y-3=0$; $P(4,6)$, $(x-1)^2+(y-2)^2=4$ ⇒ 切線段 $\sqrt{21}$, AB: $3x+4y-15=0$.
- 反射+切線: 光線自 $A(-3,3)$ 射到 x 軸, 反射後切 $x^2+y^2-4x-4y+3=0$ ⇒ reflect A to $(-3,-3)$ ⇒ $2x+y+3=0$ (and steeper one).
- 2007指定甲: 圓過 $(-2,7)$, 切 $4x+3y-14=0$ 於 $(-1,6)$ ⇒ $(a,b,c)=(10,-6,9)$. 直線 $5x-y-a=0$ 切 $3x^2+3y^2-2x+4y+b=0$ 於 $(c,-1)$ ⇒ $a=11,b=-7,c=2$. 87大學社: 互相垂直切線的交點軌跡 = 同心圓半徑 $\sqrt2r$ ⇒ $(x-4)^2+(y+2)^2=50$.
- 極值 via 圓: $x+y$ on $x^2+y^2\le2$ ⇒ max 2, min $-2$; on $x^2+y^2\le4$, $y\ge1$ ⇒ max $2\sqrt2$, min $1-\sqrt3$; $\frac{\sin\theta+3}{\cos\theta-2}$ = slope from $(2,-3)$ to unit-circle point (tangent slopes); $\frac{8-\sin\theta}{9-\cos\theta}\in[\frac34,\frac{21}{20}]$; 參數式 $x=r\cos\theta,y=r\sin\theta$: on $x^2+y^2=16$, $4x+3y\le20$, $x^2+2y\le17$, $xy\le8$, 到 $3x-4y=25$ 最短 1; on $x^2+y^2=9$: $3x+4y+5\le20$; △POQ ($Q(3,-2)$, P on unit circle) max area $\frac{\sqrt{13}}2$.
- 軌跡 (G-10 friendly): $\overline{PA}=2\overline{PB}$, $A(0,0),B(6,0)$ ⇒ $(x-8)^2+y^2=16$ (阿波羅尼斯圓; 內外分點為直徑端點); 過圓內點 $A(0,0)$ 之弦中點軌跡 for $(x-1)^2+(y-2)^2=16$: $x^2+y^2-x-2y=0$ (circle with diameter A–center); $\overline{AP}$ 中點 ($A(6,0)$, P on $x^2+y^2=4$): $(x-3)^2+y^2=1$; $\angle P=90^\circ$ with $Q(-2,3),R(1,-1)$: circle on diameter QR minus Q,R; $\overrightarrow{OP}=2\overrightarrow{OQ}$: dilation.
- 圓冪 (資優): $\overline{PT}^2=\overline{PA}\cdot\overline{PB}=f(x_0,y_0)$ (outside); inside: $\overline{PA}\cdot\overline{PB}=-f(x_0,y_0)=r^2-\overline{OP}^2$. Uses: $P(-2,5)$ 三等分 $x^2+y^2+2x-6y-3=0$ 的弦 ⇒ $\overline{AB}=6$; $P(1,2)$ 三等分 $x^2+y^2=37$ 的弦 ⇒ $PA\cdot PB=32$ ⇒ $AB=12$ ⇒ lines $y-2=\frac34(x-1)$, $x=1$.
- **[超出數A] 圓系/兩圓**: $C_1+kL=0$ (circles through circle∩line), $C_1+kC_2=0$, 公共弦/根軸 $C_1-C_2=0$ ($(d_1-d_2)x+(e_1-e_2)y+(f_1-f_2)=0$), 外公切線交角 ($C_1,C_2$: $\sin\theta=\frac{28}{53}$… handout). Only use the circle–line family $C+kL=0$ as a technique, never pose 兩圓位置關係 for 數A.

---

## 7. 多項式：運算、除法原理、函數與圖形、方程式、不等式

**Scope**: A-10-1, A-10-2 多項式之除法原理 (因式定理、餘式定理、除以 x−a、表成 (x−a) 的多項式; **綜合除法除式僅作 x−a，不推廣到 ax−b，不用分離係數法** — the handouts do teach ax+b, flag it), F-10-1 一次與二次函數, F-10-2 三次函數的圖形特徵 (對稱性、大域由最高次項決定、局部近似一直線; 一般三次函數皆為 $y=ax^3+px$ 之平移), F-10-3 多項式不等式 (一次、二次、已分解之多項式), A-11A-2 (插值多項式／牛頓插值 as source of 三元一次方程組). **[超出數A]**: 複數、虛根成對、代數基本定理 (108 moved 複數 to 12年級數甲); 有理根/一次因式檢驗定理 is not a listed 數A item (useful technique only); 勘根定理 not listed (but 「圖形與 x 軸交點」 reasoning is fine); H.C.F./L.C.M., 高斯引理, Cardano/Ferrari. **Sources**: 108一上 3-1多項式的運算與應用, 3-2多項式函數及其圖形, 3-3多項式不等式; 99第一冊 2-1簡單多項式函數, 2-2多項式的運算與應用, 2-3多項式方程式, 2-4多項式不等式; 資優 第9單元多項式, 第10單元多項式函數, 第11單元n次方程式與不等式.

### 7.1 基本概念
- 多項式 $a_nx^n+\dots+a_0$ ($n\ge0$, 只用加乘); 分式、根式（變數在分母/根號內）不是多項式. 首項係數(領導係數)、常數項、次數 deg; 零次多項式 vs 零多項式 (沒有次數); 降冪/升冪; 整係數/有理係數/實係數 ($\mathbb Z[x],\mathbb Q[x],\mathbb R[x]$).
- 相等: same degree & all coefficients equal (恆等式 ⇒ any substitution holds). $(a-2)x^2+3x+(c+1)=(2b-1)x+10$ ⇒ $a=2,b=2,c=9$.
- **係數和** $=f(1)$; 常數項 $=f(0)$; 奇次項係數和 $=\frac{f(1)-f(-1)}2$; 偶次項 $=\frac{f(1)+f(-1)}2$; $f(i)$ 實部 $=a_0-a_2+a_4-\dots$. E.g. $(x^5-2x^3+x+1)^{1999}$: 1,1,0,1; $(x-2)^8(x^2-x+1)^{10}$: 係數和 1, 偶次項和 $\frac{3^{18}+1}2$. $(x+1)(x+2)\cdots(x+n)$: $a_{n-2}=\frac1{24}n(n+1)(n-1)(3n+2)$; $(x+1)(x+3)\cdots(x+31)$: $n=16$, $a_{n-1}=256$, $a_{n-2}=30040$.
- $\deg(f\pm g)\le\max$; $\deg(fg)=\deg f+\deg g$ (2019學測-type trap: not product).

### 7.2 除法原理、綜合除法
- **除法原理**: $g\ne0$ ⇒ unique $q,r$ with $f=gq+r$, $r=0$ or $\deg r<\deg g$. If $\deg f<\deg g$: $q=0$, $r=f$. 長除法 / 待定係數: $3x^3+mx^2-61x+n$ 被 $x^2-5x+3$ 整除 ⇒ $m=-1,n=42$; $x^4+4x^2+ax+b$ 被 $x^2+2x+3$ 整除 ⇒ $a=4,b=15$; $x^2+ax+1|x^3+3x^2+bx+2$ ⇒ $a=1,b=3$; $x^3+mx^2+3x+1=(x^2-x+2)(x+1)+2x+n$ ⇒ $m=0,n=-1$.
- 綜合除法 (除以 $x-a$): bring down, multiply by a, add. 原理 by comparing coefficients ($c_2=a_3$, $c_1=a_2+bc_2$, …). Dividing by $ax-b$ (handout extension, not 數A): divide by $x-\frac ba$, then quotient $\div a$, same remainder. Variants: $f(x)\div(x-\frac ba)$ gives $Q,r$ ⇒ $f\div(ax-b)$: $\frac1aQ(x)$, $r$; $f(\frac xa)\div(x-b)$: $\frac1aQ(\frac xa)$, r.
- **表成 $(x-a)$ 的多項式** (連續綜合除法): $f(x)=2x^3-7x^2+6x=2(x-1)^3-(x-1)^2-2(x-1)+1$ ⇒ $f(0.998)\approx1.004$; $2x^4-7x^3+x^2+5x+5=2(x+1)^4-15(x+1)^3+34(x+1)^2-26(x+1)+10$ ⇒ $(x+1)^2$ 除之餘 $-26x-26$, $f(-0.999)\approx9.974$, $f(\sqrt3-1)=130-71\sqrt3$; $x^3-4x^2+7x-1=(x-2)^3+2(x-2)^2+3(x-2)+5$ ⇒ $f(2.003)\approx5.009$, $f(2+\sqrt3)=11+6\sqrt3$, $(x-2)^2$ 除之餘 $3x-1$; $54x^3-99x^2+66x-20=2(3x-1)^3-5(3x-1)^2+6(3x-1)-7$ ⇒ $f(0.333)\approx-7.006$; reverse: $(x-3)^4+5(x-3)^3+\dots$ ⇒ $x^4-7x^3+15x^2+2x+20$.
- 代值技巧: $11^5-4\cdot11^4-72\cdot11^3-56\cdot11^2+15\cdot11+7=f(11)=51$ (綜合除法); $f(3)$ for big coefficients 217; $8(\frac{\sqrt5+1}2)^3-16(\cdot)^2+2(\cdot)+15=8+\sqrt5$ (divide by $x^2-x-1$).

### 7.3 餘式定理、因式定理
- **餘式定理**: $f(x)\div(x-a)$ 餘 $f(a)$; $\div(ax+b)$ 餘 $f(-\frac ba)$. $f(a)$ 雙重意義: 函數值 & 餘式.
- **因式定理**: $(x-a)|f(x)$ ⇔ $f(a)=0$; $(ax-b)|f$ ⇔ $f(\frac ba)=0$. $f(a)=0$ ⇔ f 在 a 取值0 ⇔ a 為根 ⇔ 餘式0 ⇔ $x-a$ 為因式. 推廣: $k$ 個相異根 ⇒ $(x-a_1)\cdots(x-a_k)|f$. $x^n-a^n=(x-a)(x^{n-1}+\dots+a^{n-1})$.
- 題型:
  - 餘式 by 待定: 除以 $(x-1)(x+2)$, $f(1)=2,f(-2)=-1$ ⇒ $x+1$; 三個一次 ⇒ 二次餘式 (Lagrange): $f(1)=3,f(-1)=1,f(2)=-2$ ⇒ $-2x^2+x+4$; $f(1)=5,f(2)=3,f(3)=7$ ⇒ $3x^2-11x+13$; $(x-3)(x+4)$: 16, −19 ⇒ $5x+1$.
  - **除以 (一次)(二次)**: $f\div(x^2+2x+3)$ 餘 $x+12$, $f(-1)=-1$ ⇒ $f\div(x+1)(x^2+2x+3)$ 餘 $a(x^2+2x+3)+x+12$ with $a\cdot2+11=-1$ ⇒ $-6x^2-11x-6$. Similar: $-3x^2-5x-3$; $(2x^2+x+3)(x+2)$: $4x^2+4x+11$.
  - 重因式: 以 $(x-1)^2$ 除餘 $3x+2$, $(x+2)^2$ 除餘 $5x-3$ ⇒ $\div(x-1)$: 5; $\div(x-1)(x+2)$: $6x-1$; $\div(x-1)^2(x+2)$: $-x^2+5x+1$. 以 $(x+1)^3$ 除餘 $x^2-2x+3$ ⇒ $(x+1)^2$ 除餘 $-4x+2$. $x^{10}+2\div(x-1)^2$ → $10x-7$ (binomial in $(x-1)$); $x^{50}+1\div(x+1)^2$ → $-50x-48$.
  - 共同條件: $f\div(x^2+x-2)$, $(x^2-x-6)$, $(x^2+x-12)$ 餘 $2x+3$, $3x+a$, $4x+b$ ⇒ use shared roots: $a=5,b=2$. $f\div(x^2-3x+2)$ 餘 3, $\div(x^2-4x+3)$ 餘 $3x$ ⇒ $\div(x^2-5x+6)$ 餘 $6x-9$.
  - $f\div(x^3-1)$ 餘 $x^2-1$ ⇒ $\div(x^2+x+1)$ 餘 $-x-2$. $(x+1)f(x)\div(x^2+x+1)$ 餘 $5x+3$ ⇒ $f\div$ 餘 $2x+5$ (use $x^2\equiv-x-1$). $x^{12}+x^9-3x^6+4x^2-5$: $\div(x^3+1)$ 餘 $4x^2-8$; $\div(x^5-1)$ 餘 $x^4+5x^2-3x-5$. $x^{333}+x^{33}+x^3+3\div(x^4-1)$ → $x^3+2x+3$.
  - **2019學測** ($f_1,f_2$ 三次, $g$ 二次, 餘 $r_1,r_2$): $-f_1$ 餘 $-r_1$ ✓; $f_1+f_2$ 餘 $r_1+r_2$ ✓; $f_1f_2$ 餘 $r_1r_2$ ✗ (deg 2); $f_1\div(-3g)$ 餘 $r_1$ (not $-\frac13r_1$) ✗; $f_1r_2-f_2r_1$ 被 g 整除 ✓ → (1)(2)(5).
  - **2016指定乙**: f 除以 $(x-5)(x-6)^2$ 餘 $5x^2+6x+7$ ⇒ can find $f\div(x-6)^2$ and $f\div(x-5)(x-6)$ remainders only (4)(5).
  - 2003學測: $g(x)=f(f(x))$, $f=x^3-2x^2-x+5$ ⇒ $g(2)=f(3)=11$. 2006學測 甲把 $3x^3$ 看成 $2x^3$, 乙把 $2x$ 看成 $-2x$, 餘式相同 ⇒ $a^3=4a$ ⇒ $g=x,x-2,x+2$. **2017指定乙** $f=x^3+ax^2+bx+c$, $f(1)=f(2)=0$, $f(3)=4$ ⇒ $f=(x-1)^2(x-2)$ ⇒ $a+2b+c=-4+10-2=4$, i.e. option (4) (108 answer key prints (2) — misprint).
  - 構造: $f(11)=f(12)=f(13)=1$, $f(14)=19$ ⇒ $f=3(x-11)(x-12)(x-13)+1$; $g(1)=g(3)=g(5)=0,g(7)=96$ ⇒ $2(x-1)(x-3)(x-5)$. $2x^3+mx^2+nx-5$ 被 $x^2+x-2$ 整除 ⇒ $m=\frac92,n=-\frac32$; $3x^4+mx^2+nx-2$ 含 $x^2-x-2$ ⇒ $m=-8,n=-7$; 含 $x^2-x+2$ ⇒ $m=7,n=2$; $x^2+2x+3|3x^4+8x^3+ax^2+4x+b$ ⇒ $a=12,b=-3$.
  - 整數根 via factor theorem: $c(c-a)(c-b)=17$, $0<a<b$ ⇒ $(2,18,1)$; $c(c-a)(c-b)=2$, $a>b>c>0$ ⇒ $a+b+c=6$. 整係數 $f$: $(a-b)|f(a)-f(b)$ ⇒ 歐幾里得年齡 14 (f(7)=77, f(b)=85) ⇒ 生於西元前323年; no $f\in\mathbb Z[x]$ with $f(7)=5,f(15)=10$.
  - 差分: $\deg f=n$ ⇔ $\deg[f(x+h)-f(x+k)]=n-1$; $f(x+1)-2f(x)+f(x-1)=x+1$, $f(0)=0,f(1)=1$ ⇒ $f=\frac16x^3+\frac12x^2+\frac13x$.
  - 係數和+餘式: 係數和12, 奇次項和18, $f\div(x-3)$ 餘 $-4$, 商 Q ⇒ $Q(-1)=5$.
- **一次因式檢驗定理** (99/資優; technique): 整係數 f, $(ax-b)|f$ with $(a,b)=1$ ⇒ $a|a_n$, $b|a_0$ (converse false). Monic integer ⇒ rational roots are integers ⇒ $\sqrt[3]2$ 無理. E.g. $3x^3+5x^2+4x-2$ ⇒ $3x-1$; $2x^4+5x^3-x^2+5x-3$ ⇒ $2x-1$, $x+3$; $6x^4-7x^3+6x^2-1$ ⇒ $2x-1,3x+1$; $7x^5+x^4+\dots-6$ ⇒ $7x-6$; **2016指定乙** $7x^5-2x^4+14x^3-4x^2+7x-2=0$ has root $\frac27$; 四相異有理根 $x^4+ax^3+bx^2+cx+9$ ⇒ roots $\pm1,\pm3$ ⇒ $(0,-10,0)$; $x^4+3x^3+bx^2+cx+10$ ⇒ $b=-11,c=-3$; $x^4-2x^3+px^2+qx+35$ ⇒ max root 7.
- **[超出數A] H.C.F./L.C.M.** (資優9): 輾轉相除 for polynomials; $(x^{50}-2x^2-1,x^{48}-3x^2-4)=x^2+1$; $(x^{100}+5x^2-6,x^{98}-3x^2+2)=x^2-1$; $fg=k\cdot\text{HCF}\cdot\text{LCM}$; 高斯引理 (樸式乘積仍樸式) ⇒ Q[x] 可分解 ⇒ Z[x] 可分解.

### 7.4 插值多項式 (A-11A-2 備註: 牛頓插值)
- n 次以下多項式由 $n+1$ 個點唯一決定 (difference of two such has $n+1$ roots ⇒ zero).
- **Lagrange**: $f(x)=\sum y_i\prod_{j\ne i}\frac{x-x_j}{x_i-x_j}$. **牛頓**: $f(x)=a(x-x_1)(x-x_2)(x-x_3)+b(x-x_1)(x-x_2)+c(x-x_1)+d$, solve successively. E.g. $(1,1),(2,4),(3,9),(4,22)$ ⇒ $f=(x-1)(x-2)(x-3)+(x-1)(x-2)+3(x-1)+1$; $f(18)=8,f(19)=6,f(20)=10$ ⇒ $3(x-18)(x-19)-2(x-18)+8$; $f(6)=2,f(7)=5,f(8)=1$ ⇒ $f(10)=-28$; $1^2+\dots+n^2$ as cubic through $(1,1),(2,5),(3,14),(4,30)$; 心律 data → $f(72)\approx176$.
- **2014學測**: $f(x)=2-2x+4x(x-1)+x(x-1)(x-2)g(x)$ ⇒ $f(1)=0$ ✓, $f(2)=6$ ✓, $f(0)=2$ ⇒ 0 不是根 ✓, 過三點的最低次插值多項式為 $2-2x+4x(x-1)$ ✓; $(x+1)$ 不一定 → (1)(3)(4)(5).
- 餘式 $r(x)$ of $f\div(x-a)(x-b)(x-c)$ = the parabola through $(a,f(a)),(b,f(b)),(c,f(c))$.
- 線性內插 = 一次插值 = 分點公式 (§3 log tables).

### 7.5 函數、一次與二次函數 (F-10-1)
- 函數: 每個 x 唯一對應 y; 定義域/對應法則/值域; 圖形 = $\{(x,f(x))\}$; 鉛直線測試 (每條鉛直線至多交一點). 月份→天數是函數, 天數→月份不是.
- **一次函數** $f(x)=ax+b$: x 每增 h, y 增 ah (等差變化 ⇔ 線性); $a=\frac{\Delta y}{\Delta x}$ (斜率); $\frac{f(b)-f(a)}{b-a}=a$ ($\frac{f(8888)-f(6666)}{2222}=2020$). 內插: $f(c)$ divides like c: $f(1.32)=5,f(3.72)=17$ ⇒ $f(1.92)=8$; $f(1.4)=a,f(3.2)=b$ ⇒ $f(2)=\frac{2a+b}3$. 華氏 $y=\frac95x+32$ (−40 相同). 調分 $30\to50$, $70\to100$: $f=\frac54x+\frac{25}2$, 50→75, 及格需原始≥38. 肱骨: 男 $2.89x+70.64$. 機器人 $A(2,1)\to B(11,16)$ 1h ⇒ 20分鐘 at $(5,6)$.
- **二次函數** forms: 一般式, 頂點式 $a(x-h)^2+k$ ($h=-\frac b{2a}$, $k=-\frac{b^2-4ac}{4a}$), 因式式 $a(x-x_1)(x-x_2)$. Graph transformations from $y=x^2$: 鉛直伸縮 $kf(x)$; 對 x 軸鏡射 $-f(x)$; 平移 $f(x-h)+k$ (right h, up k). |a| 大 → 開口小.
  - 例: $-3x^2+6x+1$ 頂點 $(1,4)$; $y=-3(x+1)^2+1$ from $x^2$ (鏡射→×3→左1→上1); 點 $(a,b)$ 在 $y=2x^2$ 上 ⇒ $(a-3,b-1)$ 在 $y=2x^2+12x+17=2(x+3)^2-1$ 上; 頂點 $(-2,3)$ 過 $(0,-9)$ ⇒ $-3x^2-12x-9$; 過 $(-1,0),(2,3),(0,3)$ ⇒ $-x^2+2x+3$.
  - **極值**: 無限制 → 頂點; 閉區間 $[m,n]$: if $h\in[m,n]$ compare $f(h)$ and the endpoint farther from axis; else monotone on interval. $f=3x^2-12x+7$ on $[0,5]$: max 22, min −5; $-2x^2-4x+1$ on $[-5,-2]$: max 1, min −29. $f=ax^2+2ax+b$ on $[-1,1]$, max 7 min 3 ⇒ $(a,b)=(1,4),(-1,6)$. $ax^2+bx+\frac1a$ max 8 at $x=3$ ⇒ $(-1,6)$. $\sum(x-a_i)^2$ min at mean ($f(3)=10$ for 1..5).
  - Change of variable & domain: $x^2+3y^2=1$ ⇒ $4x+3y^2=-x^2+4x+1$ with $-1\le x\le1$ ⇒ max 4, min −4; $(x^2+3x+1)(x^2+3x+2)+3x^2+9x+2$, $t=x^2+3x\ge-\frac94$ ⇒ min $-\frac{71}{16}$ at $x=-\frac32$; $f(f(x))$ with $f=-x^2+4x+1$, $-1\le x\le6$ ⇒ max 5 at $x=2\pm\sqrt3$, min −164 at 6. 實根條件 restricts parameter: $x_1^2+x_2^2$ max 18 (not 19, since need $D\ge0$, $-4\le k\le-\frac43$).
  - 多選 (87學測): $f=a(x-1)^2+b$, $f(4)>0$, $f(5)<0$ ⇒ a<0, symmetric ⇒ $f(0),f(-1),f(-2)>0$ → (A)(B)(C). (90學測) 過 $(0,-1)$ 與 x 軸相切 ⇒ $a<0$, $c=-1$, $a+b+c\le0$ → (A)(C)(E).
  - 應用: 菜圃 66 m (門2 m) → 17×17; 吊橋 $h=0.03x^2-0.6x+5$ → 最低 2 m at 10 m; 報價 $g=-\frac1{10}x^2+8x$, 獲利最大 x=30 (千個); 套餐 定價 190 元; 睡眠死亡率 $93x^2-1336x+5460$ (min near 7.2 h); 正方形 MNP 面積 min $\frac13$.
  - 恆正/恆負 & 交點: $a>0,D<0$ 恆正 (§7.8). $y=-2x^2+4x+k+1$ 交 x 軸兩點 ⇒ $k>-3$; $2x^2-x-3$ 在 $y=3x+k$ 上方 ⇒ $k<-5$; 兩根距離 $|\alpha-\beta|=\frac{\sqrt D}{|a|}$: $x^2-kx+k$, $AB=\sqrt{21}$ ⇒ $k=-3,7$; $x^2+ax+a-2$: $|\alpha-\beta|^2=(a-2)^2+4$ min at $a=2$ (93指定乙).
- **奇偶函數 & 單調** (99): 奇 $f(-x)=-f(x)$ ⇔ 圖形對稱原點; 偶 ⇔ 對稱 y 軸 (G-10-1 symmetry). Any f = 偶部 + 奇部. $y=x^n$: n 奇 遞增、對稱原點; n 偶 對稱 y 軸. **2017學測** $ax^m$ 與 $bx^n$ ($m\ne n\le4$) 恰3交點 ⇔ m,n 皆偶且 a,b 同號 or 皆奇且同號 → (1)(3). 嚴格遞增/遞減定義. 奇函數 with $f(x-4)=-f(x)$ ⇒ 對稱 $x=2$, 週期 8.
- 其他 (資優10): $|x-a_1|+\dots+|x-a_n|$ 折線 (奇數個 → 尖點最小; 偶數個 → 水平段); $x|x-2|=a$ 恰一解 ⇔ $a>1$ or $a<0$; $|x^2-3x|+x-2=k$ 四解 ⇔ $1<k<2$; $x^2-6|x-1|+1=k$ 四解 ⇔ $-2<k<2$; 高斯函數 $[x]$ (不大於 x 的最大整數), $x-[x]$ 鋸齒.

### 7.6 三次函數的圖形特徵 (F-10-2) — 108 core
- $y=ax^3$: $a>0$ 遞增, $a<0$ 遞減 (proof: $x_1^3-x_2^3=(x_1-x_2)[(x_1+\frac{x_2}2)^2+\frac34x_2^2]$); 對稱原點.
- $y=ax^3+px$: 奇函數 ⇒ 對稱原點. **$ap>0$** (同號): 單調 (一路上升或下降); **$ap<0$** (異號): 上下起伏 (有局部高低點).
- **配方成 $f(x)=a(x-h)^3+p(x-h)+k$** with $h=-\frac b{3a}$ (消去 $(x-h)^2$ 項); via 連續綜合除法 or 乘法公式. ⇒ **對稱中心 $(h,k)=(h,f(h))$**, shape decided by sign of $ap$. 例: $x^3-6x^2+9x+3=(x-2)^3-3(x-2)+5$ (center (2,5), 起伏); $2x^3-6x^2+7x-5=2(x-1)^3+(x-1)-2$ (遞增); $x^3-3x^2+2x+1=(x-1)^3-(x-1)+1$; $x^3-6x^2=(x-2)^3-12(x-2)-16$; $2x^3-2x^2+x+1=2(x-\frac13)^3+\frac13(x-\frac13)+\frac{32}{27}$; $3x^3+9x^2+5x-3$: center $(-1,-2)$ 起伏; $2x^3-12x^2-5x+1$: $(2,-41)$ 起伏; $x^3+3x^2+5x-1$: $(-1,-4)$ 遞增; $x^3+3x^2+1=(x+1)^3-3(x+1)+3$.
- 平移: $-x^3+4x$ 左移1、下移3 ⇒ $g(x)=-(x+1)^3+4(x+1)-3=-x^3-3x^2+x$ ⇒ center $(-1,-3)$, $(a,b)=(1,0)$. 對稱中心 $(-1,4)$ for $3(x-h)^3+7(x-h)+k$ ⇒ $h=-1,k=4$. 賽車道: B(−1,11), C(3,−5) symmetric about center ⇒ center (1,3); $f=(x-1)^3-8(x-1)+3$ (passing points) ⇒ $t=f(4)=6$.
- **局部特徵 (一次近似)**: write $f(x)=A(x-\alpha)^3+B(x-\alpha)^2+C(x-\alpha)+D$; near $x=\alpha$, $f(x)\approx C(x-\alpha)+D$ = **一次近似 = 切線** (slope of secant AP $\to C$). $C=3a\alpha^2+2b\alpha+c$, $D=f(\alpha)$. 例: $2x^3-4x^2+x-1=2(x-2)^3+8(x-2)^2+9(x-2)+1$ ⇒ near 2: $y=9(x-2)+1$, $f(2.001)\approx1.009$; $2x^3-8x^2-5x+1$ at 3: $y=(x-3)-32$; $x^3-4x^2-2x+1$ at −1: $y=9(x+1)-2$; $x^3+3x^2+1$ at −1: $y=-3x$, $f(-1.002)\approx3.006$.
- **大域特徵**: $|x|$ large ⇒ $\frac{f(x)}{ax^3}\to1$; graph looks like $y=ax^3$ (leading term). 例 $2x^3-1000x^2-\dots$ vs $2x^3$. Combined: $a(x+1)^3+b(x+1)+c$ 大域像 $3x^3$, 在 $x=-1$ 近似 $y=-2x+3$ ⇒ $a=3,b=-2,c=5$.
- 多選 (108 習題): $f=2(x+3)^3-4(x+3)+1$: 不是奇函數; 不單調 ($ap<0$); 對稱中心 $(-3,1)$ ✓; 與 x 軸必有交點 ✓ (odd degree); 在 $x=-3$ 一次近似 $y=-4(x+3)+1$ ✓.
- $y=kx^3$ steepness comparison by $|k|$; $f(x+1)+4$, $f(x)-3$, $f(x-1)$ ↔ translations.

### 7.7 多項式方程式 (mostly 99/資優; partly beyond 數A)
- 方程式實根 ⇔ 圖形與 x 軸交點橫坐標; 重根 ↔ 切點. 解方程 ⇔ 因式分解.
- 二次: 公式解; 判別式 (實係數): $D>0$ 兩相異實根, $=0$ 重根, $<0$ 共軛虛根; 有理係數 and D 為完全平方 ⇒ 有理根 ($3x^2+10x+k$ 兩有理根 ⇒ $k=3,7,8$). 根與係數: $\alpha+\beta=-\frac ba$, $\alpha\beta=\frac ca$; $\alpha^2+\beta^2$, $\alpha^3+\beta^3$ via symmetric functions; $(\sqrt\alpha+\sqrt\beta)^2$ with negative roots trap: $x^2+16x+4=0$ ⇒ $=-20$ ($\sqrt\alpha\sqrt\beta=-\sqrt{\alpha\beta}$ for negatives). 黃金比 $\frac{1+\sqrt5}2$ (36°等腰三角形). 甲乙抄錯題: 甲只算錯判別式 ⇒ 兩根和 $\frac{19}{24}=-\frac ba$ 正確; 乙抄錯 $x^2$ 係數 ⇒ $\frac cb$ (= 積/和 之比) 正確 $=\frac{15}{38}$ ⇒ $48x^2-38x-15=0$.
- **[超出數A] 複數** (99 2-3): $i^2=-1$, $i^{4m+k}=i^k$; $\sqrt a\sqrt b=-\sqrt{ab}$ when both negative; 標準式, 共軛 properties; $(x+yi)^2=5+12i$ ⇒ $(3,2),(-3,-2)$. 虛根成對 ($f(\bar z)=\overline{f(z)}$ for real coefficients); 有理係數 ⇒ $a\pm\sqrt b$ 成對; 奇次實係數必有實根. 代數基本定理 (Gauss 1799) ⇒ n 次恰 n 根; Cardano/Tartaglia (三次), Ferrari (四次), Galois (五次以上無公式解). Examples: $x^4-5x^3-2x^2+14x-20$, root $1+i$ ⇒ $1\pm i,-2,5$; $2i-1$ root of $x^4+3x^3+(a+1)x^2+ax+b$ ⇒ $a=7,b=5$; 實係數三次 with $f(i)=0$ ⇒ exactly 1 x-intercept; $x^5+2x^4+3x^3-x^2-2x-3$ with $-1+\sqrt2i$ … ⇒ $(x^2+2x+3)(x-1)(x^2+x+1)$; $x^3+ax+b$ with root $1-2i$ ⇒ $(1,10)$, roots $-2,1\pm2i$, $f<0$ ⇔ $x<-2$.
  - 學測 classics: **2015學測** monic real quadratic: $f(2)=0$ ⇒ $(x-2)|f$ ✓; ⇏ 整係數; $f(\sqrt2)=0$ ⇏ $f(-\sqrt2)=0$ (real but not rational coefficients); $f(2i)=0$ ⇒ $f(-2i)=0$ ✓ and $f=x^2+4$ 整係數 ✓ → (1)(4)(5). **2016學測** $x^4+ax^3+bx^2+cx+2$ (a,b,c 正整數): 無正根 ✓; 不一定有實根/虛根; $f(1)+f(-1)=6+2b$ 偶 ✓; $a+c>b+3$ ⇒ $f(-1)<0<f(0)$ ⇒ root in $(-1,0)$ ✓ → (1)(4)(5). 89學測: $x^3-17x^2+32x-30=0$ 有兩虛根 $a+i,1+bi$ ⇒ 實根 15. 93學測: 三次實係數 with root $1+i$ … (A)(B)(E). 95學測: $ax^2+bx+c$ 整係數有根 $4+3i$, triangle with O area 12.
- 根與係數 (三、四次): $\sum\alpha=-\frac ba$, $\sum\alpha\beta=\frac ca$, $\alpha\beta\gamma=-\frac da$; 四次 analog with $+\frac ea$. $2x^3+3x-5$: $\frac1\alpha+\frac1\beta+\frac1\gamma=\frac35$, $\sum\alpha^2=-3$. 四根等差 $x^4-4x^3-34x^2+ax+b$ ⇒ roots $-5,-1,3,7$, $a=76,b=105$. 兩根比 2:3 & 另兩根差1 ⇒ $a=36,b=720$. 兩根積 −4 ⇒ factor $(x^2+ax-4)(x^2+bx+3)$.
- **勘根定理**: $f(a)f(b)<0$ ⇒ root in $(a,b)$ (converse false: $f(a)f(b)>0$ may still have roots). $12x^3-8x^2-23x+11$: roots in $(-2,-1),(0,1),(1,2)$; $x^4-4x^3-3x^2+x+1$ root in (0,1) (91指定乙); $x^3-8x+1$ 負根最接近 −3; $x^3+x-5$ 恰一實根 (increasing); $x^n=a$ 恰一正根 ⇒ defines $\sqrt[n]a$. **2014學測** $f$ 實係數二次, $f(1)>0$, $f(2)<0$, $f(3)>0$ (so f opens upward), $g=f+(x-2)(x-3)$: g also opens upward; $g(1)=f(1)+2>f(1)$ ✓; $g(1)>0>g(2)=f(2)$ ⇒ g 在 1,2 間恰一實根 ✓; for f's larger root $\alpha\in(2,3)$, $g(\alpha)=(\alpha-2)(\alpha-3)<0$ ✗ → (3)(4). $(x-a)(x-b)+(x-b)(x-c)+(x-c)(x-a)=0$ ($a<b<c$) ⇒ $a<\alpha<b<\beta<c$. 二次根的位置: $ax^2-(a-1)x-6$ 一根在(1,2) 一根在(−2,−1) ⇒ $2<a<\frac72$; $x^2+(a-5)x+a+3$ 兩正根 ⇒ $-3<a\le1$; $ax^2+(1-5a)x+6a$ 二根 >1 ⇒ $a<-\frac12$ or $a\ge5+2\sqrt6$.
- 特殊解法: 倒數方程 $12x^4-56x^3+89x^2-56x+12$ ($t=x+\frac1x$) ⇒ $\frac12,2,\frac23,\frac32$; $(x+1)(x+3)(x+5)(x+7)+15=0$ (pair to $y=x^2+8x$) ⇒ $-2,-6,-4\pm\sqrt6$; $x^4-4x^3+x^2+4x+1=0$ ⇒ $\frac{1\pm\sqrt5}2,\frac{3\pm\sqrt{13}}2$; symmetric system $a+b+c=2$, $ab+bc+ca=-5$, $abc=-6$ ⇒ roots of $x^3-2x^2-5x+6$ = $1,3,-2$.
- 選舉保證當選: 250 票選7人 ⇒ $x>\frac{250}8$ ⇒ 32 票.

### 7.8 多項式不等式 (F-10-3)
- 方法: (代數) 數線分段 sign chart; (幾何) sketch $y=f(x)$, read where graph is above/below x 軸. Adjust leading coefficient to positive first.
- **二次**: $a>0$: $D>0$ ⇒ $>0$ 為 $x<\alpha$ or $x>\beta$ (大於大根或小於小根), $<0$ 為 $\alpha<x<\beta$; $D=0$ ⇒ $>0$ 為 $x\ne\alpha$, $<0$ 無解, $\le0$ 只有 $x=\alpha$; $D<0$ ⇒ $>0$ 全體實數, $<0$ 無解. E.g. $16x^2-22x-3\le0$ ⇒ $-\frac18\le x\le\frac32$; $-4\le x^2-5x<6$ ⇒ $-1<x\le1$ or $4\le x<6$; $9x^2+1\le6x$ ⇒ $x=\frac13$; $x^2-2\sqrt3x+5>0$ 全體.
- **恆正/恆負**: $\forall x$, $ax^2+bx+c>0$ ⇔ $a>0,D<0$; $<0$ ⇔ $a<0,D<0$; $\ge0$ ⇔ $a>0,D\le0$; (check the degenerate $a=0$ case separately!). $(3-a)x^2+ax-2a>0$ ⇒ $a<0$; $(m-2)x^2+2(2m-3)x+5m-6>0$ ⇒ $m>3$; $kx^2+8x+k+6<0$ ⇒ $k<-8$; $kx^2+2x+k$ 圖形在 x 軸下方 ⇒ $k<-1$; $x^2+2(m+2)x+2m^2<0$ 無解 ⇒ $D\le0$ ⇒ $m\le2-2\sqrt2$ or $m\ge2+2\sqrt2$; $f=x^2-(k-3)x+4$ 恆在 $g=-x^2+(k-1)x+k-2$ 上方 ⇒ $-2<k<4$; $\frac{x^2+2ax+1}{3x^2-2x+3}\le5$ ∀x ⇒ $-19\le a\le9$; $-x^2+2(3m-1)x-(8m^2+17)\ge0$ 無解 ⇒ $-2<m<8$; $y=2x^2-2ax+5+2a$ 恆在 $y=ax^2$ 上方 ⇒ $-2<a<\frac53$; $(2k-3)x^2-2kx+k+2<0$ 無解 ⇒ $k\ge2$; 區間上恆負: $2x^2+(a-1)x-a(a-1)<0$ on $[0,1]$ ⇒ check endpoints ⇒ $a<-1$ or $a>3$.
- 反求係數: $x^2+ax+b<0$ 解 $\frac{-3-\sqrt5}2<x<\frac{-3+\sqrt5}2$ ⇒ $a=3,b=1$ ⇒ $x^2+ax-4b>0$: $x>1$ or $x<-4$. $ax^2-3x+b>0$ 解 $-3<x<\frac12$ ⇒ $a=-\frac65,b=\frac95$. $ax^3+bx^2+cx-6\le0$ 解 $[-2,1]\cup[3,\infty)$ ⇒ $a=-1,b=2,c=5$. $\{x^2-3x+a\ge0,\ x^2-x+b<0\}$ 解 $-3<x\le-1$ ⇒ −3 is a root of the strict one ($b=-12$, giving $(-3,4)$), −1 a root of the other ($a=-4$, giving $x\le-1$ or $x\ge4$) ⇒ $(a,b)=(-4,-12)$. $f(t)<0$ 解 $(-2,3)$ ⇒ $f(2x)<0$: $-1<x<\frac32$; $f(x-2)<0$: $0<x<5$.
- **高次**: factor; 恆正二次因式 drop; **重因式**: 偶次 → sign unchanged across root (exclude/include the root per strict/non-strict), 奇次 → sign changes. Local behaviour: near root α of multiplicity m, $f\approx Q(\alpha)(x-\alpha)^m$. 例: $(x+1)(x-2)(x-3)<0$ ⇒ $x<-1$ or $2<x<3$; $(x-1)(x-3)(5-x)<0$ ⇒ $1<x<3$ or $x>5$; $(x^2+x+1)(x-1)(x+1)\le0$ ⇒ $[-1,1]$; $(x+3)^3(x-1)^2(x-2)<0$ ⇒ $-3<x<2$, $x\ne1$; $\le0$ ⇒ $-3\le x\le2$; $(x-1)(x+2)^2\ge0$ ⇒ $x\ge1$ or $x=-2$; $(x^2-4x+4)(x-5)\ge0$ ⇒ $x\ge5$ or $x=2$; $(x+2)^2(x-1)^3(x-3)\le0$ ⇒ $1\le x\le3$ or $x=-2$; $(x-1)^{80}(x^2+x+1)(x-2)(x-3)(x-4)^4<0$ ⇒ $2<x<3$; $(x^3-1)(x^4-16)\le0$ ⇒ $x\le-2$ or $1\le x\le2$.
- **分式不等式**: $\frac fg>0$ ⇔ $fg>0$; $\frac fg\ge0$ ⇔ $fg\ge0$ and $g\ne0$; never multiply by $g$ of unknown sign. $x>\frac1x$ ⇒ $x>1$ or $-1<x<0$; $\frac{x+2}{(x^2+x+1)(x-1)}\le0$ ⇒ $-2\le x<1$; $\frac{2x+5}{3x-4}\ge0$ ⇒ $x\le-\frac52$ or $x>\frac43$; $\frac{2x^2-4x-6}{x^2-x-2}<1$ ⇒ $2<x<4$; $\frac2{x+1}<x$ ⇒ $-2<x<-1$ or $x>1$. 多選: $\frac{x-2}{x^2+x+3}<2$ ⇔ $x-2<2(x^2+x+3)$ ✓ (denominator always positive); $\frac{x+5}{x^2-x-2}>0$ ⇔ product $>0$ ✓; with ≥ ✗ (must exclude zeros of denominator).
- 讀圖: given graph of f (with tangency at double root), write $f\ge0$ etc.; $x^3\ge x^2+x$ ⇒ $\frac{1-\sqrt5}2\le x\le0$ or $x\ge\frac{1+\sqrt5}2$; $|x^2-2x-3|\ge x+1$ ⇒ $x\le2$ or $x\ge4$.
- 應用: 白鐵板 6×4 截角, 容積 ≥8 ⇒ $2-\sqrt2\le x\le1$; 12×10 鐵板容積 ≥80 ⇒ $1\le x\le5-\sqrt5$ (99) / GeoGebra $1<x<2.76$; 剎車距離 $f(v)=\frac{v^2}{100}+\frac v5\le15$ ⇒ $(v+50)(v-30)\le0$ ⇒ $v\le30$ m/s = 108 km/h; 售價 $(a-21)(350-10a)\ge400$ ⇒ $25\le a\le31$; 長方體烤漆 ≤ 成本/3 ⇒ 邊長 20–50 cm; 大砲 $y=kt(6-t)$ 不打到天花板 ⇒ 最大高度 $9k$ (at $t=3$) 小於天花板高度 (with 16 m this gives $0<k<\frac{16}9$; the 108 key prints $\frac43$, which matches a 12 m ceiling — quote the method, not the number); 儲存桶 ⇒ 8–10 m.

---

## 8. 數列、級數、數學歸納法、遞迴

**Scope**: N-10-6 數列、級數與遞迴關係 (有限項遞迴數列, 有限項等比級數, 常用的求和公式, 數學歸納法; **遞迴關係以一階為主**, 連結國中等差/等比; 歸納法先觀察發現規律再證明, 不必過度練習; 可連結常用對數求解 $a^x=b$). Formula sheet prints 等差/等比前 n 項和. **[超出數A]**: 二階線性遞迴/特徵方程 (Fibonacci closed form), 無窮級數 & 極限 (§25), 第二數學歸納法/雙基歸納法. **Sources**: 108一下 1-1數列與數學歸納法, 1-2級數; 99第二冊 1-1數列, 1-2級數; 資優 第5單元數列級數, 第7單元數學歸納法(與遞迴方法), 第43單元遞迴方法.

### 8.1 數列
- 數列 $\langle a_n\rangle$: 有限/無限; 首項, 末項; 表徵: 列舉型, 概括型, **n 項型 (一般項)** e.g. $\langle3n-2\rangle$. Find general term: $\langle1,1,3,3,5,5,\dots\rangle$: $n-\frac{1+(-1)^n}2$; $\langle\frac{-1}{1\cdot3},\frac1{2\cdot5},\dots\rangle$: $\frac{(-1)^n}{n(2n+1)}$; $\langle1,\frac13,\frac16,\frac1{10}\rangle$: $\frac2{n(n+1)}$; $\langle1,2,2,3,3,3,\dots\rangle$ 第200項 20; $1,\frac12,\frac22,\frac13,\frac23,\frac33,\dots$ 第244項 $\frac{13}{22}$, $\frac{13}{29}$ 是第419項. $9,99,999,\dots$: $10^n-1$; $1,11,111$: $\frac19(10^n-1)$.
- **等差數列**: $a_n=a_1+(n-1)d$, $a_m=a_n+(m-n)d$; 等差中項 $b=\frac{a+c}2$. $a_3=-4,a_8=16$ ⇒ $a_1=-8,d=2$; $a_1=-27,d=2$ 第15項開始為正; $a_2=1,a_8=37$ ⇒ $a_{20}=109$; 數手指 (1→拇指 …) 200 落在食指; 2018年1月週六日期 6,13,20,27.
- **等比數列**: $a_1\ne0$, $\frac{a_{n+1}}{a_n}=r\ne0$, $a_n=a_1r^{n-1}$; 等比中項 $b^2=ac$ (4,9 的等比中項 $\pm6$). 光圈值 $2,2\sqrt2,4,\dots$ ($r=\sqrt2$, 32 是第9項; 透光面積每格 ×2 ⇒ 光圈值 ×$\sqrt2$). $a_5=48,a_8=384$ ⇒ $a_1=3$, $a_{10}=1536$; $a_5=45,a_7=135$ ⇒ $r^2=3$, $r=\pm\sqrt3$, $a_1=5$; 四正數等比 $a+b=8$, $c+d=72$ ⇒ $r=3$; 首項16 公比 $\frac12$ 前10項之積 $\frac1{32}$; 四數等比 和200 首末和140 ⇒ 5,15,45,135; $a,50,80,130$ 減同數成等比 ⇒ $a=32$; $5,a,b,-1$ 等差, $a,b,p,q$ 等比 ⇒ $q=\frac19$.
- **2006學測**: $a_1..a_4$ 等差, $0<a_1<2$, $a_3=4$, $b_n=2^{a_n}$ ⇒ $\langle b_n\rangle$ 等比 ✓, $b_1<b_2$ ✓, $b_2>4$ ✓, $b_4>32$ ✓, $b_2b_4=2^{2a_3}=256$ ✓ → 全選.
- 108 習題 多選: $a_{10}=20,a_{20}=10$ ⇒ $d=-1$, $a_1=29$, $a_{15}=15$, 0 is $a_{30}$, 29 positive terms → (1)(3)(4).

### 8.2 遞迴關係 (一階為主)
- 遞迴關係式 + 初始值 defines 遞迴數列 (e.g. $a_1=5$, $a_n=a_{n-1}+3$). Excel/計算機 can iterate.
- **Solving one-step recurrences**:
  - $a_{n+1}=a_n+f(n)$ (階差): $a_n=a_1+\sum_{k=1}^{n-1}f(k)$ (累加). $a_n=a_{n-1}+4n$, $a_1=5$ ⇒ $a_n=2n^2+2n+1$, $a_{100}=20201$; $a_n=a_{n-1}+(2n+1)$, $a_1=1$ ⇒ $n^2+2n-2$; 奇數排三角形第 n 列首項 $a_n=a_{n-1}+2(n-1)$ ⇒ $n^2-n+1$; $a_{n+1}=a_n+3n^2$ ⇒ $\frac12(2n^3-3n^2+n+2)$; 1,5,12,22,35,… ($a_{n+1}-a_n=3n+1$) ⇒ $\frac12(3n^2-n)$, $a_{30}=1335$; $a_{n+1}=a_n+5(n-1)$ ⇒ $\frac12(5n^2-15n+12)$.
  - $a_{n+1}=a_n\cdot f(n)$ (累乘): $a_{n+1}=\frac n{n+1}a_n$, $a_1=2$ ⇒ $\frac2n$; $a_{n+1}=2^na_n$ ⇒ $a_n=2^{\frac{n^2-n+2}2}$; $a_n=(1-\frac1{n^2})a_{n-1}$ ⇒ $\frac{n+1}{2n}$; $a_{n+1}=\frac{n+1}na_n$ ⇒ $n$.
  - **$a_{n+1}=pa_n+q$** ($p\ne1$): find fixed point $\alpha=\frac q{1-p}$, then $a_n-\alpha=p^{n-1}(a_1-\alpha)$. 河內塔 $a_n=2a_{n-1}+1$ ⇒ $2^n-1$; $a_n=3a_{n-1}+4$, $a_1=1$ ⇒ $3^n-2$; $a_{n+1}=3a_n-2$, $a_1=2$ ⇒ $3^{n-1}+1$; $a_{n+1}=3a_n+1$ ⇒ $\frac12(3^n-1)$; $a_n=\frac23a_{n-1}+5$, $a_1=1$ ⇒ $15-14(\frac23)^{n-1}$; 細胞 7 個, 每小時死3 其餘分裂 ⇒ $a_n=2(a_{n-1}-3)$ ⇒ $6+2^n$ (8,10,14); 死2 ⇒ $a_{n+1}=2(a_n-2)$ ⇒ $3\cdot2^n+4$, 超過1000 需9小時; 先加4再乘3 ⇒ $8\cdot3^{n-1}-6$; $a_{n+1}+1=2(a_n+1)$, $a_1=3$ ⇒ $a_{10}=2^{11}-1$; $5a_{n+1}=3a_n+2$, $a_1=3$ ⇒ $1+2(\frac35)^{n-1}$; $a_{n+1}=1+\frac23a_n$ ⇒ $3-2(\frac23)^{n-1}$.
  - 分式型: $a_{n+1}=\frac{2a_n}{a_n+2}$, $a_1=\frac12$ ⇒ $\frac2{n+3}$ (guess & prove or take reciprocals); $a_{n+1}=\frac{3a_n-1}{4a_n-1}$, $a_1=1$ ⇒ $\frac{2n-1}n$; $a_{n-1}-a_n=na_na_{n-1}$ ⇒ $\frac1{a_n}-\frac1{a_{n-1}}=n$ ⇒ $a_n=\frac2{n(n+1)}$.
  - 不動點/近似: $a_{n+1}=\frac12(a_n+\frac2{a_n})$ → $\sqrt2$ (Newton); $a_{n+1}=1+\frac1{a_n}$ → 黃金比 $\varphi=\frac{1+\sqrt5}2$.
- **建立遞迴 (模型)**: 河內塔 $a_n=2a_{n-1}+1$ (64 盤 $2^{64}-1$); n 條直線(兩兩不平行、三線不共點)分割平面 $a_n=a_{n-1}+n$ ⇒ $\frac{n^2+n+2}2$ (10 條 → 56; the 資優43 key prints 61 — misprint); 過定點的 n 個圓最多分平面 $a_{n+1}=a_n+(n+1)$ ⇒ $1+\frac{n(n+1)}2$; 三角形數 $a_n=a_{n-1}+n$; 正方形點陣 $a_n=a_{n-1}+4n$; 正五邊形點 $a_{n+1}-a_n=3n+4$ ⇒ $\frac32n^2+\frac52n+1$; 四面體焊接點 4,10,20,35,56 (91指定乙: 六層56; 八層120); 黑白地磚 $a_n=a_{n-1}+5$ ⇒ $5n+3$ (第30個153); 火柴正方形 $a_{n+1}-a_n=4n+4$ ⇒ $2n^2+2n$ ($a_{12}=312$); 地毯 (九宮格去左上) $a_{n+1}=8a_n$, 超過1000 從第5圖; Sierpiński 移走倒三角 $a_1=\frac k4$, $a_{n+1}=\frac34a_n$; 移走個數 $3^{n-1}$; 剩餘面積 $S_n=\frac34S_{n-1}$; **Koch 雪花** 周長 $a_{n+1}=\frac43a_n$, $a_1=3$ ⇒ $3(\frac43)^{n-1}$; 正方形取中點連續內接: 面積 ×½ (40 → 第6個 $\frac54$); 跳蟲(奇跳1偶跳3) 127下後在2號; 機器狗 前3後2 (91學測) P(3)=3,P(5)=1,P(10)=2,P(101)=21, P(103)>P(104) → (A)(B)(C)(D); 存款 年初存1萬 7% ⇒ $a_n=1.07(a_{n-1}+10000)$ ⇒ $a_n=\frac{10700}{0.07}(1.07^n-1)$; 貸款 $a_{n+1}=(1+r)a_n-k$.
- **2015學測**: 1,2,6,15,31 satisfies $a_{t+1}=a_t+t^2$ → (3). **2017學測**: $a_n=a_{n-1}+f(n-2)$, f 二次, $a_1..a_4=1,2,5,12$ ⇒ $f(0)=1,f(1)=3,f(2)=7$ ⇒ $f=x^2+x+1$ ⇒ $a_5=12+13=25$. **92指定乙**: $a_{n+1}=\frac72a_n(1-a_n)$, $a_1=\frac17,a_2=\frac37$ ⇒ cycle $\frac37,\frac67$ ⇒ $a_{101}-a_{100}=\frac37$. **2005指定乙** 蛇形排列 第99列從左第67個 = 4884. **2008指定甲** 正三角形+正方形 陣列 (邊n) 共 m 顆, 排正五邊形多9 ⇒ $n=9$, $m=126$.
- **計數型遞迴** (資優/108 進階): 上樓梯 1 或 2 階 $a_n=a_{n-1}+a_{n-2}$ (8階34種); 0/1 字串無相鄰1: $a_n=a_{n-1}+a_{n-2}$, $a_2=3,a_3=5$, $a_{12}=377$; 囚犯取不相鄰 $F(n)=F(n-1)+F(n-2)+1$; 3色塗 2×n 方格 $a_{n+1}=3a_n$ ($a_1=6$); 警報器 1秒/2秒 + 間隔 $a_n=a_{n-2}+a_{n-3}$; 錯排 $g_n=(n-1)(g_{n-1}+g_{n-2})$, $g_1..g_4=0,1,2,9$; 傳球 甲乙丙 10 次回到甲 $a_{n+1}+a_n=2^n$ ⇒ 342; 偶數個0 的 n 位字串 $5\cdot10^{n-1}+4\cdot8^{n-1}$; $x+y\le2n+1$ 非負整數解 $(2n+3)(n+1)$; 費氏兔子 $F_n=F_{n-1}+F_{n-2}$, 12個月 144 對.
- **[超出數A] 二階常係數**: $a_{n+1}=c_1a_n+c_2a_{n-1}$, 特徵方程 $x^2-c_1x-c_2=0$: 相異根 $a_n=A\alpha^n+B\beta^n$; 重根 $(A+nB)\alpha^n$. Fibonacci $F_n=\frac1{\sqrt5}[(\frac{1+\sqrt5}2)^n-(\frac{1-\sqrt5}2)^n]$; $a_n-6a_{n-1}+9a_{n-2}=0$, $a_1=3,a_2=0$ ⇒ $(2-n)3^n$; $a_n=10a_{n-1}-21a_{n-2}$ ⇒ $-6\cdot3^n+3\cdot7^n$.

### 8.3 數學歸納法 (N-10-6)
- **原理**: (1) $P(n_0)$ 成立 (起始步驟); (2) 若 $P(k)$ 成立 ($k\ge n_0$) 則 $P(k+1)$ 成立 (遞推步驟; 「假設 $P(k)$ 成立」= 歸納假設) ⇒ $P(n)$ for all $n\ge n_0$. 骨牌比喻. **Both steps required**: 「n=n+1」 has a valid inductive step but no base; 「任何 n 個人一樣高」 fails at $k=1\to2$ (no overlap).
- 觀察→歸納→臆測→驗證; 有限驗證不夠: $n^2+n+41$ 在 $n=41$ 非質數 ($41\cdot43$); 費馬數 $F_5=641\times6700417$; Goldbach-type conjectures.
- 經典證明: $a_n=2^n-1$ (河內塔); $a_n=2n^2+2n+1$; $1+3+\dots+(2n-1)=n^2$ (Maurolico); $\sum k$, $\sum k^2$, $\sum k^3$ formulas; $10^n+3\cdot4^n+5$ 被9整除 ($a_{k+1}=10a_k-9(2\cdot4^k+5)$); $4^n+2$ 為 6 的倍數; $3^{2n+1}+2^{n+2}$ 為 7 的倍數; $2^{4n+1}-6^n$ 個位數恆為 6; $1^2-2^2+3^2-\dots+(-1)^{n+1}n^2=(-1)^{n+1}\frac{n(n+1)}2$; $\prod_{k=1}^n(1+\frac{2k+1}{k^2})=\prod\frac{(k+1)^2}{k^2}=(n+1)^2$ (telescoping product); $(1-\frac14)(1-\frac19)\cdots(1-\frac1{n^2})=\frac{n+1}{2n}$; $\sum\frac1{k^2}\le2-\frac1n$; $2^n\ge n^2$ ($n\ge4$); $5^n>2^n+3^n$ ($n>2$); 貝努利 $(1+a)^n\ge1+na$; $\frac{1\cdot3\cdots(2n-1)}{2\cdot4\cdots2n}<\frac1{\sqrt{2n+1}}$; $1+\frac12+\dots+\frac1n\ge\frac{2n}{n+1}$; $x_1^n+x_2^n\in\mathbb N$ for roots of $x^2-6x+1$ (雙基); 算幾不等式 n 項 (forward-backward); $\sum_{k}k^2 2^k=(n^2-2n+3)2^{n+1}-6$; $0.\underbrace{9\cdots9}_n<1$ for all n does **not** imply $0.\bar9<1$ (limits can attain bound).

### 8.4 級數與 Σ
- **Σ 記號**: $\sum_{k=1}^na_k$; rewrite: find general term $a_k$ and number of terms (11+14+…+305 = $\sum_{k=1}^{99}(3k+8)$; $3+\frac32+\dots+\frac3{2^{12}}=\sum_{k=1}^{13}3(\frac12)^{k-1}$; $3\times5+6\times7+\dots+57\times41=\sum_{k=1}^{19}3k(2k+3)$). 下標 dummy; $\sum_{k=1}^{10}a_k=\sum_{k=2}^{11}a_{k-1}$.
- **性質**: $\sum(a_k\pm b_k)=\sum a_k\pm\sum b_k$; $\sum ca_k=c\sum a_k$; $\sum_{k=1}^nc=nc$. **Traps**: $\sum a_kb_k\ne\sum a_k\sum b_k$; $\sum k^2\ne(\sum k)^2$; don't write $\sum a_n$ with the wrong index. $\sum_{k=1}^{100}a_k=23$, $\sum b_k=12$ ⇒ $\sum(2a_k-b_k)=34$.
- **等差級數** $S_n=\frac n2(a_1+a_n)=\frac n2[2a_1+(n-1)d]$; 對稱項和相等 ($a_1+a_{99}=8$ ⇒ $a_{50}=4$, $a_{11}+a_{89}=8$, $S_{99}=396$). 101項和0, $a_{71}=71$ ⇒ $a_{51}=0$, $a_3+a_{99}=0$, $a_1<0$ → (C)(E). 前4項和12, 後4項和120, 總和198 ⇒ 12項. $S_n$ 最小: $a_1=-200,d=7$ ⇒ $n=29$, $S=-2958$. 三位數中4的倍數和 123300. 二等差數列前n項和比 $(3n+1):(7n-11)$ ⇒ 第7項比 $=S_{13}:T_{13}=40:80=1:2$; $(7n+1):(4n+27)$ ⇒ $a_{11}:b_{11}=4:3$. $S_n=9,S_{2n}=12$ ⇒ $S_{3n}=9$ (blocks form AP). 96學測 25排、第13排64座 ⇒ 1600; 93學測 10項, 奇數項和15、偶數項和30 ⇒ $d=3$.
- **等比級數** $S_n=\frac{a_1(1-r^n)}{1-r}$ ($r\ne1$), $na_1$ ($r=1$); proof $S_n-rS_n$. 首項3公比2 前5項 93; $1+\sqrt2+2+\dots+16=15(\sqrt2+1)$; $a_1+a_2+a_3=21$, $a_2+a_3+a_4=42$ ⇒ $r=2$, $S_7=381$; $a_9=\frac14,a_{10}=\frac18$ ⇒ $S_{10}=\frac{1023}8$; $S_{10}=2,S_{30}=14$ ⇒ $S_{60}=126$ (block ratio $q=r^{10}=2$); $S_n=24,S_{2n}=30$ ⇒ $S_{3n}=\frac{63}2$; Sierpiński 前10次移去面積 $16[1-(\frac34)^{10}]$; 正方形中點連續 周長和 $70+35\sqrt2$, 面積和 $200(1-\frac1{64})$. **2016學測**: $\sum_{k=1}^{10}a_k=80$, 奇數項和120 ⇒ $1+r=\frac{80}{120}$ ⇒ $r=-\frac13$ ⇒ $a_1=\frac{80\cdot\frac43}{1-3^{-10}}\approx106.7$ → (4). 三數等比 和39, 各減1,2,12 成等差 ⇒ 4,10,25 (或25,10,4). 「9+99+…」 $=\frac{10}9(10^n-1)-n$; $0.9+0.99+\dots=n-\frac19(1-10^{-n})$; $7.7+77.77+\dots=\frac7{81}(10^{n+1}-11+10^{-n})$.
- **常用求和公式**: $\sum k=\frac{n(n+1)}2$; $\sum k^2=\frac{n(n+1)(2n+1)}6$; $\sum k^3=[\frac{n(n+1)}2]^2$ (guess by $\frac{S_n}{T_n}=\frac{2n+1}3$; prove by 歸納 or 遞迴法 telescoping $(k+1)^3-k^3=3k^2+3k+1$; 圖解法). $1^2+\dots+20^2=2870$; $11^2+\dots+20^2=2486$; $3^3+\dots+10^3=3016$; $2^3+4^3+\dots+40^3=352800$; $11^3+\dots+20^3=41075$; $2^2+\dots+20^2$ (偶) 1540; $1^2+3^2+\dots+19^2=1330$; $11^2+13^2+\dots+31^2=5291$; $10^3+\dots+20^3=42075$.
- **多項式型級數**: expand $a_k$ then use formulas: $\sum k(2k+1)$ (1×3+…+20×41) 5950, general $\frac{n(n+1)(4n+5)}6$; $\sum(2k-1)(2k+1)=\frac{n(4n^2+6n-1)}3$ (15 terms 4945); $\sum k(4k+1)$ 4165; $1\cdot2+2\cdot5+3\cdot8+\dots=n^2(n+1)$; $\sum_{k=5}^n k(k+3)=\frac{n(n+1)(n+5)}3-60$; 長方形垛 $k(k+2)$ 十層 495; 三角垛 $\frac{k(k+1)}2$ 十二層 364, n 層 $\frac{n(n+1)(n+2)}6$; 堆垛 $k(k+1)$ 十層 440; $\sum(k^2-2k)_{1}^{20}=2450$; $69\times71+68\times72+\dots+1\times139=226205$; $\sum k(2k-1)(3k+1)_{1}^{10}=17710$; $1+(1+3)+\dots=\frac{n(n+1)(2n+1)}6$; $\sum(1+2+\dots+2^{k-1})_{k=1}^{10}=2036$; $2\times2+4\times5+\dots+66\times98=74052$.
- **由 $S_n$ 求 $a_n$**: $a_1=S_1$, $a_n=S_n-S_{n-1}$ ($n\ge2$) — check whether $n=1$ fits. $S_n=3n^2+4$ ⇒ $a_1=7$, $a_n=6n-3$ ($n\ge2$), $a_{10}=57$; $S_n=n^2+2n$ ⇒ $2n+1$ ∀n; $S_n=n^2+5$ ⇒ $a_1=6$, $2n-1$; $\sum_{k=1}^nka_k=n^2+3n+1$ ⇒ $na_n=2n+2$ ($n\ge2$), $a_1=5$ ⇒ $a_{20}=\frac{21}{10}$.
- **裂項 (telescoping)**: $\frac1{k(k+1)}=\frac1k-\frac1{k+1}$ ⇒ $\sum_1^n=\frac n{n+1}$ ($\frac{99}{100}$, $\frac{30}{31}$); $\frac1{(2k-1)(2k+1)}=\frac12(\frac1{2k-1}-\frac1{2k+1})$ ⇒ $\frac12(1-\frac1{2n+1})$; $\frac1{k(k+2)}$ ⇒ $\frac12(\frac32-\frac1{n+1}-\frac1{n+2})$; $\frac1{k(k+1)(k+2)}=\frac12[\frac1{k(k+1)}-\frac1{(k+1)(k+2)}]$ ⇒ $\sum_1^{100}=\frac{2575}{10302}$; $\frac1{\sqrt{k+1}+\sqrt k}=\sqrt{k+1}-\sqrt k$ ⇒ $\sum_1^{99}=9$, $\sum_1^{120}=10$; $\frac k{(k+1)!}=\frac1{k!}-\frac1{(k+1)!}$ ⇒ $1-\frac1{(n+1)!}$; $\sum\frac{2k+1}{1^2+\dots+k^2}=\sum\frac6{k(k+1)}=\frac{6n}{n+1}$; $\sum\frac1{a_k}$ with $a_k=1+\dots+k$ ⇒ $2(1-\frac1{n+1})$; $\sum\log_2\frac{k+1}k$-type collapses ($\sum_{12}^{191}\log_2\frac{k+1}{k}=4$).
- **錯位相減 (等差×等比)**: $1+2\cdot2+3\cdot2^2+\dots+n2^{n-1}=(n-1)2^n+1$.
- 其他: 去掉2,3,5倍數的自然數 (週期30 中8個: 1,7,11,13,17,19,23,29): 小於60 有16個, 第1000項 3749, $S_{1000}=1875000$; $1,3,\dots,2n-1$ 中任取二數相乘之和 $\frac{n(n-1)(3n^2-n-1)}6$ (via $(\sum)^2=\sum x^2+2\sum_{i<j}$).

### 8.5 複利與年金 (N-10-6 × N-10-4)
- 單利 $A(1+nr)$ (等差); 複利 $A(1+r)^n$ (等比). 年利率1.2%, 10萬, 3年: 單利103600, 複利103643; 每年初存10萬 3年 307258; 1% 10萬 10年 110462; 借100萬 年利2% 半年複利 3年 1061520; 每年初存1萬 1% 10年 105668 (年金 = 等比級數 $\sum_{k=1}^{10}10000(1.01)^k$).

---

## 9. 數據分析（一維、二維）

**Scope**: D-10-2 數據分析 (一維: 平均數、標準差、百分位數; 二維: 散布圖、最適直線、相關係數、數據標準化; 最適直線 taught via 平均數0 數據 through origin; 統計量定義可能略有不同). Formula sheet gives $\mu$, $\sigma=\sqrt{\frac1n\sum(x_i-\mu)^2}=\sqrt{\frac1n(\sum x_i^2-n\mu^2)}$, $r=\frac{\sum(x_i-\mu_X)(y_i-\mu_Y)}{n\sigma_X\sigma_Y}$, 迴歸直線 $y-\mu_Y=r\frac{\sigma_Y}{\sigma_X}(x-\mu_X)$ — **學測 uses population σ (÷n)**. 用柯西解釋 $|r|\le1$ is ※. 樣本標準差 (÷(n−1)), 已分組資料公式, 平均絕對離差 are 99/資優 extras. **Sources**: 108一下 2-1一維數據分析, 2-2二維數據分析; 99第二冊 4-1單變量數據分析, 4-2雙變量數據分析; 資優 第47單元單變數資料的分析, 第50單元雙變數資料的分析.

### 9.1 統計圖表 (99)
- 數據型態: 離散 (名目數據 e.g. 血型/性別; 次序數據 e.g. 名次) vs 連續 (身高、重量). 長條圖 (離散, bars separated), 圓餅圖 (圓心角 ∝ 次數), 直方圖 (連續, bars adjacent, 組距, 含下界不含上界), 次數分配折線圖 (頂邊中點連線, 兩端補 0), 相對次數, **累積次數分配折線圖** (以各組上界為橫坐標; read medians/percentiles off it).
- 形狀: 對稱/單峰, **右偏** (右尾長 ⇒ 平均數 > 中位數), 左偏 (平均 < 中位), 雙峰 (e.g. 城鄉差距). 眾數 = 尖峰點, 中位數 = 等面積點, 平均數 = 平衡點 (翹翹板). 對稱 → use 平均數+標準差; 偏斜 → 五數 (最小值, Q1, 中位數, Q3, 最大值). 94指考物理 分布右偏, 均標23 ⇒ 平均 > 23.

### 9.2 集中趨勢
- **算術平均數** $\mu=\frac1n\sum x_i$; $\sum(x_i-\mu)=0$; 易受極端值影響. 中位數: odd n → middle; even → average of two middle (3,5,6,9,11,13,20,30 → 10). Basketball 25,35,60,70,75,80,90,85,20 → μ=60, Me=70; 186,188,189,191,226 → μ=196, Me=189.
- **線性變換** $Y=aX+b$: $\mu_Y=a\mu_X+b$; 中位數、加權平均同樣變換; ×1.5+10: 48 → 82.
- 合併資料平均 $=\frac{N_1\bar y_1+N_2\bar y_2}{N_1+N_2}$ (not the simple average). 90學科: 男600人 36%, 女400人 46% ⇒ 40%. 91指定甲: 五題答對率 80,70,60,50,40% 每題20分 ⇒ 平均 60. 96學科: 15 評審平均76, 剔除 92,45,55 ⇒ $\frac{1140-192}{12}=79$.
- **加權平均** $\sum x_iw_i$ ($\sum w_i=1$): 成績比重 20/20/30/30% → 85.4; 學分加權 73.5.
- **幾何平均數** $\sqrt[n]{x_1\cdots x_n}$ (正數); **平均成長率** $\sqrt[n]{(1+y_1)\cdots(1+y_n)}-1$ (not the arithmetic mean): +20%, −20% ⇒ $\sqrt{0.96}-1=-2.02\%$; −10%,20%,60% ⇒ 20%; 2002學科 4→6 億 then equal rates to 48 億 ⇒ 100%; 營業額 242→306 四年 ⇒ ≈8.1% (3 intervals); 台灣經濟成長率 8年 ≈6.28% (99) / ≈1.63% (2012–2019, 108). AM ≥ GM; log of GM = mean of logs.
- 已分組 (資優): 組中點 × 次數; 中位數 by 內插 $Me=L_i+\frac{\frac n2-C_{i-1}}{f_i}h$ (e.g. 120人成績表 → 62); 簡化計算 $Y=\frac{X-A}h$.

### 9.3 百分位數 (108 definition)
- $P_k$: 至少 k% 的資料 ≤ $P_k$ 且至少 (100−k)% ≥ $P_k$. **Computation** (sorted $x_1\le\dots\le x_n$): $m=n\times\frac k{100}$; if m 為整數, $P_k=\frac{x_m+x_{m+1}}2$; else $P_k=x_{\lceil m\rceil}$ (= $x_{[m]+1}$). $Q_1=P_{25}$, $Me=P_{50}$, $Q_3=P_{75}$; 四分位距 IQR $=Q_3-Q_1$; 全距 = max − min.
- 例: 280人呼吸次數 → $Q_1=17$, $Q_3=19$, $P_{17}=17$, $P_{60}=18$; 250人投籃 → $Q_1=x_{63}=2$, $Q_3=x_{188}=5$, $P_{35}=3$, $P_{60}=3.5$; 80 球員打擊率 $P_{16}=x_{13}$, $P_{45}=\frac{x_{36}+x_{37}}2$; 2..100 偶數 $P_{20}=21$, $P_{63}=64$. 生長曲線 85 百分位. 學測五標: 頂標 $P_{88}$, 前標 $P_{75}$, 均標 $P_{50}$, 後標 $P_{25}$, 底標 $P_{12}$ ⇒ 數甲 IQR $49-20=29$.
- 多選 (108 習題): 百分位數不一定唯一 (definition allows a range; convention averages); 原資料×3 or +3 ⇒ percentile transforms the same way ✓; 兩組合併的 $P_{40}$ ≠ sum; $P_{40}$ 不必小於平均 (反例 1,2,…,2). **2005指考乙** 第一十分位數 same pattern → (2)(3).

### 9.4 離散程度：變異數、標準差
- 離差 $x_i-\mu$ (sum 0); 變異數 $\sigma^2=\frac1n\sum(x_i-\mu)^2=\frac1n\sum x_i^2-\mu^2$ (平方的平均 − 平均的平方); 標準差 $\sigma=\sqrt{\sigma^2}$ (same units). $f(t)=\frac1n\sum(x_i-t)^2$ minimized at $t=\mu$ with min $\sigma^2$.
- 例: 6,1,7,10 ⇒ μ=6, σ=$\frac{\sqrt{42}}2\approx3.24$; 9,12,8,5 ⇒ 2.5; $\sum x=155$, $\sum x^2=2551$ (n=10) ⇒ 15.5, σ≈3.9; 六科平均80, 五科68,80,80,80,86 ⇒ 第六科86, σ=6; 8,20,20,20,26,? 平均20 ⇒ 26, σ=6; 0/1 資料 (k 個1) ⇒ μ=p=$\frac kn$, σ=$\sqrt{p(1-p)}$ (1000人 400 支持 ⇒ 變異數 0.24); 1,2,…,n 的 σ=$\sqrt{\frac{n^2-1}{12}}$ (=√30 ⇒ n=19); 1700,…,2200 ⇒ $\frac{50\sqrt{105}}3$.
- **線性變換** $y_i=ax_i+b$: $\mu_y=a\mu_x+b$, $\sigma_y=|a|\sigma_x$ (平移不改變 σ、全距、IQR; 伸縮乘 |a|). 88學科 長度 2.43… ×100−240 ⇒ 新 μ=5, σ=2 ⇒ 原 μ=2.45, σ=0.02, 中位數 2.45 → (A)(B)(C)(E). 2010指考乙 售價 ×1.5: 平均75, σ=15. $3x-5$ 的 σ=9 (原σ=3); $3x^2+25$… 平均 $3(\sigma^2+\mu^2)+25=3\cdot25+25=100$. 調分 $y=ax+b$: 平均40→60, 最高72→96 ⇒ $a=\frac98$, $b=15$, σ: 12→13.5. 每人加5分: 平均/中位數變, σ、變異數、全距不變 ⇒ (C)(D)(E) (88自; the handout key lists only (C)(E), but variance is also unchanged); 兩次相差 8 分: 平均不等 (B 錯).
- **非線性調分** (2016學測): $40\log(1+\frac x{10})+60$ (x≤59): 9分→60 ✓; >20分→>70 ✓; 全距不一定變大; **遞增函數保序** ⇒ 中位數對應 ✓; 平均不保持 ✗ → (1)(2)(4). 開根號×10 (2005學測/108): 調整後平均65, σ15 ⇒ $\frac1{100}\sum x=\frac{\sum(10\sqrt x)^2}{100\cdot100}$: population → 44.5; sample (n−1) → 44.4775 ⇒ $44\le M<45$.
- 修正錯誤登記: 阿牛 40→0 (n=40, μ=51, σ=2) ⇒ new σ=√65≈8.06 (recompute $\sum x^2$); 甲 80 記50, 乙 70 記100 (mean unchanged, $\sum x^2$ decreases by $100^2+50^2-80^2-70^2=1200$) ⇒ $S-5\le S_1<S$ (89自 (B)); 小明 76 誤記 86 ⇒ 不變: 中位數74 (since both > 74), Q1 → (2)(5).
- 合併兩組標準差: use $\sum x^2=n(\sigma^2+\mu^2)$ per group. A 20人 75±5, B 30人 60±6 ⇒ μ=66, σ²=85.6 (σ≈9.25); 甲54人 62±6 & 乙46人 70±5 ⇒ 65.68, σ≈6.84; 城市30人 70±5 & 鄉鎮20人 60±10 ⇒ μ=66, σ≈8.9 → (A)(C).
- 判斷 σ 大小 by eye: 資料 A (1×5, 10×5) 最大 (89學科); 2005指定乙 直方圖 (mass at extremes) (4); 甲乙丙五科 (乙 = 甲 −10 ⇒ same σ; 丙 = 0.8 甲 ⇒ smaller) → $S_甲=S_乙>S_丙$; 2017指考乙 五科 平均≥80 且 σ≤5 → (2)(5); 2003指定甲 11 數據平均、中位數皆6 ⇒ $x+y=14$, $y<9$ → (1)(2); 2006指定乙 散布圖 X/Y 中位數/σ/全距比較 → (1)(2)(3) (Z 中位數 ≠ sum of medians); 十位身高 155…166 → 全距11, 中位數160, 平均160 → (1)(2)(4).
- 樣本 vs 母體 (資優/99): $s=\sqrt{\frac1{n-1}\sum(x_i-\bar x)^2}$; 民調 0/1 樣本標準差 $\sqrt{\frac n{n-1}p(1-p)}$. 平均絕對離差 $\frac1n\sum|x_i-\bar x|$ (algebraically awkward → variance).
- 加薪方案: 每人+5000 ⇒ 平均35000, σ4000; 每人+5% ⇒ 31500, σ4200.

### 9.5 標準化、z 分數、T 分數
- **標準化** $z_i=\frac{x_i-\mu}\sigma$ ⇒ mean 0, σ 1, 無單位 ($\sum z_i=0$, $\sum z_i^2=n$). Compare across subjects by z: 數學57 (μ43, σ7) z=2 vs 國文78 (μ73, σ5) z=1 ⇒ 數學較好; 小華 數學 z=0.5, 英文 z=0.8 ⇒ 英文較好. **T 分數** $=50+10z$ (mean 50, σ 10).
- 多選: z 是與**平均數**(not 中位數)的距離為標準差的幾倍; z 可為負; 用來比較不同單位; 標準化後 σ=1, 平均0 → (3)(4)(5).

### 9.6 二維數據：散布圖與相關係數
- 散布圖, 樣本點. 正相關 (左下→右上), 負相關 (左上→右下), 完全正/負相關 (all on a line with ±slope), 零相關 (無直線趨勢; horizontal/vertical lines also 「無關」), 曲線相關 (e.g. on a parabola, r may be 0). Scale of axes can fool the eye ⇒ need r.
- Using mean lines $x=\mu_x$, $y=\mu_y$: points in quadrants I/III contribute positive $(x_i-\mu_x)(y_i-\mu_y)$, II/IV negative ⇒ sign of $S_{xy}$.
- **定義** $r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}=\frac1n\sum x_i'y_i'$ (mean of products of z-scores) $=\frac{\sum x_iy_i-n\mu_x\mu_y}{n\sigma_x\sigma_y}$, $S_{xy}=\sum(x_i-\mu_x)(y_i-\mu_y)=\sum x_iy_i-n\mu_x\mu_y$.
- **性質**: $-1\le r\le1$ (proof: $\sum(x_i'\pm y_i')^2=2n\pm2nr\ge0$; or 柯西 ※/向量夾角 $r=\cos\theta$ of centered vectors); $|r|=1$ ⇔ 共線; **單位變換**: $x^*=a+bx$, $y^*=c+dy$ ⇒ $r^*=r$ if $bd>0$, $-r$ if $bd<0$; 受極端值影響大; **相關 ≠ 因果** (電視機數 vs 壽命).
- 例: 單價 vs 需求 (8,11),(9,12),(10,10),(11,8),(12,9) ⇒ $r=-0.8$ (84學科 (E)); $(1,1),(1,2),(4,1),(4,2)$ ⇒ 0; 數學/物理 8人 ⇒ 0.82; 缺課數 vs 成績 ⇒ −0.8 / −0.93; **2010指定乙** $\sum x=135$, $\sum x^2=3661$, $\sum xy=2842$, $\sum y=105$, $\sum y^2=2209$ (n=5) ⇒ $r=\frac{2842-5\cdot27\cdot21}{\sqrt{(3661-3645)(2209-2205)}}=\frac{7}{8}=0.875$; 年齡/血壓 ⇒ 0.4; 100 筆 ⇒ 0.55.
- 多選: $r_{x,y}$, $s=ax+b$, $t=cy+d$ ($ac<0$) ⇒ $r_{s,t}=-r_{x,y}$; 90學科 $W=7(24-X)$ ⇒ $R_{WY}=-R_{XY}$ (E); $X'=-4X+5$, $Y'=6Y-4$ ⇒ $r'=-0.123$; 89學科 remove D(3,10) maximizes r; 2007指定甲 $r=0.016$: 散布圖可表示 ✓, 不適合用直線描述 ✗, $X+5,Y+5$ / $10X,10Y$ / z-scores 都不變 ✓ → (1)(3)(4)(5); 90自 X=R−W/4, Y=R+N/5 (both linear in a common quantity) → r=1, same ranking → (A)(B)(D)(E); 散布圖排序 by |r| & sign; 2015學測 路跑 → (2)(4)(5); 2002指定甲 風速vs氧化物 → (C)(D).

### 9.7 最適直線（迴歸直線）
- **最小平方法**: minimize $E=\sum[y_i-(a+bx_i)]^2$ (vertical deviations). Toy: points $(-1,1),(0,3),(1,-4)$ ⇒ $E=2(m+\frac52)^2+3k^2+\frac{27}2$ ⇒ $y=-\frac52x$.
- Standardized data: best line $y'=rx'$ (through origin — the 108 teaching route: mean-0 data). Original: $y-\mu_y=r\frac{\sigma_y}{\sigma_x}(x-\mu_x)$; slope $b=r\frac{\sigma_y}{\sigma_x}=\frac{S_{xy}}{S_{xx}}$; **passes through $(\mu_x,\mu_y)$**. Minimum mean squared error (standardized) $=1-r^2$ ⇒ larger |r| ⇒ better linear fit. Note **y 對 x** ≠ x 對 y (different lines unless |r|=1).
- 例: $\mu_x=65,\mu_y=70,\sigma_x=10,\sigma_y=5,r=0.8$ ⇒ $y=0.4x+44$ (65 → 70); 年齡/血壓 ⇒ $y=0.6x+103$ (50歲→133); 缺課 ⇒ $y=-8x+104$ (10堂→24分); $y=75-7.86(x-3)$ (7堂→43.56); 氣溫/銷售 ⇒ $y=\frac45x-13$ (35°C → 15 千元); 中古車 $r=-0.9$, $y=-0.45x+6.8$ (price in 十萬元; 8 年 → 32 萬); 100筆 ⇒ $y=0.33x+38.76$.
- 反推: 迴歸直線過 $(\mu_x,\mu_y)=(10,6)$ 及 $(0,2)$ ⇒ slope 0.4 $=0.8\frac{\sigma_y}4$ ⇒ $\sigma_y=2$; $\mu=(5,3)$, $r=1$, 過 $(0,2)$ ⇒ $y=0.2x+2$; 20筆 $\mu=(3,4)$, $r=0.8$, 過 $(2,0)$ ⇒ slope 4 ⇒ 過 (3,4),(7,20), $\sigma_x<\sigma_y$ → (1)(2)(4)(5); $X'=-2X+1$, $Y'=Y-3$ ($\mu_X=3,\sigma_X=1,\mu_Y=4,\sigma_Y=5,r=0.4$) ⇒ $r'=-0.4$, $Y'$ 對 $X'$: $y=-x-4$.
- **2013學測**: five data sets with the same regression line, all negative ⇒ smallest r (most negative, i.e. tightest) is (5). **2009指定乙**: which two scatter plots share a regression line → (4) B、C. **2009指定乙** 「就學年數每增加一年年薪平均增加8萬5」 comes from the **迴歸直線斜率** (5). **2019學測** coffee vs temperature ($r=-0.99$): use line through (11,512),(13,437), slope $-\frac{75}2$ ⇒ 8°C ≈ 625 杯 (2).
- **對數變換線性化**: power law $d=kt^n$ ⇒ $\log d=\log k+n\log t$ (straight line). **2008指定甲** $x=\log_2t$, $y=\log_2d$: $d=14.88$ ⇒ $3<\log_2d<4$ ✓; $r$ near 1 (not <0.2); read $a>2$ ✓ → (1)(4). Kepler: $\log(\text{距離})$ vs $\log(\text{週期})$ slope ≈ 0.666 ⇒ $y\propto x^{2/3}$ (r=0.99998); 步行速率 vs 人口 $P=CV^\alpha$; 除草劑 linear model breaks for large x (negative weeds) — 模型適用範圍.
- Excel: `AVERAGE`, `STDEV.P` (population), `CORREL`, `LINEST` / 趨勢線. Results may be approximations.
- 機率連結 (99): 9 分數 30..90, 抽3人 中位數 = 母體中位數60 的機率 $\frac{23}{42}$; 平均數 = 60 的機率 $\frac17$.

## 10. 集合、邏輯、計數原理、排列組合、二項式定理

**Scope**: D-10-1 集合 (表示法、宇集、空集、子集、交集、聯集、餘集、屬於與包含、文氏圖) **★＃**; N-10-7 邏輯 (命題及其否定、或/且/推論、充分/必要/充要條件) **★＃**; D-10-3 有系統的計數 (窮舉、樹狀圖、加法原理、乘法原理、**取捨原理**、直線排列與組合; 二項式展開 as an application of 組合). Per scope.md the 排列組合 here **serve 古典機率**. 108 handouts still contain 重複組合-type problems ($x+y+z=n$, $x\le y\le z$), but they solve them by 轉換成組合 (插板法) without the $H^n_k$ symbol. **[超出數A]** or 99/資優 extras: the $H^n_k$ notation, **環狀排列**/項鍊, 立體塗色 (rotations), 多項式定理 as a named theorem, and 錯排 formulas beyond small cases (do them by 取捨原理). **Sources**: 108一下 3-1計數原理, 3-2排列, 3-3組合與二項式定理; 99第二冊 2-1集合邏輯與計數原理, 2-2排列與組合, 2-3二項式定理; 資優 第8單元集合與函數, 第39單元計數方法, 第40單元排列, 第42單元二項式定理.

### 10.1 集合 (D-10-1)
- 集合 = 明確可鑑別的對象所成整體; 元素. 有限/無限集合. **列舉法** {甲,乙,…} vs **描述法** $\{x\mid \text{性質}\}$ (e.g. $\{2n\mid n\in\mathbb Z\}$, 被7除餘2的自然數 $\{7k+2\mid k\ge0\}$). $\mathbb N,\mathbb Z,\mathbb Q,\mathbb R$. $\{x\in\mathbb R\mid x^2-4x+3=0\}=\{1,3\}$.
- 元素特性: **無序性、互異性、明確性** ⇒ $\{3,5,5,1,1\}=\{3,3,5,1\}=\{1,3,5\}$.
- $\in/\notin$ link an **元素** to a set; $\subset/\supset$ link a **set** to a set. 相等: $A\subset B$ 且 $B\subset A$. **空集合** $\varnothing$ is a subset of every set. 區間 $[a,b],(a,b),(a,b],[a,b)$ are already sets (no extra {}).
- Trap problems: $S=\{\varnothing,1,\{1,3\},2\}$ ⇒ $\varnothing\in S$ ✓, $\varnothing\subset S$ ✓, $\{1,3\}\in S$ ✓, $\{1,2\}\subset S$ ✓ (A)(B)(D)(E). $S=\{\varnothing,1,\{1,2\},3\}$ ⇒ (A)(B)(D) ($2\notin S$; $\{1,2,3\}\not\subset S$). $A=\{1,\{1\},\{2\},\{1,2\}\}$ ⇒ $\{1\}\in A$, $\{1\}\subset A$, $\{1,2\}\in A$ ✓; $2\in A$ ✗, $\{1,2\}\subset A$ ✗.
- **子集合個數**: $n$ elements ⇒ $2^n$ subsets ($A=\{1,2,3\}$: 8). $\{x\in\mathbb Z\mid |x-1|\le2\}$: 5 elements, 32 subsets. 3-element subsets of a 5-set: $C^5_3=10$.
- 運算: $A\cap B$ (且), $A\cup B$ (或), $A-B=\{x\in A, x\notin B\}=A\cap B'$, 餘集 $A'=U-A$. Laws: 交換、結合、**分配律** $(A\cup B)\cap C=(A\cap C)\cup(B\cap C)$, $(A\cap B)\cup C=(A\cup C)\cap(B\cup C)$; $A\subset B\Rightarrow A\cup B=B,\ A\cap B=A$; $A\subset B\iff A'\supset B'$; **笛摩根** $(A\cup B)'=A'\cap B'$, $(A\cap B)'=A'\cup B'$ (prove with 文氏圖).
- 例 (solve, then **check membership**, since a value can make elements repeat or miss):
  - $A=\{2,4,a+1\}$, $B=\{-4,a-2,a^2-2a-3\}$, $A\cap B=\{2,5\}$ ⇒ $a=4$.
  - $A=\{-2,a-2,3\}$, $B=\{1,a^2-a-3,-5\}$, $A\cap B=\{3\}$ ⇒ $a=-2$ ($a=3$ makes $a-2=1\in A\cap B$, rejected).
  - $P=\{2,4,a^2-2a-3\}$, $T=\{-4,a^2+2a+2,a^2-3,2a^2-3a-9\}$, $P\cap T=\{2,5\}$ ⇒ $a=-2$, $T=\{-4,1,2,5\}$.
- 例:
  - $A=\{x\in\mathbb Z\mid |x+2|<3\}$, $B=\{x\in\mathbb Z\mid x^2\ge4\}$ ⇒ $A-B=\{-1,0\}$.
  - $U=\{1..8\}$, $A=\{2,3,4,7\}$, $B'=\{3,6,8\}$ ⇒ $A'=\{1,5,6,8\}$, $B=\{1,2,4,5,7\}$, $A\cup B=\{1,2,3,4,5,7\}$, $A\cap B=\{2,4,7\}$, $A-B=\{3\}$.
  - Point sets: $\{x+2y=2\}\cap\{x-4y=6\}=\{(\frac{10}3,-\frac23)\}$.
  - Equation solution sets: $f(x)g(x)=0$ ⇒ $A\cup B$; $\frac{g(x)}{h(x)}=0$ ⇒ $B-C$; $f=0$ and $gh=0$ ⇒ $A\cap(B\cup C)$.
  - Intervals: $A=\{x>3\text{ 或 }x<-1\}$, $B=\{|x-a|\le b\}$ with $A\cup B=\mathbb R$ and $A\cap B=(3,4]$ ⇒ $B=[-1,4]$, so $a=\frac32$, $b=\frac52$.
  - $A=\{x,y,z\}=B=\{x+1,2,3\}$ ⇒ 5 ordered triples.
  - $C=\{a+b\}$ with $a\in\{0,2,4,6,8\}$, $b\in\{1,3,5\}$ ⇒ $n(C)=7$.

### 10.2 邏輯 (N-10-7, ★＃)
- 命題 = statement that is either true or false. 否定 ～p. 「p 且 q」 is true only when both are true; 「p 或 q」 is false only when both are false. **De Morgan for propositions**: ～(p 且 q) ≡ ～p 或 ～q; ～(p 或 q) ≡ ～p 且 ～q. Negating a quantifier: ～(所有 x 皆 P) ≡ 存在 x 使 ～P.
- 「若 p 則 q」 (p ⇒ q) corresponds to set inclusion $P\subset Q$. Its **逆否命題** 「若～q 則～p」 is equivalent to it; its 逆命題 is not.
- **充分/必要**: if p ⇒ q, then p is a 充分條件 of q and q is a 必要條件 of p. 充要 means p ⇔ q (P=Q). Quadrilateral drills (four statements, key 充要/充分/充分/必要) follow this pattern: 「對角線互相平分」 ⇔ 平行四邊形 (充要); 「是正方形」 ⇒ 「對角線等長」 (充分 only); 「是平行四邊形」 is 必要 for 「是矩形」. Decide with the set picture: smaller set ⇒ larger set.
- 學測 examples: **2013學測 模範生** (「是模範生 ⇒ …」 statements; pick the logically equivalent / implied statement) → (5). **2015指定乙 計程車** → (2)(5). The 108/99 drills also classify sentences as A 充分非必要 / B 必要非充分 / C 充要 / D 都不是 (99 drill key: A A A B A B C D).

### 10.3 函數的集合觀點 (資優8; links to §7.5)
- $f:A\to B$: every $a\in A$ corresponds to **exactly one** $b\in B$. 定義域 $A$, 對應域 $B$, 值域 $f(A)\subset B$. 1對1 and 多對1 are functions; 1對多 is not; the domain must be fully mapped. **鉛直線檢驗**: a graph is a function graph iff every vertical line meets it at most once.
- **映成** $f(A)=B$; **1−1** $x_1\ne x_2\Rightarrow f(x_1)\ne f(x_2)$; **合成** $g\circ f(x)=g(f(x))$; **偶函數** $f(-x)=f(x)$ (graph symmetric about the y-axis); **奇函數** $f(-x)=-f(x)$ (symmetric about the origin). Every $f$ = even part $\frac{f(x)+f(-x)}2$ + odd part $\frac{f(x)-f(-x)}2$.
- 例:
  - Domains: $\frac{2x+1}{x-1}$ → $x\ne1$; $\sqrt{x+1}$ → $x\ge-1$.
  - Ranges: $3x^2+4x+7$ → $y\ge\frac{17}3$; $\frac{x+5}{2x-3}$ → $y\ne\frac12$; $\frac{2x+3}{x-5}$ → $y\ne2$; $\sqrt{-x^2+6x+16}$: domain $[-2,8]$, range $[0,5]$.
  - $g(3x+2)=f(2x+1)$ with $f=3x-6$ ⇒ $g(x)=2x-7$.
  - $f(x)=2x^2+3$, $g=3y-4$ ⇒ $f(g(y))=18y^2-48y+35$.
  - $f(n)$ = the $n$th decimal digit of $\frac27=0.\overline{285714}$ ⇒ $f(2002)=7$, range $\{2,8,5,7,1,4\}$.
  - $f$ with period 5 and odd, $f(\frac13)=1$ ⇒ $f(\frac{16}3)=1$, $f(\frac{29}3)=-1$, $f(11)+f(-6)=0$.
  - 高斯符號 $[x]$ (greatest integer ≤ x; the handout's $[-5]=5$ is a typo for $-5$; $[-3.2]=-4$).
  - Temperature: $y=20-6x$ ($0\le x\le11$), $y=-46$ ($x\ge11$); at 5.5 km ⇒ −13°C.

### 10.4 計數原理 (D-10-3)
- **加法原理**: split into 互斥 cases and add. **乘法原理**: split into 步驟 and multiply. **樹狀圖** / 有系統的窮舉 for small or irregular cases. 「至少一個」 ⇒ use the complement (反面).
- 例 (digits & divisors):
  - Integers 1–1000 with no digit 3: $8+8\cdot9+8\cdot9^2+1=729$, so 271 contain a 3 (same 271 for the digit 7).
  - $|$百位−個位$|=2$ three-digit numbers: 150 (1996學科).
  - 0s written from 1 to 999: 189.
  - Typesetting 1..1000: 2893 pieces of type.
  - 1..10000: the digit 3 is written 4000 times.
  - Four-digit numbers from 1–7 (repetition allowed) with an odd number of 5s: $4\cdot6^3+4\cdot6=888$.
- **正因數個數**: $N=p_1^{a_1}\cdots p_k^{a_k}$ ⇒ $\prod(a_i+1)$.
  - 720 = $2^4 3^2 5$ → 30.
  - 2520 = $2^3 3^2 5\cdot7$ → 48 divisors, 12 odd, 4 perfect squares.
  - 7200 = $2^5 3^2 5^2$ (54 divisors): 6的倍數 30; 2的倍數非3的倍數 15; 完全平方數 12.
  - **lcm(A,B)=245000** = $2^35^47^2$ ⇒ for each prime $p^e$ the exponent pairs number $2e+1$ ⇒ $7\cdot9\cdot5=315$ ordered pairs.
  - Rational-root candidates of $360x^5+\dots-361$: 144.
- **一一對應**: a single-elimination tournament with $n$ teams has $n-1$ matches (8 teams → 7). Double elimination → at most $2(n-1)+1=15$.
- **整數分拆** (order ignored): 15 as a sum of 3 positive integers → 19 ways; 10 → 8 ways.
- **格子點**: $|x|+|y|\le3$ → 25 lattice points; $3x+5y\le10$ with $x,y\ge0$ → 7. Points on $(x-7)^2+(y-8)^2=9$ at integer distance from O: $\sqrt{113}\pm3$ ⇒ distances 8..13, 2 points each ⇒ 12 (2004學科).
- **三角形**: integer sides with largest side 11 → $1+3+5+\dots+11=36$.
- **塗色** (adjacent regions get different colors): color in an order that maximizes constraints, and **split on whether non-adjacent regions share a color**. 5 colors / 4 regions → 260; 4 colors → 96, 2304 (figure-dependent); 5 colors / 5 regions (A,B,C,D,E pattern) → $5\cdot4\cdot3^2$ (B,D same) $+5\cdot4\cdot3\cdot2\cdot2$ (B,D different) $=180+240=420$; 86社 → 960.
- **取捨原理 (排容)**:
  - Two sets: $n(A\cup B)=n(A)+n(B)-n(A\cap B)$.
  - Three sets: $n(A\cup B\cup C)=\sum n(A)-\sum n(A\cap B)+n(A\cap B\cap C)$.
  - n sets: alternating signs over all intersections.
  - 例: multiples of 2 or 3 in 1–20 → 13; multiples of 2, 3 or 5 in 1–500 → 366 (134 are not); multiples of 3 or 5 in 1–1000 → 467, so 533 are coprime to 15.
  - 例: failing 國英數 with 8/15/20 failures, pairs 3/4/6, all three 2 ⇒ 32 failed at least one.
  - 例: newspapers 25/32/33 of 60 households, all three 7 ⇒ exactly two 16, exactly one 37.
  - 例: strings over a,b,c,d of length n containing each of a,b,c ⇒ $4^n-3\cdot3^n+3\cdot2^n-1$.
  - Euler $\varphi(n)=n\prod(1-\frac1{p_i})$ (資優 進階).
- 學測/指考: **2015學測 手機/平板** → (2)(3)(4); **2017學測 國英數** → (2)(5); **2019指定乙 公仔** → (2)(5); **2007學科 阿民公仔** (4 帽 × 3 衣 × 3 鞋; 紅帽不配灰鞋; 白衣必配藍帽) → 25; **2015指定乙** (m/n) → 17; **2014學測 瓷磚** → 11.
  - **車牌** AxxxxA4 (no three consecutive 4s; first letter A, last digit 4) → $25\times990$ (4).
  - 十字路口 (no U-turns; 東西 cannot turn left) → 10 flows. 5 doors, 甲乙 enter by different doors and exit by different doors → 400; also using a different door from one's own entry → 260; three people doing the same → 1920.

### 10.5 排列 (直線排列)
- $P^n_k=n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}$, $0!=1$, $P^n_n=n!$. Identity $P^n_r=P^{n-1}_r+rP^{n-1}_{r-1}$ (split on whether 甲 is chosen).
- Equations: $2P^n_3=3P^{n+1}_2+6P^n_1$ ⇒ $n=5$; $5P^9_n=6P^{10}_{n-1}$ ⇒ $n=7$; $P^{n+1}_3=10P^{n-1}_2$ ⇒ $n=4$ or 5; $2P^8_{n-2}=P^8_n$ ⇒ $n=8$.
- **不盡相異物排列**: $\frac{n!}{m_1!m_2!\cdots m_k!}$.
  - AAAB → 4; 3紅2黃4黑 → $\frac{9!}{3!2!4!}$.
  - pallmall → 840.
  - 0,0,1,1,2,2 as six-digit numbers → 60.
  - 4,5,5,5,8,8,8 even seven-digit numbers → 80.
  - aabbbcde → 3360.
  - 12 numbered cells colored 3 yellow, 4 red, 2 green, 3 blank → $\frac{12!}{3!4!2!3!}=277200$ (排列 ↔ 塗色 一一對應).
  - Shooting beads off strings of 2/3/4 → $\frac{9!}{2!3!4!}=1260$.
- **重複排列** $m^n$ (each of $n$ objects independently picks one of $m$ options; **identify who chooses**):
  - 10 voters, 3 candidates → $3^{10}$.
  - A multi-select item with 5 options → $2^5-1$.
  - 10 students compete for 3 titles → $10^3$.
  - 5 people leaving a crossroads (not all on the same road) → $4^5-4$.
  - Three distinct dice → 216.
- **限制條件**:
  - (a) 相鄰 ⇒ bundle them (綁), then arrange inside.
  - (b) 不相鄰 ⇒ arrange the others first, then **插空隙**.
  - (c) 男女相間 ⇒ arrange one sex, then insert the other.
  - (d) 反面計算.
  - (e) 取捨原理.
  - 7 people:
    - 甲乙丙 相鄰: $3!5!=720$.
    - 甲乙丙 分開: $4!P^5_3=1440$.
    - 甲乙相鄰 and 丙丁不相鄰: $4!\cdot2!\cdot P^5_2=960$.
    - 甲乙相鄰 and 甲丙不相鄰: $2\cdot6!-2\cdot5!=1200$.
  - 4女3男:
    - Each sex together: 288.
    - Alternating: 144.
    - 3 boys separated: 1440.
  - 6 people:
    - 乙丙 both adjacent to 甲: 48.
    - 甲乙相鄰, 甲丙不相鄰: 192.
    - Exactly two of 甲乙丙 adjacent: 432.
  - Couple fixed in the middle two of 6 seats: 48.
  - 甲乙丙 sit in 3 adjacent seats of a row of 8: 36.
  - 3 of 8 seats, not all three adjacent: $P^8_3-6\cdot3!=300$.
  - Batting order with fixed 3rd/4th and the pitcher and catcher in 7–9: 720.
  - 10 players, 3 aces in matches 1/3/5, others choose: $3!\cdot P^7_2=252$.
- **反面/排容**:
  - 課表: 7 subjects, 體育 not 4th, 數學 not 7th → $7!-2\cdot6!+5!=3720$.
  - 10 people, A,B not first and C,D not last → $10!-4\cdot9!+4\cdot8!=58\cdot8!$.
  - 7 people, A,B,C each not adjacent to D → 1440.
  - Permutations of 1–6 with $(x_1-1)(x_2-2)(x_3-3)=0$ → $3\cdot5!-3\cdot4!+3!=294$; with $\prod_{i\le4}(x_i-i)\ne0$ → 362.
  - 1–5 with $(2-a_4)(1-a_3)=0$ → 42; $(1-a_1)(3-a_3)\ne0$ → 78.
- **錯排** $D_n$: $D_n=n!\sum_{k=0}^n\frac{(-1)^k}{k!}$, recurrence $D_n=(n-1)(D_{n-1}+D_{n-2})$; $D_3=2$, $D_4=9$, $D_5=44$, $D_6=265$.
  - 5 couples dancing with nobody paired to their own spouse → 44.
  - 6 balls into 6 holes with exactly one match → $6\cdot D_5=264$.
- **同字不相鄰** (排容):
  - LKKLMM → $90-3\cdot30+3\cdot12-6=30$.
  - cabbage → $1260-2\cdot360+120=660$; 「一寸光陰一寸金」 → 660 (same structure).
  - pontoon: all 420; ooo together 60; o's all separate $\frac{4!}{2!}C^5_3=120$; exactly two o's together 240.
  - pallmall: all l together and the a's apart → 36; three l together and the fourth l apart → 240.
  - 「庭院深深深幾許」: all 840; 深 not all together 720; all separate 240; at least two adjacent 600; exactly two adjacent 480.
  - a,a,a,b,b,c,d,e,f with no equal letters adjacent: insert the a's after placing the rest (split on bb adjacent or not) → 10200.
- **定序排列** (fixed relative order ⇒ divide by $k!$ or treat as identical):
  - A,B,C,D,E,F,G with A,B,C in fixed order → $\frac{7!}{3!}=840$.
  - A before both B and C → $\frac{7!}{3}=1680$.
  - A before B and F after G → $\frac{7!}{4}=1260$.
  - A,B before C,D,E → $7!\cdot\frac{2!3!}{5!}=504$.
  - 甲 left of both 乙 and 丙 → 1680.
  - factoring with vowels in order a,o,i → $\frac{9!}{3!}$; vowels and consonants both in order → $\frac{9!}{3!6!}$.
  - attribute: consonants in odd positions → 480; vowels in order → 2520; consonants in order → 3024; both → 126.
  - 甲乙丙 in order among 5 → 20; 甲 between 丙 and 丁 → 40.
- **數字排列** (no leading 0; parity from the last digit; 4的倍數 from the last two digits; 3/9 from the digit sum; 5 from the last digit 0/5).
  - 0–5, distinct digits, four-digit numbers: total 300, even 156, multiples of 3 → 96, of 4 → 72, of 5 → 108; sum of all = 979920; >2100 → 228 (with repetition 827).
  - 0–4, distinct three-digit numbers: sum 12990.
  - 2–6 three-digit numbers: 125 with repetition; sum of the distinct-digit ones 26640.
  - Two-digit numbers with units > tens → 36; tens > units → 45.
  - 0–5 distinct three-digit → 100, of which 40 are divisible by 3.
  - 1–8, five distinct digits with positions 1,3,5 odd → 480.
- **遞迴計數**:
  - 8 stairs taking 1/2/3 steps → $a_n=a_{n-1}+a_{n-2}+a_{n-3}$ → 81.
  - A piece moving 1–3 squares to cover 7 → 44.
  - **鳴放氣笛**: 長鳴4秒, 短鳴1秒, 間隔1秒, the signal **fills exactly 30 s** ⇒ $5x+2y=31$ ⇒ $C^{14}_1+C^{11}_3+C^8_5=14+165+56=235$; (15/10/5 s, 75 s) ⇒ $4x+3y=16$ ⇒ 6.
- **分配 (distinct objects to people)**:
  - 5 letters into 4 mailboxes with 甲乙丙 each non-empty → $4^5-3\cdot3^5+3\cdot2^5-1=390$.
  - 7 books to 4 people: 甲 gets at least one $4^7-3^7$; exactly one $7\cdot3^6$; everyone gets one → $4^7-4\cdot3^7+6\cdot2^7-4=8400$.
  - 5 toys to 3 people, each at least one → 150; 2,2,1 to 甲乙丙 → 30.
  - **渡船** (3 boats, ≤6 each): 8 people → $3^8-3(C^8_7\cdot2+1)=6510$; 7 people with 甲 in A → $3^6-1=728$.
  - 7 books to 10 people, at most one each: identical $C^{10}_7=120$; distinct $P^{10}_7=604800$.
- **捷徑 (走捷徑 = shortest grid path)**: $\frac{(m+n)!}{m!n!}$; through P: multiply segments; avoiding points/regions: complement plus 取捨.
  - 210/100/80; 50/8/23; 8×6 streets 792 / through P 350 / through P and Q 180 / avoiding both 286; avoiding a shaded region 108.
  - $A(-3,-2)\to B(3,4)$: 924; through O 350; avoiding the 2nd quadrant 462; avoiding (1,1) and (−2,3) 538.
  - With moves →↑↓ allowed (資優 figure): 240 total, 105 avoiding P, 135 through P, 30 avoiding P and Q, 93 through both.
  - Diagonal moves allowed on a 3×5 board: exactly two diagonals $\frac{6!}{3!2!1!}=60$; total $56+105+60+10=231$.
  - **唱票** (A always ahead, wins 6:5) → lattice paths from (1,0) to (6,5) staying below the diagonal → 42 (Catalan).
- **[超出數A] 環狀排列 / 立體塗色** (99/資優 only):
  - $n$ distinct objects in a circle → $\frac{P^n_m}{m}$ (choosing $m$); necklace (can flip) → ÷2 again.
  - 5 couples around a table: any $9!$; alternating $4!5!$; couples adjacent $4!2^5$; both $4!\cdot2$; men opposite women $4!\cdot2^4\cdot5!$; couples opposite $4!\cdot2^4$.
  - Family of 4 adjacent at a 12-seat table with the children between the parents → 161280 (83自).
  - 8 people with 甲乙 adjacent and 丙丁 opposite → 192.
  - 6 men and 4 women in a circle with no two women adjacent → $5!P^6_4=43200$.
  - Cube with 6 colors → 30; formula $\frac{P^n_y}{x\cdot y}$ for a regular solid with $y$ faces, each a regular $x$-gon.

### 10.6 組合
- $C^n_k=\frac{P^n_k}{k!}=\frac{n!}{k!(n-k)!}$ (also $C^n_k$ = arrangements of $k$ 白球 and $n-k$ 黑球). Identities: $C^n_k=C^n_{n-k}$; **巴斯卡** $C^n_k=C^{n-1}_k+C^{n-1}_{k-1}$; **曲棍球棒** $C^k_k+C^{k+1}_k+\dots+C^n_k=C^{n+1}_{k+1}$ ($\sum_{k=2}^{19}C^k_2=C^{20}_3=1140$; $C^3_3+\dots+C^9_3=C^{10}_4=210$; $C^2_0+C^3_1+\dots+C^{10}_8=C^{11}_8=165$).
- **不相鄰選取**: choose $k$ of $1..n$ with no two consecutive → $C^{n-k+1}_k$ (4 of 1–20 → $C^{17}_4=2380$). 例: choose 4 of 10 train cars ⇒ $C^{10}_4=210$, with no two adjacent ⇒ $C^7_4=35$. Three of 1–20: an arithmetic progression ⇒ $2C^{10}_2=90$ (first and last of the same parity); no two consecutive ⇒ $C^{18}_3=816$; product even ⇒ $C^{20}_3-C^{10}_3=1020$.
- **幾何計數**:
  - 12-point grid: 35 lines, 200 triangles.
  - 15 points with 7 collinear: 85 lines, 105, 420.
  - 11 points forming 48 lines ⇒ 2 lines carry multiple collinear points; 160 triangles.
  - Regular 12-gon triangles: right 60, acute 40, obtuse 120.
  - Polygons with $n$ sides where diagonals equal $k$ sides: 9 and 7.
  - Strips of 4 cm and 3 cm: 28.
- **撲克**: 同花 (flush incl. straight flush) $4C^{13}_5=5148$; full house $13\cdot C^4_3\cdot12\cdot C^4_2=3744$.
- **分組分堆** (KEY RULE: **groups of equal size with no labels ⇒ divide by $k!$**; labelled recipients ⇒ multiply by the arrangement):
  - 9 books into 3,3,3: to 3 people $\frac{9!}{3!3!3!}=1680$; as unlabeled piles 280. Split 2,2,5 unlabeled → $\frac{9!}{2!2!5!\cdot2!}=378$.
  - 9 people into three groups of 3 → 280; 甲乙丙 all in different groups → 90; 甲乙 in the same group → 70; **90學科 鬥牛** (甲乙 not on the same team) → $280-70=210$.
  - 10 students in rooms A(4),B(3),C(3) → $C^{10}_4C^6_3=4200$; 甲乙 in the same room → 1120.
  - 8 books split 3,3,2 among 甲乙丙 → 1680.
  - **HBL** 8-team bracket → 315.
  - 8 balls into two groups of 4 → 35; given to 小安/小明 → 70.
  - 12 people into 4 groups of 3 → $\frac{12!}{3!^4\,4!}=15400$.
  - 8 students to 4 classes, 2 each → 2520; unequal patterns 1680, 20160.
  - **83自**: 12 identical pencils to 6 kids, two get 4, two get 2, two get 0 → $\frac{6!}{2!2!2!}=90$.
  - 12 people around triangle/square/rectangle tables (環狀, [超出]).
- **球入箱 (7 balls, 3 boxes, empty allowed)**:

  | | boxes distinct | boxes identical |
  |---|---|---|
  | balls distinct | $3^7=2187$ | 365 |
  | balls identical | $C^9_2=36$ | 8 |

- **函數計數**: $|A|=4,|B|=3$: all functions $3^4=81$; 映成 $81-3\cdot16+3=36$. 1−1 from a 3-set to a 7-set → $P^7_3=210$; 映成 from a 9-set onto a 2-set → $2^9-2=510$. Nondecreasing $f(1)\le\dots\le f(4)$ into a 6-set → $C^9_4=126$; strictly increasing → $C^6_4=15$.
- **Triples from 1–9**: distinct ordered $P^9_3=504$; any $9^3=729$; $x<y<z$ $C^9_3=84$; $x\le y\le z$ $C^{11}_3=165$. Three-digit $\overline{abc}$: $a>b>c$ → $C^{10}_3=120$; $a<b<c$ → $C^9_3=84$; $a\ge b\ge c$ → $C^{12}_3-1=219$; $a\le b\le c$ → $C^{11}_3=165$.
- **取相同物** (classify by 同/異 pattern):
  - Balls 5紅4白3黃2藍, choose 4 → 30.
  - Bag 5R 4W 2B 2Y 1G: choose 4 → 45; choose 4 and arrange → 478; choose at least one → $6\cdot5\cdot3\cdot3\cdot2-1=539$ (key prints 53, a misprint).
  - aaabbc choose 3 → 19 multisets. ATTENTION choose 5 → 41 multisets, 2250 arrangements. mathematical choose 4 → 143 / 2482. attention choose 4 → 41 / 626.
- **重複組合 / 插板法** (108 handouts: conversion; 99: $H^n_k=C^{n+k-1}_k$):
  - Nonnegative solutions of $x_1+\dots+x_n=k$ → $C^{n+k-1}_k$; positive solutions → $C^{k-1}_{n-1}$.
  - $x+y+z+u=100$: nonnegative $C^{103}_3$; positive $C^{99}_3$.
  - Terms in $(x+y+z)^8$ → $C^{10}_2=45$.
  - $x+y+z\le8$ (add a slack variable) → $C^{11}_3=165$.
  - Four dice: $6^4$ ordered outcomes vs $C^9_4=126$ unordered.
  - $x+y+z+u=12$: nonnegative 455, positive 165. Sums ≤9 with positive parts → 126.
  - 10 identical apples to 甲乙丙: each ≥1 → 36; ≥1/≥2/≥3 → 33.
  - Fruit to 甲乙丙: 150 / 3 / 93.
  - **2013學測 雞蛋** → (5) 253; **2015學測 盆栽** → 70.
- 學測/指考:
  - 2010學科 (sums equal 11) → (2); 2006學科 鞋 → 21; 2010學科 表格 → 432.
  - 90大學社 值日生 → 43200; 2002指定乙 停水 → 15; 2013指定乙 → 120.
  - 2006學測 頻道 (2 sports first, then the 3-news and 4-variety blocks) → $2!\cdot2\cdot3!\cdot4!=576$.
  - 轉彎恰4次 → 198; sign changes in +/− strings → 70; 連串 → 6; heights → 128.
  - 3 colors on 5 distinct boards, all colors used → $3^5-3\cdot2^5+3=150$.
  - Transfer students into 4 classes (≤3 each) → 960; 甲乙 not in the same class → 768.

### 10.7 二項式定理
- $(a+b)^n=\sum_{k=0}^nC^n_ka^{n-k}b^k$. **一般項** $C^n_ka^{n-k}b^k$ = choosing $b$ from $k$ of the $n$ factors (also $\frac{n!}{(n-k)!k!}$ as a 不盡相異物 arrangement). In descending powers of $a$, the $(k+1)$th term is $C^n_ka^{n-k}b^k$. There are $n+1$ terms. Proof by 巴斯卡 + 數學歸納法.
- **指定項係數** (write the general term, solve for $k$, keep the **sign and the constant powers**):
  - $(2x-y^2)^6$, $x^4y^4$ → 240.
  - $(x-\frac1{3x^2})^{18}$: $x^6$ → $\frac{340}9$; constant term → $\frac{6188}{243}$; $x^4$ → 0 (no such term).
  - $(2x-3y)^8$, $x^3y^5$ → −108864.
  - $(2x^2-\frac1x)^8$, $x^7$ → −1792.
  - $(x-1)(x^2-2y)^{10}$, $x^{15}y^3$ → −960.
  - $(9x+\frac1{3\sqrt x})^{12}$, constant term → 495.
  - $(x^2+1)(x-2)^7$, $x^3$ → 1008.
  - $(ax^3+\frac2{x^2})^4$ with $x^2$ coefficient 6 ⇒ $a=\pm\frac12$.
- **Sums of expansions**:
  - $\sum_{k=1}^{20}(1+x^2)^k$: $x^4$ → $C^{21}_3=1330$; $x^6$ → $C^{21}_4$.
  - $\sum_{k=1}^{20}(1+x)^k$: $x^3$ → $C^{21}_4=5985$.
  - Use the geometric-sum form $\frac{(1+x)^{n+1}-(1+x)}{x}$ or the hockey-stick identity.
- **Coefficients in AP**: in $(1+x)^n$, terms 5,6,7 (ascending) in AP ⇒ $n=7$ or 14; terms 2,3,4 ⇒ $n=7$.
- **Largest coefficient**: in $(5x+3)^{20}$, $a_k=C^{20}_k5^k3^{20-k}$; from $a_k\ge a_{k\pm1}$ ⇒ $k=13$.
- **多項式定理** (99/資優): $(a_1+\dots+a_m)^n=\sum\frac{n!}{p_1!\cdots p_m!}a_1^{p_1}\cdots a_m^{p_m}$; number of terms $C^{n+m-1}_{m-1}$.
  - $(x+2y-z)^5$: 21 terms; $x^2y^2z$ → −120.
  - $(1+2x-x^2)^{10}$: $x^3$ → 780.
  - $(\frac1x-\frac2{x^2}+x^3)^6$: $x^5$ → −120.
  - $(x+y+z+u)^5$: 56 terms; $x^2y^2z$ → 30.
  - $(x+y+z+u+t)^6$: 210 terms; $x^3y^2z$ → 60 (60 similar terms); $x^2y^2ut$ → 180 (30 similar).
  - $[(a-2b)^2-c]^5$: 36 terms; $a^2b^2c^3$ → −240. $[(a-2b)^2-3c]^5$: $a^3b^3c^2$ → −14400.
  - $(-3x^2+2x+1)^{10}$: $x$ → 20. $(x^2-2x+\frac1{x^2})^6$: constant → 260.
  - $(1+x-x^2)^{50}=1+ax+bx^2+\dots+cx^{100}$ ⇒ $a=50$, $b=C^{50}_2-50=1175$, $c=(-1)^{50}=1$. The key prints $c=1226$, which is wrong.
- **組合恆等式** from $(1+x)^n=\sum C^n_kx^k$:
  - $x=1$: $\sum C^n_k=2^n$ (combinatorial meaning: buy or don't buy each of $n$ items).
  - $x=-1$: alternating sum 0 ⇒ even-index sum = odd-index sum $=2^{n-1}$.
  - $x=2$: $\sum2^kC^n_k=3^n$.
  - Differentiate or use $kC^n_k=nC^{n-1}_{k-1}$: $\sum kC^n_k=n2^{n-1}$; $\sum(3k-1)C^n_k=(3n-2)2^{n-1}+1$.
  - $\frac1{k+1}C^n_k=\frac1{n+1}C^{n+1}_{k+1}$ ⇒ $\sum\frac{C^n_k}{k+1}=\frac{2^{n+1}-1}{n+1}$ (so $=\frac{31}{n+1}$ gives $n=4$).
  - **Vandermonde** $\sum_iC^n_iC^m_{r-i}=C^{n+m}_r$ (choose $r$ from $n$ boys and $m$ girls): $C^{10}_0C^8_3+\dots+C^{10}_3C^8_0=C^{18}_3$; $\sum_{k=0}^8C^{10}_kC^{10}_{8-k}=C^{20}_8$; $\sum(C^n_k)^2=C^{2n}_n$; $\sum_{k=0}^{49}C^{50}_kC^{50}_{k+1}=C^{100}_{49}=C^{100}_{51}$ ⇒ $n+k=149$ or 151.
  - Drills: $C^{12}_2+C^{12}_4+\dots+C^{12}_{12}=2^{11}-1=2047$. For even $n$, $\sum3^{2j}C^n_{2j}=\frac{4^n+(-2)^n}2=2^{2n-1}+2^{n-1}$ → (D). $(1-\frac13)^n<\frac1{500}$ ⇒ $n\log\frac23<-\log500$ ⇒ $n=16$. $500<2^n-1<1000$ ⇒ $n=9$. $\sum_{k\ge1}\frac1{C^k_2}\to2$ (telescoping).
  - $2a_4=3a_{n-6}$ in $(1+x)^n$ ⇒ $n=9$. In $\sum_{k=1}^n(1+x)^k$, the $x^n$ coefficient is $a_n=C^{n+1}_3$ ⇒ $\sum_{n=2}^{20}\frac1{a_n}=\frac{209}{140}$.
  - Strings over {0,1,2} of length $n$ with an even number of 0s: $\frac{3^n+1}2$ (also $\sum_jC^n_{2j}2^{n-2j}$).
- **整除、餘式、近似**:
  - $x^{100}+x \bmod (x-1)^2$: write $x=(x-1)+1$ ⇒ $101x-99$.
  - $x^{20}\bmod(x-1)^3$ → $190x^2-360x+171$.
  - $(2x^2-4x+3)^{10}=[2(x-1)^2+1]^{10}$ ⇒ remainder mod $(x-1)^3$ is $20(x-1)^2+1=20x^2-40x+21$.
  - $11^{18}=(10+1)^{18}\bmod1000$ → 481.
  - $(1.1)^{12}\approx3.14$; $(1.05)^{10}\approx1+0.5+0.1125=1.6125\to1.6$.
- 學測/指考:
  - **2014學測**: $(1+\sqrt2)^6=a+b\sqrt2$ ⇒ $b=C^6_1+2C^6_3+4C^6_5$ (odd powers of $\sqrt2$) → (2).
  - **2012指定乙** $(x^2+y)^{12}$: $x^{10}y^7$ has coefficient $C^{12}_7=792$. $x^{24}$ (1) and $x^8y^8$ ($C^{12}_8=495$) are smaller; $x^{12}y^6$ (924) is larger; $x^{14}y^5$ (792) is equal ⇒ (1)(4).
  - $(x-1)^{30}$: degree 30 ✓; integer coefficients ✓; $x^{19}$ coefficient $-C^{30}_{19}$ ✗; $x^{10}$ coefficient $+C^{30}_{10}$ ✓; **constant term $(-1)^{30}=+1$**, so option (3) 「常數項為−1」 is false ⇒ (1)(2)(5). The 99 key prints (1)(2)(3)(5), a misprint.

**Traps**:
- Check set-equation answers by substituting back (elements must stay distinct).
- $\in$ vs $\subset$ when sets contain sets.
- 分組: equal-size unlabeled groups ⇒ ÷k!.
- 「至少」 ⇒ use the complement; do not use "choose one first, then any" (it over-counts).
- 重複排列: decide who has the choices ($m^n$ vs $n^m$).
- 不盡相異物 vs 組合 when choosing from multisets: classify by the 同/異 pattern.
- Binomial coefficient vs 「係數」 including constants and sign.
- 「第k項」 is index $k-1$.

## 11. 古典機率與期望值

**Scope**: D-10-4 複合事件的古典機率 (樣本空間與事件, 複合事件的古典機率性質, **期望值**). Conditional probability, independence and 貝氏 are §21 (D-11A-2/3). Repeated trials $C^n_kp^k(1-p)^{n-k}$ appear here in 99/資優 examples; in 108 they belong to 獨立事件 (§21), and 二項分布 is [超出數A] (§24). **Sources**: 108一下 3-4古典機率與期望值; 99第二冊 3-1樣本空間與事件, 3-2機率; 資優 第44單元古典機率, 第46單元數學期望值. (資優 第45單元 → §21.)

### 11.1 樣本空間與事件
- 隨機現象 (≥2 possible outcomes, unknown in advance); 隨機試驗 = repeatable random phenomenon. **樣本空間** $S$ = set of all outcomes (元素 = 樣本點). **事件** = any subset of $S$ (including $\varnothing$ and $S$); $|S|=n$ ⇒ $2^n$ events ($S=\{a,b,c,d\}$ → 16). 基本事件 = a one-point event. An event 「發生」 iff the outcome lies in it.
- 全事件 $S$, 空事件 $\varnothing$, 餘事件 $A'$, **和事件** $A\cup B$ (at least one occurs), **積事件** $A\cap B$ (both occur), **互斥** $A\cap B=\varnothing$. 互斥 ≠ 餘事件: sum = 3 and sum = 5 on two dice are 互斥, but $B\ne A'$.
- **Writing $S$ depends on how you draw** (balls 1–4, two draws):
  - Without replacement: ordered pairs with $x\ne y$, 12 points.
  - With replacement: 16 points.
  - Two at once: unordered $\{x,y\}$, $C^4_2=6$ points.
- 例: 3 coins, $A$ = 至少一正, $B$ = 第三次反 ⇒ $A\cap B=\{(+,+,-),(+,-,-),(-,+,-)\}$, $A'=\{(-,-,-)\}$. Balls 1–5 with $A$ = odd: $S$ has 32 events; 4 of them are 互斥 with $A$ (subsets of {2,4}).

### 11.2 古典機率 (Laplace)
- If all outcomes of $S$ are **equally likely**, $P(A)=\frac{n(A)}{n(S)}$.
- **Make the sample space equally likely**: label identical balls (紅1, 紅2, …) and treat identical dice as distinct.
  - 10紅1白 gives $P(\text{白})=\frac1{11}$, not $\frac12$; likewise 3紅200黑1白 does not give $\frac13$ for 黑.
  - Two dice: $\{1,2\}$ has probability $\frac2{36}$ and $\{1,1\}$ has $\frac1{36}$, not $\frac1{21}$ each.
- **Kolmogorov 公理** (99/資優):
  - (1) $0\le P(A)\le1$.
  - (2) $P(S)=1$.
  - (3) If $A\cap B=\varnothing$, then $P(A\cup B)=P(A)+P(B)$.
  - Consequences: $P(\varnothing)=0$; $P(A')=1-P(A)$; $A\subset B\Rightarrow P(A)\le P(B)$; $P(A\cup B)=P(A)+P(B)-P(A\cap B)$; 3-event 排容.
- **Draw method matters** (2紅3白, one red and one white):
  - With replacement: $\frac{12}{25}$.
  - Without replacement: $\frac{12}{20}=\frac35$.
  - Two at once: $\frac{C^2_1C^3_1}{C^5_2}=\frac35$.
  - Without replacement in order equals the simultaneous draw.
  - Both red with 3紅2藍: $\frac9{25}$ / $\frac3{10}$ / $\frac3{10}$.
- **Sum of dice**:
  - Two dice, sums 2..12: counts 1,2,3,4,5,6,5,4,3,2,1 out of 36.
  - Three dice, sums 3..18: counts 1,3,6,10,15,21,25,27,27,25,21,15,10,6,3,1 out of 216.
  - Two dice: doubles $\frac16$; sum 4 $\frac1{12}$; sum 5 $\frac19$; sum >7 $\frac5{12}$; sum 8 $\frac5{36}$.
  - Three dice: all different $\frac59$; exactly two equal $\frac{90}{216}=\frac5{12}$ (88學科); exactly one 6 $\frac{75}{216}=\frac{25}{72}$ (the 108 練習7 key prints $\frac5{18}$; the correct value is $\frac{25}{72}$).
  - Special dice (2–7 on each die, 90自): sum 9 is most likely (D). Dice 1,1,1,2,2,3 and 1,2,2,3,3,3: sum 4 is most likely, $\frac7{18}$.
  - Three throws $a,b,c$: $a<b<c$ → $\frac{5}{54}$; $a\le b\le c$ → $\frac7{27}$; $a+b+c=11$ → $\frac18$; $(a-b)(b-c)=0$ → $\frac{11}{36}$; $(a-b)(b-c)=2$ → $\frac1{18}$.
- **袋中取球 / 選人**:
  - 3紅5黃2白: one ball red $\frac3{10}$; two balls same color $\frac{14}{45}$.
  - 3白4黑5紅, choose 3: 1黑2紅 $\frac2{11}$; same color $\frac3{44}$; all different $\frac3{11}$; exactly two colors $\frac{29}{44}$.
  - 7紅3白, choose 4, at least one white → $1-\frac{C^7_4}{C^{10}_4}=\frac56$.
  - 4 defective of 10, choose 3: at most one defective $\frac23$; at least one $\frac56$.
  - 4男2女, choose 3, both sexes present → $\frac45$.
  - 20男15女, choose 3, both sexes present → $\frac{90}{119}$ (2011學測).
  - 6男9女, committee of 5: 3男2女 $\frac{240}{1001}$; all one sex $\frac4{91}$.
  - 5 couples, choose 4: exactly two couples $\frac1{21}$; exactly one couple $\frac47$.
  - Black shoes 3 pairs + white 2 pairs, choose 4 forming 2 pairs → $\frac{23}{105}$ (left/right matters); socks → $\frac{53}{105}$.
  - **Each person's chance of being sampled** $=\frac{C^{N-1}_{n-1}}{C^N_n}=\frac nN$ (5 of 30 → $\frac16$). **2011指定乙** sampling schemes: 方案一 (25+25 from halves), 三 (one of each pair), 四 (odd/even by die) give everyone $\frac12$; 方案二 does not → (1)(3)(4).
- **Numbers**:
  - 10–99: units > tens $\frac25$; units = tens $\frac1{10}$.
  - 1–20, choose 3: product odd $\frac{2}{19}$; sum divisible by 3 $\frac{32}{95}$; arithmetic progression $\frac3{38}$; no two consecutive $\frac{68}{95}$.
  - 1–10, choose 3: AP $\frac16$; GP $\frac1{30}$ ((1,2,4),(2,4,8),(1,3,9),(4,6,9)); three consecutive $\frac1{15}$; exactly two consecutive $\frac7{15}$; none consecutive $\frac7{15}$.
  - 1–100, choose 3, AP → $\frac{2C^{50}_2}{C^{100}_3}=\frac1{66}$ (the smallest and largest share parity).
  - 1–10, choose 2: $p$(even sum)$=\frac49$, $q=\frac59$ ⇒ (1) $p+q=1$ and (4) $|p-q|\ge\frac1{20}$ (93學科).
  - 8 odd + 5 even, sum of two even → $\frac{19}{39}$.
  - 1–7, choose 4, sum odd → $\frac{16}{35}$ (86社).
  - 1–9, choose 4, sum even → $\frac{1+60+5}{126}=\frac{11}{21}$ (the 108 習題10 key prints $\frac16$, a misprint).
  - Three-digit numbers from 1–5 distinct: even $\frac25$, multiple of 4 $\frac15$.
  - Password from 3,3,8,9 → $\frac1{12}$ (92學科).
- **Cards**: two cards same rank $\frac1{17}$; royal flush $\frac{4}{C^{52}_5}=\frac1{649740}$; full house $\frac{13\cdot C^4_3\cdot12\cdot C^4_2}{C^{52}_5}=\frac6{4165}$; two pairs $\frac{C^{13}_2(C^4_2)^2\cdot44}{C^{52}_5}=\frac{198}{4165}$; four of a kind $\frac{13\cdot48}{C^{52}_5}$.
  - 20 high cards (10–A), choose 4: same suit $\frac4{969}$; exactly two suits $\frac{80}{323}$; two pairs $\frac{24}{323}$.
  - Two red cards: $\frac{C^{26}_2}{C^{52}_2}=\frac{25}{102}<\frac14$.
- **Arrangements / 錯排**:
  - 5 business cards: exactly 2 people get their own $\frac{C^5_2D_3}{120}=\frac16$; all get their own $\frac1{120}$; nobody does $\frac{44}{120}=\frac{11}{30}$.
  - **白球先取完**: 3紅5白 drawn out one by one ⇒ white finishes first iff the **last ball is red** ⇒ $\frac38$; in general $\frac m{m+n}$.
  - 紅4白3黑5: red finishes first $=1-\frac4{7}-\frac4{9}+\frac4{12}=\frac{20}{63}$.
  - 20 bulbs with 3 broken; the 3rd broken one found on the 7th check → $\frac{C^3_2C^{17}_4}{C^{20}_6}\cdot\frac1{14}=\frac1{76}$.
  - 3紅3白 laid in a row; the first three contain two adjacent whites → $\frac7{20}$ (2016指定乙, via the complement).
  - 3男3女 in 3 rows of 2, each row mixed → $\frac25$.
- **Birthday/pigeonhole and occupancy**:
  - At least two of 4 people in the same club (6 clubs) → $1-\frac{P^6_4}{6^4}=\frac{13}{18}$.
  - Birth months: $P(5)=1-\frac{P^{12}_5}{12^5}$; $P(14)=1$.
  - 4 people leave a lift on floors 2–6, some floor gets ≥2 → $1-\frac{P^5_4}{5^4}=\frac{101}{125}$.
  - $r$ distinct balls into $n$ boxes, at most one per box → $\frac{C^n_r\,r!}{n^r}$.
  - Five dice $x..v$: not all different $\frac{49}{54}$; $(x-y)(y-z)(z-u)(u-v)=0$ → $1-(\frac56)^4=\frac{671}{1296}$.
  - Rooms of 4/3/3 for 10 people; at least two of 甲乙丙 share → $\frac7{10}$.
  - HBL 16 teams in 4 groups; 3 given teams in different groups → $\frac{12}{15}\cdot\frac8{14}=\frac{16}{35}$.
  - 12 cards in two piles of 6: 1,2,3 together $\frac2{11}$; 1–4 split 2+2 $\frac5{11}$.
  - Regular 12-gon, 4 vertices pairwise non-adjacent → $\frac{105}{495}=\frac7{33}$.
- **Games and geometry**:
  - Rock-paper-scissors with 3 people: only 甲 wins $\frac19$; no result $\frac13$.
  - **2017學測 frog**: 4 random unit steps, returns to O → $\frac{36}{256}=\frac9{64}$.
  - **2014指定甲** 3×3 number card: three balls with no two in the same row/column → $\frac{3!}{C^9_3}=\frac1{14}$.
  - 5×4 grid of 1–20, two numbers in different row and column → $\frac{12}{19}$; $n\times n$ → $\frac{n-1}{n+1}$.
  - $x^2+ax+b=0$ ($a,b$ dice) with real roots and $\alpha^2+\beta^2<11$ → $\frac5{36}$.
  - A cube cut into 1000 cubes, one with no paint → $\frac{512}{1000}=\frac{64}{125}$.
  - 甲乙 each draw from 1–42 with replacement, 甲 ≥ 乙 → $1-\frac{C^{42}_2}{42^2}=\frac{43}{84}$ (1–40 → $\frac{41}{80}$).
  - Two 3-number picks from 0–99: identical $\frac1{161700}$; sharing at least one $\frac{713}{8085}$.
  - Lamps 1–10 with 3 broken, both 4 and 5 broken → $\frac1{15}$ (85社).
  - Determinant of $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ with entries 4 or 5 is odd → $\frac38$.
- **性質 problems**:
  - $P(A)=\frac13$, $P(B)=\frac14$, $P(A\cup B)=\frac25$ ⇒ $P(A\cap B)=\frac{11}{60}$, $P(A')=\frac23$, $P(A'\cap B)=\frac1{15}$, $P(A'\cup B)=\frac{17}{20}$.
  - $P(A)=\frac13$, $P(B)=\frac12$: $P(A\cap B)=\frac16$ ⇒ $P(A\cup B)=\frac23$; $P(A\cup B)=\frac56$ ⇒ $P(A\cap B)=0$.
  - Pairwise 互斥 with $\frac12,\frac3{10},\frac1{30}$ → union $\frac56$.
  - $P=\frac14$ each, $P(A\cap B)=P(B\cap C)=0$, $P(A\cap C)=\frac18$ → $\frac58$.
  - Even 0.5, even or multiple of 3 0.6, multiple of 6 0.3 ⇒ multiple of 3 is 0.4.
  - A is twice B, B is three times C ⇒ $P(A)=\frac35$.
  - Die with $P(k)\propto k$: $P(2)=\frac2{21}$, even $\frac47$, odd $\frac37$, prime $\frac{10}{21}$, odd prime $\frac8{21}$.
  - Three dice: no 1 $\frac{125}{216}$; at least one 1 $\frac{91}{216}$; at least one 1 and at least one 2 $1-2\cdot\frac{125}{216}+\frac{64}{216}=\frac5{36}$; either $\frac{19}{27}$.
  - 統一發票 last digits from 3 receipts: at least one 0 → 0.271 (C); at least one 0 and at least one 9 → $1-2(0.9)^3+0.8^3=0.054$ (B) (80自).
  - 4 children: all boys $\frac1{16}$; at least one girl $\frac{15}{16}$ (the handout key prints $\frac5{16}$; the correct value is $\frac{15}{16}$); same sex $\frac2{16}$; mixed $\frac{14}{16}$; 2+2 $\frac6{16}$.
- **Bounds from 排容** (108 core skill):
  - **2015指定乙 半糖/去冰**: 37 and 28 of 50 ⇒ $P(A\cap B)\in[\frac{15}{50},\frac{28}{50}]=[0.3,0.56]$ → (2)(3).
  - **2013指定乙**: 打工 60%, 升學 70% ⇒ $P(\text{both})\in[0.3,0.6]$ → (1)(2).
  - **2011指定乙** three tests ($A_1..A_8$ sign patterns): (1)(2).
- **Lotteries and exams**:
  - 2003指定乙: all six numbers even ≈ $\frac{C^{21}_6}{C^{42}_6}\approx0.0103$ → closest (5) $\frac1{26}$.
  - 2005學測: $\frac rR=\frac{C^{42}_6}{C^{39}_5}\approx9.1$ → (4).
  - 2006學測 grid cells in different columns → (5) $\frac45$.
  - **2009學測** two classes from the same school $\frac{3\cdot2+4\cdot3+5\cdot4}{12\cdot11}=\frac{38}{132}\approx28.8\%$ → (5).
- **重複試驗** (preview of §21/§24): exactly $k$ sixes in $n$ throws $=C^n_k(\frac16)^k(\frac56)^{n-k}$ (10 throws, 7 sixes: $C^{10}_7\frac{5^3}{6^{10}}$; 4 sixes: $C^{10}_4\frac{5^6}{6^{10}}$). Four throws: exactly two 1s $\frac{25}{216}$; at least two $\frac{171}{1296}$. Instrument readings 68–72 (freq 5,15,10,15,5); three readings averaging 71 → $\frac9{125}$.
- 是非 traps (99 習題/2017):
  - A random digit table does not have equal frequencies in each row.
  - Coins have no memory (3H2T in the first 5 says nothing about the last 5).
  - $P(\text{both H}\mid\ge1\text{ H})=\frac13$.
  - All six faces appearing on 6 dice has probability $\frac{6!}{6^6}<\frac16$.
  - 黑白 balls drawn with vs without replacement give different probabilities, but draw-in-order without replacement equals the simultaneous draw.

### 11.3 數學期望值
- If the outcomes $A_1,\dots,A_n$ partition $S$ with $P(A_i)=p_i$ ($\sum p_i=1$, which serves as a check) and value $m_i$, then $E=\sum m_ip_i$, the **weighted average** with probabilities as weights. $E$ is the **long-run average**, not a guaranteed result (one throw of a die "expects" $\frac72$, but 10 throws do not guarantee 35). **公平遊戲** ⇔ $E=0$.
- Origin: Pascal–Fermat **賭金分配** (1654). First to 3 wins, 甲 leads 1–0 ⇒ $P(\text{甲})=\frac{11}{16}$, so the 64 法郎 split 44 : 20.
  - 甲 leads 2–0 (5600元) ⇒ 4900 : 700.
  - Tennis set, first to 6, 甲 leads 5–0 ⇒ 乙 needs 6 straight ⇒ $1000\cdot\frac{63}{64}$ : $1000\cdot\frac1{64}$.
- **Linearity shortcuts** (average value × number drawn, or sum of indicators):
  - One die $\frac72$; two dice 7; six dice 21.
  - 10元 and 5元 ×3 each, take 2 → 15; ×4 each, take 3 → 22.5.
  - 200元×3 and 100元×2 cards, take 2 → 320.
  - Balls labelled 1元×4 and 5元×2, take 2 → $\frac{14}3$ (88學科, 3 balls 1,1,5: $\frac{14}3$ as well).
  - **Hypergeometric mean** $=n\cdot\frac{K}{N}$: 2 defective of 10, take 3 → $\frac35$; 3 white of 12, take 3 → $\frac34$; 2 bad of 9, take 3 → $\frac23$; 4 of 40, take 2 → $\frac15$; 3 red of 7, take 3 → $\frac97$; 2 overnight loaves of 13, take 3 → $\frac6{13}$ (at least one: $\frac{11}{26}$).
  - Empty boxes: 3 balls into 3 bags → $3(\frac23)^3=\frac89$ (all bags used $\frac29$, all in one bag $\frac19$); 3 books into 4 drawers → $4(\frac34)^3=\frac{27}{16}$.
  - Coins: number of heads in $n$ tosses → $\frac n2$.
  - Random walk (+1 with prob $\frac13$, −1 with prob $\frac23$, 4 steps) → $-\frac43$.
  - Max of 3 dice → $\sum_k k\frac{k^3-(k-1)^3}{216}=\frac{119}{24}$.
  - Cards 1,1,2,2,3,3, take 2, product → $\frac{58}{15}$.
  - Ball $k$ appears $k$ times ($k=1..n$), payoff $r$ → $\frac{2n+1}3$; payoff $r-1$ → $\frac{2(n-1)}3$. Ball $k$ appears $k^2$ times → $\frac{3n(n+1)}{2(2n+1)}$.
  - Draw with replacement until the first white (2 of 10): expected number of draws 5. 5黑3白 until white: expected number of blacks $\frac{q}{p}=\frac53$.
- **公平扣分**:
  - 5-option single choice worth 8 → deduct 2.
  - Worth 5 → deduct $\frac54$.
  - Multi-select with 31 possible answers worth 12 → deduct $\frac25$.
  - "至少一個正確" multi-select worth 5 → deduct $\frac16$.
  - One option known wrong, +4/−1 → $E=\frac14$.
  - **92學科**: 16 sure + 6 questions with 3 options left + 3 pure guesses ⇒ $64+6\cdot\frac23+0=68$.
- **Games**:
  - 108 例13: coin twice, +200 / +80 / −400 ⇒ $E=-10$; fair if the loss is 360.
  - 3 coins: +5/+10/+15, −100 for no head ⇒ −5; with −60 ⇒ 0.
  - **86學科** pick $n$, three dice: +3/+2/+1/−1 ⇒ $-\frac{17}{216}$.
  - Three dice, pay 10: all equal +120, AP +30 ⇒ unfavourable; fair if AP pays 40.
  - Slot machine (老鼠0.1 牛0.4 老虎0.5, pay 5) ⇒ −1.65.
  - **93學科** 1000/800/600/0 with a half-prize redraw on 0 ⇒ $600+\frac14\cdot\frac12\cdot600=675$.
  - **2007學科** 摸彩: $E_甲=\frac{67}{14}$ ⇒ $E_乙=E(11-k)=11-\frac{67}{14}=\frac{87}{14}$.
  - **2009學測**: 2 blue (2000) + 5 red (1000) + $x$ others, target $E=300$ ⇒ $\frac{9000}{7+x}=300$ ⇒ $x=23$.
  - Biased die $P(X)=AX+B$ with $E=4$ ⇒ $A=\frac1{35}$, $B=\frac1{15}$.
  - **Taking turns** (geometric):
    - First to throw a 1, order 甲乙丙: probabilities ∝ $1:\frac56:\frac{25}{36}$ = 36:30:25. Stakes 340/300/270 ⇒ 丙 is worst off.
    - Order 甲乙乙甲… ⇒ ratio 31:30 ⇒ 甲 should put in 310 against 乙's 300.
    - First to throw sum 7 for 110元 ⇒ 甲 60, 乙 50.
    - Two coins HH, order 甲乙丙 ⇒ ratio 16:12:9 ⇒ if 甲 pays 3600 when winning, 乙 pays 4800 and 丙 pays 6400.
- **Decisions**:
  - Insurance: 50歲 survival 0.9998, payout 200萬, premium 2400 ⇒ insurer's E = 2000. Survival 98.5%, 50萬, premium 1萬 ⇒ 2500.
  - Travel insurance: 200萬 cover, premium 800, cost 200, claim probability $\frac2{10000}$ ⇒ $800-200-400=+200$ (資優 key prints −200, a sign misprint).
  - 108 例12 禮券: $5000\cdot\frac16+3000\cdot\frac26+1000\cdot\frac36=\frac{7000}3$. 練習18: 10/20/50元 ⇒ 20.
  - **89社** 建廠 (大/中/小 × 4 景氣) ⇒ 中廠, E = 17 百萬. **91指定乙** 甲地 3200 vs 乙地 2700 萬 ⇒ 甲. The 108 例16 table gives 乙地.
  - **88社** 彩券 (10元/張; per million tickets the prizes total 370萬) ⇒ expected loss 6.3元.
  - 釋迦 (1 in 5 has worms): opened at 80/斤 ⇒ $E=-8$ versus −14 unopened ⇒ ask to open.
  - Engines (sell 10; reject the lot if either of 2 checked is defective; 1 defective): $P(\text{accept})=\frac45$ ⇒ $0.8\cdot250-0.2\cdot700=60$ 萬.
  - 飯糰 (price 15, cost 10, demand table) with 70 made ⇒ 248.
  - Cakes (25/15; demand 230/250/270/290 on 6/18/20/6 days): making 270 ⇒ 2400; the best choice is 250 (2440).
  - Melons (pick 4 yellow of 8 blind): $35000\cdot\frac1{70}+28000\cdot\frac{16}{70}+21000\cdot\frac{53}{70}=22800$.
  - 服飾店 4 A (−20), 3 B (−5), 3 C (+10); choose 3: 10 kinds of selection; break even $\frac{21}{120}=\frac7{40}$ (A+C+C or B+B+C).

**Traps**:
- Never use an unequally-likely $S$ in the Laplace formula.
- 「至少」 ⇒ use the complement.
- 互斥 ≠ 獨立 (§21).
- Expectation of a sum = sum of expectations, even without independence.
- Draw-without-replacement in order matches the simultaneous draw.
- Handout keys occasionally misprint (see the corrections noted above); always sanity-check $0\le P\le1$ and recompute.

## 12. 三角比：直角三角比、廣義角與極坐標、正弦定理、餘弦定理、三角測量

**Scope**:
- G-10-6 三角比: acute → 廣義角 sin/cos/tan, 特殊角, 計算機 keys.
- G-10-5 廣義角和極坐標: initially −180°..360°; 極坐標 ↔ 直角坐標 on grid paper; 斜率 ⇔ 斜角.
- G-10-7 三角比的性質: 正弦定理, 餘弦定理, 正射影; 斜率 = tan(斜角); 反三角鍵 for 斜角 and the angle between two lines; **三角測量＃** embedded, not a separate unit; 長方體 cross-sections and 正角錐.
- 學測 forbids calculators and prints needed values (e.g. sin 14°), so 查表/線性內插 (99) is legacy; 計算機 keys appear only in 108 classroom activities.
- cot, sec, csc are ※ (F-11A-1); they appear in 99/資優 here.
- 弧度 is §13.

**Sources**: 108一下 4-1直角三角比, 4-2廣義角三角比與極坐標, 4-3三角比的性質; 99第三冊 1-1直角三角形的邊角關係, 1-2廣義角與極坐標 (its 附錄 弧度制 → §13), 1-3正弦定理與餘弦定理, 1-5三角測量 (+三角函數值表); 資優 第16單元廣義角三角函數, 第17單元正弦與餘弦定理, 第18單元三角測量.

### 12.1 直角三角比 (G-10-6)
- In right △ABC (∠C=90°) with $a,b,c$ opposite A, B, C:
  - $\sin A=\frac ac$ (對/斜), $\cos A=\frac bc$ (鄰/斜), $\tan A=\frac ab$ (對/鄰).
  - These depend only on ∠A (相似三角形).
  - Legs: $a=c\sin A$, $b=c\cos A$. $\overline{AC}=\overline{AB}\cos A$ is the **正射影** of $\overline{AB}$ on line AC.
- 特殊角: 30°/45°/60° from the triangles $1:\sqrt3:2$ and $1:1:\sqrt2$.
  - $\sin30^\circ=\frac12$, $\cos30^\circ=\frac{\sqrt3}2$, $\tan30^\circ=\frac1{\sqrt3}$.
  - $\sin45^\circ=\cos45^\circ=\frac{\sqrt2}2$, $\tan45^\circ=1$.
  - Derived values (資優/99):
    - **15°** (from ∠A=15° with ∠ABD=15°, BC=1): CD=√3, AD=2, $AB=\sqrt6+\sqrt2$, giving $\sin15^\circ=\frac{\sqrt6-\sqrt2}4$, $\cos15^\circ=\frac{\sqrt6+\sqrt2}4$, $\tan15^\circ=2-\sqrt3$.
    - **18°** (36° isosceles triangle with angle bisectors, △BCD∼△ABC): $\sin18^\circ=\frac{\sqrt5-1}4$.
- **基本關係**:
  - 商數 $\tan\theta=\frac{\sin\theta}{\cos\theta}$.
  - 平方 $\sin^2\theta+\cos^2\theta=1$ (note $\sin^2\theta=(\sin\theta)^2$).
  - 餘角 $\sin(90^\circ-\theta)=\cos\theta$, $\cos(90^\circ-\theta)=\sin\theta$.
  - ※ extras: 倒數 $\cot=\frac1{\tan}$, $\sec=\frac1{\cos}$, $\csc=\frac1{\sin}$; $1+\tan^2=\sec^2$, $1+\cot^2=\csc^2$; $\tan(90^\circ-\theta)=\cot\theta$.
- One value gives the rest:
  - $\tan A=2$ ⇒ $\sin A=\frac2{\sqrt5}$, $\cos A=\frac1{\sqrt5}$.
  - $\cos A=\frac{24}{25}$ ⇒ $\sin A=\frac7{25}$, $\tan A=\frac7{24}$.
  - $\tan\theta=\frac56$ ⇒ $\sin\theta=\frac5{\sqrt{61}}$.
  - $\tan\theta=k$ ⇒ $\cos\theta=\frac1{\sqrt{1+k^2}}$, $\sin\theta=\frac k{\sqrt{1+k^2}}$.
  - $\sin A=k$ ⇒ $\cos A=\sqrt{1-k^2}$.
  - $\frac{1+\tan\theta}{1-\tan\theta}=3+2\sqrt2$ ⇒ $\tan\theta=\frac1{\sqrt2}$, $\sin\theta=\frac1{\sqrt3}$.
  - Isosceles 6,6,4: $\sin B=\frac{2\sqrt2}3$, $\tan B=2\sqrt2$.
  - $\sin\theta=\frac35$ ⇒ $\sin\frac\theta2=\frac1{\sqrt{10}}$, $\cos\frac\theta2=\frac3{\sqrt{10}}$ (geometric construction).
- **Monotonicity on (0°,90°)** (quarter unit circle: $\sin\theta=\overline{AB}$, $\cos\theta=\overline{OB}$, $\tan\theta$ = tangent segment): sin ↗, cos ↘, tan ↗; $\tan\theta>\sin\theta$.
  - Order: $\sin18^\circ=\cos72^\circ<\tan18^\circ<\cos18^\circ=\sin72^\circ<\tan72^\circ$.
  - $\cos\theta>\tan\theta$ ⇔ $\sin\theta<\frac{\sqrt5-1}2$ (θ ≲ 38.17°).
  - 資優 adds: $\sin<\tan<\sec$; $\cos<\cot<\csc$ (for acute angles).
- **Symmetric-sum technique** ($s=\sin\theta$, $c=\cos\theta$): $(s\pm c)^2=1\pm2sc$.
  - $s+c=\frac43$ ⇒ $sc=\frac7{18}$, $s-c=\pm\frac{\sqrt2}3$ (negative if θ<45°), $s^3+c^3=(s+c)(1-sc)=\frac{22}{27}$.
  - $s-c=\frac12$ ⇒ $sc=\frac38$, $s+c=\frac{\sqrt7}2$.
  - $s-c=\frac13$ ⇒ $sc=\frac49$, $s+c=\frac{\sqrt{17}}3$, $s=\frac{1+\sqrt{17}}6$.
  - $s+c=\frac1{\sqrt2}$ ⇒ $sc=-\frac14$, $s-c=\pm\frac{\sqrt6}2$, $s^3+c^3=\frac{5\sqrt2}8$, $s^6+c^6=1-3(sc)^2=\frac{13}{16}$.
  - $s,c$ are the roots of $5x^2-7x+k=0$ ⇒ $s+c=\frac75$, $sc=\frac{12}{25}$, $k=\frac{12}5$, $s^3+c^3=\frac{91}{125}$.
- **Linear condition plus the square relation**:
  - $2s+c=2$ ⇒ $(s,c)=(\frac35,\frac45)$.
  - $7s-c=5$ ⇒ $s=\frac45$ (reject $\frac35$, which gives $c<0$).
  - $c+3s=2$ ⇒ $c+s=\frac{4+\sqrt6}5$.
- **Homogeneous expressions given tan** (divide by $\cos^n$):
  - $\tan\theta=3$ ⇒ $\frac{2s+3c}{s-2c}=9$; $\frac{3s+c}{s-2c}=10$; $\frac{s^2-3sc+2c^2}{s^2+c^2}=\frac{9-9+2}{10}=\frac15$; $\frac{10s+3}{c+1}=\pm3\sqrt{10}$; $\frac{2s^2+sc-c^2}{s^2+sc-2c^2}=2$.
- Identities to prove: $\frac{1+\cos\theta}{\sin\theta}+\frac{\sin\theta}{1+\cos\theta}=\frac2{\sin\theta}$; $(s\pm c)^2=1\pm2sc$.
- Applications:
  - Cable-car slope 30°, 1000 m ⇒ rise 500 (450 → 950 m).
  - Rectangle with AB=9 and the diagonal at 60° to BC ⇒ area $27\sqrt3$.
  - Picture on a 2 m ladder at 72° ⇒ ≈1.9 m.
  - Right triangle with legs 3,4 and altitude CD, then DE ⊥ AC ⇒ DE = $\frac{48}{25}$.
  - **2014學測**: circle radius 24, OC=26, tangent CD ⇒ $\cos\theta=\frac{12}{13}$ ⇒ $\overline{AB}=24\sin\theta=\frac{120}{13}$.
  - **2018學測** ladder: at 60°, pulled 51 cm to $\sin=0.6$ ⇒ $0.8l-0.5l=51$ ⇒ $l=170$.
  - **2020學測** 3-4-5 and 5-12-13: $\sin\alpha>\sin30^\circ>\sin\beta$ → (2).
  - **2020指定甲**, 45°<θ<90°: $a=\sin^2\theta$, $b=\frac{\sin^2\theta}{\cos\theta}$, $c=\sin\theta\cos\theta$ ⇒ $c<a<b$ → (5).
  - Inscribed / circumscribed regular $n$-gon perimeters: $2nr\sin\frac{180^\circ}n$ and $2nr\tan\frac{180^\circ}n$.
  - Circle inscribed in a sector of angle 2θ, radius a ⇒ $r=\frac{a\sin\theta}{1+\sin\theta}$ ($\frac13a$ at θ=30°).
  - Square cut at angle θ to keep $\frac34$ of the area ⇒ $\tan\theta=3-2\sqrt2$.
  - Isosceles base 12, apex 40° ⇒ height $6\tan70^\circ$.
  - $\cos B=\frac45$, $\cos C=\frac1{\sqrt5}$, $MH=5$ ⇒ $BC=22$.
  - Embankment with top 2, height 12, $\tan\alpha=\frac13$, $\tan\beta=\frac25$ ⇒ base 68, slope $12\sqrt{10}$.
  - Orthocentre: $AH=\frac{b\cos A}{\sin B}$ (1).
  - $\tan A=1,\tan B=2,\tan C=3$ ⇒ $\frac{abc}{h_ah_bh_c}=\frac1{\sin A\sin B\sin C}=\frac53$.
  - Concentric circles trisecting a diameter ⇒ $\tan\alpha\tan\beta=\frac14$.
  - $x\cos\theta+y\sin\theta=4$, $x\sin\theta-y\cos\theta=3$ ⇒ $x^2+y^2=25$.
  - ∠BDC=90°, ∠ADB=30°, AB=CD=1 ⇒ $BC=\sqrt[3]2$.

### 12.2 廣義角、同界角、象限 (G-10-5)
- **有向角**: counter-clockwise is positive, clockwise negative; 始邊/終邊. **標準位置角**: vertex at O, 始邊 on the positive x-axis; quadrant = the quadrant of the 終邊; 象限角 = $90^\circ n$.
- **同界角** $\theta-\varphi=360^\circ k$.
  - 1178° → 98° and −262°; 1999° → 199°; −2009° → 151°; 675° → 315°/−45°; −1520° → 280°/−80°; −1473° → 327°/−33°; −21508° → 92°/−268°.
  - −1000° is in the 1st quadrant.
- Definition: on the 終邊 take $P(x,y)$ with $r=\sqrt{x^2+y^2}$: $\sin\theta=\frac yr$, $\cos\theta=\frac xr$, $\tan\theta=\frac yx$ ($x\ne0$). On the unit circle, $P=(\cos\theta,\sin\theta)$. The values are independent of the choice of P.
- **Signs**: 「全(I) 正弦(II) 正切(III) 餘弦(IV)」 — sin>0 in I, II; cos>0 in I, IV; tan>0 in I, III. $|\sin|,|\cos|\le1$; tan is any real.
- Quadrantal values: $\sin90^\circ=1$, $\cos90^\circ=0$, tan 90° undefined; sin 270° = −1. Table for 120°, 135°, 150°, 210°, 225°, 300°, 330°.
- 例:
  - $P(-5k,12k)$ ⇒ $\sin=\frac{12}{13}$, $\cos=-\frac5{13}$, $\tan=-\frac{12}5$.
  - $P(-3k,-2k)$ ⇒ $\sin=\frac{-2}{\sqrt{13}}$, $\tan=\frac23$.
  - II-quadrant $P(x,2)$ with OP=3 ⇒ $x=-\sqrt5$, $\cos=-\frac{\sqrt5}3$.
  - $(-5\sqrt3,y)$ with $\tan=\frac1{\sqrt3}$ ⇒ $y=-5$, $\sin=-\frac12$.
  - $(x,-5\sqrt2)$ with $\tan=\sqrt2$ ⇒ $\sin=-\frac{\sqrt6}3$.
  - $\sin=\frac45$ in II ⇒ $\cos=-\frac35$.
  - $\sin=-\frac45$ in III ⇒ $\cos=-\frac35$, $\tan=\frac43$.
  - $\tan=-\frac43$ in IV ⇒ $\sin=-\frac45$, $\cos=\frac35$.
  - $\tan=-\frac34$ and $\sin>0$ ⇒ $\frac{3s+5c}{2s+6c}=\frac{11}{18}$.
- **Solving basic equations on [0°,360°)**:
  - $\sin=\frac12$ → 30°, 150°; $\cos=-\frac{\sqrt2}2$ → 135°, 225°.
  - $\sin>\frac{\sqrt3}2$ → (60°,120°); $\cos\ge\frac12$ → [0°,60°]∪[300°,360°).
  - $\tan=-1$ → 135°, 315°; $\cos=-\frac{\sqrt3}2$ → 150°, 210°.
  - $\sin>-\frac12$ → [0°,210°)∪(330°,360°); $\cos\le-\frac12$ → [120°,240°].
  - $4\cos^2\theta-8\cos\theta-5=0$ ⇒ $\cos=-\frac12$ ⇒ $\sin=\pm\frac{\sqrt3}2$.
- **2010學測**: $|\cos\theta_i|=\frac13$ in quadrants I–IV ⇒ $\theta_1+\theta_2=180^\circ$ ✓, $\cos\theta_3=-\frac13$ ✓; $\theta_1>45^\circ$; $\sin\theta_4=-\frac{2\sqrt2}3$; $\theta_4=540^\circ-\theta_3$ → (2)(3).

### 12.3 角度化簡 (reduction)
- Coterminal: $f(360^\circ n+\theta)=f(\theta)$.
- Negative angle: $\sin(-\theta)=-\sin\theta$, $\cos(-\theta)=\cos\theta$, $\tan(-\theta)=-\tan\theta$ (reflection in the x-axis).
- $180^\circ\pm\theta$, $360^\circ\pm\theta$: same function, with the sign of the result quadrant **treating θ as acute**.
- $90^\circ\pm\theta$, $270^\circ\pm\theta$: **sin ↔ cos swap**, then the sign rule. Rotating $P(x,y)$ by 90° gives $(-y,x)$ ⇒ $\sin(\theta+90^\circ)=\cos\theta$ and $\cos(\theta+90^\circ)=-\sin\theta$.
- 例:
  - $\tan\theta=-\frac{12}5$ in II ⇒ $\sin=\frac{12}{13}$, $\cos(\theta+90^\circ)=-\frac{12}{13}$, $\tan(180^\circ-\theta)=\frac{12}5$.
  - $\cos100^\circ=k$ ⇒ $\sin(-260^\circ)=\sqrt{1-k^2}$, $\tan(-260^\circ)=-\frac{\sqrt{1-k^2}}k$, $\cos(-80^\circ)=-k$, $\sin(-80^\circ)=-\sqrt{1-k^2}$.
  - $\tan20^\circ=k$ ⇒ $\cos250^\circ=-\frac k{\sqrt{1+k^2}}$.
  - $\sin=-\frac35$ in IV ⇒ $\cos=\frac45$, $\sin(180^\circ+\theta)=\frac35$, $\tan(180^\circ-\theta)=\frac34$.
  - $\cos330^\circ\tan750^\circ+\sin(-300^\circ)\tan480^\circ=-1$; $4\cos(-960^\circ)+\tan585^\circ+2\sin(-1020^\circ)=-1+\sqrt3$; $\sin1230^\circ=\frac12$.
  - $a=\sin1230^\circ$, $b=\cos(-430^\circ)$, $c=\tan65^\circ$, $d=\sin(-430^\circ)$ ⇒ $c>a>b>d$ (D).
  - $\sin(180^\circ-\theta)\cos(90^\circ-\theta)+\sin(90^\circ+\theta)\cos(-\theta)=1$.
  - $\cos\theta+\sin\theta=\frac15$ in II ⇒ $\cos=-\frac35$, $sc=-\frac{12}{25}$, $\frac{\sec}{\tan}+\frac{\csc}{\cot}=\frac1s+\frac1c=-\frac5{12}$.
  - Square on hypotenuse (3-4-5), $\theta=\angle ACD=C+90^\circ$ ⇒ $\frac{\sin\theta+\cos\theta}{1+\tan(90^\circ+\theta)}=\frac4{35}$.
  - 0°<θ<45° ⇒ $\sqrt{1-2sc}-\sqrt{1+2sc}=(c-s)-(c+s)=-2\sin\theta$.
  - $\sum_{k=1}^{90}\sin^2k^\circ=\frac{91}2$; $\sum_{k=1}^{360}\sin k^\circ=0$.
  - Points $P_k$ dividing a unit semicircle into 180 parts: $\sum_{k=1}^{179}\overline{AP_k}^2=\sum(2-2\cos k^\circ)=358$.
  - $A+B+C=180^\circ$ ⇒ $\tan\frac{A+B}2=\cot\frac C2$, etc.
  - $(\sin\theta\cos\theta,\tan\theta\cos\theta)$ in quadrant III ⇒ θ in IV.
  - $\sin\theta=x+\frac1x$ is impossible ($|x+\frac1x|\ge2$).
  - $\sin\theta$ a root of $x^2+x+a=0$ ⇒ $a=-(s+\frac12)^2+\frac14\in[-2,\frac14]$.
  - 120° ≤ θ < 210° with $2(m-1)\sin\theta=m+1$ ⇒ $m<0$ or $m\ge2+\sqrt3$.
  - 45°<θ<90° and $\log_{1/2}$ of sin/cos/tan/sec ⇒ $b>a>c>d$.
- **摩天輪**: base 3 m, radius 15, period 6 min, 15 min 36 s ⇒ 2.6 turns ⇒ 216° from the bottom ⇒ height $18-15\cos216^\circ\approx30$ m.

### 12.4 極坐標 (G-10-5)
- $P[r,\theta]$ (r ≥ 0, 0° ≤ θ < 360° by convention; the pole is $[0,\theta]$); infinitely many representations $[r,\theta+360^\circ n]$. Conversion: $x=r\cos\theta$, $y=r\sin\theta$, $r=\sqrt{x^2+y^2}$.
- 例:
  - Rectangular to polar: $(-2,2\sqrt3)$ → [4,120°]; $(2,2\sqrt3)$ → [4,60°]; $(3\sqrt2,-3\sqrt2)$ → [6,315°]; $(-2,2)$ → $[2\sqrt2,135°]$; $(4\sin20^\circ,4\cos20^\circ)$ → [4,70°]; $(0,-3)$ → [3,270°]; $(-4\sqrt3,-4)$ → [8,210°].
  - Polar to rectangular: [4,240°] → $(-2,-2\sqrt3)$; [2,330°] → $(\sqrt3,-1)$; $[3,\theta]$ with $\cos\theta=\frac35$ in IV → $(\frac95,-\frac{12}5)$.
  - Calculator: (−5,12) → [13,113°]; (24,−7) → [25,344°]; (−3,−4) → [5,233°] (adjust the quadrant; $\cos^{-1}$ gives 0°..180°, $\sin^{-1}$ and $\tan^{-1}$ give −90°..90°).
- Area $\triangle AOB=\frac12r_1r_2\sin|\theta_1-\theta_2|$: [2,50°], [√3,170°] → $\frac12\cdot2\sqrt3\sin120^\circ=\frac32$.
- A[4,125°], B[2,215°]: ∠AOB = 90°, so the midpoint C has $OC=\frac12AB=\sqrt5$.
- Equilateral △OAB with A(1,1) ⇒ $B[\sqrt2,105^\circ]=(\frac{1-\sqrt3}2,\frac{1+\sqrt3}2)$.
- Rotating [2,25°] by 90° gives [2,115°].
- Square OBCD with D(−2,2): $A[2\sqrt2,345°]$, $B[2\sqrt2,45°]$, $C[4,90°]$, $D[2\sqrt2,135°]$.
- Typhoon 「花蓮東南方140公里」 = [140, 315°].

### 12.5 三角形面積、正弦定理 (G-10-7)
- **Area**:
  - $\frac12ab\sin C$ (two sides and the included angle; valid for acute, right or obtuse C).
  - Quadrilateral: $\frac12pq\sin\theta$ (diagonals p, q, angle θ); max given $p+q=10$ is $\frac{25}2$.
  - **Heron** $\sqrt{s(s-a)(s-b)(s-c)}$; $=rs$; $=\frac{abc}{4R}$.
  - 例: equilateral $\frac{\sqrt3}4a^2$; AC=10, BC=8, C=135° → $20\sqrt2$; diagonals 12 and 5 with $\theta_1=2\theta_2$ (so 60°) → $15\sqrt3$; AC=5, AB=8, $\cos A=-\frac45$ → 12.
  - Squares on the legs of a 3-4-5 triangle: $\cos\angle DCE=-\frac35$, area 6.
- **正弦定理** $\frac a{\sin A}=\frac b{\sin B}=\frac c{\sin C}=2R$. Proof: divide the area formula by $abc$; inscribed angle on the diameter BD (cases acute/right/obtuse; $\sin(180^\circ-A)=\sin A$). Uses:
  - Ratio form: $a:b:c=\sin A : \sin B : \sin C$.
  - Side ↔ angle conversion: $a=2R\sin A$, $\sin A=\frac a{2R}$.
  - Use it for 「一邊二角」 (AAS/ASA).
  - 例:
    - $(b+c):(c+a):(a+b)=5:6:7$ ⇒ $4:3:2$; =4:5:6 ⇒ 7:5:3 (largest angle 120°).
    - B=55°, C=65°, a=10 ⇒ $R=\frac{10}{\sqrt3}$.
    - A=45°, B=60°, BC=√2 ⇒ AC=√3, R=1.
    - c=8, A=105°, B=45° ⇒ $b=8\sqrt2$.
    - AB=10, C=60°, B=75° ⇒ $BC=\frac{10\sqrt6}3$.
    - ∠A:∠B:∠C = 3:4:5 ⇒ $\sin$ ratio $2\sqrt2:2\sqrt3:(\sqrt6+\sqrt2)$; ∠A=30°, ∠B=45° ⇒ $2:2\sqrt2:(\sqrt6+\sqrt2)$; $-a+2b-c=0$ and $3a+b-2c=0$ ⇒ 3:5:7.
    - Two circles meeting at A, B, with ∠ACD=30° and ∠ADC=45° ⇒ area ratio $\frac{\sin^245^\circ}{\sin^230^\circ}=2:1$.
    - Cyclic ABCD with ∠CAD=30°, ∠ACB=45°, CD=2 ⇒ 2R=4, $AB=2\sqrt2$.
    - Cyclic, ∠DBC=30°, ∠ABD=45°, CD=6 ⇒ $AD=6\sqrt2$.
    - Area $=\frac{abc}{4R}$.
    - Sun–Mars distance ≈ $2.38\times10^8$ km; balloon: PB ≈ 579 m, height ≈ 349 m.
    - **2009學測** 甲乙丙 20 km apart, roads at 45° ⇒ $x=\frac{20\sin120^\circ}{\sin45^\circ}=10\sqrt6\approx24.5$ (1).
    - **2014學測** 正三角形 side 1 with ∠1=∠2=∠3=15° ⇒ inner equilateral side $\frac{\sin45^\circ-\sin15^\circ}{\sin120^\circ}=\frac{\sqrt6-\sqrt2}2$.
    - **2006指定乙** 嘌呤 (regular pentagon + hexagon, side 1) → (2)(3)(4).

### 12.6 餘弦定理
- $a^2=b^2+c^2-2bc\cos A$ (proof: drop the altitude, $BD=c-b\cos A$ in all cases; 99/資優 also give 圖解 with rectangles), so $\cos A=\frac{b^2+c^2-a^2}{2bc}$.
- **角的分類**: $A$ is acute/right/obtuse ⇔ $a^2<,=,>b^2+c^2$. The largest angle sits opposite the largest side, so check only that one.
- **射影定理** $a=b\cos C+c\cos B$ (and cyclic versions).
- 例:
  - Ratio $\sin A : \sin B : \sin C=4:5:7$ ⇒ $\cos C=-\frac15$, $\sin C=\frac{2\sqrt6}5$.
  - AB=3, AC=4: A=60° → $\sqrt{13}$; A=90° → 5; A=138° → 6.54.
  - Sides 13, 8, 7 ⇒ $C=120^\circ$, altitude $\frac{7\sqrt3}2$.
  - $\sqrt2:2:(\sqrt3-1)$ ⇒ $B=135^\circ$.
  - $(a+b+c)(a+b-c)=3ab$ ⇒ C=60°; $(a+b+c)(b+c-a)=bc$ ⇒ A=120°.
  - Pond: AC=7, AB=10, A=60° ⇒ $BC=\sqrt{79}$. AB=80, AC=50, A=60° ⇒ 70.
  - a=3, b=4, $\tan A=\frac34$ ⇒ c = 5 or $\frac75$ (SSA).
  - **2019學測**: ∠ACB=30°, ∠EDB=60°, ∠AEB=120°, CD=15, ED=7 ⇒ AB=13.
  - **2007學科**: AB=3, AC=5, A=120°, M the midpoint of BC ⇒ $\tan\angle BAM=5\sqrt3$.
  - **2020學測** 箏形 AB=BC=√2, AD=CD=2, ∠BAD=135° ⇒ $BD=\sqrt{10}$, $AC=\frac{2\sqrt{10}}5$.
  - Triangle 7,8,9 (AB=7, BC=8, CA=9) with squares on AB and AC ⇒ $EG^2=b^2+c^2+2bc\cos A=196$ ⇒ EG=14.
  - Altitudes 6, 4, 3 ⇒ $a:b:c=2:3:4$; smallest angle cos $\frac78$; smallest side $\frac{16\sqrt{15}}{15}$.
  - $15-x$, $19-x$, $23-x$ obtuse ⇒ 3<x<11.
  - $a=3+t^2$, $b=3-2t-t^2$, $c=4t$ ⇒ 0<t<1, largest angle 120°.
  - AB=7, BC=5, AC=3 ⇒ ∠ACB=120°; extend BC by CD=2 ⇒ $AD=\sqrt7$.
  - Square ABCD with PA=1, PB=3, PD=√7 ⇒ rotate △ABP 90° ⇒ ∠APD=135° ⇒ area $8+\sqrt{14}$.
- **Shapes** (convert with 正弦/餘弦定理):
  - $\sin^2A+\sin^2B<\sin^2C$ ⇒ obtuse.
  - $\cos B\sin C=\sin B\cos C$ ⇒ isosceles.
  - $2\cos B\sin A=\sin C$ ⇒ isosceles (A=B).
  - $a\cos A-b\cos B+c\cos C=0$ ⇒ right triangle.
  - $a\cos A=b\cos B$ ⇒ $(a^2-b^2)(c^2-a^2-b^2)=0$ ⇒ isosceles or right.
- **Lengths inside a triangle**:
  - **中線定理** $AB^2+AC^2=2(AD^2+BD^2)$; $AM^2=\frac14(b^2+c^2+2bc\cos A)$. Parallelogram: sum of squares of the diagonals = sum of squares of the sides.
  - **Stewart** (資優): $AC^2\cdot EB+BC^2\cdot AE=CE^2\cdot AB+AE\cdot EB\cdot AB$.
  - **Angle bisector**: $BD:DC=AB:AC$ (AB=15, BC=20, CA=10 ⇒ BD=12, $AD=\sqrt{AB\cdot AC-BD\cdot DC}=3\sqrt6$); by areas (AB=3, AC=6, A=120° ⇒ AD=2, $CD=2\sqrt7$); AB=6, AC=10, A=120°, ∠BAD=30° ⇒ $AD=\frac{30\sqrt3}{13}$; external bisector (A=60°, 15, 24) ⇒ 40.
  - A=75°, $AB=2\sqrt6$, AC=2, ∠BAD=30° ⇒ $AD=\sqrt6$ (area splitting).
  - **87大學自**: D on BC with $BD=\frac13BC$, A=60° ⇒ $AD^2=\frac19(b^2+4c^2+2bc)$ (B).
  - $\frac1a+\frac1b=\frac{\sqrt3}c$ when ∠AOC=∠BOC=30° (area splitting).
- **圓內接四邊形** (opposite angles supplementary ⇒ $\cos D=-\cos B$; two cosine-rule equations for the diagonal):
  - Sides 1,2,3,4 ⇒ $AC=\sqrt{\frac{55}7}$, $\sin B=\frac{2\sqrt6}7$, area $2\sqrt6$.
  - AB=5, BC=12, AC=13 (diameter), ∠A=120° ⇒ $BD=13\sin120^\circ=\frac{13\sqrt3}2$.
  - AB=5, ∠ADC=105°, ∠DCB=90°, ∠ABD=60° ⇒ BD=10 (diameter), $AC=10\sin75^\circ=\frac{5(\sqrt6+\sqrt2)}2$.
  - AD=BC=5, CD=3, ∠BCD=120° ⇒ BD=7, AB=8.
  - **2011學測** AB=1, BC=5, CD=5, DA=7, ∠A=∠C=90° ⇒ $AC=4\sqrt2$ (Ptolemy: $AC\cdot BD=1\cdot5+5\cdot7$).
  - Semicircle diameter 4 with AB=BC=1 ⇒ $CD=\frac72$ (d satisfies $x^3-(a^2+b^2+c^2)x-2abc=0$).
  - **Ptolemy** $AC\cdot BD=ac+bd$ and the diagonal formulas (資優 進階).
- **解三角形 / SSA ambiguity** (given $a, b, A$; $h=b\sin A$):
  - A acute: $a<h$ → none; $a=h$ → one (right); $h<a<b$ → **two**; $a\ge b$ → one.
  - A obtuse or right: $a\le b$ → none; $a>b$ → one.
  - 例: AC=15, AB=15√3, B=30° ⇒ (A=90°, BC=30) or (A=30°, BC=15).
  - a=1, b=2, A=60° → none; A=30° → right triangle with $c=\sqrt3$.
  - $a=2\sqrt3$, $b=2\sqrt2$, A=60° ⇒ B=45°, $c=\sqrt6+\sqrt2$.
  - $a=\sqrt2$, b=2, A=30° ⇒ two solutions: $c=\sqrt3\pm1$ (B=45° or 135°).
  - AB=1, AC=√3, A=30° ⇒ BC=1, B=120°.
  - **2016學測**: A=20°, AB=5, BC=4 (SSA with BC<AB, two triangles) ⇒ only sin C and R are determined → (2)(5).
  - **2021學測**: AB=4, AC=6, plus one more datum: cos A ✓ (SAS); cos B ✓ (since AC>AB the circle meets ray BC once); cos C ✗; area ✗ (A acute or obtuse); R ✗ → (1)(2).
  - **2019學測** 50° ≤ A < B ≤ 60° ⇒ (1) sin A < sin B, (2) sin B < sin C → (1)(2).
- **Optimization**:
  - **2009學測**: AB=10, AC=9, $\cos A=\frac38$, $[APQ]=\frac12[ABC]$ ⇒ $xy=45$, $PQ^2\ge2xy(1-\cos A)=\frac{225}4$ ⇒ min $\frac{15}2$. (The 108 例14 with $\cos A=\frac35$ gives 6; with AB=9, AC=8, A=40°: AD=AE=6.)
  - a=2, b=1: max area at C=90° ⇒ $c=\sqrt5$; max B at $c=\sqrt3$.
  - Side √3 opposite 60° ⇒ $\sqrt3<x+y\le2\sqrt3$.
  - Perimeter 20, A=60°, $R=\frac{7\sqrt3}3$ ⇒ (7,8,5), $r=\sqrt3$.
- Heron examples:
  - 13, 14, 15 → 84.
  - 4, 6, 8 → $3\sqrt{15}$, height on 6 is $\sqrt{15}$, $r=\frac{\sqrt{15}}3$, $R=\frac{16\sqrt{15}}{15}$.
  - 11, 13, 20 → area 66, r=3, $R=\frac{65}6$.
  - 70, 80, 90 (well equidistant from three houses) → $\cos C=\frac23$, $R=21\sqrt5$.
  - Quadrilateral AB=2, BC=6, CD=4, BD=6, ∠ABD=30° → $3+8\sqrt2$.
  - $\triangle PQR$ (contact triangle) : $\triangle ABC=r:2R$.
  - $r=(s-a)\tan\frac A2$.
- **2014指定甲**: AB=3, BC=4, CD=3, DA=x, AC=4 ⇒ $\cos B=\frac38<\frac37$; $1<x<7$; $x<\frac{13}2$ ✓; cyclic ⇒ $x=\frac74$ ✓ → (4)(5).

### 12.7 斜角、兩直線夾角 (G-10-7)
- **斜角** θ of a line: rotate from the positive x-axis by at most 90°, so $-90^\circ<\theta\le90^\circ$. **斜率 = tan(斜角)**; horizontal → 0°, vertical → 90°. The angle between two lines is the difference of their 斜角 (and its supplement).
  - $x+\sqrt3y=5$ (−30°) and $7x-2y=0$ (≈74°) ⇒ 104° / 76°.
  - $y=\sqrt3x$ (60°) and $y=-x+1$ (−45°) ⇒ 105° / 75°.
  - $y=3x$ (72°) and $4x+y=3$ (−76°) ⇒ 148° / 32°.
- 坡度 = $\tan\theta\times100\%$ (≤12% for bridges). An 18% ramp of horizontal length 200 needs +105.73 m to reach 12%.

### 12.8 三角測量 (＃)
- Terms:
  - 鉛垂線, 水平線, 視線.
  - 仰角/俯角 (acute angle between the line of sight and the horizontal).
  - 方位: 東25°北 = 北65°東; 東北 = 東45°北.
  - Protractor with a plumb line: 仰角 = 90° − reading.
- 解題原則 (資優18): right triangle ⇒ express lengths by trig ratios; 一邊二角 ⇒ 正弦定理; 二邊一角 ⇒ 餘弦定理; **3-D problems** ⇒ convert heights to horizontal distances ($d=h\cot\alpha$), then solve a ground triangle.
- 2-D examples:
  - 101 大樓: 45° then 75° after 370 m ⇒ ≈505 m.
  - 大佛: 45° and 22.5°, 20 m apart ⇒ $h=\frac{20}{\cot22.5^\circ-1}=10\sqrt2\approx14$.
  - 30° → 45° after 200 m ⇒ $100(\sqrt3+1)$.
  - Height formula: $h=\frac{a\sin\theta\sin\varphi}{\sin(\varphi-\theta)}$.
  - Hill 45°, platform 60°, 60-ft tower 75° ⇒ hill 30, platform $30(\sqrt3-1)$.
  - Bamboo 5 m on a 3 m wall: shadow $5\cos\theta-\frac3{\tan\theta}$ ⇒ a=−3, b=5.
  - Balloon from AB=100 (∠BAD=75°, ∠ABD=60°, elevation 30°) ⇒ $AD=50\sqrt6$, $h=50\sqrt2$.
  - 新光三越: ∠BAC=105°, ∠ABC=45°, AB=400 ⇒ $AC=400\sqrt2$; $\tan14^\circ=\frac14$ ⇒ $100\sqrt2$.
- **Four-point configurations** (∠1..∠4 at A, B):
  - AB=30 with 60°, 45°, 30°, 60° ⇒ $PQ=15\sqrt6$ (or via ABQP concyclic, $PQ=2R\sin60^\circ$).
  - Lake: ∠CAB=120°, ∠DBA=135°, ∠DAB=30°, ∠CBA=45°, AB=30 ⇒ AC=AD and ∠CAD=90° ⇒ $CD=30(\sqrt6+\sqrt2)$.
  - AC=2, ∠CAB=60°, ∠CBA=45° ⇒ $AB=\frac{2\sin75^\circ}{\sin45^\circ}=\sqrt3+1$.
- **Bearings**:
  - Ship E37°S at 50 knots for 3 h; island at E53°N, then N23°W ⇒ right triangle ⇒ $100\sqrt3$.
  - **89學科** typhoon: 恆春 SE 400 km → S15°W 200 km (60° apart) ⇒ $200\sqrt3$ km in 20 h ≈ 17 km/h.
  - **90學科**: A(2,0), B(−4,0), $\tan\angle BAC=\frac89$, $\tan\angle ABC=\frac83$ ⇒ C(−2.5,4); distance from D(2.5,−8) is 13.
  - **89學科** 航標: A(27,8) → B(2,3) → port O ⇒ turn left 45°.
  - Two lighthouses both at N15°E; after 5 nmi NW they are due E and NE ⇒ distances along the ray $5(\sqrt3-1)$ and 10 ⇒ $15-5\sqrt3$ nmi (A).
  - Lighthouse 200 m: ship due W at 45°, 5 min later at W30°S at 60° ⇒ $CD=\frac{200}{\sqrt3}$ ⇒ $800\sqrt3$ m/h.
  - Tower 25 m: B at 30°, C with $\sin\theta=\frac56$, ∠BAC=120° ⇒ BC=70.
  - Mound 20 m: C at 30°, D at 45°, ∠DAC=45° ⇒ $CD=20\sqrt2$ in 5 min ⇒ $4\sqrt2$ m/min.
  - 甲 from A to B at twice 乙's speed (B to C), equilateral side 14 ⇒ $d^2=7t^2-70t+196$ ⇒ min $\sqrt{21}$.
- **3-D (塔/山)**:
  - Tower: due E elevation 30°, due S elevation 45°, AB=50 ⇒ $3h^2+h^2=2500$ ⇒ h=25; C on AB with elevation 45° ⇒ BC=25.
  - E elevation 45°, S60°E elevation 30°, AB=10 (or 1000) ⇒ ∠AOB=30°, $AB^2=h^2+3h^2-2\sqrt3h^2\cos30^\circ=h^2$ ⇒ h = AB.
  - South 10 m at 60°, east at 30° ⇒ $h=10\sqrt3$, east distance 30, so the observers are $10\sqrt{10}$ apart; from their midpoint $\tan\theta=\frac{\sqrt{30}}5$.
  - Mountain from W (45°) and S (60°), 500 m apart ⇒ $h^2(1+\frac13)=500^2$ ⇒ $h=250\sqrt3$.
  - E/S with α, β ⇒ $AB=h\sqrt{\cot^2\alpha+\cot^2\beta}$.
  - **Three collinear points with elevations 30°, 45°, 60°** (foot not on the line): ground distances $\sqrt3h, h, \frac h{\sqrt3}$; apply **Stewart / 中線定理** on the ground line. CD=600, DE=400 ⇒ $200\sqrt{15}$; 30/20 ⇒ $10\sqrt{15}$; 300/200 ⇒ $100\sqrt{15}$; 200/100 ⇒ 300; 80/80 ⇒ $40\sqrt6$.
  - Three points all at elevation 15° ⇒ the foot is the circumcentre: BC=250, ∠BAC=30° ⇒ R=250 ⇒ $h=250\tan15^\circ=250(2-\sqrt3)$.
  - Plane at height $500\sqrt3$: due N at 60° ⇒ OC=500; 5 s later at 30° ⇒ OD=1500 ⇒ $CD=1000\sqrt2$ ⇒ $200\sqrt2$ m/s.
  - Look down at 45°, turn 30°, look down at 30° ⇒ h=d (A).
  - Cube edge 3, AP=1, AQ=2 ⇒ ∠BPQ ≈ 82°, area $\frac72$.
- **2009指定甲**: two flagpoles (29°/15° and 26°/19° from two points) ⇒ ratio ≈ 3.3. **2009指定甲**: P inside an equilateral triangle of side 5 with PB=4, PC=3 ⇒ $\cos\angle ABP\approx0.92$. **2013學測** balloon rising uniformly: 30° at 10:00, 34° at 10:10 ⇒ at 10:30 ≈ 41° (3).
- 99 legacy — 三角函數值表 and 線性內插:
  - $\sin33^\circ33'\approx0.5527$.
  - $\cos40^\circ10'\approx0.7641$; $\cos\theta=0.76$ ⇒ θ ≈ 40.53°.
  - $\tan35^\circ20'\approx0.7090$; $\tan\theta=0.71$ ⇒ θ ≈ 35.37°.
  - $\sin\theta=-0.803$ in III ⇒ θ ≈ 233°25'.

**Traps**:
- Use the 終邊 point's signs, not triangle lengths, for 廣義角.
- In 90°±θ reductions, swap sin↔cos.
- SSA ambiguity.
- Largest angle is opposite the largest side.
- In 「仰角」 problems the horizontal distance is $h\cot\alpha$.
- In 3-D survey problems, never assume the foot of the mountain is collinear with the observation points.
- Answer keys in these handouts often lose radicals or denominators (e.g. $\frac{13\sqrt3}2$ printed as 「13 3」); recompute.

# Part B — 11年級必修數學A

## 13. 弧度量與三角函數的圖形

**Scope**:
- N-11A-1 弧度量: definition, 弧長與扇形面積, calculator rad key; keep practising degree↔radian conversion in later contexts.
- F-11A-1 三角函數的圖形: sin/cos/tan graphs, 定義域, 值域, 週期性, **週期現象的數學模型**.
- cot/sec/csc 之定義與圖形 are **※** (taught in 99 數甲上 and 資優).
- 和差角/疊合 are §14.

**Sources**: 108二上 1-1三角函數的圖形; 99數甲上 2-1三角函數的圖形與性質; 99第三冊 1-2 附錄(弧度制); 資優 第19單元三角函數的圖形, 三角函數複習題 (its items belong to §12/§14/§22).

### 13.1 弧度 (radian)
- **Definition**: central angle $\theta=\frac sr$ (arc ÷ radius); arc = r ⇒ 1 弳 (rad).
  - The value is a pure real number, so trig functions become functions $\mathbb R\to\mathbb R$.
  - $\pi$ rad $=180^\circ$; $1^\circ=\frac\pi{180}\approx0.01745$; $1$ rad $\approx57.2958^\circ=57^\circ17'45''$.
  - A bare number is an angle in radians: $\pi^\circ\approx3.14^\circ$ but $\pi=180^\circ$; $x^\circ\ne x$.
  - Conversion: 度→弧度 ×$\frac\pi{180}$; 弧度→度 ×$\frac{180}\pi$.
  - Examples: 45°=$\frac\pi4$, 120°=$\frac{2\pi}3$, 330°=$\frac{11\pi}6$; $\frac{3\pi}4=135^\circ$; 2 rad ≈ 114.59°; −2 rad = $-\frac{360^\circ}\pi$; 200° ≈ 3.5 rad.
- **Quadrant of a real angle**:
  - 8 rad (8−2π≈1.72) is in II; 3.2 is in III; 10 rad is in III (10−2π≈3.72); 9.8 is in III.
  - Coterminal angle in $[0,2\pi)$: 50 → $50-14\pi$; −60 → $20\pi-60$; θ → θ−2πk.
  - $(\cos4,\tan6)$ is in III; the largest of sin1..sin5 is sin2.
- **扇形** (θ in radians):
  - 弧長 $s=r\theta$; 周長 $2r+r\theta$; 面積 $\frac12r^2\theta=\frac12rs$.
  - Circular motion through θ (possibly >2π or negative) has path length $r|\theta|$.
  - 例 (r=4): arc 4π → π; arc 8 → 2; arc 12.8 → 3.2. (r=3): arc 6π → 2π; arc 9 → 3.
  - r=5: θ=2 → arc 10, area 25; θ=$\frac{2\pi}3$ → arc $\frac{10\pi}3$, area $\frac{25\pi}3$.
  - r=4: 1 rad → area 8; $\frac{3\pi}4$ → 6π; 40° → $\frac{16\pi}9$.
  - Sector perimeter equal to the circle's circumference ⇒ $\theta=2\pi-2$.
  - Circular segment (r=1, 60°) ⇒ $\frac\pi6-\frac{\sqrt3}4$.
  - Sector of perimeter 10 with maximum area: $2r+r\theta=10$, $A=5r-r^2$ ⇒ $r=\frac52$, $A_{max}=\frac{25}4$, θ=2.
  - Cone r=5, h=12 unrolled ⇒ $\frac{10\pi}{13}$; r=3, h=4 ⇒ $\frac{6\pi}5$.
  - Ant on a cone (slant 12, base diameter 6 ⇒ sector $\frac\pi2$): full loop back to C → $12\sqrt2$; to D at AD=4 → $4\sqrt{10}$.
  - Cone r=4, $h=8\sqrt2$ (slant 12, sector $\frac{2\pi}3$): lateral area 48π; shortest path from P once around to the midpoint Q of AP is $\sqrt{12^2+6^2+72}=6\sqrt7$.
- **Rolling wheels** (rolled distance = $r\theta$):
  - r=15 rolls 20π ⇒ $\theta=\frac{4\pi}3$; the contact point rises to $15-15\cos\frac{4\pi}3=\frac{45}2$. (The 資優19 key prints $15(1+\frac{\sqrt3}2)$ for the same data, which is inconsistent; use $\frac{45}2$.)
  - **88學科**: r=50 rolls 200 ⇒ 4 rad ≈ 229°.
  - Circumference 60 rolled 120 ⇒ 4π.
  - Diameter 80 around an equilateral △ABC: BC parallel to the ground again after π rad, i.e. 40π cm.
  - Hubcap r=24: 100 cm ⇒ $\frac{25}6$ rad; A first reaches C's position after $\frac{4\pi}3$ ⇒ 32π ≈ 100.5 cm.
  - r=2 with P at $(\sqrt3,1)$ (centre (0,2)), rolled clockwise $\frac{7\pi}3$ ⇒ height $2+\sqrt3$.
- Other applications:
  - Particle on $x^2+y^2=4$ at 0.2 rad/s: period 10π s; at 15 s it is at $(2\cos3,2\sin3)$; path after 100 s is 40.
  - Earth (Eratosthenes): 6° = $\frac\pi{30}$ for 667 km ⇒ R ≈ 6369 km.
  - Three tangent circles of radius 2: ∠ = $\frac\pi3$; curvilinear triangle perimeter 2π, area $4\sqrt3-2\pi$.
  - Concentric r=3, 6 with inner arc 2: perimeter 12, area 9.
  - **90學科**: roads meeting at 60°, tangent points 450 m from C ⇒ $r=450\tan30^\circ$, central angle $\frac{2\pi}3$ ⇒ arc ≈ 544 m.
  - **88社**: grid circle with tangents ⇒ ∠COD=60°, total length $4\sqrt6+\frac{2\sqrt2}3\pi$.
  - **2015指定甲** clock (hour hand 5, minute hand 8): hour tip moves $\frac\pi{72}$ cm/min; tips 7 apart ⇒ angle $\frac\pi3$ ⇒ between 6:00 and 6:30 at ≈6:22.
  - $\overline{OP}$ with P(1,√3) rotated clockwise sweeping $\frac{14\pi}3$ ⇒ $\theta=\frac{7\pi}3$ ⇒ P′(2,0).
  - **Key inequality** $\sin\theta<\theta<\tan\theta$ for $0<\theta<\frac\pi2$ (compare △AOB < sector < △AOC: $\frac12\sin\theta<\frac12\theta<\frac12\tan\theta$).
- Reduction formulas in radians: $\sin(\pi\pm\alpha)$, $\cos(\frac\pi2+\alpha)=-\sin\alpha$, etc. (same rules as §12.3).
  - $\sin\frac{100\pi}3=-\frac{\sqrt3}2$; $\tan(-\frac{13\pi}4)=-1$; $\cos(-\frac{101\pi}6)=-\frac{\sqrt3}2$; $\csc\frac{7\pi}2=-1$.
  - $\sin\theta=\frac13$, $\cos\theta<0$ ⇒ $\cos\theta=-\frac{2\sqrt2}3$, $\sin(\theta+\pi)=-\frac13$, $\tan(\pi-\theta)=\frac1{2\sqrt2}$.
  - $\sin\theta=-\frac35$ in III ⇒ $\sin(\pi+\theta)=\frac35$, $\cos(\frac\pi2+\theta)=\frac35$, $\tan(\pi-\theta)=-\frac34$.
  - Statement check: $\sin(180-\theta)=\sin\theta$ ✗ (180 radians!); $\cos(\pi-\theta)=-\cos\theta$ ✓; $\sin(\theta+\frac\pi2)=\cos\theta$ ✓; $\tan(\theta+\pi)=\tan\theta$ ✓ → (B)(C)(D).
  - Ordering: $\sin2>\sin1>\sin3>\sin4>\sin5$; $\cos1>\cos5>\cos2>\cos4>\cos3$; with $a=\sin1, b=\sin2, c=\sin3, d=\cos4, e=\cos5$: $b>a>e>c>d$.
  - **$a=\sin(\pi^2)$**: $\pi^2-3\pi\approx0.445$ ⇒ $a=-\sin0.445\approx-0.43$ ⇒ $-\frac12<a<0$ (C). The 108 習題5 key prints (B), a misprint.
  - (A) $\sin9.8>0$ ✗; (B) $\sin9.8=\sin(3\pi-9.8)$ ✓; (C) $\sec\frac\pi2$ undefined ✓; (D) $(\csc2,\cot2)$ in IV ✓; (E) $\cos(\alpha-\pi)=\cos\alpha$ ✗.
  - **2016指定甲**: closest to $\cos(2.6\pi)=\cos(0.6\pi)<0$ is $\cot(2.6\pi)\approx\cos(2.6\pi)$ since $\sin(0.6\pi)\approx1$ → (3).
  - **2017學測**: for $\frac\pi2\le x\le\frac{3\pi}2$, $\cos x^\circ>0\ge\cos x$, so no x satisfies $\cos x^\circ\le\cos x$ → (1) 0.

### 13.2 正弦函數 $y=\sin x$
- Built from the unit circle: $y$ = the y-coordinate of $P(\cos x,\sin x)$. Values: 0↗1 on $[0,\frac\pi2]$, 1↘0 on $[\frac\pi2,\pi]$, 0↘−1 on $[\pi,\frac{3\pi}2]$, −1↗0 on $[\frac{3\pi}2,2\pi]$; then repeat.
- **週期函數**: $f(x+T)=f(x)$ for all x; the smallest positive T is **the 週期**.
- Properties of $\sin x$:
  - Domain $\mathbb R$, range $[-1,1]$, period 2π, **振幅** 1.
  - **Odd function**; symmetric about the points $(n\pi,0)$ and the lines $x=\frac\pi2+k\pi$.
- **Transformations** of $y=a\sin(bx-h)+k$ (a, b > 0):
  - Period $\frac{2\pi}b$, amplitude a, max a+k, min −a+k.
  - Horizontal shift by h (inside), vertical shift by k.
  - Vertical stretch by a changes the amplitude; horizontal stretch (sin bx) changes the period.
  - Order matters: $\sin x$ → left 1 → horizontal ×2 → vertical ×3 gives $3\sin(\frac x2+1)$.
  - $\cos x$ → right ½ → horizontal ×2 → vertical ×3 gives $3\cos(\frac12x-\frac12)$.
- **Reading parameters off a graph** (max/min ⇒ a, k; adjacent max→min = half-period ⇒ b; one point ⇒ phase):
  - 例: $y=a\sin bx+k$ with period $\frac{2\pi}3$, amplitude $\frac32$ ⇒ $a=\frac32$, b=3, $k=\frac52$.
  - 例: $y=a\sin bx$ with period $\frac{4\pi}3$ ⇒ (3, $\frac32$).
  - 例: $a\sin(bx+c)$ with $|c|<\frac\pi2$ ⇒ a=3, $b=\frac12$, $c=-\frac\pi6$.
  - $A\sin(bx+c)+k$ with max $(\frac\pi8,4)$ and min $(\frac{5\pi}8,-2)$ ⇒ A=3, k=1, period π ⇒ b=2, $c=\frac\pi4$ → (1)(3)(4)(5).
  - $f(x)=2\sin3x$: range [−2,2] ✓; max at $\frac\pi6$ ✓; period $\frac{2\pi}3$ ✓; symmetric about $x=\frac\pi2$ (a minimum point) ✓; $f(2)=2\sin6<0$ ✗ → (A)(B)(C)(D) (88社).

### 13.3 $y=\cos x$ and $y=\tan x$
- $\cos x=\sin(x+\frac\pi2)$, i.e. the sine graph shifted **left** by $\frac\pi2$.
  - Domain $\mathbb R$, range [−1,1], period 2π, **even**.
  - Axes of symmetry $x=n\pi$; centres $(\frac\pi2+k\pi,0)$; y-intercept (0,1).
- $\tan x$:
  - Domain $x\ne\frac\pi2+k\pi$; range $\mathbb R$; period **π**; odd.
  - Vertical **漸近線** $x=\frac\pi2+k\pi$; centres $(n\pi,0)$.
  - Unit-circle picture: the tangent line at A(1,0) meets ray OP at $(1,\tan\theta)$.
  - $\tan(-\frac\pi3)<\tan0.5<\tan1.5$.
  - $-1<\tan x<2$ on $(-\frac\pi2,\frac\pi2)$ ⇒ $-\frac\pi4<x<\tan^{-1}2\approx1.1$.
- ※ **sec, csc, cot** (99/資優):
  - Definitions: $\sec=\frac rx$, $\csc=\frac ry$, $\cot=\frac xy$; reciprocal relations; $\tan^2+1=\sec^2$, $1+\cot^2=\csc^2$; $\cot=\frac{\cos}{\sin}$.
  - $\sec x$: domain $x\ne\frac\pi2+k\pi$, range $|y|\ge1$, even, period 2π.
  - $\csc x$: domain $x\ne k\pi$, range $|y|\ge1$, odd, period 2π.
  - $\cot x$: domain $x\ne k\pi$, range $\mathbb R$, period π, odd, decreasing branches.
  - 例 $P(-3a,4a)$: sin $\frac45$, cos $-\frac35$, tan $-\frac43$, sec $-\frac53$, csc $\frac54$, cot $-\frac34$.
  - II with $\tan=-\frac32$ ⇒ $\sin\frac3{\sqrt{13}}$, $\cos-\frac2{\sqrt{13}}$, $\sec-\frac{\sqrt{13}}2$.
  - IV with $\cos=\frac35$ ⇒ $\csc-\frac54$, $\cot-\frac34$.
  - $\sin=-\frac45$ in IV ⇒ $\tan(\pi+\theta)=-\frac43$, $\sec(\pi-\theta)=-\frac53$, $\cot(\pi-\theta)=\frac34$.
  - $\cos=-\frac13$ in II ⇒ $\sec(\pi+\theta)=3$, $\sin(\pi-\theta)=\frac{2\sqrt2}3$, $\cot=-\frac1{2\sqrt2}$.
  - $P(-3,-4)$ ⇒ $\sin(\pi-\theta)=-\frac45$, $\cos(\theta+\frac\pi2)=\frac45$, $\sec(\theta+\pi)=\frac53$, $\cot=\frac34$, $\csc=-\frac54$.
  - $\sin\theta\cos\theta=\frac49$ with $0\le\theta\le\frac\pi4$ ⇒ $s+c=\frac{\sqrt{17}}3$, $s-c=-\frac13$, $\tan+\cot=\frac94$, $s=\frac{\sqrt{17}-1}6$, $\sec+\csc=\frac{3\sqrt{17}}4$.
  - $s-c=\frac12$ ⇒ $\tan+\cot=\frac83$, $\sec-\csc=\frac43$.
  - $\sin2\theta=\frac45$ with $0\le\theta\le\frac\pi4$ ⇒ $s+c=\frac{3}{\sqrt5}$, $s-c=-\frac1{\sqrt5}$, $\tan+\cot=\frac52$.
  - Identity: $\frac{\sec+\csc}{\tan+\cot}=\sin+\cos$.
  - **2012指定甲**: sinθ and cosθ are the roots of $x^2-a=0$ ⇒ $s+c=0$, $sc=-a$ ⇒ $\tan\theta=-1$, $\sin(\theta+\frac\pi4)=0$, $\sin2\theta=-1$, $a=\frac12$; two θ values → (2)(3)(4).

### 13.4 週期 (period rules)
- sin, cos, sec, csc: $aF(kx+b)+c$ has period $\frac{2\pi}{|k|}$; $|F(kx+b)|$ has period $\frac\pi{|k|}$.
- tan, cot: $aF(kx+b)+c$ and $|F(kx+b)|$ both have period $\frac\pi{|k|}$.
- Sum of periodic terms: period = lcm of the periods ($3\cos2x-2\sin3x$ → 2π; $\sec2x-4\sin\frac x2$ → 4π).
- Examples:
  - $\sin2x$ → π; $2-\tan3x$ → $\frac\pi3$; $|\sin x|$ → π; $|\sin x|+|\cos x|$ → $\frac\pi2$; $|\tan x|+|\cot x|$ → $\frac\pi2$.
  - $3+4\sin5x$ → $\frac{2\pi}5$; $\tan\frac{\pi-2x}3$ → $\frac{3\pi}2$; $|\sec\frac x3|$ → 3π; $-2\sin\frac x3$ → 6π; $|\sec3x|$ or $|\cos3x|$ → $\frac\pi3$; $4+3\sin(5x+2)$ → $\frac{2\pi}5$; $3\sec(\frac x4+8)-12$ → 8π.
  - $|\cos x|$ → π; $\cos x+|\cos x|$ → 2π; $\sin x-|\sin x|$ (zero on the upper half-waves).
  - $\sin|x|$ is **not periodic**.

### 13.5 圖形的應用：方程式根數、不等式、最值
- **Number of roots = number of intersections** of $y=f(x)$ with a line or curve.
  - $\sin x=\frac12$ on $[-\pi,3\pi]$ → 4 roots: $\frac\pi6,\frac{5\pi}6,\frac{13\pi}6,\frac{17\pi}6$.
  - $\sin x=\frac x{10}$ → 7 (also $10\sin x=x$ → 7); $\cos x=\frac x{10}$ → 7; $8\cos x=x$ → 5.
  - **2007學科** $\sin x=\frac x{10\pi}$ → odd and <20 (3).
  - $\tan x=-x$ on $(-\pi,\pi)$ → 3; tan and cos on $(0,2\pi)$ → 2.
  - **87學科**: $y=1-x$ and $y=\tan x$ on $(0,2\pi)$ → 3 (D).
  - **2017指考甲**: $3\sin x=2\sin2x$ on $[0,2\pi]$ ⇔ $\sin x(4\cos x-3)=0$ ⇒ x = 0, π, 2π plus two from $\cos x=\frac34$ → 5 (4).
  - $\sin x=\log x$ → 3 roots.
  - $\frac23x\sin x=1$ on $(-\pi,\pi)$ → 4 (even function; $x\sin x$ peaks ≈1.82 > 1.5 on (0,π)).
  - $\sin x=\frac13$ on $[0,4\pi]$ → 4 roots; $\sin x=-\frac13$ on $[0,4\pi]$ → 4 roots with sum $3\pi+7\pi=10\pi$ (pairs symmetric about $\frac{3\pi}2,\frac{7\pi}2$); $\cos x=-\frac13$ on $[0,2\pi]$ → 2 roots with sum 2π.
  - **2004 研究用試題**: $y=k$ with $-1<k<0$ meets $\sin x$ on $[0,2\pi]$ at two points whose x-sum is 3π (C).
  - $2\cos^2x=1-\sin x$ on $[0,2\pi)$ ⇒ $\sin x=1$ or $-\frac12$ ⇒ $\frac\pi2,\frac{7\pi}6,\frac{11\pi}6$, sum $\frac{7\pi}2$.
  - $f=\sin x+2|\sin x|$ on $[0,2\pi)$ meets $y=k$ exactly twice ⇔ $1<k<3$.
- **Inequalities** (read off the unit circle or the graph):
  - $\sin x\le\frac12$ on $[0,2\pi]$ ⇒ $[0,\frac\pi6]\cup[\frac{5\pi}6,2\pi]$; $\sin x\le-\frac12$ ⇒ $[\frac{7\pi}6,\frac{11\pi}6]$; $\sin x\ge\frac{\sqrt3}2$ ⇒ $[\frac\pi3,\frac{2\pi}3]$.
  - $\cos x<\frac12$ ⇒ $\frac\pi3+2k\pi<x<\frac{5\pi}3+2k\pi$.
  - Ranges: on $[\frac\pi6,\frac{5\pi}4]$ (contains π), $-1\le\cos x\le\frac{\sqrt3}2$; on $[\frac\pi6,\frac{3\pi}4]$, $\sin x\in[\frac12,1]$.
  - **Quadratic in sin or cos** (substitute $t$, respect $|t|\le1$):
    - $4\cos^2x-4\cos x-3\ge0$ ⇒ $\cos x\le-\frac12$ ⇒ $\frac{2\pi}3\le x\le\frac{4\pi}3$ (+2kπ).
    - $\cos2x\ge\cos x$ ⇒ $(2c+1)(c-1)\ge0$ ⇒ $\frac{2\pi}3\le x\le\frac{4\pi}3$ or $x=0$.
    - $3\sqrt3\sin x+\cos2x-4<0$ ⇒ $2s^2-3\sqrt3s+3>0$ ⇒ $s<\frac{\sqrt3}2$ ⇒ $[0,\frac\pi3)\cup(\frac{2\pi}3,2\pi)$.
    - $1+\cos x-2\sin^2x>0$ ⇒ $(2c-1)(c+1)>0$ ⇒ $[0,\frac\pi3)\cup(\frac{5\pi}3,2\pi)$.
  - **Max/min**: $f=4\cos^2x-12\sin x-3=-4s^2-12s+1$ on $[\frac\pi3,\frac{7\pi}6]$ ($s\in[-\frac12,1]$) ⇒ max 6 at $\frac{7\pi}6$, min −15 at $\frac\pi2$.
  - Range of $y=\frac{3\cos x-2}{\cos x+2}=3-\frac8{\cos x+2}$ ⇒ $[-5,\frac13]$ (6 not attained; −2 attained).
  - $\sec^2\theta=\frac{4xy}{(x+y)^2}\ge1$ ⇒ $(x-y)^2\le0$ ⇒ $x=y$.

### 13.6 週期現象的數學模型 (F-11A-1)
- Model $y=a\sin(b(x-h))+k$. With the max $M$, min $m$ and the times of adjacent max/min:
  - $a=\frac{M-m}2$, $k=\frac{M+m}2$.
  - Period = 2 × (time from max to min) ⇒ $b=\frac{2\pi}T$.
  - Fix h from one point (h is not unique).
- 例:
  - **月亮亮面**: max (22,1), min (8,0) ⇒ T=28, $b=\frac\pi{14}$, a=k=0.5, h=15.
  - **風力發電機**: blade 40 m, hub 67 m, period 4 s, starts at the top ⇒ $y=40\sin(\frac\pi2x+\frac\pi2)+67$ (a=40, $b=\frac\pi2$, c=67).
  - **美麗華摩天輪**: diameter 70, lowest point 30 m, 1 h per revolution, start at the bottom ⇒ $y=35\sin(2\pi t-\frac\pi2)+65$.
  - 潮汐 (max 13, min 7, period 12 h) ⇒ $y=3\sin\frac\pi6t+10$.
  - 示波器 $v=a\sin bt$ ⇒ a=10, b=20π ⇒ 10 rev/s.
  - 交流電 $I=10\sin(120\pi t+\frac\pi3)$: period $\frac1{60}$ s; max 10, min −10; at $t=\frac1{48}$, $I=10\sin(\frac{5\pi}2+\frac\pi3)=5$ A.
  - **造父變星** (仙王座δ, period 5.4 d):
    - 108 version uses 星等 3.7 (brightest) to 4.4: $y=\frac7{20}\sin(\frac{10\pi}{27}t+\frac{3\pi}2)+\frac{81}{20}$ (brightest = smallest magnitude at t=0 ⇒ $\sin\beta=-1$).
    - 99 version uses "亮度 4.0±0.35" with the maximum at t=0: $y=0.35\sin(\frac{2\pi}{5.4}t+\frac\pi2)+4$.
  - Rocket watched from 6 km at elevation $\frac{\pi x}{120}$ ⇒ $h=6\tan\frac{\pi x}{120}$; it reaches 60000 km at x ≈ 60 s (asymptote).
  - **Tourism**: $f(n)=100[A\sin(\omega n+\alpha)+k]$; max in Aug, min (100) in Feb, difference 400 ⇒ $\omega=\frac\pi6$, A=2, k=3, $\alpha=\frac{7\pi}6$; peak season $f\ge400$ ⇔ $\sin\ge\frac12$ ⇒ n = 6, 7, 8, 9, 10.

**Traps**:
- Always know whether a bare number is in radians.
- In $\sin(bx-h)$ the shift is $\frac hb$, not h.
- $|F|$ halves the period of sin/cos/sec/csc but not of tan/cot.
- 振幅 is $|a|$ (positive).
- When substituting $t=\sin x$, keep $-1\le t\le1$.
- $\sin|x|$ is not periodic.

## 14. 和差角公式、倍角半角、正餘弦疊合（附：積化和差、反三角函數）

**Scope**:
- G-11A-5 三角的和差角公式: 正弦與餘弦的和差角、倍角與半角公式. **The tan versions are 「推論之練習」**: derive them, but they are not memorised formula-sheet items. The formula sheet prints $\sin(A+B)$, $\cos(A+B)$ and $\tan(A+B)$.
- 疊合 $a\sin x+b\cos x=r\sin(x+\alpha)$ is part of the 108 二上1-3 curriculum (三角函數的應用 / 週期現象).
- **[超出數A]**:
  - 積化和差 / 和差化積 (99/資優; usable only as a derivation from the 和角公式).
  - 三倍角 as a memorised formula (derive it instead).
  - 反三角函數 (資優23).
  - 圓/橢圓參數式 (99 數甲 2-2; ellipses go to §23).

**Sources**: 108二上 1-2三角的和差角公式, 1-3正餘弦函數的疊合; 99第三冊 1-4差角公式; 99數甲上 2-2三角函數的應用; 資優 第20單元三角函數公式一, 第21單元三角函數公式二, 第22單元正餘弦的疊合, 第23單元反三角函數; 三角函數複習題.

### 14.1 和差角公式
- **Formulas**:
  - $\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$.
  - $\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$.
  - $\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$ (divide numerator and denominator by $\cos\alpha\cos\beta$).
- **Proofs** (108):
  - (1) Rectangle with an inscribed right triangle, acute case: $AD=\sin(\alpha+\beta)=\cos\beta\sin\alpha+\sin\beta\cos\alpha$.
  - (2) General angles: unit-circle points $A(\cos\alpha,\sin\alpha)$, $B(\cos\beta,\sin\beta)$; $AB^2$ by the 餘弦定理 ($2-2\cos(\alpha-\beta)$) equals $AB^2$ by the distance formula ⇒ $\cos(\alpha-\beta)$. Check the degenerate cases α=β and α−β=180°. Derive the rest via $\sin(\alpha-\beta)=\cos[(90^\circ-\alpha)+\beta]$ and $\beta\to-\beta$.
  - (3) Area: △ABC split by the altitude ⇒ $\sin(\alpha+\beta)$.
- **Basic values**:
  - $\cos75^\circ=\sin15^\circ=\frac{\sqrt6-\sqrt2}4$; $\cos15^\circ=\sin105^\circ=\frac{\sqrt6+\sqrt2}4$; $\tan75^\circ=2+\sqrt3$.
  - $\sin73^\circ\cos13^\circ-\cos73^\circ\sin13^\circ=\frac{\sqrt3}2$.
  - $\cos44^\circ\sin164^\circ-\sin224^\circ\cos344^\circ=\sin60^\circ$.
  - $\cos(\alpha+30^\circ)\cos(\alpha-60^\circ)+\sin(\alpha+30^\circ)\sin(\alpha-60^\circ)=\cos90^\circ=0$.
  - $\frac{\tan72^\circ-\tan12^\circ}{1+\tan72^\circ\tan12^\circ}=\sqrt3$.
  - $\tan12^\circ+\tan48^\circ+\sqrt3\tan12^\circ\tan48^\circ=\sqrt3$; $\sqrt3\cot20^\circ\cot40^\circ-\cot20^\circ-\cot40^\circ=\sqrt3$.
  - $\sin(\theta+60^\circ)\cos(\theta-60^\circ)-\cos(\theta+60^\circ)\sin(\theta-60^\circ)=\sin120^\circ$.
  - $\sum\frac{\sin(A-B)}{\sin A\sin B}=\sum(\cot B-\cot A)=0$.
- **Quadrant work**:
  - α in I with $\cos\alpha=\frac5{13}$, β in II with $\sin\beta=\frac45$ ⇒ $\sin(\alpha+\beta)=-\frac{16}{65}$, $\cos(\alpha-\beta)=\frac{33}{65}$.
  - α in II with $\cos=-\frac35$, β in IV with $\sin=-\frac8{17}$ ⇒ $\sin(\alpha-\beta)=\frac{36}{85}$, $\cos(\alpha-\beta)=-\frac{77}{85}$.
  - $\sec\alpha=\frac53$ (IV), $\cot\beta=\frac8{15}$ (III) ⇒ $\sin(\alpha+\beta)=-\frac{13}{85}$.
  - α, β in II with $\sin\alpha=\frac1{\sqrt5}$, $\cos\beta=-\frac3{\sqrt{10}}$ ⇒ $\sin(\alpha+\beta)=-\frac{\sqrt2}2$, $\cos=\frac{\sqrt2}2$ ⇒ $\alpha+\beta=\frac{7\pi}4$.
  - θ in II with $\sin\theta=\frac45$ ⇒ $\cos(\theta+\frac\pi3)=\frac{-3-4\sqrt3}{10}$.
  - $\sin84^\circ=a$, $\cos63^\circ=b$ ⇒ $\cos21^\circ=b\sqrt{1-a^2}+a\sqrt{1-b^2}$, $\sin21^\circ=ab-\sqrt{1-a^2}\sqrt{1-b^2}$, $\sin147^\circ=ab+\sqrt{1-a^2}\sqrt{1-b^2}$ → (A)(B)(C).
  - **Rotating a point**: P(−3/5, 4/5) on the unit circle and ∠QOP=60° (clockwise to Q) ⇒ $Q=(\cos(\alpha-60^\circ),\sin(\alpha-60^\circ))=(\frac{-3+4\sqrt3}{10},\frac{4+3\sqrt3}{10})$.
  - $\cos\alpha=\frac{11}{61}$, $\sin\beta=\frac45$ (acute) ⇒ $\cos(\alpha-\beta)=\frac{273}{305}$, $\sin^2\frac{\alpha-\beta}2=\frac{16}{305}$, $\cos^2\frac{\alpha+\beta}2=\frac{49}{305}$.
  - $\cos A=\frac{13}{14}$, $\cos B=-\frac17$ ⇒ $\cos C=-\cos(A+B)=\frac12$ ⇒ C=60°.
- **Finding an angle from tan**:
  - $\tan\alpha=\frac13$, $\tan\beta=-2$ (α in I, β in II) ⇒ $\tan(\alpha+\beta)=-1$ ⇒ 135°.
  - $\tan\alpha=2$, $\tan\beta=-3$ (α in III, β in II) ⇒ $\tan(\alpha-\beta)=-1$, $\alpha-\beta=135^\circ$.
  - $\tan A=2$, $\tan B=4$, $\tan C=13$ (all acute) ⇒ $\tan(A+B)=-\frac67$, $A+B+C=225^\circ$.
  - $\tan\alpha,\tan\beta,\tan\gamma,\tan\delta=\frac13,\frac15,\frac17,\frac18$ ⇒ sum $=45^\circ$.
  - $\tan\alpha=1$, $\tan(\alpha-\beta)=\frac1{\sqrt3}$ ⇒ $\tan\beta=2-\sqrt3$.
  - Rectangle 1×3 split into unit squares: $\theta+\varphi=45^\circ$.
- **Roots of a quadratic as tangents**:
  - $\tan\alpha,\tan\beta$ roots of $2x^2-4x+1$ ⇒ $\tan(\alpha+\beta)=4$ ⇒ $\cos^2(\alpha+\beta)=\frac1{17}$; $2\sin^2-4\sin\cos+4\cos^2=\cos^2(2t^2-4t+4)=\frac{20}{17}$.
  - Roots of $x^2+px+q$ ⇒ $\tan(\alpha+\beta)=\frac{-p}{1-q}$; $\sin^2+p\sin\cos+q\cos^2=q$.
  - Roots of $x^2-px+q$ ⇒ $\frac{\cos(\alpha-\beta)}{\sin(\alpha+\beta)}=\frac{1+q}p$.
- **Triangle identity**: $A+B+C=\pi$ ⇒ $\tan A+\tan B+\tan C=\tan A\tan B\tan C$ (acute ⇒ product ≥ $3\sqrt3$ by AM–GM) and $\sum\cot A\cot B=1$.
- **Angle between lines** $\tan\theta=\left|\frac{m_1-m_2}{1+m_1m_2}\right|$:
  - $y=7x-8$ and $y=\frac34x-1$ ⇒ 1 ⇒ 45°/135°.
  - Slopes 3 and $\frac12$ ⇒ 45°.
  - $y=3x+1$ and $y=2x+3$ ⇒ $\frac17$.
  - $y=-2x+5$ and $y=3x+1$ ⇒ 45°.
  - Slopes $\frac12$ and −3 ⇒ $\tan\theta=\pm7$, $\sin\theta=\frac{7\sqrt2}{10}$.
  - $x+y+3=0$ and $\sqrt3x+y-1=0$ ⇒ $\pm(2-\sqrt3)$.
  - Lines at 45° to $y=2x+6$: $\left|\frac{m-2}{1+2m}\right|=1$ ⇒ $m=-3$ or $\frac13$.
  - A(2,4), B(3,1) ⇒ $\tan\angle AOB=1$.
- **Splitting an angle into a difference** (find tan of each part from right triangles):
  - $AD:BD:CD=6:2:3$ ⇒ $\tan(\angle BAD+\angle CAD)=\frac{1/3+1/2}{1-1/6}=1$ ⇒ ∠BAC=45°.
  - Isosceles right triangle with D, E trisecting BC ⇒ $\tan\angle DAE=\frac{2/3-1/3}{1+2/9}=\frac3{11}$; right triangle with CD=BD=1, AC=3 ⇒ $\tan\theta=\frac3{11}$ (A).
  - Rectangle AB=2, BC=7, BE=3 ⇒ $\tan\angle AED=-\tan(\angle AEB+\angle DEC)=-\frac74$. (The 資優20 key prints $-\frac{17}6$; recomputation gives $-\frac74$, matching 108.)
  - BD=DE=EC=½AB ⇒ $\tan\angle DAE=\frac13$, $\cos\angle EAC=\frac5{\sqrt{26}}$.
  - **Football**: field width 65.88, goal 7.32, shot from the touchline 36.6 m from the goal line ⇒ $\tan\theta=\frac{1-0.8}{1+0.8}=\frac19$.
  - BC=5AH, B+C=45° ⇒ $BH:HC=3:2$.
  - Circle r=14, P with distances 13 and 11 to OA and OB ⇒ $\cos\angle AOB=\frac{3\sqrt3}{14}\cdot\frac{5\sqrt3}{14}-\frac{13}{14}\cdot\frac{11}{14}=-\frac12$ ⇒ 120°; shaded area $\frac{196\pi}3-47\sqrt3$.
  - Quadrilateral AB=16, BC=25, CD=15, $\sin B=\frac{24}{25}$, $\sin C=\frac45$ ⇒ BD=20, AD=12.
  - AB=7, AC=10, BD:DC=3:2, $\sin\angle BAD=\frac35$ ⇒ $\cos A=\frac35$, $BC=\sqrt{65}$.
  - Point P inside ∠XOY with feet A, B ⇒ $\tan\frac\theta2=\frac{PA+PB}{OA+OB}$.
  - Two congruent right triangles (AC=4, BD=3) ⇒ distance from C to AD is $\frac{96}{25}$.
- **Triangle applications** (with 正/餘弦定理):
  - **2010指定甲**: AB=5, $\cos B=-\frac35$, $R=\frac{13}2$ ⇒ $\sin C=\frac5{13}$ ⇒ $\sin A=\sin(B+C)=\frac{33}{65}$.
  - $\tan B=\frac34$, $\cos C=\frac1{\sqrt5}$, BC=22 ⇒ $\sin A=\frac{11\sqrt5}{25}$, $R=5\sqrt5$.
  - Circumradius 8 with distances 2 and 7 from O to AB and BC ⇒ $\sin\angle ABC=\sin(\angle OBA+\angle OBC)=\frac{\sqrt{15}}4$.
- 是非 traps: $\cos(\alpha+\beta)\ne\cos\alpha+\cos\beta$; $\cos120^\circ\ne\frac{\cos240^\circ}2$; ✓ $\sin12^\circ=2\sin6^\circ\cos6^\circ$; ✓ $\sin5\theta=\sin3\theta\cos2\theta+\cos3\theta\sin2\theta$.

### 14.2 倍角、半角、三倍角
- **二倍角**:
  - $\sin2\alpha=2\sin\alpha\cos\alpha$.
  - $\cos2\alpha=\cos^2\alpha-\sin^2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$.
  - $\tan2\alpha=\frac{2\tan\alpha}{1-\tan^2\alpha}$.
  - **In terms of tan**: $\sin2\theta=\frac{2t}{1+t^2}$, $\cos2\theta=\frac{1-t^2}{1+t^2}$.
- **半角 / 降次**: $\cos^2\frac\theta2=\frac{1+\cos\theta}2$, $\sin^2\frac\theta2=\frac{1-\cos\theta}2$. The sign comes from the quadrant of $\frac\theta2$. Also $\sin\theta\cos\theta=\frac12\sin2\theta$.
- **三倍角** (derive from $2\theta+\theta$): $\sin3\theta=3\sin\theta-4\sin^3\theta$, $\cos3\theta=4\cos^3\theta-3\cos\theta$.
- **Useful identities**:
  - $(\sin\theta\pm\cos\theta)^2=1\pm\sin2\theta$.
  - $\sin^4+\cos^4=1-\frac12\sin^22\theta$; $\sin^6+\cos^6=1-\frac34\sin^22\theta$ (range $[\frac14,1]$).
  - $\tan\theta+\cot\theta=\frac2{\sin2\theta}$.
  - $\cos^4\theta-\sin^4\theta=\cos2\theta$.
- 例 (double and half angle):
  - θ in III with $\cos=-\frac35$ ⇒ $\sin2\theta=\frac{24}{25}$, $\cos2\theta=-\frac7{25}$, $\tan2\theta=-\frac{24}7$.
  - $\tan\theta=-\frac34$ in IV ⇒ $\cos2\theta=\frac7{25}$, $\tan2\theta=-\frac{24}7$, $\sin\frac\theta2=\frac1{\sqrt{10}}$, $\cos\frac\theta2=-\frac3{\sqrt{10}}$.
  - $\tan\theta=-2$ in II ⇒ $\sin2\theta=-\frac45$, $\cos2\theta=-\frac35$, $\tan2\theta=\frac43$.
  - $\sin\theta=\frac35$ in II ⇒ $\sin2\theta=-\frac{24}{25}$, $\sin\frac\theta2=\frac3{\sqrt{10}}$, $\sin3\theta=\frac{117}{125}$.
  - $\tan\theta=\frac34$ in III ⇒ $\sin\frac\theta2=\frac3{\sqrt{10}}$, $\cos\frac\theta2=-\frac1{\sqrt{10}}$.
  - $\tan\theta=\frac43$ in III ⇒ $\sin\frac\theta2=\frac2{\sqrt5}$, $\cos\frac\theta2=-\frac1{\sqrt5}$.
  - $\cos\theta=\frac35$ in IV ⇒ $\sin3\theta=-\frac{44}{125}$, $\cos\frac\theta2=-\frac2{\sqrt5}$.
  - $\sin\theta=\frac45$ acute ⇒ $\cos3\theta=-\frac{117}{125}$.
  - $\cos2\alpha=\frac13$ (α in II) ⇒ $\cos\alpha=-\frac{\sqrt6}3$, $\tan\alpha=-\frac{\sqrt2}2$, $\cos^4\frac\alpha2+\sin^4\frac\alpha2=1-\frac12\sin^2\alpha=\frac56$.
  - $\cos\theta=\frac23$ ⇒ $\cos2\theta=-\frac19$.
  - $\frac\pi8$: $\sin=\frac{\sqrt{2-\sqrt2}}2$, $\cos=\frac{\sqrt{2+\sqrt2}}2$, $\tan=\sqrt2-1$; also $\cos11.25^\circ=\frac{\sqrt{2+\sqrt{2+\sqrt2}}}2$.
  - Regular octagon with R=1: inradius $\cos22.5^\circ$, perimeter $16\sin22.5^\circ=8\sqrt{2-\sqrt2}$. 16-gon: area $8\sin\frac\pi8=4\sqrt{2-\sqrt2}$, perimeter $32\sin\frac\pi{16}$.
  - $\tan\frac\theta2=x$ ⇒ $\cos2\theta=\frac{1-6x^2+x^4}{(1+x^2)^2}$.
  - $\sin\theta+\cos\theta=\sqrt2$ ⇒ $\tan\frac\theta2=\sqrt2-1$.
- **Homogeneous equations**:
  - $3\sin^2\theta-\sin\theta\cos\theta-2\cos^2\theta=0$ (II) ⇒ $\tan=-\frac23$ ⇒ $\sin2\theta+\cos2\theta=-\frac7{13}$.
  - $\sin x=3\cos x$ ⇒ $\cos2x=-\frac45$, $\sin2x=\frac35$.
  - $3\sin2\theta+2\cos2\theta=3$ ⇒ $5t^2-6t+1=0$ ⇒ $\tan\theta=1$ or $\frac15$.
- **$\sin2\theta$ given, find the rest**:
  - $\sin2\theta=-\frac35$ with $\frac\pi2<\theta<\frac{3\pi}4$ ⇒ $\sin\theta-\cos\theta=\frac{2\sqrt{10}}5$, $\cos^4-\sin^4=\cos2\theta=-\frac45$, $\tan+\cot=-\frac{10}3$, $\sin^6+\cos^6=\frac{73}{100}$.
    - The 108 version uses 270°<θ<360°, which allows two values of cos 2θ; its key takes −4/5.
  - $\sin\theta+\cos\theta=\frac14$ ($|\theta|<\frac\pi2$) ⇒ $\sin2\theta=-\frac{15}{16}$, $\cos2\theta=\frac{\sqrt{31}}{16}$, $s^3+c^3=\frac{47}{128}$.
  - $\frac{5\pi}4<\theta<\frac{3\pi}2$, $\sin2\theta=a$ ⇒ $\sin\theta-\cos\theta=-\sqrt{1-a}$.
  - $\cos2\theta=t$ ⇒ $4(\cos^6\theta-\sin^6\theta)=t^3+3t$.
  - Root $2+\sqrt3$ of $x^2-(\tan+\cot)x+1=0$ ⇒ sum 4 ⇒ $\sin2\theta=\frac12$.
- **Geometry with double angles**:
  - **2010學測**: AB=2, BC=3, A=2C ⇒ $\frac3{\sin2C}=\frac2{\sin C}$ ⇒ $\cos C=\frac34$ ⇒ $AC=\frac52$ (reject 2).
  - **2010學測**: ∠A=90°, BC=6, AB=5, ∠ABD=2∠ABC ⇒ $\cos2\theta=\frac7{18}$ ⇒ $BD=\frac{90}7$.
  - ∠B=90°, AC=3AB, AD bisects ∠A ⇒ $\cos2\theta=\frac13$ ⇒ $\sin\theta=\frac1{\sqrt3}$.
  - AB=3, BC=6, CA=7 with the bisector of ∠B meeting the circumcircle at P ⇒ $\cos B=-\frac19$, $\sin\frac B2=\frac{\sqrt5}3$, $PC=\frac{21}4$.
  - AB=3, AC=6, AD=2 with ∠BAD=θ, ∠DAC=2θ ⇒ $3\sin3\theta=\sin\theta+2\sin2\theta$ ⇒ $3\cos^2\theta-\cos\theta-1=0$ ⇒ $\cos\theta=\frac{1+\sqrt{13}}6$.
  - Cyclic quadrilateral with R=65/8, perimeter 44, BC=CD=13 ⇒ AB, AD = 4 and 16.
  - Angle bisector length $\frac{2bc\cos\frac A2}{b+c}$.
  - Parallelogram's angle bisectors bound a rectangle of area $\frac12(b-a)^2\sin\alpha$.
  - $\sin^2\frac A2=\frac{(s-b)(s-c)}{bc}$.
  - Directed angle with AB=5, BC=12 ⇒ $\sin\frac\theta2=\frac5{\sqrt{26}}$, $\cos\frac\theta2=\frac1{\sqrt{26}}$. AB=3, BC=4 ⇒ $\sin2\theta=-\frac{24}{25}$. AB=2, BC=5 ⇒ $-\frac{20}{29}$.
  - **2018學測**: AB=5, circle about A of radius r, tangent from B at P ⇒ $[PAB]=\frac{25}4\sin2\theta\le\frac{25}4$.
  - Square ABCD with ∠EDA=∠FAB=…=θ forming an inner square of side cosθ−sinθ; half the area ⇒ θ=15°.
- **Regular pentagon / golden ratio**:
  - $\sin18^\circ=\frac{\sqrt5-1}4$ (from $\sin36^\circ=\cos54^\circ$, i.e. $2\sin18^\circ\cos18^\circ=4\cos^318^\circ-3\cos18^\circ$ ⇒ $4s^2+2s-1=0$).
  - $\sin54^\circ=\cos36^\circ=\frac{\sqrt5+1}4$.
  - Diagonal:side $=2\sin54^\circ=\frac{1+\sqrt5}2$.
  - Pentagram inscribed in a circle with AC=1 ⇒ $R=\frac1{2\sin72^\circ}$.
  - 正八角星 (big star whose vertices are the centres of 8 small stars; adjacent small stars share vertex C, the midpoint of AB): $a:b=\sin22.5^\circ=\frac{\sqrt{2-\sqrt2}}2$.
- **Products of cosines** (multiply by $2\sin$ of the smallest angle repeatedly):
  - $\cos20^\circ\cos40^\circ\cos80^\circ=\frac18$.
  - $\cos\frac\pi7\cos\frac{3\pi}7\cos\frac{5\pi}7=-\frac18$.
  - $\cos\frac\pi{15}\cos\frac{2\pi}{15}\cos\frac{4\pi}{15}\cos\frac{8\pi}{15}=-\frac1{16}$.
  - $\cos\frac\pi9\cos\frac{2\pi}9\cos\frac{3\pi}9\cos\frac{4\pi}9=\frac1{16}$.
  - $\sin20^\circ\sin40^\circ\sin80^\circ=\frac{\sqrt3}8$.
  - Sums: $\cos\frac\pi7+\cos\frac{3\pi}7+\cos\frac{5\pi}7=\frac12$; $\sum_{k\ odd<11}\cos\frac{k\pi}{11}=\frac12$.
  - $\sum\sin^4\frac{k\pi}8$ (k=1,3,5,7) $=\frac32$; $\sum\cos^4$ (same) $=\frac32$.
- **Cubic equations via triple angle**:
  - $8x^3-6x+1=0$ ⇔ $\sin3\theta=\frac12$ ⇒ roots sin10°, sin130°, sin250° (A)(C)(E); sin 10° is irrational because the cubic has no rational root.
  - $4x^3-3x+1$ divided by $x-\sin20^\circ$ leaves $1-\frac{\sqrt3}2$.
  - $3x-4x^3$ divided by $x-\cos40^\circ$ leaves $-\cos120^\circ=\frac12$.
  - Isosceles apex 20°, legs 1, base $b=2\sin10^\circ$ ⇒ $b^3-3b=-1$.
  - $2x^2+ax-1=0$ with root $\sin30^\circ+\cos30^\circ$ ⇒ a=−2.
- **Graph intersections**:
  - sin x = sin 2x on (0,2π) ⇒ x = π/3, π, 5π/3.
  - cos x = cos 2x on [0,2π] ⇒ x = 0, 2π/3, 4π/3, 2π.
  - **2011學測**: $\sin\theta=-\frac23$, $\cos\theta>0$ ⇒ tan θ<0 ✓; $\tan^2\theta=\frac45>\frac49$ ✓; sin 2θ<0<cos 2θ; θ and 2θ both in IV → (1)(2).
  - **2018學測**: $\cos(3\theta-60^\circ)$, $\cos3\theta$, $\cos(3\theta+60^\circ)$ in AP ⇒ $2\cos3\theta=2\cos3\theta\cos60^\circ$ ⇒ $\cos3\theta=0$ ⇒ θ = 30°, 90°, 150° → (3).
- Simplify $\sqrt{1+\cos x}+\sqrt{1-\cos x}$ for $\pi<x<2\pi$: $=\sqrt2(\sin\frac x2-\cos\frac x2)$. $\sqrt{1+\sin\alpha}-\sqrt{1-\sin\alpha}=2\sin\frac\alpha2$ for $0<\alpha<\frac\pi2$.
- **Sums of unit vectors**:
  - $\sum\cos=\sum\sin=0$ for three angles ⇒ $\cos(\alpha-\beta)=-\frac12$.
  - $\cos\alpha+\cos\beta=\frac12$, $\sin\alpha-\sin\beta=\frac13$ ⇒ $\cos(\alpha+\beta)=-\frac{59}{72}$, $\cos(\alpha-\beta)=\frac5{13}$.
  - $\cos x+\cos y=a$, $\sin x+\sin y=b$ ⇒ $\cos(x-y)=\frac{a^2+b^2-2}2$.
  - $\sin\alpha+\sin\beta=1$, $\cos\alpha+\cos\beta=0$ ⇒ $\cos2\alpha+\cos2\beta=1$.
  - **$\tan\frac x2=t$ substitution**: $a\cos x+b\sin x+c=0$ ⇒ $(c-a)t^2+2bt+(a+c)=0$; two roots in $(-\pi,\pi)$ need $a^2+b^2\ge c^2$; $\tan\frac{\alpha+\beta}2=\frac ba$.

### 14.3 正餘弦疊合 $a\sin x+b\cos x$
- **Motivation**: superposing equal-period waves $A\sin\omega t+B\sin(\omega t+\alpha)=(A+B\cos\alpha)\sin\omega t+(B\sin\alpha)\cos\omega t$.
- **簡諧運動** (spring): $T=2\pi\sqrt{\frac mk}$. k=2, m=18 ⇒ T=6π; start at $\frac{y_0}2$ ⇒ $y=y_0\sin(\frac t3+\frac\pi6)$.
- **Formula**: $a\sin x+b\cos x=\sqrt{a^2+b^2}\sin(x+\alpha)$, where $\cos\alpha=\frac a{\sqrt{a^2+b^2}}$ and $\sin\alpha=\frac b{\sqrt{a^2+b^2}}$ (α is the direction angle of the point (a, b)). The cosine form works the same way.
  - Same period 2π; amplitude $\sqrt{a^2+b^2}$; range $[-\sqrt{a^2+b^2},\sqrt{a^2+b^2}]$.
  - Geometric proof: the rectangle construction gives $\sqrt{a^2+b^2}\sin(x+\theta)$.
- 例 (rewriting):
  - $\sin x+\cos x=\sqrt2\sin(x+\frac\pi4)$.
  - $\sin x-\sqrt3\cos x=2\cos(x+\frac{7\pi}6)=2\sin(x-\frac\pi3)=2\cos(x-\frac{5\pi}6)$; $\cos x-\sqrt3\sin x=2\cos(x+\frac\pi3)$.
  - $\sqrt3\sin x+\cos x=2\cos(x-\frac\pi3)$.
  - $-\sin x-\cos x=\sqrt2\sin(x+\frac{5\pi}4)$.
  - $3\sin x-\sqrt3\cos x=2\sqrt3\sin(x-\frac\pi6)$.
  - $\sin x-\cos x=\sqrt2\sin(x+\frac{7\pi}4)$ (a right shift by $\frac\pi4$ plus a ×√2 stretch, so 「向左平移」 is ✗).
  - $3\sin x+\cos x=\sqrt{10}\sin(x+\alpha)$; $2\sin x-\cos x=\sqrt5\sin(x+\alpha)$; $2\sin x-3\cos x=\sqrt{13}\sin(x+\alpha)$ with α in IV.
  - $\sin(\frac\pi6-2x)+\cos2x=\sqrt3\sin(2x+\frac{2\pi}3)$.
- **Max/min** (never add the separate maxima: $\sin x+\sqrt3\cos x$ has max 2, not $1+\sqrt3$):
  - $\sqrt3\cos x-\sin x+1=2\cos(x+\frac\pi6)+1$: on ℝ, 3 and −1; on $[\frac\pi6,\pi]$, 2 and −1.
  - $3\sin x+4\cos x+10$ on $[0,\frac\pi2]$: max 15 at $\tan x=\frac34$. $5\sin x+12\cos x$: max 13 at $\tan x=\frac5{12}$. $12\cos x+5\sin x$: min when $\cos x=-\frac{12}{13}$.
  - Ranges: $\sin x+2\cos x$ ±√5; $-\sqrt3\sin x+\cos x$ ±2; $3\sin x-4\cos x$ ±5; $-\sqrt6\sin x-\sqrt2\cos x$ ±2√2; $12\sin x-5\cos x$ ±13 on ℝ, and 12 / −5 on [0,π]; $-40\sin x+9\cos x$ ±41.
  - On [0,π]: $\sin x-\sqrt3\cos x$ → 2, −√3; $-\sin x+\cos x$ → 1, −√2; $\cos x-\sqrt3\sin x$ → max 1 at x=0, min −2 at $x=\frac{2\pi}3$.
  - $\sqrt3\sin(x-\frac\pi6)-\sin x=\sin(x-\frac\pi3)$: on [0,2π] max 1 at $\frac{5\pi}6$, min −1 at $\frac{11\pi}6$; on [0,π] min $-\frac{\sqrt3}2$ at 0.
  - $2\sin(x-\frac\pi6)+2\cos x+5=2\sin(x+\frac\pi6)+5$ ⇒ 7 and 3; same for $2\cos x+2\sin y+5$ with $x-y=\frac\pi6$.
  - $\sin(x+\frac\pi4)+\sin(x-\frac\pi4)=\sqrt2\sin x$ ⇒ ±√2. $2\sin x+2\sin(x+\frac\pi2)$ ⇒ ±2√2.
  - $x+y=\frac{2\pi}3$ ⇒ $\sin x+2\sin y=2\sin x+\sqrt3\cos x$ ⇒ max √7.
- **Even-degree expressions** $a\sin^2x+b\sin x\cos x+c\cos^2x+d$: reduce the degree ⇒ $\frac b2\sin2x+\frac{c-a}2\cos2x+\frac{a+c}2+d$, then combine.
  - $3\sin^2x+4\sqrt3\sin x\cos x-\cos^2x=4\sin(2x-\frac\pi6)+1$: on [0,π], max 5 at $\frac\pi3$, min −3 at $\frac{5\pi}6$; on $[\frac\pi{12},\frac{3\pi}4]$, max 5 at $\frac\pi3$, min $1-2\sqrt3$ at $\frac{3\pi}4$.
  - $\sin^2x+\sin x\cos x+2\cos^2x$ on $[0,\frac\pi2]$ ⇒ max $\frac{3+\sqrt2}2$, min 1.
- **Quadratic in one function** (substitute and respect the range):
  - $y=\cos^2x-3\cos x+3$ ⇒ max 7 (cos=−1), min 1 (cos=1).
  - $2\sin^2x-3\cos x+1$: on [0,2π] max $\frac{33}8$ (cos=−¾), min −2; on $[0,\frac\pi3]$ max 1, min −2.
  - $\cos^2x-4\sin x-3$ on $[\frac\pi6,\frac{7\pi}6]$ ⇒ min −7 at $\frac\pi2$, max $-\frac14$ at $\frac{7\pi}6$.
- **Substitution $t=\sin\theta+\cos\theta\in[-\sqrt2,\sqrt2]$** with $\sin\theta\cos\theta=\frac{t^2-1}2$:
  - $f=sc+s+c+1=\frac12(t+1)^2$ ⇒ on ℝ max $\frac32+\sqrt2$, min 0; on $[\frac\pi4,\frac\pi2]$ ($1\le t\le\sqrt2$) max $\frac32+\sqrt2$, min 2.
  - $1+\sin x+\cos x-\sin x\cos x=\frac{4-(t-1)^2}2$ ⇒ max 2 (x=0, π/2, 2π), min $\frac12-\sqrt2$ at 225°, sum $\frac52-\sqrt2$ → (A)(C)(D)(E).
- **Range of rational trig functions via $|a\sin x+b\cos x|\le\sqrt{a^2+b^2}$**:
  - $y=\frac{1+\sin x}{3+\cos x}$ ⇒ $\sin x-y\cos x=3y-1$ ⇒ $|3y-1|\le\sqrt{1+y^2}$ ⇒ $0\le y\le\frac34$.
  - $\frac{3-\sin x}{2+\cos x}=5$ ⇔ $\sin x+5\cos x=-7$, impossible since $7>\sqrt{26}$; the range of $y=\frac{3-\sin x}{2+\cos x}$ comes from $|3-2y|\le\sqrt{1+y^2}$ ⇒ $3y^2-12y+8\le0$ ⇒ $\frac{6-2\sqrt3}3\le y\le\frac{6+2\sqrt3}3$.
- **Geometric optimisation**:
  - Brick leaning on a wall (AB=2√3, BC=2): height of C is $2\sqrt3\sin x+2\cos x=4\sin(x+\frac\pi6)$; =2√3 ⇒ $x=\frac\pi6$; =2√2 ⇒ $x=\frac\pi{12}$.
  - Semicircle (diameter 6): $3AP+4BP=18\cos\theta+24\sin\theta\le30$; diameter 10 ⇒ 50; diameter 2 ⇒ 10.
  - Rectangle inscribed in a circle of radius r: perimeter $4r(\sin\theta+\cos\theta)\le4\sqrt2r$.
  - Rectangle 3×7 inside PQRS: perimeter $20(\sin\alpha+\cos\alpha)$, max $20\sqrt2$ at 45°.
  - Squares A, B with areas summing to 1: $[MNL]=\frac12\cos\theta(\sin\theta-\cos\theta)\le\frac{\sqrt2-1}4$.
  - Quarter circle, $S=MN+ON=\cos^2\theta+\sin\theta\cos\theta=\frac12+\frac{\sqrt2}2\sin(2\theta+\frac\pi4)$ ⇒ max $\frac{1+\sqrt2}2$.
  - Sector π/3 with radius 1: quadrilateral PCOD has $\frac{\sqrt3}4\sin(2\theta+\frac\pi6)$ ⇒ max $\frac{\sqrt3}4$.
  - Unit circle, ∠CAB=60°, D on the lower arc: $S(\theta)=\cos\theta\sin(60^\circ+\theta)$ ⇒ max $\frac12+\frac{\sqrt3}4$ at $\theta=\frac\pi{12}$.
  - T-shaped bridge in a pond of radius 50 ⇒ max total $50+50\sqrt5$.
  - Right triangle with hypotenuse 6 ⇒ max perimeter $6+6\sqrt2$.
  - Direction vector: $2\sin\theta+4\cos\theta=\vec{OP}\cdot\vec{OA}$ with A(4,2); on $[0,\frac\pi2]$ max $2\sqrt5$, min 2.
- **Equations**:
  - $\sin x-\sqrt3\cos x=1$ on [0,2π] ⇒ $\frac\pi2$, $\frac{7\pi}6$.
  - $\sin x-\cos x=1$ on [0,2π) ⇒ $\frac\pi2$, π.
  - $\sqrt3\cos x-\sin x=1$ on $(-\frac\pi2,\frac\pi2)$ ⇒ $\frac\pi6$.
  - **93學測**: $\sqrt3\sin A+\cos A=2\sin2004^\circ$ with 270° < A < 360° ⇒ $\sin(A+30^\circ)=\sin204^\circ$ ⇒ A=306°. (2012-version: ⇒ 298°.)
  - $\sin x+2\cos x=k$ with two roots on $[0,\frac\pi2]$ ⇔ $2\le k<\sqrt5$.
  - $\frac{\sqrt3}{\sin20^\circ}-\frac1{\cos20^\circ}=4$.
- **Inequalities** (from the carry list):
  - $\sin x>\cos x$ ⇔ $\sqrt2\sin(x-\frac\pi4)>0$ ⇔ $\frac\pi4<x<\frac{5\pi}4$.
  - $\sin x-\sqrt3\cos x\ge1$ on [0,2π] ⇔ $\sin(x-\frac\pi3)\ge\frac12$ ⇔ $\frac\pi2\le x\le\frac{7\pi}6$.
- **Graph statements**:
  - $f=\frac12(\sqrt3\sin x+\sqrt3\cos x)$: period 2π; meets the y-axis at $(0,\frac{\sqrt3}2)$ ✓; infinitely many x-intercepts ✓; not odd → (3)(4) / (C)(D).
  - $\sin x-\cos x$: period 2π, max √2 → (A)(D).
  - **92學科** functions with smallest period π: $|\sin x\pm\cos x|$ → (3)(4) (and $|\sin x|+|\cos x|$ has period π/2).
  - **2013指定甲** $f=|\sin x|+|\cos x|$: even ✓; max √2 ✓; min 1; increasing on $(0,\frac\pi4)$; period $\frac\pi2$ → (1)(2).
  - Matching graphs: $f=\sqrt3\sin x-\cos x$, $g=\sin2x+\sqrt3\cos2x$, $h=\sqrt2\sin x+\sqrt2\cos x$ by period and phase.
  - Reading $a\sin x+b\cos x=2\sin(x+\alpha)$ from a graph with max at $\frac{2\pi}3$ ⇒ $\alpha=-\frac\pi6$ ⇒ $a=\sqrt3$, b=−1.
- **Harmonic motion**: amplitude 5, period 3, start at B ⇒ $x=5\sin(\frac{2\pi}3t+\frac\pi2)$, $x(5)=-\frac52$. Pendulum $3\sin(\sqrt{g/l}\,t+c)$ with T=4.71 ⇒ l ≈ 5.5 m.
- **Circle parametrisation (99 數甲)**:
  - $x=h+r\cos\theta$, $y=k+r\sin\theta$; restricting θ gives arcs.
  - P on $x^2+y^2=4$ with A(6,0), B(0,8): area of △ABP from 14 to 34.
  - P on the unit circle with Q(3,−2): max area of △POQ is $\frac{\sqrt{13}}2$.
  - $x=1+\sin t$, $y=2+\cos t$ is a circle of length 2π.
  - Particle from $(\sqrt3,1)$ at 0.2 rad/s ⇒ $x=2\cos(\frac\pi6+0.2t)$.
  - (Ellipse parametrisation → §23.)

### 14.4 積化和差、和差化積 **[超出數A]** (99/資優)
- Product to sum:
  - $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$.
  - $2\cos\alpha\cos\beta=\cos(\alpha-\beta)+\cos(\alpha+\beta)$.
  - $2\sin\alpha\sin\beta=\cos(\alpha-\beta)-\cos(\alpha+\beta)$.
- Sum to product: $\sin x\pm\sin y$, $\cos x+\cos y=2\cos\frac{x+y}2\cos\frac{x-y}2$, $\cos x-\cos y=-2\sin\frac{x+y}2\sin\frac{x-y}2$.
- 例:
  - $\sin37.5^\circ\sin7.5^\circ=\frac{\sqrt3-\sqrt2}4$.
  - $\cos65^\circ\sin110^\circ+\cos25^\circ\sin20^\circ=\frac{\sqrt2}2$.
  - $\sin10^\circ-\sin110^\circ+\sin130^\circ=0$; $\cos80^\circ+\cos40^\circ-\cos20^\circ=0$.
  - $\sin^2\theta+\sin^2(\frac\pi3+\theta)+\sin^2(\frac\pi3-\theta)=\frac32$; the cosine version gives $\frac32$; $-\cos^2\theta+\cos^2(\frac\pi6+\theta)+\cos^2(\frac\pi6-\theta)=\frac12$.
  - $\sin(x+y)=\frac{33}{65}$, $\sin(x-y)=-\frac{63}{65}$ ⇒ $\cos x\sin y=\frac{48}{65}$; $\cos(x+y)=-\frac{48}{65}$, $\cos(x-y)=\frac{16}{65}$ ⇒ $\cos x\cos y=-\frac{16}{65}$.
  - $\frac{\sin5\theta+\sin\theta}{\cos5\theta+\cos\theta}=\tan3\theta$ ($\theta=\frac\pi8$ ⇒ $\sqrt2+1$; $\theta=\frac\pi{18}$ ⇒ $\frac1{\sqrt3}$).
  - $\frac{\sin55^\circ\sin35^\circ}{\cos80^\circ+\cos40^\circ}=\frac12$; $\frac{2\sin80^\circ-\cos70^\circ}{\cos20^\circ}=\sqrt3$.
  - **2002學科** $\frac12(\cos10x-\cos12x)=\sin11x\sin x$: $|f|\le1$; max not 1; min −1 at $x=\frac\pi2$; infinitely many zeros → (A)(B)(D)(E).
  - **91學科**: with altitude h from C and feet splitting AB into x, y, $\cos C=\frac{h^2-xy}{ab}$ (E).
  - Telescoping: $\sum\frac{\sin2^\circ}{\sin(2k-1)^\circ\sin(2k+1)^\circ}=\cot1^\circ-\cot(2n+1)^\circ$; $\sum_k\sin\frac\theta{2^k}\cos\frac{3\theta}{2^k}=\frac12(\sin2\theta-\sin\frac\theta{2^{n-1}})$.

### 14.5 反三角函數 **[超出數A]** (資優23)
- An inverse needs a 1−1 function, so restrict the domain.
  - $\sin^{-1}:[-1,1]\to[-\frac\pi2,\frac\pi2]$.
  - $\cos^{-1}:[-1,1]\to[0,\pi]$.
  - $\tan^{-1}:\mathbb R\to(-\frac\pi2,\frac\pi2)$.
- These are the calculator keys used in 108 (G-10-7) for 斜角 and angles, with quadrant adjustment (§12.4).
- $\cos^{-1}(\cos k)$ for k=1..6 gives 1, 2, 3, 2π−4, 2π−5, 2π−6; $\cos^{-1}\pi$ is undefined.

**Traps**:
- $\cos(\alpha-\beta)$ has a **plus**.
- Half-angle signs follow the quadrant of $\frac\theta2$, not of θ.
- In 疊合, α is determined by both cos α and sin α, not by tan α alone.
- Max of a sum is not the sum of the maxima.
- When θ is restricted, find the range of $x+\alpha$ first.
- Many 資優/99 keys drop denominators (e.g. $\frac{25}4$ printed as 25, $\frac12$ printed as 1); recompute.

## 15. 指數函數、對數與對數律、對數函數及應用

**Scope**:
- A-11A-4 對數律: from $10^x$ and the 指數律 to the log laws; used to solve 指數方程式; 認識一般底的對數 but 勿過度練習.
- F-11A-4 指數與對數函數:
  - 指數函數及其圖形; 按比例成長/衰退模型; 常用對數函數的圖形; 科學與金融應用.
  - Key idea: any base converts to 常用對數 ($\log_ab=\frac{\log b}{\log a}$), and any $a^x=10^{kx}$ with $k=\log a$.
  - **Do not mix different bases in one expression on purpose.**
- 學測 prints log 2, 3, 5, 7 values; no calculator.
- e, ln, 連續複利 are **數B (F-11B-2), [超出數A]** (108 mentions e only as enrichment).
- 10年級 material (指數推廣, 常用對數, 位數/首位數字) is in §3.
- 對數表/內插 and 首數尾數 are 99 legacy.

**Sources**: 108二上 2-1指數函數, 2-2對數與對數律, 2-3對數函數; 99第一冊 3-2指數函數, 3-4對數函數, 3-5指數與對數的應用 (and 3-3對數 via §3); 資優 第14單元指數與對數函數 (+ 資優13/54 carry notes).

### 15.1 指數型成長 vs 線型成長; 指數函數
- **Linear vs exponential**: equal x-steps give an AP of y-values (線型) or a GP (指數型). Test a data table:
  - 10, 20, 40, 80 and 100, 40, 16, 6.4 are exponential; 70, 40, 10, −20 and −4, 6, 16, 26 are linear.
  - 100, 120, 144 is exponential.
  - With x = −1, 1, 3, 5: 5, 20, 80, 320 / 5, 10, 20, 40 / 1000, 1300, 1690, 2197 are exponential; 1.5, 8.5, 15.5, 22.5 and −3.25, 2, 7.25, 12.5 are linear.
- **$f(x)=a^x$** ($a>0$, $a\ne1$):
  - Domain $\mathbb R$, range $(0,\infty)$; asymptote is the x-axis; passes through (0,1) and (1,a).
  - $a>1$ increasing; $0<a<1$ decreasing.
  - Every horizontal line $y=b>0$ meets it once.
  - $a^x$ and $a^{-x}=(\frac1a)^x$ are symmetric about the y-axis.
  - **凹口向上** (convex): $\frac{f(m)+f(n)}2\ge f(\frac{m+n}2)$.
  - $a^x=10^{x\log a}=2^{x\log_2a}$: every exponential graph is a horizontal stretch of $y=2^x$ (e.g. $10^x$ is $2^x$ shrunk by $\log2\approx0.3$; $3^x=10^{x\log3}$, i.e. $10^x$ stretched by $\frac1{\log3}$).
  - **$y=c\,a^x$** is a vertical stretch by c (c = initial value): $3(1.2)^x$ from $(1.2)^x$.
- Comparing bases from a graph:
  - At x=1 the heights are a, b, … (larger base is steeper for x>0).
  - Four curves $y=a^x..d^x$ ⇒ $b<a<1<d<c$.
  - Three curves ⇒ (1)(2)(4).
  - Match $2^x$, $3^x$, $(0.2)^x$, $(0.7)^x$: A=$(0.7)^x$, B=$(0.2)^x$, C=$3^x$, D=$2^x$.
- **Ordering numbers** (same base, then use monotonicity):
  - $(0.3)^{1/2}$ vs $(0.3)^{\dots}$ ⇒ $a>b>c$.
  - Smallest of $(0.9)^{-3.5},(0.9)^{-2.5},(0.9)^{-1.5},(0.9)^{-\sqrt3},(0.9)^{-\sqrt5}$ is $(0.9)^{-1.5}$ (C).
  - $\sqrt5$, $4^{2/3}$, $3^{3/4}$ ⇒ $b>c>a$.
  - $\sqrt2<\sqrt[3]4<\sqrt[4]8$ (powers of 2).
  - $(0.6)^{0.6}<1$.
  - **90學科**: $(\frac12)^{1/2}=(\frac14)^{1/4}>(\frac13)^{1/3}$ ⇒ $a=c>b$ (C).
  - **88學科**: smallest of $2^{1/3},(\frac18)^{-2},2^{-1/4},(\frac12)^{1/2},8^{-1/3}$ is $8^{-1/3}=\frac12$ (E).
- **Convexity**: convex functions are $3^x$, $(0.6)^x$, $3x^2$, $\log_{0.5}x$; concave are $-2^x$, $\log_2x$, and sin on (0,π). Which $f$ satisfy $f(\frac{x_1+x_2}2)<\frac{f(x_1)+f(x_2)}2$: $2^x$, $(\frac12)^x$, $2^x+2^{-x}$ (all).
- **Graph transformations**:
  - $3^{x-2}$ is $3^x$ shifted right 2.
  - $9\cdot3^x+3=3^{x+2}+3$ is $3^x$ shifted left 2 and up 3.
  - $1-3^x$ is reflected in the x-axis, then shifted up 1.
  - $2^{|x|}$, $(\frac12)^{|x|}$, $-(\frac12)^{|x|}$, $-2^{-x}$, $2^{|x|}+1$, $-2^{-|x|}$ are drawn by reflection.
- **Roots by graphs**:
  - $x^2=2^{-|x|}$ → 2.
  - $2^x+x=0$ → 1.
  - $x^2=(\frac12)^x$ → 3 (x = −2, −4 and one positive).
  - $x^2=2^x$ → 3 (2, 4 and one negative).
  - $|x|=2^{-|x|}$ → 2.
  - Which graph meets $x+y=0$ exactly once: $2^x$ and $-2^{-x}$ (A)(D).
  - **91學科**: $10^x=x$ has no root; $10^x=x^2$ has one negative root; $10^x>x$ for all x; $10^x>x^2$ for x>0; $10^x=-x$ has a root → (B)(C)(D)(E).
  - **87社**: which pictures can be part of $y=a^x$ → (A)(C).
- **2021學測**: square of side 4 centred at (1,1) meets $y=a\cdot2^x$ ⇔ $-2\le a\le6$ (through (−1,3) gives a=6; through (−1,−1) gives a=−2).
- Points A, B on $y=5^x$ at heights 2 and 10 ⇒ horizontal gap 1 ⇒ $AB=\sqrt{1+64}=\sqrt{65}$.
- On $[-2,2]$, $9^x-3^{x+1}$ ($t=3^x\in[\frac19,9]$) has max 54 at x=2.
- **Hyperbolic-type quotients** $f=\frac{a^x-a^{-x}}{a^x+a^{-x}}$ ⇒ $a^{2x}=\frac{1+f}{1-f}$:
  - $f(\alpha)=\frac13$, $f(\beta)=\frac25$ ⇒ $a^{2\alpha}=2$, $a^{2\beta}=\frac73$ ⇒ $f(2\alpha)=\frac35$, $f(\alpha+\beta)=\frac{11}{17}$.
  - $f=\frac{3^x+3^{-x}}{3^x-3^{-x}}$: $f(a)=\frac54$ ⇒ $9^a=9$ ⇒ a=1; $f(m)=\frac{13}{12}$ ⇒ $9^m=25$ ⇒ $m=\log_35$.
  - $f=\frac{2^x+2^{-x}}{2^x-2^{-x}}$ with $f(a)=2$, $f(b)=3$ ⇒ $4^a=3$, $4^b=2$ ⇒ $f(a+b)=\frac75$.
  - (資優) Inverse of $\frac{10^x-10^{-x}}2$ is $\log(x+\sqrt{x^2+1})$.
- An even function of x (graph symmetric about the y-axis) has roots in pairs ±α; in the handout's example $\alpha-\beta=\frac23$ gives $a=\frac{27}8$.

### 15.2 對數的定義、換底、對數律 (A-11A-4)
- **Definition**: for $a>0$, $a\ne1$, $b>0$: $b=a^t$ ⇔ $t=\log_ab$ (底數 a, 真數 b). Hence $a^{\log_ab}=b$, $\log_aa^t=t$, $\log_aa=1$, $\log_a1=0$. Motivation: $2^x=5$ has a unique root (the graph meets $y=5$ once), $x=\log_25=\frac{\log5}{\log2}$.
  - 例: $\log_2\frac18=-3$, $\log_927=\frac32$, $\log_5\frac1{\sqrt5}=-\frac12$, $\log_749=2$, $\log_{\frac13}9=-2$
  - $\log_x27=6$ ⇒ $x=\sqrt3$; $\log_7x=\frac32$ ⇒ $x=7\sqrt7$; $\log_x8\sqrt2=7$ ⇒ $x=\sqrt2$.
  - $\log_23=x$ ⇒ $4^x=9$, $2^{-x}=\frac13$; $\log_35=x$ ⇒ $9^x=25$, $3^{-2x}=\frac1{25}$.
  - $\log2=p$, $\log3=q$ ⇒ $10^{3p+2q+1}=8\cdot9\cdot10=720$.
- **換底公式**: $\log_ab=\frac{\log b}{\log a}=\frac{\log_cb}{\log_ca}$ (proof: write $a=10^{\log a}$, $b=10^{\log b}$). Consequences:
  - $\log_ab\cdot\log_ba=1$.
  - Chain rule $\log_ab\cdot\log_bc\cdot\log_cd=\log_ad$ ($\log_35\cdot\log_57\cdot\log_727=3$; $\log_4 5\cdot\log_54=1$).
  - $\log_{a^m}b^n=\frac nm\log_ab$; $\log_{\sqrt2}\sqrt[3]8$-type values follow at once.
  - $\log_{a^r}b^r=\log_ab$, so $\log_916+\log_32=\log_34+\log_32=\log_38$.
- **對數律** ($x,y>0$):
  - $\log_ax+\log_ay=\log_a(xy)$; $\log_ax-\log_ay=\log_a\frac xy$; $\log_ax^r=r\log_ax$.
  - Proved for log by $10^{\log x+\log y}=10^{\log x}10^{\log y}$, then via 換底 for any base.
  - **Not** laws: $\log(x+y)\ne\log x+\log y$ ($\log_6(3+4)\ne\log_63+\log_64$); $\log x^2=2\log|x|$, not $2\log x$ for negative x ($\log_7(-3)^2\ne2\log_7(-3)$).
- 例 (simplification):
  - $\log7+\log8-\log4=\log14$; $3\log k-2\log(k+1)+\log4=\log\frac{4k^3}{(k+1)^2}$.
  - $3\log2+\log5-2\log20=-1$; $\log4+\log25=2$; $\log2+\log0.2+\log5+\log0.5=0$.
  - $\log\frac{50}9-\log\frac3{70}+\log\frac{27}{35}=\log100=2$; $\log_354+\log_36-2\log_32=4$; $\log_{10}\frac47-\frac43\log8+\frac23\log343=0$.
  - $(\log_23+\log_49)(\log_34+\log_92)=5$; $(\log_25+\log_40.2)(\log_52+\log_{25}0.5)=1$.
  - $\log_3 5\cdot\log_5 7\cdot\log_7 27=3$; $\frac{\log_327}{\log_24}=\frac32$; $\log_23\cdot\log_35\cdot\log_564\cdot\log_749=6\cdot2=12$.
  - $\log_2 9\cdot\log_3 4\cdot\log_{1/4}8=2\cdot2\cdot(-\frac32)=-6$.
  - $5^{\log_56}=6$; $5^{2\log_56}=36$; $3^{\log_97}=\sqrt7$.
- **Express in a, b**:
  - $\log_23=a$, $\log_311=b$ ⇒ $\log_{66}44=\frac{2+ab}{1+a+ab}$, $\log_212=2+a$, $\log_{66}18=\frac{1+2a}{1+a+ab}$.
  - $a=\log2$, $b=\log3$ ⇒ $\log_624=\frac{3a+b}{a+b}$, $\log_2\sqrt3+\log_3\sqrt[3]2=\frac b{2a}+\frac a{3b}$, $\log_56=\frac{a+b}{1-a}$, $\log_{0.75}100=\frac2{b-2a}$, $\log_38=\frac{3a}b$, $\log_224=\frac{3a+b}a$.
- **Useful identity** $a^{\log b}=b^{\log a}$ (both equal $10^{\log a\log b}$).
- 是非 (108 習題):
  - $\log_6(3+4)=\log_63+\log_64$ ✗.
  - $2=9^{\log_92}$ ✓.
  - $3^x=7$ ⇒ $x=\log_37$, not $\log_73$.
  - $\log_{\frac15}3=-\log_53$ ✓.
  - $\log x^2=2\log x$ only for x>0.

### 15.3 對數函數 (F-11A-4)
- $f(x)=\log_ax$:
  - Domain $(0,\infty)$, range $\mathbb R$; asymptote is the y-axis; passes through (1,0).
  - $a>1$: increasing and **concave (凹口向下)**, $\log\frac{m+n}2>\frac{\log m+\log n}2$ by AM–GM.
  - $0<a<1$: decreasing and convex.
  - $\log_ax$ and $\log_{1/a}x$ are symmetric about the x-axis.
  - Every $\log_ax=\frac{\log_2x}{\log_2a}$ is a vertical stretch of $\log_2x$ (e.g. $\log x=\log2\cdot\log_2x$; conversely $\log_2x$ is $\log x$ stretched by $\frac1{\log2}\approx3.3$).
- **Inverse pair**: $y=a^x$ and $y=\log_ax$ swap inputs and outputs, so their graphs are **symmetric about $y=x$** ($(x_0,y_0)\leftrightarrow(y_0,x_0)$).
  - **2007學測** ($f=a^x$, $g=\log_ax$, a>1):
    - $f(3)=6$ ⇒ $g(36)=2g(6)=6$ ✓.
    - Any chord of g has positive slope ✓.
    - $y=5x$ meeting f twice ⇔ $y=\frac15x$ meeting g twice ✓.
  - 108 習題8 variant: $f(3)=5$ ⇒ $g(5)=3$ ✓; $\frac{f(27)}{f(22)}=a^5=\frac{f(11)}{f(6)}$ ✓; $\frac{g(27)}{g(22)}\ne\frac{g(11)}{g(6)}$ → (1)(2)(4)(5).
  - $\Gamma_1:\log_3x$, $\Gamma_2:3^x$: AP inputs give GP outputs ✓; symmetric about y=x ✓; $\log_3x$ is a vertical stretch of $\log_2x$ ✓; $y=\frac x4$ meets Γ₁ twice ⇔ $y=4x$ meets Γ₂ twice ✓; every chord of Γ₂ has positive slope ✓ → all five.
- **Reading graphs**:
  - $y=a\log x$ curves: a>0 when increasing; a larger when steeper at x=10 → (1)(2)(4).
  - $\log_ax$ and $\log_dx$ symmetric about the x-axis ⇒ $ad=1$; with $\log_b,\log_c$ also ⇒ $abcd=1$, $b>a>d>c$ → (C)(D)(E).
  - $y=\log_bax$ passing through ($\frac1a$,0) increasing ⇒ a>1, b>1 (A).
  - $y=a+\log_bx$ (88社) ⇒ a<0, 0<b<1 (E).
  - $\log_ax$ together with $(1-a)^x$ for 0<a<1 ⇒ (C).
  - Picking $-\log_2x$ among five curves.
- **Comparisons**:
  - $\log_35>\log_34>0>\log_30.3$; $\log_{0.2}0.5>0>\log_{0.2}4>\log_{0.2}8$.
  - Largest of $\log_53$, 1, $\log_30.5$, 0 is 1; largest of $\log_{0.5}0.4$, 1, $\log_{0.5}5$, 0 is $\log_{0.5}0.4$.
  - Smallest of the $\log_{1/3}$-type options (B).
  - $a=\log_23$, $b=\log_43$, $c=\log_{\sqrt2}3$, $d=\log_{0.5}3$ ⇒ $d<b<a<c$.
  - $2^x=3^y=5^z>1$ ⇒ $5z>2x>3y$ (compare $\frac2{\log2},\frac3{\log3},\frac5{\log5}$).
  - $a>b>1000$, $p=\sqrt{\log_7a\log_7b}$, $q=\frac12(\log_7a+\log_7b)=\log_7\sqrt{ab}$, $r=\log_7\frac{a+b}2$ ⇒ $p<q<r$ (A)(D).
- **Graph transformations**: $\log_2(-x)$, $-\log_2x$, $-\log_2(-x)$ (reflections); $|\log_2x|$; $\log_2|x|$; $2\log x$ vs $\log x^2$ ($x\ne0$, two branches).
  - Roots: $x^2+\log|x|=0$ → 2; $x-1=|\log_2x|$ → 2; $2^x=\log_{0.5}|x|$ → 2
- **2019指定甲**: A, B on $y=\log_2x$ with chord slope 2 and $AB=\sqrt5$ ⇒ $b-a=1$, $\log_2\frac ba=2$ ⇒ $(a,b)=(\frac13,\frac43)$.
- Lines x=3 and x=6 meet $y=\log_2x$ at points $\sqrt{10}$ apart.
- $f(x)=\log_3(\log_{0.3}(\log_9x))$: $f(3^{0.054})=1$; domain $1<x<9$.

### 15.4 指數與對數方程式
- **Method** (indices):
  - Same base ⇒ compare exponents.
  - Substitution $t=a^x>0$ (reject negative t).
  - Take logs: $a^x=b$ ⇒ $x=\log_ab=\frac{\log b}{\log a}$.
- **Method** (logs):
  - **First write the domain** (all 真數 > 0, bases > 0 and ≠ 1).
  - Combine with the laws, then remove the logs.
  - **Check the roots** against the domain.
- 指數方程式:
  - $3^{2x}-8\cdot3^x-9=0$ ⇒ x=2.
  - $3^{x-2}=15$ ⇒ $x=2+\log_315$.
  - $4^x+2^x-12=0$ ⇒ $x=\log_23$.
  - $9^x-3^{x+1}-10=0$ ⇒ $3^x=5$ ⇒ $x=\log_35$.
  - $4^{3x-1}=6$ ⇒ $x=\frac13(1+\log_46)$.
  - $5^{2x-1}=12$ ⇒ $x=\frac12(1+\log_512)\approx1.2720$.
  - $3^{2x}-4\cdot3^x-5=0$ ⇒ $\log_35\approx1.4650$.
  - $2^x=3$ ⇒ 1.5850.
  - $3\cdot2^x=5^x$ ⇒ $x=\log_{5/2}3$.
  - $4^x-2^{x+3}+15=0$ ⇒ $x=\log_23$ or $\log_25$.
  - $2^{2x}-7\cdot2^x+12=0$ ⇒ x=2 or $\log_23$.
  - $2^{x-1}+2^x=5^{x-1}+5^x$ ⇒ $(\frac52)^{x-1}=\frac12$.
  - $2^{10^x}=10^6$ ⇒ $10^x=\frac6{\log2}$ ⇒ $x=\log6-\log\log2\approx1.30$ (**2014指定甲** (3)).
- 對數方程式:
  - $\log_2(x-1)=5$ ⇒ 33.
  - $\log_6x+\log_6(x-1)=1$ ⇒ x=3 (−2 rejected).
  - $\log x+\log(x-3)=1$ ⇒ x=5 (−2 rejected); this is equivalent to "x>3 and x(x−3)=10" (5), not to $x(x-3)=10$ alone.
  - $\log_6x+\log_6(x^2-7)=1$ ⇒ 3.
  - $\log(x+6)-\log(x-2)=\log5$ ⇒ 4.
  - $\log(2x-3)+\log(4x-1)=2\log5$ ⇒ $\frac{11}4$.
  - $1+\log_4(x-1)=\log_2(x-9)$ ⇒ 17.
  - $\log_x(x+3)-\frac12\log_x(x+6)=\log_x2$ ⇒ 3.
  - $\log x-6\log_x10=1$ ⇒ $10^3$ or $10^{-2}$; $x^{\log x}=10^6x$ ⇒ $10^3$ or $\frac1{100}$; $x^{\log x}=10^8x^2$ ⇒ $10^4$ or $10^{-2}$.
  - $\log_3(3^x+6)=\frac x2+\log_35$-type ⇒ 2 or $2\log_32$; $\log(10^x+100)=\frac x2+1+\log2$ ⇒ 2.
  - **2007學測**: 0<x<1, $\log_x4-\log_2x=1$ ⇒ $t=\log_2x<0$: $\frac2t-t=1$ ⇒ t=−2 ⇒ $x=\frac14$.
  - Roots α, β of $(\log x)^2-\log x^2-6=0$ ⇒ $\log_\alpha\beta+\log_\beta\alpha=\frac{u^2+v^2}{uv}=-\frac83$.
  - 抄錯 type ($\log_2x+a\log_x2+b=0$; 甲 copied b wrong, 乙 copied a wrong) ⇒ a=6, b=−5, x = 4, 8.
  - Probabilities $\log_4k$, $\log_8k$, $\log_{64}k$ summing to 1 ⇒ $\log_2k=1$ ⇒ k=2.
  - $2x=\log_23$ ⇒ $\frac{2^{3x}-2^{-3x}}{2^x-2^{-x}}=4^x+1+4^{-x}=\frac{13}3$.
  - $\frac{\log a}{\log b}=\frac ab$ (with a<b): $(2,4)$, $(\sqrt3,3\sqrt3)$; in general $a=t^{\frac1{t-1}}$, $b=t^{\frac t{t-1}}$.
  - $2^a=3^{-b}=5^c=\sqrt{90}^{\,d}$ ⇒ $\frac1a+\frac1c=2(\frac1b+\frac1d)$.
  - GP with $a_3a_{13}=256$ ⇒ $\sum_{k=1}^{15}\log_2a_k=\log_2a_8^{15}=60$.
  - $x^4+2\sqrt3(\log_2k)x^2+1-(\log_2k)^2=0$ with two real and two imaginary roots ⇒ $0<k<\frac12$ or $k>2$.
- Is the solution set the same? 「$\log x+\log(x-3)=1$」 ⇔ (5) 「x>3 且 x(x−3)=10」.

### 15.5 指數與對數不等式
- Rule: base > 1 keeps the direction; 0 < base < 1 **reverses** it. For logs, **intersect with the domain first**.
- Exponential:
  - $2^{2x}<8$ ⇒ $x<\frac32$; $(\frac1{10})^{x-1}>0.001$ ⇒ x<4.
  - $(0.7)^{x^2}>(0.7)^{2x}$ ⇒ 0<x<2.
  - $16^{x^2-x}>8$ ⇒ $4x^2-4x-3>0$ ⇒ $x>\frac32$ or $x<-\frac12$; $(0.2)^{x^2-3x-1}>0.008$ ⇒ −1<x<4.
  - $2^{2x+2}<9\cdot2^x-2$ ⇒ $(4t-1)(t-2)<0$ ⇒ −2<x<1.
  - $(\frac19)^x+(\frac13)^x>12$ ⇒ x<−1.
  - $3^{2x}+3^{x-2}>3^{x+2}+1$ ⇒ $(9t+1)(t-9)>0$ ⇒ x>2.
  - $2^{x+2}>4^{11-x}$ ⇒ $x>\frac{20}3$.
  - $5^x<3$ ⇒ $x<\log_53$.
  - $f=2(4^x+4^{-x})-7(2^x+2^{-x})+9=2t^2-7t+5<0$ with $t\ge2$ ⇒ $2\le t<\frac52$.
- Logarithmic:
  - $\log_3(x-1)<2$ ⇒ 1<x<10.
  - $\log_{0.3}(2x-1)\le\log_{0.3}(x-2)$ ⇒ x>2.
  - $\log_{0.5}x\ge3$ ⇒ $0<x\le\frac18$.
  - $\log_{\frac12}x>2$ ⇒ $0<x<\frac14$.
  - $\log(x-1)<1$ ⇒ 1<x<11.
  - $\log_3(x^2+2x)>1$ ⇒ $(x+3)(x-1)>0$ ⇒ x>1 or x<−3.
  - $\log_{\frac12}(x-1)+\log_{\frac12}(x-3)\ge-3$ ⇒ 3<x≤5.
  - $\log_x(x-1)>0$ ⇒ x>2.
  - $\log_a(x-7)+\log_a(x+3)<\log_a(2x-5)$ ⇒ a>1: 7<x<8; 0<a<1: x>8.
  - $\log_{1.5}(x+1)>\log_{2.25}(x^2-x-1)$ ⇒ $-\frac23<x<\frac{1-\sqrt5}2$ or $x>\frac{1+\sqrt5}2$.
  - $\log_3x+\log_x3<\frac{10}3$ ($x\ne1$) ⇒ 0<x<1 or $\sqrt[3]3<x<27$.
  - $\log_{14}(x^3-5x+12)<1$ ⇒ −3<x<−2 or $1-\sqrt2<x<1+\sqrt2$.
  - $\log_3(3^x+8)<\frac x2+1+\log_32$ ⇒ $t=3^{x/2}$ ⇒ $\log_34<x<\log_316$.
  - $\log(x^2+2x+a)>0$ for all x ⇔ $x^2+2x+a-1>0$ always ⇔ a>2.
  - $-1<\log_3(\log_9(\log_{27}x))<1$ with $x=3^m$ ⇒ 17 values of m.
- **Extrema with logs / AM–GM**:
  - x+2y=12 ⇒ $\log_2x+\log_2y\le\log_218=1+\log_29$.
  - $f(x)=x^{1-\log x}$ on [1,100] ⇒ $\log f=-(\log x-\frac12)^2+\frac14$ ⇒ max $10^{1/4}$, min $\frac1{100}$.

### 15.6 模型與應用 (按比例成長/衰退; 科學與金融)
- **Model** $f(t)=c\cdot a^{t/T}$:
  - c = initial value; per period T the ratio is a.
  - 半衰期 T: $f(t)=c(\frac12)^{t/T}$.
  - Doubling time: $c\cdot2^{t/T}$.
  - Each increase of x by 2 multiplies y by 9 ⇒ a=3.
- 例 (exponential models):
  - **Moore's law** (double every 18 months): $f(t)=1000\cdot2^{t/18}$; 3 years ⇒ 4000.
  - **Drug** with half-life 3 h from 10 mg/L: $10(\frac12)^{t/3}$; 6 h → 2.5, 9 h → 1.25. From its graph: m=400, $a=2^{-1/2}$.
  - Drug with $f(0)=500$, $f(0.5)=400$ ⇒ $a=\frac{16}{25}$; after 2 h 204.8 mg.
  - E. coli doubles every 20 min from $10^3$: $10^3\cdot2^{t/20}$.
  - **Bacteria** ×k per day: 2000 at day 2, 16000 at day 3.5 ⇒ $k^{1.5}=8$ ⇒ k=4, $f=125\cdot4^x$.
  - Bacteria A ×2 per 2 h, B ×3 per 3 h; B = 10·A when $t(\frac{\log3}3-\frac{\log2}2)=1$ ⇒ t ≈ 117 h (**2007學科** (5)).
  - Mixed culture: B (×4/day) exceeds 1000 × A (×2/day) when $2^n\ge1000$ ⇒ day 10 (89社).
  - Frogs $30\cdot4^t$: t=2 → 480; 1200 at $t=\log_440\approx2.7$.
  - Town population $1500\cdot2^{0.7t}$: 15000 at $t=\frac{1}{0.7\log2}\approx4.7$; 30000 at ≈6.2.
  - **2016學測** (also 108 習題): A (half-life 7.5 h) starts at twice B; equal after 120 h ⇒ $2(\frac12)^{16}=(\frac12)^{120/x}$ ⇒ x=8 h (1).
  - **87學科** 布袋蓮 (area doubles monthly; 1 m² at month 0 per the figure): base 2 ✓; >30 m² at month 5 ✓; from 4 to 12 m² takes $\log_23\ne1.5$; $t_1+t_2=t_3$ for 2, 3, 6 m² ✓; average rates differ → (A)(B)(D).
  - **89學科** world population (fixed growth; 50億 in 1987, 60億 in 1999) ⇒ 2023: $50\times1.2^3\approx86$億 (C).
  - Taiwan 1990: $21\times10^6(1.012)^x$ ⇒ 2000 ≈ $2.366\times10^7$.
  - 碳14 (5730 or 5770 y): $m(t)=m_0(\frac12)^{t/5770}$; 11540 y → ¼ (12.5 mg of 50); down to ⅔ after $5770\log_2\frac32\approx3375$–3376 y.
  - 福島 isotope: ×0.9 per 10 y ⇒ $N(0.9)^{x/10}$; below $\frac1{10}$ after $t>\frac{10\log0.1}{\log0.9}\approx219$ y.
  - 鐳 1600 y, ¾ left ≈ 664 y.
- **Interest (複利)**: $P_n=A(1+r)^n$; $m$ periods a year at annual rate R ⇒ $(1+\frac Rm)^{mt}$.
  - 1萬 at 2% compounded half-yearly: $f(t)=(1.01)^{2t}$.
  - 10萬 at 4% exceeds 20萬 after 18 years.
  - 7%: 20萬→30萬 after 6 years (C); 12.5% doubles in 6 years (86大學聯考).
  - **91指定乙** double in 10 years ⇒ 8% growth; **89自** weekly 1% loss halves in 69 weeks.
  - 20% vs 8%: the ratio doubles after 7 years.
  - **91指定甲** monthly rates (甲 0.3% throughout; 乙 0.3, 0.4, 0.2; 丙 0.3, 0.2, 0.4) ⇒ $a>b=c$ (AM–GM) → (1)(2).
  - Loan of 100萬 at 16% with half-yearly compounding.
  - (e) $(1+\frac1n)^n\to e\approx2.71828$ — Euler 1727; **[超出數A]**, ln = 自然對數.
- **Log-scale laws** (formula given in stem):
  - Richter $\log E=11.8+1.5M$: ΔM=2 ⇒ $10^3$ times; 9.1 vs 7.3 ⇒ $10^{2.7}\approx501$ times; with $r=\log I$, 7.3 vs 7.2 ⇒ 1.259 times.
  - 海嘯 $I=\frac12+\log_2H$-type: one level up ⇒ wave height ×2.
  - 分貝 $10\log\frac I{10^{-12}}$: rain 55 dB vs whisper 25 dB ⇒ 1000×; mosquito $10^{-12}$ → 0 dB; car $10^{-4}$ → 80 dB; 100 sirens at 70 dB → 90 dB (93指定乙).
  - Fechner $y=a\log x+b$ (感覺 ∝ log 刺激): the handout's graph gives $y=\frac32\log x+3$; one unit less sweet ⇒ sweetness ×$10^{-2/3}\approx0.2$.
  - Brightness $y=a\log_2x$ through (10,1) ⇒ $a=\log2$; raising the feeling from 1 to 2 ⇒ illuminance ×10.
  - Visual magnitude $-\frac52\log\frac xa$: a star 10× as bright as Vega has magnitude −2.5.
  - Advertising $N=1000+500\log_2(x+1)$: N(0)=1000; 2000 needs x=3 萬.
  - Tornado $v=65+93\log d$: d=200 → 279 mph; v ≥ 120 ⇔ $d\ge10^{55/93}\approx4$ miles.
  - Wind $v(z_2)=v(z_1)\frac{\log z_2+c}{\log z_1+c}$: 12 at 2 m and 16 at 10 m ⇒ $c=3-4\log2$, v(100) ≈ 22 km/h.
  - **Memory test** $P(t)=a-b\log_2t$: (2,62), (8,26) ⇒ a=80, b=18; below 1% when $t\ge2^{79/18}\approx21$ s.
  - **Information spread** $100(1-2^{-kt})\%$ with 70% at 3 h ⇒ $2^{-3k}=0.3$:
    - 90% at $t=3\frac{\log0.1}{\log0.3}\approx5.7$ h. (The 108 2-3 key prints 17.3, from multiplying instead of dividing the logs.)
    - 99% at ≈11.5 h (**92學測** (4) 11½).
  - **Epidemic** $I(t)=\frac1{1+a\cdot b^{-t}}$-type:
    - 1% at t=0 ⇒ a=99; peak (50%) at $t=3\frac{\log99}{\log5}\approx9$ weeks.
    - 4萬 of 200萬 at t=0 and 25萬 at t=3 ⇒ k=49, $a=\frac13$ ⇒ peak at month 6; at t=12, 98%.
  - **Newton cooling** $T=A\cdot3^{kt}+5$: 185 → 95 in 5 min ⇒ A=180, $3^{5k}=\frac12$ ⇒ at 15 min, $T=180\cdot\frac18+5=27.5$°C. (The key rounds k to −0.1 first and gets 40; this illustrates error from early rounding.)
  - 轟炸機 learning curve $T=(\frac45)^{\log_2n}$: 4th plane → $\frac{16}{25}$ year; 6th / 3rd = $\frac45$.
  - Mercator $y=\ln\frac{1+\sin d}{\cos d}$ (uses ln; enrichment).
  - Salt solution 8%, replacing 20 g of 100 g each time: below 2% after n=7.
- **Log–log linearisation** (links §9):
  - Planets: $\log R$ vs $\log T$ has slope $\frac23$ ⇒ $R=kT^{2/3}$ (Kepler; regression $Y=1.5016X-0.393$, r=0.99998, for T vs R).
  - Models: power $y=ax^b$ ⇒ $\log y=\log a+b\log x$; exponential $y=a10^{bx}$ ⇒ $\log y=\log a+bx$; logarithmic $y=a+b\log x$.
  - Walking speed vs city population (Bornstein).
- Large numbers (see §3.3):
  - $3^{500}\approx3.639\times10^{238}$ (239 digits).
  - $(\frac17)^{200}\approx9.55\times10^{-170}$ (170th decimal place).
  - $2^{607}-1\approx5.311\times10^{182}$ (183 digits, leading 5).
  - $0.5^{500}\approx3.1\times10^{-151}$.
  - $2^{50}$: 16 digits, leading 1; $(\frac13)^{200}$: 96th place, digit 3.
  - $2^{6972593}-1$ needs ≈700 A4 sheets at 3000 digits per sheet (89學科 E).
  - **2012學測** $\log x=2.8$, $\log y=5.6$ ⇒ $\log(x^2+y)=\log2y\approx5.9$ (3).
  - **2012學測** $10^{3.032}\approx1076$ (4).
  - **2017學測** interpolation: $\frac13\log a+\frac23\log b$ with a=45, b=48 ⇒ x=47.
  - **2007指定甲** zig-zag moves of $\log a_k$ ⇒ $(a_1,r)=(5,\sqrt2)$.
  - $77^{20}$ has 38 digits (given $7^{100}$ has 85 and $11^{100}$ has 105); $n^4<10^6<(n+1)^4$ ⇒ n=31; $1.6^n$ has three integer digits for n=10..14.
  - $400<(\frac54)^n<500$ ⇒ n=27.
  - **2009指定甲** interpolation: $\log4.342\approx0.8\log4.34+0.2\log4.35$.

**Traps**:
- Domain first for logs, and check the roots.
- 0 < base < 1 reverses inequalities.
- $t=a^x$ must be positive; in $t=a^x+a^{-x}$, $t\ge2$.
- $\log(x+y)\ne\log x+\log y$.
- $\log x^2=2\log|x|$.
- Don't round intermediate constants (see the cooling example).
- 「幾倍」 questions mean ratios of $10^{\Delta}$; 星等 is smaller for brighter stars.

## 16. 平面向量（運算、線性組合、分點、內積、正射影、柯西、面積與二階行列式）

**Scope**:
- G-11A-1 平面向量: 係數積與加減, **線性組合** (main goal; use 位置向量).
- G-11A-4 三角不等式: vector length; covers the real-number triangle inequality as a special case.
- G-11A-6 平面向量的運算: 正射影與內積, **面積與行列式**, 平行/垂直判定, 夾角, **柯西不等式**.
- A-11A-1 (2×2 方程組的矩陣表達, **克拉瑪公式** tied to linear combinations and parallelogram area) is introduced here and continued in §20.
- 孟氏/西瓦 theorems and vector proofs of triangle centres are 資優/99 enrichment.

**Sources**: 108二上 3-1平面向量與其運算, 3-2平面向量的內積, 3-3平面向量的應用; 99第三冊 3-1平面向量的運算, 3-2平面向量的應用(一), 3-3平面向量的應用(二), 3-4面積與二階行列式; 資優 第25單元向量的基本概念, 第26單元向量的應用, 第27單元平面向量的坐標化.

### 16.1 向量、坐標表示、加減、係數積
- **Vectors and equality**:
  - A vector = 有向線段 (direction + magnitude): $\overrightarrow{AB}$ with 始點 A, 終點 B, length $|\overrightarrow{AB}|=\overline{AB}$.
  - 零向量 $\vec0$ has length 0 and any direction; 反向量 $\overrightarrow{BA}=-\overrightarrow{AB}$.
  - **相等** ⇔ same length and same direction, so vectors can be translated freely.
  - Regular hexagon with centre O and side 1: $\overrightarrow{AB}=\overrightarrow{FO}=\overrightarrow{OC}=\overrightarrow{ED}$; there are 6 vectors of length 2 ($\overline{AD},\overline{BE},\overline{CF}$, each in both directions).
- **Coordinates**: $\vec a=\overrightarrow{OP}=(a_1,a_2)$ (x 分量, y 分量), $|\vec a|=\sqrt{a_1^2+a_2^2}$.
  - $\overrightarrow{AB}=(b_1-a_1,b_2-a_2)$.
  - With length r and 方向角 θ: $\overrightarrow{AB}=(r\cos\theta,r\sin\theta)$.
  - A(−2,5), B(1,1): $\overrightarrow{AB}=(3,-4)$, length 5.
  - Parallelogram ABCD with A(3,−2), B(−1,2), C(2,3) ⇒ D(6,−1).
  - Regular hexagon of side 3 with $\cos\theta=\frac23$ ⇒ $\overrightarrow{AB}=(2,\sqrt5)$.
- **Addition**: 三角形法 $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$ (displacement); 平行四邊形法 $\overrightarrow{AB}+\overrightarrow{AC}=\overrightarrow{AD}$ (resultant force).
  - Subtraction: $\overrightarrow{AB}-\overrightarrow{AC}=\overrightarrow{CB}$ (from the end of $\vec b$ to the end of $\vec a$).
  - **拆解**: $\overrightarrow{AB}=\overrightarrow{AP}+\overrightarrow{PB}=\overrightarrow{PB}-\overrightarrow{PA}$ for any P.
  - In coordinates the operations are componentwise; addition is commutative and associative.
- **係數積** $r\vec a$: length $|r||\vec a|$; same direction if r>0, opposite if r<0; $0\vec a=r\vec0=\vec0$ (a vector, not the number 0). Distributive and associative laws hold.
- **平行** $\vec a\parallel\vec b$ (non-zero) ⇔ $\vec a=t\vec b$ ⇔ $a_1b_2=a_2b_1$.
  - $(\vec a+t\vec b)\parallel\vec c$: (1,2), (2,3), (3,4) ⇒ t=−2; (−2,1), (3,−2), (4,−3) ⇒ t=2; (1,−3), (−2,4), (3,−5) ⇒ t=2.
- **單位向量** $\frac{\vec a}{|\vec a|}$; parallel unit vectors are $\pm\frac{\vec a}{|\vec a|}$ ((3,1) → $\pm\frac1{\sqrt{10}}(3,1)$; (4,−3) → $\pm\frac15(4,-3)$).
- **Minimum length** $|\vec a+t\vec b|$ occurs when $(\vec a+t\vec b)\perp\vec b$, i.e. $t=-\frac{\vec a\cdot\vec b}{|\vec b|^2}$:
  - (2,−3), (1,4) ⇒ $t=\frac{10}{17}$, min $\frac{11}{\sqrt{17}}$.
  - (2,1), (3,4) ⇒ $t=-\frac25$.
  - (1,−3), (−2,4) ⇒ min $\frac{\sqrt5}5$.
- **Regular hexagon with $\overrightarrow{AB}=\vec a$, $\overrightarrow{BC}=\vec b$**: $\overrightarrow{AC}=\vec a+\vec b$, $\overrightarrow{BD}=2\vec b-\vec a$, $\overrightarrow{CD}=\vec b-\vec a$, $\overrightarrow{BE}=2\vec b-2\vec a$, $\overrightarrow{BF}=\vec b-2\vec a$.
  - Points A..F evenly spaced on a line: $\overrightarrow{AB}=\frac15\overrightarrow{AF}=\frac13\overrightarrow{CF}$, $\overrightarrow{BE}=-\frac32\overrightarrow{DB}$, $\overrightarrow{AB}+2\overrightarrow{DE}=3\overrightarrow{BC}$.
- 學測/指考:
  - **2014學測**: from (−3,6), which directions eventually enter quadrant I → (1,−1), (0.001,0), (0.001,1) (2)(3)(4).
  - **2015學測**: circle with diameter AE split into 4 equal arcs, $\overrightarrow{MD}=8(\cos(\theta+90^\circ),\sin(\theta+90^\circ))$ ⇒ $\overrightarrow{MC}=8(\cos(\theta+45^\circ),\dots)$ ✓, $\overrightarrow{MB}\cdot\overrightarrow{MD}=0$ ✓ → (2)(4).
  - **2009學測**: O → P (along $\overrightarrow{AO}$ by $\overline{AO}$) → Q (along $\overrightarrow{BP}$ by $2\overline{BP}$) → back to O (along $\overrightarrow{CQ}$ by $3\overline{CQ}$) ⇒ $O=4Q-3C$ ⇒ C(−4,20).
  - 北極星: 天樞 + 5(天樞 − 天璇) = (7,8) + 5(−2,−3) = (−3,−7).
  - **2015學測**: P with $\overrightarrow{Q_1P}=(-7,9)$ from $Q_1$ on $x+2y=0$ and $\overrightarrow{Q_2P}=(-6,-8)$ from $Q_2$ on $3x-5y=0$ ⇒ P(9,1).
  - **86學科**: unit vectors between cube vertices → 6 (B).
  - **90學科**: A(150,200), B(146,203), C(−4,3) ⇒ $\overrightarrow{OA}\cdot\overrightarrow{OC}=0$ and $\overrightarrow{OA}+\overrightarrow{OC}=\overrightarrow{OB}$, so OABC is a rectangle with area 1250, $AC\approx250.05<251$ → (A)(B)(E).
  - Polyline OA=8, AB=4, BC=2, CD=1 turning 120° each time: C$(9,3\sqrt3)$; $\overrightarrow{OD}=-\frac78\overrightarrow{OA}+\frac32\overrightarrow{OB}$.
  - $\overrightarrow{OA}=(3,1)$, $\overrightarrow{OB}=(-1,2)$, $\overrightarrow{OC}\perp\overrightarrow{OB}$, $\overrightarrow{BC}\parallel\overrightarrow{OA}$, $\overrightarrow{OD}+\overrightarrow{OA}=\overrightarrow{OC}$ ⇒ $\overrightarrow{OD}=(11,6)$.

### 16.2 線性組合、分點公式、三點共線、區域
- **Theorem**: if $\overrightarrow{OA},\overrightarrow{OB}$ are non-zero and not parallel, every plane vector is **uniquely** $x\overrightarrow{OA}+y\overrightarrow{OB}$ (draw parallels; uniqueness otherwise contradicts non-parallelism). Uniqueness ⇔ $\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}\ne0$.
  - (3,8) = 2(2,3) + 1(−1,2); (3,8) = 2(3,1) + 3(−1,2); (5,9) = 1(3,1) + 2(1,4).
  - $\vec c=\vec a+t\vec b$ with $|\vec c|=\sqrt{41}$ ⇒ t=1 or $-\frac{31}{17}$.
  - Parallelogram ABCD with $AE=2EC$ and F the midpoint of BC: $\overrightarrow{AE}=\frac23\overrightarrow{AB}+\frac23\overrightarrow{AD}$, $\overrightarrow{EF}=\frac13\overrightarrow{AB}-\frac16\overrightarrow{AD}$. With $AE=3EC$: $\frac34,\frac34$ and $\frac14,-\frac14$.
  - Parallelogram with $AG=\frac12AB$, $BE=\frac13BC$, $CF=\frac34CD$: $\overrightarrow{EF}=-\frac34\vec a+\frac23\vec b$, $\overrightarrow{GF}=-\frac14\vec a+\vec b$.
  - Coefficients of a vector identity must vanish when the base vectors are independent: $(3x-y-2)\overrightarrow{AB}+\dots=\vec0$ ⇒ x=−2, y=3.
- **分點公式**: P on $\overline{AB}$ with $AP:PB=m:n$ ⇒ $\overrightarrow{OP}=\frac n{m+n}\overrightarrow{OA}+\frac m{m+n}\overrightarrow{OB}$ for any O (taking O=A: $\overrightarrow{AP}=\frac m{m+n}\overrightarrow{AB}$).
  - External division uses a negative ratio. P not on segment AB with AP:BP=5:2 ⇒ $\overrightarrow{OP}=-\frac23\overrightarrow{OA}+\frac53\overrightarrow{OB}$; 3:2 ⇒ $-2\overrightarrow{OA}+3\overrightarrow{OB}$.
  - A(−2,3), B(3,13), AD:DB=4:1 ⇒ D(2,11) or $(\frac{10}3,\frac{41}3)$.
  - A(2,5), B(−3,0), AP:PB=2:3 ⇒ (0,3) internally, (12,15) externally.
  - A(−4,9), B(1,4), AP:BP=3:2 ⇒ (−1,6) or (11,−6).
  - AP:AB=4:11 with $\overrightarrow{PA}=t\overrightarrow{PB}$ ⇒ $t=-\frac47$ or $\frac4{15}$.
  - **Centroid** $\overrightarrow{OG}=\frac13(\overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC})$ ⇔ $\overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC}=\vec0$; A(−2,2), B(5,3), G(2,1) ⇒ C(3,−2).
  - **Incentre** $\overrightarrow{OI}=\frac{a\overrightarrow{OA}+b\overrightarrow{OB}+c\overrightarrow{OC}}{a+b+c}$. With AB=5, BC=4, CA=6: $\overrightarrow{AD}=\frac6{11}\overrightarrow{AB}+\frac5{11}\overrightarrow{AC}$, $\overrightarrow{AI}=\frac25\overrightarrow{AB}+\frac13\overrightarrow{AC}$. With AB=5, BC=6, CA=7: $\overrightarrow{AI}=\frac7{18}\overrightarrow{AB}+\frac5{18}\overrightarrow{AC}$, bisector $AT=\frac{\sqrt{105}}2$.
  - **Angle bisector direction**: $\frac{\vec a}{|\vec a|}+\frac{\vec b}{|\vec b|}$.
    - $|\vec a|=4$, $|\vec b|=5$ with $\vec c=\alpha\vec a+\beta\vec b$, α+β=1 ⇒ $\alpha=\frac59$, $\beta=\frac49$.
    - $(-3,4)$ and $(6,8)$ ⇒ $\vec c=\frac23\vec a+\frac13\vec b$.
    - (2,4) and (−2,−1): $\vec a+t\vec b$ bisects ⇒ t=2 ($\vec c=(-2,2)$), unit bisector $\frac1{\sqrt2}(-1,1)$.
    - (3,4), (1,0) ⇒ $\frac1{\sqrt5}(2,1)$; (−1,3), (3,1) ⇒ $\frac1{2\sqrt5}(2,4)$.
    - AB=3, AC=5: internal bisector $\overrightarrow{AD}=\frac58\overrightarrow{AB}+\frac38\overrightarrow{AC}$; external $\overrightarrow{AE}=\frac52\overrightarrow{AB}-\frac32\overrightarrow{AC}$.
    - △ABC with A(1,−2), B(−5,2), C(7,7) ⇒ internal D$(-\frac15,4)$, external E(−29,−8).
- **三點共線**: A, B, P collinear ⇔ $\overrightarrow{OP}=\alpha\overrightarrow{OA}+\beta\overrightarrow{OB}$ with **α+β=1**.
  - P on segment AB ⇔ additionally α, β ≥ 0.
  - Line through O, A, B with $\vec u,\vec v$: $\overrightarrow{OA}=\vec u+2\vec v$, $\overrightarrow{OB}=-\vec u+5\vec v$, $\overrightarrow{OC}=r\vec u+s\vec v$ collinear with 2r+s=−1 ⇒ r=−9, s=17.
  - Checks: $\overrightarrow{AP}+3\overrightarrow{AB}=\vec0$ ✓; $\frac25+\frac35=1$ ✓; $\frac4{12}+\frac3{12}\ne1$ ✗; $\frac75-\frac25=1$ ✓; $\overrightarrow{PA}+\overrightarrow{AB}=\overrightarrow{PB}$ always (no info).
  - A(3,1), B(2,3), C(k−2,−1) collinear ⇒ k=6.
- **Intersections via two expressions** (solve with uniqueness of coefficients):
  - AD:DB=3:2 (on AB), AE:EC=2:5 (on AC), P = BE∩CD ⇒ $\overrightarrow{AP}=\frac{15}{29}\overrightarrow{AB}+\frac4{29}\overrightarrow{AC}$, $BP:PE=\frac{14}{15}$.
  - D the midpoint of AB, AE:EC=2:1, P = CD∩BE ⇒ $\overrightarrow{AP}=\frac14\overrightarrow{AB}+\frac12\overrightarrow{AC}$, BP:PE=3:1.
  - C the midpoint of OB with AD:DC=2:3 ⇒ $\overrightarrow{OD}=\frac35\overrightarrow{OA}+\frac15\overrightarrow{OB}$.
  - Parallelogram with AE:ED=1:2 and AF=3FB, P=BE∩DF ⇒ $\overrightarrow{AP}=\frac12\overrightarrow{AB}+\frac13\overrightarrow{AD}$, DP:PF=2:1.
  - $5\overrightarrow{AP}=\overrightarrow{AB}+2\overrightarrow{AC}$, AP meets BC at D ⇒ $\overrightarrow{AD}=\frac53\overrightarrow{AP}$, BD:DC=2, $\frac{[PBD]}{[ABC]}=\frac4{15}$.
  - $7\overrightarrow{AD}=8\overrightarrow{AB}+6\overrightarrow{AC}$ ⇒ AE (with E on BC) $=\frac12\overrightarrow{AD}$, BE:EC=3:4, $[ABD]:[ABC]=6:7$ (92 北區模擬).
  - $4\overrightarrow{AB}+5\overrightarrow{AD}=6\overrightarrow{AC}$ ⇒ $\overrightarrow{AC}=\frac23\overrightarrow{AB}+\frac56\overrightarrow{AD}$ ⇒ $[ABC]:[ACD]=5:4$.
  - Points dividing the sides 2:1 cyclically ⇒ cevians form an inner triangle with area $\frac17$; $\overrightarrow{AP}=\frac17\overrightarrow{AB}+\frac27\overrightarrow{AC}$.
  - D, E, F on BC, CA, AB with DC=4BD, EC=2AE, FB=2AF; G the centroid of DEF ⇒ $\overrightarrow{AG}=\frac{17}{45}\overrightarrow{AB}+\frac8{45}\overrightarrow{AC}$.
  - D on BC with BD:DC=3:2, P on AD with AP:PD=1:2 ⇒ $\overrightarrow{OP}=\frac23\overrightarrow{OA}+\frac2{15}\overrightarrow{OB}+\frac15\overrightarrow{OC}$.
  - P the midpoint of AG, $\overrightarrow{AP}=x\overrightarrow{AC}+y\overrightarrow{BG}$ ⇒ $x=\frac14$, $y=-\frac14$.
  - A line through the centroid G meets AB, AC at P, Q ⇒ $\frac{AB}{AP}+\frac{AC}{AQ}=3$. General: $\frac m{1+\lambda}+\frac{n\lambda}{1+\lambda}=\frac1k$.
  - Parallelogram with DP=CP and CQ=2BQ ⇒ $\overrightarrow{PQ}=\frac76\overrightarrow{AB}-\frac23\overrightarrow{AC}$.
  - $\triangle ABK:\triangle ACK=3:4$ ⇒ $\overrightarrow{AD}=\frac47\overrightarrow{AB}+\frac37\overrightarrow{AC}$.
  - **2021指定甲** trapezoid AB∥DC, $AB=\frac25DC$, AE=2EC, BF=$\frac23$FD ⇒ $\overrightarrow{FE}=\frac9{25}\overrightarrow{AC}-\frac4{25}\overrightarrow{AD}$.
- **Area ratios from barycentric weights**:
  - $l\overrightarrow{PA}+m\overrightarrow{PB}+n\overrightarrow{PC}=\vec0$ (positive) ⇒ $[PBC]:[PCA]:[PAB]=l:m:n$.
  - $2\overrightarrow{AB}+\overrightarrow{AC}=2(2\overrightarrow{PB}+\overrightarrow{PC})$ ⇒ $3\overrightarrow{PA}+2\overrightarrow{PB}+\overrightarrow{PC}=\vec0$ ⇒ $[ABP]:[BCP]:[ACP]=1:3:2$.
  - $\overrightarrow{AP}=\frac15\overrightarrow{AB}+\frac25\overrightarrow{AC}$ ⇒ $\frac{[ABP]}{[ABC]}=\frac25$ (**2003學測/92學科** (C)).
  - 孟氏 (Menelaus) $\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA}=1$ for collinear D, E, F; 西瓦 (Ceva) the same product = 1 for concurrent cevians. 例: BD:DC=1:2, AE:EC=3:2 ⇒ $\overrightarrow{AP}=\frac6{11}\overrightarrow{AB}+\frac3{11}\overrightarrow{AC}$; areas $[ABP]:[BCP]:[CAP]=3:2:6$.
- **Regions** for $\overrightarrow{AP}=x\overrightarrow{AB}+y\overrightarrow{AC}$:
  - x+2y=1 ⇒ a line; with extra sign conditions, a segment.
  - $a\le x\le b$, $c\le y\le d$ ⇒ a parallelogram of area $(b-a)(d-c)\cdot|\overrightarrow{AB}\times\overrightarrow{AC}|$.
  - s+t ≤ 1 ⇒ a half-plane; x, y ≥ 0 and x+y ≤ 1 ⇒ △ABC.
  - AB=2, AC=1, ∠A=60°, $-1\le x\le3$, $-4\le y\le2$ ⇒ 24 unit parallelograms ⇒ area $24\cdot2\cdot1\cdot\sin60^\circ=24\sqrt3$.
  - **2004學測/93學科**: $\overrightarrow{AP}=\frac13\overrightarrow{AB}+t\overrightarrow{AC}$ inside △ABC ⇔ $0<t<\frac23$ (D).
  - **2020學測**: regular hexagon with centre O, $\overrightarrow{OP}=x\overrightarrow{OC}+y\overrightarrow{OE}$ inside △ODE (where $\overrightarrow{OD}=\overrightarrow{OC}+\overrightarrow{OE}$) ⇔ $0<x<y<1$ → (2) $\frac14,\frac12$.
  - x+y=3 with x, y ≥ 0, |AB|=3, |AC|=4, ∠A=120° ⇒ the segment from $3\overrightarrow{AB}$ to $3\overrightarrow{AC}$, of length $3|\overrightarrow{BC}|=3\sqrt{37}$.
  - O(0,0), A(1,2), B(4,5), $\overrightarrow{OP}=\overrightarrow{OA}+t\overrightarrow{AB}$: on the x-axis at $t=-\frac23$, on the y-axis at $t=-\frac13$; in quadrant II for $-\frac23<t<-\frac13$; for −2 ≤ t ≤ 3 the path has length $5|\overrightarrow{AB}|=15\sqrt2$; OABP is never a parallelogram.

### 16.3 內積 (dot product)
- **Definition**: angle θ ∈ [0°,180°] between $\vec a,\vec b$ placed tail to tail; $\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta$ (a number). Motivated by work $W=\vec F\cdot\vec s$; engine power $P=\frac1{75}\vec F\cdot\vec v$ (1000 kg, 15 m/s, 30° ⇒ $100\sqrt3$ hp).
  - Sign: positive for an acute angle, 0 for perpendicular, negative for an obtuse angle.
  - **Coordinates**: $\vec a\cdot\vec b=a_1b_1+a_2b_2$ (proof by the law of cosines). $\cos\theta=\frac{\vec a\cdot\vec b}{|\vec a||\vec b|}$.
- **Properties**: commutative, distributive, $r(\vec a\cdot\vec b)=(r\vec a)\cdot\vec b$, $\vec a\cdot\vec a=|\vec a|^2$, $\vec0\cdot\vec a=0$ (the number). $|m\vec a+n\vec b|^2=m^2|\vec a|^2+2mn\,\vec a\cdot\vec b+n^2|\vec b|^2$ (law of cosines in vector form). $\vec a\perp\vec b$ ⇔ $\vec a\cdot\vec b=0$ ⇔ $|\vec a+\vec b|^2=|\vec a|^2+|\vec b|^2$ (Pythagoras).
- **Angle/length problems**:
  - (−2,4), (−1,−2) ⇒ $\cos\theta=-\frac35$.
  - A(3,−2), B(−1,−4), C(6,−3) ⇒ ∠A=135°.
  - (2,0), (−1,√3) ⇒ dot −2, 120°.
  - A(1,−2), B(0,2), C(−3,4) ⇒ $\sin A=\frac5{\sqrt{221}}$.
  - $\vec u=(k,1)$, $\vec v=(2,3)$: perpendicular $k=-\frac32$; parallel $k=\frac23$; at 60°, $k=-8+\frac{13\sqrt3}3$.
  - $|\vec a|=8$ at 120° to $(\sqrt3,1)$ ⇒ (0,−8) or $(-4\sqrt3,4)$.
  - $|\vec a|=3$, $|\vec b|=4$, $|\vec a+\vec b|=\sqrt{13}$ ⇒ 120°, $|3\vec a+2\vec b|=\sqrt{73}$.
  - $|\vec a|,|\vec b|,|\vec c|=3,5,7$ with sum 0 ⇒ $\vec a\cdot\vec b=\frac{15}2$, 60°.
  - $|\vec a|,|\vec b|,|\vec c|=2,3,4$ with sum 0 ⇒ $\sum\vec a\cdot\vec b=-\frac{29}2$, $\cos\langle\vec a,\vec b\rangle=\frac14$.
  - |OA|=2, |OB|=3 at 60° ⇒ dot 3, $|2\overrightarrow{OA}+\overrightarrow{OB}|=\sqrt{37}$, $|\overrightarrow{OA}-2\overrightarrow{OB}|=2\sqrt7$.
  - $|\vec a|=3$, $|\vec b|=1$, $\cos\theta=-\frac13$, $\overrightarrow{OP}=\vec a+\vec b$, $\overrightarrow{OQ}=2\vec a-\vec b$ ⇒ $|\overrightarrow{PQ}|=\sqrt{17}$.
  - $|\vec a|=1$, $|\vec b|=2$ at 60°, $\overrightarrow{OP}=2\vec a-3\vec b$, $\overrightarrow{OQ}=4\vec a+\vec b$ ⇒ $|\overrightarrow{PQ}|=\sqrt{84}$.
  - $|\vec a+\vec b|=4$, $|\vec a-\vec b|=2$ ⇒ $|\vec a-2\vec b|^2+|2\vec a-\vec b|^2=26$.
  - $(\vec a-2\vec b)\perp(\vec a+t\vec b)$ with |a|=1, |b|=2 at 60° ⇒ $t=-\frac17$.
  - $|\vec b|=2|\vec a|$ and $(\vec a+\vec b)\perp(\vec a-\frac25\vec b)$ ⇒ 60°.
  - $|\vec a|=|\vec b|$ and $|\vec a+\vec b|-|\vec a-\vec b|=\sqrt2|\vec a|$ ⇒ $2\cos\frac\theta2-2\sin\frac\theta2=\sqrt2$ ⇒ 30°.
  - **2006指定甲**: $|\vec u|=2|\vec v|=|2\vec u+3\vec v|$ ⇒ $\cos\theta=-\frac78$.
  - **2014學測**: unit $\vec u,\vec v$ with $\vec u+\vec v$ at 75° to $\vec u$ ⇒ angle 150° ⇒ $\vec u\cdot\vec v=-\frac{\sqrt3}2$.
  - Monkeys 3, 8, 7 kg balancing on three ropes ⇒ $|3\vec u+8\vec v|=7$ ⇒ ∠AOB=120°.
  - Equal-size and perpendicular: **2011學測** $\vec w\perp\vec v=(2,5)$ and equal length ⇒ $\vec w=\pm(5,-2)$ ✓; $|\vec v+\vec w|=|\vec v-\vec w|$ ✓; the angle between $\vec v+\vec w$ and $\vec w$ is 45°, not 135°; $|a\vec v+b\vec w|=\sqrt{29(a^2+b^2)}$; (1,0) has c>0 ✓ → (1)(2)(5).
  - Projection lengths: $\vec a$'s projection on $\vec b$ is 3|b| and $\vec b$'s on $\vec a$ is |a|/6 ⇒ $\cos^2\theta=\frac12$ ⇒ 45°.
  - Road A→B→C→D with 4√3, 11, 6 at angles 90° and 120° ⇒ $AD=7\sqrt7$.
- **Using dot products in triangles** (write everything in two base vectors):
  - Equilateral with side 2, M the midpoint of BC: $(\overrightarrow{BC}+\overrightarrow{AM})\cdot\overrightarrow{AC}=5$; $(\overrightarrow{BC}-\overrightarrow{AM})\cdot(\overrightarrow{AB}+\overrightarrow{AM})=-8$.
  - Parallelogram ABCD: $\overrightarrow{AC}\cdot\overrightarrow{BD}=|BC|^2-|AB|^2$ (AB=2, BC=3 ⇒ 5).
  - AB=3, AC=2, BC=4, D and F at quarter points of BC ⇒ $\overrightarrow{AD}\cdot\overrightarrow{AF}=\frac{3}{16}\cdot9+\frac{10}{16}(-\frac32)+\frac3{16}\cdot4=\frac32$.
  - Equilateral side 6 with P, Q trisecting BC: $\overrightarrow{AB}\cdot\overrightarrow{AC}=18$, $AP=2\sqrt7$, $\overrightarrow{AP}\cdot\overrightarrow{AQ}=26$. Side 2 ⇒ $\overrightarrow{AD}\cdot\overrightarrow{AE}=\frac{26}9$.
  - AB=3, AC=2, A=60°, BP:PC=1:2 ⇒ $AP=\frac{2\sqrt{13}}3$.
  - Isosceles trapezoid AD∥BC with $\overrightarrow{AB}=(12,-1)$, $\overrightarrow{AD}=(-2,5)$ ⇒ $\overrightarrow{BC}=3\overrightarrow{AD}$ ⇒ $\overrightarrow{BC}\cdot\overrightarrow{CD}=-87$.
  - Quadrilateral AB=4, BC=1, CD=√3, BC⊥CD, ∠ABC=120° ⇒ $AD=2\sqrt3$.
  - A(1,3), B(−2,6), C(7,5): $\overrightarrow{AB}\cdot\overrightarrow{AC}=-12$, $\cos\theta=-\frac1{\sqrt5}$, $\sin2\theta=-\frac45$.
  - Parallelogram AB=13, AC=10, AD=5, $\cos\angle DAC=\frac35$, $\overrightarrow{AB}\cdot\overrightarrow{AC}=120$ ⇒ $\cos\angle BAD=\frac{16}{65}$, $\overrightarrow{AC}=\frac{40}{63}\overrightarrow{AB}+\frac{50}{63}\overrightarrow{AD}$.
- **Triangle centres with dot products**:
  - **Circumcentre K**: $\overrightarrow{AK}\cdot\overrightarrow{AB}=\frac12|AB|^2$, $\overrightarrow{AK}\cdot\overrightarrow{AC}=\frac12|AC|^2$ ⇒ solve for the coefficients.
    - A=60°, BC=2√7, AC=4 (AB=6) ⇒ $\overrightarrow{AK}=\frac49\overrightarrow{AB}+\frac16\overrightarrow{AC}$.
    - AB=4, BC=5, AC=6 ⇒ $\overrightarrow{AO}=\frac4{35}\overrightarrow{AB}+\frac{16}{35}\overrightarrow{AC}$ (weights $a\cos A:b\cos B:c\cos C$). The 108 3-2 key prints $\frac{27}{35},\frac3{35}$; recomputation gives $\frac4{35},\frac{16}{35}$.
  - **Orthocentre H**: $\overrightarrow{AH}\cdot\overrightarrow{AB}=\overrightarrow{AH}\cdot\overrightarrow{AC}=\overrightarrow{AB}\cdot\overrightarrow{AC}$. AB=4, BC=6, AC=2√7 ⇒ $x=\frac29$. With $\overrightarrow{AO}=\frac25\overrightarrow{AB}+\frac4{15}\overrightarrow{AC}$, Euler gives $\overrightarrow{AH}=\overrightarrow{AB}+\overrightarrow{AC}-2\overrightarrow{AO}=\frac15\overrightarrow{AB}+\frac7{15}\overrightarrow{AC}$. A(−2,1), B(1,2), C(−4,3) ⇒ $H(-\frac52,-\frac32)$.
  - Circumradius 2, A=60°, B=45°: $|\overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}|=|\overrightarrow{OH}|=\sqrt6-\sqrt2$; $|OH|^2=8-4\sqrt3$.
  - $4\overrightarrow{OA}+5\overrightarrow{OB}+6\overrightarrow{OC}=\vec0$ on the unit circle ⇒ $\overrightarrow{OA}\cdot\overrightarrow{OB}=-\frac18$, $AB=\frac32$.
  - $\vec a+\vec b+\vec c=\vec0$ with $\vec a\cdot\vec b=-1$, $\vec b\cdot\vec c=-2$, $\vec c\cdot\vec a=-3$ ⇒ $|\vec a|=2$, $|\vec b|=\sqrt3$, $|\vec c|=\sqrt5$; $|2\vec a+3\vec b+4\vec c|=\sqrt{15}$; $[ABC]=3[OAB]=\frac{3\sqrt{11}}2$.
  - |OA|=1, |OB|=2, |OC|=√2, sum 0 ⇒ $\sin\angle AOB=\frac{\sqrt7}4$, $[ABC]=\frac{3\sqrt7}4$, $|\overrightarrow{OA}+2\overrightarrow{OB}-\overrightarrow{OC}|=\sqrt{22}$.
  - Equilateral inscribed in a circle centred G(12,−5) ⇒ $|\overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}|=3|OG|=39$.
  - Right △OAB with legs 20, 15; P on AB with $\overrightarrow{OA}\cdot\overrightarrow{OP}=\overrightarrow{OB}\cdot\overrightarrow{OP}$ ⇒ OP ⊥ AB ⇒ value $OP^2=144$.
  - △OAB with sides 2, 3, 4: $\vec a\cdot\vec b=-\frac32$; foot of the altitude $\overrightarrow{OH}=\frac{21}{32}\vec a+\frac{11}{32}\vec b$.
- **Shape from dot products**:
  - $\overrightarrow{AB}\cdot\overrightarrow{AC}=|\overrightarrow{AC}|^2$ ⇒ right angle at C.
  - $\overrightarrow{AB}\cdot\overrightarrow{BC}=\overrightarrow{BC}\cdot\overrightarrow{CA}=\overrightarrow{CA}\cdot\overrightarrow{AB}$ ⇒ equilateral.
  - A parallelogram's diagonals are perpendicular ⇔ it is a rhombus.
  - Isosceles with D, E, F dividing AB, BC, CA in m:n, AE ⊥ DF ⇔ m=n.
- **Proofs with vectors**:
  - 中線定理 $2(AB^2+AC^2)=4AD^2+BC^2$.
  - Tangent to $x^2+y^2=r^2$ at T: $x_0x+y_0y=r^2$ (from $\overrightarrow{PT}\cdot\overrightarrow{OT}=0$).
  - Circle with diameter AB: $(x-x_1)(x-x_2)+(y-y_1)(y-y_2)=0$.
  - Chord of contact from P to a circle: $(c-a)(x-a)+(d-b)(y-b)=r^2$.
  - Altitudes are concurrent (垂心).
- **Extrema**:
  - P on $x+y=0$, A(4,0), B(0,−3): $\overrightarrow{PA}\cdot\overrightarrow{PB}=2t^2-7t$ ⇒ min $-\frac{49}8$.
  - Tangents PA, PB to the unit circle ⇒ min $\overrightarrow{PA}\cdot\overrightarrow{PB}=-3+2\sqrt2$.
  - **2013學測**: |A|=1, |B|=2 at 60°, $\vec u=\vec A+\vec B$, $\vec v=x\vec A+y\vec B$ with 6 ≤ x+y ≤ 8 and −2 ≤ x−y ≤ 0 ⇒ $\vec u\cdot\vec v=2x+5y$, max 31 at (3,5).
  - Unit vectors OA, OB at 120° with C on arc AB, $\overrightarrow{OC}=x\overrightarrow{OA}+y\overrightarrow{OB}$ ⇒ max x+y = 2.

### 16.4 柯西不等式、三角不等式
- **柯西**:
  - Vector form: $|\vec a\cdot\vec b|\le|\vec a||\vec b|$, i.e. $(a_1b_1+a_2b_2)^2\le(a_1^2+a_2^2)(b_1^2+b_2^2)$, with equality ⇔ $\vec a\parallel\vec b$ ($a_1:a_2=b_1:b_2$).
  - It also explains $|r|\le1$ (§9, ※).
- **三角不等式**: $\big||\vec a|-|\vec b|\big|\le|\vec a\pm\vec b|\le|\vec a|+|\vec b|$, with equality when the vectors are parallel (same or opposite direction). Real-number version: $|a+b|\le|a|+|b|$.
- 例:
  - 2x+3y=13 ⇒ $x^2+y^2\ge13$ at (2,3).
  - $a^2+b^2=10$ ⇒ $a-3b\in[-10,10]$ (at (1,−3) and (−1,3)).
  - $x^2+y^2=1$ ⇒ $x-3y\in[-\sqrt{10},\sqrt{10}]$; $x^2+y^2=9$ ⇒ $3x-4y+5\in[-10,20]$ at $(\mp\frac95,\pm\frac{12}5)$.
  - Line $3x-y=k$ meets $x^2+y^2=9$ ⇔ $|k|\le3\sqrt{10}$; $3x-2y=k$ meets $(x+2)^2+(y-1)^2=13$ ⇔ $-21\le k\le5$.
  - 3x+5y=4 ⇒ $3x^2+5y^2\ge2$ at $(\frac12,\frac12)$.
  - P on $2x+3y=9$ ⇒ $(x-1)^2+(y+2)^2\ge13$ at (3,1).
  - $(a+\frac4b)(b+\frac9a)\ge25$; $\frac9{\cos^2\theta}+\frac4{\sin^2\theta}\ge25$.
  - **溝渠**: $x^2+y^2=125$ ⇒ $x+2y\le25$ at (5,10).
  - $y=\sqrt{2x-1}+\sqrt{5-3x}$: with $u^2=2x-1$, $v^2=5-3x$, $3u^2+2v^2=7$ ⇒ $(u+v)^2\le(\frac13+\frac12)\cdot7$ ⇒ max $\frac{\sqrt{210}}6$ at $x=\frac{29}{30}$.
  - $a\sqrt{1-b^2}+b\sqrt{1-a^2}=1$ ⇒ $a^2+b^2=1$ (equality case).
  - $2\sin\theta+4\cos\theta=\overrightarrow{OP}\cdot\overrightarrow{OA}$ with A(4,2) ⇒ max $2\sqrt5$; on $[0,\frac\pi2]$ the min is 2.
  - $(2x^2+3y^2)(2+3)\ge(2x+3y)^2$; 是非: $(x^2+y^2)(3^2+4^2)\ge(3x+4y)^2$ ✓ always.

### 16.5 正射影 (orthogonal projection)
- The projection of $\vec a$ on $\vec b$ is $\frac{\vec a\cdot\vec b}{|\vec b|^2}\vec b$; its signed length is $\frac{\vec a\cdot\vec b}{|\vec b|}=|\vec a|\cos\theta$.
  - Decomposition: $\vec a=\vec p+\vec q$ with $\vec p\parallel\vec b$, $\vec q\perp\vec b$.
  - Projecting on $\vec c\parallel\vec b$ gives the same result.
  - The projection of a vector onto (2,5) cannot be (5,2) (it must be parallel to (2,5)).
- 例:
  - A(−3,−1), B(2,4), C(−1,5): projection of $\overrightarrow{AC}$ on $\overrightarrow{AB}$ is (4,4); foot of C is (1,3); $\overrightarrow{AC}=(4,4)+(-2,2)$.
  - $\overrightarrow{AB}$ on $\overrightarrow{AC}$ = (4,8); foot (5,9); $\overrightarrow{AB}=(4,8)+(2,-1)$.
  - P(8,9), Q(−2,4), R(1,8): $\overrightarrow{QP}$ on $\overrightarrow{QR}$ = (6,8); foot (4,12); $\overrightarrow{QP}=(6,8)+(4,-3)$.
  - (3,−1) along (1,2): $\vec p=\frac15(1,2)$, $\vec q=\frac15(14,-7)$.
  - (3,4) along the line $x-2y+4=0$ (direction (2,1)): $\vec b=(4,2)$, $\vec c=(-1,2)$.
  - $(x,4)$ projecting onto (1,2) gives (−2,−4) ⇒ $\frac{x+8}5=-2$ ⇒ x=−18.
  - OC ⊥ AB with B(−5,0), C(−3,6): projection of $\overrightarrow{OA}$ on $\overrightarrow{OC}$ is (−1,2).
  - A △ from a figure: $\cos\angle ABC=\frac1{\sqrt5}$, projection $(\frac35,\frac95)$, foot $(\frac85,\frac95)$.
- **Distance from a point to a line via projection**: d(P, ax+by+c=0) $=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$.
  - (2,−1) to $5x-12y+4=0$ ⇒ 2.
  - $\sqrt{(x+1)^2+(y-2)^2}$ on $3x-4y+2=0$ ⇒ min $\frac95$.
  - Lines parallel to $7x+24y+3=0$ at distance 1: $7x+24y+28=0$ or $7x+24y-22=0$.
  - Angle bisectors of $3x+y-5=0$ and $3x-y-1=0$: y=2, x=1.
  - Through (1,−4) at 45° to $3x+4y-2=0$: $7x+y-3=0$, $x-7y-29=0$.
  - Through (9,−6) at distance $5\sqrt2$ from (4,1): $25m^2-70m+1=0$ ⇒ slope $\frac{7\pm4\sqrt3}5$.
  - **2014指定乙**: line L through A(11,2) perpendicular to AB with B(23,18), points C, D on L at distance 5: (15,−1), (7,5); [OCD] = 41.
  - **2007學測**: P(s,t) and Q symmetric about $3x-4y=0$: $\overrightarrow{PQ}\parallel(3,-4)$ ✓; $\overrightarrow{OP}+\overrightarrow{OQ}\perp\overrightarrow{PQ}$ ✓; the line through Q parallel to L passes through (−s,−t) ✓; Q≠(t,s) → (1)(2)(4)(5).

### 16.6 面積、二階行列式、克拉瑪公式
- **Area**:
  - Parallelogram spanned by $\vec a,\vec b$: $|\vec a||\vec b|\sin\theta=\sqrt{|\vec a|^2|\vec b|^2-(\vec a\cdot\vec b)^2}=\left|\begin{vmatrix}a_1&a_2\\b_1&b_2\end{vmatrix}\right|=|a_1b_2-a_2b_1|$.
  - Triangle: half of that; △ABC: $\frac12\sqrt{|AB|^2|AC|^2-(\overrightarrow{AB}\cdot\overrightarrow{AC})^2}$.
  - Convex quadrilateral: $\frac12|\vec{d_1}||\vec{d_2}|\sin\theta$.
- **二階行列式**: $\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc$, defined from both the area and the elimination denominator.
  - The sign is + when $\vec a$ turns counter-clockwise (0°<θ<180°) to reach $\vec b$.
  - Properties:
    - Transpose invariance.
    - A zero row gives 0.
    - A factor can be pulled out of a row.
    - Swapping rows changes the sign.
    - Adding a multiple of one row to another leaves it unchanged.
    - Split a row that is a sum into two determinants.
  - Geometric meaning: $\langle r\vec a,\vec b\rangle=r\langle\vec a,\vec b\rangle$ (stretch) and $\langle\vec a,\vec b+k\vec a\rangle=\langle\vec a,\vec b\rangle$ (shear).
  - $\vec a\parallel\vec b$ ⇔ det = 0; A, B, C collinear ⇔ $\begin{vmatrix}b_1-a_1&b_2-a_2\\c_1-a_1&c_2-a_2\end{vmatrix}=0$.
- 例 (area):
  - A(1,0), B(3,2), C(0,4) ⇒ [ABC]=5; with $0\le x\le2$, $-1\le y\le1$ the region has area 40.
  - (5,2), (3,−2) ⇒ 16.
  - A(3,8), B(4,9), C(1,3) ⇒ $\frac32$.
  - A(−1,2), B(4,−2), C(0,5) ⇒ $\frac{19}2$; with $-1\le x\le3$, $0\le y\le2$ the region has area 152.
  - (−3,2), (5,1) ⇒ 13.
  - A(3,−2), B(−1,1), C(5,4) (det −30) ⇒ region with $-1\le x\le2$, $0\le y\le3$ has area 270; region with x ≥ −1, y ≥ 1, x+y ≤ 2 has area 60.
  - A(1,0), B(−1,2), C(3,k): area 4 ⇒ k=2 or −6; collinear ⇒ k=−2. A(1,2), B(−2,4), C(−6,r) with area 4 ⇒ r=4 or $\frac{28}3$.
  - |AB|=2, |AC|=3, area $\frac{3\sqrt3}2$ ⇒ $\overrightarrow{AB}\cdot\overrightarrow{AC}=\pm3$.
  - (5,−2), (k,−4) with area 24 ⇒ $|-20+2k|=24$ ⇒ k=22 or −2.
  - Quadrilateral with $\overrightarrow{AB}=(6,1)$, $\overrightarrow{CD}=(-2,-3)$, $\overrightarrow{BC}\parallel\overrightarrow{DA}$, $\overrightarrow{AC}\perp\overrightarrow{BD}$ ⇒ area 16.
- **Areas of combinations**: $\langle p\vec a+q\vec b,r\vec a+s\vec b\rangle=(ps-qr)\langle\vec a,\vec b\rangle$.
  - $\langle3\vec a-2\vec b,4\vec b\rangle=12D=60$ ⇒ $\langle\vec a+2\vec b,4\vec a+3\vec b\rangle=-5D$ ⇒ 25.
  - Area 5 ⇒ $(2\vec a+\vec b,\vec a-3\vec b)$ → 35; $(2\vec a-\vec b,-3\vec a)$ → 15.
  - det = −5 ⇒ $(\vec a,3\vec a-2\vec b)$ → 10; $(2\vec a+\vec b,\vec a-\vec b)$ → 15 (not 30) → (2)(4).
  - $\vec c=x\vec a+y\vec b$ (x>0>y) with $[\vec a,\vec c]=3[\vec a,\vec b]$ and $[\vec b,\vec c]=2[\vec a,\vec b]$ ⇒ x=2, y=−3.
- **Evaluate**:
  - $\begin{vmatrix}3&5\\-2&8\end{vmatrix}=34$.
  - $\begin{vmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{vmatrix}=1$.
  - $\begin{vmatrix}31&58\\63&117\end{vmatrix}=-27$.
  - $\begin{vmatrix}a&b\\c&d\end{vmatrix}=2$ ⇒ $\begin{vmatrix}3a-2c&3c\\3b-2d&3d\end{vmatrix}=18$; $=5$ ⇒ scaled versions 60 and 85.
  - Integers with $\begin{vmatrix}5&a\\b&7\end{vmatrix}=4$ ⇒ ab=31 ⇒ |a+b|=32.
- **克拉瑪公式**: for $a_1x+b_1y=c_1$, $a_2x+b_2y=c_2$ with $\Delta=\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}$:
  - $\Delta\ne0$ ⇒ unique solution $x=\frac{\Delta_x}\Delta$, $y=\frac{\Delta_y}\Delta$.
  - Δ=0 and $\Delta_x=\Delta_y=0$ ⇒ infinitely many (dependent).
  - Δ=0 and $\Delta_x$ or $\Delta_y\ne0$ ⇒ none.
  - Geometrically: is $\vec c$ a combination of the columns $\vec a,\vec b$?
- 例 (Cramer):
  - $4x-y=13$, $3x+5y=4$ ⇒ (3,−1); $2x+3y=4$, $30x+31y=62$ ⇒ $(\frac{31}{14},-\frac17)$.
  - Solution (2,3) of the original ⇒ $a_ix+2b_iy=3c_i$ has $(6,\frac92)$.
  - $2x+(5-k)y=k+3$, $(5-k)x+2y=9-k$: Δ=4−(5−k)²: unique for k≠3, 7; infinitely many at k=3; none at k=7.
  - $(2-k)x+5y=0$, $3x+(4-k)y=0$ with a non-zero solution ⇒ Δ=(k−7)(k+1)=0 ⇒ k=7 or −1.
  - A k-dependent system (108 練習12): unique for k≠1, $\frac32$; infinitely many at k=1; none at $k=\frac32$.
  - $3x-4y+3z=0$ and $x-y+2z=0$ ⇒ $x:y:z=-5:-3:1$ ⇒ $\frac{x^2+y^2+z^2}{xy+yz+zx}=\frac{35}7=5$.

**Traps**:
- $\vec0$ vs 0.
- Collinearity needs α+β=1 (not just proportionality).
- Ratios of division must be checked for internal vs external.
- The dot product of perpendicular vectors is 0, but $\vec a\cdot\vec b=\vec a\cdot\vec c$ does not imply $\vec b=\vec c$.
- Area uses the **absolute value** of the determinant.
- In a projection, the coefficient is $\frac{\vec a\cdot\vec b}{|\vec b|^2}$ (squared length).
- Many answer keys in this cluster lose fractions in extraction; recompute (two genuine misprints noted above).

## 17. 空間概念（點線面關係、二面角、三垂線定理、立體圖形）

**Scope**: S-11A-1 空間概念: 空間的基本性質, 兩直線/兩平面/直線與平面的位置關係, **三垂線定理**. **Recognise 兩面角**, but apart from right angles, general dihedral angles are **not** handled geometrically in 數A; they are handled via normal vectors (G-11A-9, §19). The 108/99/資優 handouts nevertheless compute many general dihedral angles by plane geometry; treat those as practice of the law of cosines / 三垂線, and expect 學測 to use coordinates/vectors instead. **Sources**: 108二下 1-1空間概念; 99第四冊 1-1空間概念; 資優 第29單元空間概念.

### 17.1 公設與決定平面的條件
- **公設**:
  - (1) Two distinct points determine a line.
  - (2) Three non-collinear points determine a unique plane (a tripod stands steadily).
  - (3) The line through two points of a plane lies in the plane.
  - (4) Two distinct intersecting planes meet in a line.
- **A plane is determined by**:
  - (1) three non-collinear points;
  - (2) a line and a point not on it;
  - (3) two intersecting lines;
  - (4) two parallel lines.
- **Two lines**:
  - Coplanar: intersecting (angle; perpendicular if 90°) or **parallel** (coplanar, no common point).
  - Not coplanar: **歪斜線** (neither parallel nor intersecting).
  - Two skew lines have exactly one **公垂線**; its length is the distance between them.
- **Line vs plane**: lies in it (infinitely many common points), meets it at one point, or is parallel (no common point).
- **Plane vs plane**: parallel or meeting in a line (交線).
- Cuboid ABCD−EFGH: lines skew to AE are FG and FH (3)(4). Square pyramid with equilateral sides: lines skew to AD are BE and CE (3)(4).
- **True/false bank**:
  - ✓ In a plane, non-intersecting lines are parallel.
  - ✗ In space, non-intersecting lines are parallel (they may be skew).
  - ✗ Three points determine a unique plane (not if collinear).
  - ✗ Two planes can meet in a single point.
  - ✓ Exactly one plane contains two parallel lines.
  - ✓ Two distinct planes that meet do so in a line.
  - ✓ Skew lines are not coplanar.
  - ✓ A line and an external point determine one plane.
  - ✓ Through a point of a line there is exactly one plane perpendicular to the line.
  - ✗ A line and a plane always meet.
  - ✗ In a plane, any two distinct lines have a common perpendicular (not intersecting ones).
  - ✓ In space, any two distinct lines have a common perpendicular.
  - ✓ Two intersecting planes always have a common perpendicular plane.
  - ✗ Through a point of a line exactly one line is perpendicular to it (infinitely many in space).
  - ✓ Through an external point exactly one line is perpendicular to a given plane.
  - ✓ Through an external point exactly one line is parallel to a given line.
  - ✗ Through an external point exactly one line is parallel to a given plane (infinitely many).
  - ✓ (handout convention, perpendicular meaning "meets at a right angle") Through an external point exactly one line is perpendicular to a given line.
  - ✗ Lines in parallel planes are parallel.
  - ✗ Skewness is not transitive.
  - ✓ Two lines perpendicular to the same plane are parallel.
  - ✓ The projections of two skew lines onto a plane may be parallel.
  - ✗ Three planes meeting pairwise in three lines need not have those lines parallel (they may be concurrent).
  - ✗ Two lines parallel to the same plane need not be coplanar or parallel.
  - 資優 練習9 marks all six statements wrong:
    - "any two points determine a line" (they may coincide);
    - three points may be collinear;
    - a line and a point may be incident;
    - non-parallel lines may be skew;
    - the points equidistant from A, B, C form a line, not a single point;
    - a segment has infinitely many perpendicular bisectors in space (they fill a plane).

### 17.2 二面角
- **半平面**, **二面角** (稜 + 兩個面). Its size is the **plane angle** formed by two rays, one in each face, both perpendicular to the edge at the same point (independent of the point). Two intersecting planes form four dihedral angles, equal or supplementary. Perpendicular planes: 90°.
- **How to find one**: from a point on the edge (or a foot of a perpendicular) draw perpendiculars to the edge in both faces; often use isosceles triangles (medians are perpendicular to the base) or 三垂線.
- 例:
  - Cuboid 12×9×8: faces ADHE and BDHF meet along DH ⇒ angle ADB ⇒ $\tan\theta=\frac{12}9=\frac43$.
  - Square folded along diagonal BD with dihedral 60° ⇒ $\cos\angle ABC=\frac34$; if ∠ABC=60° ⇒ the planes are perpendicular (90°).
  - Tetrahedron with AD ⊥ DB and AD ⊥ DC: the dihedral angle between ABD and ACD (edge AD) is ∠BDC (2).
  - Cuboid 3, 4, 5: tetrahedron E−ABD has volume 10; dihedral angle between ABD and BDE (edge BD) has $\tan\theta=\frac{AE}{d(A,BD)}=\frac5{12/5}=\frac{25}{12}$.
  - Square pyramid with height 3 and base side 4: lateral-to-base $\tan\alpha=\frac32$; adjacent lateral faces $\cos\beta=-\frac4{13}$ (via the foot F of the perpendicular from B to OC and the law of cosines in △BFD).
  - Pyramid with all edges a: adjacent lateral faces $\cos\alpha=-\frac13$; lateral-to-base $\cos\beta=\frac1{\sqrt3}$.
  - PA=PB=PC=PD=5 on a square of side 6: lateral-to-base $\cos\theta=\frac34$, height $\sqrt7$.
  - AB=AC=AD=4, BC=CD=DB=2: dihedral angle ABC–BCD has $\cos\theta=\frac{\sqrt5}{15}$; volume $\frac{2\sqrt{11}}3$.
  - AC=AD=BC=BD=5, AB=4, CD=6 ⇒ midpoint M of CD with AM=BM=4 ⇒ $\cos\theta=\frac12$.
  - Rhombus folded into two equilateral triangles (side 2) at 60° ⇒ AD=√3, $\cos\angle ABD=\frac58$.
  - Roof: rectangle 10×8, ridge EF=6 at height 3 ⇒ $AE=\sqrt{29}$; side ADE vs base $\cos\theta=\frac2{\sqrt{13}}$.
  - Notebook: screen and keyboard as rectangles, PQ=PR=19, QR=33 ⇒ θ=∠QPR≈121°. When A, B, C form an equilateral triangle on a 33.17×20.73 laptop ⇒ ≈141°.
  - Volume via a dihedral angle: AB=3, [ABC]=15, [ABD]=12, dihedral 30° ⇒ the height from D to plane ABC is $\frac{2\cdot12}3\sin30^\circ=4$ ⇒ V=20.
  - Projection: AB=2 at 30° to the edge L, dihedral 60° ⇒ projection $A'B=\sqrt{3+\frac14}=\frac{\sqrt{13}}2$.
  - △ABC with right angle at A meeting plane E along BC at angle α, with AB, AC making angles β, γ with E ⇒ $\sin^2\alpha=\sin^2\beta+\sin^2\gamma$.
  - Two square pyramids glued (an octahedron): the two dihedral angles α, β are equal.

### 17.3 直線垂直平面、投影、線面夾角
- **L ⊥ E**: L meets E at P and is perpendicular to every line of E through P.
- **判別定理**: if L is perpendicular to **two intersecting lines** of E through P, then L ⊥ E (proof by congruent triangles and the perpendicular bisector). One line is not enough.
- **投影點** (foot of the perpendicular) and **投影直線**.
- **Angle between a line and a plane** = the angle between L and its projection L′ (two supplementary values).
- 例:
  - Square of side 2 with E the midpoint of AB; fold △ADE, △BCE so that AE and BE coincide at P ⇒ PE ⊥ PC and PE ⊥ PD ⇒ PE ⊥ plane PCD; volume $\frac13\cdot\sqrt3\cdot1=\frac{\sqrt3}3$.
  - Cuboid with PB=3, BC=4, CE=12: CE ⊥ plane ABC ⇒ CE ⊥ CP ⇒ $EP=\sqrt{9+16+144}=13$. Cuboid with AB=3, BC=2, CD=6 ⇒ AB ⊥ plane BCE ⇒ AB ⊥ BD; $DA=\sqrt{9+4+36}=7$.
  - P moving along the normal L at P of plane F with ∠ABP=90°: ∠ABP stays 90° (E) — 三垂線.
  - SB ⊥ the base of a unit square with $SB=\sqrt3$ ⇒ AD ⊥ plane SAB ⇒ $\sin\angle ASD=\frac{AD}{SD}=\frac1{\sqrt5}$.

### 17.4 三垂線定理
- **Statement**: AB ⊥ plane E at B; in E, BC ⊥ L at C ⇒ AC ⊥ L. Proof: for D on L, $AD^2=AB^2+BD^2=(AC^2-BC^2)+(BC^2+CD^2)=AC^2+CD^2$.
- **Projection view**: if L′ is the projection of a slanted line L onto E and M ⊂ E passes through the intersection, then L′ ⊥ M ⇔ L ⊥ M.
- 例:
  - Cube: P, Q, R midpoints of AD, EF, FG ⇒ PQ ⊥ QR.
  - O projects to A on E; A projects to B on L ⊂ E; C on L with BC=12, OC=13, AB=4 ⇒ OB=5, OA=3; the dihedral angle between ABC and OBC has $\cos\theta=\frac45$.
  - AH=3 (H the foot on E), HB=2 (B the foot on L), AC=7 ⇒ BC=6.
  - BC=24, $CD=24\sqrt3$ ⇒ BD=48. AB=8, BC=6, $CD=2\sqrt{11}$ ⇒ AC=10, AD=12.
  - **2013指定甲**: CD ⊥ plane ABC, AB=BC=CD=10, $\sin\angle ABC=\frac45$ (acute) ⇒ $AC^2=100+100-200\cdot\frac35=80$ ⇒ $AD=\sqrt{180}=6\sqrt5$.
  - AB=20 as a diameter, ∠CAB=60° ⇒ AC=10; a pole at A with distance 30 from its top to B ⇒ height² = 500 ⇒ rope to C $=\sqrt{600}=10\sqrt6$.
  - Tripod with equal legs PA=PB=PC ⇒ the foot O is the circumcentre; AC=7, BC=5, AB=8, PA=10 ⇒ $R=\frac7{\sqrt3}$ ⇒ $PO=\sqrt{100-\frac{49}3}=\frac{\sqrt{753}}3$.
  - Cube ABCD−EFGH with K = HF∩EG: HF ⊥ EG ✓, KB ⊥ EG ✓ (三垂線) → (B)(C).

### 17.5 立體圖形 (柱、錐、球) and folding
- Volumes: prism/cylinder = base × height; pyramid/cone = $\frac13$ base × height.
- **Regular tetrahedron** (edge a):
  - The foot of the apex is the circumcentre = centroid of the base.
  - Height $\frac{\sqrt6}3a$; volume $\frac{\sqrt2}{12}a^3$.
  - Distance between opposite edges $\frac{\sqrt2}2a$.
  - Inradius $\frac{\sqrt6}{12}a$; circumradius $\frac{\sqrt6}4a$.
- 例:
  - Regular pyramid on an 8×6 rectangle with lateral edges 13 ⇒ height 12; [OAB] $=4\sqrt{153}$.
  - **2021學測**: AB=AC=AD=$4\sqrt6$, BD=CD=8, $\cos\angle BAC=\frac13$ ⇒ distance from D to plane ABC is $4\sqrt2$.
  - Net of a square pyramid with 3-4-5 side triangles: $EF=\sqrt5$, $EG=\sqrt{21}$; EF ⊥ base (∠EFG=∠AFE=90°); volume $\frac{16\sqrt5}3$ (from 2015學測).
  - Rectangle 4×3 folded along AC into a right dihedral angle ⇒ $BD=\frac{\sqrt{337}}5$ (feet on AC are $\frac75$ apart; both heights $\frac{12}5$).
  - **2018學測**: 15×20 folded along BD into perpendicular planes ⇒ $AC=\sqrt{193+144}=\sqrt{337}$.
  - Rectangle $AB=\sqrt3$, BC=1 folded along AC with the foot of D′ on AB ⇒ $BD'=\sqrt2$.
  - **88學科**: plane through midpoints A, B, C of three cube edges cuts a non-square rectangle (D).
  - **91指定甲**: four cube vertices pairwise 1 apart (regular tetrahedron on face diagonals) ⇒ edge $\frac1{\sqrt2}$ ⇒ volume $\frac{\sqrt2}4$ (B).
  - **2019學測**: a cube with vertices on z=0 and z=6 ⇒ the distance 6 equals a, $\sqrt2a$ or $\sqrt3a$ ⇒ minimum edge $2\sqrt3$.
  - **90學科**: tetrahedron of volume 12; cutting off four corners at edge midpoints leaves an octahedron of volume $12-4\cdot\frac{12}8=6$.
  - Cuboid 12×9×8: BH = 17.

**Traps**:
- Non-intersecting ≠ parallel in space.
- To prove L ⊥ E you need two **intersecting** lines.
- In 三垂線, check which segment is perpendicular to the plane.
- A dihedral angle is measured with rays perpendicular to the edge, not with arbitrary rays.
- For 學測, prefer coordinates/normal vectors for non-right dihedral angles (§19).

## 18. 空間坐標、空間向量、內積、外積、三階行列式

**Scope**:
- G-11A-2 空間坐標系: 點坐標, 兩點距離, 點到坐標軸或坐標平面的投影.
- G-11A-3 空間向量: 係數積與加減, 線性組合.
- G-11A-7 空間向量的運算: 正射影與內積, 平行/垂直, 柯西不等式, **外積** (using 柯西 to explain the range of r is ※).
- G-11A-8 **三階行列式**: the volume of the parallelepiped spanned by three vectors, 三重積 (the volume meaning is the focus).
- Direction cosines (方向餘弦) are a 99/資優 extra.
- 三元一次方程組 / 高斯消去 are in §20.

**Sources**: 108二下 1-2空間坐標與空間向量, 1-3空間向量的內積, 1-4空間向量的外積與三階行列式; 99第四冊 1-2空間坐標, 1-3空間向量, 1-4外積與三階行列式; 資優 第30單元空間向量, 第32單元行列式 (the 2×2 and 3×3 parts).

### 18.1 空間坐標
- **Setup**:
  - **Right-handed system**: fingers point along +x and curl to +y; the thumb gives +z.
  - Point P(x,y,z); three coordinate planes, eight 卦限; a point in the xy-plane has z=0.
- **Distance and midpoint**: $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2}$; midpoint averages.
- **Projections and reflections** of P(a,b,c):
  - Onto the x-axis: (a,0,0); onto the xy-plane: (a,b,0).
  - Distance to the x-axis: $\sqrt{b^2+c^2}$; distance to the xy-plane: |c|.
  - Reflection in the xy-plane: (a,b,−c); in the z-axis: (−a,−b,c); in the origin: (−a,−b,−c).
- 例 (coordinates):
  - Cuboid with B at the origin, A(0,−3,0), F(−1,0,4) ⇒ O(−1,−3,0), C(−1,0,0), D(0,−3,4), E(0,0,4), G(−1,−3,4).
  - Cuboid A(1,0,3), G(−3,3,−4): F, distance from A to the xy-plane 3, reflection of G in the z-axis (3,−3,−4).
  - Symmetric roof (OABC 8×10, ridge DE=6 at height 3) ⇒ A(8,0,0), B(8,10,0), C(0,10,0), D(4,2,3), E(4,8,3); $AE=\sqrt{89}$.
  - **2014學測**: A(5,0,12), B(−5,0,12), P in the xy-plane with PA=PB=13 ⇒ P on x=0 with $25+y^2+144=169$ ⇒ (0,0,0) (4).
  - Regular tetrahedron of edge 2 in a cube of edge √2: $A(\sqrt2,0,0)$, $B(0,0,\sqrt2)$, $C(0,\sqrt2,0)$, $D(\sqrt2,\sqrt2,\sqrt2)$; with AE:EB=CF:FD=2:1, $EF=\frac{2\sqrt5}3$.
  - Regular tetrahedron with A(2,0,0), B(0,2,0), C(0,0,2) ⇒ D(2,2,2) or $(-\frac23,-\frac23,-\frac23)$.
  - Pyramid with slope ($\tan$ of face angle) $\frac35$ and A(5,−5,0) ⇒ B(5,5,0), C(−5,5,0), D(−5,−5,0), P(0,0,3).
  - Equilateral PQR with P(3,0,1), Q(1,1,2) and R(x,2,z) in the xy-plane: z=0, $(x-3)^2+5=6$ and $(x-1)^2+5=6$ ⇒ **x=2** only (the 108 key prints "4 或 2", but x=4 gives QR=√14).
  - P on the x-axis equidistant from A(1,2,−1), B(−3,2,1) ⇒ (−1,0,0). P in the xy-plane equidistant from A(−1,2,1), B(1,2,3), C(0,−2,3) ⇒ $(2,-\frac38,0)$.
  - Mirror xy-plane: ray from P(1,2,1) to O reflects to R with OR=2PO ⇒ R(−2,−4,2).
- **Optimisation**:
  - P in the xy-plane minimising $AP^2+BP^2$ for A(3,2,5), B(1,−4,3) ⇒ the projection of the midpoint, (2,−1,0).
  - Q on the z-axis with ∠AQB ≥ 90° ⇔ $\overrightarrow{QA}\cdot\overrightarrow{QB}\le0$ ⇔ $z^2-8z+10\le0$ ⇒ a segment of length $2\sqrt6$.
  - Unit cube with P on EF, Q on BC, EP=BQ=t ⇒ $PQ^2=(1-t)^2+t^2+1$ ⇒ min $\frac{\sqrt6}2$ at $t=\frac12$.

### 18.2 空間向量 (same algebra as §16)
- $\overrightarrow{AB}=(b_1-a_1,b_2-a_2,b_3-a_3)$, $|\vec a|=\sqrt{a_1^2+a_2^2+a_3^2}$. Addition, scalar multiples, **parallel** ⇔ proportional components, unit vectors, **division points**, centroid, linear combinations.
- In space, three non-coplanar vectors are a basis; any vector is uniquely $x\vec a+y\vec b+z\vec c$.
- 例:
  - A(2,3,−4), B(1,1,−2), C(−2,7,−6) with AB=3, AC=6 ⇒ internal bisector foot $D(0,3,-\frac{10}3)$; external E(4,−5,2).
  - A(5,2,4), B(a,b,5), C(2,−1,7) collinear ⇒ (a,b)=(4,1), AB:BC=1:2.
  - $\overrightarrow{OA}=(2,3,-6)$ (length 7), $\overrightarrow{OB}=(1,-2,2)$ (length 3); $\overrightarrow{OA}+t\overrightarrow{OB}$ bisects ∠AOB ⇒ $t=\frac73$.
  - Three cube vertices A(5,2,9), B(1,6,5), C(3,4,1): distances $4\sqrt3$, $2\sqrt6$, $6\sqrt2$ in ratio $\sqrt2:1:\sqrt3$, so the edge is $2\sqrt6$ and AC is the space diagonal ⇒ centre (4,3,5). P in plane ABC with $\overrightarrow{AP}=\frac25\overrightarrow{AB}+t\overrightarrow{AC}$ is inside △ABC ⇔ $0<t<\frac35$.
  - Parallelepiped ABCD−EFGH with J the centre of BCGF: $\overrightarrow{AJ}=\overrightarrow{AB}+\frac12\overrightarrow{AD}+\frac12\overrightarrow{AE}$ ⇒ a+b+c=2, a=1, a=2c → (2)(3)(4).
  - [APB]:[BPC]:[CPA]=3:4:5 ⇒ $\overrightarrow{AP}=\frac5{12}\overrightarrow{AB}+\frac14\overrightarrow{AC}$; with A(−2,0,6), B(0,4,3), C(3,5,7) ⇒ $P(\frac1{12},\frac{35}{12},5)$.
  - **2016學測**: cuboid with P on plane BDG, $\overrightarrow{AP}=\frac13\overrightarrow{AB}+2\overrightarrow{AD}+a\overrightarrow{AE}$. In unit-edge coordinates the plane BDG is x+y−z=1 ⇒ $a=\frac43$. (Equivalently, the coefficients for B, D, G sum to 1.)
- **方向角 / 方向餘弦** (99/資優): $\cos\alpha=\frac a{|\vec v|}$, etc.; $\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1$; $\sum\sin^2=2$.
  - (1,−2,5) ⇒ $\frac1{\sqrt{30}}(1,-2,5)$.
  - A(0,−3,1), B(4,1,t) with α=π/3 ⇒ |AB|=8 ⇒ $t=1\pm4\sqrt2$, $\gamma=\frac\pi4$ or $\frac{3\pi}4$.
  - |v|=10 at angles $\frac\pi3,\frac\pi4,\frac\pi3$ ⇒ $(5,5\sqrt2,5)$.
  - $\cos\alpha+2\cos\beta-2\cos\gamma\in[-3,3]$ (Cauchy).

### 18.3 內積 (space)
- $\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta=a_1b_1+a_2b_2+a_3b_3$ (proof via the law of cosines). The same properties and uses as §16: angle, length, $\perp$, 正射影 $\frac{\vec a\cdot\vec b}{|\vec b|^2}\vec b$, area $\frac12\sqrt{|\vec a|^2|\vec b|^2-(\vec a\cdot\vec b)^2}$.
- **柯西 (3D)**: $(a_1b_1+a_2b_2+a_3b_3)^2\le(a_1^2+a_2^2+a_3^2)(b_1^2+b_2^2+b_3^2)$; ※ explains $|r|\le1$ for 相關係數 (viewing the deviations as n-dimensional vectors).
- 例:
  - A(1,0,6), B(4,5,−2), C(7,3,4): $\overrightarrow{AB}\cdot\overrightarrow{AC}=49$, ∠A=45°, projection (6,3,−2), area $\frac{49}2$, distance from B to AC is 7.
  - $\vec c\perp(1,2,3)$ and $(-2,4,5)$ ⇒ $p:q:r=2:11:(-8)$ (a cross product).
  - P on the y-axis with $\overrightarrow{PA}\perp\overrightarrow{PB}$ for A(1,2,3), B(2,2,−1) ⇒ (0,1,0) or (0,3,0).
  - $\vec a=(1,2,\lambda-1)$, $\vec b=(4,1,-\lambda)$, $\vec c=(-1,2,\lambda+3)$ pairwise perpendicular ⇒ λ=−2.
  - $\vec c\perp(1,-1,-1)$ at 60° to (2,−1,3) with $|\vec c|=\sqrt{14}$ ⇒ (3,2,1) or (−1,−3,2).
  - $\vec a=(2,-3,6)$, $\vec a\cdot\vec b=14$ ⇒ $|\vec b|\ge2$.
  - Cuboid AB=4, AD=2, AE=3: $\overrightarrow{AC}\cdot\overrightarrow{AF}=16$; the acute angle between diagonals AG and BH has $\cos\alpha=\frac3{29}$; $[FAC]=\frac12\sqrt{20\cdot25-16^2}=\sqrt{61}$.
  - Regular tetrahedron of edge 2 with E, F, G the midpoints of AB, AC, CD: $\overrightarrow{AB}\cdot\overrightarrow{AC}=2$; $\overrightarrow{GE}=\frac12\overrightarrow{AB}-\frac12\overrightarrow{AC}-\frac12\overrightarrow{AD}$; $\overrightarrow{GE}\cdot\overrightarrow{GF}=1$.
  - O−ABC regular with edge 2 and P on OA with $\overrightarrow{OA}\cdot\overrightarrow{PB}=1$ ⇒ $OP=\frac14OA$, $\overrightarrow{PB}=-\frac14\vec a+\vec b$.
  - Rhombohedron (edges a, all face angles 60°) ⇒ $AH=|\vec a+\vec b+\vec c|=\sqrt6a$.
  - Squares ABCD, ABEF of side 4 with $\overrightarrow{AD}\cdot\overrightarrow{AF}=20$ ⇒ $\overrightarrow{AC}\cdot\overrightarrow{AE}=16+20=36$.
  - P, Q, R, S with PQ, QR, RS, ∠PQR=120°, ∠QRS=150°, $\overrightarrow{PQ}$ at 30° to $\overrightarrow{RS}$ ⇒ $|PS|^2=|\overrightarrow{PQ}+\overrightarrow{QR}+\overrightarrow{RS}|^2$.
  - **86自**: AB=1, BC=2, CD=3 with both angles 120° and $\overrightarrow{AB}$ at 60° to $\overrightarrow{CD}$ ⇒ $|AD|^2=14+2(1+3+\frac32)=25$ ⇒ AD=5.
  - **2017學測**: in a tetrahedron, $\overrightarrow{DB}\cdot\overrightarrow{DC}=\overrightarrow{AB}\cdot\overrightarrow{AC}+|AD|^2$ (when AD ⊥ AB, AC) ⇒ if ∠BAC is acute then ∠BDC is acute ✓; if AB<DA and AC<DA then ∠BDC is acute ✓ → (3)(5).
  - **2005學科**: unit cube, $\overrightarrow{AP}=\frac34\overrightarrow{AB}+\frac12\overrightarrow{AD}+\frac23\overrightarrow{AE}$ ⇒ distance to line AB $=\sqrt{\frac14+\frac49}=\frac56$.
  - 2002學科 / 2006學科 / 91學科 / 95學科: angles inside a cube via coordinates (e.g. cos∠MON with M, N on edges and O the centre) — set up coordinates at a vertex.
- **柯西 optimisation**:
  - $3x^2+y^2+2z^2=6$ ⇒ $x+2y+3z\in[-\sqrt{53},\sqrt{53}]$.
  - a+b+c=4 ⇒ $(a+1)^2+(b-2)^2+c^2-4\ge\frac{3^2}3-4=-1$.
  - Inside a 3-4-5 triangle with distances x, y, z to the sides: $3x+4y+5z=12$ ⇒ $x^2+y^2+z^2\ge\frac{144}{50}=\frac{72}{25}$.
  - Equilateral triangle of side $2\sqrt3$: x+y+z=3 ⇒ min $x^2+y^2+z^2=3$; max $\sqrt x+\sqrt y+\sqrt z=3$.
  - |OP|=3 with positive coordinates ⇒ $[OAB]+[OBC]+[OCA]=\frac12(ab+bc+ca)\le\frac92$.
  - $x^2+y^2+(2x-3y-2)^2\ge\frac27$ at $(\frac27,-\frac37)$.
  - Cuboid with surface area 8 and total edge length k ⇒ $k\ge8\sqrt3$.

### 18.4 外積 (cross product)
- **Definition** (from 力矩): $\vec a\times\vec b$ is a vector with:
  - length $|\vec a||\vec b|\sin\theta$ = the area of the parallelogram spanned;
  - direction perpendicular to both, with $\vec a,\vec b,\vec a\times\vec b$ right-handed;
  - $\vec0$ if the vectors are parallel.
  - $\vec i\times\vec j=\vec k$, $\vec j\times\vec k=\vec i$, $\vec k\times\vec i=\vec j$.
- **Components**: $\vec a\times\vec b=\left(\begin{vmatrix}a_2&a_3\\b_2&b_3\end{vmatrix},\begin{vmatrix}a_3&a_1\\b_3&b_1\end{vmatrix},\begin{vmatrix}a_1&a_2\\b_1&b_2\end{vmatrix}\right)$ (derived by Cramer from the two ⊥ equations; λ=1 is fixed by the length and right-handedness). All common perpendiculars are parallel to it.
- **Properties**:
  - Anti-commutative $\vec a\times\vec b=-\vec b\times\vec a$; scalars pull out; distributive.
  - **Not associative.**
  - $\vec a\times\vec a=\vec0$; $(\vec a\times\vec b)\perp\vec a,\vec b$.
- 例:
  - A(1,2,1), B(0,6,4), C(3,5,6): $\overrightarrow{AB}\times\overrightarrow{AC}=(11,11,-11)$ ⇒ unit normal $\pm\frac1{\sqrt3}(1,1,-1)$.
  - A(2,1,3), B(5,−2,4), C(3,2,1): cross product (5,7,6) ⇒ area $\frac{\sqrt{110}}2$.
  - (−1,2,3)×(4,6,−1) = (−20,11,−14) ⇒ $[AOB]=\frac{\sqrt{717}}2$.
  - (1,1,2)×(1,2,3) = (−1,−1,1) ⇒ a common perpendicular of length $2\sqrt3$ is ±(2,2,−2).
  - (2,1,−3)×(3,2,−4) = (2,−1,1); (0,−4,1)×(−4,0,1) = (−4,−4,−16).
  - (−3,2,0) and (0,−2,1): a common perpendicular of length 7 is ±(2,3,6).
  - (1,3,2)×(3,0,2) = (6,4,−9) (the reverse order is the negative); area $\sqrt{133}$; volume with (1,−1,3) is 25.
  - **Cube via cross product**: $\overrightarrow{AB}=(0,3,3)$, $\overrightarrow{AD}=(\sqrt2,2\sqrt2,-2\sqrt2)$ ⇒ $\overrightarrow{AE}=\pm\frac{3\sqrt2}{18}\overrightarrow{AB}\times\overrightarrow{AD}=\pm(4,-1,1)$ (sign from the figure's orientation).
  - **Regular octahedron**: $\overrightarrow{AB}\times\overrightarrow{AC}=(6,12,-12)$ (length 18) ⇒ edge $3\sqrt2$ ⇒ $\overrightarrow{EF}$, the opposite diagonal of length 6, is $-\frac13(6,12,-12)=(-2,-4,4)$.
- **True/false** (108 習題3): with $\vec a=(-1,3,5)$, $\vec b=(0,3,-1)$, $\vec c=(3,6,-2)$:
  - ✗ $\vec a\times\vec b=(18,1,3)$ (the correct value is (−18,−1,−3)).
  - ✗ "$\vec b\times\vec c$ equals $|\vec b||\vec c|\sin\theta$" (that is its length, not the vector).
  - The volume is 54 ✓.
  - $(\vec a\times\vec b)\perp(2\vec a-3\vec b)$ ✓.
  - → (4)(5).
- **2018指定甲**: $\vec a\times\vec b=\vec c$, $\vec a\times\vec c=\vec d$, lengths of a, b, c all 4:
  - $\sin\theta=\frac14$.
  - Volume $=|\vec c|^2=16$ ✓.
  - $\vec a,\vec c,\vec d$ are pairwise perpendicular ✓.
  - |d| = 16.
  - The angle between b and d is $\theta+\frac\pi2$.
  - → (2)(3).
- **2013指定甲**: $\vec u=(a,b,0)$, $\vec v=(c,d,1)$ on unit circles:
  - $\vec v$ makes 45° with +z always ✓.
  - $\vec u\cdot\vec v=ac+bd\le1$ (not √2).
  - The maximum angle is 135° ✓ (cos ≥ $-\frac1{\sqrt2}$).
  - $|ad-bc|\le1$.
  - $|\vec u\times\vec v|=\sqrt2\sin\alpha$, max $\sqrt2$ at α=90° ✓.
  - → (1)(3)(5).
- $\vec a\times\vec b=\vec c$, $\vec b\times\vec c=\vec a$, $\vec c\times\vec a=\vec b$ (non-zero) ⇒ pairwise perpendicular unit vectors.

### 18.5 平行六面體體積、三階行列式
- **Volume**: the parallelepiped spanned by $\vec a,\vec b,\vec c$ has volume (base area $|\vec b\times\vec c|$) × (height $|\vec a\cos\varphi|$) $=|\vec a\cdot(\vec b\times\vec c)|$, which is cyclic: $=|\vec b\cdot(\vec c\times\vec a)|=|\vec c\cdot(\vec a\times\vec b)|$. The sign is + when $\vec a$ is on the same side as $\vec b\times\vec c$.
- Tetrahedron volume $=\frac16$ of the parallelepiped.
- **三階行列式**: $\begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}=\vec a\cdot(\vec b\times\vec c)$.
  - Expansion along any row or column with signs $(-1)^{i+j}$ times minors (降階).
  - 直接展開 (Sarrus): $(a_1b_2c_3+a_2b_3c_1+a_3b_1c_2)-(a_3b_2c_1+a_2b_1c_3+a_1b_3c_2)$.
- **Properties** (each with a volume meaning):
  - (1) Transpose invariance.
  - (2) A common factor of a row/column comes out.
  - (3) Swapping two rows changes the sign.
  - (4) Proportional rows give 0.
  - (5) Adding a multiple of one row to another changes nothing (shear).
  - (6) Split a row that is a sum.
  - **Computation tips**: create zeros with (5), then expand; factor out common factors; use arithmetic-progression rows; when the row sums are equal, add all columns to one, then factor.
- 例 (evaluate):
  - 例題5 evaluates one 3×3 determinant three ways (direct, column, row expansion) = −280; the 1..9 matrix gives 0.
  - $\begin{vmatrix}1&1&1\\a&b&c\\a^2&b^2&c^2\end{vmatrix}=(b-a)(c-a)(c-b)$ (**Vandermonde**). $\begin{vmatrix}1&1&1\\2&3&4\\4&9&16\end{vmatrix}=2$. $\begin{vmatrix}1&1&1\\x&5&-3\\x^2&25&9\end{vmatrix}=0$ ⇒ x=5 or −3.
  - $\begin{vmatrix}a+b&a&a\\a&a+b&a\\a&a&a+b\end{vmatrix}=3ab^2+b^3$; $\begin{vmatrix}x+3&x&x\\x&x+3&x\\x&x&x+3\end{vmatrix}=0$ ⇒ x=−1.
  - $\begin{vmatrix}b+c&a&a\\b&c+a&b\\c&c&a+b\end{vmatrix}=4abc$; $\begin{vmatrix}1&1&1\\a&b&c\\bc&ca&ab\end{vmatrix}=(a-b)(b-c)(c-a)$.
  - $\begin{vmatrix}a+b+2c&a&b\\c&b+c+2a&b\\c&a&c+a+2b\end{vmatrix}=2(a+b+c)^3$.
  - $\begin{vmatrix}b^2+c^2&ab&ac\\ab&c^2+a^2&bc\\ac&bc&a^2+b^2\end{vmatrix}=4a^2b^2c^2$.
  - Circulant $\begin{vmatrix}a&b&c\\b&c&a\\c&a&b\end{vmatrix}=-(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$; =0 with a+b+c=15 ⇒ a=b=c=5 ⇒ area $\frac{25\sqrt3}4$.
- **Transforming determinants**:
  - 例題7: a determinant of value 5 with its columns recombined ⇒ 55.
  - D=7 ⇒ 42, 0, 91 for combined columns.
  - D₁=−2 and D₂=4 combine linearly to −12 and −108.
  - Determinant 1 transformed ⇒ −20.
- **Volumes of combinations**: multiply by the determinant of the coefficient matrix.
  - $(2\vec a-3\vec b,3\vec b+4\vec c,\vec c)$ ⇒ $\begin{vmatrix}2&-3&0\\0&3&4\\0&0&1\end{vmatrix}=6$ ⇒ 6·5=30.
  - $(2\vec a-3\vec b,3\vec b+4\vec c,\vec c-5\vec a)$ ⇒ 66 ⇒ 330.
  - $(3\vec a,-2\vec b,-\vec c)$ ⇒ 6V.
  - $(\vec a-\vec c,2\vec b+3\vec c,\vec a-\vec b)$ ⇒ det 5 ⇒ the tetrahedron has $\frac{5V}6$.
  - $(2\vec a,\vec b,3\vec c)$ ⇒ 6V; $(\vec a,2\vec a+\vec b,\vec c)$ ⇒ V.
- 例 (volumes):
  - (0,3,2), (2,2,4), (3,1,−1) ⇒ 34.
  - (1,−2,−1), (2,2,1), (−1,k,1) span volume 6 ⇒ k=0 or −4.
  - A(1,−1,0), B(0,1,0), C(2,3,4), D(−1,1,3) ⇒ parallelepiped 26, tetrahedron $\frac{13}3$.
  - A(1,0,1), B(5,1,−5), C(0,2,1), D(2,4,5) ⇒ 72, 12, $[ABC]=\frac{3\sqrt{29}}2$.
  - A(2,0,−1), B(3,1,4), C(−2,5,2), D(1,4,−3) ⇒ parallelepiped 88, tetrahedron $\frac{44}3$.
  - Cube of edge 6 with P the midpoint of EF, Q with BQ:QF=1:2, R with CR:RG=2:1 ⇒ $\overrightarrow{AP}=(3,0,6)$, $\overrightarrow{AQ}=(6,0,2)$, $\overrightarrow{AR}=(6,6,4)$ ⇒ det 180 ⇒ tetrahedron APQR has volume 30.
  - Max of $\begin{vmatrix}1&2&2\\a&b&c\\x&y&z\end{vmatrix}$ with $a^2+b^2+c^2=1$, $x^2+y^2+z^2=4$ ⇒ $|\vec u||\vec v||\vec w|=3\cdot1\cdot2=6$ (attained when the vectors are mutually perpendicular).
- **Coplanarity and concurrency**:
  - A, B, C, D coplanar ⇔ $\overrightarrow{AB}\cdot(\overrightarrow{AC}\times\overrightarrow{AD})=0$.
    - A(0,1,3), B(1,3,6), C(3,1,t), D(−1,t,7) ⇒ $-t^2+11t-30=0$ ⇒ t=5 or 6.
    - A(0,1,2), B(3,1,4), C(1,2,3), D(4,1,k): the given tetrahedron volume ⇒ $k=\frac{28}3$ or 0; A, B, D, E(k,−1,2) coplanar ⇒ k=14.
    - A(−1,2,1), B(2,−1,2), C(1,2,3), D(−t−1,t,1): volume |2t+8|; tetrahedron 10 ⇒ t=26 or −34.
  - Three lines $a_ix+b_iy=c_i$ concurrent ⇒ $\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}=0$ (necessary).
    - $(1-k)x+2y=3$, $x+(2-k)y=3$, $x+2y=3-k$ ⇒ k=6.
    - $x+ky=1$, $kx+5y=2k$, $-3x+2y=13$ ⇒ $19k^2+2k-80=0$ ⇒ k=2 or $-\frac{40}{19}$.
  - Line through two points as a determinant: $\begin{vmatrix}x&y&1\\x_1&y_1&1\\x_2&y_2&1\end{vmatrix}=0$; plane through three points: $\begin{vmatrix}x-a_1&y-a_2&z-a_3\\b-a&\cdots\\c-a&\cdots\end{vmatrix}=0$.
- **2016指考甲**: $\vec w\parallel\vec u\times\vec v=(-2,4,-2)$ with $\begin{vmatrix}1&2&3\\1&0&-1\\x&y&z\end{vmatrix}=-12$ ⇒ $\vec w=(1,-2,1)$.
- **88學科**: which determinants equal the original → transpose (B), and the column operation $(b_i-c_i)$ (C).
- **89學科**: a 3×3 determinant in x expands to a cubic f(x) with roots 1, 2, −3 → (A)(B)(C)(D).

**Traps**:
- The cross product is a vector and its order matters.
- Volume = |triple product| (absolute value); a tetrahedron is ⅙ of it.
- A determinant changes sign under a row swap.
- Coplanarity of four points needs three difference vectors from the same point.
- Concurrency via the 3×3 determinant also needs the lines not parallel.

## 19. 平面方程式、空間直線方程式（附：球面）

**Scope**:
- G-11A-9 平面方程式: 法向量與標準式, **兩平面的夾角**, **點到平面的距離**.
- G-11A-10 空間直線: 參數式與比例式, 直線與平面的關係, **點到直線距離**, **兩平行或歪斜線的距離**.
- General dihedral angles are computed here via normal vectors (not by plane geometry, §17).
- **[超出數A]** 球面方程式 (資優34; 99 數學IV). 數B touches 球面經緯線 (S-11B-1) only.

**Sources**: 108二下 2-1平面方程式, 2-2空間中的直線方程式; 99第四冊 2-1平面方程式, 2-2空間中直線方程式; 資優 第31單元空間中的平面與直線, 第34單元球面.

### 19.1 平面方程式
- **法向量** $\vec n$: any non-zero vector along a perpendicular of E; any $k\vec n$ also works; every vector lying in E is ⊥ $\vec n$.
- **點法式**: through $A(x_0,y_0,z_0)$ with normal (a,b,c) ⇒ $a(x-x_0)+b(y-y_0)+c(z-z_0)=0$ (from $\overrightarrow{AP}\cdot\vec n=0$).
- **一般式** $ax+by+cz+d=0$ has normal (a,b,c).
- Special planes:
  - xy-plane z=0; $z=5$ parallel to xy; $x=2$ has normal (1,0,0).
  - $2x+3y=6$ is a plane **parallel to the z-axis** (not a line).
  - $2x+z=6$ has normal (2,0,1).
- **截距式**: intercepts a, b, c ⇒ $\frac xa+\frac yb+\frac zc=1$.
- **Three points**: normal $=\overrightarrow{AB}\times\overrightarrow{AC}$. A(3,−1,1), B(4,2,−1), C(7,0,3) ⇒ (8,−10,−11).
- 例:
  - Through (−2,3,−4) with normal (3,2,−1) ⇒ $3x+2y-z=4$; through (2,−3,1) with (2,−3,4) ⇒ $2x-3y+4z=17$; through (−1,3,2) with (−4,1,3) ⇒ $4x-y-3z+13=0$.
  - B(5,−2,6) projects onto E at A(4,2,−1) ⇒ normal $\overrightarrow{AB}$ ⇒ $x-4y+7z+11=0$.
  - Perpendicular bisector plane of P(2,1,3), Q(4,5,5) ⇒ $x+2y+z=13$. Point (1,2,3) projecting to (2,3,4) ⇒ $x+y+z=9$.
  - Intercepts 2, −1, 3 ⇒ $3x-6y+2z=6$.
  - Cuboid with G(2,4,3) ⇒ plane BDE: $6x+3y+4z=12$; cuboid 4×3×2 ⇒ CFH: $2x+2y+5z=14$; cube of edge 2 with P, Q, R midpoints ⇒ $x+y+z=3$ (it also passes through the midpoints of BF, BC, CD — a regular hexagonal cross-section).
  - (2,7,3), (4,6,2), (5,6,1) ⇒ $x+y+z=12$.
  - A(1,2,1), B(0,−1,1), C(−1,0,0) ⇒ $3x-y-4z=-3$, area $\frac{\sqrt{26}}2$; D(4,3,k) coplanar ⇒ k=3.
  - Parallel to $3x+2y+z+11=0$ with intercept sum 22 ⇒ $3x+2y+z=12$.
  - Normal (3,−2,1) with intercept sum 13 ⇒ $15x-10y+5z=78$.
  - G(−1,2,−3) is the centroid of the intercept triangle ⇒ intercepts −3, 6, −9 ⇒ $6x-3y+2z+18=0$.
  - Parallel to $x-3y+12z-5=0$ cutting off a tetrahedron of volume 1 ⇒ $x-3y+12z=\pm6$.
  - **Through a point, minimising the cut-off tetrahedron**: through P(2,3,4) ⇒ $\frac2a+\frac3b+\frac4c=1$ ⇒ AM–GM gives $V=\frac{abc}6\ge108$ at a=6, b=9, c=12.
  - Containing A(2,3,1), B(3,−1,0) and parallel to the z-axis ⇒ normal ⊥ (1,−4,−1), (0,0,1) ⇒ $4x+y=11$. Parallel to z with x-, y-intercepts 3, 4 ⇒ $4x+3y=12$.
  - **Perpendicular to two planes through P(1,1,1)**: normal $=\vec n_1\times\vec n_2$ with (3,1,−1), (4,−2,−1) ⇒ $3x+y+10z=14$.
  - Through A(2,1,−1), B(1,1,2) and ⊥ $7x+4y-4z=0$ ⇒ normal $\overrightarrow{AB}\times(7,4,-4)\parallel(12,-17,4)$ ⇒ $12x-17y+4z=3$.
  - Through (1,−2,1) and ⊥ both $x+2y-z+1=0$ and $x-y+z-1=0$ ⇒ $x-2y-3z=2$.
  - Containing A(−1,1,0), B(3,2,1) and ⊥ $x+y-z=5$ ⇒ $2x-5y-3z+7=0$.
  - $E_1\parallel E_2$: $\frac{a-1}2=\frac21=\frac{b-2}3$ ⇒ (a,b)=(5,8).
- **True/false about $ax+by+cz+d=0$**:
  - Through O ⇒ d=0 ✓.
  - a=0 ⇒ E ⊥ yz-plane ✓.
  - b=0 ⇒ E ∥ xz-plane ✗ (it is ⊥ the xz-plane).
  - b=c=0 ⇒ E ⊥ yz-plane ✗ (it is parallel to it).
  - E ∥ xy-plane ⇒ a=b=0 and d ≠ 0 ✓ (if not the xy-plane itself).
  - → (1)(2)(5).
- **2019學測**: plane P through O, (1,2,3), (−1,2,3) ⇒ $3y-2z=0$: ⊥ the xy-plane? ✗; (0,4,6) on P ✓; contains the x-axis ✓; distance from (1,1,1) is $\frac1{\sqrt{13}}$ → (3)(4).
- **2006指定甲**: A(−2,7,15), B(1,16,3), C(10,7,3) ⇒ plane $x+y+z=20$; circumcentre (3,9,8) (solve the two equal-distance equations together with the plane).
- **Orthocentre**: A(0,1,2), B(−1,0,3), C(1,2,3) ⇒ plane $x-y+1=0$, H(0,1,1) (use $\overrightarrow{AH}\cdot\overrightarrow{BC}=0$, $\overrightarrow{BH}\cdot\overrightarrow{AC}=0$ and H in the plane).

### 19.2 兩平面的夾角
- The angle between planes = the angle θ between the normals, together with 180°−θ: $\cos\theta=\pm\frac{\vec n_1\cdot\vec n_2}{|\vec n_1||\vec n_2|}$. Perpendicular ⇔ $\vec n_1\cdot\vec n_2=0$.
- 例:
  - $x+2y+3z=7$ and $2x-3y-z=5$ ⇒ 60°/120°.
  - $x-2y+3z=0$ and $2x+y-4z=2$ ⇒ $\cos\theta=\pm\frac{2\sqrt6}7$.
  - $2x+y-z=4$ vs the xy-plane ⇒ $\sin\alpha=\frac{\sqrt{30}}6$.
  - Notebook: C(1,2,0), D(3,5,0), E(2,−4,5) ⇒ plane CDE $3x-2y-3z+1=0$; its angle with the keyboard (xy-plane) has $\cos\theta=\pm\frac3{\sqrt{22}}$.
  - **2015學測**: square pyramid with all face slopes $\frac25$ (half-side 5, height 2) ⇒ adjacent face normals (2,0,5), (0,2,5) ⇒ $|\cos|=\frac{25}{29}$.
  - Through A(0,−1,0), B(0,0,1) at 60° to $y-z-2=0$ ⇒ $\pm\sqrt6x+y-z+1=0$ (written $\pm\sqrt6x-y+z=1$).
  - Through A(1,−1,1), B(−1,3,1) at 45° to $x+y+1=0$ ⇒ normal (2,1,c) with $\frac3{\sqrt2\sqrt{5+c^2}}=\frac1{\sqrt2}$ ⇒ c=±2 ⇒ $2x+y+2z-3=0$ or $2x+y-2z+1=0$.
  - Angle 60° between $x+ky+z-2=0$ and $x+\sqrt2y-z+1=0$ ⇒ $k=\pm\sqrt2$.
  - Line of intersection L of E: x+y+z=2 with the xy-plane; rotate E about L to pass through (3,1,4) ⇒ use the pencil $x+y-2+\lambda z=0$ ⇒ λ = −½ ⇒ $2x+2y-z-4=0$. (The 108 key prints "+z"; check: the point satisfies only the "−z" version.)
- **Angle bisector planes**: $\frac{a_1x+b_1y+c_1z+d_1}{|\vec n_1|}=\pm\frac{a_2x+\dots}{|\vec n_2|}$.
  - $7x-y+2z+10=0$ and $4x+4y-8z+3=0$ ⇒ $16x-16y+32z+31=0$, $40x+8y-16z+49=0$.
  - $x-2y+2z-5=0$ and $2x+y-2z+3=0$ ⇒ $3x-y-2=0$, $x+3y-4z+8=0$.
- **Plane pencil** (planes through the line of intersection of E₁, E₂): $E_1+\lambda E_2=0$.
  - Through the intersection of $x+y-z+2=0$, $x+z-3=0$ and through (0,0,2) ⇒ $x+y-z+2=0$.
  - Through the intersection of $3x+2y-2z+1=0$, $x+y-5z-6=0$ and parallel to $4x+2y+3z+1=0$ ⇒ $37x+28y-68z-51=0$.
  - Containing a line and ⊥ a plane: L through (1,−2,2) with direction (2,3,−1), ⊥ $x-y+z=3$ ⇒ $2x-3y-5z+2=0$; containing L and P(−2,1,3) ⇒ $6x+y+15z-34=0$.

### 19.3 點到平面的距離
- $d(P,E)=\frac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}$ (the projection of $\overrightarrow{QP}$ onto $\vec n$). Parallel planes: $\frac{|d_1-d_2|}{\sqrt{a^2+b^2+c^2}}$ (after matching coefficients).
- 例:
  - (5,−2,−4) to $3x+2y+z-21=0$ ⇒ $\sqrt{14}$.
  - (5,0,8) to $2x-y+2z+1=0$ ⇒ 9.
  - $2x+2y+z-7=0$ vs $4x+4y+2z-1=0$ ⇒ $\frac{13}6$.
  - Parallel to $2x-y-2z+3=0$ at distance 1 ⇒ constant 0 or 6.
  - $x-2y+2z-1=0$ and $x-2y+2z+k=0$ at distance 7 ⇒ k=20 or −22.
  - Tetrahedron A(−1,3,3), B(1,3,4), C(3,−5,−5), D(2,2,7): plane ABC $2x+5y-4z=1$ ⇒ height from D $=\frac{15}{3\sqrt5}=\sqrt5$.
  - Plane ⊥ PQ (P(2,1,−1), Q(3,−2,1)) with R(1,1,2) at distance $2\sqrt{14}$ ⇒ $x-3y+2z=30$ or −26.
  - Cube of edge 5 with the corner APQR cut off (AP=4, AQ=AR=2): plane $\frac x4+\frac y2+\frac z2=1$ is $\frac43$ from A ⇒ standing on PQR, the far vertex is at height 7 m.
- **Line meeting a plane — ratio**: AP:BP = d(A,E):d(B,E) (external if both points are on the same side).
  - A(1,2,−3), B(1,−1,0), $x+y-2z+3=0$ ⇒ 12:3 = 4:1.
  - A(−2,5,4), B(1,4,−5), $2x-y+2z+4=0$ ⇒ 3:8.
- **Inscribed sphere of a corner tetrahedron**: intercepts 6, 4, 2 ($2x+3y+6z=12$) ⇒ surface area 12+4+6+14=36, $r=\frac{3V}S=\frac23$. Unit-corner tetrahedron x+y+z ≤ 1 ⇒ $r=\frac{3-\sqrt3}6$ (87大學自).
- **Reflection/projection of a point**: A(−4,0,−6) on $3x-y+2z-4=0$ ⇒ foot (2,−2,−2), mirror (8,−4,2). P(2,5,−3) on $x-3y-z-12=0$ ⇒ (4,−1,−5), (6,−7,−7).
- **Minimum distance-squared** from a fixed point to points of a plane = d². $(x_0+5)^2+(y_0-1)^2+(z_0+3)^2$ for points on a plane is the squared distance from (−5,1,−3).
- **2020指定甲** cube ($D(0,0,0)$, A(1,0,0), C(0,1,0), H(0,0,1); P the midpoint of CG, Q on BF with BQ=t, R on DH; AQPR a parallelogram):
  - $\overrightarrow{AR}=(-1,0,\frac12-t)$.
  - Pyramid G−AQPR has constant volume $\frac16$.
  - At $t=\frac14$, the distance from G to the plane is $\frac23$.

### 19.4 空間直線
- **方向向量**: any vector along the line (all parallel); slope m in 2D ↔ (1,m).
- **參數式** $(x,y,z)=(x_0,y_0,z_0)+t(a,b,c)$; segment AB: $\overrightarrow{OA}+t\overrightarrow{AB}$, 0 ≤ t ≤ 1; ray: t ≥ 0.
- **比例式** $\frac{x-x_0}a=\frac{y-y_0}b=\frac{z-z_0}c$; a zero denominator means that coordinate is constant (write "$\frac{x+1}3=\frac{z-5}4$, y=3").
- **兩面式**: the intersection of two planes; direction $\vec n_1\times\vec n_2$.
  - $3x-6y-2z=15$, $2x+y-2z=5$ ⇒ direction (14,2,15), point (3,−1,0).
  - $x+3y-z+4=0$, $2x+5y+z+1=0$ ⇒ direction (8,−3,−1).
- Which represent lines: two independent planes ✓; a parametrisation with one parameter ✓; a 比例式 ✓; one equation $3x+2y=1$ in space is a plane ✗; three planes may give a point.
- 例:
  - Perpendicular from A(1,2,4) to $2x-3y+2z=6$: $(1+2t,2-3t,4+2t)$.
  - A(−1,4,3), B(2,3,5): line $(-1+3t,4-t,3+2t)$; segment for 0 ≤ t ≤ 1.
  - A(−2,4,7), B(1,−3,5): $\frac{x+2}3=\frac{y-4}{-7}=\frac{z-7}{-2}$; check C(4,−10,3), D(1,−3,0).
  - Through (3,3,−1) parallel to the y-axis: x=3, y=3+t, z=−1.
  - Through (9,8,7) parallel to the intersection line of two given planes (108 習題1) ⇒ direction (7,1,−17).
  - Through (11,4,−6) perpendicular to (meeting) a given line ⇒ $\frac{x-11}4=\frac{y-4}3=\frac{z+6}{-2}$.

### 19.5 直線與直線、直線與平面
- **Two lines**: parallel/coincident (directions parallel; test a point), intersecting (solve the parameters), or **skew** (no common point, directions not parallel).
  - $(3+2t,-1+3t,2-t)$ and $(1+4t,-4+6t,3-2t)$ coincide.
  - $(1+2t,-5+4t,-1+t)$ and $(1+4t,1+2t,-2+4t)$ are skew.
  - **2016學測** lines skew to the z-axis: $\{z=0,x+y=1\}$ and $\{y=1,z=1\}$ → (3)(5).
  - Two planes' flight paths: A(1,2,−1)→B(5,8,−3) in 2 s; C(0,8,4)→D(2,10,3) in 1 s ⇒ positions $(1+2t,2+3t,-1-t)$ and $(2t,8+2t,4-t)$ never coincide at the same t ⇒ no collision (the paths themselves may cross).
  - $L_1$ and $L_2$ with a parameter a meeting ⇒ $a=-7$, $P(\frac12,2,-\frac32)$.
- **Line vs plane**: substitute the parametrisation.
  - An identity means the line lies in the plane.
  - A contradiction means it is parallel.
  - Otherwise it meets at one point.
  - Equivalently: $\vec v\cdot\vec n=0$ ⇒ parallel or contained.
  - Line direction (3,−1,2): the parallel plane among the options is $x+y-z-2=0$ (B).
  - **2018學測** (a line L and planes $E_1$, $E_2$): L ⊥ E₁ ✓ and E₁∩E₂ is a line ✓ → (3)(5).
  - Projection onto a plane: segment AB, A(0,−2,1), B(1,−3,1), onto $x-2y-z+3=0$ ⇒ $\overrightarrow{AB}=(1,-1,0)$ minus its normal component $\frac12(1,-2,-1)$ is $(\frac12,0,\frac12)$ ⇒ projected length $\frac{\sqrt2}2$.
- **Point to line**: foot H from $\overrightarrow{PH}\cdot\vec v=0$; distance |PH|; or $\frac{|\overrightarrow{AP}\times\vec v|}{|\vec v|}$.
  - Two parallel lines: distance from a point of one to the other ⇒ 3.
  - P(−1,3,6) to $\frac{x+2}{-2}=\frac{y-8}3=z-6$: distance and mirror point.
  - P(−3,1,−5) to the intersection line of $x+y+2z=0$ and $2x+y-z=6$ ⇒ $2\sqrt2$.
  - **2020學測**: A(1,7,2) to line BC through B(2,−6,3), C(0,−4,1) ⇒ foot (−3,−1,−2).
  - **2010學測**: L in $2x-y=2$ through (2,2,2): the foot from O must satisfy $\overrightarrow{OP}\cdot\overrightarrow{AP}=0$ and lie in the plane → (1)(3)(5).
  - **2011學測**: L in $x-y+z=2$ with P(2,1,1) the nearest point to O ⇒ direction ⊥ (2,1,1) and ⊥ (1,−1,1) ⇒ (2,−1,−3) ⇒ (m,n)=(−1,−3).
- **Skew lines**: the common perpendicular meets both lines; its length is the distance. Methods:
  - (a) Parametrise P∈L₁, Q∈L₂ with $\overrightarrow{PQ}$ ⊥ both directions.
  - (b) Take the plane E containing L₂ and parallel to L₁ (normal $\vec v_1\times\vec v_2$); the distance = d(any point of L₁, E).
  - 例: plane $2x+y+2z-2=0$, distance 3.
  - L₁, L₂ with a plane containing L₁ parallel to L₂ ⇒ $x+5y-7z+5=0$, distance $\frac{7\sqrt3}{15}$.
- **Planes containing lines**:
  - A point and a line: A(4,3,1) with the given line (例題13) ⇒ $2x-6y+z+9=0$.
  - Two intersecting lines ⇒ $5x-4y-3z-10=0$.
  - Two parallel lines ⇒ $2x-3y+2z+11=0$.
  - Parallel to two skew lines through a point ⇒ normal $\vec v_1\times\vec v_2=(-5,3,-2)$ through (1,−1,2) ⇒ $5x-3y+2z-12=0$.
- **Angle between lines / bisectors**: $\cos\theta=\pm\frac{\vec v_1\cdot\vec v_2}{|\vec v_1||\vec v_2|}$ (one example gives $\pm\frac49$). Bisector directions are $\frac{\vec v_1}{|\vec v_1|}\pm\frac{\vec v_2}{|\vec v_2|}$. Given bisector M of L₁, L₂ ⇒ $a=\frac23$, $b=\frac43$.
- **2019指定甲**: $\overrightarrow{OA}=(1,\sqrt2,1)$, $\overrightarrow{OB}=(2,0,0)$; |OP|=2 at 60° to OA ⇒ $\overrightarrow{OA}\cdot\overrightarrow{OP}=2$ ⇒ P on the plane $x+\sqrt2y+z=2$. Also at 60° to OB ⇒ x=1, so Q lies on the line of the two planes, direction (0,1,−√2) ⇒ Q = $(1,\sqrt2,-1)$ or $(1,-\frac{\sqrt2}3,\frac53)$.
- **2021指定甲**: A(0,−1,−1), B(1,−1,−2), C(0,1,0), $\overrightarrow{AH}=\frac23\overrightarrow{AB}-\frac13\overrightarrow{AC}+3(\overrightarrow{AB}\times\overrightarrow{AC})$ with $\overrightarrow{AB}\times\overrightarrow{AC}=(2,-1,2)$:
  - $V_{ABCH}=\frac16\cdot3|\overrightarrow{AB}\times\overrightarrow{AC}|^2=\frac92$.
  - The mirror image is $H'=A+\frac23\overrightarrow{AB}-\frac13\overrightarrow{AC}-3(\overrightarrow{AB}\times\overrightarrow{AC})=(-\frac{16}3,\frac43,-8)$.
  - The common foot has coefficients $(\frac23,-\frac13)$ (y<0), so it lies outside △ABC.
- **Optimisation with lines/planes**:
  - P on plane $x+y+z=3$ with A(2,3,1), B(4,6,−2): min $PA^2+PB^2=2PM^2+\frac{AB^2}2=\frac{32}3+11=\frac{65}3$ at $(\frac53,\frac{19}6,-\frac{11}6)$. A, B on the same side ⇒ reflect A to A′(0,1,−1) ⇒ min PA+PB $=|A'B|=\sqrt{42}$ at $(\frac32,\frac{23}8,-\frac{11}8)$.
  - Same idea on a line: min $PA^2+PB^2=\frac{99}2$ at $(2,1,\frac32)$; min PA+PB $=3\sqrt{10}$ at $(\frac53,\frac43,\frac43)$.
  - Cuboid OABC−DEFG with A(3,0,0), C(0,5,0), D(0,0,4): plane BEG $20x+12y+15z=120$; P on FG minimising the perimeter of △CEP ⇒ unfold to 2D ⇒ $P(\frac43,5,4)$.
  - Equilateral △PQR with P on L₁ and Q, R on L₂ (skew) ⇒ area $\frac1{\sqrt3}(\text{dist}(P,L_2))^2$, minimised at a specific P.
  - Midpoints of PQ with P∈L₁, Q∈L₂ form the plane $4x+y-2z=3$.
  - Line L through A with A, P(3,1,2), B collinear for A∈L₁, B∈L₂ ⇒ A(−1,−5,4), B(5,4,1).

### 19.6 [超出數A] 球面 (資優34)
- **Equation**: $(x-x_0)^2+(y-y_0)^2+(z-z_0)^2=r^2$. A general $x^2+y^2+z^2+Dx+Ey+Fz+G=0$ is a sphere, a point, or empty by completing the square ($k<-3$ or $k>4$ sphere; k=−3, 4 a point; else empty).
  - Diameter AB: $(x-a_1)(x-b_1)+\dots=0$.
  - Circumsphere of O, (1,0,0), (0,1,0), (0,0,2): $x^2+y^2+z^2-x-y-2z=0$.
- **Sphere vs plane** (by d vs R):
  - The section is a circle with centre the foot of the centre and radius $\sqrt{R^2-d^2}$; the great circle passes through the centre.
  - Tangent plane at A: $\overrightarrow{OA}\cdot\overrightarrow{AP}=0$ (e.g. $2x-2y-z=11$).
- **Sphere vs line**: $d(O,L)$ vs R, or the discriminant of the substituted quadratic.
  - **85大學社**: chord on $x^2+y^2+z^2=4$ along $\{x+y+z=1,\ 2x+2y+z=1\}=\{(t,-t,1)\}$ ⇒ distance 1 ⇒ $PQ=2\sqrt3$.
  - Cone of tangents from an external point; circle of contact.
- **Extrema on a sphere = Cauchy**: $(x-1)^2+(y-1)^2+(z-1)^2=9$ ⇒ $2x-y-2z\in[-10,8]$.
- 經緯度, spherical distance $s=R\theta$ (θ = central angle), 球面坐標 (enrichment; 數B S-11B-1).

**Traps**:
- A single linear equation in space is a plane, not a line.
- Use the normal for planes and the direction vector for lines; a line ⊥ a plane has direction = normal; a line ∥ a plane has $\vec v\cdot\vec n=0$.
- The angle between planes comes with its supplement.
- The distance formula needs the plane in general form.
- Skew-line distance uses $\vec v_1\times\vec v_2$.
- Check coincidence (common point) before declaring lines parallel.

---

## 20. 線性方程組、矩陣運算、反方陣、轉移矩陣、平面上的線性變換

**Scope**:
- A-11A-1: 二元一次方程組的矩陣表達, 克拉瑪公式 (see §16.6).
- A-11A-2: 三元一次聯立方程式 by 消去法 and in matrix form; 高斯消去法 / 增廣矩陣; 插值多項式; **三平面幾何關係的代數判定 ★**. rank and 線性獨立 are excluded.
- A-11A-3: 矩陣的定義, 加減, 係數積, 乘法, 反方陣. Inverses are computed exactly **only for 2×2**; 3×3 inverses are concept-only.
- F-11A-3: 平面上的線性變換, 二階轉移方陣.

**Sources**: 99第四冊 2-3三元一次聯立方程組, 3-1線性方程組與矩陣, 3-2矩陣的運算, 3-3矩陣的應用, 3-4平面上的線性變換; 資優 第32單元行列式 (方程組 part), 第51單元矩陣的運算, 第52單元矩陣的應用.

### 20.1 三元一次聯立方程組：消去法與克拉瑪公式
- **消去法**: eliminate one variable from two pairs to get a 2×2 system, solve it, then back-substitute.
- **克拉瑪公式 (3×3)**: for $a_ix+b_iy+c_iz=d_i$ (i=1,2,3), let $\Delta=\det[\text{coefficients}]$, and let $\Delta_x,\Delta_y,\Delta_z$ be Δ with the corresponding column replaced by $(d_1,d_2,d_3)$.
  - $\Delta\ne0$ ⇒ exactly one solution $x=\frac{\Delta_x}\Delta,\ y=\frac{\Delta_y}\Delta,\ z=\frac{\Delta_z}\Delta$.
  - $\Delta=0$ and one of $\Delta_x,\Delta_y,\Delta_z\ne0$ ⇒ 無解.
  - $\Delta=\Delta_x=\Delta_y=\Delta_z=0$ ⇒ 無限多解 **or** 無解 — must check by elimination (unlike the 2×2 case).
- **Geometric meaning**: $\Delta=\vec n_1\cdot(\vec n_2\times\vec n_3)$ (§18).
  - $\Delta\ne0$ ⇔ the three normals are not coplanar ⇔ **三平面交於一點**.
  - $\Delta=0$ ⇒ the normals are coplanar, giving four cases:
    1. 三平面交於一直線 (共線), with infinitely many solutions.
    2. 兩兩交於一直線 and the three lines are parallel (三角柱), with no solution.
    3. Two planes parallel and the third cuts both, with no solution.
    4. Three parallel planes, or coincidences, with no solution or with infinitely many if they coincide.
  - Tell the cases apart by comparing normals (parallel?) and by elimination (does the reduced system contradict, e.g. 0=1?).
- 例 (資優32):
  - $x+2y-3z=4,\ 2x+4y-6z=7,\ 3x+6y+z=5$ ⇒ the first two planes are parallel and the third cuts both ⇒ 無解.
  - $x+y+2z=2,\ 2x+y+z=2,\ x+2y+5z=2$ ⇒ 兩兩交於一直線, the three lines are not concurrent (parallel) ⇒ 無解.
- **Parameter discussion** (classic): $ax+y+z=1,\ x+ay+z=1,\ x+y+az=1$ has $\Delta=(a-1)^2(a+2)$.
  - $a\ne1,-2$: unique solution $(\frac1{a+2},\frac1{a+2},\frac1{a+2})$.
  - $a=1$: one plane, so $(s,t,1-s-t)$, infinitely many.
  - $a=-2$: 無解 (adding all three gives 0=3).
- 99 2-3 exercises:
  - A family with parameter k: k=−18 ⇒ 三平面交於一直線; k≠−18 ⇒ the planes meet pairwise in three parallel lines.
  - A 4-plane version: put the line of the first three into the fourth to find the parameter (a=−58).
- **齊次方程組** ($d_i=0$) always has (0,0,0).
  - $\Delta\ne0$ ⇒ only the trivial solution.
  - $\Delta=0$ ⇒ infinitely many (non-zero) solutions; the planes share a line through O.
  - 例: a homogeneous system with a parameter has a non-trivial solution at a=3, giving $(-t,-18t,13t)$.
- **Linear-combination view**: the system is $x\vec u+y\vec v+z\vec w=\vec d$ with column vectors $\vec u,\vec v,\vec w$. "Every $\vec d$ is a unique combination" ⇔ $\det[\vec u\ \vec v\ \vec w]\ne0$ ⇔ the columns are not coplanar.
- **Scaling trick**: if (α,β,γ) solves a system, substitute X=4x etc. to read off the solution of the rescaled system (e.g. $(4\alpha,2\beta,4\gamma)$).

**Applications (建立方程組)**:
- **2003學測**: $a_1,\dots,a_{50}\in\{-1,0,1\}$ with $\sum a_i=9$ and $\sum(a_i+1)^2=107$.
  - $\sum a_i^2+2\cdot9+50=107$ ⇒ $\sum a_i^2=39$ ⇒ 39 non-zero terms ⇒ **11 個 0**.
- **2011學測 輻射**: A, B, C emit 1, 2, 1 units per kg; every half year their masses become $\frac12,\frac13,\frac14$ of before. Readings: 66 one year ago, 22 half a year ago, 8 now.
  - Masses now x, y, z: $x+2y+z=8$, $2x+6y+4z=22$, $4x+18y+16z=66$ ⇒ **(4,1,2)** kg.
- **白羅包子**: 999 buns sold out, price 8/15/21 for 1/2/3 buns, 432 customers, revenue 7195, cost 5 each.
  - Profit $7195-5\cdot999=2200$.
  - $x+y+z=432$, $x+2y+3z=999$, $8x+15y+21z=7195$ ⇒ (95,107,230).
- Water pipes: A, B, C fill $100,\ \frac{200}3,\ 200$ m³ per hour. GPS-type distance equations: subtract pairs of sphere equations to get linear equations ⇒ (1,−2,3).
- **插值多項式**: $y=ax^2+bx+c$ through three points with distinct x gives a 3×3 system in (a,b,c).
  - Its determinant is $(x_1-x_2)(x_2-x_3)(x_3-x_1)\ne0$, so the solution is unique (Lagrange / Newton forms in §7).
  - A circle $x^2+y^2+dx+ey+f=0$ through three points is likewise a 3×3 system in (d,e,f).

### 20.2 高斯消去法、增廣矩陣、列運算
- **Matrix notation**: a matrix of m 列 (rows) × n 行 (columns) is m×n 階.
  - The (i,j)元 is $a_{ij}$, in 第i列 and 第j行.
  - The 係數矩陣 holds the coefficients; the 增廣矩陣 also holds the constants.
- **三種列運算** (they do not change the solution set):
  1. Swap two rows.
  2. Multiply a row by a non-zero constant.
  3. Add a multiple of one row to another.
- **高斯消去法**: reduce to **列梯形** (upper triangular), then back-substitute.
  - **高斯-喬登消去法** continues to the **最簡列梯矩陣** (each leading 1 is the only non-zero entry in its column), from which the solution can be read off.
  - 例: $\{x-y+z=8,\ 2x+3y-z=-2,\ \dots\}$ ⇒ (4,−3,1).
  - 例: $2x+y-z=5,\ x+2y+z=7,\ \dots$ reduces to $x-z=1,\ y+z=3$ ⇒ $(1+t,3-t,t)$, a line through (1,3,0) with direction (1,−1,1).
- **Reading the final echelon form**:
  - A row $[0\ 0\ 0\mid k]$ with k≠0 ⇒ 無解.
  - Fewer pivots than unknowns, with no contradiction ⇒ 無限多解; the free variables become parameters.
  - Otherwise ⇒ unique solution.
- **2007學測**: which augmented matrices can be row-reduced to $\begin{bmatrix}1&2&3&7\\0&1&1&2\\0&0&1&1\end{bmatrix}$? Ans (1)(5).
  - Test: does each candidate system have the same unique solution (x,y,z)=(2,1,1)?
- **2009指定甲**: $\begin{bmatrix}4&9&a\\3&7&b\end{bmatrix}$ row-reduces to $\begin{bmatrix}1&0&1\\0&1&1\end{bmatrix}$ ⇒ the solution is x=y=1 ⇒ $a=4+9=13$, $b=3+7=10$.
- Lines in space as intersections: $L_1, L_2$ meet at $(-\frac12,\frac72,-\frac12)$, found by solving the joint system by row reduction.
- **Computer solving** (A-11A-2): larger systems are solved by software (spreadsheets, GeoGebra) using the same elimination. GSAT asks only for the concept.

### 20.3 矩陣的運算
- **Definitions**:
  - Equality needs the same order and equal entries.
  - $O$ is the 零矩陣; $I_n$ is the 單位方陣.
  - **轉置** $A^T$ has entries $(A^T)_{ij}=a_{ji}$, with $(A+B)^T=A^T+B^T$ and $(AB)^T=B^TA^T$.
  - Symmetric means $A^T=A$; skew-symmetric means $A^T=-A$. Any square matrix is $\frac12(A+A^T)+\frac12(A-A^T)$.
- **加減與係數積**: entrywise, same order required. Solve matrix equations like numbers.
  - 例: $3X-2B+3A=2X-5C$ ⇒ $X=-3A+2B-5C$.
  - 例: $5(X+A)=4X-7B$ ⇒ $X=-5A-7B$.
- **乘法**: an (m×n)(n×p) product is m×p, with $(AB)_{ij}=$ (row i of A)·(column j of B), an inner product.
  - **Matrix as data table**: a scores matrix times a weights matrix gives the weighted totals for each student and each school.
  - **2015指定乙**: prices rise 3% per year for 2 years ⇒ the new price matrix is $(1.03)^2M$ (equivalently a scalar matrix $(1.03)^2I$ times M), not $2(1.03)M$.
- **Properties**:
  - Associative: $(AB)C=A(BC)$.
  - Distributive: $A(B+C)=AB+AC$ and $(A+B)C=AC+BC$.
  - $r(AB)=(rA)B=A(rB)$.
  - $AI=IA=A$.
- **Not true for matrices**:
  - $AB\ne BA$ in general (BA may not even exist).
  - $AB=O\not\Rightarrow A=O$ or $B=O$.
  - $AB=AC\not\Rightarrow B=C$; this holds only if $A^{-1}$ exists.
  - $(A+B)^2=A^2+AB+BA+B^2$, which is $\ne A^2+2AB+B^2$ unless AB=BA.
  - $A^2=I\not\Rightarrow A=\pm I$ (e.g. a reflection).
  - $AB=O\not\Rightarrow BA=O$.
  - $A^2-I=(A+I)(A-I)$ **is** true, because I commutes with A.
  - $\det(A+B)\ne\det A+\det B$, and $\det(kA)=k^n\det A$ for n×n A.
  - 例: X+Y=$\begin{bmatrix}2&2\\2&5\end{bmatrix}$, X−Y=$\begin{bmatrix}0&2\\4&3\end{bmatrix}$ ⇒ $X^2-Y^2=\begin{bmatrix}6&10\\17&21\end{bmatrix}$, which is **not** $(X+Y)(X-Y)=\begin{bmatrix}8&10\\20&19\end{bmatrix}$.
- **Exam items**:
  - **2019學測**: $\begin{bmatrix}3&-1&3\\2&4&-1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix}=\begin{bmatrix}6\\-6\end{bmatrix}$ ⇒ $3x-y=3$, $2x+4y=-5$ ⇒ $(\frac12,-\frac32)$, $x+3y=-4$.
  - **2020學測**: $A=\begin{bmatrix}1&1\\3&4\end{bmatrix}$, $B=I+A+A^{-1}$ ⇒ $BA=A+A^2+I=\begin{bmatrix}6&6\\18&24\end{bmatrix}$, option (5). No inverse is needed.
  - **2018學測**: $\begin{bmatrix}a&b\\c&d\\1&2\end{bmatrix}\begin{bmatrix}-3&5&7\\-4&6&e\end{bmatrix}=\begin{bmatrix}3&x&7\\0&y&7\\-11&z&23\end{bmatrix}$.
    - Row 3 gives z=17 and e=8.
    - Row 2: $-3c-4d=0$, $7c+8d=7$ ⇒ c=7, $d=-\frac{21}4$ ⇒ $y=5c+6d=\frac72$.
  - **2018指定甲**: A is 3×3 with $A(a,b,c)^T=(b,c,a)^T$ for all a, b, c ⇒ $A^2(1,0,-1)^T=A(0,-1,1)^T=(-1,1,0)^T$, option (2).
  - AB=2I with integer entries ⇒ $a^2+b^2+c^2+d^2=30$ (99 3-2 綜合12).
  - Circuit matrices (串聯/並聯 as 2×2 transfer matrices $\begin{bmatrix}1&-R\\0&1\end{bmatrix}$-type) multiply in order (99 3-2 綜合14).
- **Powers $A^n$**:
  - Diagonal: $\mathrm{diag}(a,b,c)^n=\mathrm{diag}(a^n,b^n,c^n)$.
  - Rotation: $R_\theta^n=R_{n\theta}$, so $R_{60^\circ}^6=I$ (smallest n=6). The reflection $\begin{bmatrix}\cos\theta&\sin\theta\\\sin\theta&-\cos\theta\end{bmatrix}^n$ is A for odd n and I for even n.
  - **Nilpotent split**: $A=\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix}=I+B$ with $B^3=O$ ⇒ $A^n=I+nB+\binom n2B^2=\begin{bmatrix}1&n&\frac{n(n+1)}2\\0&1&n\\0&0&1\end{bmatrix}$.
  - $A=\begin{bmatrix}2&1&2\\0&2&3\\0&0&2\end{bmatrix}=2I+B$ ⇒ $A^5=32I+80B+80B^2$, whose largest entry is 400.
  - Upper-triangular $I+N$ variants give entries like $a_{13}=3160$ (99 3-2).
  - $\sum_{k=1}^{20}\begin{bmatrix}1&-1\\0&1\end{bmatrix}^k=\begin{bmatrix}20&-210\\0&20\end{bmatrix}$ ⇒ b=−210.
  - **All-ones J** (n×n): $J^2=nJ$.
    - $(I+\frac13J_3)^8=I+85J$; $(I+\frac15J_5)^8=I+51J$.
    - Since $\frac1nJ$ is idempotent, $(I+\frac1nJ)^8=I+(2^8-1)\frac1nJ$.
  - $(M+I)^3=57M+I$-type items: reduce with the relation M satisfies.
  - **對角化**: $P^{-1}AP=D$ ⇒ $A^n=PD^nP^{-1}$.
    - $A=\begin{bmatrix}1&-1\\2&4\end{bmatrix}$, D=diag(2,3) ⇒ $A^n=\begin{bmatrix}2^{n+1}-3^n&2^n-3^n\\2\cdot3^n-2^{n+1}&2\cdot3^n-2^n\end{bmatrix}$.
    - $A=\begin{bmatrix}0.7&0.4\\0.3&0.6\end{bmatrix}$, D=diag(1,0.3) ⇒ $A^n=\frac17\begin{bmatrix}4+3(0.3)^n&4-4(0.3)^n\\3-3(0.3)^n&3+4(0.3)^n\end{bmatrix}\to\frac17\begin{bmatrix}4&4\\3&3\end{bmatrix}$.
    - Diagonalisation is enrichment; GSAT may give P.
- **Cayley–Hamilton (2×2)**: $A^2-(a+d)A+(ad-bc)I=O$. Use it to reduce powers and to find inverses.
- **2007指定甲**: $A=\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ (reflection in the x-axis), $B=R_{60^\circ}$.
  - (1) AB=BA ✗.
  - (2) $A^2B=BA^2$ ✓, since $A^2=I$.
  - (3) $A^{11}B^3=-A$ but $B^6A^5=A$ ✗.
  - (4) $AB^{12}=A=A^7$ ✓.
  - (5) $(ABA)^{15}=AB^{15}A$ ✓ (the inner $A^2=I$ cancel).
  - Ans (2)(4)(5).

### 20.4 反方陣
- **Definition**: $AB=BA=I$ ⇒ $B=A^{-1}$. It exists ⇔ $\det A\ne0$; a matrix with an inverse is 可逆.
- **2×2 formula**: $\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1}=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$.
  - 例: $\begin{bmatrix}3&5\\2&-1\end{bmatrix}^{-1}=\frac1{13}\begin{bmatrix}1&5\\2&-3\end{bmatrix}$.
- **n×n (concept only for GSAT)**: row-reduce $[A\mid I]\to[I\mid A^{-1}]$; or for 3×3, use cross products of the columns divided by det.
  - 3×3 singular-parameter items reduce to det=0 (e.g. a=2 or −3).
  - Computing a 3×3 inverse exactly is **[超出數A]**.
- **Properties**:
  - $(AB)^{-1}=B^{-1}A^{-1}$; $(A^{-1})^{-1}=A$; $(A^T)^{-1}=(A^{-1})^T$; $(kA)^{-1}=\frac1kA^{-1}$.
  - $\det(AB)=\det A\det B$ and $\det(A^{-1})=\frac1{\det A}$.
  - $(ABA^{-1})^n=AB^nA^{-1}$.
- **Solving matrix equations**:
  - $AX=C$ ⇒ $X=A^{-1}C$; $XA=C$ ⇒ $X=CA^{-1}$. The side matters.
  - $AXB=C$ ⇒ $X=A^{-1}CB^{-1}$.
  - 2×2 systems: $AX=\vec d$ ⇒ $X=A^{-1}\vec d$, which is Cramer.
- **From a polynomial identity**:
  - $A^2-2A-3I=O$ ⇒ $A(A-2I)=3I$ ⇒ $A^{-1}=\frac13A-\frac23I$.
  - $A^2-5A+6I=O$ ⇒ $(5I-A)A=6I$ ⇒ $(5I-A)^{-1}=\frac16A$.
- **Determine A from images**: if $A\vec p_1=\vec q_1$ and $A\vec p_2=\vec q_2$, then $A[\vec p_1\ \vec p_2]=[\vec q_1\ \vec q_2]$, so $A=[\vec q_1\ \vec q_2][\vec p_1\ \vec p_2]^{-1}$.
  - **2006指定甲**: $A\binom73=\binom21$, $A\binom94=\binom15$, $A=\begin{bmatrix}2&1\\1&5\end{bmatrix}\begin{bmatrix}a&c\\b&d\end{bmatrix}$.
    - Then $\begin{bmatrix}2&1\\1&5\end{bmatrix}^{-1}A=\begin{bmatrix}2&1\\1&5\end{bmatrix}^{-1}\begin{bmatrix}2&1\\1&5\end{bmatrix}\begin{bmatrix}7&9\\3&4\end{bmatrix}^{-1}$ ⇒ $\begin{bmatrix}a&c\\b&d\end{bmatrix}=\begin{bmatrix}7&9\\3&4\end{bmatrix}^{-1}=\begin{bmatrix}4&-9\\-3&7\end{bmatrix}$.
    - So **a=4, b=−3, c=−9, d=7**.
- **2010指定乙 密碼**: $\begin{bmatrix}a&b\\c&d\end{bmatrix}\begin{bmatrix}5&-15\\-10&35\end{bmatrix}=5I$ ⇒ the first matrix is $5M^{-1}=\frac5{25}\begin{bmatrix}35&15\\10&5\end{bmatrix}=\begin{bmatrix}7&3\\2&1\end{bmatrix}$ ⇒ **7321**.
- **2011指定甲**: $A=\begin{bmatrix}4&a\\9&b\end{bmatrix}$, $B=\begin{bmatrix}6&7\\c&d\end{bmatrix}$, $AB=\begin{bmatrix}3&10\\-2&15\end{bmatrix}$, det A=2.
  - (1) $9a-4b=-2$ ✓.
  - (2) $ac=3-24=-21$ ✗.
  - (3) Second row of $B=A^{-1}(AB)$ gives d=−15 ✓.
  - (4) $\begin{bmatrix}b&-a\\-9&4\end{bmatrix}A=2I$ ✗.
  - Ans (1)(3).
- **2019指定甲 坐標變換**: $\vec y=\begin{bmatrix}1&0\\-1&2\end{bmatrix}\vec x+\binom{-2}3$ maps $\binom rs$ to $\binom1{-2}$ ⇒ $\begin{bmatrix}1&0\\-1&2\end{bmatrix}\binom rs=\binom3{-5}$ ⇒ **(r,s)=(3,−1)**.
- **2005指定乙**: $a_{n+1}=2(a_n+b_n)$, $b_{n+1}=2b_n$ ⇒ one step is $M=\begin{bmatrix}2&2\\0&2\end{bmatrix}$ ⇒ $A=M^3=8\begin{bmatrix}1&3\\0&1\end{bmatrix}$ ⇒ **(a,b,c,d)=(8,24,0,8)**.
- **編碼/解碼**: encode with $Y=AX$ and decode with $X=A^{-1}Y$.

### 20.5 轉移矩陣 (馬可夫鏈)
- **Setup**: states $S_1,\dots,S_n$; $p_{ij}=P(\text{next}=S_i\mid\text{now}=S_j)$ is in **column j**. Then $X_{k+1}=AX_k$, so $X_k=A^kX_0$.
- **轉移矩陣**: all entries ≥0 and **each column sums to 1**. The textbook convention is columns; check whether a problem uses rows.
  - Then $x_k+y_k=1$ and $x_k,y_k\ge0$ persist.
- **穩定狀態**: X with $AX=X$ and entries summing to 1. Not every chain stabilises (e.g. $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ oscillates).
  - For 2×2: $\begin{bmatrix}1-p&q\\p&1-q\end{bmatrix}$ ⇒ stable $\left(\frac q{p+q},\frac p{p+q}\right)$, i.e. the flows balance: $p\cdot x=q\cdot y$.
- **Closure properties (2002指定甲)**: for transition matrices A, B:
  - $A^2$ ✓.
  - AB is also a transition matrix, so "(2) AB 不滿足(乙)" ✗.
  - $\frac12(A+B)$ ✓.
  - $\frac14(A^2+B^2)$ ✗ (its columns sum to ½).
  - Ans (1)(3).
  - **2011指定乙**: prove that $A^2$ is a transition matrix (column sums: $(a_{11}+a_{21})b_{11}+(a_{12}+a_{22})b_{21}=b_{11}+b_{21}=1$).
- **Standard results**:
  - 甲/乙工廠 ($\frac14$ stay at 甲, $\frac23$ stay at 乙) ⇒ long run $(\frac4{13},\frac9{13})$.
  - Newspapers (甲 keeps $\frac13$, 乙→甲 $\frac35$) ⇒ 9:10.
  - **捷運/開車/機車**: $A=\begin{bmatrix}.8&.3&.2\\.1&.5&.2\\.1&.2&.6\end{bmatrix}$, $X_0=(.2,.3,.5)$ ⇒ one year later 35% 捷運; long run $\frac{16}{29}$.
  - **Basketball**: P(make | made) = 0.8, P(make | missed) = 0.6; after a made warm-up shot ⇒ 0.8, 0.76, 0.752; long run 0.75.
  - **Insurance** (3 classes, 1000 drivers in class 1): year 2 is 800/150/50; year 3 is 640/225/135.
  - **2003指定甲**: high income = 2 × low income; 40% of high become low each year ⇒ balance $2\cdot0.4=x\cdot1$ ⇒ 8成 (C).
  - Stocks (up/flat/down with given rows): up today ⇒ P(up the day after tomorrow) $=\frac13\cdot\frac13+\frac12\cdot\frac13+\frac16\cdot\frac16=\frac{11}{36}$.
  - **Gas stations C/F/T**: every column sends 20% to T, so $x_T=0.2$ from year 1 on.
    - $x_{C,1}=0.48$, $x_{F,2}=0.424$; stable state (0.35, 0.45, 0.2).
- **Ball-exchange chains** (state = composition of one box):
  - Box A has 1 black and 1 white, box B has 1 white; one round is A→B then B→A. P(A is 1 black + 1 white) is $\frac34$ after round 1 and $\frac{43}{64}$ after round 3; in general $\frac23+\frac13(\frac14)^n$.
  - Box A has 2 white, B has 1 white and 1 black (same rule) ⇒ P(A still 2 white) = $\frac23,\frac59,\frac{14}{27}$.
  - **Swap one-for-one**:
    - 甲 has two 3s and 乙 two 4s ⇒ states are the number of 4s in 甲: 0→1 surely; from 1: to 0 or 2 each $\frac14$, stay $\frac12$.
    - After 5 swaps, P(甲 sum even) $=P(0)+P(2)=\frac5{16}$. Stable state $(\frac16,\frac23,\frac16)$ ⇒ P(乙 sum odd) $=\frac23$ (2009 北區模擬).
    - Same chain with 2 white vs 2 red: P(甲 has 2 red) after 2 swaps is $\frac14$; stable value $\frac16$.
  - **Bills**: 甲 has two 100s, 乙 three 50s, swap one each round.
    - From 150: →100 w.p. $\frac13$, stay $\frac12$, →200 w.p. $\frac16$. From 100: →150 w.p. $\frac23$.
    - After 3 rounds (start 200): $P(200,150,100)=(\frac3{36},\frac{23}{36},\frac{10}{36})$.
    - Stable state $(\frac1{10},\frac35,\frac3{10})$ ⇒ expected value 140 元.
  - **Drawing rule**: 甲 has 1R 2W, 乙 has 2R 1W; white ⇒ next draw from 乙, red ⇒ from 甲; start at 甲.
    - $P_{n+1}=\frac23-\frac13P_n$ with $P_1=\frac23$ ⇒ $P_3=\frac{14}{27}$, $P_\infty=\frac12$.
  - Other 99 3-3 results: red ball $\frac23$; 果汁 68.75%.

### 20.6 平面上的線性變換
- **Core fact**: $T(\vec x)=A\vec x$; the columns of A are $T(\vec e_1)$ and $T(\vec e_2)$.
  - Linear: $T(\alpha\vec x+\beta\vec y)=\alpha T(\vec x)+\beta T(\vec y)$. So if $\overrightarrow{OP}=x\vec e_1+y\vec e_2$, then $\overrightarrow{OP'}=x\vec e_1'+y\vec e_2'$ with the same coefficients.
  - The origin is fixed.
  - If det A≠0, lines map to lines, segments to segments, parallelograms to parallelograms, and centroids to centroids (affine ratios are kept). If det A=0, the plane collapses to a line or a point.
- **Finding A**:
  - Two point–image pairs ⇒ $A=[\vec q_1\ \vec q_2][\vec p_1\ \vec p_2]^{-1}$.
  - 例: (2,−1)→(2,4) and (−1,1)→(1,1) ⇒ $B=\begin{bmatrix}3&4\\5&6\end{bmatrix}$, $B\binom{10}{-7}=\binom28$.
  - 例: $x'=3x-4y$, $y'=-2x+3y$ ⇒ $A=\begin{bmatrix}3&-4\\-2&3\end{bmatrix}$, $A(5\vec e_1-2\vec e_2)=(23,-16)$.
- **Image of a curve**: substitute the inverse, $\binom xy=A^{-1}\binom{x'}{y'}$, into the equation.
  - $x+y=3$ → $x-y+6=0$ (99 3-4).
  - Line $2x-y=3$ is mapped onto $3x+7y=15$ by $\begin{bmatrix}1&a\\b&-1\end{bmatrix}$: take two points (0,−3), $(\frac32,0)$ ⇒ $(a,b)=(\frac23,1)$.
- **Standard matrices**:

| 變換 | Matrix | det |
|---|---|---|
| 旋轉 θ (about O) | $R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$ | 1 |
| 鏡射 in line through O with 斜角 θ | $M_\theta=\begin{bmatrix}\cos2\theta&\sin2\theta\\\sin2\theta&-\cos2\theta\end{bmatrix}$ | −1 |
| 中心伸縮 k | $kI$ | $k^2$ |
| 水平伸縮 r / 鉛直伸縮 r | $\begin{bmatrix}r&0\\0&1\end{bmatrix}$ / $\begin{bmatrix}1&0\\0&r\end{bmatrix}$ | r |
| 推移 (x-shear) $x'=x+ky$ | $\begin{bmatrix}1&k\\0&1\end{bmatrix}$ | 1 |
| 推移 (y-shear) $y'=kx+y$ | $\begin{bmatrix}1&0\\k&1\end{bmatrix}$ | 1 |
| Projection onto line through O along (a,b) | $\frac1{a^2+b^2}\begin{bmatrix}a^2&ab\\ab&b^2\end{bmatrix}$ | 0 |

- **Rotation facts**: $R_\alpha R_\beta=R_{\alpha+\beta}$ (they commute); $R_\theta^{-1}=R_{-\theta}=R_\theta^T$; $R_\theta^n=R_{n\theta}$. Rotating by θ is multiplication by $\cos\theta+i\sin\theta$ in the complex plane.
  - $kR_\theta$ is a rotation plus scaling, and is commutative: $R\,(kI)=(kI)\,R$.
  - 例: $A=\begin{bmatrix}1&-\sqrt3\\\sqrt3&1\end{bmatrix}=2R_{60^\circ}$ ⇒ $A^{10}=2^{10}R_{600^\circ}=2^{10}R_{240^\circ}$.
  - 例: $\begin{bmatrix}1&\sqrt3\\\sqrt3&-1\end{bmatrix}=2M_{30^\circ}$ ⇒ its 10th power is $2^{10}I$.
  - $\frac12\begin{bmatrix}1&-1\\1&1\end{bmatrix}=\frac1{\sqrt2}R_{45^\circ}$: the triangles $OP_nP_{n+1}$ shrink by $\frac12$ in area each step ($S_n/S_{n+1}=2$).
  - **2014指定甲**: $(1+i)^n=a_n+ib_n$ ⇒ $a_4^2+b_4^2=|1+i|^8=16$. $\binom{a_{n+1}}{b_{n+1}}=T\binom{a_n}{b_n}$ with $T=\begin{bmatrix}1&-1\\1&1\end{bmatrix}=\sqrt2R_{45^\circ}$, which preserves angles and scales lengths by $\sqrt2$.
- **Reflection facts**:
  - $M_\theta^2=I$, i.e. $M_\theta^{-1}=M_\theta$.
  - Two reflections give a rotation: $M_\alpha M_\beta=R_{2(\alpha-\beta)}$. Rotation then reflection is a reflection.
  - Lines: x-axis $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$; y-axis $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$; $y=x$ $\begin{bmatrix}0&1\\1&0\end{bmatrix}$.
  - For $y=mx$: $\frac1{1+m^2}\begin{bmatrix}1-m^2&2m\\2m&m^2-1\end{bmatrix}$.
  - $y=3x$: $\begin{bmatrix}-\frac45&\frac35\\\frac35&\frac45\end{bmatrix}$; (1,1)→$(-\frac15,\frac75)$ and (−2,4)→(4,2).
  - $y=2x$: $\begin{bmatrix}-\frac35&\frac45\\\frac45&\frac35\end{bmatrix}$; (4,−2)→$(-4,2)$ and (−4,3)→$(\frac{24}5,-\frac75)$.
  - A line not through O (e.g. x=1, or $x-2y+1=0$): translate to O, reflect, translate back. Example: A(4,−2) in x=1 → (−2,−2); in y=2 → (4,6).
- **Recognising matrices**:
  - Rotation ⇔ $\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ with $a^2+b^2=1$.
  - Reflection ⇔ $\begin{bmatrix}a&b\\b&-a\end{bmatrix}$ with $a^2+b^2=1$.
  - Both have orthonormal columns ($A^TA=I$), which ⇔ the map preserves length and angle ⇔ it preserves inner products (99 3-4 進階26).
  - 例: $\begin{bmatrix}\frac{\sqrt3}2&\frac12\\-\frac12&\frac{\sqrt3}2\end{bmatrix}$ is rotation by −30°; $\begin{bmatrix}\frac{\sqrt3}2&\frac12\\\frac12&-\frac{\sqrt3}2\end{bmatrix}$ is reflection in $y=(\tan15^\circ)x$.
  - $\begin{bmatrix}2&0\\0&1\end{bmatrix}$ is a horizontal stretch ×2; $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ is reflection in y=x; $\begin{bmatrix}1&0\\4&1\end{bmatrix}$ is a y-shear by 4x.
- **2003指定甲**: A is reflection in $y+\sqrt3x=0$ and $AB=-I$ ⇒ $B=-A^{-1}=-A$.
  - So AB=BA ✓; A+B=O ✓; −A is $B^{-1}$ ✓; B is a reflection (det B=−1), not a rotation ✗.
  - Ans (1)(2)(4).
- **2005指定甲**: $A\binom1{-1}=\binom11$ and $A\binom11=\binom{-1}1$ ⇒ A=$R_{90^\circ}$, a rotation; $A^2\binom1{-1}=\binom{-1}1$.
  - $A^4=I$ ⇒ from $A^4\binom ab=\binom32$ we get b=2 (a=3, not −3).
  - Ans (2)(3)(4).
- **2016指定甲**: rectangle A(3,−2), B(3,2), C(−3,2), D(−3,−2); M maps A→B and B→C.
  - $M=\begin{bmatrix}3&3\\2&-2\end{bmatrix}\begin{bmatrix}3&3\\-2&2\end{bmatrix}^{-1}=\begin{bmatrix}0&-\frac32\\\frac23&0\end{bmatrix}$, det M=1, not a reflection.
  - It maps C→D and D→A, so $M^4=I$ and $M^3=M^{-1}=-M$.
  - Ans (2)(3)(5).
- **Composite transforms** (apply right-to-left): "first rotate 60°, then reflect in the x-axis" $=\begin{bmatrix}1&0\\0&-1\end{bmatrix}R_{60^\circ}=\begin{bmatrix}\frac12&-\frac{\sqrt3}2\\-\frac{\sqrt3}2&-\frac12\end{bmatrix}$.
  - With R a 60° rotation ($R^6=I$, θ=60°) and M=diag(2,−1): $(RMR^{-1})^5=RM^5R^{-1}=\begin{bmatrix}\frac{29}4&\frac{33\sqrt3}4\\\frac{33\sqrt3}4&\frac{95}4\end{bmatrix}$.
  - $L: y=-x$ rotated 30° then reflected in y=x ⇒ $y=-(2+\sqrt3)x$.
- **Area**: area(image) = area × |det A|; |det A| is the 面積漲縮率.
  - Rotations, reflections and shears keep area.
  - (rx, sy) scales area by rs; ellipse area is πab.
  - 例: $\begin{bmatrix}1&2\\3&-8\end{bmatrix}$ applied to OP=(2,1), OQ=(−3,4) (area 11) ⇒ area 154.
  - 例: $\begin{bmatrix}2&3\\4&8\end{bmatrix}$ with OP=(2,1), OQ=(−1,1) ⇒ S=3, S′=12.
  - Which has area factor <1? $\begin{bmatrix}\frac34&0\\0&\frac34\end{bmatrix}$ ($\frac9{16}$).
  - Shear $\begin{bmatrix}1&3\\0&1\end{bmatrix}$ on $[0,2]\times[0,3]$ ⇒ a parallelogram with sides 2 and $3\sqrt{10}$, perimeter $4+6\sqrt{10}$, same area 6.
  - **2013指定甲**: A(1,0)→(1,√2), B(0,1)→(−1,√2) ⇒ $M=\begin{bmatrix}1&-1\\\sqrt2&\sqrt2\end{bmatrix}$, det $2\sqrt2$.
    - △ABC area 3 ⇒ △A′B′C′ area $6\sqrt2$; A′B′=2 ⇒ distance from C′ to A′B′ is $6\sqrt2$.
    - Centroids map to centroids by linearity.
  - 99 3-4 例12: A(1,2)→(−1,5), B(−2,3)→(2,4) ⇒ $M=\begin{bmatrix}-1&0\\1&2\end{bmatrix}$.
    - Area 5 ⇒ area 10, and $A'B'=\sqrt{10}$ ⇒ distance $2\sqrt{10}$.
    - AB = A′B′ here, yet distances to the line are not preserved.
- **Vertex problems by rotation** (rotate a vector by ±90°/60°/120°):
  - Square ABCD with A(2,1), B(5,5) ⇒ $\overrightarrow{AD}=R_{90^\circ}\overrightarrow{AB}=(-4,3)$ ⇒ D(−2,4), C(1,8).
  - Equilateral OAB with A(1,4) ⇒ $B=R_{60^\circ}A=(\frac12-2\sqrt3,\ 2+\frac{\sqrt3}2)$.
  - Equilateral PQT with circumcentre O and P(4,2) ⇒ $Q,T=R_{\pm120^\circ}P$: $(-2-\sqrt3,\ 2\sqrt3-1)$ and $(-2+\sqrt3,\ -1-2\sqrt3)$. The same C appears for a regular hexagon centred at O with A(4,2).
  - Rectangle OABC with OC = 2·OA and A(2,1) ⇒ C=(−2,4), B(0,5), or C=(2,−4), B(4,−3).
  - Right △ABC with ∠C=90°, AC:BC=4:3, A(0,0), C(−2,4), B in quadrant I ⇒ $\overrightarrow{CB}=\frac34R_{-90^\circ}\overrightarrow{CA}=(3,\frac32)$ ⇒ B(1, $\frac{11}2$).
  - A(3,−1), B in quadrant I, $OB=5\,OA$, ∠AOB=θ with $\tan\theta=\frac43$ ⇒ $B=5R_\theta A=(13,9)$.
- **Curve images**:
  - $y^2=4x$ rotated 45° ⇒ $x^2-2xy+y^2-4\sqrt2x-4\sqrt2y=0$.
  - $y=x^2$ reflected in y=2x ⇒ $9x^2-24xy+16y^2-20x-15y=0$.
  - $2x-y-6=0$ reflected in y=3x ⇒ $11x-2y+30=0$.
  - $\sqrt3x+y=4$ rotated 30° ⇒ $x+\sqrt3y=4$.
  - Circle $x^2+y^2=4$ sheared $(x,y)\to(x+y,y)$ ⇒ $x^2-2xy+2y^2=4$, an ellipse.
  - Unit circle stretched ×3 horizontally and ×2 vertically ⇒ $\frac{x^2}9+\frac{y^2}4=1$.
  - Rotating 60° about O: A(2,−4) → $(1+2\sqrt3,\ \sqrt3-2)$; line $x-\sqrt3y=2$ → x=1; circle $(x-1)^2+(y+\sqrt3)^2=4$ → $(x-2)^2+y^2=4$.
  - Circle reflected in y=2x ⇒ $(x-\frac15)^2+(y-\frac75)^2=1$.
  - $S$: $x^2+2xy+y^2+3\sqrt2x+\sqrt2y+6=0$ rotated 45° clockwise ⇒ $y=x^2+2x+3$, a parabola with axis x=−1. So S is a parabola with axis $x+y+\sqrt2=0$.
- **Invariant directions** (enrichment): $A=\begin{bmatrix}2&3\\5&4\end{bmatrix}$.
  - $\overrightarrow{OQ}=s\overrightarrow{OP}$ ⇒ s=7 or −1.
  - |OQ|=|OP| ⇒ $(x+y)(7x+6y)=0$.
  - OP ⊥ OQ ⇒ $x=(-2\pm\sqrt2)y$.
- **[超出數A] enrichment**:
  - Max-area triangle inscribed in $\frac{x^2}{228}+\frac{y^2}{76}=1$ with A(9,−7): scale y by √3 to get a circle, use an equilateral triangle, scale back ⇒ B(6,8), C(−15,−1).
  - Rotations of conics (轉軸) are 數甲-style.

**Traps**:
- AB≠BA. Expand $(A+B)^2$ fully. Do not cancel without an inverse.
- $X=A^{-1}C$ vs $CA^{-1}$: keep the side.
- $\det(kA)=k^2\det A$ for 2×2.
- 3×3 with Δ=0 and $\Delta_x=\Delta_y=\Delta_z=0$ can still be 無解; decide by elimination.
- Transition matrices: columns (not rows) sum to 1 in the textbook. Check the convention, and multiply $A^nX_0$ in the right order.
- Composite transforms apply right-to-left (the first transform is written rightmost).
- The rotation matrix has −sinθ top-right. A clockwise rotation uses −θ.
- A reflection matrix is symmetric with det −1; a rotation has det 1. Both preserve area; shears do too.
- |det| is the area factor, not det. Two images having equal length does not make T an isometry.

---

## 21. 條件機率、獨立事件、貝氏定理、主觀機率與客觀機率

**Scope**:
- D-11A-1 主觀機率與客觀機率: check that a subjective probability obeys the axioms; get objective probability from data.
- D-11A-2 條件機率 and 事件的獨立性.
- D-11A-3 貝氏定理 and the 乘法公式.
- Classical counting is §11. Transition-matrix chains are §20.5. Binomial distributions are [超出數A] (§24).

**Sources**: 108二下 3-1條件機率與獨立事件, 3-2貝氏定理、客觀機率與主觀機率; 99第二冊 3-3條件機率與貝氏定理; 資優 第45單元條件機率、貝氏定理與獨立事件.

### 21.1 條件機率
- **Definition**: $P(B\mid A)=\frac{P(A\cap B)}{P(A)}$ for $P(A)>0$.
  - Classical case: $P(B\mid A)=\frac{n(A\cap B)}{n(A)}$, i.e. **A becomes the new sample space**.
  - Information changes probability. With 2 envelopes of 100元 and 1 of 十萬, P(十萬)=1/3; once a 100元 envelope is opened it is 1/2.
  - Company table (生產: 男50 女250; 技術: 男550 女150): P(男)=0.6, but P(男 | 生產)=$\frac{50}{300}=\frac16$.
- **Properties** (P(· | A) is a probability on A):
  - $P(\varnothing\mid A)=0$ and $P(A\mid A)=1$.
  - $P(B'\mid A)=1-P(B\mid A)$.
  - $P(B_1\cup B_2\mid A)=P(B_1\mid A)+P(B_2\mid A)-P(B_1\cap B_2\mid A)$.
  - $P(A\mid B)\ne P(B\mid A)$ in general. They are equal ⇔ P(A)=P(B) (when $P(A\cap B)>0$).
- **Dice / coins / children**:
  - Two dice, sum 6 ⇒ P(a 2 appears) $=\frac25$.
  - Given **exactly one** 2 (10 outcomes), P(sum 7) $=\frac15$. Given the **first** die is 2, P(sum 7) $=\frac16$. Given sum 7, P(both prime) $=\frac13$.
  - Two coins, given "at least one head" ⇒ P(two heads) $=\frac13$.
  - Two children: given at least one boy ⇒ P(two boys) $=\frac13$; given the elder is a boy ⇒ $\frac12$.
  - Three coins, given at least one head ⇒ P(exactly two heads) $=\frac37$.
  - Three dice: A = 至少一個6, B = 至少一個1 ⇒ $n(A)=216-125=91$, $n(A\cap B)=216-2\cdot125+64=30$ ⇒ $P(B\mid A)=\frac{30}{91}$.
  - Two dice: A = sum 8, B = first > second ⇒ $P(A\mid B)=\frac2{15}$, $P(B\mid A)=\frac25$.
  - Three dice, given the sum is a multiple of 5 (sums 5, 10, 15: 6+27+10=43 outcomes) ⇒ P(sum ≤10) $=\frac{33}{43}$.
  - Two of 1–9 without repetition, given an even sum ⇒ P(both even) $=\frac{6}{6+10}=\frac38$.
- **From given probabilities**: $P(A)=\frac38,\ P(B)=\frac34,\ P(A\cup B)=\frac78$ ⇒ $P(A\cap B)=\frac14$.
  - Then $P(A\mid B)=\frac13$, $P(A'\mid B)=\frac23$, $P(A'\mid B')=\frac{1/8}{1/4}=\frac12$.
  - $P(A)=\frac13,\ P(B)=\frac14,\ P(A\cap B)=\frac16$ ⇒ $P(A\mid B)=\frac23$, $P(B\mid A)=\frac12$, $P(A'\mid B')=\frac{7/12}{3/4}=\frac79$, $P(B'\mid A')=\frac78$.
- **Tables (two-way)**:
  - 45 students: 21 pass English, 9 pass both, 9 fail both ⇒ P(fail math | pass English) $=\frac{12}{21}=\frac47$.
  - Boys 18 (13 with phones), girls 20 (18 with phones) ⇒ P(phone | boy) $=\frac{13}{18}$, P(boy | phone) $=\frac{13}{31}$.
  - Overweight 40%, heart disease 10%, both 8% ⇒ $\frac15$ and $\frac45$. Overweight 45%, fatty liver 30%, both 25% ⇒ $\frac59$, and P(not overweight | fatty liver) $=\frac16$.
  - Drunk 0.005, drunk and crash 0.003 ⇒ $\frac35$.
  - Freestyle 28, backstroke 20, both 12 ⇒ $\frac37$ and $\frac35$.
- **2011指定乙**: P(A)=P(B)=0.6. Only "(4) P(A | B)=P(B | A)" is forced (equal denominators).
  - $P(A\cup B)$ may be 0.8, giving $P(A\cap B)=0.4$, $P(A\mid B)=\frac23$, and not independent.
- **2011指定乙 (groups A–D of 100 each, Q1/Q2 correct rates)**:
  - Q1 correct counts 100/80/70/20 and Q2 correct 100/80/30/0.
  - P(group B | wrong on Q2) $=\frac{20}{20+70+100}<0.5$.
  - Overall rates $\frac{270}{400}$ vs $\frac{210}{400}$ differ by 15% ✓.
  - In group C, P(both correct) ≤ 0.3 ✓.
  - Ans (3)(4).
- **Symmetry shortcut**:
  - 10 balls (6W 4R), 3 draws, given exactly 2 white ⇒ P(2nd is white) $=\frac23$.
  - 12 balls (8W), 4 draws, given exactly 3 white ⇒ P(3rd is white) $=\frac34$, with or without replacement.
  - **2015學測**: 3W3R drawn by 甲…戊; given 甲 and 乙 drew different colours ⇒ P(戊 red) $=\frac12$.

### 21.2 乘法原理、全機率 (加法原理)、抽籤
- **乘法原理**: $P(A\cap B)=P(A)P(B\mid A)$; $P(A_1\cap\cdots\cap A_k)=P(A_1)P(A_2\mid A_1)P(A_3\mid A_1\cap A_2)\cdots$. Follow a tree diagram.
- **全機率**: for a 分割 $\{A_1,\dots,A_r\}$ (disjoint, union S), $P(B)=\sum P(A_i)P(B\mid A_i)$.
  - 例: pick 甲 (3藍5白) or 乙 (2藍1白2紅) with probability ½ each ⇒ P(藍) $=\frac12\cdot\frac38+\frac12\cdot\frac25=\frac{31}{80}$.
  - 例: die 1–2 ⇒ 甲 (5W2R), else 乙 (4W3R); draw 2 ⇒ P(1W1R) $=\frac13\cdot\frac{10}{21}+\frac23\cdot\frac{12}{21}=\frac{34}{63}$.
  - 例: 3 bags (1R2W / 3R4W / 5R6W) ⇒ P(白) $=\frac13(\frac23+\frac47+\frac6{11})=\frac{412}{693}$.
  - 例 (83社): 甲 2B3W, 乙 2B2W, 丙 1B2W; one from each ⇒ P(at least 2 black) $=\frac{11}{30}$.
- **With vs without replacement** (4R 5B, two draws):

| | 兩紅 | 先藍後紅 | 第一紅⇒第二藍 | 一紅一藍 |
|---|---|---|---|---|
| 放回 | $\frac{16}{81}$ | $\frac{20}{81}$ | $\frac59$ | $\frac{40}{81}$ |
| 不放回 | $\frac{12}{72}$ | $\frac{20}{72}$ | $\frac58$ | $\frac{40}{72}$ |

- More draws:
  - 5W 8B, three draws without replacement ⇒ P(W,B,W) $=\frac{5\cdot8\cdot4}{13\cdot12\cdot11}=\frac{160}{1716}$; P(1st black) = P(2nd black) $=\frac8{13}$.
  - 4W 3B ⇒ P(2W1B as a set) $=\frac{18}{35}$; ordered W,W,B without replacement $=\frac6{35}$; with replacement, P(2W1B) $=\frac{144}{343}$.
  - 5W 4B ⇒ P(W then B) is $\frac{20}{81}$ with replacement and $\frac5{18}$ without.
  - **Pólya urn** (put back plus one of the same colour; 4R 3W) ⇒ P(R,R,R) $=\frac47\cdot\frac58\cdot\frac69=\frac5{21}$.
  - 20 products with 4 defective: P(2nd defective found on the 4th check) is $\frac{3\cdot4\cdot16\cdot15\cdot3}{20\cdot19\cdot18\cdot17}=\frac{24}{323}$ without replacement and $3(0.2)^2(0.8)^2=\frac{48}{625}$ with replacement.
- **抽籤公平性**: drawing lots in order without replacement, every position has the same win probability $\frac rn$.
  - Proof by the tree, or by arranging the n lots in a line.
  - 10 lots with 3 prizes: P(甲乙 both win) $=\frac1{15}$; P(甲 loses, 乙 wins) $=\frac7{30}$; P(乙 wins | 甲 loses) $=\frac13$; P(乙 wins) $=\frac3{10}$.
  - 9 lots with 4 prizes: P(甲乙 lose, 丙 wins) $=\frac59\cdot\frac48\cdot\frac47=\frac{10}{63}$.
  - 4R 3W, P(3rd draw white) $=\frac37$.
  - 12 cells with 5 prizes: $\frac5{33}$, $\frac{35}{132}$, and $\frac7{11}$ for P(乙 not | 甲 wins).
  - Keys: 5 keys, 1 opens ⇒ $\frac15$; given the first failed ⇒ $\frac14$.
  - N balls with M white ⇒ P(2nd black | 1st white) $=\frac{N-M}{N-1}$.
- **Recursive probabilities**:
  - Balls 1–9, with replacement; P(n) = P(sum of first n is even) ⇒ $P(n+1)=\frac49P(n)+\frac59(1-P(n))$ ⇒ $(r,s)=(\frac59,-\frac19)$.
  - Balls 1–5 ⇒ $(\frac35,-\frac15)$.
  - **2002指定甲 彩票**: numbers 1–3, never the same as yesterday, day 1 is 3 ⇒ $q_{n+1}=\frac12(1-q_n)$ ⇒ $q_5=\frac38$.
  - Ball swaps between two bags (甲 1W1B, 乙 2W; move 甲→乙 then 乙→甲, twice) ⇒ P(甲 1W1B) $=\frac59$, P(乙 1W1B) $=\frac49$.
- **2007指定乙**: 4 equal teams, random bracket ⇒ P(final is 甲 vs 乙) $=\frac23\cdot\frac14=\frac16\approx0.167$.
- **2008指定甲 (odd-one-out coin game)**: each round someone is out with probability $\frac34$.
  - (A) P(甲 out in round 1) $=\frac14$, not $\frac13$ ✗.
  - (C) P(first exit in round 3) $=(\frac14)^2\frac34=\frac3{64}$ ✓.
  - (D) By symmetry, P(甲 | exit in round 10) $=\frac13$ ✓.
  - (E) P(at least 6 rounds) $=(\frac14)^5=\frac1{1024}<\frac1{1000}$ ✗.
  - Ans (C)(D).
- **8 people in 4 cars, two per car**: P(甲乙 together) $=\frac17$.
- **Racing car** (breaks down at A w.p. $\frac1{10}$, at B w.p. $\frac1{21}$, independently):
  - P(one lap) $=\frac{9}{10}\cdot\frac{20}{21}=\frac67$.
  - P(exactly n laps) $=(\frac67)^n\frac17$.
  - E[laps] $=\frac{6/7}{1/7}=6$.

### 21.3 獨立事件
- **Definition**: A, B are 獨立 ⇔ $P(A\cap B)=P(A)P(B)$ ⇔ $P(B\mid A)=P(B)$ (if P(A)>0). Otherwise they are 相關.
  - Independence is decided by the definition, never by intuition.
  - One die: A={1,2,3}, B={2,4} are independent ($\frac16=\frac12\cdot\frac13$); A and C={4,5,6} are not.
  - Without replacement, successive draws are dependent: 5R3W gives P(B | A) $=\frac47\ne P(B)=\frac58$. With replacement they are independent.
- **Properties**:
  - A, B independent ⇒ so are A′,B; A,B′; and A′,B′.
  - Any event is independent of ∅ and of S.
  - **互斥 with positive probabilities ⇒ 相關** (never independent).
  - "A⊥B and B⊥C" does not give A⊥C.
- **三事件獨立** needs **all four** conditions: the three pairwise ones and $P(A\cap B\cap C)=P(A)P(B)P(C)$.
  - Pairwise independence is not enough. Balls 1–9 with A={1,5,9}, B={2,5,8}, C={3,5,7}: pairwise $\frac19=\frac13\cdot\frac13$, but $P(A\cap B\cap C)=\frac19\ne\frac1{27}$.
  - Two coins with A = 1st tail, B = 2nd head, C = one head and one tail: all pairs are independent, but A, B, C are 相關.
  - If A, B, C are independent, so is any choice of complements.
- **Using independence**:
  - $P(A\cup B)=\frac12$, $P(A)=\frac25$: independent ⇒ $P(B)=\frac16$; mutually exclusive ⇒ $P(B)=\frac1{10}$.
  - "At least one" = $1-\prod(1-p_i)$. Example: A, B, C with 0.1, 0.2, 0.3 ⇒ $1-0.9\cdot0.8\cdot0.7=0.496$.
  - Shooters $\frac14,\frac16,\frac18$ ⇒ none hit $\frac{35}{64}$, exactly one $\frac{71}{192}$.
  - Shooters 0.5, 0.6, 0.8 ⇒ exactly one 0.26, none 0.04, P(甲 | exactly one) $=\frac2{13}$.
  - Shooters 0.4, 0.5, 0.6 ⇒ exactly two $\frac{19}{50}$, P(甲 and 乙 | exactly two) $=\frac4{19}$.
  - Shooters $\frac13,\frac34,\frac25$ ⇒ hit $\frac9{10}$, three $\frac1{10}$, two $\frac{23}{60}$, one $\frac{25}{60}$, P(甲 | exactly one) $=\frac3{25}$.
  - Seeds 0.9 and 0.75 ⇒ exactly one 0.3, none 0.025, at least one 0.975.
  - Phones (switch with 0.8, independent) ⇒ both 0.64, at least one 0.96.
  - Life over ten years ($\frac14,\frac13$) ⇒ both $\frac1{12}$, at least one $\frac12$, none $\frac12$.
  - Two hires: P(at least one stays) $=\frac49$, P(exactly one) $=\frac29$ ⇒ P(both stay) $=\frac49-\frac29=\frac29$.
  - Allergic 0.1, three patients ⇒ at least one $1-0.9^3=0.271$.
  - Alarm false w.p. 0.1, four alarms ⇒ all real $0.9^4$, exactly one false $C^4_1(0.9)^3(0.1)$.
  - **How many trials**:
    - Missile hit $\frac1{10}$ each ⇒ $1-(0.9)^n>0.98$ ⇒ $n\ge38$.
    - 愛國者 hit 0.4 ⇒ $1-0.6^n\ge0.9$ ⇒ $n\ge5$ (log2 = 0.3010, log3 = 0.4771).
  - **Circuits**: a series block works with $\prod p_i$; a parallel block with $1-\prod(1-p_i)$. Combine blocks; the answers are figure-specific.
  - **Parity**: x, y, z even with $\frac12,\frac13,\frac14$; given xy even ⇒ P(xy+z odd) = P(z odd) $=\frac34$.
    - All even with probability p ⇒ $f(p)=P(xy+z\text{ odd})=p(1-p)(3-2p)$, and $f>\frac12$ ⇔ $1-\frac{\sqrt2}2<p<\frac12$.
  - **2015指定乙**: 30 boys, 20 girls, 35 不適應 (15 適應). Independence ⇒ boys 適應 $=30\cdot\frac{15}{50}=9$, 不適應 21; girls 6 and 14.
  - **2016指定甲**: 8 coin tosses, given a head among the first two ($P=\frac34$), P(exactly 3 heads) $=\frac{\frac14C^6_1+\frac24C^6_2}{2^6}\Big/\frac34=\frac{9/64}{3/4}=\frac3{16}$.
  - **True/false guessing**: 10 T/F items (+1/−1/0); 4 certain and correct, 6 guessed ⇒ score >4 needs ≥4 of the 6 correct ⇒ $\frac{15+6+1}{64}=\frac{11}{32}$.
  - **Points problem**: first to 3 wins 7200元, stopped at 甲2:乙1 with $p=\frac23$ ⇒ P(甲 wins) $=\frac23+\frac13\cdot\frac23=\frac89$ ⇒ 甲 gets 6400元.
  - **First red wins** (2R 4W, 甲 then 乙 alternate):
    - With replacement, P(甲 wins on his 2nd draw) $=(\frac23)^2\frac13=\frac4{27}$.
    - Without replacement, P(甲 wins) $=\frac13+\frac15+\frac1{15}=\frac35$. (The 108 key prints $\frac15$, which is only P(甲 wins on his 2nd draw).)
  - Red finished first (6R 4B, no replacement): $P(A)=\frac4{10}$ (last ball black), $P(A\cap B)=\frac1{C^{10}_6}$ ⇒ P(first 6 are red | red finished first) $=\frac1{84}$.
  - **2021學測**: 2 black, 2 white, 3 red in a row. A = blacks adjacent, B = blacks not adjacent, C = no two reds adjacent.
    - $P(A)=\frac27$, $P(B)=\frac57$, $P(C)=\frac{4!\,P^5_3}{7!}=\frac27$.
    - $P(C\mid A)=\frac15$ and $P(C\mid B)=\frac8{25}$, so $2P(C\mid A)+5P(C\mid B)=2$.
    - Ans (2)(5).

### 21.4 貝氏定理
- **Formula**: $P(A_k\mid B)=\dfrac{P(A_k)P(B\mid A_k)}{\sum_iP(A_i)P(B\mid A_i)}$.
  - $P(A_k)$ is the 事前機率 (prior); $P(A_k\mid B)$ is the 事後機率 (posterior).
  - Two-case form: $P(A\mid B)=\frac{P(A)P(B\mid A)}{P(A)P(B\mid A)+P(A')P(B\mid A')}$.
- **Method**: draw a tree, or a **100000-person table** (the textbook's preferred visual). The answer is (target branch) / (all branches showing B).
- **Screening (偽陽性 when prevalence is low)**:
  - **心電圖**: prevalence 0.2%, sensitivity 90%, false positive 5% ⇒ $\frac{0.0018}{0.0018+0.0499}=\frac{18}{517}\approx0.0348$. Table per 100000: 180 true +, 4990 false +.
  - **尿液篩檢**: 0.1%, 95%, 1% ⇒ $\frac{95}{1094}\approx0.0868$.
    - Over 91% of positives are false, because non-users dominate.
    - Two independent positive tests ⇒ $\frac{9025}{10024}\approx0.9003$. So retest positives, and screen high-risk groups rather than everyone.
  - **2022學測數A**: prevalence 30%, sensitivity 80%, specificity 60%. P = P(infected | one negative) $=\frac{0.3\cdot0.2}{0.3\cdot0.2+0.7\cdot0.6}=\frac18$. P′ (three negatives) $=\frac{0.3(0.2)^3}{0.3(0.2)^3+0.7(0.6)^3}=\frac1{64}$ ⇒ $\frac P{P'}=8$, option (2).
  - **2002指定甲**: sensitivity 100%, false positive 4%, prevalence 0.2% ⇒ $\frac{0.002}{0.002+0.998\cdot0.04}\approx0.0477$ ⇒ >3% ✓, >4% ✓, >5% ✗; Ans (A)(B).
  - Cancer: 6%, 0.90, 0.05 ⇒ P(+) = 0.101, posterior $\frac{54}{101}$.
  - Disease 5%, sensitivity 99%, false positive 0.2% ⇒ P(+) = 0.0514; P(false positive | +) $=\frac{190}{5140}\approx0.037$.
  - 肝炎 10%, 90%, 5% ⇒ $\frac23$.
  - 快篩 with 偽陰率 = 偽陽率 = 20% and prevalence 2% ⇒ $\frac{0.016}{0.212}=\frac4{53}\approx0.075$.
  - TB X-ray (0.1%, 90%, 1% false positive) ⇒ $\frac{0.0009}{0.01089}=\frac{10}{121}$.
  - 口蹄疫 (prevalence 0.05; correct on healthy 0.8, on sick 0.9) ⇒ P(test healthy) = 0.765; P(sick | test healthy) $=\frac{0.005}{0.765}=\frac1{153}$.
  - Factory inspection: good→"bad" 0.20, bad→"good" 0.16, 5% defective ⇒ P(defective | tested good) $=\frac{0.008}{0.768}=\frac1{96}$.
  - **Jury**: 95% correct either way, 99% of defendants guilty ⇒ P(innocent | acquitted) $=\frac{0.0095}{0.0095+0.0495}\approx0.161$.
  - **2014學測**: 70% type 1 (cure rate 0.7 per course), 30% type 2 (never cured) ⇒ P(2nd course works | 1st failed) $=\frac{0.7\cdot0.3\cdot0.7}{0.7\cdot0.3+0.3}=\frac{49}{170}\approx0.29$, option (2) 0.3.
- **Suppliers / factories**:
  - LCD suppliers 70%/30% with 3%/6% defective ⇒ P(甲 | defective) $=\frac{21}{39}\approx0.5385$.
  - Bulbs 40/35/25% with 3/2/4% ⇒ P(defective) $=\frac{29}{1000}$, P(甲 | def) $=\frac{12}{29}$.
  - Machines 50/30/20% with 3/4/5% ⇒ 0.037 and $\frac{15}{37}$.
  - **2007指定甲**: six equal factories, defect rate $\frac k{50}$ ⇒ P(factory 5 | defective) $=\frac5{21}$.
  - Lines 甲乙丙 with 5%/3%/3% defective; require P(甲 | defective) ≤ $\frac5{12}$ ⇒ 甲's share ≤ 30%.
  - Insurance: high-risk 30% (accident 0.4), others 0.2 ⇒ P(accident) = 0.26, P(high | accident) $=\frac6{13}\approx0.462$.
- **Bags**:
  - 3 bags (1R2W / 3R4W / 5R6W), white drawn ⇒ P(甲) $=\frac{2/3}{2/3+4/7+6/11}=\frac{77}{206}$.
  - Bag 甲 (1R 2橙 3黃) or 乙 (4綠 5藍 6紫), two balls of different colours ⇒ P(甲) $=\frac{11/15}{11/15+74/105}=\frac{77}{151}$.
  - Die: 1 ⇒ 甲 (3R2W), even ⇒ 乙 (1R5W), 3 or 5 ⇒ 丙 (4R6W); white ⇒ P(甲) $=\frac4{41}$.
  - Grades 36/34/30% with myopia 30/40/50%; not myopic ⇒ P(高一) $=\frac{0.252}{0.606}=\frac{42}{101}$.
  - Teachers 45% male (40% coffee), 55% female (60%) ⇒ P(male | coffee) $=\frac6{17}$.
  - **2012指定甲**: staff 15/35/50% with degrees 60/40/80% ⇒ P(technical | degree) $=\frac{0.14}{0.63}=\frac29$, option (1).
  - **Bridge club**: classes 40/30/30% with basketball shares $\frac14,\frac15,\frac13$ ⇒ P(basketball) $=\frac{13}{50}$. (99 version with shares $\frac15,\frac15,\frac13$: $\frac{24}{100}$, and P(甲 | basketball) $=\frac13$.)
  - Gold coin: 甲 has 5 silver + 1 gold, 乙 has 3 silver; move 4 from 甲 to 乙, then 5 back ⇒ P(gold goes to 乙) $=\frac{C^5_3}{C^6_4}=\frac{10}{15}$, P(it stays among 乙's 2 kept coins) $=\frac{C^6_5}{C^7_5}=\frac6{21}$ ⇒ $\frac4{21}$.
  - Lock at 10–11 pm w.p. ½; takes 3 of 10 keys (2 fit) ⇒ P(gets in) $=\frac12+\frac12\cdot\frac8{15}=\frac{23}{30}$.
  - Umbrella forgotten w.p. $\frac15$ at each of 乙, 丙, 丁; it was lost ⇒ P(at 丙) $=\frac{(4/5)(1/5)}{1-(4/5)^3}=\frac{20}{61}$.
- **Guessing / testimony**:
  - Knows the answer w.p. 0.8, else guesses 1 of 5; answered correctly ⇒ P(knew) $=\frac{0.8}{0.84}=\frac{20}{21}$ (89學科).
  - Knows w.p. 0.7; correct ⇒ P(guessed) $=\frac{0.06}{0.76}=\frac3{38}$.
  - Forecast: sunny 40%; says sunny w.p. 0.7 if sunny, 0.2 if not ⇒ $\frac7{10}$.
  - Two witnesses (甲 truthful 0.7, 乙 0.9); 3W 7B; both say white ⇒ $\frac{0.189}{0.189+0.021}=\frac9{10}$.
  - 4R 6B, 甲 0.6, 乙 0.7, both say black ⇒ P(actually red) $=\frac{0.4\cdot0.12}{0.4\cdot0.12+0.6\cdot0.42}=\frac4{25}$.
- **Updating several hypotheses**: priors $\frac16,\frac13,\frac12$ for advisers A, B, C. After "unemployment rose", the posteriors are $\frac49,\frac29,\frac39$.
- **2021學測 (dark-room digit reading)**: the actual→perceived table has 6→(6, 8, 9) = (0.4, 0.3, 0.2); 8→8 is 0.4; 9→9 is 0.5.
  - P(actual 6 | seen 6) $=\frac{0.4}{0.4+0.3+0.2}=\frac49<\frac12$ ✓.
  - P(actual 9 | seen 9) $=\frac58<\frac23$ ✗.
  - Ans (2)(3)(4).
- **Two dice in a bag**: a fair die, and one with faces 1, 3, 5, 7, 9, 11. Prime ⇒ roll the same die again, else switch. P(1st prime | 2nd prime) $=\frac{25/72}{43/72}=\frac{25}{43}$.
- **2009指定乙 (misclassification)**: 760 tested, 735 healthy; 665 judged healthy, of whom 660 truly are.
  - Errors are 5 (sick judged healthy) plus 75 (healthy judged sick) ⇒ $\frac{80}{760}=\frac2{19}$.

### 21.5 客觀機率與主觀機率
- **古典機率**: from equally likely outcomes. Two 筊杯 ⇒ P(聖筊) = 50%.
- **客觀機率 (頻率機率)**: the relative frequency $\frac kn$ from repeated trials or recorded data. 5014 聖筊 in 10000 throws ⇒ 50.14%.
  - It varies from sample to sample but stabilises as n grows (GeoGebra die simulations approach $\frac16$). A persistent deviation suggests an unfair die.
  - Small samples are unreliable. In the 王威晨 batting example, the 2016 and 2017 seasons had only 12 and 113 at-bats, so they are poor predictors.
  - Examples:
    - Red lights over 20 days: P(2) $=\frac5{20}$, P(≥3) $=\frac{6+4+2}{20}=\frac35$.
    - Commute-time table: P(late) = P(T > 16) = 0.2+0.1 = 0.3.
    - 甲 hits 3 of 5, 乙 2 of 3 ⇒ both $\frac25$, exactly one $\frac7{15}$.
- **主觀機率**: a personal degree of belief (NBA champion, "運氣很旺 so 80%").
  - There is no single right value, but it **must obey the axioms**: $0\le P\le1$; complementary or exhaustive outcomes sum to 1; and $A\subseteq B\Rightarrow P(A)\le P(B)$.
  - Not appropriate: P(win final) = 80% > P(reach final) = 50%.
  - Not appropriate: Lakers 70% and Warriors 40% in a two-team final.
  - Not appropriate: P(ends in "ing") = 0.6 > P(5th letter n) = 0.5, since the first event implies the second.
  - Not appropriate: 120%.
- **Classify** (108 習題13/14):
  - Fair coin twice ⇒ 25% is 古典.
  - "Sunny so stocks rise $\frac23$" and "nicer uniforms so 80%" are 主觀.
  - "12–8 record ⇒ 60%" and "15 defects per 100 ⇒ 15%" are 客觀.
  - "6 hits in 10 ⇒ 60% hit rate" is a 客觀 frequency, but it does not guarantee 6 hits in the next 10.
  - A subjective 60% for 甲 forces 40% for 乙 when there is no draw.
- **Mixed (2019指定乙)**: walk 60 min, or bike T ∈ [30, 40] with interval probabilities. Ans (3)(4).
  - (3) A 5-day total of 250 forces 3 walking days and 2 biking days.
  - (4) P(2-day total ≥90) $=1-\frac14=\frac34$.
- **Data-based probability**: from birth data, P(male newborn) ≈ 0.519 for 105年 and ≈ 0.518 pooled over 101–107年.

**Traps**:
- $P(A\mid B)$ vs $P(B\mid A)$: identify which event is **given**; the denominator is the given event.
- "Exactly one 2" vs "at least one 2" vs "the first is 2" are different conditions.
- 互斥 ≠ 獨立. Positive-probability mutually exclusive events are always dependent.
- Pairwise independence does not imply three-way independence; check the triple product.
- Without replacement, draws are dependent, but each position is still equally likely (抽籤公平).
- Bayes with a low prior: even accurate tests give small posteriors. Do not equate sensitivity with P(disease | +).
- "At least one" ⇒ use the complement $1-\prod(1-p_i)$, valid only under independence.
- A subjective probability is free in value but must satisfy the axioms (range, complements, monotonicity).

---

# Part C — handout content beyond 學測數A **[超出數A]**

These sections record what the 99課綱 數甲 handouts and the 資優班 units teach beyond the 108 數A 學測 scope (scope.md §8: 極限、微積分、圓錐曲線、二項分布、統計推論 are not tested; 複數極式 is 數甲). Use them for enrichment or for recognising old 指考 items. Do not present them as 學測數A targets.

## 22. 複數與複數極式（棣美弗定理、n 次方根、複數平面幾何） [超出數A]

**Scope**: [超出數A]. 108 places 複數 in 12年級數甲. Basic $i$, standard form and quadratics with complex roots are summarised in §7 (99 2-3), also [超出數A]. **Sources**: 資優 第4單元複數, 第24單元複數極式; 99數甲上 2-3複數的幾何意涵; 資優 三角函數複習題 (complex items).

### 22.1 複數基本
- **Powers of i**: $i^2=-1$ and $i^{4m+k}=i^k$. For a<0, $\sqrt a=\sqrt{-a}\,i$, so $\sqrt{-2}\sqrt{-3}=-\sqrt6$; the rule $\sqrt a\sqrt b=\sqrt{ab}$ fails when both are negative.
  - $i^{97}+i^{102}+i^{303}-i^{27}=i-1$.
  - $x+y=-7$, $xy=4$ ⇒ x, y<0 ⇒ $(\sqrt x+\sqrt y)^2=x+y+2\sqrt x\sqrt y=-7-4=-11$.
  - $a+b=-13$, $ab=9$ ⇒ $\sqrt a+\sqrt b=\sqrt{19}\,i$ (pick the sign: both roots are $\sqrt{|\cdot|}\,i$).
- **Standard form a+bi**: Re z = a and Im z = b.
  - $z=a+bi$ with b≠0 is 虛數; with a=0 as well it is 純虛數.
  - $N\subset Z\subset Q\subset R\subset C$.
  - Equality: equal real parts and equal imaginary parts.
- **Operations**: as polynomials with $i^2=-1$; to divide, multiply by the conjugate.
- **Conjugate** $\bar z=a-bi$:
  - $z+\bar z$ and $z\bar z=|z|^2$ are real.
  - z is real ⇔ $\bar z=z$; z is purely imaginary or 0 ⇔ $\bar z=-z$.
  - $\overline{z_1\pm z_2}=\bar z_1\pm\bar z_2$, $\overline{z_1z_2}=\bar z_1\bar z_2$, $\overline{z^n}=\bar z^n$.
- **Square roots**: solve $(x+yi)^2=a+bi$ by comparing parts.
  - $8+6i$ ⇒ $\pm(3+i)$; $5+12i$ ⇒ $\pm(3+2i)$; $5-12i$ ⇒ $\pm(3-2i)$; $i$ ⇒ $\pm\frac{1+i}{\sqrt2}$.
  - $z^2-2(1+i)z-5+14i=0$ ⇒ $(z-1-i)^2=5-12i$ ⇒ $z=-2+3i,\ 4-i$.
- **No order on C**: $a^2+b^2=0\not\Rightarrow a=b=0$ and $a^2\ge0$ can fail. "5i > 4i" is meaningless.
- **Quadratics**: with real coefficients, D<0 gives 共軛虛根; with complex coefficients the discriminant test fails.
  - $4x^2-(3a+i)x+a-i=0$ with a real root ⇒ compare imaginary parts ⇒ root −1, other root 1+i.
  - $3x^2+(a+i)x+2i-6=0$ ⇒ roots −2 and 1−i.
  - $\omega=\frac{-1+\sqrt3i}2$: $\omega^3=1$, $1+\omega+\omega^2=0$, $\omega^2=\bar\omega=\frac1\omega$.
  - $x^3+ax^2+x+2=0$ has a purely imaginary root ⇒ put x=ki ⇒ a=2.
  - $i(x+i)^3$ real ⇒ x=0 or $\pm\sqrt3$.

### 22.2 複數平面、絕對值
- **Plane**: z=x+yi ↔ (x,y); $\bar z$ is the reflection in the real axis.
- **Modulus**: $|z|=\sqrt{x^2+y^2}$.
  - $|z_1z_2|=|z_1||z_2|$, $|\frac{z_1}{z_2}|=\frac{|z_1|}{|z_2|}$, $|z|^2=z\bar z$.
  - Triangle inequality: $||z_1|-|z_2||\le|z_1\pm z_2|\le|z_1|+|z_2|$.
  - Example: $\left|\frac{(2+i)^2(3+i)^3}{(1-3i)(1-2i)^4}\right|=2$.
- **Geometry of + and −**: z+w completes the parallelogram; $|z-w|$ is the distance AB.
  - $|z-a|=|z-b|$ is a perpendicular bisector (直線). $|z-a|=r$ is a circle.
  - Sum of distances to two points is an ellipse ([超出], §23).
  - $|z+3|^2+|z-3|^2$ with $|z|=2$ ⇒ $2(|z|^2+9)=26$.
- **Exam items**:
  - **2007學科**: Γ: |z−1|=1, Ω={iz}, i.e. Γ rotated 90° ⇒ the circle |w−i|=1 ⇒ 2i, 1+i, −1+i ∈ Ω; Ans (1)(3)(5).
  - **2005指定甲**: $(1+i)z-(1-i)\bar z=0$ ⇒ $(1+i)z$ is real ⇒ a line through O, option (3).
  - **Line + circle**: $z-\bar z=-3i$ ⇒ $y=-\frac32$ ⇒ min $|7+8i-z|=8+\frac32=\frac{19}2$.
  - Min of $|z-z_1|+|z-z_2|$ for z=t+ti, with $z_1=-6+6i$, $z_2=2+6i$ (same side of y=x): reflect $z_2$ to (6,2) ⇒ min $4\sqrt{10}$ at t=3.
  - |z|=1 ⇒ $|z^2-z+1|\in[0,3]$ (max at z=−1; zero at $z=\frac{1+\sqrt3i}2$).

### 22.3 極式與棣美弗定理
- **Polar form**: $z=r(\cos\theta+i\sin\theta)$ with r=|z|≥0; θ is an 輻角 and the 主輻角 Arg z lies in [0,2π).
  - The form must be **r(cos θ + i sin θ) with r≥0 and the same angle**. Rewrite first:
    - $\sin25^\circ+i\cos25^\circ=\mathrm{cis}65^\circ$.
    - $\cos70^\circ-i\sin70^\circ=\mathrm{cis}(-70^\circ)$.
    - $-3\,\mathrm{cis}25^\circ=3\,\mathrm{cis}205^\circ$.
    - $\sin200^\circ-i\cos160^\circ=\mathrm{cis}250^\circ$ (indeed $\cos250^\circ=\sin200^\circ$ and $\sin250^\circ=-\cos160^\circ$).
    - $\cos135^\circ-i\sin45^\circ=\mathrm{cis}225^\circ$.
  - $1-\cos140^\circ+i\sin140^\circ=2\sin70^\circ\,\mathrm{cis}20^\circ$, by half-angle: $1-\cos\phi=2\sin^2\frac\phi2$. Likewise $1-\cos130^\circ+i\sin130^\circ=2\sin65^\circ\,\mathrm{cis}25^\circ$, whose 18th power is purely imaginary and 36th power is real.
- **Products and quotients**: multiply the moduli and add the arguments; divide the moduli and subtract the arguments. $\frac1z=\frac1r\mathrm{cis}(-\theta)$.
- **棣美弗**: $(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$ for every integer n.
  - $\left(\frac{-\sqrt3+i}2\right)^6=\mathrm{cis}900^\circ=-1$.
  - $(\sqrt3+i)^n$ is purely imaginary first at n=3.
  - $x=\frac{1-\sqrt3i}2=\mathrm{cis}(-60^\circ)$ ⇒ $1+x+\dots+x^{84}=1$.
  - $\frac{1+i\tan\frac\pi8}{1-i\tan\frac\pi8}=\mathrm{cis}\frac\pi4$.
  - |z|=1 ⇒ $\frac{1+z}{1+\bar z}=z$; with $z=\mathrm{cis}\frac\pi{24}$, $\left(\frac{1+\cos\theta+i\sin\theta}{1+\cos\theta-i\sin\theta}\right)^{100}=\mathrm{cis}\frac{25\pi}6=\frac{\sqrt3}2+\frac i2$.
  - $z^2-2\cos8^\circ z+1=0$ ⇒ $z=\mathrm{cis}(\pm8^\circ)$ ⇒ $z^{15}+z^{-15}=2\cos120^\circ=-1$.
  - $z(\sqrt3+i)=-2\sqrt3+2i$ ⇒ $z=2\,\mathrm{cis}\frac{2\pi}3$.
- **Triangle identities**: in △ABC, $\mathrm{cis}A\,\mathrm{cis}B\,\mathrm{cis}C=\mathrm{cis}\pi=-1$. If $\frac{\mathrm{cis}A}{\mathrm{cis}B\,\mathrm{cis}C}$ is real ⇒ $2A-\pi=k\pi$ ⇒ A=90°.
- **2003學科**: $(4+3i)\mathrm{cis}\theta<0$ ⇒ $\theta=\pi-\arg(4+3i)\approx143^\circ$, 第二象限 (2).
- **2012學測**: ∠AOB=90° ⇒ $\frac zw$ is purely imaginary ⇒ $\frac{z^2}{w^2}<0$ and $(z\bar w)^2<0$ (since $z\bar w=|w|^2\frac zw$); Ans (4)(5).
- **2018指定甲**: |z₁|=2, |z₂|=3, |z₁−z₂|=√5 ⇒ cos∠AOB $=\frac{4+9-5}{12}=\frac23$ ✓.
  - $|z_1+z_2|=\sqrt{2(4+9)-5}=\sqrt{21}$, so the option √23 ✗.
  - $\frac{z_2}{z_1}=\frac32\mathrm{cis}(\pm\angle AOB)$ ⇒ $a=\frac32\cdot\frac23=1>0$ ✓, the sign of b is unknown ✗, and ∠BOC = arg z₁ can be $\frac\pi2$ ✓.
  - Ans (1)(3)(5).
- **2011學測**: points inside △O(0), (1+i), (1−i), i.e. $|y|<x<1$: cos60°, $\frac{4-3i}5$, $(\mathrm{cis}30^\circ)^{25}=\mathrm{cis}30^\circ$. Ans (1)(3)(5).
- Region $A=\{r\,\mathrm{cis}\theta: 0\le r\le1,\ \frac{3\pi}4\le\theta\le\frac{5\pi}4\}$ ⇒ $z^3$ fills r≤1, $\frac{9\pi}4\le3\theta\le\frac{15\pi}4$, i.e. the disc minus the wedge $|\theta|<\frac\pi4$ (option (5)).
- **Expanding with the binomial theorem** gives multiple-angle formulas: $\cos3\theta=4\cos^3\theta-3\cos\theta$, $\sin3\theta=3\sin\theta-4\sin^3\theta$, $\cos4\theta=8\cos^4\theta-8\cos^2\theta+1$.
  - $a_0-a_2+a_4-\dots$ for $(1+x)^n$ equals $\mathrm{Re}(1+i)^n=2^{n/2}\cos\frac{n\pi}4$.
- **Trigonometric sums**: $\sum_{k=1}^{n}\cos\frac{2k\pi}{2n+1}=-\frac12$ (real part of a geometric series of roots).
  - $\sum\cos(\alpha+k\beta)=\frac{\sin\frac{n\beta}2}{\sin\frac\beta2}\cos(\alpha+\frac{(n-1)\beta}2)$.
  - $\prod_{k=1}^{m}\sin\frac{k\pi}{2m+1}=\frac{\sqrt{2m+1}}{2^m}$ ⇒ $\prod_{k=1}^7\sin\frac{k\pi}{15}=\frac{\sqrt{15}}{128}$.
  - $\cos\frac\pi{10}\cos\frac{2\pi}{10}\cos\frac{3\pi}{10}\cos\frac{4\pi}{10}=\frac{\sqrt5}{16}$.

### 22.4 n 次方根
- **Roots of unity**: $z^n=1$ ⇒ $z_k=\mathrm{cis}\frac{2k\pi}n$, k=0,…,n−1. They are the vertices of a regular n-gon on the unit circle.
  - With $\omega=\mathrm{cis}\frac{2\pi}n$: $1+\omega+\dots+\omega^{n-1}=0$, and $z^{n-1}+\dots+z+1=\prod_{k=1}^{n-1}(z-\omega^k)$.
    - ⇒ $\prod_{k=1}^{n-1}(1-\omega^k)=n$. For example, the product of $AB\cdot AC\cdot AD\cdot AE$ for the 5th roots is 5; for 7th roots it is 7.
    - ⇒ for n=5, $\prod(2+\omega^k)=2^4-2^3+2^2-2+1=11$.
  - $z^4+z^3+z^2+z+1=0$ has roots $\mathrm{cis}\frac{2k\pi}5$, k=1–4, and then $\sum_{k=1}^4\cos k\theta=-1$, $\sum\sin k\theta=0$.
  - $\sum_{k=1}^7\alpha^{2k}=0$ for $\alpha=\mathrm{cis}\frac{2\pi}7$.
  - **2002學科**: $z^6=1$, z≠1 ⇒ |z|=1 ✓; $z^3=\pm1$ ✓; $|z^4|=1$ ✓; $1+\dots+z^5=0$ ✓; but $z^2=1$ ✗. Ans (A)(C)(D)(E).
- **General roots**: $z^n=R\,\mathrm{cis}\phi$ ⇒ $z_k=\sqrt[n]R\,\mathrm{cis}\frac{\phi+2k\pi}n$, a regular n-gon of radius $\sqrt[n]R$.
  - $x^5=-1+i=\sqrt2\,\mathrm{cis}\frac{3\pi}4$ ⇒ $2^{1/10}\mathrm{cis}\frac{3\pi+8k\pi}{20}$.
  - $(z+3)^6=8-8\sqrt3i$ ⇒ $z=-3+\sqrt[6]{16}\,\mathrm{cis}\frac{-\pi/3+2k\pi}6$.
  - $x^3-6x^2+12x+8=0$ ⇒ $(x-2)^3=-16$.
  - $(z-1+2i)^4=-8-8\sqrt3i$ ⇒ a square centred at 1−2i with circumradius 2 ⇒ area 8.
- **Polygons from cyclotomic pieces**:
  - $z^6+z^4+z^2+1=0$ ⇒ the 8th roots except ±1 ⇒ a hexagon of area $2\sqrt2-(\sqrt2-1)=\sqrt2+1$.
  - $x^{10}+x^8+\dots+1=0$ ⇒ the 12th roots except ±1 ⇒ a 10-gon of area $3-\frac{2-\sqrt3}2=2+\frac{\sqrt3}2$.
- **2017指定甲**: $z^n+z^{-n}+2=0$ ⇔ $(z^n+1)^2=0$ ⇔ $z^n=-1$.
  - So r=1; n can be even; there are exactly n solutions; $\theta=\frac{(2k+1)\pi}n$.
  - $\frac{3\pi}7$ ✓ (n=7). $\frac{4\pi}7$ ✗ (odd/even parity).
  - Ans (1)(4).

### 22.5 複數與平面幾何
- **Multiplying by $r\,\mathrm{cis}\theta$** rotates by θ about O and scales by r (the matrix $rR_\theta$, §20.6). Multiplying by i is a 90° rotation, so z ⊥ iz. $\bar z$, $-z$, $-\bar z$ are the reflections in the real axis, the origin and the imaginary axis.
- **Rotation about a point a**: $w-a=(z-a)\,\mathrm{cis}\theta$.
- **Angle** ∠AOB = arg$\frac{z_2}{z_1}$. $\frac{z_2-z_1}{z_3-z_1}$ real ⇔ collinear; purely imaginary ⇔ perpendicular.
  - **2003指定乙**: equilateral OAB with A(1,2), B counter-clockwise ⇒ $b_1+ib_2=\mathrm{cis}60^\circ(1+2i)$ ⇔ $R_{60^\circ}\binom12$; Ans (A)(D).
  - Equilateral OAB with A=1+i ⇒ $B=\frac{1\mp\sqrt3}2+\frac{1\pm\sqrt3}2i$.
  - |OB|=4, |OA|=2, ∠AOB=60° ⇒ $\frac{z_2}{z_1}=1+\sqrt3i$.
  - $z_2=(1+i)z_1$, |z₁|=2 ⇒ area of △OAB = 2.
  - $\alpha=2\mathrm{cis}\frac\pi5$, $\beta=3\mathrm{cis}\frac{8\pi}{15}$ ⇒ angle $\frac\pi3$ ⇒ area $\frac{3\sqrt3}2$, AB=√7.
  - $\alpha^2-2\alpha\beta+4\beta^2=0$ ⇒ $\frac\alpha\beta=1\pm\sqrt3i=2\mathrm{cis}(\pm\frac\pi3)$ ⇒ OP:OQ:PQ = 2:1:√3.
  - $x^4-x^2+1=0$ with roots A–D, P=i ⇒ $PA\cdot PB\cdot PC\cdot PD=|i^4-i^2+1|=3$.
  - Hexagon centred at O with A(4,2) ⇒ $C=A\cdot\mathrm{cis}120^\circ=(-2-\sqrt3,\ 2\sqrt3-1)$. Hexagon with A(a,0), F(0,b), B(9,√3) ⇒ (a,b)=(4,2√3). Square with A(2,1), B(5,5) ⇒ D(−2,4), C(1,8).
  - **2019指定甲**: a regular hexagon has consecutive clockwise vertices z, 0, z+5−2√3i.
    - With w = z+5−2√3i, going clockwise means $w=z\,\mathrm{cis}120^\circ$ (the interior angle at 0 is 120°). The centre is $z+w$.
    - So $z(\mathrm{cis}120^\circ-1)=5-2\sqrt3i$, with $\mathrm{cis}120^\circ-1=\sqrt3\,\mathrm{cis}150^\circ$ ⇒ $z=\frac{(5-2\sqrt3i)\,\mathrm{cis}(-150^\circ)}{\sqrt3}=-\frac72+\frac{\sqrt3}6i$.
    - So **Re z = $-\frac72$**.
- **Polar coordinates** (overlaps §12): [r, θ] ↔ (r cos θ, r sin θ); [r, θ] = [−r, θ+π].
  - Distance via the law of cosines: $AB^2=r_1^2+r_2^2-2r_1r_2\cos(\theta_1-\theta_2)$; e.g. [3, π/3] and [4, π] ⇒ $\sqrt{37}$.
  - Polar curves (資優24 補充): line $r\cos(\theta-\alpha)=p$; circle with centre [ρ, α] and radius a: $r^2-2\rho r\cos(\theta-\alpha)=a^2-\rho^2$; $r=a\sin2\theta$ (four-leaf rose). These are enrichment only.

**Traps**: $\sqrt a\sqrt b$ with both negative; a polar form needs r≥0 and the pattern cos + i sin of the same angle; complex numbers cannot be ordered; real-coefficient facts (conjugate roots, discriminant) fail for complex coefficients; the n-th roots number exactly n.

---

## 23. 圓錐曲線（拋物線、橢圓、雙曲線） [超出數A]

**Scope**:
- [超出數A]. 圓錐曲線 is 數B (S-11B-2 截痕) and 12年級 數甲 content.
- For 數A, a parabola appears only as the **graph of a quadratic function** (§7: vertex, axis, opening). Focus, directrix, ellipse and hyperbola are not tested.
- Old 學測 items (2005–2020) did test these under the 99 curriculum; they are listed here for reference.

**Sources**: 99第四冊 4-1拋物線, 4-2橢圓, 4-3雙曲線; 資優 第35–38單元圓錐曲線(一)–(四).

### 23.1 圓錐截痕
- **Setup**: a right circular cone with half-angle α; a plane meets the axis at angle β (not through the vertex).
  - β = 90° gives a 圓; α < β < 90° an 橢圓; β = α a 拋物線; β < α a 雙曲線 (two branches).
- **Degenerate cases** (plane through the vertex): a point, one line, or two intersecting lines.
- **History**: Menaechmus (doubling the cube), Apollonius (eight books, named the curves), Pappus (focus–directrix), Kepler (continuity: hyperbola → parabola → ellipse → circle as $F_2$ moves).

### 23.2 拋物線
- **Definition**: the points P with PF = d(P, L), where F is the 焦點 and L the 準線. Related terms: 對稱軸, 頂點 V (the midpoint of F and the foot A), 焦距 = VF, 正焦弦 = 4·焦距.
- **Standard forms**:
  - $y^2=4cx$: focus (c,0), directrix x=−c, opens right if c>0.
  - $x^2=4cy$: focus (0,c), directrix y=−c.
  - Translated: $(y-k)^2=4c(x-h)$ or $(x-h)^2=4c(y-k)$, with vertex (h,k).
  - Translating by (h,k) means replacing x, y by x−h, y−k. Lengths do not change.
- **Quadratic graphs**: $y=ax^2+bx+c$ is $(x-h)^2=\frac1a(y-k)$, with focal length $\frac1{4|a|}$.
  - $y=2x^2-4x+7$ ⇒ $(x-1)^2=\frac12(y-5)$, focus $(1,\frac{41}8)$, 正焦弦 $\frac12$.
- **Oblique case**: focus F(3,−1), directrix x−y+1=0 ⇒ $x^2+2xy+y^2-14x+6y+19=0$; axis x+y−2=0; 正焦弦 $5\sqrt2$; vertex $(\frac74,\frac14)$.
  - $|3x+y-19|=\sqrt{10}\sqrt{(x+1)^2+(y-2)^2}$-type equations give a parabola with focus (−1,2); its axis is ⊥ to the directrix.
- **Focal-distance tricks**: PF = distance to the directrix.
  - **2007學測**: vertex (0,3), focus (0,6) ⇒ $x^2=12(y-3)$. With P(a,b), Q(a,0) and ∠FPQ=60°: PF=PQ=b ⇒ △FPQ is equilateral ⇒ $a^2+36=b^2$ and $a^2=12(b-3)$ ⇒ **b=12**.
  - **2008學測**: circles $O_1$ (centre (7,1), r=12) and $O_2$ (centre (−2,13), r=3) are both tangent to x=−5. The parabola with directrix x=−5 through both centres has $FO_1=12$, $FO_2=3$, and $O_1O_2=15$, so F lies on the segment ⇒ $F=(-\frac15,\frac{53}5)$.
  - $|d(P,L)-AP|$ with L: y=−5 on $x^2=8y$ (F(0,2), directrix y=−2) $=|PF-AP+3|\le AF+3=\frac{21}4$ for $A(\frac94,2)$.
  - Min PF+PA on $y^2=12x$ with A(5,4) ⇒ drop to the directrix ⇒ $P(\frac43,4)$.
  - A focal chord $AB$ of $x^2=8y$ with AB=16 ⇒ $y_1+y_2+4=16$ ⇒ $y_1+y_2=12$.
  - Equilateral △PAB on $y^2=12x$ with focus A(3,0) ⇒ b=15.
- **Other items**:
  - **2020學測**: a parabola contains an isosceles trapezoid with bases 4, 6 and height 14 ⇒ $y=ax^2$ with $4a-9a=14$ ⇒ focal length $\frac1{4|a|}=\frac5{56}$.
  - **2010學測**: $y=x^2+ax+b$ cuts the x-axis in a chord of length 7 ($a^2-4b=49$) ⇒ for b+2 the chord is $\sqrt{a^2-4b-8}=\sqrt{41}$.
  - Headlamp with diameter 12 and depth 6 ⇒ focal length $\frac32$.
  - Arch bridge: water width 4 at depth 2 ⇒ after the water drops 1 m the width is $2\sqrt6$.
  - Light from P(7,3) parallel to the axis of $y^2=8x$ reflects to F ⇒ path length = distance to the directrix = 7+2 = 9.
  - Closest point of $y^2=16x$ to $4x-3y+24=0$ is $(\frac94,6)$ at distance 3. Closest point of $y=x^2$ to AB with A(1,−4), B(5,2) is $(\frac34,\frac9{16})$ (tangent slope $\frac32$).

### 23.3 橢圓
- **Definition**: $PF_1+PF_2=2a$ with $2a>F_1F_2=2c$. If 2a=2c the locus is the segment; if 2a<2c it is empty.
- **Terms**: 中心, 長軸 2a, 短軸 2b, $a^2=b^2+c^2$, 正焦弦 $\frac{2b^2}a$, 離心率 $e=\frac ca\in(0,1)$ (larger e is flatter).
  - Focal radii range over [a−c, a+c].
- **Standard forms**: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ (a>b, foci on the x-axis), or with the larger denominator under y² for a vertical major axis. Translate as usual.
  - The focal radius is $a\pm\frac cax$.
  - Parametric form: $(a\cos\theta,b\sin\theta)$, i.e. the circle scaled by $\frac ba$ vertically ⇒ area πab (§20.6).
  - **Area / max-area problems** reduce to the circle by scaling (§20.6 enrichment).
- **Items**:
  - **91指定乙**: the vertices are 5 and 1 from a focus ⇒ a+c=5, a−c=1 ⇒ $(a,b)=(3,\sqrt5)$.
  - **2010學測**: $l_1$ for $\frac{x^2}{25}+\frac{y^2}9=1$ is 10; $l_2$ for $=2$ is $10\sqrt2$; $l_3$ for $=\frac{2x}5$ ⇔ $\frac{(x-5)^2}{25}+\frac{y^2}9=1$ is 10 ⇒ $l_1=l_3<l_2$, option (4).
  - **2011學測**: ellipse with foci (±3,0) and parabola $y^2=12x$ (focus (3,0), directrix x=−3) meet on x=3 ⇒ P(3,6) ⇒ $2a=6+6\sqrt2$ ⇒ $a=3+3\sqrt2$.
  - **2019學測**: $\frac{x^2}{a^2}+\frac{y^2}{16}=1$ with rhombus ABCD of area 58 ⇒ $2\cdot a\cdot4=58$ ⇒ $a=\frac{29}4$.
  - Billiard table with major axis 10, F₁→A→F₂→B→F₁ ⇒ perimeter of △ABF₁ = 4a = 20.
  - Planet distances 100 and 300 (萬km) ⇒ a=200, c=100 ⇒ $b^2=30000$ ⇒ 正焦弦 $\frac{2b^2}a=300$.
  - Foci (6,0), (0,8), major axis 20: centre (3,4), and all options true.
  - Focal triangle: ∠F₁PF₂=θ ⇒ area $=b^2\tan\frac\theta2$. For $\frac{x^2}{25}+\frac{y^2}{16}=1$: θ=60° ⇒ $\frac{16\sqrt3}3$; θ=30° ⇒ $16(2-\sqrt3)$.
  - Families $\frac{x^2}{p}+\frac{y^2}{q}=1$: foci on the x-axis need p>q>0. Confocal ellipses share $p-q=c^2$.
- **Optical property**: a ray from one focus reflects to the other. The tangent at P bisects the external angle of $\angle F_1PF_2$.

### 23.4 雙曲線
- **Definition**: $|PF_1-PF_2|=2a<2c$.
  - Terms: 貫軸 2a, 共軛軸 2b, $c^2=a^2+b^2$, 正焦弦 $\frac{2b^2}a$, e>1.
- **Standard forms**: $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$, with asymptotes $\frac xa\pm\frac yb=0$.
  - The 共軛雙曲線 $\frac{x^2}{a^2}-\frac{y^2}{b^2}=-1$ has the same asymptotes.
  - 等軸 means a=b, with perpendicular asymptotes.
  - Asymptotes $L_1L_2=0$ ⇒ the hyperbola is $L_1L_2=k$. The product of the distances to the two asymptotes is constant, $\frac{a^2b^2}{a^2+b^2}$.
- **Items**:
  - **2005學測**: $\frac{x^2}9-\frac{y^2}{16}=1$ (a=3, c=5); isosceles △PF₁F₂.
    - $PF_1=F_1F_2=10$ ⇒ $PF_2=4$ or 16 ⇒ perimeter 24 or 36.
    - $PF_1=PF_2$ is impossible.
    - Ans (B)(E).
  - **2018學測**: which conics have focus $(\frac12,0)$ (the focus of $y^2=2x$)?
    - $y=(x-\frac12)^2-\frac14$ ✓; $x^2+\frac{4y^2}3=1$ ✓ ($c^2=1-\frac34$); $8x^2-8y^2=1$ ✓ ($c^2=\frac18+\frac18$).
    - Not $\frac{x^2}4+\frac{y^2}3=1$ (c=1) and not $4x^2-4y^2=1$ ($c=\frac1{\sqrt2}$).
    - Ans (1)(3)(4).
  - **2017學測**: the point $(t,t^2)$ for t>0 against $\Gamma:\frac{y^2}{a^2}-\frac{x^2}{b^2}=1$ and its asymptote ℓ: y=$\frac abx$.
    - Along the curve, $f(t)=\frac{t^4}{a^2}-\frac{t^2}{b^2}$ is 0 on ℓ (at $t=\frac ab$) and then increases to 1.
    - So the point meets ℓ first, then Γ: option (5).
  - **2010學測**: $(\frac{x^2}{25}+\frac{y^2}{16})(\frac{x^2}9-\frac{y^2}{16})=0$ ⇒ the origin, or $\frac{x^2}9=\frac{y^2}{16}$ ⇒ **two intersecting lines** (3).
  - **85大學社**: the distance to x=−1 is twice the distance to F(1,0) ⇒ an ellipse with e=½: $3(x-\frac53)^2+4y^2=\frac{16}3$ ⇒ the other focus is $(\frac73,0)$.
  - A hyperbola through (3,4) with foci (−1,1), (3,1) ⇒ by symmetry also passes through (−1,4), (3,−2), (−1,−2). Ans (B)(C)(D).
  - Sound-delay (two villages as foci, a point on the hyperbola): the path-length difference is 2a, so the arrival-time difference is $\frac{2a}{340}$ (99 4-3 綜合7: 5 s).
- **Loci giving conics**:
  - A circle tangent to $x^2+y^2-4x+3=0$ and x=5 ⇒ parabolas $y^2=-8x+32$ and $y^2=-4x+12$.
  - A circle internally tangent to $x^2+y^2-8x-20=0$ and through O ⇒ $\frac{(x-2)^2}9+\frac{y^2}5=1$.
  - Ratio of distance to F(2,0) and to $x=-\frac{10}3$ is 3:5 (e=$\frac35$) ⇒ $\frac{(x-5)^2}{25}+\frac{y^2}{16}=1$: a=5, c=3, centre (5,0), focus 5−3=2, directrix $x=5-\frac{a^2}c=-\frac{10}3$.
  - "Distance to F(4,0) is 1 less than distance to x+7=0" ⇒ PF = distance to x=−6 ⇒ $y^2=20(x+1)$.
- **Tangent lines** (資優38): substitute and set the discriminant to 0, or use the "half-substitution" rule at a point $(x_0,y_0)$: $x^2\to x_0x$, $y^2\to y_0y$, $x\to\frac{x+x_0}2$.
  - Tangents of slope m: $y=mx\pm\sqrt{a^2m^2+b^2}$ for the ellipse; $y=mx\pm\sqrt{a^2m^2-b^2}$ for the hyperbola; $y=mx+\frac cm$ for $y^2=4cx$.
- **Optical properties**:
  - Parabola: rays parallel to the axis reflect through the focus (headlamps, dishes).
  - Hyperbola: the tangent bisects $\angle F_1PF_2$.

**Traps**: in 數A only quadratic-function parabolas count. For an ellipse $a^2=b^2+c^2$; for a hyperbola $c^2=a^2+b^2$. The 正焦弦 is $\frac{2b^2}a$ for both. A product of factors set to zero can describe lines rather than a conic.

---

## 24. 隨機變數、二項分布、常態分布、抽樣與信賴區間 [超出數A]

**Scope**:
- [超出數A]. 隨機變數, 變異數, 二項分布, 常態分布 and 信賴區間 are 12年級數甲 or 數B content (scope.md §8).
- 數A keeps only the 期望值 of simple games (§11) and independent repeated trials (§21).
- The old 學測 items below (2002–2010) used these tools.

**Sources**: 99數甲上 1-1隨機的意義, 1-2二項分布, 1-3抽樣與統計推論; 資優 第48單元信心水準的解讀, 第49單元二項分配.

### 24.1 隨機變數、期望值、變異數
- **隨機變數**: a real-valued function on the sample space. 離散型 takes finitely or countably many values; 連續型 takes values in an interval (e.g. lifetime).
  - The 機率分布 (機率質量函數) satisfies $f(x_i)=P(X=x_i)\ge0$ and $\sum f=1$.
- **Mean and variance**:
  - $E(X)=\sum x_ip_i$.
  - $\mathrm{Var}(X)=E[(X-\mu)^2]=E(X^2)-\mu^2$, and $\sigma_X=\sqrt{\mathrm{Var}X}$ measures spread: a smaller Var means values cluster near μ.
- **Linearity**:
  - $E(aX+b)=aE(X)+b$, $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$, $\sigma_{aX+b}=|a|\sigma_X$.
  - $E(X^2)\ne[E(X)]^2$ in general.
  - $E(X+Y)=E(X)+E(Y)$ always. If X and Y are independent, also $E(XY)=E(X)E(Y)$ and $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$.
  - Example: 10 dice ⇒ E(sum) = 35.
  - Example: $E(-2X+10)=54$ and $\mathrm{Var}(-2X+10)=196$ ⇒ $E(X)=-22$, $\mathrm{Var}(X)=49$.
  - Example: $Y=\frac23X+10$ with E(X)=6 and Var(X)=0.9 ⇒ E(Y)=14, Var(Y)=0.4.
  - Example: prize mean 250, SD 120, under a linear change Y=1.2X+150 ⇒ mean 450 and SD 144.
- **Special distributions**:
  - 均勻 on 1..n: $E=\frac{n+1}2$, $\mathrm{Var}=\frac{n^2-1}{12}$.
  - 白努利 with parameter p: E = p, Var = p(1−p).
  - **超幾何** (n draws without replacement from N with r special): $E=n\frac rN$.
    - 12 balls with 3 white, draw 3 ⇒ $\frac34$.
    - 9 items with 2 defective, draw 3 ⇒ $\frac23$.
    - 100 bulbs with 5 bad, draw 10 ⇒ $\frac12$.
    - 4W 2R, draw 3 ⇒ E = 2 white, Var = $\frac25$.
    - 3R 4W, draw 3 ⇒ $E=\frac97$, $\mathrm{Var}=\frac{24}{49}$.
  - A die weighted proportionally to its face value ⇒ $E=\frac{91}{21}=\frac{13}3$.
  - Ball k appears k² times ⇒ $E(X)=\frac{3n(n+1)}{2(2n+1)}$.
- **Exam items**:
  - **2009學測**: 2 blue (2000元), 5 red (1000元) and n others, with E=300 ⇒ $\frac{9000}{7+n}=300$ ⇒ **n=23**.
  - **2013指定甲**: two of balls 1–8, X = the smaller number ⇒ $p_k=\frac{8-k}{28}$ ⇒ $p_k>\frac15$ for k=1, 2 only. Option (2).
  - **2014指定甲**: best-of-5 series, E(games) $f(p)=6p^4-12p^3+3p^2+3p+3$.
    - (1) $P(3\text{ games})=p^3+(1-p)^3$ ✓.
    - f(p) is of degree 4 ✗.
    - (3) Constant term 3 ✓.
    - (4) f is symmetric and maximal at $p=\frac12$ ✓.
    - $f(\frac14)>f(\frac45)$ ✗.
    - Ans (1)(3)(4).
  - **2016指定甲**: a spinner with P(same region) = ¼ and P(switch) = ¾, three spins from region 1 ⇒ E(sum) $=\frac{3+42+39}{64}=\frac{21}{16}$.
  - **2016指定乙**: an unfair die with P(1)=P(4)=x and others y, E=3 ⇒ $2x+4y=1$, $5x+16y=3$ ⇒ $x=\frac13$, $y=\frac1{12}$; P(sum 3 in two rolls) $=2xy=\frac1{18}$.
  - **2017指定甲**: knockout bracket ⇒ E(孝班 prize) = 880元.
  - **2018指定乙**: red envelopes drawn by 甲乙丙 ⇒ key 750 = 3 × 250, the mean of {100, 200, 300, 400}. (The handout's stem lists only 100/200/400, which would force a total of 700; the original item has four envelopes.)
  - **2019指定乙**: win 36元 if the sum is 6 or at least one die shows 6 ⇒ $\frac{5+11}{36}\cdot36=16$.
  - Points problem (first to 3, stopped at 2:0) ⇒ 甲 $\frac78$ of 5600 = 4900, 乙 700.
- **Pooled blood testing**: groups of k, each person positive w.p. p.
  - $E(\text{tests per group})=1\cdot(1-p)^k+(k+1)[1-(1-p)^k]$, so per person $1-(1-p)^k+\frac1k$.
  - For p=0.1 the best k is 4; it stops helping at k≥34.
  - 106 研究試題: k=10, p=0.01 ⇒ P(11 tests) $=1-0.99^{10}$, option (4).

### 24.2 二項分布
- **Bernoulli trials** (independent, same p): $X\sim B(n,p)$ with $P(X=k)=C^n_kp^k(1-p)^{n-k}$. These sum to 1 by the binomial theorem.
  - The 3rd success on exactly the 5th trial: $C^4_2p^2(1-p)^2\cdot p$.
- **Moments and shape**: $E(X)=np$, $\mathrm{Var}(X)=np(1-p)$.
  - The pmf is unimodal with mode near (n+1)p.
  - It is symmetric if p=½, right-skewed if p<½, left-skewed if p>½.
- **Without replacement from a huge population** (n ≪ N) ≈ B(n, r/N), so polls are modelled as binomial.
- **Examples**:
  - 20 coin tosses ⇒ E=10, σ=√5≈2.2.
  - Two coins tossed 300 times, X = double heads ⇒ E=75, σ=15.
  - Shooter 0.6 with 150 shots ⇒ E=90, Var=36, rough 95% range [78, 102].
  - B(20, 0.4): E=8 ✓, σ=√4.8>2, mode 8 ✓, P(7)≠P(9), right-skewed ✓.
  - 10 coins: $p_4=p_6$, the maximum is $p_5$, and the average of $p_0..p_{10}$ is $\frac1{11}$.
  - Recessive trait (rd×rd ⇒ P(rr) = ¼), 4 children, exactly one without the trait ⇒ $C^4_1\frac14(\frac34)^3=\frac{27}{64}$.
  - Mean 12, variance 7.2 ⇒ p=0.4, n=30.
  - Walk +3 on heads, −2 on tails, 12 tosses, end at −4 ⇒ 4 heads ⇒ $C^{12}_4/2^{12}$.
  - A 4-engine plane is safer than a 2-engine plane (needs half working) ⇔ $p<\frac13$.
- **Exam items**:
  - **2018指定甲**: errors per inning ~ B(9, p) with $p_4+p_5=\frac{45}8p_6$ ⇒ $15p^2+4p-4=0$ ⇒ $p=\frac25$ ⇒ $E=\frac{18}5$.
  - **2009指定甲**: prizes 1, 2, 3, … for successive heads.
    - (1) k heads give a total of $\frac{k(k+1)}2$, not $\frac{k^2-k}2$ ✗.
    - (2) After 2 tosses, P(total 1) $=2p(1-p)$ ✓.
    - (3) A total of 2 is impossible, since totals are triangular numbers ✗.
    - (4) A total of $\frac{n^2-n}2$ ⇔ exactly n−1 heads ⇒ $n(p^{n-1}-p^n)$ ✓.
    - Ans (2)(4).
  - 8 coin tosses: P(4H4T) $=\frac{70}{256}>\frac14$; alternating patterns (2/70) are equally likely as front-loaded ones (2/70).

### 24.3 常態分布與經驗法則
- **Normal curve** (Gauss, de Moivre): bell-shaped and symmetric, with mean = median. $Z=\frac{X-\mu}\sigma$ has mean 0 and SD 1.
- **68–95–99.7 rule**: P(|X−μ|≤σ) ≈ 68%, ≤2σ ≈ 95%, ≤3σ ≈ 99.7%.
  - So beyond +1σ is about 16%, and beyond +2σ about 2.5%.
- **中央極限定理**: the standardised sample mean (or proportion) is ≈ N(0,1) for large n, whatever the population shape.
- **Exam items**:
  - **2002學測**: μ=65.24, σ=5.24 ⇒ 60 = μ−σ ⇒ about 16% of 1000 ⇒ **160** (B).
  - **2010指定乙**: μ=70, σ=10 ⇒ P(<60) ≈ 0.16, option (1).
  - **2009指定乙**: IQ N(100, 15), 300000 students, cut-off 130 = +2σ (about 2.5%, not 5%).
    - About 15萬 have IQ ≥100 ✓; 68% ⇒ 20.4萬 lie in 85–115 ✓; 25 per 1000 ✓.
    - A school with 14 students may still have one.
    - Ans (2)(3)(4).
  - **2006學測**: weights of 100 women (mean 55, SD 12.5) vs the normal curve N. In N, ≥55 is 50% and ≥80 is 2.5%. In the skewed sample, the 第一四分位數 > 45 and the overweight share ≥5%. Ans (1)(2)(4)(5).
  - School of 1000, mean 70, SD 10: about 160 fail, about 25 above 90, a score of 80 ranks about 160th, and z-scores have mean 0 and SD 1.
  - SAT N(560, 120), capped at 800 = +2σ ⇒ 2.5% receive 800.
  - Spec 300±20 where 20 = 2σ ⇒ about 5% out of spec.

### 24.4 抽樣方法與信賴區間
- **Sampling**:
  - 便利抽樣 (non-probability, biased).
  - 簡單隨機抽樣 (equal chance; by 母體清冊 plus a 亂數表 or computer).
  - 分層隨機抽樣 (stratify, allocate proportionally, then simple-random within each stratum; reduces imbalance).
  - **2011指定乙**: 50 of 100 by four schemes. Each person has equal chance ½ in schemes 1, 3, 4; scheme 2 gives $\frac{32}{60}$ vs $\frac{18}{40}$. Ans (1)(3)(4).
  - **2008學科**: simple random sampling of 80 from 800 gives everyone probability $\frac1{10}$, regardless of sex. Ans (4)(5).
  - **亂數表**: digits are random, so rows need not contain equal counts. P(a given triple = 000) ≈ $\frac1{1000}$, and "0000" can occur.
  - **2014指定乙**: P(both H | at least one H) $=\frac13$ ✓; P(all six faces in 6 dice) $=\frac{6!}{6^6}$ is small ✓; two red cards $=\frac{25}{102}<\frac14$. Ans (3)(4).
- **Sample proportion**: $\hat p=\frac Xn$ with $E(\hat p)=p$ and $\sigma_{\hat p}=\sqrt{\frac{p(1-p)}n}$.
  - **95% 信賴區間**: $\left[\hat p-2\sqrt{\frac{\hat p(1-\hat p)}n},\ \hat p+2\sqrt{\frac{\hat p(1-\hat p)}n}\right]$.
  - Use 1× for 68% and 3× for 99.7%. The half-width is the 抽樣誤差 (最大誤差).
- **Interpretation**: "95% 信心水準" means that **if the sampling were repeated many times, about 95% of the intervals would cover the true p**.
  - It is **not** "p lies in this interval with probability 95%".
  - Nor is it "95% of future $\hat p$ fall in this interval".
- **Examples**:
  - 642 of 1070 ⇒ $\hat p=0.6$, error ≈ 3% ⇒ [0.57, 0.63].
  - 60 of 100 ⇒ error ≈ 9.8% ⇒ [0.502, 0.698].
  - 20 of 50 ⇒ [0.261, 0.539].
  - Defect 8% of 400 ⇒ 95% [0.0529, 0.1071]; 99.7% [0.0393, 0.1207]; 68% [0.0664, 0.0936].
  - 32 coin tosses with 19 heads ⇒ 95% CI [0.420, 0.767]. Repeating 100 times, 93 of the intervals covered 0.5, close to 95%.
- **Reverse problems**:
  - CI [0.608, 0.672] ⇒ $\hat p=0.64$, e=0.032 ⇒ n=900, 576 heard of it.
  - CI [0.37, 0.43] ⇒ $\hat p=0.4$, e=0.03 ⇒ n≈1067 (about 427 heads).
  - CI [0.55, 0.65] ⇒ n≈384, about 230 myopic.
  - $\hat p=0.6$: e=4% ⇒ n=600; e=2% ⇒ n=2400.
  - $\hat p=0.36$, n=576 ⇒ SE = 0.02, so a 2-point error corresponds to 68%.
- **Sample size**: $n=\frac{4\hat p(1-\hat p)}{e^2}$. Conservatively ($\hat p=\frac12$), $n\approx\frac1{e^2}$.
  - With 1.96: $n\approx\left(\frac{0.98}e\right)^2$, so e=3% ⇒ about 1068 (the standard poll size).
  - Quadrupling n halves the error, other things equal.
- **Exam items**:
  - **2009學測**: CIs [0.50, 0.58] (甲) and [0.08, 0.16] (乙).
    - (1) The sample proportion 0.54 ✓.
    - (2) $n=\frac{4\hat p(1-\hat p)}{e^2}$ is about 621 for 甲 vs 264 for 乙 ⇒ fewer sampled in 乙 ✓.
    - (3) and (4) misread the confidence level ✗.
    - (5) Re-polling with 4n changes $\hat p$, so the width need not exactly halve ✗.
    - Ans (1)(2).
  - **2010學測**: by sex, the women's $\hat p=0.52$ with SE 0.02 ⇒ [0.48, 0.56] ✓.
    - The men's SE 0.04 ⇒ fewer men sampled.
    - The pooled $\hat p$ lies between 0.52 and 0.59 ✓.
    - The sample cannot prove men > women in the population.
    - Ans (2)(4).

**Traps**: $\mathrm{Var}(aX+b)=a^2\mathrm{Var}X$; binomial needs independence and the same p; the confidence level describes the method, not one interval; the 68–95–99.7 rule applies to normal data only; quadrupling n halves the error.

---

## 25. 函數概念、數列極限、無窮級數、函數極限 [超出數A]

**Scope**:
- [超出數A]. Limits and infinite series are 12年級數甲 (scope.md §8).
- In 數A, the infinite geometric series is not tested; only finite 等比級數 (§8) is.
- The function vocabulary (定義域, 值域, 合成, Gauss [x], piecewise tax/fare functions) is background for §7/§15.

**Sources**: 99數甲下 1-1數列與極限, 1-2函數的概念, 1-3函數的極限; 資優 第6單元極限與無窮級數, 第55單元函數的極限, 第59單元數列極限 (the folder also contains an identical duplicate file 第59單元數列極限(1)).

### 25.1 函數概念 (99數甲下1-2)
- **Function**: each x in the 定義域 maps to exactly one y. Representations are tables, graphs, formulas and words.
  - Two functions are equal ⇔ they have the same domain and the same rule.
- **Gauss function [x]** (the largest integer ≤ x) gives step graphs: taxi fares, postage, call charges.
  - **2011指定甲**: $C(t)=5-2[1-2t]$.
    - C(10)=5+38=43 ✓.
    - $[1-2t]=-[2t-1]$ fails for non-integer 2t ✗.
    - $\lim_{t\to10.5}C$ does not exist (45 from the left, 47 from the right) ✗.
    - $\lim_{t\to11.2}C=5-2(-22)=49$ ✓.
    - Ans (1)(4).
- **Piecewise linear tax** (綜合所得稅 brackets): continuous, but the slope changes at the bracket edges.
- **Operations and composition**:
  - The domain of f±g, fg is $D_f\cap D_g$; for $\frac fg$, also remove the zeros of g.
  - $f(x)=\sqrt{9-x^2}$-type examples restrict the domain.
  - $(f\circ g)(x)=f(g(x))$, and in general $f\circ g\ne g\circ f$.
  - Decompose: $(x+3)^4=f(g(x))$ with g=x+3, f=y⁴; $|x^2-2|$ with g=x²−2, f=|y|.
- **Graph transforms**: $y=f(x-h)+k$ is a translation, $y=af(x)$ a vertical stretch, $y=f(-x)$ a reflection in the y-axis. Implicit and rational/radical functions are named.

### 25.2 數列極限
- **Convergence**: $\lim a_n=\alpha$ when $|a_n-\alpha|$ eventually stays as small as we like. Otherwise $\langle a_n\rangle$ is 發散 (including →∞ and oscillation like $(-1)^n$).
- **Geometric**: $\langle r^n\rangle$ converges ⇔ −1<r≤1 (limit 0 for |r|<1, 1 for r=1).
- **Arithmetic of limits**: sums, differences, products and quotients (non-zero denominator) of convergent sequences converge to the corresponding results.
  - Convergent + divergent is divergent. Products or quotients of a convergent and a divergent sequence, and any combination of two divergent ones, may go either way.
- **Standard limits**:
  - $\frac{\text{poly}}{\text{poly}}$: compare degrees.
  - $\sqrt{n^2+n}-n\to\frac12$ (rationalise).
  - $\frac{a^n}{b^n}$: divide by the largest base.
  - **夾擠定理** (squeeze).
  - A recursive sequence that is monotone and bounded converges; find the limit from the fixed point.
- **Exam items**:
  - **2015指定乙**: lattice points with x, y ≥1 and x+2y ≤ 2n ≈ the area n² ⇒ $\lim\frac{a_n}{n^2}=1$, option (2).
  - **2019指定甲**: $a_n<b_n^2<a_{n+1}$ with $a_n\to4$ ⇒ $a_n$ increases to 4, so all $a_n<4$; $b_n^2$ is increasing and $\to4$; $b_n$ itself may oscillate between ±2. Ans (3)(4).
  - **2017指定乙**: $a_n=(\frac12)^{n-1}$ ⇒ $-a_n$, $a_n^2$, $\sqrt{a_n}$ converge; $\frac1{a_n}$ and $\log a_n$ diverge. Ans (1)(2)(3).
  - **2016指定甲**: A starts at 0 with steps 1, ½, ¼, …; B starts at 8 with steps −4, −4/3, ….
    - $c_n=2-(\frac12)^n+3(\frac13)^n$ ⇒ $c_1=\frac52$ ✓, $c_2<c_1$, the differences are not geometric, $\lim c_n=2$ ✓, $c_{1000}<2$.
    - Ans (1)(4).
  - **2002指定甲**: isosceles triangle (0,2), (±1/n, 0) ⇒ the circumdiameter $D_n=2(1+\frac1{4n^2})\to2$. With apex (0,1): $D_n=\frac{n^2+1}{n^2}\to1$.
  - **2003指定甲**: $A_n$ = the intersection of $\frac{x^2}{n^2}+y^2\le1$ and $x^2+\frac{y^2}{n^2}\le1$. It contains the unit disc and lies in $[-1,1]^2$ ⇒ π < area < 4, perimeter > 5, and area → 4. Ans (1)(2)(3)(4).
  - **2004指定甲**: positive roots of tan x = x lie near $(k+\frac12)\pi$ ⇒ $x_{n+1}-x_n\to\pi\approx3.14$.
  - **2005指定甲**: upper branch of $y^2-x^2=1$; the distance from $(n,\sqrt{n^2+1})$ to y=x is $\frac{\sqrt{n^2+1}-n}{\sqrt2}$ ⇒ $n d_n\to\frac1{2\sqrt2}\approx0.35$.
  - **2010指定甲**: $x+y+z=0$, $x+2y+3z=0$, $-2nx+ny+3z=8n$ ⇒ (x,y,z)=t(1,−2,1) with $t=\frac{8n}{3-4n}$ ⇒ $a_n\to-2$.
  - **2014指定甲**: the remainder of $2(x+1)^n\div(3x-2)^n$ has constant term $r_n=2-2(-\frac23)^n\to2$, option (3).
  - **2017指定甲**: lattice points in the triangle under $y=-\frac x{2n}+3$ (axes included) $=(6n+1)+(4n+1)+(2n+1)+1=12n+4$ ⇒ $\frac{a_n}n\to12$.
  - **2015指定甲**: 1 red (2n points), 2 blue (n), n−3 white (1); draw 3 ⇒ $E_n=3\cdot\frac{2n+2n+(n-3)}n\to15$.
  - $\lim(\frac{5n-1}{3n+2}-a_n)=7$ with $a_n$ convergent ⇒ $\lim a_n=\frac53-7=-\frac{16}3$.
  - $a_n=a_{n-1}a_{n-2}\bmod5$ is bounded ⇒ $\frac{a_n}{10^n}\to0$.

### 25.3 無窮級數
- **Definition**: $\sum a_n$ = the limit of the partial sums $S_n$ when it exists (收斂級數); otherwise the series is 發散.
  - $\sum a_n$ converges ⇒ $a_n\to0$; the converse fails.
- **無窮等比級數**: $\sum ar^{n-1}=\frac a{1-r}$ ⇔ |r|<1 (or a=0).
  - Repeating decimals: $0.\overline{763}=\frac{763}{999}$.
  - $1+(1-3x)+(1-3x)^2+\cdots$ converges ⇔ $0<x<\frac23$.
  - **87學科**: $\frac a2+\frac b4+\frac a8+\frac b{16}+\cdots=\frac{2a}3+\frac b3=3$ ⇒ 2a+b=9.
  - Nested midpoint triangles form a geometric series with area ratio ¼.
  - **Telescoping**: $\sum\frac1{1+2+\cdots+k}=\sum\frac2{k(k+1)}\to2$.
- **2018指定乙**: $a_n=(-1)^n$ diverges; $b_n=a_n+a_{n+1}=0$ converges; $c_n=(-\frac{\sqrt{10}}3)^n$ with |r|>1 diverges, and so does $d_n=\frac13c_n$; $e_n=\frac1{c_n}$ with |r|<1 converges. Ans (2)(5).
- Termwise: if $\sum a_n$ and $\sum b_n$ converge, $\sum(\alpha a_n+\beta b_n)$ converges to the matching combination.

### 25.4 函數極限
- **One-sided limits**: $\lim_{x\to a}f$ exists ⇔ both one-sided limits exist and are equal.
  - $\frac{|x-2|}{x-2}$ has one-sided limits ±1, so no limit at 2.
  - Step functions jump at integers.
- **0/0 forms**: factor, cancel, or rationalise.
  - $\lim_{x\to2}\frac{2x^2+ax+b}{x^2-x-2}=\frac53$ ⇒ the numerator vanishes at 2 ($8+2a+b=0$). After cancelling (x−2): $\frac{2x+(a+4)}{x+1}\to\frac{8+a}3=\frac53$ ⇒ a=−3, b=−2.
  - $\lim_{x\to1}\frac{m\sqrt{x+1}-2}{x-1}=k$ ⇒ the numerator must vanish at 1: $m\sqrt2=2$ ⇒ $m=\sqrt2$. Rationalising gives $k=\frac{\sqrt2}{2\sqrt2}=\frac12$.
- **2007指考甲**: near x=1, $3-3x-x^2<0$, so $|3-3x-x^2|-1=x^2+3x-4$ ⇒ the limit is $\lim(x+4)=5$, option (4).
- **2018指定甲**: if $\lim_{x\to0}f(x)\frac{|x|}x$ exists, then $\lim(\frac{|x|}x)^2=1$, $\lim f(x)\frac x{|x|}$ (the same thing) and $\lim f(x)^2$ exist; $\lim f$ and $\lim(f+1)\frac x{|x|}$ need not. Ans (1)(2)(5).
- **Gauss function limits**:
  - $\lim_{x\to0^+}\frac{[x]}x=0$.
  - $\lim_{x\to0^-}\frac{|x|}x=-1$.
  - $\lim_{x\to0}x^2[x]=0$.
  - $\lim_{x\to2}\frac{[x]}x$ does not exist.
- **Continuity** (資優55): f is continuous at a if $\lim_{x\to a}f(x)=f(a)$.
  - Polynomials are continuous, and so are rational functions on their domains.
  - **勘根定理/中間值定理** (§7 uses the polynomial version).

**Traps**: a limit is about the approach, not the value at the point; one-sided limits must agree; a convergent geometric series needs |r|<1; $a_n\to0$ does not imply that $\sum a_n$ converges.

---

## 26. 微分與應用 [超出數A]

**Scope**:
- [超出數A]. Derivatives are 12年級數甲 (scope.md §8).
- What 數A keeps without calculus: 三次函數的圖形特徵 (F-10-2), meaning the 對稱中心 (point symmetry), end behaviour from the leading term, and the local linear approximation near a point (§7). Several items below (2007指定甲 (4), the cubic shape facts) are answerable that way.

**Sources**: 99數甲下 2-1微分, 2-2函數性質的判斷(一), 2-3函數性質的判斷(二); 資優 第56單元函數的微分, 第57–58單元微分的應用.

### 26.1 導數與切線
- **Definition**: $f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h$, the slope of the tangent and the instantaneous rate of change (velocity, flow rate).
  - Differentiable ⇒ continuous. Corners like |x| at 0 and jumps are not differentiable.
- **Rules**:
  - $(x^n)'=nx^{n-1}$, together with linearity.
  - Product $(fg)'=f'g+fg'$; quotient; chain $(f(g(x)))'=f'(g(x))g'(x)$, e.g. $((ax+b)^n)'=na(ax+b)^{n-1}$.
- **Tangent lines**:
  - At $(a,f(a))$: $y-f(a)=f'(a)(x-a)$.
  - From an external point P: write the tangent at t, substitute P, and solve for t. Example: P(1,2) to $y=x^2+x+1$ gives t=0, 2, i.e. y=x+1 and y−7=5(x−2).
  - Given slopes 2 and −4 on $y=x^2+2x-7$ ⇒ the tangents meet at $P(-\frac32,-10)$.
  - Steepest tangent of $y=-x^3+3x^2$: the slope $-3x^2+6x$ is maximal at x=1 ⇒ y−2=3(x−1).
- **Interpolation with slopes**:
  - **2008指考甲**: cubic p through (1,3) and (−1,5) with p′(1)=7, p′(−1)=−5 ⇒ $p=x^3+3x^2-2x+1$.
  - $f=x^3+ax^2+b$ through (1,4) with slope −3 ⇒ a=−3, b=6. Then f has a local max f(0)=6 and a local min f(2)=2.
  - **2010指定甲**: $f''=8x+11$ and f′(1)=0 ⇒ $f'=4x^2+11x-15$ ⇒ f′(0)=−15.
- **Double roots**: α is a double root ⇔ f(α)=f′(α)=0 ≠ f″(α); a triple root also has f″(α)=0 (a tangent that is also an inflection).

### 26.2 單調、極值、凹凸、反曲點
- **Monotonicity and extrema**:
  - f′>0 ⇒ increasing; f′<0 ⇒ decreasing.
  - A local extremum at an interior point where f′ changes sign. Second-derivative test: f′=0 with f″<0 is a maximum, with f″>0 a minimum.
  - Global extrema on [a,b]: compare the critical values with the endpoint values.
- **Concavity**: f″>0 is 凹口向上, f″<0 is 凹口向下; a 反曲點 is where f″ changes sign.
  - A cubic has exactly one inflection point, at $x=-\frac b{3a}$, and the graph is point-symmetric about it.
- **Cubic shapes**: $f'=3ax^2+2bx+c$.
  - $b^2-3ac>0$ gives two extrema; ≤0 gives a monotone cubic.
  - The number of real roots follows from the signs of the extreme values (both same sign ⇒ 1 root; one is 0 ⇒ a double root; opposite signs ⇒ 3 roots).
  - f(x)=k has as many solutions as the line y=k meets the graph.
- **Exam items**:
  - **2007指定甲**: $y=x^3+2x+3$.
    - $y'=3x^2+2>0$ ⇒ no highest or lowest point and no horizontal tangent.
    - Every horizontal line meets it once ✓.
    - It is symmetric about (0,3): (a,b) on the graph ⇒ (−a, −b+6) on it ✓.
    - $\int_0^1=\frac14+1+3=4.25>4$ ✓.
    - Ans (3)(4)(5).
  - **2005指定甲**: $f=(1-a)x^2+a$.
    - a=1 makes f a constant (a line) ✗.
    - Any extremum is f(0)=a ✓.
    - 0 can never be a maximum ✗.
    - a≠0 ⇒ no repeated root ✓.
    - Ans (B)(D).
  - **2009指定甲**: quartic with inflection points at x=±1, slopes 1 and −1 there, through (±1, 2).
    - $f''=k(x^2-1)$ ⇒ $f'=\frac12x^3-\frac32x$ (odd, constant term 0) and $f=\frac{x^4}8-\frac34x^2+\frac{21}8$.
    - Ans (1)(3).
  - **2010指定甲**: an increasing cubic with an inflection point at x=5 ⇒ $f'=(x-5)^2+1$, option (2).
  - **2018指定甲**: $f=-x^3-3x^2+3$ has a local min f(−2)=−1 and a local max f(0)=3.
    - Roots $a_1\in(-3,-2)$, $a_2\in(-2,-1)$, $a_3\in(0,1)$.
    - f(x)=a₁ and f(x)=a₂ each have 1 solution (both are below −1); f(x)=a₃ has 3.
    - ⇒ f(f(x))=0 has **5** real roots.
  - **2008指定甲**: f′ is an upward parabola through (1,0) and (2,0) ⇒ f is a cubic with exactly two extrema, decreasing on (1,2). Ans (1)(3).
  - **2012指定甲**: sign patterns of f′ and f″ ⇒ the minimum is at x=4 ✓; f′(2)<f′(3) (f′ increases on (1,4)); there are two inflection points (0 and 1), so n≥4; the leading coefficient is positive ✓. Ans (2)(5).
  - **2017指定甲**: a cubic (leading coefficient >0) tangent to a line at x=1 with only one common point ⇒ $f-g=a(x-1)^3$ ⇒ f(1)=g(1), f′(1)=g′(1), f″(1)=0. No other a has f′(a)=g′(a) or f″(a)=g″(a). Ans (1)(2)(3).
  - **2019指定甲**: cubic $ax^3+bx^2+cx+2$ shown on [−2,1], concave up with a minimum just left of 0.
    - The slope at 0 is >0 ⇒ c>0. f″(0)=2b>0 ⇒ b>0. The sign of a cannot be read.
    - Both extreme values are positive ⇒ exactly one real root; the inflection point's y is positive.
    - Ans (2)(3)(5).
  - **2003指定甲**: a monic cubic whose f(x)=k has 3 roots exactly for 0<k<4 ⇒ local max 4 and local min 0.
    - f−4 and f′ share a root ✓; f and f′ share a root ✓.
    - The root of f+5=0 lies left of all roots of f−2=0 ✓.
    - Ans (1)(2)(4).
  - **2004指定甲**: an integer polynomial vanishing only at 2, 4, 6 and positive elsewhere ⇒ each root has even multiplicity ⇒ degree ≥6 and even, and f′(4)=0. f(1) need not be odd (e.g. a factor 2). Ans (A)(D). (The 99 key lists "(3)(4)(5)", which does not match the A–D options.)
  - $f=ax^3-3ax^2-9ax+b$ (a>0) with local max 10 and local min −22 ⇒ critical points −1, 3 ⇒ 5a+b=10, −27a+b=−22 ⇒ (a,b)=(1,5).
- **Optimisation**:
  - **2006指定甲**: A(4,3), B(x,0) ⇒ max of $\frac x{AB}=\frac x{\sqrt{x^2-8x+25}}$ ⇒ $\frac{x^2}{AB^2}$ has its reciprocal $25u^2-8u+1$ minimal at $u=\frac4{25}$ ⇒ the maximum is $\frac53$.
  - $f=\frac{3x}{x^2+3x+4}$ on [−3,3] ⇒ f′=0 at ±2 ⇒ max $f(2)=\frac37$, min f(−2)=−3.
  - Box or volume problems give a cubic in one variable (e.g. max volume 72 at height 3).
  - $x^4-2x^3+2x\ge-\frac{11}{16}$ (minimum by f′).
  - P(exactly one rainy day in 3) $Q=3p(1-p)^2$ is maximal at $p=\frac13$, where $Q=\frac49$.
- **Newton's method** (enrichment): $a_{n+1}=a_n-\frac{f(a_n)}{f'(a_n)}$ (tangent-line iteration); the choice of starting point matters.
- **資優56–57 extras**:
  - 隱函數微分: differentiate both sides, e.g. $x^2+y^2=r^2$ ⇒ $y'=-\frac xy$.
  - 參數式微分: $\frac{dy}{dx}=\frac{dy/dt}{dx/dt}$.
  - 高階導數.
  - Non-differentiable points: 斷點, 尖點 and jumps.
  - Asymptotes of rational functions: vertical where the denominator is 0, horizontal or oblique by long division (e.g. $f(x)=ax+b+\frac{c}{x-d}$).
  - Curve-sketching checklist: domain, intercepts, symmetry, f′ table, f″ table, asymptotes.

**Traps**: f′(a)=0 does not by itself give an extremum (x³ at 0); global extrema need the endpoints; the inflection point is where f″ **changes sign**; for cubics, use the 對稱中心 $x=-\frac b{3a}$ (the in-scope idea for 數A).

---

## 27. 積分與應用（附：指對數函數的微積分） [超出數A]

**Scope**:
- [超出數A]. 12年級數甲 content.
- e and ln are 數B (F-11B-2) for the 連續複利 idea only. Calculus of $e^x$ and $\ln x$ is 數甲.

**Sources**: 99數甲下 2-4積分, 2-5積分的應用; 資優 第60單元黎曼和與面積, 第61單元定積分與不定積分, 第62單元定積分的應用, 第63單元指對數函數的微積分.

### 27.1 黎曼和與定積分
- **黎曼和**: split [a,b] into n parts, take $\sum f(t_i)\Delta x$, and let n→∞ to get $\int_a^bf(x)\,dx$, the signed area. The sum formulas $\sum k$, $\sum k^2$, $\sum k^3$ from §8 are what make these computable.
  - Example: $\int_0^3(4-x^2)dx=12-9=3$ via the right-endpoint sums with $\Delta x=\frac3n$.
  - Upper and lower sums: for a decreasing f, the left sum > integral > right sum.
- **2018指定甲**: $f=-x^2+499$ on [0,10] (decreasing, concave down).
  - A = ∫ is the area ✓.
  - B (left sum) > A > C (right sum).
  - The trapezoid sum $D=\frac{B+C}2$ < A (concave) and C < D ✓.
  - Ans (1)(4).
- **Properties**:
  - $\int_a^b(\alpha f+\beta g)=\alpha\int f+\beta\int g$.
  - $\int_a^b=\int_a^c+\int_c^b$, and $\int_a^b=-\int_b^a$.
  - Odd f: $\int_{-a}^af=0$; even f: twice $\int_0^a$.
  - Inequalities: f ≤ g ⇒ ∫f ≤ ∫g.
  - Not every elementary function has an elementary antiderivative (e.g. the Fresnel $\int\sin\frac{\pi t^2}2dt$), so the definition via Riemann sums still matters.

### 27.2 微積分基本定理
- **Statement**: if F′=f, then $\int_a^bf=F(b)-F(a)$. Also $\frac d{dx}\int_a^xf(t)dt=f(x)$.
  - Indefinite integral: $\int x^ndx=\frac{x^{n+1}}{n+1}+C$; $\int(ax+b)^ndx=\frac{(ax+b)^{n+1}}{a(n+1)}+C$.
- **Exam items**:
  - **2017指定甲**: local max f(1)=3 and tangent slope −5 at x=4 ⇒ $\int_1^4f''=f'(4)-f'(1)=-5-0=-5$, option (1).
  - **2013指定甲**: the area between p(x) and $-1-x^2$ on [1,t] is $t^4+t^3+t^2+t+C$.
    - Setting t=1 gives C=−4.
    - Differentiating gives $p(t)+1+t^2=4t^3+3t^2+2t+1$ ⇒ $p=4x^3+2x^2+2x$.
    - Also $\int_1^t(-1-x^2)dx=-\frac{t^3}3-t+\frac43$.
  - **2019指定甲**: $xf(x)=3x^4-2x^3+x^2+\int_1^xf$.
    - x=1 gives f(1)=2. Differentiating gives $f'=12x^2-6x+2$ ⇒ $f=4x^3-3x^2+2x-1$.
    - Then $\int_0^af=a^4-a^3+a^2-a=1$ has exactly one root a>1 (g(1)<0, g increasing for a≥1).
  - **2012指定甲**: $\frac{f(n)}{n^4}\to5$, $\frac{f(x)}x\to3$ at 0, and f″(0)=2 ⇒ $f=5x^4+bx^3+x^2+3x$.
    - The tangent at 0 is y=3x.
    - $\int_{-1}^1f=2(1+\frac13)=\frac83$ (the odd terms vanish).
  - $f=x(x-1)(x^3-2)$: $\int_0^af'=f(a)=0$ ⇒ a=0, 1, ∛2, so **3** values.

### 27.3 面積
- **Formula**: the area between curves is $\int_a^b|f-g|dx$. Split at the intersection points; for a region bounded in y, integrate in y.
  - $y=x^2$ and $y=4x-x^2$ ⇒ $\int_0^2(4x-2x^2)=\frac83$.
  - $y=x^2$ and $y=-x^2+2x+4$ ⇒ 9.
  - $x^3-2x^2$ and $x-2$ ⇒ $\frac83+\frac5{12}=\frac{37}{12}$.
  - $y=x^3-3x^2+2x$ with the x-axis ⇒ $2\cdot\frac14=\frac12$.
  - **Parabola segment** (Archimedes): the area cut by a chord is $\frac{|a|}6(\beta-\alpha)^3$.
- **2010指定甲**: origin is an inflection point with tangent y=−x ⇒ b=d=0, c=−1 ⇒ $f=ax^3-x$. The area with y=0 is $2\int_0^{1/\sqrt a}(x-ax^3)=\frac1{2a}=2$ ⇒ $a=\frac14$.
- **2011指定甲**: leading coefficient 12, meets y=25 at x=0, 1, 2 ⇒ $f=12x(x-1)(x-2)+25$. The inflection point is (1,25); by point symmetry $\int_0^2f=2\cdot25=50$.

### 27.4 體積與變化量
- **Slicing**: $V=\int_a^bA(x)dx$ (cross-sectional area).
  - A pyramid has $\frac13a^2h$, and a sphere $\frac43\pi r^3$, both by slicing.
  - Part of the unit ball between planes is $\pi\int(1-z^2)dz$.
- **旋轉體**: about the x-axis, $V=\pi\int_a^bf(x)^2dx$ (washers: $\pi\int(R^2-r^2)$).
  - $y=x^2$ on [1,2] ⇒ $\frac{31\pi}5$.
  - $y=x^2$ on [0,1] ⇒ $\frac\pi5$.
  - $y=x+1$ on [0,2] ⇒ $\frac{26\pi}3$.
  - $y=x^2$ for 1≤y≤4, about the y-axis ⇒ $\pi\int_1^4y\,dy=\frac{15\pi}2$.
  - The disc $x^2+(y-3)^2\le4$ about the x-axis (a torus) ⇒ $2\pi\cdot3\cdot4\pi=24\pi^2$.
- **殼層法 (shell method, 資優62)**: rotating the region under y=f(x) about the y-axis gives $V=2\pi\int_a^bx\,f(x)\,dx$. The handout also proves the 酒桶 (barrel) volume formula by integration.
- **Work**: $W=\int_a^bF(x)\,dx$ (spring, pumping).
- **變數變換積分法 (substitution, 資優61)**: e.g. $\int(ax+b)^ndx$, and $\int f(g(x))g'(x)dx=F(g(x))$.
- **Rate → change**: $\int_a^bf'(t)dt=f(b)-f(a)$.
  - Velocity integrates to displacement; |v| to distance.
  - Free fall: $v=v_0+gt$, $s=v_0t+\frac12gt^2$.
  - Flow-rate and memory-rate examples.

### 27.5 [超出] 指對數函數的微積分 (資優63)
- **Derivatives**:
  - $(\ln x)'=\frac1x$, $(e^x)'=e^x$, $(a^x)'=a^x\ln a$, $(\log_ax)'=\frac1{x\ln a}$.
  - $\int\frac1xdx=\ln|x|+C$.
- **Growth and decay**: $y'=ky$ ⇒ $y=y_0e^{kt}$. Continuous compounding $\lim(1+\frac rn)^{nt}=e^{rt}$ is the only part that touches 數B.
- **Techniques**: substitution, integration by parts (enrichment).

**Traps**: area is ∫|f−g|, not the signed integral; take π·f² for volumes of revolution; $\int_a^bf'=f(b)-f(a)$ needs no antiderivative of f; e and ln are not 數A content.
