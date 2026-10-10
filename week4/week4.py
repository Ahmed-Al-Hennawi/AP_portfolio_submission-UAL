import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return mo,


@app.cell
def _():
    import numpy as np
    import time
    import random
    return np, random, time


@app.cell
def _():
    import matplotlib.pyplot as plt
    return plt,


@app.cell
async def _():
    # Dynamically fetch NetworkX in the browser (WASM) environment
    try:
        import networkx as nx
    except ModuleNotFoundError:
        import micropip
        await micropip.install("networkx")
        import networkx as nx
    return nx,


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1:
    Implement the Linear Search Algorithm for an arbitrary input array
    """)
    return


@app.cell
def _(mo):
    def search(arr, val):
        # Traverse through the array linearly
        for i in range(len(arr)):
            if arr[i] == val:
                return i
        return -1

    output_t1 = mo.show_code()
    output_t1
    return (search,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2
    Create an array of 500 elements, where the array is not sorted and has elements from 0 to 499 with no repetitions (Hint: use ```np.arange()``` and then ```np.random.shuffle()```).
    Then, call the ```search()``` function to find number 10 in the array. Calculate the time it takes to find the number.
    """)
    return


@app.cell
def _(mo, np, search, time):
    arr_500 = np.arange(500)

    np.random.shuffle(arr_500)

    start_time = time.time()

    found_index = search(arr_500, 10)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Value 10 found at index: {found_index}")
    print(f"Time taken for linear search: {execution_time:.8f} seconds")

    output_t2 = mo.show_code()
    output_t2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3
    Repeat the process in Task 2 for 1000 different arrays (all of them of size 500), and store the time for each one of these runs. Then plot a frequency histogram for the time values.
    """)
    return


@app.cell
def _(mo, np, plt, search, time):
    search_times = []

    for _ in range(1000):
        temp_arr = np.arange(500)
        np.random.shuffle(temp_arr)

        t_start = time.time()
        search(temp_arr, 10)
        t_end = time.time()

        search_times.append(t_end - t_start)

    # Plotting the frequency histogram
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(search_times, bins=30, color='skyblue', edgecolor='black')
    ax.set_title('Frequency Histogram of Linear Search Execution Times')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Frequency')

    output_t3 = mo.vstack([
        mo.show_code(),
        fig
    ])
    output_t3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4:
    Implement the Binary Search Algorithm for a sorted input array.
    """)
    return


