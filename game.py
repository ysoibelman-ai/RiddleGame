import json
import csv
import time
from datetime import date
from player import Player
from results import GameResult, QuestionResult
from riddles import Riddle, Open_Riddle, TwoAnswerRiddle, FourAnswerRiddle
from riddleCrud import RiddleRipository
import questionary

class RiddleGame:
    def __init__(self, player: Player, riddles:list[Riddle], results: list[QuestionResult]):
        self.__player = player
        self.__riddles = riddles
        self.__results = results

    @staticmethod
    def start() -> GameResult:
        option = questionary.select("What would you like to do?",choices = ["play game","manage riddles","Leader-Board","exit"]).ask()

        if option == "play game":
            player = Player(RiddleGame.create_player())
            return RiddleGame.play(player)
        
        elif option == "exit":
            print("exiting game")

        elif  option == "Leader-Board":
            leader_board_options = questionary.select("What would you like to do?", choices = ["View leader-board","Sort by username","Sort by total time"]).ask()
            if  leader_board_options == "View leader-board":
                RiddleGame.view_leader_board()
            elif leader_board_options == "Sort by username":
                RiddleGame.sort_by_username()
            elif leader_board_options == "Sort by total time":
                RiddleGame.sort_by_total_time()

        else:
            manage_select = questionary.select("what would you like to manage?", choices = ["Add riddle","Show all riddles","Update riddle","Delete riddle","Return"]).ask()
            if manage_select == "Add riddle":
                RiddleRipository.add_riddle()
            if manage_select == "Delete riddle":
                RiddleRipository.delete_riddle()
            if manage_select == "Show all riddles":
                RiddleRipository.show_all_riddles()
            if manage_select == "Return":
                RiddleGame.start()
            if manage_select == "Update riddle":
                RiddleRipository.update_riddle()

    def play (player:Player) -> GameResult:
        riddle_list = RiddleRipository.load_riddles()
        game = RiddleGame(player,riddle_list,[])

        start_time = time.perf_counter()
        today = str(date.today())
        for riddle in game.__riddles:
            game.ask_riddle(riddle)
        total_time = time.perf_counter() - start_time
        gameresult = GameResult(game.__player.username,today,f"{total_time:.2f} seconds",list(game.__results))
        return gameresult

    def ask_riddle(self,riddle:Riddle) -> QuestionResult:
        start_time = time.perf_counter()
        answered_correctly = False
        while not answered_correctly:
            riddle.display()
            answer = input ("enter your answer: ")
            if riddle.check_answer(answer):
                answered_correctly = True
                print ("you answerd correctly")
            else:
                print ("wrong answer")

        total_time = time.perf_counter() - start_time
        question_result = QuestionResult(riddle.id, riddle.get_type(), riddle.category, total_time)
        self.__results.append(question_result)

    @staticmethod        
    def print_summary (result: GameResult) -> None:
        print("\nGame Summary")
        print (f"Username: {result.username}")
        print (f"Total game time: {result.total_time}")
        print (f"Total riddles answered: {result.get_total_riddles()}\n")

        print("Average time by type:")
        avg_by_typ = result.average_time_by_type()
        for key,value in avg_by_typ.items():
                print(f"{key}: {value:.2f} seconds")
        print()
        print("Average time by category")
        avg_by_cat = result.average_time_by_category()
        for key, value in avg_by_cat.items():
            print(f"{key}: {value:.2f} seconds")

    @staticmethod
    def create_player():
        username = input ("please enter a username: ")
        return username

    def add_to_leader_board(game_results):
        file = open("LeaderBoard.csv", "a+", newline="")
        file.seek(0)
        writer = csv.writer(file)
        new = len(file.readlines())
        if  new == 0:
            writer.writerow(["Username","Date","Total Time","Riddles Answered"])
        writer.writerow(game_results.to_csv_row())
        file.close()

    def view_leader_board():
        file = open("LeaderBoard.csv", "r")
        content = file.read().strip()
        if not content:
            print("Leader board is empty")
        else:
            print("Leader Board\n")
            print(content)
        file.close()

    def sort_by_username():
        file = open("LeaderBoard.csv", "r")
        reader = csv.reader(file)
        rows = list(reader)
        file.close()

        if len(rows) <= 1:
            print("Leader board is empty")
        else:
            header = rows[0]
            players = rows[1:]
            sorted_rows = sorted(players)

            print("Leader Board (sorted by username)\n")
            print(",".join(header))
            for row in sorted_rows:
                print(",".join(row))


    def get_total_time(row):
        time_string = row[2]
        number_part = time_string.replace(" seconds", "")
        return float(number_part)

    def sort_by_total_time():
        file = open("LeaderBoard.csv", "r")
        reader = csv.reader(file)
        rows = list(reader)
        file.close()

        if len(rows) <= 1:
            print("Leader board is empty")
        else:
            header = rows[0]
            players = rows[1:]
            sorted_rows = sorted(players, key=RiddleGame.get_total_time)

            print("Leader Board (sorted by total time)\n")
            print(",".join(header))
            for row in sorted_rows:
                print(",".join(row))

