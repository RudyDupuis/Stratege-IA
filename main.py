import os
from ai_training.training import train_agents

START_EPISODE = int(os.environ.get("START_EPISODE", 0))
NB_EPISODES = int(os.environ.get("NB_EPISODES", 1000000))
DISPLAY_BOARD_IN_TERMINAL = (
    os.environ.get("DISPLAY_BOARD_IN_TERMINAL", "False").lower() == "true"
)

train_agents(
    num_episodes=NB_EPISODES,
    start_episode=START_EPISODE,
    agent1_model_path=f"h5/{START_EPISODE}_agent1.h5",
    agent2_model_path=f"h5/{START_EPISODE}_agent2.h5",
    displayBoardInTerminal=DISPLAY_BOARD_IN_TERMINAL,
)