@app.cell
def _(mo):
    def binSearch(arr, val):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    output_t4 = mo.show_code()
    output_t4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5:
    Implement the Recursive Binary Search Algorithm for a sorted input array.
    """)
    return


@app.cell
def _(mo):
    def binSearchRec(arr, left, right, val):
        # Check base case: range is valid
        if right >= left:
            mid = (left + right) // 2

            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                return binSearchRec(arr, left, mid - 1, val)
            else:
                return binSearchRec(arr, mid + 1, right, val)
        else:
            return -1

    output_t5 = mo.show_code()
    output_t5
    return


@app.cell
def _(mo, nx, plt):
    def binary_search_tree(arr, val):
        tree = []
        node_id = 0

        def helper(left, right, parent):
            nonlocal node_id
            if left > right:
                return

            curr_id = node_id
            node_id += 1
            current_sub = list(arr[left:right+1])
            mid = (left + right) // 2
            mid_val = arr[mid]

            # Node labels and coloring based on binary search decision
            if mid_val == val:
                # Mark as found (Green)
                tree.append(
                    (curr_id, parent, f"{current_sub}\nMid: {mid_val}\nFound!", "lightgreen"))
                return
            elif mid_val < val:
                tree.append(
                    (curr_id, parent, f"{current_sub}\nMid: {mid_val}", "lightblue"))

                # Show discarded branch (Red)
                disc_id = node_id
                node_id += 1
                tree.append(
                    (disc_id, curr_id, f"Discarded:\n{list(arr[left:mid+1])}", "lightcoral"))

                helper(mid + 1, right, curr_id)
            else:
                tree.append(
                    (curr_id, parent, f"{current_sub}\nMid: {mid_val}", "lightblue"))

                # Show discarded branch (Red)
                disc_id = node_id
                node_id += 1
                tree.append(
                    (disc_id, curr_id, f"Discarded:\n{list(arr[mid:right+1])}", "lightcoral"))

                helper(left, mid - 1, curr_id)

        helper(0, len(arr)-1, None)
        return tree

    def build_graph(tree, step):
        G = nx.DiGraph()
        # Step limits how many elements of the tree trace we add
        nodes_to_show = min(step, len(tree))
        for i in range(nodes_to_show):
            node, parent, label, color = tree[i]
            G.add_node(node, label=label, color=color)
            if parent is not None:
                G.add_edge(parent, node)
        return G

    def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        if not nx.is_tree(G):
            return nx.spring_layout(G)
        if root is None:
            root = next((n for n, d in G.in_degree() if d == 0), None)
        if root is None:
            return {}

        def recurse_pos(G, node, left, right, vert_loc, pos):
            children = list(G.successors(node))
            pos[node] = ((left + right) / 2, vert_loc)
            if len(children) != 0:
                dx = (right - left) / len(children)
                nextx = left
                for child in children:
                    recurse_pos(G, child, nextx, nextx + dx,
                                vert_loc - vert_gap, pos)
                    nextx += dx

            return pos

        return recurse_pos(G, root, 0, width, vert_loc, {})

    def draw_tree(G):
        if len(G.nodes) == 0:
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.axis("off")
            return mo.mpl.interactive(fig)

        pos = hierarchy_pos(G)
        labels = nx.get_node_attributes(G, "label")
        colors = [nx.get_node_attributes(G, "color").get(
            n, "lightblue") for n in G.nodes()]

        fig, ax = plt.subplots(figsize=(8, 5))
        nx.draw(
            G, pos,
            ax=ax,
            with_labels=True,
            labels=labels,
            node_size=2000,
            node_color=colors,
            font_size=8,
            node_shape="s",
            bbox=dict(facecolor="white", edgecolor='black',
                      boxstyle='round,pad=0.3')
        )
        ax.axis("off")
        return mo.mpl.interactive(fig)

    output_ft = mo.show_code()
    output_ft
    return binary_search_tree, build_graph, draw_tree, hierarchy_pos


@app.cell
def _(mo):
    arr_input = mo.ui.text(
        label="Enter sorted array (comma-separated)", value="1,2,3,4,5,6,7,8")
    val_input = mo.ui.text(label="Value to search", value="6")
    next_btn = mo.ui.button(label="Next Step ▶️")
    reset_btn = mo.ui.button(label="🔄 Reset")
    return arr_input, next_btn, reset_btn, val_input


@app.cell
def _(mo):
    # State mechanism to track the current step of the interactive visualization
    get_count, set_count = mo.state(1)
    return get_count, set_count


@app.cell
def _(get_count, next_btn, set_count):
    # Increment state on next click
    next_btn
    set_count(get_count() + 1)
    return


@app.cell
def _(reset_btn, set_count):
    # Reset state to step 1
    reset_btn
    set_count(1)
    return


@app.cell
def _(
    arr_input,
    binary_search_tree,
    build_graph,
    draw_tree,
    get_count,
    mo,
    next_btn,
    reset_btn,
    val_input,
):
    # Parse inputs
    arr_text = arr_input.value
    arr = [int(x.strip()) for x in arr_text.split(",") if x.strip().isdigit()]
    arr.sort()

    try:
        val = int(val_input.value)
    except ValueError:
        val = 6  # Default fallback

    # Build the tree trace based on inputs
    tree = binary_search_tree(arr, val)

    # Render the current step
    step = min(get_count(), len(tree))
    G = build_graph(tree, step)

    # Combine controls and visualization
    layout = mo.vstack([
        mo.hstack([arr_input, val_input]),
        mo.hstack([reset_btn, next_btn]),
        mo.md(f"### Step {step}/{len(tree)}"),
        draw_tree(G),
    ])

    output_layout = mo.vstack([
        mo.show_code(),
        layout
    ])
    output_layout
    return arr, arr_text, G, layout, output_layout, step, tree, val


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()