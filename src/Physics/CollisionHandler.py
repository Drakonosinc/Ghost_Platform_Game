from pygame import Rect
class CollisionHandler:
    def __init__(self, game):
        self.game = game
        self.sound_death = self.game.check_sound(game.sound_game_lose,"game_over")
    def handle_collision(self, player, reward=-25):
        if self.sound_death:self.sound_death.play(loops=0)
        player.reward += reward
        player.active = False
        self.game.restart()
    def get_next_object(self, player, objects):
        sorted_objects = sorted(objects, key=lambda t: t[1],reverse=True)
        for i, elements in enumerate(sorted_objects):
            if elements[1] < player.rect.y:
                current_object = elements
                next_object1 = sorted_objects[i + 1] if i + 1 < len(sorted_objects) else None
                next_object2 = sorted_objects[i + 2] if i + 2 < len(sorted_objects) else None
                next_object3 = sorted_objects[i + 3] if i + 3 < len(sorted_objects) else None
                next_object4 = sorted_objects[i + 4] if i + 4 < len(sorted_objects) else None
                return current_object, next_object1, next_object2, next_object3, next_object4
        return None, None, None, None, None
    def update_objects(self, width, height, objects, current_object, next_object1, next_object2, next_object3, next_object4):
        if current_object:setattr(self.game, objects, Rect(current_object[0], current_object[1], width, height))
        if next_object1:self.game.platarforms_nexts[0]=Rect(next_object1[0],next_object1[1], width, height)
        if next_object2:self.game.platarforms_nexts[1]=Rect(next_object2[0],next_object2[1], width, height)
        if next_object3:self.game.platarforms_nexts[2]=Rect(next_object3[0],next_object3[1], width, height)
        if next_object4:self.game.platarforms_nexts[3]=Rect(next_object4[0],next_object4[1], width, height)