For the code to work with the dice.png you need to change the line:
frames = strip_from_sheet(sheet, (0,0), (54,95), 1, 28)

to:

frames = strip_from_sheet(sheet, (0,0), (36,36), 1, 6) on line 16

and

sheet = pg.image.load('spritesheet.png')
to
sheet = pg.image.load('dice.png')