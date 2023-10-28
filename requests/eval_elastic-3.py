#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings
warnings.filterwarnings("ignore")

# Connexion au cluster
client = Elasticsearch(hosts = "http://@localhost:9200")

# Préciser le numéro de votre question ici.
question_number = "3"

query ={
    "size": 0,
    "aggs": {
        "missing_age": {"missing": {"field": "Age.keyword"}},
        "missing_class_name": {"missing": {"field": "Class Name.keyword"}},
        "missing_clothing_id": {"missing": {"field": "Clothing ID.keyword"}},
        "missing_department_name": {"missing": {"field": "Department Name.keyword"}},
        "missing_division_name": {"missing": {"field": "Division Name.keyword"}},
        "missing_positive_feedback_count": {"missing": {"field": "Positive Feedback Count.keyword"}},
        "missing_rating": {"missing": {"field": "Rating.keyword"}},
        "missing_recommended_ind": {"missing": {"field": "Recommended IND.keyword"}},
        "missing_review_text": {"missing": {"field": "Review Text.keyword"}},
        "missing_title": {"missing": {"field": "Title.keyword"}}
    }
}

response = client.search(index="eval", body=query)

# Sauvegarde de la requête et la réponse dans un fichier json
with open("./eval/{}.json".format("q_" + question_number + "_response"), "w") as f:
  json.dump(dict(response), f, indent=2)

with open("./eval/{}.json".format("q_" + question_number + "_request"), "w") as f:
  json.dump(query, f, indent=2)