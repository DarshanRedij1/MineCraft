from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController



app = Ursina()


wooden_plank_texture = load_texture('Wooden Plank.png')
stone_texture = load_texture('Stone Block.png')
diamond_texture = load_texture('Diamond Block.png')
wood_texture    = load_texture('Wood Block.png')
water_texture     = load_texture('Water Block.png')
texture_list = [stone_texture]
block_pick = 1

def update():
    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = stone_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color= color.color(0,0,random.uniform(0.8,1))


        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: voxel = Voxel(position= self.position + mouse.normal, texture=stone_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=diamond_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=wood_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=water_texture)
                if block_pick == 5: voxel = Voxel(position=self.position + mouse.normal, texture=wooden_plank_texture)

            if key == 'right mouse down':
                destroy(self)


for z in range(30):
    for x in range(30):
        voxel = Voxel((x,0,z))


player = FirstPersonController()
app.run()