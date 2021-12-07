1. Run the docker image in order to enable the search mechanism to find similar terms, existing in a given ontology, to terms existing in pre-defined topics
To run the docker image on port 8062:
docker run -p 8062:8062 --rm -ti ke4wot /bin/bash
2. Run the client. The client queries the search mechanism by providing several ontologies and retrieving all the similar terms to the pre-defined topics
To run the client:
python ke4wot-client.py
3. Interpret the results.
The returned format of the data is as follows:
"topic 1": ["most_similar_term_in_ontology_for_topic1"], "topic 2": ["most_similar_term_in_ontology_for_topic2"]
