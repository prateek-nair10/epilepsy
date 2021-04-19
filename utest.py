from ursina import *

app = Ursina()

def update():
    cube.rotation_y = cube.rotation_y + time.dt*100
    cube.rotation_x = cube.rotation_x - time.dt*100
    cube.rotation_z = cube.rotation_z - time.dt*100
    cube.color = color.random_color() # set it to a random color


cube = Entity(model = 'cube', scale = (5,5,5), rotation = (90, 45, 0), color = color.cyan)

app.run()
