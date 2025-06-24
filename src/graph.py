# src/graph.py
import heapq
from collections import defaultdict, deque
from datetime import datetime, timedelta

class Flight:
    def __init__(self, src, dst, dep_time, arr_time, cost):
        self.src = src
        self.dst = dst
        self.dep_time = datetime.strptime(dep_time, "%H:%M")
        self.arr_time = datetime.strptime(arr_time, "%H:%M")
        self.cost = cost
        self.duration = (self.arr_time - self.dep_time).seconds // 60

    def __str__(self):
        return f"{self.src} -> {self.dst} | {self.dep_time.strftime('%H:%M')} - {self.arr_time.strftime('%H:%M')} | ₹{self.cost}"

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_flight(self, flight):
        self.adj[flight.src].append(flight)

    def dijkstra(self, source, dest, minimize='cost'):
        pq = [(0, source, [], datetime.min)]
        visited = set()

        while pq:
            cost_or_time, node, path, last_arrival = heapq.heappop(pq)
            if (node, last_arrival) in visited:
                continue
            visited.add((node, last_arrival))

            if node == dest:
                return path, cost_or_time

            for flight in self.adj[node]:
                if last_arrival != datetime.min:
                    layover = (flight.dep_time - last_arrival).seconds // 60
                    if layover < 60 or flight.dep_time < last_arrival:
                        continue

                if minimize == 'cost':
                    next_metric = cost_or_time + flight.cost
                else:
                    next_metric = cost_or_time + flight.duration

                heapq.heappush(pq, (next_metric, flight.dst, path + [flight], flight.arr_time))

        return None, float('inf')

    def bfs_min_stops(self, source, dest):
        queue = deque([(source, [], datetime.min)])
        visited = set()

        while queue:
            node, path, last_arrival = queue.popleft()
            if node == dest:
                return path, len(path)

            for flight in self.adj[node]:
                if last_arrival != datetime.min:
                    layover = (flight.dep_time - last_arrival).seconds // 60
                    if layover < 60 or flight.dep_time < last_arrival:
                        continue
                if (flight.dst, flight.arr_time) not in visited:
                    visited.add((flight.dst, flight.arr_time))
                    queue.append((flight.dst, path + [flight], flight.arr_time))

        return None, float('inf')
