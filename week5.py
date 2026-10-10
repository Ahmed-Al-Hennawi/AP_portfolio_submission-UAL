import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import time
    import matplotlib.pyplot as plt
    import random
    import sys

    # Increase the recursion depth to avoid RecursionError during worst-case
    # Quicksort scenarios (like sorting an already sorted array of size 1000)
    sys.setrecursionlimit(5000)
    return mo, np, plt, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mergesort and Quicksort
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this notebook, we will explore how these two algorithms behave for different inputs, varying in size and degree of order. We will see how to empirically find the best, average and worst case scenarios as we have done theoretically.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mergesort
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 1
    Implement ```mergeSort(arr)```, which takes an array ```arr``` and it sorts it using Mergesort algorithm. You are given the function ```merge(left,right)``` that merges two arrays (```left``` and ```right```) in a sorted way.
    """)
    return


@app.cell
def _(mo):
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left_half = mergeSort(arr[:mid])

        right_half = mergeSort(arr[mid:])

        return merge(left_half, right_half)

    output_t1 = mo.show_code()
    output_t1
    return (mergeSort,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 2
    Call the mergeSort() function for a sorted array of size 1000. Calculate the overall time it takes mergeSort() to run. Then, do the same for a reverse-sorted array
    """)
    return


@app.cell
def _(mergeSort, mo, time):
    # 1. Create the arrays
    sorted_arr_t2 = list(range(1000))
    reverse_arr_t2 = list(range(1000, 0, -1))

    # 2. Measure time for the sorted array
    start_t2_sorted = time.time()
    mergeSort(sorted_arr_t2)
    time_t2_sorted = time.time() - start_t2_sorted

    # 3. Measure time for the reverse-sorted array
    start_t2_reverse = time.time()
    mergeSort(reverse_arr_t2)
    time_t2_reverse = time.time() - start_t2_reverse

    print(f"Time for Sorted Array (N=1000): {time_t2_sorted:.6f} sec")
    print(f"Time for Reverse-Sorted Array (N=1000): {time_t2_reverse:.6f} sec")

    output_t2 = mo.show_code()
    output_t2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 3
    Now repeat Task 2 but now run each experiment 100 times. Plot the values of time complexity for each experiment. Do you see a statistical difference between them?
    """)
    return


@app.cell
def _(mergeSort, mo, plt, time):
    runs_sorted = []
    runs_reversed = []

    for _ in range(100):
        # Fresh arrays to prevent caching issues or sorting an already sorted array in place
        s_arr = list(range(1000))
        r_arr = list(range(1000, 0, -1))

        t0 = time.time()
        mergeSort(s_arr)
        runs_sorted.append(time.time() - t0)

        t1 = time.time()
        mergeSort(r_arr)
        runs_reversed.append(time.time() - t1)

    # Plot the results as a histogram overlapping each other
    fig_t3, ax_t3 = plt.subplots(figsize=(8, 4))
    ax_t3.hist(runs_sorted, bins=20, alpha=0.6,
               label='Sorted Array', color='blue')
    ax_t3.hist(runs_reversed, bins=20, alpha=0.6,
               label='Reversed Array', color='red')
    ax_t3.set_title('Merge Sort Time Complexity (100 Runs)')
    ax_t3.set_xlabel('Execution Time (seconds)')
    ax_t3.set_ylabel('Frequency')
    ax_t3.legend()

    output_t3 = mo.vstack([
        mo.show_code(),
        fig_t3
    ])
    output_t3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 4
    Call the mergeSort() function for three arrays of sizes 10, 100, and 1000. Do this for:
    a) Sorted array
    b) Inverse-sorted array
    c) Random array
    Plot the time complexity as a function of array size for the three cases.
    """)
    return


