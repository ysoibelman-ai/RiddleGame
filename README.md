RiddleGame

This is a  terminal riddle game. You answer riddles, it times how long you take, and at the end it shows you a summary of how you did. There's also a leaderboard, and a menu where you can add/edit/delete your own riddles.


What it does

- Asks you for a username, then goes through all the riddles one by one
- There are 3 types of riddles: open answer, 2-choice, and 4-choice
- You have to get each riddle right before it moves on to the next one
- It times you on each riddle and shows your average time per riddle type and per category at the end
- Saves your result to a leaderboard file (`LeaderBoard.csv`)
- Has a menu to manage riddles too — you can add new ones, update them, delete them, or just print them all out

How to run it

1. In terminal write git clone https://github.com/ysoibelman-ai/RiddleGame.git
2. Install  requirements: in terminal write: pip install -r requirements.txt
3. Run game by writeing in terminal: python main.py

The menu

When you run it you get 4 options:

- **play game** - asks for your username and starts the riddles
- **manage riddles** - lets you add/update/delete/show riddles
- **view leader-board** - shows everyone's scores so far
- **exit** - quits

If you pick multiple choice you can type either the answer itself or the number next to it, both work.

Files

Here's  what each file does:

- main.py - the main file that starts everything
- game.py' - the main game logic, the menu, timing, printing the summary, and the leaderboard stuff
- riddles.py - the Riddle class and its subclasses (open riddle, 2-answer, 4-answer)
- riddleCrud.py - handles loading/saving riddles to the json file and adding/updating/deleting them
- player.py - just holds the username
- results.py - keeps track of the scores/timing and does the averages
- validations.py - some checks so you can't do stuff like add a riddle with an id that already exists
- gameRiddles.json - where all the riddles are actually stored
- LeaderBoard.csv - gets created/added to every time someone finishes a game

Riddle format

Riddles in the json file look like this:

```json
{
    "id": 1,
    "question": "What is 12 times 8?",
    "correct_answer": "96",
    "type": "open",
    "difficulty": "easy",
    "category": "Math"
}
```

if it's multiple choice (`multiple_2` or `multiple_4`) there's also a `possible_answers` list with the options.

## Things that still don't work

- can't change a riddle's type once it's made, only the fields inside it — didn't have time to handle that yet
- you need `gameRiddles.json` and `LeaderBoard.csv` to already exist in the folder for it to work
