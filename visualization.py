"""Visualization Module for Search Algorithm Results"""

import matplotlib.pyplot as plt
from typing import Dict, Any, List

from experiments import run_all_algorithms


def plot_nodes_expanded(start: str, goal: str, save_path: str = None) -> None:
    results = run_all_algorithms(start, goal)
    algorithms = list(results.keys())
    nodes_expanded = [results[algo]["nodes_expanded"] for algo in algorithms]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, nodes_expanded, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.title(f'Nodes Expanded by Algorithm for {start} -> {goal}', fontsize=14, fontweight='bold')
    plt.xlabel('Search Algorithm', fontsize=12)
    plt.ylabel('Number of Nodes Expanded', fontsize=12)
    
    for bar, value in zip(bars, nodes_expanded):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                 str(value), ha='center', va='bottom', fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()


def plot_comparison_metrics(start: str, goal: str, save_path: str = None) -> None:
    results = run_all_algorithms(start, goal)
    algorithms = list(results.keys())
    
    path_costs = [results[algo]["path_cost"] for algo in algorithms]
    nodes_expanded = [results[algo]["nodes_expanded"] for algo in algorithms]
    max_frontiers = [results[algo]["max_frontier"] for algo in algorithms]
    runtimes = [results[algo]["runtime_sec"] * 1000 for algo in algorithms]
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'Algorithm Comparison for {start} -> {goal}', fontsize=16, fontweight='bold')
    
    bars1 = ax1.bar(algorithms, path_costs, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax1.set_title('Path Cost', fontweight='bold')
    ax1.set_ylabel('Cost')
    for bar, value in zip(bars1, path_costs):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                 str(value), ha='center', va='bottom', fontweight='bold')
    
    bars2 = ax2.bar(algorithms, nodes_expanded, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax2.set_title('Nodes Expanded', fontweight='bold')
    ax2.set_ylabel('Count')
    for bar, value in zip(bars2, nodes_expanded):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                 str(value), ha='center', va='bottom', fontweight='bold')
    
    bars3 = ax3.bar(algorithms, max_frontiers, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax3.set_title('Max Frontier Size', fontweight='bold')
    ax3.set_ylabel('Size')
    for bar, value in zip(bars3, max_frontiers):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                 str(value), ha='center', va='bottom', fontweight='bold')
    
    bars4 = ax4.bar(algorithms, runtimes, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax4.set_title('Runtime', fontweight='bold')
    ax4.set_ylabel('Time (ms)')
    for bar, value in zip(bars4, runtimes):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                 f'{value:.3f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()


def create_summary_plot(df, save_path: str = None) -> None:
    algo_stats = df.groupby('Algo').agg({
        'Path Cost': 'mean', 'Nodes Expanded': 'mean', 
        'Max Frontier': 'mean', 'Time (s)': 'mean'
    })
    
    algorithms = algo_stats.index.tolist()
    
    normalized_stats = algo_stats.copy()
    for col in normalized_stats.columns:
        min_val = normalized_stats[col].min()
        max_val = normalized_stats[col].max()
        if max_val > min_val:
            normalized_stats[col] = (normalized_stats[col] - min_val) / (max_val - min_val)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    x = range(len(algorithms))
    width = 0.2
    
    metrics = ['Path Cost', 'Nodes Expanded', 'Max Frontier', 'Time (s)']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    for i, (metric, color) in enumerate(zip(metrics, colors)):
        ax.bar([pos + width * i for pos in x], normalized_stats[metric], 
               width, label=metric, color=color, alpha=0.8)
    
    ax.set_xlabel('Algorithm')
    ax.set_ylabel('Normalized Performance (0-1 scale)')
    ax.set_title('Average Algorithm Performance Comparison (Normalized)', fontweight='bold')
    ax.set_xticks([pos + width * 1.5 for pos in x])
    ax.set_xticklabels(algorithms)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
