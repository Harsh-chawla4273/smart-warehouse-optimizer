title: Smart Warehouse Optimizer
emoji: 📦
colorFrom: blue
colorTo: indigo
sdk: docker
app_file: app.py
pinned: false
# 📦 AI-Driven Warehouse Inventory Optimizer (OpenEnv)

This repository contains a custom **Reinforcement Learning (RL) Environment** designed for the **Meta PyTorch OpenEnv Hackathon**. It simulates a complex supply chain warehouse focusing on inventory management under uncertainty.

## 🚀 Key Features
- **Stochastic Lead Time:** Orders take 3-5 days to arrive, simulating real-world delivery delays.
- **Seasonality & Demand Spikes:** Demand follows a weekly cycle with 200% surges on "weekends" (Day 7, 14, 21, 28).
- **Interactive Dashboard:** Built with Streamlit to visualize stock levels, rewards, and strategy comparisons.

## 🧠 The Mathematical Formulation
The environment operates on a reward-maximization principle. The reward function for each step (day) is:

$$Reward = (S \times R) - (I \times H) - (O \times P)$$

Where:
- $S$: Successful Sales (Units sold)
- $R$: Revenue per unit
- $I$: Current Inventory level
- $H$: Holding Cost (Storage expense)
- $O$: Out-of-Stock units
- $P$: Stockout Penalty

## 🛠️ Tech Stack
- **Framework:** PyTorch / OpenEnv
- **Interface:** Streamlit & Plotly
- **Infrastructure:** Docker (Deployed on Hugging Face Spaces)

## 📊 How to Run
1. Select the **Difficulty Level** from the sidebar.
2. Toggle **"Show Comparison"** to see how a Smart Heuristic performs against a Random Agent.
3. Click **"Run Simulation"** to see the 30-day forecast and reward analytics.
