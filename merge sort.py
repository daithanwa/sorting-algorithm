import pyglet
from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet import clock

def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

def merge_sort(arr, steps):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half, steps)
    merge_sort(right_half, steps)

    merge(arr, left_half, right_half, steps)

def merge(arr, left, right, steps):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    for k in range(len(result)):
        arr[k] = result[k]

    steps.append(arr.copy())

class Renderer(Window):
    def __init__(self):
        super().__init__(1300, 1000, "Merge Sort Algorithm")
        self.batch = Batch()
        self.x = [3, 2, 8, 4, 1, 5, 7, 6, 15, 9, 11, 13, 10, 12, 14]
        self.bars = self.create_bars()
        self.merge_sort_steps = []
        merge_sort(self.x, self.merge_sort_steps)

    def create_bars(self):
        bars = []
        for e, i in enumerate(self.x):
            bars.append(Rectangle(100 + e * 70, 150, 50, i * 40, color=hex_to_rgb('#000000'), batch=self.batch))
        return bars

    def on_update(self, deltatime):
        if not self.merge_sort_steps:
            clock.unschedule(self.on_update)
            return

        step = self.merge_sort_steps.pop(0)
        self.x = step
        self.update_bars()

    def update_bars(self):
        for e, i in enumerate(self.x):
            self.bars[e].height = i * 40

    def on_draw(self):
        self.clear()
        self.set_background_color(1, 1, 1, 1)
        self.batch.draw()

    def set_background_color(self, r, g, b, a):
        pyglet.gl.glClearColor(r, g, b, a)

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 2)
run()
