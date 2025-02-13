import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Game:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Pelement")
        self.jp_font = pyxel.Font("umplus_j10r.bdf")
        pyxel.run(self.update, self.draw)

    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        pyxel.text(SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 - 4, "Pelement", pyxel.COLOR_WHITE)


Game()