import matplotlib.pyplot as plt
import numpy as np
from agent import QLearningAgent

agent = QLearningAgent()
agent.load()

rewards = np.array(agent.rewards_history)

print("Loaded rewards:", len(rewards))  # 🔥 проверка

plt.figure(figsize=(10,5))
plt.plot(rewards, label="Reward per Episode")

if len(rewards) > 50:
    smooth = np.convolve(rewards, np.ones(50)/50, mode='valid')
    plt.plot(smooth, label="Smoothed Reward", linewidth=2)

plt.title("Q-Learning Training Progress")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.legend()
plt.grid()
plt.show()