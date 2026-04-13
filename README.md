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
