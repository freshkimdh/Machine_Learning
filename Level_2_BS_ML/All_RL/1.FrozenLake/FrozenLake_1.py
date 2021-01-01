import gym

# FozenLake
env = gym.make("FrozenLake-v0") # 환경설정
observation = env.reset() # 초기화

for _ in range(1000): # "_" 별도로 i를 선언하지 않고 반복 할때 사용
    env.render() # 화면 출력
    action = env.action_space.sample() # 환경에 따른 액션 설정 즉, 알고리즘 작성
    observation, reward, done, info = env.step(action) # 결과, 보상, 게임종료 여부 확인, 추가정보 = 액션 넣어 줌