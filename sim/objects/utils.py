from dat import THRESH_HOLD


def update_temp(self, others):

    # profiler.start()
    # find neigbours
    # include self in average

    total = 0
    if all(abs(i.temp - self.temp) <= THRESH_HOLD for i in others):
        return

    temp = 0
    for other in others:
        conduct = other.conduct * other.mass
        temp += other.temp * conduct
        total += conduct

    temp += self.temp
    total += 1

    return temp/total


def get_others(self, board):
    if self.y > 0:  # above
        yield board[self.y - 1, self.x]
        # others.append(other)

    if self.y < len(board) - 1:  # below
        yield board[self.y + 1, self.x]
        # others.append(other)

    if self.x > 0:  # left
        yield board[self.y, self.x - 1]
        # others.append(other)

    if self.x < len(board[self.y]) - 1:  # right
        yield board[self.y, self.x + 1]
        # others.append(other)
