#board
BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

#solider
SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part

#flag
FLAG_ROWS = 3
FLAG_COLS = 4

#mines
MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3

#images
EXPLOTION_IMG = "explotion.png"
FLAG_IMG = "flag.png"
GRASS_IMG = "grass.png"
GUARD_IMG = "guard.png"
INJURY_IMG = "injury.png"
MINE_IMG = "mine.png"
SNAKE_IMG = "snake.png"
SOLDIER_IMG = "soldier.png"
SOLDIER_NIGHT_IMG = "soldier_night.png"
TELEPORT_IMG = "teleport.png"

#colors
BACKGROUND_COLOR = (76, 177, 45)

#Grass
GRASS_AMOUNT = 20
GRASS_HEIGHT = FLAG_ROWS * CELL_SIZE - 2
GRASS_WIDTH = FLAG_COLS * CELL_SIZE - 20

#Mine
MINE_SIGN=1
GRASS_SIGN=0
SOLIDER_SIGN=2
FLAG_SIGN=3

#Night Vision
GRID_COLOR = (0,0,0)