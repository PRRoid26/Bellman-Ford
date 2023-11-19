class Network:
  def __init__(self, num_nodes):
      self.num_nodes = num_nodes
      self.edges = []

  def add_edge(self, src, dest, weight):
      self.edges.append((src, dest, weight))

  def bellman_ford(self, source):
      distance = [float('inf')] * self.num_nodes
      distance[source] = 0

      for _ in range(self.num_nodes - 1):
          for src, dest, weight in self.edges:
              if distance[src] + weight < distance[dest]:
                  distance[dest] = distance[src] + weight

      negative_cycle = False
      for src, dest, weight in self.edges:
          if distance[src] + weight < distance[dest]:
              negative_cycle = True
              break

      if negative_cycle:
          print("Negative weight cycle detected. Cannot find reliable routes.")
      else:
          print("Shortest distance from the source node:")
          for node, dist in enumerate(distance):
              if dist == float('inf'):
                  print(f"Node {node}: Not reachable")
              else:
                  print(f"Node {node}: Distance {dist}")

if __name__ == "__main__":
  num_nodes = int(input("Enter the number of nodes: "))
  network = Network(num_nodes)

  num_edges = int(input("Enter the number of edges: "))
  for _ in range(num_edges):
      src = int(input("Enter the source node for the edge: "))
      dest = int(input("Enter the destination node for the edge: "))
      weight = int(input("Enter the weight of the edge: "))
      network.add_edge(src, dest, weight)

  source_node = int(input("Enter the source node for the Bellman-Ford algorithm: "))
  network.bellman_ford(source_node)
