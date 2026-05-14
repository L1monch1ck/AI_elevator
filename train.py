from environment import MazeEnv
from agent import QLearningAgent

env = MazeEnv()
agent = QLearningAgent()

episodes = 5000

for episode in range(episodes):

    state = env.reset()

    done = False

    # 🔥 ДОБАВИЛИ
    episode_reward = 0

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        agent.update(state, action, reward, next_state)

        state = next_state

        # 🔥 ДОБАВИЛИ
        episode_reward += reward

    # 🔥 ДОБАВИЛИ (самое важное)
    agent.log_episode(episode_reward)

print("Training completed!")

agent.save()

print("Model saved!")