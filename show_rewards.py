import numpy as np
import pandas as pd

rewards = np.load("rewards.npy")

df = pd.DataFrame({
    "Episode": range(1, len(rewards) + 1),
    "Reward": rewards
})

print(df)