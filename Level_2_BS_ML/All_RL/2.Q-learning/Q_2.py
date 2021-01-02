# Q-Learning - Discounted reward

import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import register

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False}
)

env = gym.make('FrozenLake-v3')

Q = np.zeros([env.observation_space.n, env.action_space.n]) # 테이블 생성
dis = 0.9
num_episodes = 2000 # 2000 학습

rList = []

for i in range(num_episodes):
    state = env.reset() # 초기화
    rAll = 0
    done = False

    # The Q-Table learning 알고리즘
    while not done:
        # Q 값에 노이즈를 추가
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n)/(i+1))

        # 새로운 환경과 보상을 얻는다
        new_state, reward, done, _ = env.step(action)

        # update Q-Table
        Q[state, action] = reward + dis * np.max(Q[new_state,:]) # ':' 모든 경우

        rAll += reward # reward 모두의 합
        state = new_state

    rList.append(rAll)

print("Success rate: " + str(sum(rList)/num_episodes)) # 2000번 중에 얼마나 성공 했는지
print("Final Q-Table Values")
print(Q)
plt.bar(range(len(rList)), rList, color="blue")
plt.show()
