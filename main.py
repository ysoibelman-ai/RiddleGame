from game import RiddleGame
class Main:
    game_results = RiddleGame.start()
    if game_results:
        RiddleGame.print_summary(game_results)
        RiddleGame.add_to_leader_board(game_results)
Main ()