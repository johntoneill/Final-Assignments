import random

class AgentX:
    def __init__(self, identity, worldX):
        self.identity = identity
        self.worldX = worldX
        self.positionX = None
    
    def move(self):
        neighborsX = self.worldX.get_neighborsX(self.positionX)
        empty_patchesX = [patch for patch in neighborsX if self.worldX.is_emptyX(patch)]
        
        if empty_patchesX:
            new_positionX = random.choice(empty_patchesX)
            self.worldX.move_agentX(self, new_positionX)

class WorldX:
    def __init__(self, widthX, heightX, num_agentsX):
        self.widthX = widthX
        self.heightX = heightX
        self.gridX = [[None for _ in range(widthX)] for _ in range(heightX)]
        self.agentsX = []
        
        for iX in range(num_agentsX):
            agentX = AgentX(iX, self)
            self.agentsX.append(agentX)
            self.place_agentX(agentX)
    
    def place_agentX(self, agentX):
        xX = random.randint(0, self.widthX - 1)
        yX = random.randint(0, self.heightX - 1)
        agentX.positionX = (xX, yX)
        self.gridX[yX][xX] = agentX
    
    def move_agentX(self, agentX, new_positionX):
        xX, yX = agentX.positionX
        self.gridX[yX][xX] = None
        agentX.positionX = new_positionX
        xX, yX = new_positionX
        self.gridX[yX][xX] = agentX
    
    def get_neighborsX(self, positionX):
        xX, yX = positionX
        neighborsX = []
        for dxX in [-1, 0, 1]:
            for dyX in [-1, 0, 1]:
                if dxX == 0 and dyX == 0:
                    continue
                nxX = xX + dxX
                nyX = yX + dyX
                if 0 <= nxX < self.widthX and 0 <= nyX < self.heightX:
                    neighborsX.append((nxX, nyX))
        return neighborsX
    
    def is_emptyX(self, positionX):
        xX, yX = positionX
        return self.gridX[yX][xX] is None
    
    def display_gridX(self):
        for rowX in self.gridX:
            for cellX in rowX:
                if cellX is None:
                    print(".", end=" ")
                else:
                    print(cellX.identity, end=" ")
            print()

def mainX():
    widthX = 5
    heightX = 5
    num_agentsX = 3
    num_stepsX = 3
    
    worldX = WorldX(widthX, heightX, num_agentsX)
    
    for stepX in range(num_stepsX):
        print(f"Step {stepX + 1}:")
        worldX.display_gridX()
        for agentX in worldX.agentsX:
            agentX.move()
            print(f"Agent {agentX.identity} moved to {agentX.positionX}")
        print()

if __name__ == "__main__":
    mainX()

