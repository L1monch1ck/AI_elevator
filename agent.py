import numpy as np
import os


class QLearningAgent:

    def __init__(self):

        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2

        # 6x6 = 36 states
        self.q_table = np.zeros((36, 4))

        self.rewards_history = []

    # =========================
    # ACTION SELECTION
    # =========================

    def choose_action(self, state):

        if np.random.rand() < self.epsilon:
            return np.random.randint(0, 4)

        return np.argmax(self.q_table[state])

    # =========================
    # UPDATE
    # =========================

    def update(self, state, action, reward, next_state):

        best_next = np.max(self.q_table[next_state])

        self.q_table[state, action] += self.alpha * (
            reward + self.gamma * best_next - self.q_table[state, action]
        )

    # =========================
    # SAVE
    # =========================

    def save(self):

        np.save("q_table.npy", self.q_table)
        np.save("rewards.npy", np.array(self.rewards_history))

    # =========================
    # LOAD
    # =========================

    def load(self):

        if os.path.exists("q_table.npy"):
            self.q_table = np.load("q_table.npy")

        if os.path.exists("rewards.npy"):
            self.rewards_history = list(np.load("rewards.npy"))

    # =========================
    # LOG
    # =========================

    def log_episode(self, reward_sum):

        self.rewards_history.append(reward_sum)