import streamlit as st
import pandas as pd
import plotly.express as px
from warehouse_env import WarehouseEnv

st.set_page_config(page_title="AI Warehouse Optimizer", layout="wide")

st.title("📦 Smart Warehouse AI Dashboard")
st.markdown("Meta Pytorch Hackathon: **Advanced Inventory Management Environment**")

# Sidebar
st.sidebar.header("Environment Settings")
level = st.sidebar.selectbox("Difficulty Level", ["easy", "medium", "hard"])
comparison_mode = st.sidebar.checkbox("Show Comparison (Random vs Smart Agent)")

# Initialize Environment
env = WarehouseEnv(task_level=level)

if st.button("Run Simulation (30 Days)"):
    strategies = ["Smart", "Random"] if comparison_mode else ["Smart"]
    all_data = []

    for strategy in strategies:
        obs = env.reset()
        for day in range(1, 31):
            # Agent Logic
            if strategy == "Random":
                action = env.action_space.sample() 
            else:
                # Humara Smart Logic: Agar stock 30 se kam hai toh order karo
                action = 1 if obs[0] < 30 else 0 
            
            obs, reward, done = env.step(action)
            all_data.append({
                "Day": day, 
                "Strategy": strategy, 
                "Stock Level": obs[0], 
                "On-the-way": obs[1], 
                "Reward": reward
            })

    df = pd.DataFrame(all_data)

    # --- VISUALS ---
    st.subheader("Inventory Strategy Analysis")
    
    # 1. Stock Comparison Graph
    fig_stock = px.line(df, x="Day", y="Stock Level", color="Strategy", 
                        title="Stock Management: Smart vs Random")
    st.plotly_chart(fig_stock, use_container_width=True)

    col1, col2 = st.columns(2)
    
    with col1:
        # 2. Reward Bar Chart (Only for Smart if not in comparison)
        st.subheader("Daily Rewards (Performance)")
        fig_reward = px.bar(df[df['Strategy'] == "Smart"], x="Day", y="Reward", 
                             title="Smart Agent Efficiency")
        st.plotly_chart(fig_reward)

    with col2:
        # 3. Data Table
        st.subheader("Simulation Logs")
        st.dataframe(df.tail(10))

    # Final Success Message
    smart_avg = df[df['Strategy'] == "Smart"]['Reward'].mean()
    st.success(f"Simulation Complete! Smart Agent Average Reward: {smart_avg:.2f}")