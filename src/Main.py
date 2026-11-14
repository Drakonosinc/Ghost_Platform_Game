import sys
from Game.Ghost_Platform import *
from pyforgeai import genetic_algorithm, save_model


def _evaluate_population_in_game(game, population):
    game.models = list(population)
    scores = game.run_with_models()
    return [float(s) for s in scores] if isinstance(scores, (list, tuple)) else [float(scores) for _ in population]


if __name__ == "__main__":
    while True:
        (game := ghost_platform()).run()
        game.game_over = False
        match game.mode_game:
            case {"Training AI": True}:
                best_model = genetic_algorithm(
                    batch_fitness_fn=lambda pop: _evaluate_population_in_game(game, pop),
                    input_size=len(game.ai_handler.get_state(game.players[0])),
                    output_size=3,
                    generations=game.config.config_AI["generation_value"],
                    population_size=game.config.config_AI["population_value"],
                    num_trials=game.config.config_AI["try_for_ai"],
                    stop_fn=lambda: bool(getattr(game, "exit", False)),
                    on_generation_fn=lambda g: setattr(game, "generation", g),
                )
                if game.models:
                    game.models[0] = best_model
                else:
                    game.models = [best_model]
                if game.config.config_AI["model_save"] and best_model is not None:
                    save_model(game.models[0], torch.optim.Adam(game.models[0].parameters(), lr=0.001), game.model_path)
            case {"Player": True} | {"AI": True}:
                game.run_with_models()
        if game.exit:
            break
pygame.quit(), sys.exit()
