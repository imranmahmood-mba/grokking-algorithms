import heapq

def dj_algorithm(start, end, graph):
    distances = {node: float('inf') for node in graph} # set the distances to 0
    distances[start] = 0
    priority_queue = [(0, start)]