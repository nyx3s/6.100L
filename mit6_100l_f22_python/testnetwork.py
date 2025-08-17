import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edges_from([(1, 2), (1, 3)])

nx.draw(G, with_labels=True, font_weight='bold')



nx.draw_shell(G)
plt.show()




