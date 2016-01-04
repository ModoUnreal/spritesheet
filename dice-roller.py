import pygame as pg
pg.init()

def strip_from_sheet(sheet, start, size, columns, rows=1):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames

screen = pg.display.set_mode((600,400))
screen_rect = screen.get_rect()
done = False
sheet = pg.image.load('spritesheet.png')
frames = strip_from_sheet(sheet, (0,0), (54,95), 1, 28)
frame = 0
image = frames[frame]
image_rect = image.get_rect(center=screen_rect.center)
timer = 0


while not done:
    for event in pg.event.get():
        if event == pg.QUIT:
            done = True
    screen.blit(image, image_rect)
    if pg.time.get_ticks()-timer > 1000:
        timer = pg.time.get_ticks()
        frame += 1
        if frame >= len(frames):
            frame = 0
        image = frames[frame]
        image_rect = image.get_rect(center=screen_rect.center)
    pg.display.update()

pg.quit()
