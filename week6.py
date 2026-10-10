import marimo

__generated_with = "0.23.8"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import random
    import numpy as np

    return np, random


@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


@app.cell
async def _():
    # In a WebAssembly (WASM) browser environment, plotly might not be 
    # installed by default. This safely fetches and installs it!
    try:
        import plotly.graph_objects as go
    except ModuleNotFoundError:
        import micropip
        await micropip.install("plotly")
        import plotly.graph_objects as go
    return (go,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Example 1: Maxone
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1: Initialisation
    Implement the ```createInital(nInd,nBits)``` function that creates ```nInd``` arrays of ```nBits``` bits each one, where each bit is 1 or 0 with 50% chance.
    """)
    return


@app.cell
def _(mo, random):
    def createInitial(nInd, nBits):
        population = []
        for _ in range(nInd):
            individual = [random.choice([0, 1]) for _ in range(nBits)]
            population.append(individual)
        return population

    output_t1 = mo.show_code()
    output_t1
    return (createInitial,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2: Evaluation
    Implement the ```fitness(individual)``` function that receives an array ```individual``` and it returns ```nOnes```, the number of ones that the array contains (you can assume the array only contains zeros or ones).
    """)
    return


@app.cell
def _(mo):
    def fitness(individual):
        return sum(individual)

    output_t2 = mo.show_code()
    output_t2
    return (fitness,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3: Selection
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Implement the ```selectThreeWinners(population)``` function, that takes as an input the whole population. This function should do the following:
    1. Select randomly two individuals from ```population```, then compare their fitness and select the one with highest fitness. This individual is called ```firstWinner```
    2. Repeat the above step twice, in order to obtain ```secondWinner``` and ```thirdWinner```
    3. Return ```firstWinner```,```secondWinner```, and ```thirdWinner```

    You can use the ```random.sample(population,k)``` for randomly extract ```k``` elements from ```population```
    """)
    return


@app.cell
def _(fitness, mo, random):
    def selectThreeWinners(population):
        winners = []
        for _ in range(3):
            candidates = random.sample(population, 2)
            if fitness(candidates[0]) > fitness(candidates[1]):
                winners.append(candidates[0])
            else:
                winners.append(candidates[1])
        return winners[0], winners[1], winners[2]

    output_t3 = mo.show_code()
    output_t3
    return (selectThreeWinners,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4: Crossover
    Implement the ```crossover(parent1,parent2)``` function, that takes as an input two individuals ```parent1``` and ```parent2``` and returns ```firstChild``` and ```secondChild``` which are obtained with the following procedure:
    1. Create a random crossover point x, with ```x=[1,len(parent1)-1]```
    2. Create ```firstChild```, an array containing the same elements from ```parent1``` from index 0 to x-1, and containing the same elements from ```parent2``` from index x to len(parent)-1.
    3. Create ```secondChild``` as the inverse combination from ```firstChild```
    """)
    return


@app.cell
def _(mo, random):
    def crossover(parent1, parent2):
        x = random.randint(1, len(parent1) - 1)
        firstChild = parent1[:x] + parent2[x:]
        secondChild = parent2[:x] + parent1[x:]
        return firstChild, secondChild

    output_t4 = mo.show_code()
    output_t4
    return (crossover,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5: Mutation
    Implement the ```mutation(individual,pMut)``` function, that takes as an input an array ```individual``` and ```pMut```, the probability of mutation, and for each element of ```individual``` it changes its value (from 0 to 1 or from 1 to 0) with probability ```pMut```
    """)
    return


@app.cell
def _(mo, random):
    def mutation(individual, pMutation):
        mutated = []
        for bit in individual:
            if random.random() < pMutation:
                mutated.append(1 - bit)
            else:
                mutated.append(bit)
        return mutated

    output_t5 = mo.show_code()
    output_t5
    return (mutation,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Putting all together
    Now we implement our ```runGA()``` function, that will call every other function we created.
    """)
    return


