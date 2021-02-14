from room import Room
from path_finder_agents import RandAgent, BBAgent, DFSAgent, BFSAgent, GreedyAgent, AStarAgent

# env = Room(room=[[0, 0, 1], [0, 0, 1], [0, 0, 0]], target=[2, 2])
env = Room(prob=0.45, n=16, plot_on=True)

#agent = RandAgent(env)
#agent = DFSAgent(env)
#agent = BFSAgent(env)
#agent = IDAgent(env)
agent = AStarAgent(env)
#agent = GreedyAgent(env)
#agent = BBAgent(env, bound=50)

agent.run()
input('Press ENTER to get out of here')
