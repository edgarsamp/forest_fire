# Forest Fire Model

## Resumo

Para criar este modelo foi utilizado como base o exemplo [forest fire model](https://github.com/projectmesa/mesa-examples/tree/main/examples/forest_fire) do framework Mesa e adicionado . 



## Como executar

Para a execução do programa é necessário ter o Python 3.8 ou maior instalado em seu computador.



Primeiramente é necessario instalar os requisitos, para isso execute:

```
    pip install -r requirements.txt
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

To view and run the model analyses, use the ``Forest Fire Model`` Notebook.

## Files

### ``forest_fire/model.py``

This defines the model. There is one agent class, **TreeCell**. Each TreeCell object which has (x, y) coordinates on the grid, and its condition is *Fine* by default. Every step, if the tree's condition is *On Fire*, it spreads the fire to any *Fine* trees in its [Von Neumann neighborhood](http://en.wikipedia.org/wiki/Von_Neumann_neighborhood) before changing its own condition to *Burned Out*.

The **ForestFire** class is the model container. It is instantiated with width and height parameters which define the grid size, and density, which is the probability of any given cell having a tree in it. When a new model is instantiated, cells are randomly filled with trees with probability equal to density. All the trees in the left-hand column (x=0) are set to *On Fire*.

Each step of the model, trees are activated in random order, spreading the fire and burning out. This continues until there are no more trees on fire -- the fire has completely burned out.


### ``forest_fire/server.py``

This code defines and launches the in-browser visualization for the ForestFire model. It includes the **forest_fire_draw** method, which takes a TreeCell object as an argument and turns it into a portrayal to be drawn in the browser. Each tree is drawn as a rectangle filling the entire cell, with a color based on its condition. *Fine* trees are green, *On Fire* trees red, and *Burned Out* trees are black.

## Further Reading

Read about the Forest Fire model on Wikipedia: http://en.wikipedia.org/wiki/Forest-fire_model

This is directly based on the comparable NetLogo model:

Wilensky, U. (1997). NetLogo Fire model. http://ccl.northwestern.edu/netlogo/models/Fire. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

