import questionary
import json
from pprint import pprint


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
        f = open ("gameRiddles.json","w")
        json.dump(riddles, f, indent= 4,)
        f.close()

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

    def show_all_riddles():
        f = open ("gameRiddles.json","r")
        riddles = json.load(f)
        f.close()
        pprint(riddles, sort_dicts=False)
    