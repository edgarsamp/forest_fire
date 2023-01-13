import mesa

class TreeCell(mesa.Agent):
    """
    A tree cell.

    Attributes:
        x, y: Grid coordinates
        condition: Can be "Fine", "On Fire", or "Burned Out"
        unique_id: (x,y) tuple.
        biomass: Amount of agent biomass

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """

    def __init__(self, pos, model, biomass):
        """
        Create a new tree.
        Args:
            pos: The tree's coordinates on the grid.
            model: standard model reference for agent.
            biomass: Amount of agent biomass
        """
        super().__init__(pos, model)
        self.biomass = max(0, biomass)
        self.pos = pos
        self.condition = "Fine"

    def step(self):
        """
        If the tree is on fire, spread it to nearby trees and reduce their biomass by 1. If nearby trees are not on fire, put out the fire on the tree.
        """
        if self.condition == "On Fire":
            neighbors = self.model.grid.iter_neighbors(self.pos, True)
            neighborsConditions = []
            for neighbor in neighbors:
                neighborsConditions.append(neighbor.condition)
                if neighbor.condition == "Fine":
                    neighbor.condition = "On Fire"

            if not ("On Fire" in neighborsConditions):
                self.condition = "Partially Burnt"

            
            self.biomass = max(0, self.biomass-1)
            if self.biomass == 0:
                self.condition = "Burned Out"
