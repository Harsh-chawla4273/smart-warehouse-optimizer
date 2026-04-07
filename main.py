from warehouse_env import WarehouseEnv

def test_advanced_logic():
    # Hard level test karte hain
    env = WarehouseEnv(task_level="hard")
    state = env.reset()
    
    print("--- Advanced Warehouse AI Test (Lead Time & Seasonality) ---")
    print(f"Initial State: Stock={state[0]}, On-the-way={state[1]}")

    for day in range(1, 16): # 15 din ka test
        # Day 1 par bada order dete hain (Action 2)
        action = 2 if day == 1 else 0 
        
        next_state, reward, done = env.step(action)
        
        print(f"Day {day:02d}: Stock={next_state[0]:.1f} | On-the-way={next_state[1]:.1f} | Reward={reward:.2f}")

if __name__ == "__main__":
    test_advanced_logic()