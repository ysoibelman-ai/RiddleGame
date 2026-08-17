
class QuestionResult:
    def __init__(self,riddle_id: int, riddle_type: str, riddle_category: str, time_taken: float):
        self.__riddle_id = riddle_id
        self.__riddle_type = riddle_type
        self.__riddle_category = riddle_category
        self.__time_taken = time_taken

class GameResult:
    def __init__(self, username:str, date:str, total_time: float, question_results :list):
        self.__usrename = username
        self.__date = date
        self.__total_time = total_time
        self.__question_results = question_results



    def get_total_riddles(self) -> int:
        return len(self.__question_results)
    
    def average_time_by_type(self) -> dict:
        pass

    def average_time_by_category(self) -> dict:
        pass

    def to_csv_row(self) -> list:
        pass
