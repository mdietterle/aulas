import  osmnx  as  ox, network  as nx

ox.config(log_console=True, use_cache=True)
# download the street network for Piedmont, CA
G = ox.graph_from_place('Piedmont, California, USA', network_type='drive')
# plot the street network with folium
graph_map = ox.plot_graph_folium(G, popup_attribute='name', edge_width=2)

# save as html file then display map as an iframe
filepath = 'data/graph.html'
graph_map.save(filepath)
IFrame(filepath, width=600, height=500)
# use networkx to calculate the shortest path between two nodes
origin_node = list(G.nodes())[0]
destination_node = list(G.nodes())[-1]
route = nx.shortest_path(G, origin_node, destination_node)
# plot the route with folium
route_map = ox.plot_route_folium(G, route)

# save as html file then display map as an iframe# save  
filepath = 'data/route.html'
route_map.save(filepath)
IFrame(filepath, width=600, height=500)