@app.cell
def _(mergeSort, mo, np, plt, time):
    sizes = [10, 100, 1000]
    time_sorted = []
    time_inverse = []
    time_random = []

    for size in sizes:
        # Generate arrays
        arr_s = list(range(size))
        arr_i = list(range(size, 0, -1))
        arr_r = np.random.randint(0, 10000, size).tolist()

        # Measure Sorted
        t_start = time.time()
        mergeSort(arr_s)
        time_sorted.append(time.time() - t_start)

        # Measure Inverse
        t_start = time.time()
        mergeSort(arr_i)
        time_inverse.append(time.time() - t_start)

        # Measure Random
        t_start = time.time()
        mergeSort(arr_r)
        time_random.append(time.time() - t_start)

    # Plotting line chart
    fig_t4, ax_t4 = plt.subplots(figsize=(8, 4))
    ax_t4.plot(sizes, time_sorted, marker='o', label='Sorted')
    ax_t4.plot(sizes, time_inverse, marker='s', label='Inverse')
    ax_t4.plot(sizes, time_random, marker='^', label='Random')
    ax_t4.set_title('Merge Sort: Time vs Array Size')
    ax_t4.set_xlabel('Array Size (N)')
    ax_t4.set_ylabel('Execution Time (seconds)')
    ax_t4.legend()
    ax_t4.grid(True, linestyle='--', alpha=0.6)

    output_t4 = mo.vstack([
        mo.show_code(),
        fig_t4
    ])
    output_t4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quicksort
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now implement two versions of quicksort: first using the last element as a pivot  (```Quicksort()```), and second using a random element as the pivot (```QuicksortRandom()```)
    """)
    return


@app.cell
def _(mo, np):
    def Quicksort(arr):
        # Base case
        if len(arr) <= 1:
            return arr

        # Choose the last element as pivot
        pivot = arr[-1]

        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]

        return Quicksort(left) + [pivot] + Quicksort(right)

    def QuicksortRandom(arr):
        # Base case
        if len(arr) <= 1:
            return arr

        p_idx = np.random.randint(0, len(arr))
        pivot = arr[p_idx]

        # Create a new list without the pivot element to partition the rest
        arr_rest = arr[:p_idx] + arr[p_idx+1:]

        left = [x for x in arr_rest if x <= pivot]
        right = [x for x in arr_rest if x > pivot]

        return QuicksortRandom(left) + [pivot] + QuicksortRandom(right)

    output_qs = mo.show_code()
    output_qs
    return Quicksort, QuicksortRandom


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 5
    Create an array A=[0,1,2,..,999] and then B an array of the same amount of elements but randomised (i.e. not sorted).
    Call ```Quicksort()``` and calculate how much time it takes to run for each case
    """)
    return


@app.cell
def _(Quicksort, mo, np, time):
    A = list(range(1000))
    B = list(range(1000))
    np.random.shuffle(B)

    # Time A
    t_start_A = time.time()
    Quicksort(A)
    time_A = time.time() - t_start_A

    # Time B
    t_start_B = time.time()
    Quicksort(B)
    time_B = time.time() - t_start_B

    print(f"Quicksort Time (Sorted Array A): {time_A:.6f} seconds")
    print(f"Quicksort Time (Randomised Array B): {time_B:.6f} seconds")

    output_t5 = mo.show_code()
    output_t5
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 6
    Now repeat the process for A and B 100 times each. Then store the times for each run in an array and plot them to check their differences.
    """)
    return


@app.cell
def _(A, B, Quicksort, mo, plt, time):
    qs_runs_A = []
    qs_runs_B = []

    for _ in range(100):
        # Time A runs
        t_A0 = time.time()
        Quicksort(A)
        qs_runs_A.append(time.time() - t_A0)

        # Time B runs
        t_B0 = time.time()
        Quicksort(B)
        qs_runs_B.append(time.time() - t_B0)

    fig_t6, ax_t6 = plt.subplots(figsize=(8, 4))
    ax_t6.hist(qs_runs_A, bins=20, alpha=0.6,
               label='Sorted (Worst Case)', color='red')
    ax_t6.hist(qs_runs_B, bins=20, alpha=0.6,
               label='Randomised (Average Case)', color='green')
    ax_t6.set_title('Quicksort (Last Pivot) Time Complexity (100 Runs)')
    ax_t6.set_xlabel('Execution Time (seconds)')
    ax_t6.set_ylabel('Frequency')
    ax_t6.legend()

    output_t6 = mo.vstack([
        mo.show_code(),
        fig_t6
    ])
    output_t6
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 7
    Create 1000 sorted arrays of sizes going from 0 to 999.
    For each array, call the ```Quicksort()``` function and calculate the time it takes to run it.
    Plot size against time complexity for each of the arrays.
    """)
    return


