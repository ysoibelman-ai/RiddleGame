import questionary
import json
from riddles import *
from validations import Validations


class RiddleRipository:

    def load_riddles():
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

    def save_riddles (riddles:list[Riddle]):
        f = open ("gameRiddles.json","w")
        json.dump(riddles, f, indent= 4,)
        f.close()
    
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

        difficulty = questionary.select("Please choose a difficulty",choices=["Easy","Medium","Hard"]).ask()
        category = questionary.select("Please choose a category",choices = ["Math","English","Geography","Science","History","Other"]).ask()

        f = open("gameRiddles.json","r")
        riddles = json.load(f)
        f.close()

        if type == "open":
           riddles.append({"id": int(id),"question": question, "correct_answer": correct_answer, "difficulty": difficulty, "category":category})
        if type == "multiple_2":
            riddles.append({"id": int(id),"question": question, "correct_answer": correct_answer,"possible_answers":possible_answers, "difficulty": difficulty, "category":category})
        if type == "multiple_4":
            riddles.append({"id": int(id),"question": question, "correct_answer": correct_answer,"possible_answers":possible_answers, "difficulty": difficulty, "category":category})
        RiddleRipository.save_riddles(riddles)

    def delete_riddle():
        f = open ("gameRiddles.json","r")
        riddles = json.load(f)
        f.close()
        if riddles == [] or riddles == None:
            print ("There are no riddles to delete")
        else:
            id = int(input ("enter id of riddle you want to delete: "))
            exists = False
            for riddle in riddles:
                if riddle["id"] == int(id):
                    exists = True
                    riddles.remove(riddle)
                   
            if exists == False:
                print ("there is no riddle with that id")
            else:
                f = open ("gameRiddles.json","w")
                if len(riddles) == 0:
                    json.dump("", f, indent= 4,)
                else:
                    json.dump(riddles, f, indent= 4,)
                f.close()

    def update_riddle():
        f = open ("gameRiddles.json","r")
        riddles = json.load(f)
        f.close()
        if riddles == [] or riddles == None:
            print ("There are no riddles to delete")
        else:

            id = int(input ("enter id of riddle you want to update: "))
            index = None

            for i in range (len(riddles)):
                riddle = riddles[i]
                if riddle["id"] == int(id):
                    index = i
                    break
            if index == None:
                print ("there is no riddle with that id")
            else:

                update_select = questionary.select("what field would you like to update",choices = list(riddle.keys())).ask()

                if type(riddle[update_select]) == list:
                    possible_answer_index = int(input("enter which answer you would like to change: ")) -1
                    if Validations.check_possible_answer_index(possible_answer_index,riddle):
                        riddle[update_select][possible_answer_index] = input ("enter new answer: ")

                elif update_select == "question":
                    new_question = input("please enter the new qquestion: ")
                    if Validations.check_question(new_question):
                        riddle[update_select] = new_question+"?"

                elif update_select == "id":
                    new_id = int(input("Enter new id"))
                    if Validations.check_id(int(new_id)):
                        riddle[update_select] = new_id

                elif update_select == "type":
                    new_type = questionary.select("to what type would you like to change to?",choices = ["open","multiple_2","multiple_4"]).ask()
                    riddle[update_select] = new_type

                elif update_select == "category":
                    new_category = questionary.select("to what category would you like to change to?",choices = ["Math","English","Geography","Science","History"]).ask()
                    riddle[update_select] = new_category

                elif update_select == "difficulty":
                    new_difficulty = new_category = questionary.select("select new difficulty:",choices = ["easy","hard","medium"]).ask()
                    riddle[update_select] = new_difficulty

                elif update_select == "correct_answer":
                    new_correct_answer = input ("enter new correct answer")
                    if Validations.check_new_correct_answer(new_correct_answer,riddle):
                        riddle[update_select] = new_correct_answer
                    
                else:
                    riddle[update_select] = input (f"enter new {update_select}: ")
                

                riddles[index] = riddle
                RiddleRipository.save_riddles(riddles)


    def show_all_riddles():
        f = open ("gameRiddles.json","r")
        riddles = json.load(f)
        f.close()
        for riddle in riddles:
            for item in riddle:
                print(f"{item.upper()}: {riddle[item]}")
            print()