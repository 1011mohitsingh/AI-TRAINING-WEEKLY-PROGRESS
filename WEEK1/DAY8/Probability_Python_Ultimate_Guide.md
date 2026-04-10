# 🎲 Probability with Python — The Ultimate Reference Guide
### From Mathematical Foundations to Machine Learning Applications

> **Target Audience:** B.Tech CS/AI students · Data Science learners · ML/AI practitioners  
> **Prerequisites:** Basic Python · High-school mathematics  
> **Libraries:** NumPy · SciPy · pandas · Matplotlib · Seaborn  
> **Depth:** Beginner → Advanced with full Python implementations

---

## 📚 Table of Contents

<details>
<summary><strong>Part 1: Foundations of Probability</strong></summary>

1. [Introduction to Probability](#1--introduction-to-probability)
2. [Random Experiments & Sample Space](#2--random-experiments--sample-space)
3. [Basic Probability Rules](#3--basic-probability-rules)

</details>

<details>
<summary><strong>Part 2: Conditional Probability & Bayes Theorem</strong></summary>

4. [Conditional Probability](#4--conditional-probability)
5. [Bayes Theorem](#5--bayes-theorem)

</details>

<details>
<summary><strong>Part 3: Random Variables & Probability Distributions</strong></summary>

6. [Random Variables](#6--random-variables)
7. [Discrete Probability Distributions](#7--discrete-probability-distributions)
8. [Continuous Probability Distributions](#8--continuous-probability-distributions)

</details>

<details>
<summary><strong>Part 4: Simulation & Visualization</strong></summary>

9. [Monte Carlo Simulation](#9--monte-carlo-simulation)
10. [Visualization of Probability](#10--visualization-of-probability)

</details>

<details>
<summary><strong>Part 5: Probability in Statistics & ML</strong></summary>

11. [Expectation & Variance](#11--expectation--variance)
12. [Likelihood & Log-Likelihood](#12--likelihood--log-likelihood)
13. [Probability in Machine Learning](#13--probability-in-machine-learning)

</details>

<details>
<summary><strong>Part 6: Best Practices & Revision</strong></summary>

14. [Common Mistakes](#14--common-mistakes)
15. [Best Practices](#15--best-practices)
16. [Quick Probability Cheat Sheet](#16--quick-probability-cheat-sheet)

</details>

---

## 🛠️ Environment Setup

```python
# ── Install (run once in terminal) ────────────────────────────────────────────
# pip install numpy scipy pandas matplotlib seaborn

# ── Master import block — paste at top of every notebook ─────────────────────
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

from scipy import stats
from scipy.stats import (
    bernoulli, binom, poisson, geom, nbinom,   # discrete
    uniform, norm, expon, gamma, beta,          # continuous
    chi2, t, f                                  # inference
)
from scipy.optimize import minimize
from scipy.special import comb, factorial

# ── Reproducibility & display settings ───────────────────────────────────────
np.random.seed(42)
np.set_printoptions(precision=4, suppress=True, linewidth=100)

plt.rcParams.update({
    'figure.figsize'    : (10, 5),
    'axes.spines.top'   : False,
    'axes.spines.right' : False,
    'axes.titlesize'    : 13,
    'axes.labelsize'    : 11,
    'legend.fontsize'   : 9,
    'font.family'       : 'sans-serif',
})
sns.set_theme(style="whitegrid", palette="muted")

# ── Version check ─────────────────────────────────────────────────────────────
import scipy
print(f"NumPy  : {np.__version__}")
print(f"pandas : {pd.__version__}")
print(f"SciPy  : {scipy.__version__}")
```

---

# ═══════════════════════════════════════════════
# PART 1 · FOUNDATIONS OF PROBABILITY
# ═══════════════════════════════════════════════

---

## 1. 📌 Introduction to Probability

### 1.1 Intuition First

Every day, without realising it, you reason probabilistically:

```
"There's a 70% chance of rain today"       → Should I carry an umbrella?
"There's a 1-in-a-million chance of fraud" → Should the bank block this card?
"This email looks like spam"               → P(spam | words) > 0.9 → block it
```

**Probability** is the mathematical framework for quantifying uncertainty. It gives us a rigorous language to reason about events that haven't happened yet—or events we don't have complete information about.

### 1.2 Formal Definition

For a **sample space** Ω containing all possible outcomes, the probability of event A is:

```
Classical (equally likely outcomes):
    P(A) = |A| / |Ω|   =   (outcomes in A) / (total outcomes)

Frequentist (repeated trials):
    P(A) = lim (n→∞) [ count(A occurs in n trials) / n ]

Axiomatic (Kolmogorov, 1933):
    Axiom 1: P(A) ≥ 0              for all events A
    Axiom 2: P(Ω) = 1              something always happens
    Axiom 3: P(A ∪ B) = P(A)+P(B)  if A ∩ B = ∅ (mutually exclusive)
```

### 1.3 Python — Probability from First Principles

> **Library: NumPy** — fast array math; simulates millions of trials in milliseconds

```python
import numpy as np
np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# CLASSICAL PROBABILITY — counting
# ─────────────────────────────────────────────────────────────────────────────
sample_space = np.arange(1, 7)          # fair die: {1,2,3,4,5,6}
event_even   = sample_space[sample_space % 2 == 0]  # {2,4,6}

p_even_exact = len(event_even) / len(sample_space)
print(f"[Classical] P(even) = {len(event_even)}/{len(sample_space)} = {p_even_exact:.4f}")

# ─────────────────────────────────────────────────────────────────────────────
# FREQUENTIST PROBABILITY — simulation
# ─────────────────────────────────────────────────────────────────────────────
def estimate_probability(n_trials: int, event_fn) -> float:
    """Generic frequentist probability estimator."""
    rolls  = np.random.randint(1, 7, size=n_trials)
    return np.mean(event_fn(rolls))

for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    p_sim = estimate_probability(n, lambda x: x % 2 == 0)
    error = abs(p_sim - p_even_exact)
    print(f"  n={n:>9,}  P(even) ≈ {p_sim:.5f}   error = {error:.5f}")

# ─────────────────────────────────────────────────────────────────────────────
# VISUALISE CONVERGENCE (Law of Large Numbers)
# ─────────────────────────────────────────────────────────────────────────────
import matplotlib.pyplot as plt

n_max  = 50_000
rolls  = np.random.randint(1, 7, size=n_max)
is_even = (rolls % 2 == 0).astype(float)
running_p = np.cumsum(is_even) / np.arange(1, n_max + 1)

plt.figure(figsize=(10, 4))
plt.plot(running_p, color='steelblue', linewidth=1.5, alpha=0.9,
         label='Simulated P(even)')
plt.axhline(0.5, color='red', linestyle='--', linewidth=2,
            label='True P(even) = 0.5')
plt.fill_between(np.arange(n_max),
                 running_p - 0.05, running_p + 0.05,
                 alpha=0.1, color='steelblue')
plt.xscale('log')
plt.xlabel("Number of Trials (log scale)")
plt.ylabel("Estimated Probability")
plt.title("Law of Large Numbers — Convergence to True Probability")
plt.legend()
plt.tight_layout()
plt.show()
```

### 1.4 Role of Probability in AI & ML

```python
import pandas as pd

roles = {
    "Concept"             : [
        "Classification Output",
        "Bayesian Inference",
        "Uncertainty Estimation",
        "Generative Models",
        "Reinforcement Learning",
        "Anomaly Detection",
        "Loss Functions",
        "Regularisation",
    ],
    "Probability Behind It" : [
        "P(class | features) — softmax/sigmoid",
        "P(hypothesis | data) — posterior update",
        "Confidence intervals, dropout at inference",
        "Learn P(data) and sample from it (VAE, GAN)",
        "Policy π(action | state) — stochastic policies",
        "P(observation) low → anomaly",
        "Cross-entropy = −log P(true class | model)",
        "Prior on weights → MAP estimation",
    ],
    "Library Used" : [
        "sklearn, PyTorch", "PyMC, scipy.stats",
        "scipy.stats", "torch.distributions",
        "numpy.random", "scipy.stats",
        "scipy.special", "scipy.stats",
    ]
}
df_roles = pd.DataFrame(roles)
print(df_roles.to_string(index=False))
```

---

## 2. 🎲 Random Experiments & Sample Space

### 2.1 Key Terminology

| Term | Definition | Example |
|------|-----------|---------|
| **Random Experiment** | Process with uncertain outcome | Roll a die |
| **Outcome (ω)** | A single result | Getting a 4 |
| **Sample Space (Ω)** | All possible outcomes | {1,2,3,4,5,6} |
| **Event (A)** | Subset of outcomes we care about | Getting an even number |
| **Certain Event** | Ω itself, always occurs | P(Ω)=1 |
| **Impossible Event** | Empty set ∅, never occurs | P(∅)=0 |
| **Mutually Exclusive** | A ∩ B = ∅ | Getting 1 AND getting 2 |
| **Exhaustive** | A ∪ B = Ω | Getting odd OR even |
| **Independent** | P(A∩B)=P(A)·P(B) | Two separate coin flips |

### 2.2 Simulating Experiments with NumPy

> **Library: NumPy** — `np.random` provides the full toolkit for random simulation

```python
import numpy as np
import pandas as pd
np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# EXPERIMENT 1: Single Fair Die
# ─────────────────────────────────────────────────────────────────────────────
n = 100_000
die = np.random.randint(1, 7, size=n)

print("=== Single Die ===")
print(f"Sample Space : {{1, 2, 3, 4, 5, 6}}")
print(f"P(4)         = {np.mean(die == 4):.4f}  (exact: {1/6:.4f})")
print(f"P(even)      = {np.mean(die % 2 == 0):.4f}  (exact: {1/2:.4f})")
print(f"P(> 4)       = {np.mean(die > 4):.4f}  (exact: {2/6:.4f})")
print(f"P(1 or 6)    = {np.mean((die==1)|(die==6)):.4f}  (exact: {2/6:.4f})")

# ─────────────────────────────────────────────────────────────────────────────
# EXPERIMENT 2: Two Dice — Joint Sample Space (36 outcomes)
# ─────────────────────────────────────────────────────────────────────────────
die1 = np.random.randint(1, 7, size=n)
die2 = np.random.randint(1, 7, size=n)
total = die1 + die2

print("\n=== Two Dice — Sum Distribution ===")
# Count theoretical probabilities
sums = np.arange(2, 13)
exact_counts = {s: 0 for s in sums}
for d1 in range(1, 7):
    for d2 in range(1, 7):
        exact_counts[d1+d2] += 1

print(f"{'Sum':>4} | {'Exact P':>8} | {'Simulated P':>11} | {'Error':>8}")
print("-" * 42)
for s in sums:
    p_exact = exact_counts[s] / 36
    p_sim   = np.mean(total == s)
    print(f"{s:>4} | {p_exact:>8.4f} | {p_sim:>11.4f} | {abs(p_exact-p_sim):>8.5f}")

# ─────────────────────────────────────────────────────────────────────────────
# EXPERIMENT 3: Coin Toss Sequences — Sample Space Enumeration
# ─────────────────────────────────────────────────────────────────────────────
import itertools

def enumerate_sample_space(n_coins: int) -> list:
    return list(itertools.product(['H','T'], repeat=n_coins))

for n_coins in [1, 2, 3]:
    space = enumerate_sample_space(n_coins)
    print(f"\n{n_coins} coin(s) — |Ω| = {len(space)}")
    print(f"  Ω = {space}")

# ─────────────────────────────────────────────────────────────────────────────
# EXPERIMENT 4: Card Drawing Without Replacement
# ─────────────────────────────────────────────────────────────────────────────
suits  = ['♠','♥','♦','♣']
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck   = [f"{v}{s}" for s in suits for v in values]
print(f"\nFull Deck: {len(deck)} cards")

n_draws = 100_000
heart_ace_count = 0
for _ in range(n_draws):
    hand = np.random.choice(deck, size=5, replace=False)
    if 'A♥' in hand:
        heart_ace_count += 1

p_sim = heart_ace_count / n_draws
print(f"P(Ace of Hearts in 5-card hand) simulated = {p_sim:.4f}")
print(f"P(Ace of Hearts in 5-card hand) exact     = {5/52:.4f}")

# ─────────────────────────────────────────────────────────────────────────────
# VISUALISE: Sum of Two Dice
# ─────────────────────────────────────────────────────────────────────────────
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# Simulated
axes[0].bar(sums, [np.mean(total==s) for s in sums],
            color='steelblue', edgecolor='white', alpha=0.85)
axes[0].set_title("Simulated: Sum of Two Dice (n=100,000)")
axes[0].set_xlabel("Sum"); axes[0].set_ylabel("Relative Frequency")
axes[0].set_xticks(sums)

# Exact
axes[1].bar(sums, [exact_counts[s]/36 for s in sums],
            color='darkorange', edgecolor='white', alpha=0.85)
axes[1].set_title("Exact: Sum of Two Dice (Theoretical)")
axes[1].set_xlabel("Sum"); axes[1].set_xticks(sums)

plt.tight_layout()
plt.show()
```

### 2.3 Event Algebra with Sets

```python
import numpy as np

# Represent events as sets of outcomes
Omega = set(range(1, 7))           # {1,2,3,4,5,6}
A     = {x for x in Omega if x % 2 == 0}    # even  {2,4,6}
B     = {x for x in Omega if x > 3}         # > 3   {4,5,6}

print(f"Ω = {sorted(Omega)}")
print(f"A = {sorted(A)}  (even)")
print(f"B = {sorted(B)}  (> 3)")
print()
print(f"A ∪ B  (A or B)   = {sorted(A | B)}")
print(f"A ∩ B  (A and B)  = {sorted(A & B)}")
print(f"Aᶜ     (not A)    = {sorted(Omega - A)}")
print(f"A \\ B  (A not B)  = {sorted(A - B)}")
print()
print(f"P(A)     = {len(A)/len(Omega):.4f}")
print(f"P(B)     = {len(B)/len(Omega):.4f}")
print(f"P(A∪B)   = {len(A|B)/len(Omega):.4f}")
print(f"P(A∩B)   = {len(A&B)/len(Omega):.4f}")
print(f"P(Aᶜ)    = {len(Omega-A)/len(Omega):.4f}")
```

---

## 3. 📊 Basic Probability Rules

### 3.1 The Three Fundamental Rules

```
┌─────────────────────────────────────────────────────────────────┐
│  RULE 1 — COMPLEMENT                                           │
│  P(Aᶜ) = 1 - P(A)                                             │
├─────────────────────────────────────────────────────────────────┤
│  RULE 2 — ADDITION                                             │
│  P(A ∪ B) = P(A) + P(B) - P(A ∩ B)         [general]         │
│  P(A ∪ B) = P(A) + P(B)                    [if A∩B = ∅]      │
├─────────────────────────────────────────────────────────────────┤
│  RULE 3 — MULTIPLICATION                                       │
│  P(A ∩ B) = P(A) × P(B|A)                  [general]         │
│  P(A ∩ B) = P(A) × P(B)                    [if independent]  │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Complement Rule

```python
import numpy as np
np.random.seed(42)
n = 1_000_000
rolls = np.random.randint(1, 7, size=n)

# P(not getting a 6) = 1 - P(6)
p_six     = np.mean(rolls == 6)
p_not_six = np.mean(rolls != 6)

print("=== Complement Rule ===")
print(f"P(6)          = {p_six:.5f}   (exact: {1/6:.5f})")
print(f"P(not 6) sim  = {p_not_six:.5f}")
print(f"1 - P(6)      = {1 - p_six:.5f}   ← same as P(not 6) ✓")

# Real-world: system reliability
# If a component fails with P = 0.02, P(no failure) = 0.98
p_fail   = 0.02
p_ok     = 1 - p_fail
# Two independent components in SERIES — both must work
p_series = p_ok ** 2
# Two independent components in PARALLEL — at least one must work
p_parallel = 1 - p_fail ** 2

print(f"\n=== System Reliability ===")
print(f"Component P(fail) = {p_fail}")
print(f"Series  P(system ok) = {p_series:.4f}")
print(f"Parallel P(system ok)= {p_parallel:.4f}")
```

### 3.3 Addition Rule — Full Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

np.random.seed(42)
n = 1_000_000
rolls = np.random.randint(1, 7, size=n)

print("=== Addition Rule — Mutually Exclusive ===")
# P(2 or 5) — can't happen simultaneously
p2    = np.mean(rolls == 2)
p5    = np.mean(rolls == 5)
p2o5  = np.mean((rolls == 2) | (rolls == 5))
print(f"P(2)          = {p2:.5f}")
print(f"P(5)          = {p5:.5f}")
print(f"P(2) + P(5)   = {p2+p5:.5f}")
print(f"P(2 ∪ 5) sim  = {p2o5:.5f}  ← match ✓ (no overlap)")

print("\n=== Addition Rule — Non Mutually Exclusive ===")
# P(even or > 4): overlap = {6}
A = rolls % 2 == 0     # {2,4,6}
B = rolls > 4          # {5,6}
AandB = A & B          # {6}
AorB  = A | B          # {2,4,5,6}

pA     = np.mean(A)
pB     = np.mean(B)
pAandB = np.mean(AandB)
pAorB  = np.mean(AorB)

print(f"P(even)         = {pA:.5f}   (exact: {3/6:.5f})")
print(f"P(>4)           = {pB:.5f}   (exact: {2/6:.5f})")
print(f"P(even ∩ >4)    = {pAandB:.5f}   (exact: {1/6:.5f})")
print(f"P(A)+P(B)-P(A∩B)= {pA+pB-pAandB:.5f}")
print(f"P(even ∪ >4) sim= {pAorB:.5f}   ← same ✓")

# Venn Diagram
fig, ax = plt.subplots(figsize=(7, 5))
ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.set_aspect('equal'); ax.axis('off')
ax.set_title("Venn Diagram: A={even}={2,4,6}, B={>4}={5,6}", fontsize=12)

circleA = plt.Circle((3.8, 3.5), 2.5, color='steelblue', alpha=0.35)
circleB = plt.Circle((6.2, 3.5), 2.5, color='darkorange', alpha=0.35)
ax.add_patch(circleA); ax.add_patch(circleB)

ax.text(2.5, 3.5, '{2, 4}',    ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(5.0, 3.5, '{6}',       ha='center', va='center', fontsize=12, fontweight='bold', color='white')
ax.text(7.5, 3.5, '{5}',       ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(1.0, 6.2, 'A = even',  ha='center', fontsize=11, color='steelblue')
ax.text(9.0, 6.2, 'B = > 4',   ha='center', fontsize=11, color='darkorange')

plt.tight_layout()
plt.show()
```

### 3.4 Multiplication Rule — Independence Testing

```python
import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd

np.random.seed(42)
n = 100_000

# ── INDEPENDENT events ───────────────────────────────────────────────────────
flip1 = np.random.choice([0,1], size=n)   # coin 1
flip2 = np.random.choice([0,1], size=n)   # coin 2 (independent)

p_H1    = np.mean(flip1 == 1)
p_H2    = np.mean(flip2 == 1)
p_HH    = np.mean((flip1 == 1) & (flip2 == 1))
product = p_H1 * p_H2

print("=== Independent Events (Two Coins) ===")
print(f"P(H1)         = {p_H1:.4f}")
print(f"P(H2)         = {p_H2:.4f}")
print(f"P(H1) × P(H2) = {product:.4f}")
print(f"P(H1 ∩ H2) sim= {p_HH:.4f}   ← match confirms independence ✓")

# ── DEPENDENT events ─────────────────────────────────────────────────────────
# Weather (Rain) and Commute (Late)
rain = np.random.choice([0,1], size=n, p=[0.7, 0.3])   # P(rain)=0.3
late = np.where(rain==1,
                np.random.binomial(1, 0.8, n),           # P(late|rain)=0.8
                np.random.binomial(1, 0.1, n))           # P(late|no rain)=0.1

p_rain = np.mean(rain)
p_late = np.mean(late)
p_both = np.mean((rain==1) & (late==1))

print("\n=== Dependent Events (Rain & Late) ===")
print(f"P(Rain)           = {p_rain:.4f}")
print(f"P(Late)           = {p_late:.4f}")
print(f"P(Rain)×P(Late)   = {p_rain*p_late:.4f}   ← assumed independence")
print(f"P(Rain ∩ Late) sim= {p_both:.4f}   ← actual joint probability")
print(f"Difference        = {abs(p_rain*p_late - p_both):.4f}  (non-zero → DEPENDENT)")

# Chi-square test of independence
ct = pd.crosstab(rain, late)
chi2, p_val, dof, _ = chi2_contingency(ct)
print(f"\nChi² test: χ²={chi2:.2f}, p-value={p_val:.2e}")
print(f"Conclusion: {'DEPENDENT (reject independence)' if p_val < 0.05 else 'INDEPENDENT'}")

# ── GENERAL MULTIPLICATION RULE ───────────────────────────────────────────────
# P(A ∩ B) = P(A) × P(B|A)
# P(late ∩ rain) = P(rain) × P(late | rain)
p_late_given_rain = np.mean(late[rain == 1])
result = p_rain * p_late_given_rain
print(f"\n=== General Multiplication Rule ===")
print(f"P(Rain) × P(Late|Rain) = {p_rain:.4f} × {p_late_given_rain:.4f} = {result:.4f}")
print(f"P(Rain ∩ Late) direct  = {p_both:.4f}  ← match ✓")
```

---

# ═══════════════════════════════════════════════
# PART 2 · CONDITIONAL PROBABILITY & BAYES
# ═══════════════════════════════════════════════

---

## 4. 🔍 Conditional Probability

### 4.1 Intuition

Conditional probability **restricts the universe**. When we know B has happened, we throw away all outcomes where B didn't happen, and re-calculate probabilities within that smaller world.

```
Universe: All 100 patients
Event A: Patient has disease
Event B: Patient tested positive

P(A)     = 1/100 = 0.01          (before knowing test result)
P(A | B) = ?                     (after learning the test was positive)
            ↑ this is what actually matters in practice
```

### 4.2 Mathematical Definition

```
P(A | B) = P(A ∩ B) / P(B)     [provided P(B) > 0]

Rearranged → Multiplication Rule:
P(A ∩ B) = P(A | B) × P(B) = P(B | A) × P(A)
```

### 4.3 Full Python Implementation

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# SCENARIO 1: Student Exam — Grade given Study Hours
# ─────────────────────────────────────────────────────────────────────────────
n = 100_000
# Students study (1) or don't study (0)
studied = np.random.binomial(1, 0.6, n)          # 60% study
# Grade: Pass(1) / Fail(0)
passed  = np.where(studied==1,
                   np.random.binomial(1, 0.85, n), # P(pass|studied)=0.85
                   np.random.binomial(1, 0.25, n)) # P(pass|not studied)=0.25

df = pd.DataFrame({'studied': studied, 'passed': passed})

# Compute all conditional probabilities
p_pass               = df['passed'].mean()
p_studied            = df['studied'].mean()
p_pass_given_studied = df.loc[df['studied']==1, 'passed'].mean()
p_pass_given_not     = df.loc[df['studied']==0, 'passed'].mean()
p_studied_given_pass = df.loc[df['passed']==1,  'studied'].mean()

print("=== Conditional Probability — Study vs Pass ===")
print(f"P(pass)                  = {p_pass:.4f}")
print(f"P(pass | studied)        = {p_pass_given_studied:.4f}  (set: 0.85)")
print(f"P(pass | not studied)    = {p_pass_given_not:.4f}  (set: 0.25)")
print(f"P(studied | passed)      = {p_studied_given_pass:.4f}  ← reversed conditioning")

# Verify formula: P(A|B) = P(A∩B)/P(B)
p_pass_and_studied = df[(df['passed']==1)&(df['studied']==1)].shape[0] / n
formula_result     = p_pass_and_studied / p_studied
print(f"\nFormula check: P(pass∩studied)/P(studied) = {p_pass_and_studied:.4f}/{p_studied:.4f} = {formula_result:.4f}")
print(f"Direct P(pass|studied)                   = {p_pass_given_studied:.4f}  ✓")

# ─────────────────────────────────────────────────────────────────────────────
# SCENARIO 2: Crosstab — The classic conditional probability table
# ─────────────────────────────────────────────────────────────────────────────
ct_counts  = pd.crosstab(df['studied'], df['passed'],
                         rownames=['Studied'], colnames=['Passed'])
ct_row_pct = pd.crosstab(df['studied'], df['passed'],
                         rownames=['Studied'], colnames=['Passed'],
                         normalize='index')  # P(Passed | Studied)
ct_col_pct = pd.crosstab(df['studied'], df['passed'],
                         rownames=['Studied'], colnames=['Passed'],
                         normalize='columns')  # P(Studied | Passed)

print("\n--- Joint Counts ---")
print(ct_counts)
print("\n--- P(Passed | Studied)  [normalize='index'] ---")
print(ct_row_pct.round(4))
print("\n--- P(Studied | Passed)  [normalize='columns'] ---")
print(ct_col_pct.round(4))

# ─────────────────────────────────────────────────────────────────────────────
# VISUALISE: Conditional distributions
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 4))

ct_row_pct.plot(kind='bar', ax=axes[0], color=['salmon','steelblue'],
                edgecolor='white', alpha=0.85, rot=0)
axes[0].set_title("P(Passed | Studied) — Row-normalised")
axes[0].set_xlabel("Studied (0=No, 1=Yes)")
axes[0].set_ylabel("Probability")
axes[0].legend(['Failed','Passed'])

# Heatmap of joint probability
joint = pd.crosstab(df['studied'], df['passed'], normalize='all')
sns.heatmap(joint, annot=True, fmt='.4f', cmap='Blues',
            ax=axes[1], cbar=True,
            xticklabels=['Failed','Passed'],
            yticklabels=['Not Studied','Studied'])
axes[1].set_title("Joint Probability Heatmap")

plt.tight_layout()
plt.show()

# ─────────────────────────────────────────────────────────────────────────────
# SCENARIO 3: Total Probability Theorem
# ─────────────────────────────────────────────────────────────────────────────
# P(B) = Σ P(B|Aᵢ) × P(Aᵢ)   where {A₁, A₂, ...} partition Ω
print("\n=== Total Probability Theorem ===")
# Three types of students: poor(30%), average(50%), excellent(20%)
p_poor      = 0.30;  p_pass_poor = 0.20
p_avg       = 0.50;  p_pass_avg  = 0.65
p_excel     = 0.20;  p_pass_exc  = 0.95

p_pass_total = (p_pass_poor * p_poor +
                p_pass_avg  * p_avg  +
                p_pass_exc  * p_excel)
print(f"P(pass) = P(pass|poor)×P(poor) + P(pass|avg)×P(avg) + P(pass|excel)×P(excel)")
print(f"        = {p_pass_poor}×{p_poor} + {p_pass_avg}×{p_avg} + {p_pass_exc}×{p_excel}")
print(f"        = {p_pass_poor*p_poor:.3f} + {p_pass_avg*p_avg:.3f} + {p_pass_exc*p_excel:.3f}")
print(f"        = {p_pass_total:.4f}")
```

---

## 5. 🧠 Bayes Theorem

### 5.1 Intuition — Updating Beliefs

Bayes Theorem answers: *"Given new evidence, how should I update my belief?"*

```
Prior Belief  +  New Evidence  →  Updated Belief (Posterior)

Think of it as:
  P(cause | effect) = [P(effect | cause) × P(cause)] / P(effect)
```

**The Formula:**
```
                P(B | A) × P(A)
P(A | B)  =   ─────────────────
                     P(B)

where P(B) = Σᵢ P(B | Aᵢ) × P(Aᵢ)   [Total Probability]
```

### 5.2 Step-by-Step Medical Diagnosis Example

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ─────────────────────────────────────────────────────────────────────────────
# PROBLEM SETUP
# ─────────────────────────────────────────────────────────────────────────────
p_disease        = 0.005   # Prevalence: 0.5% of population
p_pos_given_dis  = 0.99    # Sensitivity: test correctly identifies sick
p_neg_given_dis  = 0.01    # Miss rate (1 - sensitivity)
p_pos_given_well = 0.02    # False positive rate
p_neg_given_well = 0.98    # Specificity (1 - false positive rate)
p_well           = 1 - p_disease

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: Compute P(positive) using Total Probability Theorem
# ─────────────────────────────────────────────────────────────────────────────
p_positive = (p_pos_given_dis * p_disease) + (p_pos_given_well * p_well)
p_negative = 1 - p_positive

print("=" * 55)
print("BAYES THEOREM — Medical Diagnosis")
print("=" * 55)
print(f"\nGiven:")
print(f"  P(disease)                = {p_disease:.4f}  ({p_disease*100:.1f}%)")
print(f"  P(positive | disease)     = {p_pos_given_dis:.4f}  (sensitivity)")
print(f"  P(positive | no disease)  = {p_pos_given_well:.4f}  (false positive rate)")

print(f"\nStep 1 — Total Probability P(positive):")
print(f"  P(+) = P(+|sick)×P(sick) + P(+|well)×P(well)")
print(f"       = {p_pos_given_dis}×{p_disease} + {p_pos_given_well}×{p_well}")
print(f"       = {p_pos_given_dis*p_disease:.5f} + {p_pos_given_well*p_well:.5f}")
print(f"       = {p_positive:.5f}")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 2: Apply Bayes Theorem
# ─────────────────────────────────────────────────────────────────────────────
p_dis_given_pos  = (p_pos_given_dis * p_disease) / p_positive
p_well_given_pos = (p_pos_given_well * p_well)   / p_positive
p_dis_given_neg  = (p_neg_given_dis * p_disease) / p_negative

print(f"\nStep 2 — Bayes Theorem:")
print(f"  P(sick | positive) = P(+|sick)×P(sick) / P(+)")
print(f"                     = {p_pos_given_dis*p_disease:.5f} / {p_positive:.5f}")
print(f"                     = {p_dis_given_pos:.4f}  ({p_dis_given_pos*100:.2f}%)")
print(f"\n  P(well | positive) = {p_well_given_pos:.4f}  ({p_well_given_pos*100:.2f}%)")
print(f"  P(sick | negative) = {p_dis_given_neg:.6f}  ({p_dis_given_neg*100:.4f}%)")
print(f"\n  ⚠️  Despite 99% sensitive test, only {p_dis_given_pos*100:.1f}% chance of disease!")
print(f"  This is because the disease is RARE (base rate = {p_disease*100:.1f}%)")

# ─────────────────────────────────────────────────────────────────────────────
# SIMULATION VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
np.random.seed(42)
N = 2_000_000

has_disease  = np.random.binomial(1, p_disease, N)
test_pos     = np.where(has_disease == 1,
                        np.random.binomial(1, p_pos_given_dis, N),
                        np.random.binomial(1, p_pos_given_well, N))

positives       = test_pos == 1
sim_posterior   = np.mean(has_disease[positives])
print(f"\nSimulation verification (N={N:,}):")
print(f"  Analytical P(sick|+) = {p_dis_given_pos:.5f}")
print(f"  Simulated  P(sick|+) = {sim_posterior:.5f}   ← match ✓")

# ─────────────────────────────────────────────────────────────────────────────
# BAYESIAN UPDATING — Sequential Evidence
# ─────────────────────────────────────────────────────────────────────────────
def bayes_update(prior, p_evidence_given_true, p_evidence_given_false):
    """Single Bayes update step."""
    p_evidence = p_evidence_given_true * prior + p_evidence_given_false * (1-prior)
    posterior  = (p_evidence_given_true * prior) / p_evidence
    return posterior

# Update belief after multiple positive tests
print("\n=== Sequential Bayesian Updating ===")
print(f"{'Test #':<8} {'Prior':>10} {'Posterior':>12}")
print("-" * 33)
belief = p_disease
print(f"{'Start':<8} {belief:>10.6f}")
for i in range(1, 6):
    belief = bayes_update(belief, p_pos_given_dis, p_pos_given_well)
    print(f"{'Test '+str(i):<8} {'-':>10} {belief:>12.6f}  ({belief*100:.2f}%)")
```

### 5.3 Visualising Prior → Posterior

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# ── Plot 1: Posterior vs Prevalence ──────────────────────────────────────────
prevalences = np.linspace(0.001, 0.5, 500)
p_sens, p_fpr = 0.99, 0.02

posteriors = []
for prev in prevalences:
    p_pos   = p_sens * prev + p_fpr * (1 - prev)
    post    = (p_sens * prev) / p_pos
    posteriors.append(post)

axes[0].plot(prevalences * 100, posteriors, color='steelblue', linewidth=2.5)
axes[0].axhline(0.5, color='salmon', linestyle='--', linewidth=1.5, label='50% threshold')
axes[0].axvline(0.5, color='gray',   linestyle=':', linewidth=1.5, label='0.5% prevalence')
axes[0].set_xlabel("Disease Prevalence (%)")
axes[0].set_ylabel("P(Disease | Positive Test)")
axes[0].set_title("Posterior Probability vs Base Rate\n(Sensitivity=99%, FPR=2%)")
axes[0].legend()

# ── Plot 2: Sequential updates ────────────────────────────────────────────────
priors = [0.005]
for _ in range(10):
    priors.append(bayes_update(priors[-1], p_sens, p_fpr))

axes[1].plot(range(len(priors)), priors, 'o-', color='darkorange',
             linewidth=2, markersize=7)
axes[1].axhline(0.5, color='salmon', linestyle='--', label='50%')
axes[1].axhline(0.95, color='seagreen', linestyle=':', label='95%')
axes[1].set_xlabel("Number of Positive Tests")
axes[1].set_ylabel("P(Disease)")
axes[1].set_title("Bayesian Updating — Belief After Each Positive Test")
axes[1].set_xticks(range(len(priors)))
axes[1].legend()

plt.tight_layout()
plt.show()
```

### 5.4 Bayes in ML — Naive Bayes Classifier from Scratch

```python
import numpy as np
import pandas as pd
from collections import defaultdict

# ─────────────────────────────────────────────────────────────────────────────
# DATASET: Email spam classification
# Features: contains_free, contains_win, contains_click, is_short
# ─────────────────────────────────────────────────────────────────────────────
data = {
    'free'  : [1,1,0,0,1,0,1,0,0,0,1,1,0,0,1],
    'win'   : [1,0,0,0,1,0,1,0,0,0,0,1,0,0,0],
    'click' : [0,1,0,1,1,0,0,0,1,0,1,0,0,1,1],
    'short' : [1,0,1,0,0,1,1,1,0,1,0,1,1,0,1],
    'spam'  : [1,1,0,0,1,0,1,0,0,0,1,1,0,1,1],
}
df = pd.DataFrame(data)

class NaiveBayesClassifier:
    def __init__(self, laplace_smoothing: float = 1.0):
        self.alpha  = laplace_smoothing   # Laplace/additive smoothing
        self.priors = {}
        self.likelihoods = {}

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.classes = y.unique()
        self.features = X.columns.tolist()
        n_total = len(y)

        # Compute priors P(class)
        for c in self.classes:
            self.priors[c] = (y == c).sum() / n_total

        # Compute likelihoods P(feature=v | class) with Laplace smoothing
        self.likelihoods = defaultdict(dict)
        for c in self.classes:
            X_c = X[y == c]
            n_c = len(X_c)
            for feat in self.features:
                n_feat = (X_c[feat] == 1).sum()
                # Laplace smoothing: (count + α) / (total + α × n_values)
                self.likelihoods[c][feat] = (n_feat + self.alpha) / (n_c + 2*self.alpha)

    def predict_proba(self, X: pd.DataFrame) -> pd.DataFrame:
        results = []
        for _, row in X.iterrows():
            scores = {}
            for c in self.classes:
                log_prob = np.log(self.priors[c])
                for feat in self.features:
                    p_feat = self.likelihoods[c][feat]
                    if row[feat] == 1:
                        log_prob += np.log(p_feat)
                    else:
                        log_prob += np.log(1 - p_feat)
                scores[c] = log_prob

            # Convert log-probs to probabilities (softmax over two classes)
            max_score = max(scores.values())
            exp_scores = {c: np.exp(s - max_score) for c, s in scores.items()}
            total = sum(exp_scores.values())
            results.append({c: v/total for c, v in exp_scores.items()})
        return pd.DataFrame(results)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        proba = self.predict_proba(X)
        return (proba[1] >= 0.5).astype(int).values

# Train & evaluate
X = df[['free','win','click','short']]
y = df['spam']
clf = NaiveBayesClassifier(laplace_smoothing=1.0)
clf.fit(X, y)

# Show priors and likelihoods
print("=== Naive Bayes — Learned Parameters ===")
print(f"P(spam)    = {clf.priors[1]:.4f}")
print(f"P(not spam)= {clf.priors[0]:.4f}")
print("\nLikelihoods P(feature | class):")
print(f"{'Feature':<8} {'P(feat|spam)':>14} {'P(feat|ham)':>13}")
print("-" * 38)
for feat in clf.features:
    print(f"{feat:<8} {clf.likelihoods[1][feat]:>14.4f} {clf.likelihoods[0][feat]:>13.4f}")

# Predict on new email
new_email = pd.DataFrame({'free':[1], 'win':[1], 'click':[0], 'short':[0]})
proba = clf.predict_proba(new_email)
print(f"\nNew email: free=1, win=1, click=0, short=0")
print(f"P(spam)    = {proba[1].values[0]:.4f}")
print(f"P(not spam)= {proba[0].values[0]:.4f}")
print(f"Prediction : {'SPAM' if proba[1].values[0] >= 0.5 else 'HAM'}")
```

---

# ═══════════════════════════════════════════════
# PART 3 · RANDOM VARIABLES & DISTRIBUTIONS
# ═══════════════════════════════════════════════

---

## 6. 🔢 Random Variables

### 6.1 Definition and Types

A **random variable** X is a function that maps each outcome ω in Ω to a real number.

```
Experiment      Sample Space     Random Variable X
─────────────   ────────────     ───────────────────────────────────
Coin flip       {H, T}           X(H)=1, X(T)=0
Die roll        {1,2,3,4,5,6}   X(ω) = ω
Height of adult Ω = ℝ⁺           X(ω) = ω (in cm)
```

### 6.2 PMF vs PDF — Full Comparison

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

# ── PMF: Binomial ─────────────────────────────────────────────────────────────
x_d  = np.arange(0, 21)
pmf  = binom.pmf(x_d, n=20, p=0.4)

axes[0,0].bar(x_d, pmf, color='steelblue', edgecolor='white', alpha=0.85)
axes[0,0].set_title("PMF — Binomial(n=20, p=0.4)\nP(X=k) at each discrete k")
axes[0,0].set_xlabel("k"); axes[0,0].set_ylabel("P(X = k)")
axes[0,0].axvline(binom.mean(20,0.4), color='red', linestyle='--',
                  label=f"Mean={binom.mean(20,0.4):.1f}")
axes[0,0].legend()
print(f"PMF sum = {pmf.sum():.6f}  (must equal 1)")

# ── CDF: Binomial ─────────────────────────────────────────────────────────────
cdf_d = binom.cdf(x_d, n=20, p=0.4)
axes[0,1].step(x_d, cdf_d, where='post', color='steelblue', linewidth=2)
axes[0,1].scatter(x_d, cdf_d, color='steelblue', s=30, zorder=5)
axes[0,1].set_title("CDF — Binomial(n=20, p=0.4)\nF(x) = P(X ≤ x)")
axes[0,1].set_xlabel("x"); axes[0,1].set_ylabel("P(X ≤ x)")
axes[0,1].axhline(0.5, color='gray', linestyle=':', alpha=0.7)

# ── PDF: Normal ───────────────────────────────────────────────────────────────
x_c   = np.linspace(-4, 4, 400)
pdf_c = norm.pdf(x_c, 0, 1)

axes[1,0].plot(x_c, pdf_c, color='darkorange', linewidth=2.5)
axes[1,0].fill_between(x_c, pdf_c, alpha=0.25, color='darkorange')
# Shade P(-1 ≤ X ≤ 1)
mask = (x_c >= -1) & (x_c <= 1)
axes[1,0].fill_between(x_c[mask], pdf_c[mask], alpha=0.5, color='gold',
                        label='P(-1≤X≤1)=68%')
axes[1,0].set_title("PDF — Normal(μ=0, σ=1)\nf(x) = density, NOT probability")
axes[1,0].set_xlabel("x"); axes[1,0].set_ylabel("f(x) — density")
axes[1,0].legend()
print(f"PDF integral ≈ {np.trapz(pdf_c, x_c):.6f}  (must equal 1)")

# ── CDF: Normal ───────────────────────────────────────────────────────────────
cdf_c = norm.cdf(x_c, 0, 1)
axes[1,1].plot(x_c, cdf_c, color='darkorange', linewidth=2.5)
axes[1,1].axhline(0.5, color='gray', linestyle=':', alpha=0.7, label='50%')
axes[1,1].axvline(0,   color='red',  linestyle='--', alpha=0.7, label='μ=0')
axes[1,1].set_title("CDF — Normal(μ=0, σ=1)\nF(x) = P(X ≤ x)")
axes[1,1].set_xlabel("x"); axes[1,1].set_ylabel("P(X ≤ x)")
axes[1,1].legend()

plt.suptitle("PMF vs PDF — Discrete vs Continuous Random Variables",
             fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.show()
```

---

## 7. 🎯 Discrete Probability Distributions

> **Library: SciPy stats** — consistent API for all distributions:
> `.pmf(k)` · `.cdf(k)` · `.sf(k)` · `.ppf(q)` · `.rvs(size)` · `.mean()` · `.var()` · `.std()`

---

### 7.1 Bernoulli Distribution

**Intuition:** One binary trial — success (1) or failure (0).

```
P(X=1) = p       P(X=0) = 1-p
E[X] = p         Var[X] = p(1-p)
```

**When to use:** Any single yes/no experiment — spam/not-spam, click/no-click, defect/no-defect.

```python
from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

p = 0.65   # probability of success

# ── Core computations ─────────────────────────────────────────────────────────
print("=== Bernoulli(p=0.65) ===")
print(f"P(X=0) = {bernoulli.pmf(0, p):.4f}")
print(f"P(X=1) = {bernoulli.pmf(1, p):.4f}")
print(f"CDF at 0: P(X≤0) = {bernoulli.cdf(0, p):.4f}")
print(f"CDF at 1: P(X≤1) = {bernoulli.cdf(1, p):.4f}")
print(f"E[X]   = {bernoulli.mean(p):.4f}")
print(f"Var[X] = {bernoulli.var(p):.4f}")
print(f"Std[X] = {bernoulli.std(p):.4f}")

# ── Simulation & verification ─────────────────────────────────────────────────
np.random.seed(42)
samples = bernoulli.rvs(p, size=100_000)
print(f"\nSimulated mean  = {samples.mean():.4f}  (exact: {p})")
print(f"Simulated var   = {samples.var():.4f}  (exact: {p*(1-p):.4f})")

# ── Visualise how p changes the distribution ──────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(13, 4))
for ax, prob in zip(axes, [0.2, 0.5, 0.8]):
    ax.bar([0, 1], [bernoulli.pmf(0, prob), bernoulli.pmf(1, prob)],
           color=['salmon', 'steelblue'], edgecolor='white', alpha=0.85, width=0.4)
    ax.set_title(f"Bernoulli(p={prob})")
    ax.set_xlabel("Outcome (0=Fail, 1=Success)")
    ax.set_ylabel("Probability")
    ax.set_xticks([0, 1])
    ax.set_ylim(0, 1)
    ax.text(0, bernoulli.pmf(0,prob)+0.02, f"{bernoulli.pmf(0,prob):.2f}", ha='center')
    ax.text(1, bernoulli.pmf(1,prob)+0.02, f"{bernoulli.pmf(1,prob):.2f}", ha='center')

plt.suptitle("Bernoulli PMF for Different p Values", fontsize=13, y=1.02)
plt.tight_layout()
plt.show()
```

---

### 7.2 Binomial Distribution

**Intuition:** Run n independent Bernoulli trials. Count successes.

```
P(X=k) = C(n,k) × pᵏ × (1-p)ⁿ⁻ᵏ     k ∈ {0,1,...,n}
E[X] = np                               Var[X] = np(1-p)
```

**When to use:** n independent trials, constant success probability — quality control, A/B tests.

```python
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n, p = 20, 0.35

# ── Core probabilities ────────────────────────────────────────────────────────
print("=== Binomial(n=20, p=0.35) ===")
print(f"E[X]    = {binom.mean(n,p):.4f}   (= np = {n*p})")
print(f"Var[X]  = {binom.var(n,p):.4f}   (= np(1-p) = {n*p*(1-p):.4f})")
print(f"Std[X]  = {binom.std(n,p):.4f}")

print(f"\nP(X=7)    = {binom.pmf(7,n,p):.4f}")
print(f"P(X≤8)    = {binom.cdf(8,n,p):.4f}")
print(f"P(X>10)   = {binom.sf(10,n,p):.4f}   (= 1 - CDF(10))")
print(f"P(5≤X≤10) = {binom.cdf(10,n,p)-binom.cdf(4,n,p):.4f}")
print(f"90th pct  = {binom.ppf(0.90,n,p):.0f}   (smallest k with CDF≥0.90)")

# ── PMF table ────────────────────────────────────────────────────────────────
print("\n--- PMF Table (k=0 to 12) ---")
print(f"{'k':>3} | {'P(X=k)':>10} | {'P(X≤k)':>10} | bar")
print("-" * 50)
for k in range(13):
    pmf_k = binom.pmf(k, n, p)
    cdf_k = binom.cdf(k, n, p)
    bar   = '█' * int(pmf_k * 200)
    print(f"{k:>3} | {pmf_k:>10.5f} | {cdf_k:>10.5f} | {bar}")

# ── Full visualisation ────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
x = np.arange(0, n+1)

# PMF — multiple p values
for prob, color in zip([0.2, 0.35, 0.6], ['steelblue','darkorange','seagreen']):
    axes[0].plot(x, binom.pmf(x, n, prob), 'o-', color=color,
                 linewidth=2, markersize=4, label=f'p={prob}')
axes[0].set_title("Binomial PMF — Different p")
axes[0].set_xlabel("k"); axes[0].set_ylabel("P(X=k)")
axes[0].legend()

# PMF + CDF
pmf_vals = binom.pmf(x, n, p)
cdf_vals = binom.cdf(x, n, p)
ax2b = axes[1].twinx()
axes[1].bar(x, pmf_vals, color='steelblue', alpha=0.7, label='PMF')
ax2b.step(x, cdf_vals, where='mid', color='red', linewidth=2, label='CDF')
axes[1].set_title(f"Binomial PMF + CDF (n={n}, p={p})")
axes[1].set_xlabel("k"); axes[1].set_ylabel("P(X=k)", color='steelblue')
ax2b.set_ylabel("P(X≤k)", color='red')

# Simulation vs Theoretical
np.random.seed(42)
sim = binom.rvs(n, p, size=50_000)
axes[2].hist(sim, bins=np.arange(-0.5, n+1.5, 1), density=True,
             color='steelblue', edgecolor='white', alpha=0.7, label='Simulation')
axes[2].plot(x, binom.pmf(x,n,p), 'ro-', linewidth=2, markersize=5,
             label='Theoretical PMF')
axes[2].set_title("Simulation vs Theoretical")
axes[2].set_xlabel("k"); axes[2].legend()

plt.tight_layout()
plt.show()

# ── Real-world: A/B Test ──────────────────────────────────────────────────────
print("\n=== A/B Test Example ===")
# Baseline click-through rate = 5%. New design tested on 500 users.
n_users  = 500;  p_baseline = 0.05
observed_clicks = 32

# P(seeing ≥ 32 clicks if baseline is true) = p-value
p_value = binom.sf(observed_clicks - 1, n_users, p_baseline)
print(f"Expected clicks under baseline: {n_users * p_baseline:.0f}")
print(f"Observed clicks: {observed_clicks}")
print(f"P(X ≥ {observed_clicks} | p=0.05) = {p_value:.5f}")
print(f"Conclusion: {'SIGNIFICANT (p<0.05) — new design works!' if p_value < 0.05 else 'Not significant'}")
```

---

### 7.3 Poisson Distribution

**Intuition:** Count of events in a fixed interval when events occur at a constant average rate λ.

```
P(X=k) = (e⁻λ × λᵏ) / k!      k ∈ {0,1,2,...}
E[X] = λ                        Var[X] = λ
```

**Key property:** Mean = Variance = λ. If data shows Var >> Mean → overdispersion (use Negative Binomial instead).

**When to use:** Emails per hour, server requests per second, rare disease cases per year, insurance claims per month.

```python
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── Core computations ─────────────────────────────────────────────────────────
lam = 6   # average 6 events per interval

print("=== Poisson(λ=6) ===")
print(f"E[X]    = {poisson.mean(lam):.4f}   (= λ = {lam})")
print(f"Var[X]  = {poisson.var(lam):.4f}   (= λ = {lam})")
print(f"Std[X]  = {poisson.std(lam):.4f}   (= √λ = {lam**0.5:.4f})")

print(f"\nP(X=6)    = {poisson.pmf(6, lam):.5f}   (most likely value = λ)")
print(f"P(X=0)    = {poisson.pmf(0, lam):.5f}   (probability of no events)")
print(f"P(X≤4)    = {poisson.cdf(4, lam):.5f}")
print(f"P(X>8)    = {poisson.sf(8, lam):.5f}")
print(f"P(3≤X≤9)  = {poisson.cdf(9,lam)-poisson.cdf(2,lam):.5f}")

# ── PMF for different λ ───────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
x = np.arange(0, 25)

for l, color in zip([1, 4, 8, 15], ['steelblue','darkorange','seagreen','purple']):
    axes[0].plot(x, poisson.pmf(x, l), 'o-', color=color,
                 linewidth=2, markersize=4, label=f'λ={l}')
axes[0].set_title("Poisson PMF for Different λ")
axes[0].set_xlabel("k — Number of Events"); axes[0].set_ylabel("P(X=k)")
axes[0].legend()

# Simulation
np.random.seed(42)
sim = poisson.rvs(lam, size=50_000)
axes[1].hist(sim, bins=np.arange(-0.5, 22.5, 1), density=True,
             color='steelblue', edgecolor='white', alpha=0.7, label='Simulated')
axes[1].plot(x, poisson.pmf(x, lam), 'ro-', linewidth=2, markersize=5,
             label=f'Theoretical (λ={lam})')
axes[1].set_title(f"Poisson(λ={lam}) — Theory vs Simulation")
axes[1].set_xlabel("k"); axes[1].legend()

plt.tight_layout()
plt.show()

# ── Real-world: Overdispersion Test ──────────────────────────────────────────
print("\n=== Overdispersion Check ===")
np.random.seed(42)
# If Var > Mean → NOT Poisson (overdispersed) → use Negative Binomial
data_poisson = poisson.rvs(5, size=1000)
data_overdispersed = np.random.negative_binomial(2, 0.28, 1000)  # overdispersed

for name, data in [("Poisson-generated", data_poisson),
                   ("Overdispersed-data", data_overdispersed)]:
    ratio = data.var() / data.mean()
    print(f"{name}: Mean={data.mean():.2f}, Var={data.var():.2f}, "
          f"Var/Mean={ratio:.2f} {'← OVERDISPERSED' if ratio > 1.5 else '← OK for Poisson'}")
```

---

### 7.4 Geometric Distribution

**Intuition:** Number of trials until the first success.

```
P(X=k) = (1-p)^(k-1) × p     k ∈ {1,2,3,...}
E[X] = 1/p                    Var[X] = (1-p)/p²
```

```python
from scipy.stats import geom
import numpy as np
import matplotlib.pyplot as plt

p = 0.3   # probability of success on each trial

print("=== Geometric(p=0.3) ===")
print(f"E[X] = 1/p = {1/p:.4f}   (expected trials until first success)")
print(f"Var  = {geom.var(p):.4f}")
print(f"\nP(X=1) = {geom.pmf(1,p):.4f}  (success on 1st try)")
print(f"P(X=3) = {geom.pmf(3,p):.4f}  (fail twice, succeed on 3rd)")
print(f"P(X≤5) = {geom.cdf(5,p):.4f}  (succeed within 5 trials)")

x = np.arange(1, 20)
plt.figure(figsize=(9, 4))
for prob, color in zip([0.1, 0.3, 0.6], ['steelblue','darkorange','seagreen']):
    plt.plot(x, geom.pmf(x, prob), 'o-', color=color,
             linewidth=2, markersize=5, label=f'p={prob}, E[X]={1/prob:.1f}')
plt.title("Geometric PMF — Trials Until First Success")
plt.xlabel("k (trial number of first success)")
plt.ylabel("P(X = k)")
plt.legend()
plt.tight_layout()
plt.show()
```

---

## 8. 📈 Continuous Probability Distributions

---

### 8.1 Uniform Distribution

**Intuition:** All values in [a, b] are equally likely. The "I have no preference" distribution.

```
f(x) = 1/(b-a)     for a ≤ x ≤ b,  else 0
E[X] = (a+b)/2     Var[X] = (b-a)²/12
```

```python
from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

a, b = 2, 10

print("=== Uniform(a=2, b=10) ===")
print(f"f(x) = 1/(b-a) = 1/{b-a} = {1/(b-a):.4f}  for x in [{a},{b}]")
print(f"E[X]   = (a+b)/2 = {(a+b)/2:.4f}")
print(f"Var[X] = (b-a)²/12 = {(b-a)**2/12:.4f}")
print(f"Std[X] = {uniform.std(loc=a, scale=b-a):.4f}")

print(f"\nP(X ≤ 5)    = {uniform.cdf(5, loc=a, scale=b-a):.4f}")
print(f"P(3 ≤ X ≤ 7)= {uniform.cdf(7,a,b-a)-uniform.cdf(3,a,b-a):.4f}")
print(f"Median      = {uniform.ppf(0.5, loc=a, scale=b-a):.4f}")

# Compare with simulation
np.random.seed(42)
samples = uniform.rvs(loc=a, scale=b-a, size=100_000)
print(f"\nSimulated mean = {samples.mean():.4f}  (exact: {(a+b)/2:.4f})")
print(f"Simulated std  = {samples.std():.4f}  (exact: {uniform.std(a,b-a):.4f})")

# Visualise PDF + CDF
fig, axes = plt.subplots(1, 2, figsize=(13, 4))
x = np.linspace(0, 12, 400)

axes[0].plot(x, uniform.pdf(x, a, b-a), color='steelblue', linewidth=3)
axes[0].fill_between(x, uniform.pdf(x, a, b-a), alpha=0.3, color='steelblue')
# Shade P(3 ≤ X ≤ 7)
mask = (x>=3) & (x<=7)
axes[0].fill_between(x[mask], uniform.pdf(x[mask],a,b-a), alpha=0.6,
                     color='gold', label='P(3≤X≤7)')
axes[0].set_title(f"Uniform PDF [a={a}, b={b}]")
axes[0].set_xlabel("x"); axes[0].set_ylabel("f(x)")
axes[0].legend()

axes[1].plot(x, uniform.cdf(x, a, b-a), color='darkorange', linewidth=2.5)
axes[1].set_title(f"Uniform CDF [a={a}, b={b}]")
axes[1].set_xlabel("x"); axes[1].set_ylabel("F(x) = P(X ≤ x)")

plt.tight_layout()
plt.show()
```

---

### 8.2 Normal (Gaussian) Distribution

**Intuition:** The most important distribution in statistics. Appears naturally when many independent effects add together (Central Limit Theorem).

```
f(x) = (1/σ√2π) × exp(−(x−μ)²/2σ²)
E[X] = μ       Var[X] = σ²

Empirical Rule:
  P(μ−1σ ≤ X ≤ μ+1σ) ≈ 68.27%
  P(μ−2σ ≤ X ≤ μ+2σ) ≈ 95.45%
  P(μ−3σ ≤ X ≤ μ+3σ) ≈ 99.73%
```

```python
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu, sigma = 170, 10   # human heights in cm

print("=== Normal(μ=170, σ=10) ===")
print(f"E[X]   = {norm.mean(mu, sigma):.2f} cm")
print(f"Var[X] = {norm.var(mu, sigma):.2f}")
print(f"Std[X] = {norm.std(mu, sigma):.2f} cm")

print(f"\nP(X ≤ 170)      = {norm.cdf(170, mu, sigma):.4f}  (median = mean for Normal)")
print(f"P(X > 185)      = {norm.sf(185, mu, sigma):.4f}")
print(f"P(160≤X≤180)    = {norm.cdf(180,mu,sigma)-norm.cdf(160,mu,sigma):.4f}")
print(f"P(μ±1σ)         = {norm.cdf(mu+sigma,mu,sigma)-norm.cdf(mu-sigma,mu,sigma):.5f}")
print(f"P(μ±2σ)         = {norm.cdf(mu+2*sigma,mu,sigma)-norm.cdf(mu-2*sigma,mu,sigma):.5f}")
print(f"P(μ±3σ)         = {norm.cdf(mu+3*sigma,mu,sigma)-norm.cdf(mu-3*sigma,mu,sigma):.5f}")

print(f"\nPercentiles:")
for q in [0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]:
    print(f"  {int(q*100):2d}th = {norm.ppf(q, mu, sigma):.2f} cm")

# 95% confidence interval
lo, hi = norm.interval(0.95, loc=mu, scale=sigma)
print(f"\n95% interval: [{lo:.2f}, {hi:.2f}] cm")

# ── Full visualisation ────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 9))
x = np.linspace(130, 210, 400)
pdf_vals = norm.pdf(x, mu, sigma)

# 1: PDF with empirical rule
axes[0,0].plot(x, pdf_vals, color='steelblue', linewidth=2.5)
colors = ['gold','orange','tomato']
for k, color in zip([1, 2, 3], colors):
    lo_k = mu - k*sigma; hi_k = mu + k*sigma
    mask = (x>=lo_k) & (x<=hi_k)
    p = norm.cdf(hi_k,mu,sigma)-norm.cdf(lo_k,mu,sigma)
    axes[0,0].fill_between(x[mask], pdf_vals[mask], alpha=0.4,
                            color=color, label=f'±{k}σ ({p*100:.1f}%)')
axes[0,0].axvline(mu, color='black', linestyle='--', linewidth=1.5, label=f'μ={mu}')
axes[0,0].set_title("Normal PDF — Empirical Rule")
axes[0,0].set_xlabel("Height (cm)"); axes[0,0].set_ylabel("f(x)")
axes[0,0].legend(fontsize=8)

# 2: CDF
axes[0,1].plot(x, norm.cdf(x, mu, sigma), color='darkorange', linewidth=2.5)
for q, color in zip([0.25,0.5,0.75],['gray','red','gray']):
    val = norm.ppf(q, mu, sigma)
    axes[0,1].axhline(q, color=color, linestyle=':', alpha=0.7)
    axes[0,1].axvline(val, color=color, linestyle=':', alpha=0.7)
axes[0,1].set_title("Normal CDF"); axes[0,1].set_xlabel("Height (cm)")
axes[0,1].set_ylabel("P(X ≤ x)")

# 3: Multiple Normal curves
for m, s, color in [(160,5,'steelblue'),(170,10,'darkorange'),(170,20,'seagreen')]:
    axes[1,0].plot(x, norm.pdf(x,m,s), linewidth=2.5, color=color,
                   label=f'μ={m}, σ={s}')
axes[1,0].set_title("Effect of μ and σ on Normal PDF")
axes[1,0].set_xlabel("x"); axes[1,0].set_ylabel("f(x)"); axes[1,0].legend()

# 4: QQ-plot (normality check)
np.random.seed(42)
sim = norm.rvs(mu, sigma, size=500)
from scipy.stats import probplot
res = probplot(sim, dist='norm', plot=axes[1,1])
axes[1,1].set_title("QQ-Plot — Checking Normality (straight line = Normal)")

plt.suptitle("Normal (Gaussian) Distribution — Complete Reference", fontsize=14,
             fontweight='bold', y=1.01)
plt.tight_layout()
plt.show()

# ── Z-score standardisation ───────────────────────────────────────────────────
print("\n=== Z-Score Standardisation ===")
# Any Normal → Standard Normal via Z = (X - μ) / σ
x_val = 185
z     = (x_val - mu) / sigma
print(f"X={x_val}cm → Z = ({x_val}-{mu})/{sigma} = {z:.2f}")
print(f"P(X ≤ 185) using Normal({mu},{sigma}) = {norm.cdf(x_val,mu,sigma):.4f}")
print(f"P(Z ≤ {z:.2f}) using Standard Normal  = {norm.cdf(z,0,1):.4f}  ← same ✓")
```

---

### 8.3 Exponential Distribution

**Intuition:** Waiting time between consecutive events in a Poisson process. If λ events occur per unit time, waiting time follows Exp(λ).

```
f(x) = λe⁻λˣ        x ≥ 0
F(x) = 1 − e⁻λˣ
E[X] = 1/λ           Var[X] = 1/λ²

MEMORYLESS PROPERTY:
P(X > s+t | X > s) = P(X > t)
"The past gives no information about the future"
```

```python
from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

lam   = 0.5          # rate: 0.5 events per minute
scale = 1 / lam      # SciPy parameterises by scale = 1/λ

print(f"=== Exponential(λ={lam}) — scale={scale} ===")
print(f"E[X]   = 1/λ = {1/lam:.4f} minutes")
print(f"Var[X] = 1/λ² = {1/lam**2:.4f}")
print(f"Std[X] = 1/λ = {1/lam:.4f}")
print(f"Median = ln(2)/λ = {np.log(2)/lam:.4f}")

print(f"\nP(X ≤ 2)   = {expon.cdf(2, scale=scale):.4f}")
print(f"P(X > 5)   = {expon.sf(5, scale=scale):.4f}   (sf = 1-cdf)")
print(f"P(1≤X≤4)   = {expon.cdf(4,scale=scale)-expon.cdf(1,scale=scale):.4f}")
print(f"90th pct   = {expon.ppf(0.90, scale=scale):.4f} minutes")

# Memoryless property
s, t = 3, 2
p1 = expon.sf(s+t, scale=scale) / expon.sf(s, scale=scale)   # P(X>s+t | X>s)
p2 = expon.sf(t, scale=scale)                                  # P(X>t)
print(f"\n=== Memoryless Property ===")
print(f"P(X>{s+t} | X>{s}) = {p1:.6f}")
print(f"P(X>{t})           = {p2:.6f}   ← identical ✓")

# ── Visualisation ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 4))
x = np.linspace(0, 14, 400)

# Multiple lambda values
for l, color in zip([0.3, 0.5, 1.0, 2.0], ['steelblue','darkorange','seagreen','purple']):
    s_ = 1/l
    axes[0].plot(x, expon.pdf(x, scale=s_), linewidth=2.5, color=color,
                 label=f'λ={l} (mean={s_:.1f})')
axes[0].set_title("Exponential PDF for Different λ")
axes[0].set_xlabel("x (time)"); axes[0].set_ylabel("f(x)")
axes[0].set_ylim(0, 2.1); axes[0].legend()

# PDF + shaded region
axes[1].plot(x, expon.pdf(x, scale=scale), color='steelblue', linewidth=2.5)
mask = x <= 2
axes[1].fill_between(x[mask], expon.pdf(x[mask],scale=scale),
                     alpha=0.5, color='gold', label=f'P(X≤2)={expon.cdf(2,scale=scale):.3f}')
axes[1].axvline(1/lam, color='red', linestyle='--', label=f'Mean={1/lam:.0f}')
axes[1].set_title(f"Exponential PDF (λ={lam})")
axes[1].set_xlabel("x (time)"); axes[1].set_ylabel("f(x)"); axes[1].legend()

plt.tight_layout()
plt.show()
```

---

### 8.4 Gamma Distribution

**Intuition:** Waiting time until the k-th event in a Poisson process. Generalization of Exponential (k=1).

```
f(x) = x^(α-1) × e^(-x/β) / [β^α × Γ(α)]
E[X] = αβ       Var[X] = αβ²
```

```python
from scipy.stats import gamma
import numpy as np
import matplotlib.pyplot as plt

print("=== Gamma Distribution ===")
# α = shape, β = scale (= 1/rate)
for a, b in [(1,2),(2,2),(5,1),(9,0.5)]:
    print(f"Gamma(α={a}, β={b}): E[X]={a*b:.2f}, Var={a*b**2:.2f}, Std={np.sqrt(a*b**2):.2f}")

x = np.linspace(0, 25, 400)
plt.figure(figsize=(9, 4))
for (a, b), color in zip([(1,2),(2,2),(5,1),(9,0.5)],
                          ['steelblue','darkorange','seagreen','purple']):
    plt.plot(x, gamma.pdf(x, a, scale=b), linewidth=2.5, color=color,
             label=f'α={a}, β={b}  E={a*b}')
plt.title("Gamma Distribution PDF")
plt.xlabel("x"); plt.ylabel("f(x)")
plt.legend()
plt.tight_layout()
plt.show()
```

---

### 8.5 Beta Distribution

**Intuition:** Distribution over probabilities — values always in [0,1]. Perfect as a prior in Bayesian analysis when the parameter itself is a probability.

```
f(x) = x^(α-1) × (1-x)^(β-1) / B(α,β)     0 ≤ x ≤ 1
E[X] = α/(α+β)       Var[X] = αβ / [(α+β)²(α+β+1)]
```

```python
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

print("=== Beta Distribution ===")
for a, b in [(1,1),(2,5),(5,2),(2,2),(0.5,0.5)]:
    print(f"Beta(α={a}, β={b}): E[X]={a/(a+b):.4f}, Var={a*b/((a+b)**2*(a+b+1)):.5f}")

x = np.linspace(0.001, 0.999, 400)
plt.figure(figsize=(9, 4))
configs = [(1,1,'Uniform'),(2,5,'Left-skewed'),(5,2,'Right-skewed'),
           (2,2,'Symmetric bell'),(0.5,0.5,'U-shaped')]
colors = ['gray','steelblue','darkorange','seagreen','purple']
for (a, b, label), color in zip(configs, colors):
    plt.plot(x, beta.pdf(x, a, b), linewidth=2.5, color=color,
             label=f'α={a}, β={b} ({label})')
plt.title("Beta Distribution PDF — Modeling Probabilities")
plt.xlabel("x ∈ [0, 1]  (represents a probability)")
plt.ylabel("f(x)")
plt.legend(fontsize=8)
plt.tight_layout()
plt.show()

# ML use: Bayesian A/B testing
print("\n=== Bayesian A/B Test with Beta ===")
# Prior: Beta(1,1) = Uniform (no prior knowledge)
# Variant A: 47 successes, 153 failures → Beta(48, 154)
# Variant B: 56 successes, 144 failures → Beta(57, 145)
np.random.seed(42)
samples_a = beta.rvs(48, 154, size=100_000)
samples_b = beta.rvs(57, 145, size=100_000)
p_b_better = np.mean(samples_b > samples_a)
print(f"Variant A: 47/200 = {47/200:.3f} conversion rate")
print(f"Variant B: 56/200 = {56/200:.3f} conversion rate")
print(f"P(B > A)  = {p_b_better:.4f}  ({p_b_better*100:.1f}% probability B is better)")
```

---

# ═══════════════════════════════════════════════
# PART 4 · SIMULATION & VISUALIZATION
# ═══════════════════════════════════════════════

---

## 9. 🎲 Monte Carlo Simulation

### 9.1 Core Concept

Monte Carlo methods estimate quantities by:
1. Defining a domain and probability model
2. Generating random samples from that model
3. Computing the desired quantity from the samples

```
Estimate = (samples satisfying condition) / (total samples)
Error ≈ 1/√n   →  10× more samples gives 3× better accuracy
```

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# EXAMPLE 1: Estimating π
# ─────────────────────────────────────────────────────────────────────────────
def estimate_pi(n: int, seed: int = 42) -> tuple:
    np.random.seed(seed)
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    inside = (x**2 + y**2) <= 1
    return 4 * inside.mean(), x, y, inside

# Convergence analysis
print("=== Monte Carlo: Estimating π ===")
print(f"{'Samples':>10} | {'π Estimate':>12} | {'Abs Error':>12} | {'% Error':>10}")
print("-" * 52)
for n in [100, 1000, 10_000, 100_000, 1_000_000]:
    pi_est, *_ = estimate_pi(n)
    err = abs(pi_est - np.pi)
    print(f"{n:>10,} | {pi_est:>12.6f} | {err:>12.6f} | {err/np.pi*100:>9.4f}%")

# Visualise
pi_est, x, y, inside = estimate_pi(5_000)
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].scatter(x[inside],  y[inside],  s=2, color='steelblue', alpha=0.6, label='Inside')
axes[0].scatter(x[~inside], y[~inside], s=2, color='salmon',    alpha=0.6, label='Outside')
circle = plt.Circle((0,0),1,fill=False,color='black',linewidth=2)
axes[0].add_patch(circle)
axes[0].set_aspect('equal')
axes[0].set_title(f"Monte Carlo π ≈ {pi_est:.5f}  (true: {np.pi:.5f})")
axes[0].legend(markerscale=8)

# Running estimate
ns = np.arange(100, 100_001, 100)
pi_ests = [estimate_pi(n)[0] for n in ns]
axes[1].plot(ns, pi_ests, color='steelblue', linewidth=1, alpha=0.8)
axes[1].axhline(np.pi, color='red', linewidth=2, linestyle='--', label=f'True π={np.pi:.5f}')
axes[1].fill_between(ns, np.pi-0.05, np.pi+0.05, alpha=0.1, color='red')
axes[1].set_title("Convergence of π Estimate")
axes[1].set_xlabel("Number of Samples"); axes[1].set_ylabel("Estimated π")
axes[1].legend()
plt.tight_layout(); plt.show()
```

```python
# ─────────────────────────────────────────────────────────────────────────────
# EXAMPLE 2: Birthday Paradox
# ─────────────────────────────────────────────────────────────────────────────
def birthday_prob(n_people: int, n_sim: int = 50_000) -> float:
    birthdays = np.random.randint(1, 366, size=(n_sim, n_people))
    # Count rows where any birthday is repeated
    matches = np.array([len(set(row)) < n_people for row in birthdays])
    return matches.mean()

print("\n=== Birthday Paradox ===")
print(f"{'Group Size':>11} | {'P(shared birthday)':>20} | {'Note':}")
print("-" * 55)
for n in [5, 10, 15, 20, 23, 30, 40, 50, 60]:
    p = birthday_prob(n, n_sim=30_000)
    print(f"{n:>11} | {p:>20.4f} | {'← first > 50%!' if 0.50 <= p < 0.55 else ''}")

# ─────────────────────────────────────────────────────────────────────────────
# EXAMPLE 3: Monty Hall Problem
# ─────────────────────────────────────────────────────────────────────────────
def monty_hall(n_games: int, switch: bool) -> float:
    np.random.seed(42)
    car_door      = np.random.randint(1, 4, n_games)
    chosen_door   = np.random.randint(1, 4, n_games)

    wins = 0
    for i in range(n_games):
        if switch:
            # Switching: wins if original choice was WRONG
            wins += (car_door[i] != chosen_door[i])
        else:
            # Staying: wins if original choice was RIGHT
            wins += (car_door[i] == chosen_door[i])
    return wins / n_games

n = 100_000
print(f"\n=== Monty Hall Problem (n={n:,}) ===")
print(f"P(win | STAY)   = {monty_hall(n, switch=False):.5f}  (exact: 1/3 = {1/3:.5f})")
print(f"P(win | SWITCH) = {monty_hall(n, switch=True):.5f}  (exact: 2/3 = {2/3:.5f})")

# ─────────────────────────────────────────────────────────────────────────────
# EXAMPLE 4: Monte Carlo Integration
# ─────────────────────────────────────────────────────────────────────────────
from scipy import integrate

def monte_carlo_integrate(f, a, b, n=100_000):
    """Estimate ∫_a^b f(x)dx using Monte Carlo."""
    x = np.random.uniform(a, b, n)
    return (b - a) * np.mean(f(x))

# Estimate ∫₀¹ x² dx = 1/3 ≈ 0.3333
f = lambda x: x**2
mc_result  = monte_carlo_integrate(f, 0, 1)
sci_result = integrate.quad(f, 0, 1)[0]
print(f"\n=== Monte Carlo Integration: ∫₀¹ x² dx ===")
print(f"Monte Carlo result = {mc_result:.6f}")
print(f"SciPy quad result  = {sci_result:.6f}")
print(f"Exact result       = {1/3:.6f}")

# ─────────────────────────────────────────────────────────────────────────────
# EXAMPLE 5: Portfolio Risk Simulation (Finance)
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Portfolio Risk — Monte Carlo ===")
np.random.seed(42)
n_sims    = 100_000
n_days    = 252       # trading days in a year

initial   = 100_000   # starting portfolio value
mu_daily  = 0.0005    # daily expected return (≈12.6% annual)
sigma_day = 0.012     # daily volatility

# Simulate daily returns
daily_returns = np.random.normal(mu_daily, sigma_day, (n_sims, n_days))
portfolio_paths = initial * np.cumprod(1 + daily_returns, axis=1)

final_values = portfolio_paths[:, -1]
print(f"Starting value      : ${initial:,.0f}")
print(f"Expected final value: ${final_values.mean():,.0f}")
print(f"Median final value  : ${np.median(final_values):,.0f}")
print(f"5th percentile (VaR): ${np.percentile(final_values, 5):,.0f}")
print(f"P(loss > 20%)       : {np.mean(final_values < 0.8 * initial):.4f}")
print(f"P(gain > 30%)       : {np.mean(final_values > 1.3 * initial):.4f}")
```

---

## 10. 📊 Visualization of Probability

### 10.1 Histograms — The Foundation

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, expon

np.random.seed(42)
data = norm.rvs(loc=50, scale=10, size=2_000)

fig, axes = plt.subplots(2, 3, figsize=(16, 9))

# 1: Basic histogram
axes[0,0].hist(data, bins=30, color='steelblue', edgecolor='white', alpha=0.85)
axes[0,0].set_title("Basic Histogram (counts)")
axes[0,0].set_xlabel("Value"); axes[0,0].set_ylabel("Count")

# 2: Density histogram + PDF overlay
x_line = np.linspace(data.min()-5, data.max()+5, 300)
axes[0,1].hist(data, bins=30, density=True, color='steelblue',
               edgecolor='white', alpha=0.7)
axes[0,1].plot(x_line, norm.pdf(x_line, 50, 10), 'r-', linewidth=2.5, label='True PDF')
axes[0,1].set_title("Density Histogram + PDF Overlay")
axes[0,1].set_xlabel("Value"); axes[0,1].set_ylabel("Density")
axes[0,1].legend()

# 3: Seaborn histplot + KDE
sns.histplot(data, kde=True, stat='density', bins=30,
             color='darkorange', ax=axes[0,2])
axes[0,2].plot(x_line, norm.pdf(x_line, 50, 10), 'b--',
               linewidth=2, label='True PDF')
axes[0,2].set_title("Seaborn histplot with KDE")
axes[0,2].legend()

# 4: KDE only
sns.kdeplot(data, fill=True, color='seagreen', ax=axes[1,0], linewidth=2.5)
axes[1,0].set_title("KDE Plot (kernel density estimate)")
axes[1,0].set_xlabel("Value")

# 5: ECDF vs theoretical CDF
sns.ecdfplot(data, color='steelblue', linewidth=2, ax=axes[1,1], label='Empirical CDF')
axes[1,1].plot(x_line, norm.cdf(x_line, 50, 10), 'r--',
               linewidth=2, label='Theoretical CDF')
axes[1,1].set_title("ECDF vs Theoretical CDF")
axes[1,1].legend()

# 6: Multiple distributions comparison
data_a = norm.rvs(50, 10, 1000)
data_b = expon.rvs(scale=15, size=1000) + 30
for d, label, color in [(data_a,'Normal(50,10)','steelblue'),
                         (data_b,'Exponential','darkorange')]:
    sns.kdeplot(d, ax=axes[1,2], label=label, color=color, linewidth=2, fill=True, alpha=0.3)
axes[1,2].set_title("Comparing Two Distributions (KDE)")
axes[1,2].legend()

plt.suptitle("Probability Visualization — Matplotlib & Seaborn", fontsize=14,
             fontweight='bold', y=1.01)
plt.tight_layout()
plt.show()
```

### 10.2 Advanced Statistical Plots

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
np.random.seed(42)

# Generate multi-group dataset
n = 500
groups = pd.DataFrame({
    'Group A': norm.rvs(70, 10, n),
    'Group B': norm.rvs(75,  8, n),
    'Group C': norm.rvs(65, 15, n),
})

fig, axes = plt.subplots(2, 3, figsize=(16, 9))

# 1: Box plot
groups_melted = groups.melt(var_name='Group', value_name='Score')
sns.boxplot(data=groups_melted, x='Group', y='Score',
            palette=['steelblue','darkorange','seagreen'], ax=axes[0,0])
axes[0,0].set_title("Box Plot — Five-Number Summary")

# 2: Violin plot
sns.violinplot(data=groups_melted, x='Group', y='Score',
               palette=['steelblue','darkorange','seagreen'],
               inner='quartile', ax=axes[0,1])
axes[0,1].set_title("Violin Plot — Shape + Quartiles")

# 3: Strip + Box overlay
sns.boxplot(data=groups_melted, x='Group', y='Score',
            palette=['steelblue','darkorange','seagreen'],
            ax=axes[0,2], width=0.4, fliersize=0)
sns.stripplot(data=groups_melted, x='Group', y='Score',
              color='black', alpha=0.15, size=2, jitter=True, ax=axes[0,2])
axes[0,2].set_title("Box + Strip — All Data Points")

# 4: QQ Plot
data_test = norm.rvs(0, 1, 500)
stats.probplot(data_test, plot=axes[1,0])
axes[1,0].set_title("QQ-Plot: Normal data (straight line = Normal)")

data_exp = expon.rvs(scale=1, size=500)
stats.probplot(data_exp, plot=axes[1,1])
axes[1,1].set_title("QQ-Plot: Exponential data (curved = non-normal)")

# 5: Heatmap of correlation
corr_data = pd.DataFrame({
    'Math'   : norm.rvs(70, 10, n),
    'Physics': norm.rvs(65, 12, n),
})
corr_data['Eng']   = 0.8 * corr_data['Math'] + norm.rvs(0, 5, n)
corr_data['Bio']   = norm.rvs(60, 15, n)
corr_data['CS']    = 0.6 * corr_data['Math'] + 0.4 * corr_data['Eng'] + norm.rvs(0,5,n)
sns.heatmap(corr_data.corr(), annot=True, fmt='.3f', cmap='coolwarm',
            center=0, ax=axes[1,2], square=True)
axes[1,2].set_title("Correlation Heatmap")

plt.suptitle("Advanced Statistical Plots", fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.show()
```

---

# ═══════════════════════════════════════════════
# PART 5 · PROBABILITY IN STATISTICS & ML
# ═══════════════════════════════════════════════

---

## 11. 📐 Expectation & Variance

### 11.1 Full Mathematical Treatment

```python
import numpy as np
import pandas as pd
from scipy.stats import binom, poisson, norm, expon, uniform
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────────────────────
# DISCRETE EXPECTATION — computed manually from PMF
# ─────────────────────────────────────────────────────────────────────────────
print("=== E[X] from PMF — Manual Calculation ===")

# Die roll: E[X] = Σ x·P(x)
x_vals = np.array([1,2,3,4,5,6])
p_vals = np.array([1/6]*6)
E_die  = np.sum(x_vals * p_vals)
E2_die = np.sum(x_vals**2 * p_vals)   # E[X²]
Var_die = E2_die - E_die**2            # Var = E[X²] - (E[X])²
print(f"Die Roll: E[X] = {E_die:.4f}, E[X²] = {E2_die:.4f}, Var = {Var_die:.4f}")

# Custom distribution
x_custom = np.array([0, 1, 2, 3, 4])
p_custom = np.array([0.1, 0.25, 0.35, 0.20, 0.10])
print(f"Sum of probs = {p_custom.sum():.2f}  (must = 1)")

E_custom   = np.sum(x_custom * p_custom)
E2_custom  = np.sum(x_custom**2 * p_custom)
Var_custom = E2_custom - E_custom**2
Std_custom = np.sqrt(Var_custom)
print(f"Custom: E[X]={E_custom:.4f}, Var={Var_custom:.4f}, Std={Std_custom:.4f}")

# ─────────────────────────────────────────────────────────────────────────────
# USING SCIPY — distribution objects
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Distribution Statistics via SciPy ===")
distributions = [
    ("Binomial(n=15, p=0.4)",   binom,   (15, 0.4),  {}),
    ("Poisson(λ=7)",            poisson, (7,),         {}),
    ("Normal(μ=50, σ=10)",      norm,    (50, 10),     {}),
    ("Exponential(scale=3)",    expon,   (),            {'scale':3}),
    ("Uniform(a=2, b=12)",      uniform, (),            {'loc':2,'scale':10}),
]

print(f"{'Distribution':<25} {'Mean':>8} {'Var':>10} {'Std':>8} {'Median':>8}")
print("-" * 65)
for name, dist, args, kwargs in distributions:
    mean   = dist.mean(*args, **kwargs)
    var    = dist.var(*args, **kwargs)
    std    = dist.std(*args, **kwargs)
    median = dist.median(*args, **kwargs)
    print(f"{name:<25} {mean:>8.4f} {var:>10.4f} {std:>8.4f} {median:>8.4f}")

# ─────────────────────────────────────────────────────────────────────────────
# PROPERTIES OF EXPECTATION AND VARIANCE
# ─────────────────────────────────────────────────────────────────────────────
np.random.seed(42)
print("\n=== Properties of E[X] and Var(X) ===")
n_samp = 1_000_000
X = norm.rvs(loc=3, scale=2, size=n_samp)
Y = norm.rvs(loc=1, scale=1, size=n_samp)
a, b = 4, 5

# E[aX + b] = a·E[X] + b
exact_EX = 3
print(f"E[aX+b] analytical = {a*exact_EX + b:.4f}")
print(f"E[aX+b] simulated  = {np.mean(a*X + b):.4f}  ✓")

# Var(aX + b) = a²·Var(X)
exact_VarX = 4
print(f"Var(aX+b) analytical = {a**2 * exact_VarX:.4f}")
print(f"Var(aX+b) simulated  = {np.var(a*X + b):.4f}  ✓")

# E[X + Y] = E[X] + E[Y]  (always)
print(f"E[X+Y] analytical  = {3+1:.4f}")
print(f"E[X+Y] simulated   = {np.mean(X+Y):.4f}  ✓")

# Var(X+Y) = Var(X) + Var(Y)  ONLY if independent
print(f"Var(X+Y) analytical = {4+1:.4f}  (if independent)")
print(f"Var(X+Y) simulated  = {np.var(X+Y):.4f}  ✓")

# ─────────────────────────────────────────────────────────────────────────────
# LAW OF LARGE NUMBERS — simulation
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 4))
n_max = 10_000
samples = expon.rvs(scale=3, size=n_max)
running_mean = np.cumsum(samples) / np.arange(1, n_max+1)
true_mean    = expon.mean(scale=3)

axes[0].plot(running_mean, color='steelblue', linewidth=1.5)
axes[0].axhline(true_mean, color='red', linestyle='--', linewidth=2,
                label=f'True Mean = {true_mean}')
axes[0].set_xlabel("n"); axes[0].set_ylabel("Running Mean")
axes[0].set_title("LLN — Exponential(scale=3)")
axes[0].legend()

# Central Limit Theorem
n_per_sample  = 30
n_samples_clt = 10_000
pop = expon.rvs(scale=3, size=1_000_000)   # very skewed population
sample_means  = [pop[np.random.randint(0, len(pop), n_per_sample)].mean()
                 for _ in range(n_samples_clt)]

axes[1].hist(pop[:5_000], bins=50, density=True, alpha=0.5,
             color='darkorange', edgecolor='white', label='Population (Exp)')
axes[1].hist(sample_means, bins=50, density=True, alpha=0.7,
             color='steelblue', edgecolor='white', label=f'Sample Means (n={n_per_sample})')
mu_clt  = np.mean(sample_means)
std_clt = np.std(sample_means)
x_clt   = np.linspace(min(sample_means), max(sample_means), 300)
axes[1].plot(x_clt, norm.pdf(x_clt, mu_clt, std_clt), 'r-',
             linewidth=2.5, label='Normal Fit (CLT)')
axes[1].set_title("Central Limit Theorem — Skewed → Normal Sample Means")
axes[1].legend(fontsize=8); axes[1].set_xlim(0, 15)

plt.tight_layout()
plt.show()
```

---

## 12. 🧠 Likelihood & Log-Likelihood

### 12.1 Full MLE Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson
from scipy.optimize import minimize
from scipy.special import factorial

np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# WHAT IS LIKELIHOOD?
# ─────────────────────────────────────────────────────────────────────────────
print("=== Likelihood Intuition ===")
# Observed data: 3 heads in 10 flips
# Question: What value of p makes this most likely?
n_flips = 10; n_heads = 7

p_grid = np.linspace(0.01, 0.99, 500)
likelihood = binom.pmf(n_heads, n_flips, p_grid)
log_likelihood = binom.logpmf(n_heads, n_flips, p_grid)

mle_p = p_grid[np.argmax(likelihood)]
print(f"Observed: {n_heads} heads in {n_flips} flips")
print(f"MLE of p = {mle_p:.4f}  (exact: n_heads/n_flips = {n_heads/n_flips:.4f})")

fig, axes = plt.subplots(1, 2, figsize=(13, 4))
axes[0].plot(p_grid, likelihood, color='steelblue', linewidth=2.5)
axes[0].axvline(mle_p, color='red', linestyle='--', linewidth=2, label=f'MLE = {mle_p:.3f}')
axes[0].set_title(f"Likelihood: P({n_heads} heads in {n_flips} flips | p)")
axes[0].set_xlabel("p"); axes[0].set_ylabel("L(p)")
axes[0].legend()

axes[1].plot(p_grid, log_likelihood, color='darkorange', linewidth=2.5)
axes[1].axvline(mle_p, color='red', linestyle='--', linewidth=2, label=f'MLE = {mle_p:.3f}')
axes[1].set_title("Log-Likelihood (same optimum, better numerics)")
axes[1].set_xlabel("p"); axes[1].set_ylabel("log L(p)")
axes[1].legend()
plt.tight_layout(); plt.show()

# ─────────────────────────────────────────────────────────────────────────────
# MLE FOR NORMAL DISTRIBUTION — analytical + numerical
# ─────────────────────────────────────────────────────────────────────────────
true_mu, true_sigma = 5.0, 2.0
data = norm.rvs(true_mu, true_sigma, size=200)

def neg_log_likelihood_normal(params, data):
    mu, log_sigma = params
    sigma = np.exp(log_sigma)   # ensure sigma > 0
    return -np.sum(norm.logpdf(data, mu, sigma))

result = minimize(neg_log_likelihood_normal,
                  x0=[data.mean(), np.log(data.std())],
                  args=(data,), method='Nelder-Mead')
mle_mu_opt    = result.x[0]
mle_sigma_opt = np.exp(result.x[1])

print("\n=== MLE for Normal Distribution ===")
print(f"True parameters : μ={true_mu}, σ={true_sigma}")
print(f"Analytical MLE  : μ̂={data.mean():.4f}, σ̂={data.std():.4f}  (sample mean & std)")
print(f"Numerical MLE   : μ̂={mle_mu_opt:.4f}, σ̂={mle_sigma_opt:.4f}  ← scipy.optimize ✓")

# ─────────────────────────────────────────────────────────────────────────────
# LOG-LIKELIHOOD AS LOSS — CROSS-ENTROPY
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Cross-Entropy = Negative Log-Likelihood ===")

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def binary_cross_entropy(y_true, y_pred, eps=1e-12):
    y_pred = np.clip(y_pred, eps, 1-eps)
    return -np.mean(y_true * np.log(y_pred) + (1-y_true) * np.log(1-y_pred))

def negative_log_likelihood(y_true, y_pred, eps=1e-12):
    """Bernoulli NLL = binary cross-entropy. Identical."""
    y_pred = np.clip(y_pred, eps, 1-eps)
    log_lik = np.where(y_true==1, np.log(y_pred), np.log(1-y_pred))
    return -np.mean(log_lik)

np.random.seed(42)
y_true  = np.array([1,0,1,1,0,1,0,0,1,1])
y_pred  = np.array([0.9, 0.1, 0.8, 0.75, 0.25, 0.6, 0.4, 0.15, 0.85, 0.7])

bce = binary_cross_entropy(y_true, y_pred)
nll = negative_log_likelihood(y_true, y_pred)
print(f"Cross-Entropy  = {bce:.6f}")
print(f"Neg LL         = {nll:.6f}  ← identical! ✓")
print("\nConclusion: Cross-entropy loss IS negative log-likelihood of a Bernoulli model")
print("            Training a classifier = maximising likelihood of data")

# ─────────────────────────────────────────────────────────────────────────────
# 2D LIKELIHOOD SURFACE — Normal distribution
# ─────────────────────────────────────────────────────────────────────────────
mu_grid    = np.linspace(3, 7, 80)
sigma_grid = np.linspace(1, 4, 80)
MU, SIGMA  = np.meshgrid(mu_grid, sigma_grid)

LL = np.array([
    np.sum(norm.logpdf(data, mu, sigma))
    for mu, sigma in zip(MU.ravel(), SIGMA.ravel())
]).reshape(MU.shape)

fig, ax = plt.subplots(figsize=(8, 6))
cf = ax.contourf(MU, SIGMA, LL, levels=40, cmap='viridis')
plt.colorbar(cf, ax=ax, label='Log-Likelihood')
ax.plot(data.mean(), data.std(), 'r*', markersize=18, label=f'MLE: μ̂={data.mean():.2f}, σ̂={data.std():.2f}')
ax.plot(true_mu, true_sigma, 'w^', markersize=12, label=f'True: μ={true_mu}, σ={true_sigma}')
ax.set_xlabel("μ"); ax.set_ylabel("σ")
ax.set_title("Log-Likelihood Surface — Normal(μ, σ)")
ax.legend()
plt.tight_layout()
plt.show()
```

---

## 13. 🤖 Probability in Machine Learning

### 13.1 Probabilistic Predictions — Full Pipeline

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import expit   # sigmoid
from scipy.stats import norm

np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# SIGMOID — Binary classification output
# ─────────────────────────────────────────────────────────────────────────────
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z_vals = np.linspace(-8, 8, 400)
fig, axes = plt.subplots(1, 2, figsize=(13, 4))

axes[0].plot(z_vals, sigmoid(z_vals), color='steelblue', linewidth=2.5)
axes[0].axhline(0.5, color='red', linestyle='--', alpha=0.7, label='Decision boundary')
axes[0].axvline(0, color='gray', linestyle=':', alpha=0.7)
axes[0].fill_between(z_vals, sigmoid(z_vals),
                     where=sigmoid(z_vals) >= 0.5, alpha=0.15, color='steelblue',
                     label='Predict class 1')
axes[0].fill_between(z_vals, sigmoid(z_vals),
                     where=sigmoid(z_vals) < 0.5, alpha=0.15, color='salmon',
                     label='Predict class 0')
axes[0].set_title("Sigmoid Function — Logistic Regression Output")
axes[0].set_xlabel("z (linear combination Xw)"); axes[0].set_ylabel("P(Y=1 | X)")
axes[0].legend(fontsize=9)

# Show logit → probability mapping
logits = np.array([-4, -2, -1, 0, 1, 2, 4])
probs  = sigmoid(logits)
axes[1].bar(range(len(logits)), probs, color='steelblue', edgecolor='white', alpha=0.85)
axes[1].axhline(0.5, color='red', linestyle='--')
axes[1].set_xticks(range(len(logits)))
axes[1].set_xticklabels([f'z={z}' for z in logits], rotation=45, ha='right')
axes[1].set_ylabel("P(Y=1)")
axes[1].set_title("Logit → Probability via Sigmoid")
for i, (z, p) in enumerate(zip(logits, probs)):
    axes[1].text(i, p+0.02, f'{p:.3f}', ha='center', fontsize=9)

plt.tight_layout(); plt.show()

# ─────────────────────────────────────────────────────────────────────────────
# SOFTMAX — Multiclass classification
# ─────────────────────────────────────────────────────────────────────────────
def softmax(z):
    """Numerically stable softmax."""
    exp_z = np.exp(z - np.max(z))
    return exp_z / exp_z.sum()

# Neural network output for 5 classes
logits_mc = np.array([3.2, 1.5, -0.8, 0.2, -1.1])
probs_mc  = softmax(logits_mc)
classes   = ['Cat','Dog','Bird','Fish','Rabbit']

print("=== Softmax — 5-Class Output ===")
print(f"{'Class':<10} {'Logit':>8} {'P(class)':>10} {'Bar'}")
print("-" * 50)
for cls, logit, prob in zip(classes, logits_mc, probs_mc):
    bar = '█' * int(prob * 50)
    print(f"{cls:<10} {logit:>8.2f} {prob:>10.4f}  {bar}")
print(f"{'Sum':>20} {probs_mc.sum():>10.6f}  (always 1.0)")

# Temperature scaling — calibration of softmax
print("\n=== Temperature Scaling ===")
T_vals = [0.1, 0.5, 1.0, 2.0, 5.0]
print(f"{'Temperature':>12} | {'Cat':>8} {'Dog':>8} {'Bird':>8} → Behaviour")
print("-" * 60)
for T in T_vals:
    p = softmax(logits_mc / T)
    behaviour = ('Very confident' if T < 0.5 else
                 'Confident'     if T == 1.0 else
                 'Smooth'        if T < 3.0 else 'Uniform')
    print(f"{T:>12.1f} | {p[0]:>8.4f} {p[1]:>8.4f} {p[2]:>8.4f}  → {behaviour}")

# ─────────────────────────────────────────────────────────────────────────────
# LOGISTIC REGRESSION — gradient descent with probability outputs
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Logistic Regression from Scratch ===")
np.random.seed(42)

# Generate binary classification data
n = 500
X = np.random.randn(n, 2)
y = ((X[:, 0] + X[:, 1]) > 0.5).astype(float)

# Add bias column
X_b = np.column_stack([np.ones(n), X])

# Gradient Descent
w     = np.zeros(X_b.shape[1])
lr    = 0.1
losses = []

for epoch in range(500):
    z     = X_b @ w
    p     = sigmoid(z)
    error = p - y
    grad  = X_b.T @ error / n
    w    -= lr * grad

    # NLL loss
    eps  = 1e-12
    p_c  = np.clip(p, eps, 1-eps)
    loss = -np.mean(y * np.log(p_c) + (1-y) * np.log(1-p_c))
    losses.append(loss)

p_final  = sigmoid(X_b @ w)
acc      = np.mean((p_final >= 0.5) == y)
print(f"Final weights: w={w.round(4)}")
print(f"Training accuracy: {acc:.4f}")
print(f"Final loss (BCE): {losses[-1]:.6f}")

# ─────────────────────────────────────────────────────────────────────────────
# CALIBRATION — Are probabilities trustworthy?
# ─────────────────────────────────────────────────────────────────────────────
print("\n=== Probability Calibration ===")
np.random.seed(42)
n = 10_000

y_true       = np.random.binomial(1, 0.4, n)
y_well       = np.clip(0.4 + 0.2*np.random.randn(n), 0.01, 0.99)
y_overconf   = np.clip(np.power(y_well, 0.3), 0.01, 0.99)
y_underconf  = np.clip(0.3 + 0.4*y_well, 0.01, 0.99)

from sklearn.calibration import calibration_curve
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot([0,1],[0,1],'k--', linewidth=1.5, label='Perfect calibration')
for y_pred, label, color in [(y_well,'Well-calibrated','steelblue'),
                               (y_overconf,'Overconfident','salmon'),
                               (y_underconf,'Underconfident','seagreen')]:
    frac, mean_pred = calibration_curve(y_true, y_pred, n_bins=10)
    ax.plot(mean_pred, frac, 's-', color=color, linewidth=2, markersize=7, label=label)
ax.set_xlabel("Mean Predicted Probability")
ax.set_ylabel("Fraction of Positives (Actual)")
ax.set_title("Calibration Curve — Trust Your Model's Probabilities?")
ax.legend()
plt.tight_layout(); plt.show()
```

---

# ═══════════════════════════════════════════════
# PART 6 · BEST PRACTICES & REVISION
# ═══════════════════════════════════════════════

---

## 14. ⚠️ Common Mistakes

### Mistake 1 — Prosecutor's Fallacy: Confusing P(A|B) with P(B|A)

```python
import numpy as np
np.random.seed(42)

print("=== MISTAKE 1: Prosecutor's Fallacy ===")
print("P(evidence | innocent) ≠ P(innocent | evidence)")
print()

# DNA evidence example
p_innocent       = 0.9999   # 1 in 10,000 is guilty
p_dna_match_inno = 0.00001  # false positive rate
p_dna_match_guil = 0.9999   # true positive rate
p_guilty         = 1 - p_innocent

# Total probability of DNA match
p_match = p_dna_match_inno * p_innocent + p_dna_match_guil * p_guilty

# What prosecutor (WRONGLY) claims: P(DNA match | innocent) = 0.001%
# What actually matters: P(innocent | DNA match)
p_innocent_given_match = (p_dna_match_inno * p_innocent) / p_match

print(f"P(DNA match | innocent) = {p_dna_match_inno:.5f}  ← what prosecutor says")
print(f"P(innocent | DNA match) = {p_innocent_given_match:.4f}  ← what actually matters")
print(f"\n⚠️  Prosecutor says '1 in 100,000 chance of innocence'")
print(f"   Reality: {p_innocent_given_match*100:.1f}% chance of innocence after DNA match!")
print(f"   Because only {p_guilty*100:.4f}% of population is guilty (base rate)")
```

### Mistake 2 — Ignoring Base Rates

```python
print("\n=== MISTAKE 2: Ignoring Base Rate ===")
# Same test (95% sensitive, 5% FPR), different prevalences
from scipy.stats import norm

for prevalence in [0.001, 0.01, 0.05, 0.1, 0.3, 0.5]:
    p_pos = 0.95 * prevalence + 0.05 * (1-prevalence)
    posterior = (0.95 * prevalence) / p_pos
    print(f"Prevalence={prevalence:.3f}  →  P(sick|+)={posterior:.4f}  ({posterior*100:.1f}%)")

print("\n⚠️  Even with 95% accurate test: at 0.1% prevalence, only 1.87% truly sick!")
```

### Mistake 3 — Gambler's Fallacy

```python
print("\n=== MISTAKE 3: Gambler's Fallacy ===")
np.random.seed(42)
n = 1_000_000
flips = np.random.choice([0,1], n)  # 0=T, 1=H

# After k consecutive heads, what is P(next=Heads)?
for k in [3, 5, 7, 10]:
    indices = []
    for i in range(k, n):
        if all(flips[i-k:i] == 1):
            indices.append(i)
    if indices:
        p_next = np.mean(flips[indices])
        print(f"After {k} consecutive Heads: P(next=H) = {p_next:.4f}  ← always ≈ 0.5!")
print("Each flip is INDEPENDENT. Past outcomes give ZERO information about future.")
```

### Mistake 4 — Small Sample Over-Confidence

```python
import numpy as np
import matplotlib.pyplot as plt

print("\n=== MISTAKE 4: Small Sample Estimation ===")
np.random.seed(42)
true_p = 0.3   # true probability

print(f"{'n':>8} | {'Estimate':>10} | {'95% CI Width':>14} | {'Error':>8}")
print("-" * 48)
for n in [10, 30, 100, 500, 2000, 10000]:
    samples = np.random.binomial(1, true_p, n)
    p_hat   = samples.mean()
    ci_half = 1.96 * np.sqrt(p_hat*(1-p_hat)/n)   # Wilson CI approx
    error   = abs(p_hat - true_p)
    print(f"{n:>8,} | {p_hat:>10.4f} | {2*ci_half:>14.4f} | {error:>8.5f}")
```

### Mistake 5 — Assuming Independence

```python
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

print("\n=== MISTAKE 5: Assuming Independence Without Testing ===")
np.random.seed(42)
n = 10_000

# Scenario: Temperature and Ice Cream Sales — CORRELATED
temperature  = np.random.normal(25, 5, n)
ice_cream    = 0.8 * temperature + np.random.normal(0, 3, n)

# Wrong: P(high temp ∩ high sales) = P(high temp) × P(high sales)
hi_temp  = (temperature > 27).astype(int)
hi_sales = (ice_cream > 25).astype(int)

p_HT  = hi_temp.mean()
p_HS  = hi_sales.mean()
p_ind = p_HT * p_HS   # assumes independence
p_act = ((hi_temp==1)&(hi_sales==1)).mean()   # actual joint probability

print(f"P(high temp)            = {p_HT:.4f}")
print(f"P(high sales)           = {p_HS:.4f}")
print(f"P(HT)×P(HS) [WRONG]     = {p_ind:.4f}  ← assumes independence")
print(f"P(HT ∩ HS)  [ACTUAL]    = {p_act:.4f}  ← much higher!")
print(f"Difference              = {abs(p_act-p_ind):.4f}")

ct   = pd.crosstab(hi_temp, hi_sales)
chi2, pval, _, _ = chi2_contingency(ct)
print(f"\nChi² independence test: p-value = {pval:.2e}")
print(f"{'DEPENDENT' if pval < 0.05 else 'INDEPENDENT'} — {'reject' if pval<0.05 else 'fail to reject'} independence")
```

---

## 15. ✅ Best Practices

### 15.1 When to Simulate vs Calculate

```python
import numpy as np
from scipy.stats import binom, norm
import time

print("=== Simulate vs Calculate — Decision Guide ===\n")

# RULE 1: Simple closed-form → Calculate (faster, exact)
start = time.time()
p_exact = binom.cdf(15, 30, 0.4)
t_calc = time.time() - start
print(f"Calculation: P(X≤15) = {p_exact:.8f}  Time: {t_calc*1000:.4f}ms")

start = time.time()
samples = np.random.binomial(30, 0.4, 1_000_000)
p_sim   = np.mean(samples <= 15)
t_sim   = time.time() - start
print(f"Simulation:  P(X≤15) ≈ {p_sim:.8f}  Time: {t_sim*1000:.1f}ms")
print(f"Simulation is {t_sim/t_calc:.0f}× slower for this simple query → USE FORMULA\n")

# RULE 2: Complex distributions → Simulate
print("COMPLEX PROBLEM: P(max of 3 dice > 5)")
# Formula: P(max > 5) = 1 - P(max ≤ 5) = 1 - (5/6)^3
p_formula = 1 - (5/6)**3
# Simulation
dice   = np.random.randint(1, 7, (500_000, 3))
p_sim2 = np.mean(dice.max(axis=1) > 5)
print(f"Formula: {p_formula:.6f}   Simulation: {p_sim2:.6f}  ← easy here too")

print("\nBUT for VERY complex problems, simulation is the ONLY practical option:")
print("  - Correlated multi-variable systems")
print("  - Option pricing under stochastic volatility")
print("  - Epidemiological models (SIR)")
print("  - Any problem where the PDF has no closed form")
```

### 15.2 Choosing the Right Distribution

```python
import numpy as np
import pandas as pd
from scipy.stats import (bernoulli, binom, poisson, geom,
                         norm, expon, gamma, beta, uniform)
import matplotlib.pyplot as plt
import seaborn as sns

print("=== Distribution Selection Guide ===\n")

guide = pd.DataFrame({
    'Question'      : [
        'Single binary trial?',
        'n independent binary trials?',
        'Events in fixed time/space?',
        'Trials until first success?',
        'Count: Var >> Mean?',
        'All values equally likely?',
        'Sum of many iid effects?',
        'Waiting time between events?',
        'Sum of k Exponential RVs?',
        'Parameter is a probability?',
    ],
    'Distribution'  : [
        'Bernoulli(p)',
        'Binomial(n,p)',
        'Poisson(λ)',
        'Geometric(p)',
        'Negative Binomial',
        'Uniform(a,b)',
        'Normal(μ,σ)',
        'Exponential(λ)',
        'Gamma(k,θ)',
        'Beta(α,β)',
    ],
    'Key Params'    : [
        'p = P(success)',
        'n = trials, p = P(success)',
        'λ = average rate',
        'p = P(success)',
        'r = # successes, p = prob',
        'a = min, b = max',
        'μ = mean, σ = std dev',
        'λ = rate (1/mean)',
        'k = shape, θ = scale',
        'α,β > 0 (shape params)',
    ],
    'ML Use Case'   : [
        'Binary output neuron',
        'Binomial loss, A/B test',
        'Count data regression',
        'Sequence modelling',
        'Over-dispersed counts',
        'Initial weight range',
        'Feature distribution',
        'Survival/time models',
        'Bayesian waiting times',
        'Beta-Bernoulli model',
    ]
})
print(guide.to_string(index=False))

# Goodness-of-fit test to identify distribution
print("\n=== Goodness-of-Fit Testing ===")
np.random.seed(42)
# Generate mystery data
mystery = np.random.poisson(lam=4, size=1_000)
mystery_mean = mystery.mean()
mystery_var  = mystery.var()
ratio = mystery_var / mystery_mean

print(f"Mystery data: mean={mystery_mean:.3f}, var={mystery_var:.3f}")
print(f"Var/Mean ratio = {ratio:.3f}")
if ratio < 1.2:
    print("→ Likely Poisson (Var ≈ Mean)")
elif ratio < 2.0:
    print("→ Possible Binomial or slight overdispersion")
else:
    print("→ Likely Negative Binomial (overdispersed)")
```

### 15.3 Reproducibility Checklist

```python
import numpy as np
import pandas as pd

print("=== Reproducibility Best Practices ===\n")

checklist = {
    "Practice"                          : [
        "Set random seed at start",
        "Use np.random.Generator (new API)",
        "Record library versions",
        "Separate train/test splits deterministically",
        "Log all random states in experiments",
        "Avoid global state mutations",
        "Use scipy distribution objects (not manual)",
        "Vectorise: avoid Python loops for probability",
        "Clip probabilities before log",
        "Test simulation with known analytical results",
    ],
    "Example / Code"                    : [
        "np.random.seed(42)",
        "rng = np.random.default_rng(42)",
        "np.__version__, scipy.__version__",
        "from sklearn.model_selection import train_test_split",
        "mlflow.log_param('seed', 42)",
        "Use function scope, not global variables",
        "norm.cdf(x, mu, sigma) not manual integration",
        "np.mean(data > 0) not sum([x>0 for x in data])/n",
        "np.clip(p, 1e-12, 1-1e-12)",
        "estimate_pi(n) vs np.pi",
    ]
}
df_check = pd.DataFrame(checklist)
for _, row in df_check.iterrows():
    print(f"  ✅ {row['Practice']:<45}  {row['Example / Code']}")
```

---

## 16. 📘 Quick Probability Cheat Sheet

### 16.1 Core Formulas

```python
print("""
╔══════════════════════════════════════════════════════════════════════════╗
║           PROBABILITY QUICK REFERENCE — FORMULAS                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  FUNDAMENTAL RULES                                                       ║
║  P(Aᶜ)      = 1 - P(A)                        [Complement]              ║
║  P(A ∪ B)   = P(A) + P(B) - P(A ∩ B)          [Addition]               ║
║  P(A ∩ B)   = P(A) × P(B|A)                   [Multiplication]         ║
║  P(A ∩ B)   = P(A) × P(B)  if independent     [Independence]           ║
╠══════════════════════════════════════════════════════════════════════════╣
║  CONDITIONAL & BAYES                                                     ║
║  P(A|B)     = P(A ∩ B) / P(B)                 [Conditional]            ║
║  P(A|B)     = P(B|A)·P(A) / P(B)              [Bayes Theorem]          ║
║  P(B)       = Σᵢ P(B|Aᵢ)·P(Aᵢ)               [Total Probability]      ║
╠══════════════════════════════════════════════════════════════════════════╣
║  EXPECTATION & VARIANCE                                                  ║
║  E[X]       = Σ x·P(x)  or  ∫ x·f(x)dx       [Expected Value]         ║
║  Var(X)     = E[X²] - (E[X])²                 [Variance]               ║
║  E[aX+b]    = a·E[X] + b                      [Linearity]              ║
║  Var(aX+b)  = a²·Var(X)                       [Scaling]                ║
║  E[X+Y]     = E[X] + E[Y]                     [Always true]            ║
║  Var(X+Y)   = Var(X)+Var(Y) if independent    [Independence]           ║
╠══════════════════════════════════════════════════════════════════════════╣
║  LIKELIHOOD                                                              ║
║  L(θ|data)  = Π P(xᵢ|θ)                       [Likelihood]             ║
║  ℓ(θ)       = Σ log P(xᵢ|θ)                   [Log-Likelihood]         ║
║  MLE        = argmax ℓ(θ)                      [ML Estimation]          ║
╚══════════════════════════════════════════════════════════════════════════╝
""")
```

### 16.2 NumPy Probability Functions

```python
import numpy as np
import pandas as pd

numpy_ref = pd.DataFrame({
    'Function'               : [
        'np.random.seed(42)',
        'np.random.rand(n)',
        'np.random.randn(n)',
        'np.random.randint(a,b,n)',
        'np.random.choice(arr,n,p=)',
        'np.random.binomial(n,p,size)',
        'np.random.normal(μ,σ,size)',
        'np.random.poisson(λ,size)',
        'np.random.exponential(scale,size)',
        'np.random.uniform(a,b,size)',
        'np.mean(arr == val)',
        'np.cumsum(arr)/np.arange(1,n+1)',
    ],
    'What it does'           : [
        'Set random seed for reproducibility',
        'Uniform random floats in [0,1)',
        'Standard Normal random floats',
        'Random integers in [a,b)',
        'Sample from arr with given probabilities',
        'Binomial random samples',
        'Normal (Gaussian) random samples',
        'Poisson random samples',
        'Exponential random samples',
        'Uniform random samples in [a,b)',
        'Estimate P(X = val) from data',
        'Running mean — LLN visualisation',
    ]
})
print("=== NumPy Probability Reference ===")
for _, row in numpy_ref.iterrows():
    print(f"  {row['Function']:<45}  # {row['What it does']}")
```

### 16.3 SciPy Distribution API — Complete Reference

```python
from scipy.stats import norm, binom, poisson
import pandas as pd

print("=== SciPy stats — Universal Distribution API ===\n")
print("For ANY distribution dist = norm / binom / poisson / expon / ...\n")

api = [
    ("dist.pmf(k, *params)",        "P(X=k)         — discrete only"),
    ("dist.pdf(x, *params)",        "f(x)            — density (continuous only)"),
    ("dist.cdf(x, *params)",        "P(X ≤ x)        — cumulative distribution"),
    ("dist.sf(x, *params)",         "P(X > x)        — survival = 1 - CDF"),
    ("dist.ppf(q, *params)",        "x such that P(X≤x)=q — inverse CDF"),
    ("dist.isf(q, *params)",        "x such that P(X>x)=q — inverse SF"),
    ("dist.interval(0.95,*params)", "95% central interval [lo, hi]"),
    ("dist.rvs(*params, size=n)",   "Random samples from distribution"),
    ("dist.mean(*params)",          "E[X]"),
    ("dist.var(*params)",           "Var(X)"),
    ("dist.std(*params)",           "Std(X) = √Var(X)"),
    ("dist.median(*params)",        "median(X)"),
    ("dist.moment(n,*params)",      "n-th central moment"),
    ("dist.entropy(*params)",       "Shannon entropy H(X)"),
    ("dist.fit(data)",              "MLE of params from data — continuous only"),
    ("dist.logpdf(x, *params)",     "log f(x)        — numerically stable"),
    ("dist.logcdf(x, *params)",     "log P(X ≤ x)    — numerically stable"),
    ("dist.logsf(x, *params)",      "log P(X > x)    — numerically stable"),
]

for func, desc in api:
    print(f"  {func:<42}  # {desc}")

# Quick demo
print("\n=== Quick Demo: norm API ===")
from scipy.stats import norm
mu, sigma = 100, 15   # IQ distribution
print(f"P(IQ ≤ 115)  = {norm.cdf(115, mu, sigma):.4f}  (top {norm.sf(115,mu,sigma)*100:.1f}%)")
print(f"P(IQ > 130)  = {norm.sf(130, mu, sigma):.4f}  (gifted threshold)")
print(f"Top 5th pct  = {norm.ppf(0.95, mu, sigma):.2f}  IQ")
print(f"Middle 95%   = [{norm.interval(0.95,mu,sigma)[0]:.1f}, {norm.interval(0.95,mu,sigma)[1]:.1f}]")
```

### 16.4 Distribution Parameters Quick Reference

```python
from scipy.stats import (bernoulli, binom, poisson, geom,
                         uniform, norm, expon, gamma, beta)
import numpy as np

print("=== Distribution Parameters & SciPy Syntax ===\n")

dist_ref = [
    ("DISCRETE",     "",                    "",                "",              ""),
    ("Bernoulli",    "bernoulli.pmf(k,p)",  "E=p",            "V=p(1-p)",      "k∈{0,1}"),
    ("Binomial",     "binom.pmf(k,n,p)",    "E=np",           "V=np(1-p)",     "k∈{0..n}"),
    ("Poisson",      "poisson.pmf(k,mu)",   "E=λ",            "V=λ",           "k∈{0,1,2...}"),
    ("Geometric",    "geom.pmf(k,p)",       "E=1/p",          "V=(1-p)/p²",    "k∈{1,2,...}"),
    ("",             "",                    "",                "",              ""),
    ("CONTINUOUS",   "",                    "",                "",              ""),
    ("Uniform",      "uniform.pdf(x,a,b-a)","E=(a+b)/2",     "V=(b-a)²/12",   "x∈[a,b]"),
    ("Normal",       "norm.pdf(x,μ,σ)",     "E=μ",            "V=σ²",          "x∈(-∞,∞)"),
    ("Exponential",  "expon.pdf(x,0,1/λ)",  "E=1/λ",          "V=1/λ²",        "x≥0"),
    ("Gamma",        "gamma.pdf(x,α,0,β)",  "E=αβ",           "V=αβ²",         "x≥0"),
    ("Beta",         "beta.pdf(x,α,β)",     "E=α/(α+β)",      "V=αβ/(α+β)²(α+β+1)","x∈[0,1]"),
]

print(f"{'Distribution':<15} {'SciPy Call':<28} {'Mean':<15} {'Variance':<20} {'Support'}")
print("-" * 90)
for row in dist_ref:
    if row[1] == "":
        if row[0]:
            print(f"\n--- {row[0]} ---")
    else:
        print(f"{row[0]:<15} {row[1]:<28} {row[2]:<15} {row[3]:<20} {row[4]}")
```

---

## 🎯 Summary of Key Probability Concepts

```python
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    MASTER SUMMARY — PROBABILITY WITH PYTHON                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  PART 1: FOUNDATIONS                                                         ║
║  • Probability ∈ [0,1] measures uncertainty using classical or frequentist  ║
║    definitions; verified by simulation via Law of Large Numbers             ║
║  • Sample space Ω = all outcomes; Events = subsets of Ω                     ║
║  • 3 rules: Complement (1-P), Addition (P∪ = P+P-P∩), Multiplication       ║
║  • Library: NumPy (np.random.*)  for all simulation work                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  PART 2: CONDITIONAL PROBABILITY & BAYES                                     ║
║  • P(A|B) = P(A∩B)/P(B) — restricts the sample space to B                  ║
║  • Bayes: Posterior = Likelihood × Prior / Evidence                         ║
║  • Base rate dominates when events are rare — NEVER ignore prevalence       ║
║  • Library: NumPy simulation + pandas crosstab for data-based conditionals  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  PART 3: DISTRIBUTIONS                                                       ║
║  • Discrete: PMF sums to 1; Continuous: PDF integrates to 1                 ║
║  • Bernoulli→ Binomial→ Poisson for counts; Normal→ Exponential for time   ║
║  • SciPy API: .pmf/.pdf, .cdf, .sf, .ppf, .rvs, .mean, .var               ║
║  • β distribution for modelling probabilities themselves (Bayesian A/B)    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  PART 4: SIMULATION & VISUALISATION                                          ║
║  • Monte Carlo: estimate via repeated random sampling; error ∝ 1/√n        ║
║  • Always visualise: histogram, KDE, ECDF, QQ-plot, violin, heatmap        ║
║  • Seaborn for fast statistical plots; Matplotlib for fine control         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  PART 5: STATISTICS & ML                                                     ║
║  • E[X] = long-run average; Var(X) = spread; CLT makes means Normal        ║
║  • Log-likelihood = what ML optimisers maximise                             ║
║  • Cross-entropy = Negative Log-Likelihood of Bernoulli model               ║
║  • Sigmoid for binary; Softmax for multiclass; calibrate outputs!           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  PART 6: BEST PRACTICES                                                      ║
║  • Never swap P(A|B) and P(B|A)          [Prosecutor's Fallacy]            ║
║  • Always account for base rates          [Base Rate Neglect]               ║
║  • Past events don't change future probs  [Gambler's Fallacy]              ║
║  • Test independence statistically        [Chi-Square Test]                 ║
║  • Simulate to VERIFY, not as first choice for simple problems              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")
```

---

## 💡 Learning Tips for AI/ML Students

**1. Code alongside the math.** For every formula you read, immediately write the equivalent NumPy or SciPy line. The gap between equation and code must become zero.

**2. Simulate first to build intuition.** Before accepting any probability result, simulate it. If the simulation agrees, your understanding is correct. If not, your model is wrong.

**3. Always ask "Which distribution?"** When you encounter a real problem, resist the urge to assume Normal. Ask: Is the outcome binary? Counted? A time? Bounded? Let the data shape tell you.

**4. Master Bayes Theorem deeply.** It is not a formula — it is a philosophy of updating beliefs. It appears in spam filters, medical tests, A/B testing, and Bayesian neural networks.

**5. Visualise before modelling.** Plot a histogram and KDE of any variable before fitting. The shape tells you which distribution to use and whether assumptions hold.

**6. Connect every loss function to a distribution.** Cross-entropy ↔ Bernoulli NLL. MSE ↔ Gaussian NLL. MAE ↔ Laplace NLL. Understanding this unifies all of ML.

**7. Calibration matters as much as accuracy.** A model that says 90% confident but is right 60% of the time is dangerous. Always check your probability outputs with calibration curves.

---

## 📝 Practice Roadmap

### 🟢 Beginner (Week 1–2)
- [ ] Simulate 100,000 coin flips; verify complement, addition, and multiplication rules
- [ ] Implement Bayes Theorem from scratch for 3 different medical test scenarios
- [ ] Plot PMF and CDF for Bernoulli, Binomial, Poisson using SciPy
- [ ] Simulate the birthday paradox and verify against the analytical formula
- [ ] Plot Normal distribution with empirical rule shading

### 🟡 Intermediate (Week 3–4)
- [ ] Build a full Naive Bayes email spam classifier using only NumPy + pandas
- [ ] Verify the Central Limit Theorem with 5 different population shapes
- [ ] Implement MLE for Normal distribution both analytically and via `scipy.optimize`
- [ ] Run the Monty Hall simulation and explain the result mathematically
- [ ] Simulate the birthday paradox, Monty Hall, and π estimation with convergence plots

### 🔴 Advanced (Week 5–8)
- [ ] Implement logistic regression from scratch using gradient descent + NLL loss
- [ ] Build a Bayesian A/B tester using Beta distribution with sequential updating
- [ ] Implement softmax temperature scaling and show its effect on confidence
- [ ] Fit a Poisson distribution to real count data using MLE; test for overdispersion
- [ ] Build a Monte Carlo portfolio risk model with Value-at-Risk estimation

### 🚀 Projects
- [ ] **Spam Classifier** — Naive Bayes from scratch on real email dataset
- [ ] **Bayesian A/B Test** — Real click-through data with Beta posterior updates
- [ ] **Monte Carlo Finance** — Portfolio simulator with VaR and expected shortfall
- [ ] **Distribution Identifier** — Tool that takes data and identifies best-fit distribution
- [ ] **Calibration Audit** — Compare sklearn classifiers on probability calibration

---

## 📦 Library Reference Card

| Library | Primary Role | Key Probability Functions |
|---------|-------------|--------------------------|
| **NumPy** | Simulation & array math | `np.random.*`, `np.mean`, `np.cumsum` |
| **SciPy stats** | All standard distributions | `.pmf/.pdf`, `.cdf`, `.sf`, `.ppf`, `.rvs`, `.fit` |
| **pandas** | Conditional probs on data | `crosstab`, `groupby`, `value_counts`, `pivot_table` |
| **Matplotlib** | Custom, fine-tuned plots | `hist`, `plot`, `fill_between`, `scatter` |
| **Seaborn** | Statistical visualisation | `histplot`, `kdeplot`, `ecdfplot`, `violinplot` |
| **scipy.optimize** | MLE numerical fitting | `minimize`, `minimize_scalar` |
| **scipy.special** | Math functions | `comb`, `factorial`, `expit`, `softmax` |

---

## 🔭 Next Steps After This Guide

| Topic | Why It Matters | Resources |
|-------|---------------|-----------|
| `statsmodels` | Hypothesis testing, regression | Wes McKinney's Python for Data Analysis |
| `PyMC` | Bayesian modelling, MCMC | Bayesian Analysis with Python |
| `torch.distributions` | Probability in deep learning | PyTorch docs |
| `sklearn.calibration` | Calibration in ML | Scikit-learn user guide |
| Information Theory | Entropy, KL divergence, mutual info | Elements of Information Theory |
| Stochastic Processes | Markov chains, HMMs, random walks | Durrett: Probability |

---

*Built with 💙 for the next generation of AI/ML engineers*  
*Fork · Star · Share · Improve*

> **"Probability theory is nothing but common sense reduced to calculation."**  
> — Pierre-Simon Laplace
