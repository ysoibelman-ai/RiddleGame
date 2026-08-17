from player import *
from results import *
from riddles import *

class RiddleGame:
    def __init__(self, player: Player, riddles:list[Riddle], results: list[QuestionResult]):
        self.__player = player
        self.__riddles = riddles
        self.__results = results

        pass

    def start (self) -> GameResult:
        # runs the complete game and return final result
        pass

    def ask_riddle(self,riddle:Riddle) -> QuestionResult:
        # shows one riddle until the player answers correctly
        pass
    def print_summary (self, result: GameResult) -> None:
        #prints the end-of-game statistics
        pass
