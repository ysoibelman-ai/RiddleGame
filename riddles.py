from abc import *
import json

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