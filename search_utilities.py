"""Search Utilities for AI Search Algorithms"""

from collections import deque
import heapq
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple, Optional


@dataclass
class Node:
    state: Any
    parent: Optional["Node"] = None
    action: Optional[Any] = None
    path_cost: float = 0.0
    depth: int = 0


def reconstruct_path(node: Optional[Node]) -> List[Any]:
    if node is None:
        return []
    path = []
    current = node
    while current is not None:
        path.append(current.state)
        current = current.parent
    return path[::-1]


class FIFOQueue:
    def __init__(self):
        self.queue = deque()
    
    def put(self, item):
        self.queue.append(item)
    
    def get(self):
        return self.queue.popleft()
    
    def empty(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)


class LIFOStack:
    def __init__(self):
        self.stack = []
    
    def put(self, item):
        self.stack.append(item)
    
    def get(self):
        return self.stack.pop()
    
    def empty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)


class MinPQ:
    def __init__(self):
        self.heap = []
        self.counter = 0
    
    def put(self, item, priority):
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1
    
    def get(self):
        _, _, item = heapq.heappop(self.heap)
        return item
    
    def empty(self):
        return len(self.heap) == 0
    
    def __len__(self):
        return len(self.heap)


def run_metrics(start_time: float, nodes_expanded: int, max_frontier: int, 
                solution_node: Optional[Node]) -> Dict[str, Any]:
    end_time = time.perf_counter()
    runtime = end_time - start_time
    
    return {
        "path": reconstruct_path(solution_node),
        "path_cost": solution_node.path_cost if solution_node else float("inf"),
        "nodes_expanded": nodes_expanded,
        "max_frontier": max_frontier,
        "solution_depth": solution_node.depth if solution_node else None,
        "runtime_sec": runtime,
    }
