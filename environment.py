class MazeEnv:

    def __init__(self):

        self.size = 6

        self.start = (0, 0)
        self.goal = (5, 5)

        # СТЕНЫ
        self.walls = [
            (0, 3),
            (1, 1),
            (1, 3),
            (2, 3),
            (3, 1),
            (4, 4),
        ]

        # ЛОВУШКИ
        self.traps = [
            (1, 5),
            (3, 4),
        ]

        self.reset()

    def reset(self):

        self.agent_pos = [0, 0]
        return self.get_state()

    def get_state(self):

        return self.agent_pos[0] * self.size + self.agent_pos[1]

    def step(self, action):

        x, y = self.agent_pos

        moves = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        dx, dy = moves[action]

        nx, ny = x + dx, y + dy

        if (
            0 <= nx < self.size and
            0 <= ny < self.size and
            (nx, ny) not in self.walls
        ):
            x, y = nx, ny

        self.agent_pos = [x, y]

        reward = -1
        done = False

        if (x, y) in self.traps:
            reward = -25

        if (x, y) == self.goal:
            reward = 100
            done = True

        return self.get_state(), reward, done