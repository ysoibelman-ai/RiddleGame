from player import *
from results import *
from riddles import *
import json

class RiddleGame:
    def __init__(self, player: Player, riddles:list[Riddle], results: list[QuestionResult]):
        self.__player = player
        self.__riddles = riddles
        self.__results = results

        game_results = self.start()
        self.print_summary(game_results)

    def start (self) -> GameResult:
        
        for riddle in  self.__riddles:
            self.ask_riddle(riddle)
        print (len(self.__results))
        gameresult = GameResult(self.__player.username,"Jan",13,list(self.__results))
        return gameresult

    def ask_riddle(self,riddle:Riddle) -> QuestionResult:
        answered_correctly = False
        while not answered_correctly:
            riddle.display()
            answer = input ("enter your answer: ")
            if riddle.check_answer(answer):
                answered_correctly = True
                print ("you answerd correctly")
            else:
                print ("wrong answer")

        question_result = QuestionResult(riddle.id,"non",riddle.category,10.5)
        self.__results.append(question_result)
            

    def print_summary (self, result: GameResult) -> None:
        print (result.__dict__)
        pass

    @staticmethod
    def create_player():
        username = input ("please enter a username: ")
        return username


    @staticmethod
    def create_riddle_list():
        f = open("gameRiddles.json","r")
        riddles = json.load(f)
        riddle_list = []
        f.close()
        for riddle in riddles:
            if riddle["type"] == "open":
                riddle_list.append(Open_Riddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["difficulty"],riddle["category"],))
            elif riddle["type"] == "multiple_2":
                riddle_list.append(TwoAnswerRiddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["possible_answers"],riddle["difficulty"],riddle["category"],))
            elif riddle["type"] == "multiple_4":
                riddle_list.append(FourAnswerRiddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["possible_answers"],riddle["difficulty"],riddle["category"],))

        return riddle_list
    

class Main:
    player = Player(RiddleGame.create_player())
    riddle_list = RiddleGame.create_riddle_list()
    game = RiddleGame(player,riddle_list,[])

Main ()