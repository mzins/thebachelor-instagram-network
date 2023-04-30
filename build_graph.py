import json
import networkx as nx


with open("data/following.json") as f:
    followers_list = json.load(f)

edge_list = []

for cast, following in followers_list.items():
    for follow in following:
        if followers_list.get(follow[1]) is not None:
            edge_list.append((cast, follow[1]))

G = nx.from_edgelist(edge_list)

with open("data/usernames.json") as f:
    seasons = json.load(f)

attrs = {}
for season, cast in seasons.items():
    for c,v in cast.items():
        attrs.update({v: {"season": season}})

for lead in ["zachshallcross", "claytonechard", "pilot.rachel", "gabby.windey"]:
    attrs.get(lead).update({"lead": True})


finalists = ["greggrippo", "justinglaze", "oh_for_schwer", "johnnyxdep", 
             "zachshallcross", "tino.360", "tylerjnorris9", "susiecevans", 
             "serenebrookrussell", "gabby.windey", "pilot.rachel", 
             "sprinkling_sunshine", "afrenkel1", "charitylawson", "kaityylane"]

for finalist in finalists:
    attrs.get(finalist).update({"finalist": True})

villains = ["thomasajacobs", "hmark01221", "shanae.a", "christinamandrell"]
for villain in villains:
    attrs.get(villain).update({"villain": True})

nx.set_node_attributes(G, attrs)

nx.write_graphml(G, "data/bachelor-nation.graphml")

