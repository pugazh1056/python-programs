class Alien:
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
       pass

def new_aliens_collection(coordinates):
    aliens = []
    for x, y in coordinates:
        aliens.append(Alien(x, y))
    return aliens