@app.cell
def _(createInitial, crossover, fitness, mo, mutation, selectThreeWinners):
    def runGA(totalIndividuals, numberBits, numberIterations, pMutation):
        fitnesses = []
        population = createInitial(totalIndividuals, numberBits) 

        for _k in range(numberIterations):
            winners = selectThreeWinners(population)
            next_gen = []  

            for i in [0, 1]:
                for j in range(i + 1, 3):
                    children = crossover(winners[i], winners[j])
                    next_gen.append(children[0])
                    next_gen.append(children[1])

            for i in range(len(next_gen)):
                next_gen[i] = mutation(next_gen[i], pMutation)

            population.sort(key=fitness)  
            population = population[6:]  
            population = population + next_gen  

            fitnesses.append(max([fitness(ind) for ind in population]))

        return fitnesses  

    output_run = mo.show_code()
    output_run
    return (runGA,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we call the function with specific values for the parameters
    """)
    return


@app.cell
def _(mo, plt, runGA):
    _fit = runGA(100, 50, 100, 0.01)

    fig_ga, ax_ga = plt.subplots(figsize=(8, 4))
    ax_ga.plot(range(100), _fit, color='blue', marker='o', markersize=3)
    ax_ga.set_title("Genetic Algorithm: Maxone Progress")
    ax_ga.set_xlabel("Generation")
    ax_ga.set_ylabel("Max Fitness (Number of 1s)")
    ax_ga.grid(True)

    output_plot = mo.vstack([
        mo.show_code(),
        fig_ga
    ])
    output_plot
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6:
    Explore modifying the selection and crossover processes to achieve a better fitness. You can also modify how the ```next_gen``` is being defined in ```runGA()```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Example 2: Maximising a real-valued function
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We want to find the values $x^{*}$ and $y^{*}$ such that $f(x,y)=-(x+y)^2$ has a maximum.

    We can start with random arrays of two elements $[x_0,y_0]$ where $x_0,y_0\in[-1,1]$ and use genetic algorithm to see if we find the optimal solution.

    Let's visualise $f(x,y)$:
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    plt.rcParams['figure.dpi'] = 150

    from matplotlib import cm
    _fig, _ax = plt.subplots(subplot_kw={'projection': '3d'})
    _X = np.arange(-5, 5, 0.25)
    _Y = np.arange(-5, 5, 0.25)
    _X, _Y = np.meshgrid(_X, _Y)
    _Z = -(_X ** 2 + _Y ** 2)
    _surf = _ax.plot_surface(_X, _Y, _Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    _ax.set(xlabel='X', ylabel='Y', zlabel='Z')
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------------
    ## Final Task:
    Implement the following functions to run a genetic algorithm for the problem stated above.
    Your algorithm should do the following:
    - Create an initial population of 100 points scattered randomnly in the range $x=[-1,1]$ and $y=[-1,1]$
    - Calculate the fitness of each point is given by evaluating the point in the function $f(x,y)$.
    - Selection process is similar as Example 1 (i.e. selecting three winners)
    - You can implement whatever crossover you consider adequate.
    - For each step, each individual suffers a mutation on each of its coordinates $x$ and $y$ which are modified by a random noise $\delta$, where $\delta=[-0.05,0.05]$ (uniformly distributed).
    - Implement the ```runGA_1()``` function so it runs 100 iterations of the algorithm. Check if the points converge to a solution.

    **EXTRA TASK ADDED BELOW:** A fully interactive 3D slider to watch the points converge over generations!
    """)
    return


@app.cell
def _(mo, random):
    def createInitial_1(nInd=100):
        population = []
        for _ in range(nInd):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            population.append([x, y])
        return population

    def fitness_1(individual):
        x, y = individual[0], individual[1]
        return -(x**2 + y**2)

    def selectThreeWinners_1(population):
        winners = []
        for _ in range(3):
            candidates = random.sample(population, 2)
            if fitness_1(candidates[0]) > fitness_1(candidates[1]):
                winners.append(candidates[0])
            else:
                winners.append(candidates[1])
        return winners[0], winners[1], winners[2]

    def crossover_1(parent1, parent2):
        child1 = [parent1[0], parent2[1]]
        child2 = [parent2[0], parent1[1]]
        return child1, child2

    def mutation_1(individual):
        x = individual[0] + random.uniform(-0.05, 0.05)
        y = individual[1] + random.uniform(-0.05, 0.05)
        x = max(-1, min(1, x))
        y = max(-1, min(1, y))
        return [x, y]

    def runGA_1():
        population = createInitial_1(100)
        history = [population.copy()] 

        for _ in range(100):
            winners = selectThreeWinners_1(population)
            next_gen = []

            for i in range(2):
                for j in range(i + 1, 3):
                    child1, child2 = crossover_1(winners[i], winners[j])
                    next_gen.extend([child1, child2])

            for i in range(len(next_gen)):
                next_gen[i] = mutation_1(next_gen[i])

            population.sort(key=fitness_1)
            population = population[6:] + next_gen
            history.append([ind.copy() for ind in population])

        return history

    output_t_final = mo.show_code()
    output_t_final
    return (runGA_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧬 Interactive GA Visualizer
    Use the slider below to step through all 100 generations and watch your algorithm push the points to the absolute top of the function!
    """)
    return


@app.cell
def _(runGA_1):
    ga_history = runGA_1()
    return (ga_history,)


@app.cell
def _(mo):
    gen_slider = mo.ui.slider(start=0, stop=100, step=1, value=0, label="Generation: ")
    return (gen_slider,)


@app.cell
def _(ga_history, gen_slider, go, mo, np):
    current_pop = ga_history[gen_slider.value]

    x_vals = [p[0] for p in current_pop]
    y_vals = [p[1] for p in current_pop]
    z_vals = [-(x**2 + y**2) for x, y in current_pop]

    scatter = go.Scatter3d(
        x=x_vals, y=y_vals, z=z_vals,
        mode='markers',
        marker=dict(size=6, color='red', opacity=1.0, line=dict(width=1, color='black')),
        name='Individuals'
    )

    X_grid = np.linspace(-1, 1, 50)
    Y_grid = np.linspace(-1, 1, 50)
    X_grid, Y_grid = np.meshgrid(X_grid, Y_grid)
    Z_grid = -X_grid**2 - Y_grid**2

    surface = go.Surface(
        x=X_grid, y=Y_grid, z=Z_grid,
        colorscale='Viridis', opacity=0.5, showscale=False
    )

    fig = go.Figure(data=[surface, scatter])
    fig.update_layout(
        title=f"Evolution Progress - Generation {gen_slider.value} / 100",
        scene=dict(
            xaxis_title="X", yaxis_title="Y", zaxis_title="Z",
            xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1]), zaxis=dict(range=[-2, 0])
        ),
        width=750, height=600,
        margin=dict(l=0, r=0, b=0, t=40)
    )

    # Use mo.ui.plotly to ensure Pyodide renders it correctly
    chart = mo.ui.plotly(fig)

    layout_ex2 = mo.vstack([
        gen_slider,
        chart
    ])

    output_ex2 = mo.vstack([
        mo.show_code(),
        layout_ex2
    ])
    output_ex2
    return


if __name__ == "__main__":
    app.run()
