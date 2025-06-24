# src/planner.py
from graph import Graph, Flight
import csv

def load_flights(filepath):
    g = Graph()
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            flight = Flight(row['src'], row['dst'], row['dep_time'], row['arr_time'], int(row['cost']))
            g.add_flight(flight)
    return g

def display_path(path):
    if not path:
        print("No valid path found.")
        return
    for f in path:
        print(f)
