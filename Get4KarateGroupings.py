# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'python-modularity-maximization'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# The following two examples use data in the both cited papers mentioned in the index page.

#%%
import networkx as nx
nx.__version__


#%%
from modularity_maximization import partition
from modularity_maximization.utils import get_modularity

#%% [markdown]
# #### Undirected Network: Karate

#%%
karate = nx.Graph(nx.read_pajek("data/karate.net"))


#%%
print(nx.info(karate))


#%%
comm_dict = partition(karate)


#%%
for comm in set(comm_dict.values()):
    print("Community %d"%comm)
    print(', '.join([node for node in comm_dict if comm_dict[node] == comm]))


#%%
print('Modularity of such partition for karate is %.3f' % get_modularity(karate, comm_dict))

#%% [markdown]
# #### Jazz Network

#%%
jazz = nx.Graph(nx.read_pajek("data/jazz.net"))


#%%
print(nx.info(jazz))


#%%
comm_dict = partition(jazz)


#%%
for comm in set(comm_dict.values()):
    print("Community %d"%comm)
    print(', '.join([node for node in comm_dict if comm_dict[node] == comm]))


#%%
print('Modularity of such partition for jazz is %.3f' % get_modularity(jazz, comm_dict))

#%% [markdown]
# #### Directed Network: Big 10 Football Season 2005

#%%
big_10_football = nx.read_gml("data/big_10_football_directed.gml")


#%%
print(nx.info(big_10_football))


#%%
comm_dict = partition(big_10_football)


#%%
for comm in set(comm_dict.values()):
    print("Community %d"%comm)
    print(', '.join([node for node in comm_dict if comm_dict[node] == comm]))


#%%
print('Modularity of such partition for karate is %.3f' %      get_modularity(big_10_football, comm_dict))

