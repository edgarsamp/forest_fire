import mesa
from .model import ForestFire

COLORS = {"Fine": "#00AA00", "On Fire": "#880000", "Burned Out": "#000000", "Partially Burnt": "#ffa600"}
TREE_COLORS = {"Fine": "#00AA00", "On Fire": "#880000",  "Partially Burnt": "#ffa600"}

def forest_fire_portrayal(tree):
    if tree is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = tree.pos
    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = COLORS[tree.condition]
    return portrayal

canvas_element = mesa.visualization.CanvasGrid(
    forest_fire_portrayal, 100, 100, 500, 500
)
tree_chart = mesa.visualization.ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

tree_bar_chart = mesa.visualization.BarChartModule(
    [{"Label": label, "Color": color} for (label, color) in TREE_COLORS.items()]
)
pie_chart = mesa.visualization.PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

model_params = {
    "height": 100,
    "width": 100,
    "density": mesa.visualization.Slider("Tree density", 0.65, 0.01, 1.0, 0.01),
    "biomass": mesa.visualization.Slider("Average biomass", 1, 1, 10, 1),
    "variation": mesa.visualization.Slider("Biomass variation", 2, 0, 5, 1),
}

server = mesa.visualization.ModularServer(
    ForestFire,
    [canvas_element, tree_chart, tree_bar_chart, pie_chart],
    "Forest Fire",
    model_params,
)