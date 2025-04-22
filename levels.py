class Levels:
    def __init__(self, game, level):
        self.game = game
        self.counter = 0
        print(level)
        self.generate_bin(f'level.txt')
        
        self.map, self.sky, self.wall, self.static, self.animated, self.npc = self.read_bin(f'levels/l{level}.bin')
        print(self.static)
    
    def read_bin(self, path):
        file = open(path, 'r')
        maps = []
        wall = []
        sky = None
        static = []
        animated = []
        npc = []
        while line := file.readline():
            if line.startswith('map'):
                self.counter += 1
                continue
            if line.startswith('sky'):
                self.counter += 1
                continue
            if line.startswith('wall'):
                self.counter += 1
                continue
            if line.startswith('static'):
                self.counter += 1
                continue
            if line.startswith('animated'):
                self.counter += 1
                continue
            if line.startswith('npc'):
                self.counter += 1
                continue
            if self.counter == 1:
                row = line.split()
                maps.append([int(i) for i in row])
            if self.counter == 2:
                sky = line.split()[0]
            if self.counter == 3:
                wall.append(line.split()[0])
            if self.counter == 4:
                static_sprite = line.split()
                static.append([static_sprite[0], (float(static_sprite[1]), float(static_sprite[2])), float(static_sprite[3]), float(static_sprite[4]), static_sprite[5]=='0', (int(static_sprite[6]), int(static_sprite[7]), int(static_sprite[8]))])
            if self.counter == 5:
                animated_sprite = line.split()
                animated.append([animated_sprite[0], (float(animated_sprite[1]), float(animated_sprite[2])), float(animated_sprite[3]), float(animated_sprite[4]), animated_sprite[5]=='0', (int(animated_sprite[6]), int(animated_sprite[7]), int(animated_sprite[8]))])
            if self.counter == 6:
                npc_data = line.split()
                npc.append([npc_data[0], (float(npc_data[1]), float(npc_data[2]))], float(npc_data[3]), float(npc_data[4]))
        
        file.close()
        return maps, sky, wall, static, animated, npc
    
    def generate_bin(self, path_txt):
        with open(path_txt, 'r') as file:
            line = file.read()
        binarray = str.encode(line)
        binfile = path_txt.split('.')[0] + '.bin'
        with open(binfile, 'wb') as file:
            file.write(binarray)
        