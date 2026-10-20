# 🎓 Advanced Algorithms and Complexity Showcase

**Developer:** Ahmed AlHennawi  
**Program:** MSc Computer Science @ University of the Arts London (UAL)  
**Live Portfolio:** https://github.com/Ahmed-Al-Hennawi/AP_portfolio_submission-UAL

## 📝 Overview
This repository contains a 6-week portfolio of interactive Python applications developed for the **Advanced Algorithms and Complexity** module. The goal of this portfolio is to move beyond static code execution by bringing algorithms to life through interactive visualisations, mathematical plotting, and dynamic data structures.

All projects are built using **[Marimo](https://marimo.io/)**, a reactive Python notebook framework. Using WebAssembly (Pyodide), the Python code is compiled directly into the browser, allowing users to interact with complex algorithms via a custom-designed HTML/CSS/JS landing page without needing a backend server.

---

## 🚀 Weekly Projects Breakdown

### 🎯 Week 1: My Interactive CV
A creative, data-driven resume built natively in Python.

**Key Features:**
- Interactive dropdowns
- Dynamic CSS animations injected via Python
- Plotly-powered Radar Chart visualising technical skill progression over the years

### 🎯 Week 2: Basic Algorithms
Establishing the foundational logic required for advanced algorithmic analysis.

**Key Features:**
- Exploration of basic algorithmic structures
- Loops and conditional logic
- Standard computational problem solving

### 🎯 Week 3: Sorting Visualiser
A deep dive into sorting algorithms and time complexity.

**Key Features:**
- Implemented **Bubble Sort**, **Insertion Sort**, and **Selection Sort**
- Interactive UI for stepping through the sorting process frame-by-frame
- Dynamic Plotly bar charts visualising array transformations

### 🎯 Week 4: Binary Search Visualisation
Comparing linear and logarithmic time complexities (*O(n)* vs *O(log n)*).

**Key Features:**
- Linear Search
- Binary Search
- Recursive Binary Search
- Execution time histograms
- Interactive Binary Search Tree visualisation using **NetworkX**

### 🎯 Week 5: Sorting Race
A comparative performance analysis of algorithms under stress.

**Key Features:**
- Performance comparison of sorting algorithms
- Large randomised datasets
- Partially sorted datasets
- Interactive speed and efficiency visualisations

### 🎯 Week 6: Genetic Algorithms
Exploring evolutionary computing and heuristic search methods.

**Key Features:**
1. Solved the Maxone problem using initialization, fitness evaluation, crossover, and mutation.
2. Maximised the real-valued function *f(x,y)=-(x+y)^2*.
3. Interactive 3D Plotly surface visualisation.
4. Generation slider allowing users to step through 100 generations and observe population evolution toward the optimal solution.

---

## 🛠️ Technologies Used

### Languages
- Python
- HTML5
- CSS3
- JavaScript

### Framework
- Marimo (v0.16.5)

### Libraries
- NumPy (Data manipulation)
- Plotly (Interactive 2D & 3D charting)
- NetworkX (Graph and Tree visualizations)
- Matplotlib (Static plotting and histograms)

### Deployment
- GitHub Pages
- Pyodide (WebAssembly)

---

## 💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://git.arts.ac.uk/a-alhennawi0520251/AP_portfolio_Resubmission.git
cd AP_portfolio_Resubmission
```

### 2. Install Dependencies

```bash
pip install marimo numpy matplotlib plotly networkx
```

### 3. Run a Specific Week

```bash
marimo edit weekX.py
```

Replace `X` with the week number you want to view (for example, `week6.py`).

---

## 🌐 WebAssembly Architecture Note

The front-end web portal (`index.html`) connects to standalone web applications inside the `docs/` folders. These were generated using Marimo's WASM exporter:

```bash
python -m marimo export html-wasm weekX.py -o docs
```

Because the Python environment runs entirely client-side, dynamic dependency fetching (`micropip`) is utilized within the notebooks to ensure heavy libraries like Plotly and NetworkX load smoothly in the browser.
