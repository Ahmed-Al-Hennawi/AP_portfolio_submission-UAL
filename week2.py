import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import time
    import matplotlib.pyplot as plt

    return mo, np, plt, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercises
    """)
    return


@app.cell
def _(mo):
    # Create the button
    counter_button = mo.ui.button(
        value=0, on_click=lambda value: value + 1, label="increment"
    )
    return (counter_button,)


@app.cell
def _(counter_button, mo, np):
    # Read the button's value and generate the array
    _ = counter_button.value
    a = np.random.randint(1, 100, 10)

    layout = mo.vstack([
        counter_button,
        mo.md(f"**Array:**\n\n{a}")
    ])

    layout
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 1:
    Create an array of 100 random elements. Then, for each element "i", print "Element number i is X".
    """)
    return


@app.cell
def _(mo, np):
    def print_elements():
        random_num = np.random.rand(100)
        for i, val in enumerate(random_num):
            print(f"Element number {i+1} is {val:.4f}")

    print_elements()

    # Show the code in App View
    output_t1 = mo.show_code()
    output_t1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 2
    Create a function that inputs an array and an integer "n", and it outputs the first element of the array that is greater or equal than "n"
    """)
    return


@app.cell
def _(mo):
    def find_first_bigger(arr, n):
        for x in arr:
            if x >= n:
                return x
        return f"No element greater than or equal to {n}"

    print("First bigger than 888:", find_first_bigger(
        [2, 4, 7, 22, 47, 666, 333, 777], 888))
    print("First bigger than 20:", find_first_bigger(
        [2, 4, 7, 22, 47, 666, 333, 777], 20))

    # Show the code in App View
    output_t2 = mo.show_code()
    output_t2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 3
    Create a function that takes an array and an integer "n" and outputs the element of the array that is closest to "n"
    """)
    return


@app.cell
def _(mo):
    def find_closest(arr, n):
        if not arr:
            return None

        closest_element = arr[0]
        min_diff = abs(arr[0] - n)

        for x in arr:
            current_diff = abs(x - n)
            if current_diff < min_diff:
                min_diff = current_diff
                closest_element = x

        return closest_element

    print("Closest to 23 is:", find_closest([10, 20, 30, 40, 50], 23))

    # Show the code in App View
    output_t3 = mo.show_code()
    output_t3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 4
    Create a function that takes an array and it goes through it without doing anything. The function returns the time it took to transverse the array
    """)
    return


@app.cell
def _(mo, time):
    def measure_traversal_time(arr):
        start = time.time()
        for _x in arr:
            pass
        return time.time() - start

    # Test with a large array
    test_time = measure_traversal_time([0] * 1000000)
    print(f"Time to traverse 1,000,000 elements: {test_time:.6f} seconds")

    # Show the code in App View
    output_t4 = mo.show_code()
    output_t4
    return (measure_traversal_time,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 5
    Using matplotlib, plot x vs y where x is the size of the array from the previous task and y is the time it takes to call the function from previous task
    """)
    return


@app.cell
def _(measure_traversal_time, mo, plt):
    sizes = [10, 100, 1000, 2500, 10000, 50000, 100000]
    times = []

    for s in sizes:
        temp_arr = [0] * s
        times.append(measure_traversal_time(temp_arr))

    # Build the figure
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(sizes, times, marker='o', linestyle='-', color='b')
    ax.set_title("Array Traversal Time vs Size")
    ax.set_xlabel("Array Size")
    ax.set_ylabel("Time (seconds)")
    ax.grid(True)

    # Stack the code on top of the graph so both show in App View!
    output_t5 = mo.vstack([
        mo.show_code(),
        fig
    ])
    output_t5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 6
    Create a function that sorts an array of numbers
    """)
    return


@app.cell
def _(mo):
    def sort_array(arr):
        # Using bubble sort
        a = arr.copy()
        n = len(a)

        for i in range(n):
            for j in range(0, n - i - 1):
                if a[j] > a[j+1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

        return a

    print("Sorted array:", sort_array([4, 7, 54, 97, 34, 16]))

    # Show the code in App View
    output_t6 = mo.show_code()
    output_t6
    return


if __name__ == "__main__":
    app.run()
