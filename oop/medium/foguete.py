class Foguete():
    def __init__(self, speed) -> None:
        self.speed = speed / 3600

        self.last_time = 0

    def atualizar(self, time):
        self.last_time += time
        pos = self.speed * (self.last_time)

        return pos
