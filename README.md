

# Delhi Metro Map

This repository contains a Python implementation of a Delhi Metro Map system. The implementation includes various functionalities such as adding and removing vertices (stations) and edges (connections), displaying the metro map, finding the shortest path using Dijkstra's algorithm, calculating the shortest distance and minimum time between two stations, and identifying interchanges in the path.

## Features

- **Add and Remove Stations and Connections**: Dynamically add or remove stations and connections in the metro map.
- **Display Metro Map**: Visual representation of the entire metro map with stations and connections.
- **Shortest Path Calculation**: Compute the shortest distance between two stations using Dijkstra's algorithm.
- **Minimum Time Calculation**: Compute the minimum travel time between two stations considering fixed and variable time components.
- **Interchange Identification**: Identify and display interchanges in the path between two stations.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone [https://github.com/yourusername/DelhiMetroMap.git](https://github.com/devansh-kumar-24/Metro-Maps-
    cd DelhiMetroMap
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Run the main script:
    ```sh
    python metro_map.py
    ```

## Usage

Upon running the script, you will be presented with a menu-driven interface to interact with the Delhi Metro Map system.

### Menu Options

1. **Display Metro Map**: Displays the entire metro map with stations and connections.
2. **Display All Stations**: Lists all the stations in the metro map.
3. **Shortest Distance**: Prompts for source and destination stations and calculates the shortest distance path.
4. **Minimum Time**: Prompts for source and destination stations and calculates the minimum travel time path.
5. **Exit**: Exit the application.

### Example

```sh
Menu:
1. Display Metro Map
2. Display All Stations
3. Shortest Distance
4. Minimum Time
5. Exit
Enter your choice: 1

# Output: Displays the metro map

Enter your choice: 3
Enter source station: Noida Sector 62~B
Enter destination station: Rajiv Chowk~BY

# Output: Shortest Distance Path: Noida Sector 62~B -> Botanical Garden~B -> Yamuna Bank~B -> Rajiv Chowk~BY
```

## Implementation Details

### Graph and Vertex Classes

- **Graph Class**: Manages the entire metro map, including adding/removing stations and connections, and computing paths.
- **Vertex Class**: Represents each station and its connections to neighboring stations.

### Algorithms

- **Dijkstra's Algorithm**: Used for computing the shortest path between two stations.
- **Depth-First Search (DFS)**: Used for calculating minimum distance and minimum time paths.

### Methods

- **add_vertex(name)**: Adds a new station to the metro map.
- **remove_vertex(name)**: Removes a station from the metro map.
- **add_edge(v1, v2, value)**: Adds a connection between two stations with a specified distance.
- **remove_edge(v1, v2)**: Removes a connection between two stations.
- **display_map()**: Displays the entire metro map.
- **display_stations()**: Lists all stations in the metro map.
- **has_path(v1, v2)**: Checks if there is a path between two stations.
- **dijkstra(src, des, is_time)**: Computes the shortest path using Dijkstra's algorithm.
- **get_min_distance(src, des)**: Computes the minimum distance path between two stations.
- **get_min_time(src, des)**: Computes the minimum time path between two stations.
- **get_interchanges(path)**: Identifies interchanges in the path.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

