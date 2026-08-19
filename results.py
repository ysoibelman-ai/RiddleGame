class QuestionResult:
    def __init__(self,riddle_id: int, riddle_type: str, riddle_category: str, time_taken: float):
        self.__riddle_id = riddle_id
        self.__riddle_type = riddle_type
        self.__riddle_category = riddle_category
        self.__time_taken = time_taken

    @property
    def riddle_type(self):
        return self.__riddle_type

    @property
    def time_taken(self):
        return self.__time_taken

    @property
    def riddle_category(self):
        return self.__riddle_category

class GameResult:
    def __init__(self, username:str, date:str, total_time: float, question_results :list[QuestionResult]):
        self.__username = username
        self.__date = date
        self.__total_time = total_time
        self.__question_results = question_results

    @property
    def total_time(self):
        return self.__total_time
    @property
    def username(self):
        return self.__username
    @property
    def date(self):
        return self.__date
    
    def get_total_riddles(self) -> int:
        return len(self.__question_results)
    
    def average_time_by_type(self) -> dict:
        average_time_by_type_dict = {}
        for result in self.__question_results:
            if result.riddle_type not in average_time_by_type_dict:
                average_time_by_type_dict[result.riddle_type] = result.time_taken
            else:
                average_time_by_type_dict[result.riddle_type] +=  result.time_taken
        return dict(average_time_by_type_dict)

    def average_time_by_category(self) -> dict:
        average_time_by_category_dict = {}
        for result in self.__question_results:
            if result.riddle_category not in average_time_by_category_dict:
                average_time_by_category_dict[result.riddle_category] = result.time_taken
            else:
                average_time_by_category_dict[result.riddle_category] += result.time_taken
        return dict(average_time_by_category_dict)

    def to_csv_row(self) -> list:
        return [self.__username,self.__date,self.total_time,self.get_total_riddles()]