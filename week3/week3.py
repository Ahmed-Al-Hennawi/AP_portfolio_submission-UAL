import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo,


@app.cell
def _():
    import numpy as np
    import time
    import random
    import sys
    return np, random, sys, time


@app.cell
async def _():
    # Dynamically fetch Plotly in the browser (WASM) environment
    try:
        import plotly.graph_objects as go
    except ModuleNotFoundError:
        import micropip
        await micropip.install("plotly")
        import plotly.graph_objects as go
    return go,


@app.cell
def _(sys):
    print(sys.executable)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 1: Insertion sort
    From the discussion in class, implement insertion sort.
    """)
    return


@app.cell
def _(mo):
    def insertionSort(arr):
        for i in range(1, len(arr)):
            j = i - 1
            k = arr[i]
            while (arr[j] > k and j >= 0):
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = k
        return arr

    insertionSort([34, 1, 3, 12, 13, 5, 24524, 1, 2])

    output_t1 = mo.show_code()
    output_t1
    return (insertionSort,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 2:
    Calculate the time that Insertion Sort takes to sort an array of 1000 random elements.

    Hint: Use the *time* library and *time.time()* method to get the instant time of execution
    """)
    return


@app.cell
def _(insertionSort, mo, random, time):
    # Generating 1000 random elements
    random_array = [random.randint(0, 10000) for _ in range(1000)]

    start_time = time.time()
    insertionSort(random_array)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Time taken to sort 1000 elements: {execution_time:.6f} seconds")

    output_t2 = mo.show_code()
    output_t2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 3: Bubble sort
    Now implement Bubble Sort
    """)
    return


@app.cell
def _(mo):
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    output_t3 = mo.show_code()
    output_t3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    -----------------------------------------------------------
    ### Final Task (for next week)
    """)
    return


@app.cell
def _(mo):
    dropdown = mo.ui.dropdown(
        options=["bubble", "insertion", "selection"], value="bubble", label="Sorting algorithm:"
    )
    reset_button = mo.ui.button(label="Reset")
    next_button = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="Increment")
    return dropdown, next_button, reset_button


@app.cell
def _(np, reset_button):
    # By depending on reset_button.value, this cell re-runs when the button is clicked, resetting the state.
    _ = reset_button.value

    n = 75  # size of the array
    state = {
        "arr": np.random.randint(0, 100, n),
        "i": 0
    }
    return n, state


@app.cell
def _(dropdown, go, mo, n, next_button, np, reset_button, state):
    arr = state["arr"]
    colors = ["skyblue"] * n
    info_msg = ""

    # Logic runs reactively when next_button is clicked
    match dropdown.value:
        case "bubble":
            info_msg = "Bubble Sort: Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order."
            if next_button.value > 0 and state["i"] < n - 1:
                for j in range(n - state["i"] - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                state["i"] += 1

            if state["i"] < n:
                for k in range(n - state["i"], n):
                    colors[k] = "lightgreen"
            else:
                colors = ["lightgreen"] * n

        case "insertion":
            info_msg = "Insertion Sort: Builds the final sorted array one item at a time by inserting elements into their correct position."
            if state["i"] == 0:
                state["i"] = 1

            if next_button.value > 0 and state["i"] < n:
                curr_idx = state["i"]
                key = arr[curr_idx]
                j = curr_idx - 1
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
                state["i"] += 1

            for k in range(0, state["i"]):
                colors[k] = "lightgreen"

        case "selection":
            info_msg = "Selection Sort: Divides the list into a sorted and unsorted region, repeatedly selecting the smallest element from the unsorted region."
            if next_button.value > 0 and state["i"] < n - 1:
                curr_idx = state["i"]
                min_idx = curr_idx
                for j in range(curr_idx + 1, n):
                    if arr[j] < arr[min_idx]:
                        min_idx = j
                arr[curr_idx], arr[min_idx] = arr[min_idx], arr[curr_idx]
                state["i"] += 1

            for k in range(0, state["i"]):
                colors[k] = "lightgreen"

    # Visualization
    fig = go.Figure(
        data=[go.Bar(x=np.arange(n), y=arr, marker_color=colors)]
    )
    fig.update_layout(
        title=f"{dropdown.value.capitalize()} Sort Step {state['i']}",
        xaxis_title="Index",
        yaxis_title="Value",
        template="plotly_white",
        width=650,
        height=400
    )

    # Combine UI controls and the plot into one unified view
    layout = mo.vstack([
        mo.md(f"**{info_msg}**"),
        mo.hstack([dropdown, reset_button, next_button]),
        mo.ui.plotly(fig)
    ])

    output_layout = mo.vstack([
        mo.show_code(),
        layout
    ])

    output_layout
    return (output_layout,)


@app.cell
def _(output_layout):
    output_layout
    return


if __name__ == "__main__":
    app.run()