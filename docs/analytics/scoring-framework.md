# Scoring Framework

## Overview

The Scoring Framework converts raw analytics into standardized scores that can be compared, ranked, filtered, and monitored.

The objective is not to predict outcomes with certainty.

The objective is to create a consistent decision-support system.

---

# Core Scores

The platform uses five primary scores:

```text
Opportunity Score
Confidence Score
Risk Score
Momentum Score
Infrastructure Health Score
```

All scores are normalized to:

```text
0 – 100
```

---

# Opportunity Score

Measures attractiveness.

Factors:

- valuation
- trend strength
- relative performance
- sector strength
- sentiment
- earnings quality

Scale:

```text
0-25     Weak
26-50    Neutral
51-75    Attractive
76-100   High Conviction
```

Example:

```text
Opportunity Score: 82
Interpretation: High Conviction
```

---

# Confidence Score

Measures reliability of the signal.

Factors:

- data quality
- signal consistency
- historical accuracy
- liquidity
- market conditions

Scale:

```text
0-39     Very Low
40-59    Low
60-74    Moderate
75-89    High
90-100   Very High
```

---

# Risk Score

Measures downside risk.

Factors:

- volatility
- concentration
- leverage
- macro sensitivity
- liquidity

Scale:

```text
0-25     Low Risk
26-50    Moderate Risk
51-75    High Risk
76-100   Speculative
```

Important:

Higher Risk Score = Higher Risk

Unlike Opportunity Score.

---

# Momentum Score

Measures trend strength.

Inputs:

- RSI
- MACD
- Moving Averages
- Volume
- Relative Strength

Scale:

```text
0-25     Weak
26-50    Neutral
51-75    Strong
76-100   Very Strong
```

---

# Infrastructure Health Score

Measures operational health.

Inputs:

- CPU utilization
- RAM utilization
- Storage utilization
- Docker status
- Service uptime

Scale:

```text
0-50     Critical
51-70    Warning
71-85    Healthy
86-100   Excellent
```

---

# Composite Intelligence Score

Future versions may combine:

```text
Opportunity Score
+
Confidence Score
+
Momentum Score
-
Risk Score
```

to generate a unified ranking metric.

---

# Ranking Philosophy

Scores should:

- simplify complexity
- remain explainable
- remain auditable
- remain data-driven

Scores should never be treated as guarantees.

They are decision-support indicators.

---

# Example Output

📈 Asset

```text
Opportunity Score: 81
Confidence Score: 76
Risk Score: 34
Momentum Score: 79
```

Interpretation:

```text
Strong momentum
Attractive opportunity
Moderate risk
High confidence
```

---

# Long-Term Objective

Create a scoring system capable of ranking:

- equities
- mutual funds
- ETFs
- IPOs
- crypto assets
- infrastructure assets

using a unified methodology.