@app.cell
def _(Quicksort, mo, plt, time):
    sizes_t7 = list(range(1000))
    times_t7 = []

    for s_t7 in sizes_t7:
        arr_t7 = list(range(s_t7))  # Creating a sorted array of size 's_t7'

        t_start_t7 = time.time()
        Quicksort(arr_t7)
        times_t7.append(time.time() - t_start_t7)

    fig_t7, ax_t7 = plt.subplots(figsize=(8, 4))
    ax_t7.plot(sizes_t7, times_t7, label="Quicksort (Last Pivot)", color='red')
    ax_t7.set_title("Quicksort Time Complexity vs Size (Sorted Arrays)")
    ax_t7.set_xlabel("Array Size")
    ax_t7.set_ylabel("Time (seconds)")
    ax_t7.legend()

    output_t7 = mo.vstack([
        mo.show_code(),
        fig_t7
    ])
    output_t7
    return sizes_t7, times_t7


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 8
    Repeat Task 7 but now call ```QuicksortRandom()```.
    Compare your results in the same plot.
    """)
    return


@app.cell
def _(QuicksortRandom, mo, plt, sizes_t7, time, times_t7):
    times_t8 = []

    for s_t8 in sizes_t7:
        arr_t8 = list(range(s_t8))  # Sorted array again

        t_start_t8 = time.time()
        QuicksortRandom(arr_t8)
        times_t8.append(time.time() - t_start_t8)

    # Plotting BOTH tasks in the same graph for comparison
    fig_t8, ax_t8 = plt.subplots(figsize=(8, 5))
    # Results from Task 7
    ax_t8.plot(sizes_t7, times_t7,
               label="Quicksort (Last Pivot - Worst Case O(N^2))", color='red')
    # Results from Task 8
    ax_t8.plot(sizes_t7, times_t8,
               label="QuicksortRandom (Random Pivot - O(N log N))", color='blue')

    ax_t8.set_title("Quicksort Comparison on Sorted Arrays")
    ax_t8.set_xlabel("Array Size")
    ax_t8.set_ylabel("Time (seconds)")
    ax_t8.legend()

    output_t8 = mo.vstack([
        mo.show_code(),
        fig_t8
    ])
    output_t8
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------------------------
    ## Final Task:
    Create a **Sorting Algorithms Race** dashboard. This dashboard should include the following features (at least). The dashboard allows the user to choose two sorting algorithms and it will run them to compare which one takes less time. The particular minimum requirements of the dashboard are:
    - The user can input (through a slider or number input) the value of ```N```, the size of the array.
    - A dropdown menu allows the user to choose between sorted, random or reversed sorted array as an input for the algorithms (it should be the same array for both algorithms).
    - There are two dropdown menus that allow the user to choose which two algorithms are competing. The options should be, at least: bubble sort, insertion sort, merge sort and quick sort.
    - Once the user has set this variables, they can press **Start Race** button. This triggers that each algorithm runs 100 times. The output is a plot that shows the 100 run values for each algorithm, and also the average time for each one (averaged over the 100 runs). It also displays a message of which algorithm is the winner
    """)
    return


