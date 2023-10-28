#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings
warnings.filterwarnings("ignore")

# Connexion au cluster
client = Elasticsearch(hosts = "http://@localhost:9200")

# Préciser le numéro de votre question ici.
question_number = "5-1"

query ={
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "Rating": {
              "gt": 4
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "most_frequent_classes": {
      "terms": {
        "field": "Class Name.keyword",
        "size": 5
      }
    }
  },
  "size": 0
}

response = client.search(index="eval", body=query)

# Sauvegarde de la requête et la réponse dans un fichier json
with open("./eval/{}.json".format("q_" + question_number + "_response"), "w") as f:
  json.dump(dict(response), f, indent=2)

with open("./eval/{}.json".format("q_" + question_number + "_request"), "w") as f:
  json.dump(query, f, indent=2)