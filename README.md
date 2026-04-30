# PPO & DQN Trading Agent — Setup & Run Guide

A reinforcement learning project implementing PPO and DQN agents (both from scratch and via Stable-Baselines3) on a stock trading environment using a custom `gym_anytrading` package.

---

## Project Structure

```
Project/
├── setup.py                        ← local package installer
├── gym_anytrading/                 ← custom trading environment (local, fixed version)
│   ├── __init__.py
│   ├── datasets/
│   │   └── data/
│   │       ├── STOCKS_GOOGL.csv
│   │       └── FOREX_EURUSD_1H_ASK.csv
│   └── envs/
│       ├── trading_env.py
│       ├── stocks_env.py
│       └── forex_env.py
└── Implimintation/
    ├── PPO_sb3.ipynb               ← PPO + DQN using Stable-Baselines3
    └── PPO.ipynb                   ← PPO from scratch (pure PyTorch)
```

---

## Step 1 — Prerequisites

Make sure you have **Python 3.10 or 3.11** installed.

Check your version:
```bash
python --version
```

---

## Step 2 — Install Required Packages

Run the following command to install all dependencies:

```bash
pip install gymnasium numpy pandas matplotlib seaborn tqdm torch stable-baselines3
```

> **Note:** If you are on Windows and `torch` fails, install it from the official PyTorch website:
> https://pytorch.org/get-started/locally/

---

## Step 3 — Install the Local `gym_anytrading` Package

This project uses a **custom fixed version** of `gym_anytrading` (not the one on PyPI).
You must install it from the project folder — do **not** run `pip install gym-anytrading`.

Open a terminal, navigate to the `Project/` folder, and run:

```bash
cd path\to\Project
pip install -e .
```

**Windows example:**
```bash
cd C:\Users\YourName\Downloads\Project
pip install -e .
```

**Mac / Linux example:**
```bash
cd ~/Downloads/Project
pip install -e .
```

Verify the installation worked:
```bash
python -c "import gym_anytrading; print(gym_anytrading.__file__)"
```

The printed path should point **inside your `Project/` folder**, not to `site-packages`.

---

## Step 4 — Open the Notebooks

Launch Jupyter from **inside** the `Implimintation/` folder:

```bash
cd path\to\Project\Implimintation
jupyter notebook
```

## Step 5 — Run the Notebooks

### `PPO_sb3.ipynb` — Stable-Baselines3 agents

Run cells top to bottom. This notebook:
- Runs a **random baseline** for 100 episodes
- Trains a **PPO agent** for 25K timesteps and tests it
- Trains a **DQN agent** for 25K timesteps and tests it
- Plots reward comparison across all three

---

# Stock Trading with Reinforcement Learning

## Results & Observations

### Evaluation: Random Agent vs. PPO vs. DQN (25K Timesteps)

The agents were evaluated over **100 episodes** and compared against a random action baseline.

| Agent | Avg. Reward | Timesteps |
|-------|:-----------:|:---------:|
| Random | 249.73 | — |
| PPO | **608.20** | 25K |
| DQN | 597.72 | 25K |

---

### Key Observations

#### RL Agents vs. Random Baseline
- Both RL agents **significantly outperform the random baseline**, achieving more than **2.4× the average reward**, confirming meaningful policy learning within just 25K training timesteps.

#### PPO vs. DQN
- **PPO slightly edges out DQN** (608.20 vs. 597.72), though the ~1.7% margin suggests both algorithms converge to comparable strategies on this environment.

#### Stability Analysis
- **PPO exhibits higher reward variance**, with spikes exceeding **1200** (around episode 75) and occasional dips near **0** — reflecting a more aggressive and exploratory policy.
- **DQN demonstrates comparatively more stable reward curves**, with fewer extremes, owing to its off-policy, replay-buffer-driven learning.

#### Random Agent Behavior
- The random agent stays consistently in the **0–400 range** and is highly erratic throughout all 100 episodes, frequently dipping near or below 0 — underscoring the necessity of learned policies for profitable trading.

#### Early Generalization
- Both RL agents show a **strong early performance advantage** (episodes 0–20), maintaining rewards well above 500, suggesting the learned policies generalize reasonably to unseen test episodes.

#### Room for Improvement
- The **high episode-to-episode variance** in both PPO and DQN suggests that further training (50K–100K timesteps) or hyperparameter tuning could yield more stable and higher returns.

---

### Takeaway

> With only **25K training timesteps**, both PPO and DQN learn substantially better stock trading policies than random action selection. **PPO achieves marginally higher peak and average rewards**, while **DQN offers slightly more consistent episode-level performance**.

---
# Forex Trading with Reinforcement Learning

## Results & Observations

### Evaluation: Random Agent vs. PPO vs. DQN (25K Timesteps — Forex)

The agents were evaluated over **100 episodes** and compared against a random action baseline on a **Forex trading environment**.

| Agent | Avg. Reward | Timesteps |
|-------|:-----------:|:---------:|
| Random | 43.83 | — |
| PPO | **92.35** | 25K |
| DQN | -166.06 | 25K |

---

###  Key Observations

#### PPO vs. Random Baseline
- **PPO is the only agent that meaningfully outperforms the random baseline**, achieving approximately **2.1× the average reward** (92.35 vs. 43.83), indicating partial policy learning within 25K timesteps on this complex environment.

#### DQN Underperforms Severely
- **DQN yields a deeply negative average reward of -166.06**, performing **far worse than even the random agent**, suggesting that DQN's off-policy learning struggles significantly in the **noisy and non-stationary Forex environment** within the given training budget.

#### Stability Analysis
- **All three agents show extremely high variance** across 100 episodes, with rewards fluctuating between **-600 and +700**, reflecting the inherent difficulty and stochasticity of Forex markets.
- **PPO** occasionally achieves strong peaks (e.g., ~650 around episode 75) but also suffers deep drawdowns (e.g., ~-650 around episode 35), indicating an unstable policy.
- **DQN** remains consistently in **negative territory** for most episodes, rarely recovering to positive rewards — a strong sign of policy divergence or inadequate exploration.

#### Random Agent Behavior
- Interestingly, **the random agent maintains a slightly positive average** (43.83), which is a known phenomenon in Forex environments where market drift can occasionally favor random actions over poorly trained policies.

#### Room for Improvement
- The **Forex environment is significantly harder** than standard stock trading, requiring more training timesteps, better reward shaping, and possibly **curriculum learning** or **domain-specific feature engineering** to achieve stable profitability.
- Increasing training to **100K–500K timesteps** and tuning hyperparameters (especially for DQN's replay buffer and learning rate) is strongly recommended.

---

### Takeaway

> The Forex environment proves far more challenging than stock trading. **PPO marginally outperforms the random baseline** with an average reward of **92.35**, while **DQN fails to learn a profitable policy** at 25K timesteps, averaging **-166.06**. Both agents require substantially more training and tuning to be viable for real-world Forex trading scenarios.

---
