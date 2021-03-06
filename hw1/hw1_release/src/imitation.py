import sys
import argparse
import numpy as np
import keras
import random
import gym


class Imitation():
    def __init__(self, model_config_path, expert_weights_path):
        # Load the expert model.
        with open(model_config_path, 'r') as f:
            self.expert = keras.models.model_from_json(f.read())
        self.expert.load_weights(expert_weights_path)
        
        # Initialize the cloned model (to be trained).
        with open(model_config_path, 'r') as f:
            self.model = keras.models.model_from_json(f.read())

        # TODO: Define any training operations and optimizers here, initialize
        #       your variables, or alternatively compile your model here.

    def run_expert(self, env, render=False):
        # Generates an episode by running the expert policy on the given env.
        return Imitation.generate_episode(self.expert, env, render)

    def run_model(self, env, render=False):
        # Generates an episode by running the cloned policy on the given env.
        return Imitation.generate_episode(self.model, env, render)

    @staticmethod
    def generate_episode(model, env, render=False):
        # Generates an episode by running the given model on the given env.
        # Returns:
        # - a list of states, indexed by time step
        # - a list of actions, indexed by time step
        # - a list of rewards, indexed by time step
        # TODO: Implement this method.
        states = []
        actions = []
        rewards = []
        return states, actions, rewards
    
    def train(self, env, num_episodes=100, num_epochs=50, render=False):
        # Trains the model on training data generated by the expert policy.
        # Args:
        # - env: The environment to run the expert policy on. 
        # - num_episodes: # episodes to be generated by the expert.
        # - num_epochs: # epochs to train on the data generated by the expert.
        # - render: Whether to render the environment.
        # Returns the final loss and accuracy.
        # TODO: Implement this method. It may be helpful to call the class
        #       method run_expert() to generate training data.
        loss = 0
        acc = 0
        return loss, acc


def parse_arguments():
    # Command-line flags are defined here.
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-config-path', dest='model_config_path',
                        type=str, default='LunarLander-v2-config.json',
                        help="Path to the model config file.")
    parser.add_argument('--expert-weights-path', dest='expert_weights_path',
                        type=str, default='LunarLander-v2-weights.h5',
                        help="Path to the expert weights file.")

    # https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
    parser_group = parser.add_mutually_exclusive_group(required=False)
    parser_group.add_argument('--render', dest='render',
                              action='store_true',
                              help="Whether to render the environment.")
    parser_group.add_argument('--no-render', dest='render',
                              action='store_false',
                              help="Whether to render the environment.")
    parser.set_defaults(render=False)

    return parser.parse_args()


def main(args):
    # Parse command-line arguments.
    args = parse_arguments()
    model_config_path = args.model_config_path
    expert_weights_path = args.expert_weights_path
    render = args.render
    
    # Create the environment.
    env = gym.make('LunarLander-v2')
    
    # TODO: Train cloned models using imitation learning, and record their
    #       performance.


if __name__ == '__main__':
  main(sys.argv)
