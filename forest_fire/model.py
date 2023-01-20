from forest_fire.agent import TreeCell
import mesa
import random as rd

class ForestFire(mesa.Model):
    """
    Simple Forest Fire model.
    """
    def __init__(self, width=100, height=100, density=0.65, biomass=5, variation=5):
        """
        Create a new forest fire model.

        Args:
            width, height: The size of the grid to model
            density: What fraction of grid cells have a tree in them.
        """
        # Set up model objects
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.Grid(width, height, torus=False)
        self.end_check = False

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Fine": lambda m: self.count_type(m, "Fine"),
                "On Fire": lambda m: self.count_type(m, "On Fire"),
                "Burned Out": lambda m: self.count_type(m, "Burned Out"),
                "Partially Burnt": lambda m: self.count_type(m, "Partially Burnt"),
                "Alived": lambda m: self.count_types(m, "Partially Burnt", "Fine"),
            }
        )

        # Place a tree in each cell with Prob = density
        for (contents, x, y) in self.grid.coord_iter():
            if self.random.random() < density:
                # Create a 
                new_tree = TreeCell((x, y), self, rd.randint(biomass-variation, biomass+variation))
                # Set all trees in the first column on fire.
                if x == 0:
                    new_tree.condition = "On Fire"
                self.grid.place_agent(new_tree, (x, y))
                self.schedule.add(new_tree)


        self.running = True
        self.datacollector.collect(self)
    
    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()

        if self.end_check:
            self.running = False

        # Halt if no more fire
        if self.count_type(self, "On Fire") == 0:
            self.end_check = True

        # collect data
        self.datacollector.collect(self)


    @staticmethod
    def count_type(model, tree_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for tree in model.schedule.agents:
            if tree.condition == tree_condition:
                count += 1
        return count

    @staticmethod
    def count_types(model, tree_condition, tree_condition2):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for tree in model.schedule.agents:
            if tree.condition == tree_condition or tree.condition == tree_condition2:
                count += 1
        return count