from game.Sistem import *


p = Player(None, 0, 0, None)
p.move_to(4000, 2300)
t = time.time()
i = 0
while True:
    if time.time() - t > 0.1:
        p.made_step()
        t = time.time()
        i += 1
