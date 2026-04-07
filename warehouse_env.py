import numpy as np

class WarehouseEnv:
    def __init__(self, task_level="hard"):
        self.max_capacity = 200
        self.task_level = task_level
        self.reset()

    def reset(self):
        self.current_stock = 100
        self.pending_orders = [] # [ (amount, days_left) ]
        self.day = 0
        return self.state()

    def state(self):
        # AI ab ye dekhega: [Stock, Aaj ki Demand, Kitna maal raste mein hai]
        on_the_way = sum([amt for amt, days in self.pending_orders])
        return np.array([self.current_stock, on_the_way, self.day], dtype=np.float32)

    def step(self, action):
        self.day += 1
        
        # 1. Lead Time Logic (Maal raste mein hai)
        # Action 1: 20 units mangwao (aane mein 3 din lagenge)
        if action == 1:
            self.pending_orders.append([20, 3])
        elif action == 2:
            self.pending_orders.append([50, 5]) # Bada order, zyada time
            
        # Update pending orders
        arrived_stock = 0
        for i in range(len(self.pending_orders)):
            self.pending_orders[i][1] -= 1 # Ek din kam hua
            if self.pending_orders[i][1] <= 0:
                arrived_stock += self.pending_orders[i][0]
        
        self.pending_orders = [o for o in self.pending_orders if o[1] > 0]
        self.current_stock += arrived_stock

        # 2. Advanced Demand (Seasonality)
        # Har 7 din mein demand badh jati hai (Weekend sale)
        base_demand = 15
        if self.day % 7 == 0: base_demand = 40 
        demand = np.random.normal(base_demand, 5) # Randomness

        # 3. Complex Reward (The "Secret Sauce" for Selection)
        holding_cost = self.current_stock * 0.1  # Zyada maal = zyada kiraya
        revenue = 0
        stockout_penalty = 0

        if self.current_stock >= demand:
            self.current_stock -= demand
            revenue = 2.0 # Paisa kamaya
        else:
            stockout_penalty = 5.0 # Bada nuksan! Grahak chala gaya
            self.current_stock = 0

        # Final Reward Formula
        reward = revenue - holding_cost - stockout_penalty
        
        # Reward ko 0-1 ki range mein normalize karna (Hackathon rule)
        final_score = max(0, min(1, (reward + 10) / 20))

        done = self.day >= 30
        return self.state(), final_score, done
    # --- YE VALA HISSA ADD KARO ---
if __name__ == "__main__":
    env = WarehouseEnv(task_level="hard")
    obs = env.reset()
    print(f"Game Start! Initial State: {obs}")
    
    for i in range(1, 11): # 10 din ka test
        # Pehle din order dete hain (Action 2), baaki din wait karte hain (Action 0)
        action = 2 if i == 1 else 0
        obs, reward, done = env.step(action)
        print(f"Day {i:02d}: Action={action} | Stock={obs[0]:.1f} | On-the-way={obs[1]:.1f} | Reward={reward:.2f}")