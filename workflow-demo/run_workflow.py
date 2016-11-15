
# coding: utf-8

# ## Container setup

# In[1]:

url = "http://192.168.99.100"
data_port = "5010"
snap_port = "5020"
shiny_data = "5030"
shiny_server = "32769"


# ## Get the Baylor network

# In[19]:

import json
import requests
r1 = requests.get("{}:{}/".format(url, data_port))


# In[20]:

data = json.loads(r1.text)
ctd = data["ctd"]
labels = data["labels"]
print ctd[0:250]


# ## Run community detection with SNAP

# In[21]:

r2 = requests.post('{}:{}/'.format(url, snap_port), data = {'ctd':ctd})


# In[22]:

data = json.loads(r2.text)
graph = data["graph"]
print graph[:500]
with open("current_graph.json" ,"w") as f:
    f.write(data["graph"])


# ## Load data into visualization tool

# In[24]:

r = requests.post('{}:{}/'.format(url, shiny_data), data = {'graph':graph})
print r.text


# ## Open the visualization
# 
# http://192.168.99.100:32769/sample-apps/BaylorInteractiveViewer/
import webbrowser

webbrowser.open("http://192.168.99.100:32769/sample-apps/BaylorInteractiveViewer/")
# In[11]:

graph_bak = graph


# In[ ]:



