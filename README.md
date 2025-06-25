# ✈️ Smart Travel Planner with Constraints

A graph-based route planning system that simulates multi-city travel across flight networks using Dijkstra’s algorithm, BFS, and scheduling logic. It finds the cheapest, fastest, or fewest-stop routes between cities while respecting real-world constraints like layovers and valid flight times.

---

## 🚀 Features

- ✨ **Optimal Route Calculation**
  - Uses **Dijkstra’s algorithm** to find the cheapest or fastest path
  - Uses **BFS** to compute routes with the fewest stops (hops)

- 🧠 **Constraint Handling**
  - Minimum layover: 60 minutes
  - Non-overlapping flight schedules
  - Valid departure–arrival time windows

- 📊 **User-Friendly Input**
  - CSV-based flight database
  - CLI-based route querying

- 🔧 **Modular Codebase**
  - Separated logic for graph building, route planning, and constraint checks

---

## ⚙️ How to Run

```bash
# Clone the repository
git clone https://github.com/ajay-techspace/smart_travel_planner_with_constraints.git

# Navigate to the project folder
cd smart_travel_planner_with_constraints/src

# Run the planner
python main.py

## License

This project is licensed under the [MIT License](./LICENSE).

