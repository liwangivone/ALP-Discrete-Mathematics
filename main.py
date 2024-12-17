import networkx as nx 
import matplotlib.pyplot as plt 

class Graf:
    def __init__(self):
        # Membuat objek graf kosong
        self.G = nx.Graph()

    def add_node(self, node):
        # Menambahkan node ke dalam graf
        self.G.add_node(node)
        print(f"Node {node} berhasil ditambahkan.")

    def add_edge(self, node1, node2, weight):
        # Menambahkan edge antara dua node dengan bobot
        self.G.add_edge(node1, node2, weight=weight)
        print(f"Edge dari {node1} ke {node2} dengan bobot {weight} berhasil ditambahkan.")

    def visualize_graph(self):
        # Visualisasi graf dengan menampilkan bobot edge
        pos = nx.spring_layout(self.G)  # Layout posisi node
        labels = nx.get_edge_attributes(self.G, 'weight')  # Ambil atribut bobot
        nx.draw(self.G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.title("Visualisasi Graf")
        plt.show()

    def shortest_path(self, start, end):
        # Menentukan jalur terpendek antara dua node
        path = nx.shortest_path(self.G, source=start, target=end, weight='weight')
        print(f"Jalur terpendek dari {start} ke {end} adalah: {path}")
        return path

    def visual_shortest_path(self, start, end):
        # Visualisasi jalur terpendek
        path = self.shortest_path(start, end)
        edge_list = [(path[i], path[i+1]) for i in range(len(path)-1)]
        pos = nx.spring_layout(self.G)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw(self.G, pos, with_labels=True, node_color='lightgrey', node_size=500)
        nx.draw_networkx_edges(self.G, pos, edgelist=edge_list, edge_color='red', width=2)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.title("Visualisasi Jalur Terpendek")
        plt.show()

    # Metode tambahan
    def check_connected(self):
        # Mengecek apakah graf terhubung
        is_connected = nx.is_connected(self.G)
        print(f"Graf terhubung: {is_connected}")
        return is_connected

    def get_degree(self):
        # Menampilkan derajat setiap node
        degrees = dict(self.G.degree())
        print("Derajat setiap node:")
        for node, degree in degrees.items():
            print(f"Node {node}: Degree {degree}")
        return degrees

    def display_nodes_and_edges(self):
        # Menampilkan semua node dan edge dalam graf
        print("Nodes dalam graf:", list(self.G.nodes))
        print("Edges dalam graf:", list(self.G.edges))

    def calculate_density(self):
        # Menghitung densitas graf
        density = nx.density(self.G)
        print(f"Densitas graf: {density}")
        return density

    def find_all_shortest_paths(self, start, end):
        # Menemukan semua jalur terpendek antara dua node
        all_paths = list(nx.all_shortest_paths(self.G, source=start, target=end, weight='weight'))
        print(f"Semua jalur terpendek dari {start} ke {end}: {all_paths}")
        return all_paths


# Implementasi
if __name__ == "__main__":
    # Membuat objek graf
    graph = Graf()

    # Menambahkan node
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    # Menambahkan edge
    graph.add_edge(1, 2, weight=4.5)
    graph.add_edge(1, 3, weight=3.2)
    graph.add_edge(2, 4, weight=2.7)
    graph.add_edge(3, 4, weight=1.8)
    graph.add_edge(1, 4, weight=6.7)
    graph.add_edge(3, 5, weight=2.7)

    # Visualisasi graf
    graph.visualize_graph()

    # Jalur terpendek
    graph.shortest_path(1, 5)

    # Visualisasi jalur terpendek
    graph.visual_shortest_path(1, 5)

    # Metode tambahan
    graph.check_connected()
    graph.get_degree()
    graph.display_nodes_and_edges()
    graph.calculate_density()
    graph.find_all_shortest_paths(1, 5)
