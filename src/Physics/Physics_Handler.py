class PhysicsHandler:
    def __init__(self, gravity=0.25):
        self.gravity = gravity
    def apply_gravity(self, player):
        player.dy += self.gravity
        player.rect.y += player.dy