from abc import *

class Riddle (ABC):
    def __init__(self, id:int, question:str, correct_answer:str, difficulty:str, category:str):
        self.__id = id
        self.__question = question
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty
        self.__category = category

    @abstractmethod
    def display (self):
        raise NotImplementedError

    def check_answer(self,answer:str) -> bool
        if answer == self.__correct_answer:
            return True

    @abstractmethod
    def get_type(self):
        raise NotImplementedError

    def to_dict (self):
        pass

class MultipleChoiceRiddle(Riddle):

    def __init__(self, id, question, correct_answer,possible_answers, difficulty, category):
        super().__init__(id, question, correct_answer, difficulty, category)
        self.possible_answers = possible_answers

    def display (self):
        print (f"Question: {self.__question}\n Possible Answers: {self.possible_answers}")

    def check_answer(self,answer: int | str):
        if answer == self.check_answer:
            return True

    def get_possible_answers():
        pass

class FourAnswerRiddle(MultipleChoiceRiddle):

    def get_type(self):
        return "Four Answer Riddle"

class TwoAnswerRiddle(MultipleChoiceRiddle):

    def get_type(self):
        return "Two Answer Riddle"

class Open_Riddle (Riddle):

    def display(self):
        print (self.__question)

    def get_type(self):
        return "open"