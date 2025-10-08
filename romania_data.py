"""
Romania Map Data for AI Search Algorithms

This module contains the Romania map graph and straight-line distance heuristic
data used in the search algorithm implementations.
"""

# Romania map (AIMA 3e/4e style). Undirected weighted graph.
# Each entry: city -> list of (neighbor, distance)
ROMANIA_GRAPH = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Dobreta", 75)],
    "Dobreta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Dobreta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Craiova", 146), ("Sibiu", 80), ("Pitesti", 97)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    "Giurgiu": [("Bucharest", 90)],
    "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Eforie": [("Hirsova", 86)],
    "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
    "Iasi": [("Vaslui", 92), ("Neamt", 87)],
    "Neamt": [("Iasi", 87)],
}

# Straight-line distance (SLD) to Bucharest (admissible heuristic)
SLD_TO_BUCHAREST = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242, "Eforie": 161,
    "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244,
    "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193,
    "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
}

# Test start-goal pairs for experiments
TEST_PAIRS = [
    ("Arad", "Bucharest"),
    ("Lugoj", "Bucharest"),
    ("Oradea", "Bucharest"),
    ("Neamt", "Bucharest"),
    ("Fagaras", "Bucharest")
]
