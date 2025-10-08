# Romania Map Search Algorithms

Implementation and comparison of four AI search algorithms: BFS, DFS, GBFS, and A*.

## Quick Start

```bash
pip install -r requirements.txt
python main.py --start Arad --goal Bucharest
```

## Usage

```bash
# Basic search
python main.py --start Arad --goal Bucharest

# Run all experiments
python main.py --experiments

# Create visualizations
python main.py --visualize

# Save plots
python main.py --experiments --visualize --save-plots ./plots
```

## Files

- `main.py` - Main script
- `search_algorithms.py` - BFS, DFS, GBFS, A* implementations
- `experiments.py` - Experiment runner and analysis
- `visualization.py` - Plotting functions
- `romania_data.py` - Map data and heuristics
- `search_utilities.py` - Data structures and helpers

## Algorithms

- **BFS**: FIFO queue, complete, optimal for unweighted graphs
- **DFS**: LIFO stack, complete, not optimal
- **GBFS**: Priority queue by h(n), complete with admissible heuristic
- **A***: Priority queue by f(n)=g(n)+h(n), complete and optimal

## Dependencies

- pandas >= 1.3.0
- matplotlib >= 3.5.0
- numpy >= 1.21.0
