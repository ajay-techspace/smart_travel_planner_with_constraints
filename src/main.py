# src/main.py
from planner import load_flights, display_path

def main():
    g = load_flights('../data/flights.csv')

    print("Welcome to Smart Travel Planner")
    source = input("Enter source city: ").strip().title()
    dest = input("Enter destination city: ").strip().title()

    print("Choose optimization criterion:")
    print("1. Cheapest")
    print("2. Fastest")
    print("3. Fewest stops")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == '1':
        path, metric = g.dijkstra(source, dest, minimize='cost')
        print(f"\nCheapest Path (Cost = ₹{metric}):")
        display_path(path)
    elif choice == '2':
        path, metric = g.dijkstra(source, dest, minimize='time')
        print(f"\nFastest Path (Duration = {metric} mins):")
        display_path(path)
    elif choice == '3':
        path, stops = g.bfs_min_stops(source, dest)
        print(f"\nPath with Fewest Stops ({stops} stops):")
        display_path(path)
    else:
        print("Invalid choice. Exiting.")

if __name__ == '__main__':
    main()
