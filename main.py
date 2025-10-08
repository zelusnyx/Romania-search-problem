"""
Romania Map Search Algorithms - Main Script
"""

import argparse
import sys
from typing import Optional

from romania_data import ROMANIA_GRAPH, SLD_TO_BUCHAREST, TEST_PAIRS
from experiments import run_experiments, print_detailed_results, analyze_performance
from visualization import plot_nodes_expanded, plot_comparison_metrics, create_summary_plot


def main():
    parser = argparse.ArgumentParser(description='Romania Map Search Algorithms')
    parser.add_argument('--start', type=str, default='Arad', help='Starting city')
    parser.add_argument('--goal', type=str, default='Bucharest', help='Goal city')
    parser.add_argument('--experiments', action='store_true', help='Run full experiments')
    parser.add_argument('--visualize', action='store_true', help='Create visualizations')
    parser.add_argument('--save-plots', type=str, default=None, help='Directory to save plots')
    
    args = parser.parse_args()
    
    if args.start not in ROMANIA_GRAPH or args.goal not in ROMANIA_GRAPH:
        print(f"Error: City not found. Available: {list(ROMANIA_GRAPH.keys())}")
        sys.exit(1)
    
    print_detailed_results(args.start, args.goal)
    
    if args.visualize:
        save_dir = args.save_plots
        if save_dir:
            import os
            os.makedirs(save_dir, exist_ok=True)
            nodes_plot_path = f"{save_dir}/nodes_expanded_{args.start}_to_{args.goal}.png"
            comparison_plot_path = f"{save_dir}/comparison_{args.start}_to_{args.goal}.png"
        else:
            nodes_plot_path = None
            comparison_plot_path = None
        
        plot_nodes_expanded(args.start, args.goal, nodes_plot_path)
        plot_comparison_metrics(args.start, args.goal, comparison_plot_path)
    
    if args.experiments:
        df = run_experiments()
        print(df)
        analyze_performance(df)
        
        if args.visualize:
            summary_plot_path = f"{args.save_plots}/summary_comparison.png" if args.save_plots else None
            create_summary_plot(df, summary_plot_path)


if __name__ == "__main__":
    main()
