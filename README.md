# Sequence Alignment: Brute Force vs Greedy vs Dynamic Programming

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/CSC_311-Design_%26_Analysis_of_Algorithms-1f6feb)

Three ways to align two strings, with an honest comparison of what each one costs and how good its answer is. This was built for the **CSC 311 algorithms course at King Saud University**.

```text
GATTACA  →  G-ATTA-CA
GCATGCA  →  GCA-T-GCA        cost = 4  (optimal)
```

## The problem

Given two strings, insert gap characters (`-`) so they have the same length. Then score each column:

| Column | Example | Cost |
|---|---|---|
| Match | `A` over `A` | 0 |
| Mismatch | `A` over `G` | α = 2 |
| Gap | `A` over `-` | β = 1 |

The goal is the alignment with the **lowest total cost**. This is the same problem behind DNA sequence comparison, `diff` tools and spell checkers.

## Three approaches

| Algorithm | Strategy | Time | Optimal? |
|---|---|---|---|
| [**Brute force**](BruteForce.py) | Recursively generates every gapped version of both strings and scores every equal-length pair | Exponential | ✅ Always |
| [**Greedy**](Greedy.py) | Scans left to right. On a mismatch it looks one character ahead to decide which string gets the gap | O(m + n) | ❌ Not always |
| [**Dynamic programming**](DynamicProgramming.py) | Fills a Longest Common Subsequence table, then traces back to build the alignment | O(m · n) | ✅ For this cost model |

### Why the DP uses LCS

Because a mismatch costs exactly two gaps (α = 2β), any mismatch column can be split into two gap columns at the same cost. So an optimal alignment only needs matches and gaps. With *k* matched characters it costs:

```text
cost = (m − k) + (n − k) = m + n − 2k
```

Minimizing the cost means maximizing *k*, which is the **length of the longest common subsequence**. The DP solves the alignment problem by solving LCS.

## Results

| Input | Greedy | Dynamic programming |
|---|---|---|
| `GATTACA` / `GCATGCA` | `G-AT--TACA` / `GCATGC-A--` → **6** | `G-ATTA-CA` / `GCA-T-GCA` → **4** |
| `AGGCTA` / `AGCTTA` | `AGGCT-A` / `AG-CTTA` → **2** | `AGGC-TA` / `A-GCTTA` → **2** |

- **Correctness check:** on 80 random DNA string pairs (up to 3 characters each), the DP cost matched the brute-force optimum every time. Greedy was worse in 2 cases.
- **Why brute force doesn't scale:** aligning two 3-character strings takes about 0.05 s. At 4 characters it takes about 16 s, because the number of gapped strings grows exponentially.

## Run it

```bash
git clone https://github.com/SultanAbdulaziz/CSC311-Project.git
cd CSC311-Project
python Main.py
```

```text
Enter two strings to align:
String 1: ACGT
String 2: AGT
Choose an algorithm to align the strings:
1. Brute Force
2. Greedy
3. Dynamic Programming
4. Exit
3
Dynamic Programming:
ACGT A-GT
1
```

No dependencies beyond the Python standard library.

## Files

```text
├── Main.py                 # Interactive menu
├── BruteForce.py           # Exhaustive search over all gap placements
├── Greedy.py               # One-character look-ahead greedy aligner
└── DynamicProgramming.py   # LCS table + traceback
```

## Team

- [Sultan Aleidan](https://github.com/SultanAbdulaziz): brute force and dynamic programming
- Bader AlRasheed: greedy algorithm and menu
