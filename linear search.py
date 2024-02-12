import pyglet
import random
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

window = pyglet.window.Window(width=990, height=300, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

numbers = random.sample(range(1, 100), 15) + [59]
random.shuffle(numbers)

current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 59:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

pyglet.clock.schedule_interval(lambda dt: linear_search(), 1)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        x = i * 60 + 10
        y = window.height // 2
        width = 50
        height = 50

        if i == current_index and not search_complete:
             color = hex_to_rgb('#FFB3C6')
        elif i == found_index:
             color = hex_to_rgb('#00F5D4')
        else:
             color = hex_to_rgb('#EDF2FB')

        border_radius = 7 
        pyglet.shapes.BorderedRectangle(x, y, width, height, border_radius, color=color, batch=batch).draw()
        label_color = (0, 0, 0, 255)
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', color=label_color, batch=batch)
        label.draw()

pyglet.app.run()