"""Experiments and Analysis Module"""

import pandas as pd
from typing import Dict, List, Tuple, Any

from romania_data import ROMANIA_GRAPH, SLD_TO_BUCHAREST, TEST_PAIRS
from search_algorithms import bfs, dfs, gbfs, astar


def run_all_algorithms(start: str, goal: str) -> Dict[str, Dict[str, Any]]:
    results = {}
    results['BFS'] = bfs(ROMANIA_GRAPH, start, goal)
    results['DFS'] = dfs(ROMANIA_GRAPH, start, goal)
    results['GBFS'] = gbfs(ROMANIA_GRAPH, start, goal, lambda city: SLD_TO_BUCHAREST[city])
    results['A*'] = astar(ROMANIA_GRAPH, start, goal, lambda city: SLD_TO_BUCHAREST[city])
    return results


def run_experiments() -> pd.DataFrame:
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_columns', None)
    
    rows = []
    for start, goal in TEST_PAIRS:
        results = run_all_algorithms(start, goal)
        for algo_name, result in results.items():
            rows.append([
                start, goal, algo_name, result["path_cost"], result["solution_depth"],
                result["nodes_expanded"], result["max_frontier"], result["runtime_sec"],
                " -> ".join(result["path"])
            ])
    
    return pd.DataFrame(rows, columns=[
        "Start", "Goal", "Algo", "Path Cost", "Depth",
        "Nodes Expanded", "Max Frontier", "Time (s)", "Path"
    ])


def print_detailed_results(start: str, goal: str) -> None:
    results = run_all_algorithms(start, goal)
    for algo, result in results.items():
        print(f"{algo}: Cost={result['path_cost']}, Depth={result['solution_depth']}, "
              f"Nodes={result['nodes_expanded']}, Time={result['runtime_sec']:.3f}s")
        print(f"Path: {' -> '.join(result['path'])}")
        print()


def analyze_performance(df: pd.DataFrame) -> None:
    algo_stats = df.groupby('Algo').agg({
        'Path Cost': 'mean', 'Nodes Expanded': 'mean', 
        'Max Frontier': 'mean', 'Time (s)': 'mean'
    }).round(3)
    
    print("Average Performance:")
    print(algo_stats)
    print()
    
    for metric in ['Path Cost', 'Nodes Expanded', 'Max Frontier', 'Time (s)']:
        best_algo = algo_stats[metric].idxmin()
        best_value = algo_stats.loc[best_algo, metric]
        print(f"{metric}: {best_algo} ({best_value})")
