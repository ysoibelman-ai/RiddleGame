import json

class Validations:

    @staticmethod
    def check_id(new_id):
        f = open ("gameRiddles.json","r")
        riddles = json.load(f)
        f.close()
        id_array = []
        for riddle in riddles:
            id_array.append(riddle["id"])
        if new_id not in id_array:
            return True
        else:
            raise ValueError ("This is is already in use")
        
    @staticmethod
    def check_question (question):
        f = open ("gameRiddles.json","r")
        riddles = json.load(f)
        f.close()
        question_array = []
        for riddle in riddles:
            question_array.append(riddle["question"])
        if question not in question_array:
            return True
        else:
            raise ValueError ("This question is already in use")

    @staticmethod
    def check_new_correct_answer (new_correct_answer:str, riddle) -> bool:
        
        if riddle["type"] == "open":
            return True
        elif riddle["type"] == "multiple_2" or riddle["type"] == "multiple_4":
            if new_correct_answer in riddle["possible_answers"]:
                return True
            else:
                raise ValueError ("this answer is not one of the possible answers")

    @staticmethod
    def check_possible_answer_index (possible_answer_index, riddle) -> bool:
        if riddle["possible_answers"][possible_answer_index] == riddle["correct_answer"]:
            raise ValueError ("You cant change this answer because it is the correct answer")
        return True


            
            


    




