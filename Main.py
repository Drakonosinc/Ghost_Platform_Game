import sys
from Ghost_Platform import *
from Genetic_Algorithm import *
if __name__=="__main__":
    while True:
        (game:=ghost_platform()).run()
        if game.mode_game["Training AI"]:
            print("hola1")
            best_model = genetic_algorithm(game, input_size=len(game.get_state()), output_size=3,generations=game.generation_value, population_size=game.population_value)
            game.model = best_model
            save_model(game.model, torch.optim.Adam(game.model.parameters(), lr=0.001),game.model_path)
        if game.mode_game["Player"]:
            print("hola2")
            game.run_with_model()
        if game.mode_game["AI"]:
            print("hola3")
            game.run_with_model()
        else:break
pygame.quit(),sys.exit()