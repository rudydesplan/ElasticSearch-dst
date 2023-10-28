#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings
warnings.filterwarnings("ignore")

# Connexion au cluster
client = Elasticsearch(hosts="http://localhost:9200")

# Specify the question number for the count query
question_number = "2-4"

# Perform a count operation on Elasticsearch
response = client.count(index="eval")

# Save the count response to a JSON file
with open("./eval/{}.json".format("q_" + question_number + "_response"), "w") as f:
  json.dump(dict(response), f, indent=2)