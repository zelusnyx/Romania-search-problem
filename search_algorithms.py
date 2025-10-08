"""Search Algorithms Implementation"""

import time
from typing import Dict, Any, Callable, List, Tuple

from search_utilities import Node, FIFOQueue, LIFOStack, MinPQ, run_metrics


def bfs(graph: Dict[str, List[Tuple[str, float]]], start: str, goal: str) -> Dict[str, Any]:
    start_time = time.perf_counter()
    
    node = Node(state=start, path_cost=0, depth=0)
    frontier = FIFOQueue()
    frontier.put(node)
    reached = {start: node}
    
    nodes_expanded = 0
    max_frontier = 1
    
    while not frontier.empty():
        max_frontier = max(max_frontier, len(frontier))
        node = frontier.get()
        nodes_expanded += 1
        
        if node.state == goal:
            return run_metrics(start_time, nodes_expanded, max_frontier, node)
        
        for neighbor, cost in graph[node.state]:
            child_path_cost = node.path_cost + cost
            child_node = Node(
                state=neighbor,
                parent=node,
                action=neighbor,
                path_cost=child_path_cost,
                depth=node.depth + 1
            )
            
            if neighbor not in reached or child_path_cost < reached[neighbor].path_cost:
                reached[neighbor] = child_node
                frontier.put(child_node)
    
    return run_metrics(start_time, nodes_expanded, max_frontier, None)


def dfs(graph: Dict[str, List[Tuple[str, float]]], start: str, goal: str) -> Dict[str, Any]:
    start_time = time.perf_counter()
    
    node = Node(state=start, path_cost=0, depth=0)
    frontier = LIFOStack()
    frontier.put(node)
    reached = {start: node}
    
    nodes_expanded = 0
    max_frontier = 1
    
    while not frontier.empty():
        max_frontier = max(max_frontier, len(frontier))
        node = frontier.get()
        nodes_expanded += 1
        
        if node.state == goal:
            return run_metrics(start_time, nodes_expanded, max_frontier, node)
        
        for neighbor, cost in graph[node.state]:
            child_path_cost = node.path_cost + cost
            child_node = Node(
                state=neighbor,
                parent=node,
                action=neighbor,
                path_cost=child_path_cost,
                depth=node.depth + 1
            )
            
            if neighbor not in reached or child_path_cost < reached[neighbor].path_cost:
                reached[neighbor] = child_node
                frontier.put(child_node)
    
    return run_metrics(start_time, nodes_expanded, max_frontier, None)


def gbfs(graph: Dict[str, List[Tuple[str, float]]], start: str, goal: str, 
         heuristic: Callable[[str], float]) -> Dict[str, Any]:
    start_time = time.perf_counter()
    
    node = Node(state=start, path_cost=0, depth=0)
    frontier = MinPQ()
    frontier.put(node, heuristic(start))
    reached = {start: node}
    
    nodes_expanded = 0
    max_frontier = 1
    
    while not frontier.empty():
        max_frontier = max(max_frontier, len(frontier))
        node = frontier.get()
        nodes_expanded += 1
        
        if node.state == goal:
            return run_metrics(start_time, nodes_expanded, max_frontier, node)
        
        for neighbor, cost in graph[node.state]:
            child_path_cost = node.path_cost + cost
            child_node = Node(
                state=neighbor,
                parent=node,
                action=neighbor,
                path_cost=child_path_cost,
                depth=node.depth + 1
            )
            
            if neighbor not in reached or child_path_cost < reached[neighbor].path_cost:
                reached[neighbor] = child_node
                frontier.put(child_node, heuristic(neighbor))
    
    return run_metrics(start_time, nodes_expanded, max_frontier, None)


def astar(graph: Dict[str, List[Tuple[str, float]]], start: str, goal: str, 
          heuristic: Callable[[str], float]) -> Dict[str, Any]:
    start_time = time.perf_counter()
    
    node = Node(state=start, path_cost=0, depth=0)
    frontier = MinPQ()
    f_value = node.path_cost + heuristic(start)
    frontier.put(node, f_value)
    reached = {start: node}
    
    nodes_expanded = 0
    max_frontier = 1
    
    while not frontier.empty():
        max_frontier = max(max_frontier, len(frontier))
        node = frontier.get()
        nodes_expanded += 1
        
        if node.state == goal:
            return run_metrics(start_time, nodes_expanded, max_frontier, node)
        
        for neighbor, cost in graph[node.state]:
            child_path_cost = node.path_cost + cost
            child_node = Node(
                state=neighbor,
                parent=node,
                action=neighbor,
                path_cost=child_path_cost,
                depth=node.depth + 1
            )
            
            if neighbor not in reached or child_path_cost < reached[neighbor].path_cost:
                reached[neighbor] = child_node
                f_value = child_path_cost + heuristic(neighbor)
                frontier.put(child_node, f_value)
    
    return run_metrics(start_time, nodes_expanded, max_frontier, None)
