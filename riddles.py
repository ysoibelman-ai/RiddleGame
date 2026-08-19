from abc import *
import questionary
import json

class RiddleRipository:
    def add_riddle():
        type = questionary.select("please select what kind of riddle you would like to add:",choices = ["open","multiple_2","multiple_4"]).ask()
        print ("please enter the following fields:\n")
        id = input("id: ")
        question = input("question: ")

        if type == "multiple_2":
            print("please enter 2 options for the answer one after another:\n")
            possible_answers =[input(),input()] 
            correct_answer = questionary.select("plesee select which one is the correct answer:", choices = [possible_answers[0],possible_answers[1]]).ask()
        elif type == "multiple_4":
            print("please enter 4 options for the answer one after another:\n")
            possible_answers =[input(),input(),input(),input()] 
            correct_answer = questionary.select("plesee select which one is the correct answer:", choices = [possible_answers[0],possible_answers[1],possible_answers[2],possible_answers[3]]).ask()
        elif type == "open":
            correct_answer = input ("please type in the correct answer")

        difficulty = questionary.select("Please choose a difficulty",choices=["easy","medium","hard"]).ask()
        category = questionary.select("Please choose a category",choices = ["Math","English","Geography","Science","History","Other"]).ask()

        f = open("gameRiddles.json","r")
        riddles = json.load(f)
        f.close()
        if type == "open":
           riddles.append({"id": id,"question": question, "correct_answer": correct_answer, "difficulty": difficulty, "category":category})
        if type == "multiple_2":
            riddles.append({"id": id,"question": question, "correct_answer": correct_answer,"possible_answers":possible_answers, "difficulty": difficulty, "category":category})
        if type == "multiple_4":
            riddles.append({"id": id,"question": question, "correct_answer": correct_answer,"possible_answers":possible_answers, "difficulty": difficulty, "category":category})
        f = open ("gameRiddles.json","w")
        json.dump(riddles, f, indent= 4,)
        f.close()
        


       

class Riddle (ABC):
    def __init__(self, id:int, question:str, correct_answer:str, difficulty:str, category:str):
        self.__id = id
        self.__question = question
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty
        self.__category = category

    @property
    def id(self) -> int:
        return self.__id
    @property
    def correct_answer(self) -> str:
        return self.__correct_answer
    
    @property
    def category(self) -> str:
        return self.__category
    
    @property
    def question(self) -> str:
        return self.__question
    
    @property
    def difficulty(self) -> str:
        return self.__difficulty

    @abstractmethod
    def display (self):
        raise NotImplementedError

    def check_answer(self,answer:str) -> bool:
        if answer.lower() == self.__correct_answer.lower():
            return True

    @abstractmethod
    def get_type(self):
        raise NotImplementedError

    def to_dict (self):
        pass

class MultipleChoiceRiddle(Riddle):

    def __init__(self, id, question, correct_answer,possible_answers, difficulty, category):
        super().__init__(id, question, correct_answer, difficulty, category)
        self.__possible_answers = possible_answers

    def display (self):
        print (f"Question: {self.question}")
        for index, answer in enumerate(self.__possible_answers, start =1):
            print (f"{index}.{answer} ")


    def check_answer(self,answer: int | str):
        correct_answer = self.correct_answer.lower()
        answer = answer.lower()
        possible_answers = []
        for ans in self.__possible_answers:
            ans = ans.lower()
            possible_answers.append(ans)
        correct_index = possible_answers.index(correct_answer) +1
        if answer == correct_answer or answer == str(correct_index):
            return True

    def get_possible_answers(self):
        return list(self.__possible_answers)

class FourAnswerRiddle(MultipleChoiceRiddle):

    def get_type(self):
        return "multiple_4"

class TwoAnswerRiddle(MultipleChoiceRiddle):

    def get_type(self):
        return "multiple_2"

class Open_Riddle (Riddle):

    def display(self):
        print (f"{self.question}\n")

    def get_type(self):
        return "open"