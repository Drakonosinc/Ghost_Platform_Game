import sys
from Ghost_Platform import *
from Genetic_Algorithm import *
if __name__=="__main__":
    while True:
        (game:=ghost_platform()).run()
        game.game_over=False
        match game.mode_game:
            case {"Training AI": True}:
                best_model = genetic_algorithm(game, input_size=len(game.get_state()), output_size=3,generations=game.generation_value, population_size=game.population_value, num_trials=game.try_for_ai)
                game.model = best_model
                if game.model_save:save_model(game.model, torch.optim.Adam(game.model.parameters(), lr=0.001),game.model_path)
            case {"Player": True} | {"AI": True}:game.run_with_models()
        if game.exit:break
pygame.quit(),sys.exit()