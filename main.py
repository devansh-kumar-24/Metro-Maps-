import heapq
import math

class Graph:
    class Vertex:
        def __init__(self):
            self.neighbors = {}

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = self.Vertex()

    def remove_vertex(self, name):
        if name in self.vertices:
            for neighbor in list(self.vertices[name].neighbors):
                self.vertices[neighbor].neighbors.pop(name)
            self.vertices.pop(name)

    def add_edge(self, v1, v2, value):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].neighbors[v2] = value
            self.vertices[v2].neighbors[v1] = value

    def remove_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].neighbors.pop(v2, None)
            self.vertices[v2].neighbors.pop(v1, None)

    def contains_vertex(self, name):
        return name in self.vertices

    def contains_edge(self, v1, v2):
        return v1 in self.vertices and v2 in self.vertices and v2 in self.vertices[v1].neighbors

    def num_vertices(self):
        return len(self.vertices)

    def num_edges(self):
        count = 0
        for vertex in self.vertices.values():
            count += len(vertex.neighbors)
        return count // 2

    def display_map(self):
        print("\t Delhi Metro Map")
        print("\t------------------")
        print("----------------------------------------------------\n")
        for key, vertex in self.vertices.items():
            print(f"{key} =>")
            for neighbor, value in vertex.neighbors.items():
                print(f"\t{neighbor}\t{value}")
        print("\t------------------")
        print("---------------------------------------------------\n")

    def display_stations(self):
        print("\n***********************************************************************\n")
        for i, key in enumerate(self.vertices.keys(), 1):
            print(f"{i}. {key}")
        print("\n***********************************************************************\n")

    def has_path(self, v1, v2, processed=None):
        if processed is None:
            processed = {}
        if self.contains_edge(v1, v2):
            return True
        processed[v1] = True
        for neighbor in self.vertices[v1].neighbors:
            if neighbor not in processed:
                if self.has_path(neighbor, v2, processed):
                    return True
        return False

    def dijkstra(self, src, des, is_time):
        class DijkstraPair:
            def __init__(self, name, path, cost):
                self.name = name
                self.path = path
                self.cost = cost
            def __lt__(self, other):
                return self.cost < other.cost

        map_ = {}
        heap = []
        for key in self.vertices:
            if key == src:
                dp = DijkstraPair(key, key, 0)
            else:
                dp = DijkstraPair(key, "", float('inf'))
            heapq.heappush(heap, dp)
            map_[key] = dp

        while heap:
            rp = heapq.heappop(heap)
            if rp.name == des:
                return rp.cost
            for neighbor, value in self.vertices[rp.name].neighbors.items():
                if neighbor in map_:
                    new_cost = rp.cost + (120 + 40 * value if is_time else value)
                    if new_cost < map_[neighbor].cost:
                        map_[neighbor].cost = new_cost
                        map_[neighbor].path = rp.path + neighbor
                        heapq.heappush(heap, map_[neighbor])
        return float('inf')

    def get_min_distance(self, src, des):
        class Pair:
            def __init__(self, name, path, min_dis, min_time):
                self.name = name
                self.path = path
                self.min_dis = min_dis
                self.min_time = min_time

        min_distance = float('inf')
        ans = ""
        processed = set()
        stack = [Pair(src, src + "  ", 0, 0)]
        while stack:
            rp = stack.pop(0)
            if rp.name in processed:
                continue
            processed.add(rp.name)
            if rp.name == des:
                if rp.min_dis < min_distance:
                    ans = rp.path
                    min_distance = rp.min_dis
                continue
            for neighbor, value in self.vertices[rp.name].neighbors.items():
                if neighbor not in processed:
                    stack.append(Pair(neighbor, rp.path + neighbor + "  ", rp.min_dis + value, 0))
        return ans + str(min_distance)

    def get_min_time(self, src, des):
        class Pair:
            def __init__(self, name, path, min_dis, min_time):
                self.name = name
                self.path = path
                self.min_dis = min_dis
                self.min_time = min_time

        min_time = float('inf')
        ans = ""
        processed = set()
        stack = [Pair(src, src + "  ", 0, 0)]
        while stack:
            rp = stack.pop(0)
            if rp.name in processed:
                continue
            processed.add(rp.name)
            if rp.name == des:
                if rp.min_time < min_time:
                    ans = rp.path
                    min_time = rp.min_time
                continue
            for neighbor, value in self.vertices[rp.name].neighbors.items():
                if neighbor not in processed:
                    stack.append(Pair(neighbor, rp.path + neighbor + "  ", 0, rp.min_time + 120 + 40 * value))
        minutes = math.ceil(min_time / 60)
        return ans + str(minutes)

    def get_interchanges(self, path):
        parts = path.split("  ")
        interchanges = [parts[0]]
        count = 0
        for i in range(1, len(parts) - 1):
            if '~' in parts[i]:
                prev = parts[i - 1].split('~')[-1]
                next_ = parts[i + 1].split('~')[-1]
                if prev == next_:
                    interchanges.append(parts[i])
                else:
                    interchanges.append(parts[i] + " ==> " + parts[i + 1])
                    count += 1
                    i += 1
            else:
                interchanges.append(parts[i])
        interchanges.append(str(count))
        interchanges.append(parts[-1])
        return interchanges

    def create_metro_map(self):
        self.add_vertex("Noida Sector 62~B")
        self.add_vertex("Botanical Garden~B")
        self.add_vertex("Yamuna Bank~B")
        self.add_vertex("Rajiv Chowk~BY")
        self.add_vertex("Vaishali~B")
        self.add_vertex("Moti Nagar~B")
        self.add_vertex("Janak Puri West~BO")
        self.add_vertex("Dwarka Sector 21~B")
        self.add_vertex("Huda City Center~Y")
        self.add_vertex("Saket~Y")
        self.add_vertex("Vishwavidyalaya~Y")
        self.add_vertex("Chandni Chowk~Y")
        self.add_vertex("New Delhi~YO")
        self.add_vertex("AIIMS~Y")
        self.add_vertex("Shivaji Stadium~O")
        self.add_vertex("DDS Campus~O")
        self.add_vertex("IGI Airport~O")
        self.add_vertex("Rajouri Garden~BP")
        self.add_vertex("Netaji Subhash Place~PR")
        self.add_vertex("Punjabi Bagh West~P")

        self.add_edge("Noida Sector 62~B", "Botanical Garden~B", 8)
        self.add_edge("Botanical Garden~B", "Yamuna Bank~B", 10)
        self.add_edge("Yamuna Bank~B", "Vaishali~B", 8)
        self.add_edge("Yamuna Bank~B", "Rajiv Chowk~BY", 6)
        self.add_edge("Rajiv Chowk~BY", "Moti Nagar~B", 9)
        self.add_edge("Moti Nagar~B", "Janak Puri West~BO", 7)
        self.add_edge("Janak Puri West~BO", "Dwarka Sector 21~B", 6)
        self.add_edge("Huda City Center~Y", "Saket~Y", 15)
        self.add_edge("Saket~Y", "AIIMS~Y", 6)
        self.add_edge("AIIMS~Y", "Rajiv Chowk~BY", 7)
        self.add_edge("Rajiv Chowk~BY", "New Delhi~YO", 1)
        self.add_edge("New Delhi~YO", "Chandni Chowk~Y", 2)
        self.add_edge("Chandni Chowk~Y", "Vishwavidyalaya~Y", 5)
        self.add_edge("New Delhi~YO", "Shivaji Stadium~O", 2)
        self.add_edge("Shivaji Stadium~O", "DDS Campus~O", 4)
        self.add_edge("DDS Campus~O", "IGI Airport~O", 8)
        self.add_edge("Janak Puri West~BO", "Rajouri Garden~BP", 2)
        self.add_edge("Rajouri Garden~BP", "Netaji Subhash Place~PR", 6)
        self.add_edge("Netaji Subhash Place~PR", "Punjabi Bagh West~P", 3)

# Main method to handle user interaction
def main():
    g = Graph()
    g.create_metro_map()

    while True:
        print("\nMenu:")
        print("1. Display Metro Map")
        print("2. Display All Stations")
        print("3. Shortest Distance")
        print("4. Minimum Time")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            g.display_map()
        elif choice == '2':
            g.display_stations()
        elif choice == '3':
            src = input("Enter source station: ")
            des = input("Enter destination station: ")
            if g.contains_vertex(src) and g.contains_vertex(des):
                print("Shortest Distance Path:", g.get_min_distance(src, des))
            else:
                print("Invalid stations!")
        elif choice == '4':
            src = input("Enter source station: ")
            des = input("Enter destination station: ")
            if g.contains_vertex(src) and g.contains_vertex(des):
                print("Minimum Time Path:", g.get_min_time(src, des))
            else:
                print("Invalid stations!")
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
