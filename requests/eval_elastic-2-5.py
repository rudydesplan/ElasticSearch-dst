#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings
warnings.filterwarnings("ignore")

# Connexion au cluster
client = Elasticsearch(hosts = "http://@localhost:9200")

# Préciser le numéro de votre question ici.
question_number = "2-5"

query ={
  "size": 0,
  "aggs": {
    "by_division": {
      "terms": {
        "field": "Division Name.keyword",
        "size": 10
      },
      "aggs": {
        "by_department": {
          "terms": {
            "field": "Department Name.keyword",
            "size": 10
          }
        }
      }
    }
  }
}

response = client.search(index="eval", body=query)

# Sauvegarde de la requête et la réponse dans un fichier json
with open("./eval/{}.json".format("q_" + question_number + "_response"), "w") as f:
  json.dump(dict(response), f, indent=2)

with open("./eval/{}.json".format("q_" + question_number + "_request"), "w") as f:
  json.dump(query, f, indent=2)