@app.cell
def _(mo):
    # UI Elements setup
    # Keeping default N to 100, as Bubble Sort 1000 times takes significant time
    n_input = mo.ui.slider(start=10, stop=1000, step=10,
                           value=100, label="Array Size (N): ")
    array_dropdown = mo.ui.dropdown(
        options=["Random", "Sorted", "Reversed"],
        value="Random",
        label="Input Array State: "
    )

    algo_options = ["Merge Sort", "Quick Sort",
                    "Quick Sort (Random Pivot)", "Bubble Sort", "Insertion Sort"]
    algo1_dropdown = mo.ui.dropdown(
        options=algo_options, value="Merge Sort", label="Competitor 1: ")
    algo2_dropdown = mo.ui.dropdown(
        options=algo_options, value="Quick Sort", label="Competitor 2: ")

    start_btn = mo.ui.button(
        label="🏁 Start Race",
        value=0,
        on_click=lambda value: value + 1
    )
    return algo1_dropdown, algo2_dropdown, array_dropdown, n_input, start_btn


@app.cell
def _(
    Quicksort,
    QuicksortRandom,
    algo1_dropdown,
    algo2_dropdown,
    array_dropdown,
    mergeSort,
    mo,
    n_input,
    np,
    plt,
    start_btn,
    time,
):
    # Defining Bubble and Insertion sorts for the race
    def bubble_sort(arr):
        a = arr.copy()  # Operate on a copy to prevent in-place sorting from skewing the next 99 runs
        n = len(a)
        for i in range(n):
            for j in range(0, n-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a

    def insertion_sort(arr):
        a = arr.copy()
        for i in range(1, len(a)):
            key = a[i]
            j = i-1
            while j >= 0 and key < a[j]:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = key
        return a

    algo_mapping = {
        "Merge Sort": mergeSort,
        "Quick Sort": Quicksort,
        "Quick Sort (Random Pivot)": QuicksortRandom,
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort
    }

    # Structuring the UI Layout
    controls = mo.vstack([
        mo.md("### 🏎️ Configure Sorting Race"),
        mo.hstack([n_input, array_dropdown]),
        mo.hstack([algo1_dropdown, algo2_dropdown]),
        start_btn
    ])

    dashboard_layout = controls

    # Logic execution
    if start_btn.value > 0:
        N = n_input.value

        # Array creation
        if array_dropdown.value == "Sorted":
            base_arr = list(range(N))
        elif array_dropdown.value == "Reversed":
            base_arr = list(range(N, 0, -1))
        else:
            base_arr = np.random.randint(0, 10000, N).tolist()

        func1 = algo_mapping[algo1_dropdown.value]
        func2 = algo_mapping[algo2_dropdown.value]

        times1 = []
        times2 = []

        # Running the Race (100 times)
        for _ in range(100):
            # Competitor 1
            t_0 = time.time()
            func1(base_arr)
            times1.append(time.time() - t_0)

            # Competitor 2
            t_1 = time.time()
            func2(base_arr)
            times2.append(time.time() - t_1)

        avg_time1 = np.mean(times1)
        avg_time2 = np.mean(times2)

        winner_name = algo1_dropdown.value if avg_time1 < avg_time2 else algo2_dropdown.value

        # Plotting the Race Profile
        fig_race, ax_race = plt.subplots(figsize=(10, 4))
        ax_race.plot(
            times1, label=f"{algo1_dropdown.value} (Avg: {avg_time1:.6f}s)", alpha=0.8, color="purple")
        ax_race.plot(
            times2, label=f"{algo2_dropdown.value} (Avg: {avg_time2:.6f}s)", alpha=0.8, color="orange")
        ax_race.set_title(
            f"Sorting Race: {algo1_dropdown.value} vs {algo2_dropdown.value} (N={N}, {array_dropdown.value})")
        ax_race.set_xlabel("Run Iteration")
        ax_race.set_ylabel("Execution Time (seconds)")
        ax_race.legend()
        ax_race.grid(True, linestyle="--", alpha=0.5)

        # Combine everything
        dashboard_layout = mo.vstack([
            controls,
            mo.md(f"### 🏆 The winner is: **{winner_name}**!"),
            fig_race
        ])

    output_dashboard = mo.vstack([
        mo.show_code(),
        dashboard_layout
    ])
    output_dashboard
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------------
    """)
    return


if __name__ == "__main__":
    app.run()
