# ✈️ Smart Travel Planner with Constraints

[🔗 View on GitHub](https://github.com/ajay-techspace/smart_travel_planner_with_constraints.git)

A graph-based route planning system that simulates multi-city travel across flight networks using **Dijkstra's algorithm**, **BFS**, and scheduling logic. It finds the **cheapest**, **fastest**, or **fewest-stop** routes between cities while respecting real-world constraints like layovers and time windows.

---

## 📌 Features

- 🧠 **Dijkstra’s Algorithm**: Finds optimal paths by cost or time
- 🔄 **BFS**: Computes routes with the fewest hops (flights)
- ⏱ **Constraint Handling**:
  - Minimum layover of 60 minutes
  - Non-overlapping flight schedules
  - Valid arrival-departure time logic
- 📊 **CSV-Based Input** for easy editing or testing

---

## 📂 Folder Structure

smart-travel-planner/
├── src/
│ ├── graph.py # Graph structure, Dijkstra, BFS
│ ├── planner.py # Flight loader, constraint handling
│ └── main.py # CLI interface for user input
├── data/
│ └── flights.csv # Sample flight dataset
├── README.md # Project overview
└── requirements.txt # Dependencies



## 🛠 How To Run

1. Clone the repo or download the folder  
2. Ensure Python 3.6+ is installed  
3. From the project root, run:

```bash
git clone https://github.com/ajay-techspace/smart_travel_planner_with_constraints.git
cd src
python main.py

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, or share with attribution.
