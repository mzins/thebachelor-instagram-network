import networkx as nx
from pprint import pprint
from collections import defaultdict
import statistics


def print_metrics(G):
    print(f"Number of nodes: {len(G.nodes)}")
    print(f"Number of edges: {len(G.edges)}")

    print(f"Density: {nx.density(G)}")
    
    print(f"Diameter: {nx.diameter(G)}")
    print(f"Average Path: {nx.average_shortest_path_length(G)}")

    degrees = [x[1] for x in G.degree]
    print(f"Average Degree: {statistics.mean(degrees)}")
    print(f"Median Degree: {statistics.median(degrees)}")

    print(f"Transitivity: {nx.transitivity(G)}")

    degrees = list(nx.degree(G))
    degrees.sort(key=lambda tup: tup[1], reverse=True)
    print(f"Users with highest degree: {degrees[:3]}")
    print(f"Users with lowest degree: {degrees[-3:]}")

    centrality = nx.betweenness_centrality(G)
    centrality = [(k,v) for k,v in centrality.items()]
    centrality_val = [v for k,v in nx.betweenness_centrality(G).items()]

    centrality.sort(key=lambda tup: tup[1], reverse=True)

    print(f"Average Centrality: {statistics.mean(centrality_val)}")
    print(f"Median Centrality: {statistics.median(centrality_val)}")

    print(f"Users with highest betweenness centrality: {centrality[:3]}")

    eigenvector = nx.eigenvector_centrality(G)
    eig = [(k,v) for k,v in eigenvector.items()]
    eig.sort(key=lambda tup: tup[1], reverse=True)

    print(f"Users with highest eigenvector centrality: {eig[:3]}")

def print_contestant_metrics(contestants):
    centrality = nx.degree_centrality(G)

    for c in contestants:
        print(c, G.nodes[c]['season'], G.degree(c), centrality[c])

G = nx.read_graphml("data/bachelor-nation.graphml")
print_metrics(G)

season_27_nodes = [x for x,y in G.nodes(data=True) if y["season"]=="bachelor-27"]
season_27_edges = []
for x in season_27_nodes:
    season_27_edges.extend(G.edges(x))

g_27 =  G.__class__()
g_27.add_nodes_from(season_27_nodes)
g_27.add_edges_from(season_27_edges)

print_metrics(g_27)

# Print inter-season connectivity
pairs = defaultdict(int)
seasons = nx.get_node_attributes(G, "season")

for node in G.nodes():
    edges = G.edges(node)
    node_season = seasons.get(node)
    for e in edges:
        edge_season = seasons.get(e[1])
        key = node_season + edge_season
        pairs[key] += 1

pprint(pairs)

villains = nx.get_node_attributes(G, "villain")
finalists = nx.get_node_attributes(G, "finalist")

print_contestant_metrics(finalists)

