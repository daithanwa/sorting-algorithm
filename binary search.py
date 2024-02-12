import pyglet
import random

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

window = pyglet.window.Window(width=990, height=300, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

numbers = sorted(random.sample(range(1, 100), 15) + [59])

left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 59:
            found = True
        elif numbers[mid] < 59:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

pyglet.clock.schedule_interval(lambda dt: binary_search(), 1)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        x = i * 60 + 10
        y = window.height // 2
        width = 50
        height = 50

        if left <= i <= right and not search_complete:
            color = hex_to_rgb('#FFB3C6')  
        elif i == mid and not search_complete:
            color = hex_to_rgb('#FCF300')  
        elif found and i == mid:
            color = hex_to_rgb('#00F5D4') 
        else:
            color = hex_to_rgb('#EDF2FB') 

        border_radius = 7 
        pyglet.shapes.BorderedRectangle(x, y, width, height, border_radius, color=color, batch=batch).draw()
        label_color = (0, 0, 0, 255)
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', color=label_color , batch=batch)
        label.draw()

pyglet.app.run()