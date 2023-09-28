from pico2d import *
from multiprocessing import Process

TUK_WIDTH, TUK_HEIGHT = 640, 512
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def move_events(p1, p2, i):
    global running
    global x, y

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    t = i / 100
    x = (1 - t) * x1 + t * x2
    y = (1 - t) * y1 + t * y2

    pass

def mouse_events():
    global running
    global cursor_x, cursor_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursor_x, cursor_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            X, Y = event.x, TUK_HEIGHT - 1 - event.y
            points.append((X, Y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
cursor_x, cursor_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

frame = 0

points = [(x, y)]

last_count = 1
counts = 0

hide_cursor()

while running:
        clear_canvas()

        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        mouse_events()
        hand_arrow.draw(cursor_x, cursor_y)
        character.clip_draw(frame*100, 100*1, 100, 100, x, y)
        update_canvas()

        if(counts<len(points)-1):
            for i in range(0, 100+1, 1):

                TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
                mouse_events()
                hand_arrow.draw(cursor_x, cursor_y)
                for ii in range(last_count, len(points)):
                    hand_arrow.draw(points[ii][0],points[ii][1])



                character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
                move_events(points[counts], points[counts + 1], i)
                frame = (frame + 1) % 8
                delay(0.01)

                update_canvas()

            counts += 1
            last_count += 1
