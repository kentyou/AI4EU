import numpy as np
import sys
import time
import argparse
import json
from collections import defaultdict
from Levenshtein import distance as levenshtein_distance
from gensim.models import KeyedVectors
from owlready2 import *

predefined_mobility_terms = "vehicle car electric vehicle,charging charging station,speed acceleration,driver participant passenger,road lane marking road condition route,traffic sign traffic light traffic sign information sign danger sign marking,trajectory,fuel gas oil petrol,power,location spatial spatiotemporal point time instant,date time,unit,wind,water,Actuator Actuation,Sensor Device,Feature interest,Observation,Sampling,bicycle,camera,parking,bus".split(",")
predefined_city_terms = "parking,bike,event,facility,country,person,city,neighborhood,station,bus,transport,monument museum,location altitude longitude latitude point spatial,actuator,device,sensor,feature interest,time temporal,unit,measurement,pollen,air quality".split(",")
predefined_terms = predefined_mobility_terms + predefined_city_terms

# load google embeddings
news_path = 'https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz'  # 'GoogleNews-vectors-negative300.bin'
embeddings_index = KeyedVectors.load_word2vec_format(news_path, binary=True)


def getSimilarTopicsFor(inputOntology, outputFile):

	try:
		best_concepts = defaultdict(list)
		# parse ontology to extract entities and vocabulary
		ontology = get_ontology(inputOntology).load()
		ontology_cpi = list(ontology.classes()) + list(ontology.properties()) + list(ontology.individuals())
		wordsOfDocument = list()
		for ontology_class in ontology_cpi:
			splitted_class = str(ontology_class).split(".")
			lastWordAfterDot = splitted_class[len(splitted_class) - 1]
			lastSplit = str(lastWordAfterDot).split(":")
			wordsOfDocument.append(lastSplit[len(lastSplit) - 1])


		#for each predefined topic, we search for a similar term in the input ontology
		for topic in set(predefined_terms):
			try:
				similar_terms = embeddings_index.most_similar(positive=topic.split(" "))
				splitted_topics = topic.split(" ")
				for sp_top in splitted_topics: #each term belongs to the similar terms
					similar_terms.insert(0, (sp_top, 1))
				min_distance = sys.maxsize
				for term in similar_terms: #we search each similar term if it belongs to the input ontology
					for word in wordsOfDocument:
						distance = levenshtein_distance(word, term[0])

						if distance < min_distance:
							min_distance = distance
							best_topic_in_O = word
				if min_distance < 5:
					best_concepts[topic].append(best_topic_in_O)
				else:
					best_concepts[topic].append("Not found")
				best_topic_in_O = ""
			except Exception as ex:
				print(f'exception: {topic} {ex}')


		# f = open(outputFile, 'a')
		# f.write("," + inputOntology + "\n")
		# for x in best_concepts:
		# 	f.write(str(x) + "," + str(best_concepts[x])[1:len(str(best_concepts[x])) - 1] + "\n")
		# f.close()
		print(json.dumps(best_concepts))
		return json.dumps(best_concepts)
		# with open(outputFile,'w') as convert_file:
		# 	convert_file.write("," + inputOntology + "\n")
		# 	for x in best_concepts:
		# 		convert_file.write(str(x) + "," + str(best_concepts[x])[1:len(str(best_concepts[x])) - 1] + "\n")
	except Exception as ex:
		print(f'Exception in main {ex}')

