import grpc
from random import randint
from timeit import default_timer as timer

# import the generated classes
import model_pb2
import model_pb2_grpc

start_ch = timer()
port_addr = 'localhost:8062'

# open a gRPC channel
channel = grpc.insecure_channel(port_addr)

# create a stub (client)
stub = model_pb2_grpc.SearchStub(channel)
end_ch = timer()

OntologyFiles = [
    "http://vi.uni-klu.ac.at/ontology/DrivingContext.owl",
    "https://raw.githubusercontent.com/doroam/planning-do-roam/master/Ontology/tags.owl",
    "https://raw.githubusercontent.com/iand/vocab-transit/master/vocab.rdf",
    "https://raw.githubusercontent.com/jwaliszko/msc-thesis/master/setup/ontology/TrafficDanger.owl",
    "http://www.heppnetz.de/ontologies/vso/ns.owl",
    "https://www.toyota-ti.ac.jp/Lab/Denshi/COIN/Ontology/TTICore-0.03/TTIControlOnto.owl",
    "https://www.toyota-ti.ac.jp/Lab/Denshi/COIN/Ontology/TTICore-0.03/TTIMapOnto.owl",
    "https://raw.githubusercontent.com/talespaiva/step/gh-pages/ontology/step_v2.rdf",
    "https://raw.githubusercontent.com/transportdisruption/transportdisruption.github.io/master/transportdisruption.owl",
    "http://iot.ee.surrey.ac.uk/citypulse/ontologies/sao/saov06.rdf",
    "http://philippe.morignot.free.fr/Articles/Perception.owl",
    "D:/kentyou.com/kentyou.com - General/2- Institutional Projects/7-AI4EU/KE4WoT/datasets/transportation/bikesharing.rdf"
]

ans_lst = []
start = timer()

for i in range(0, len(OntologyFiles) - 1):
    # create a valid request message
    print(OntologyFiles[i])
    requestSearch = model_pb2.Features(inputOntology=OntologyFiles[i], outputFile="output.csv")
    print('returned request search')
    # make the call
    responseSearch = stub.getSimilarTopicsFor(requestSearch)
    print(f'returned response {responseSearch.terms}')
    ans_lst.append(responseSearch.terms)
    print('The terms are :', responseSearch.terms)

print('Done!')
end = timer()
all_time = end - start
ch_time = end_ch - start_ch
print('Time spent for {} predictions is {}'.format(len(MSSubClass), (all_time)))
print('In average, {} second for each prediction'.format(all_time / len(MSSubClass)))
print('That means you can do {} predictions in onesecond'.format(int(1/(all_time/len(MSSubClass)))))
print('Time for connecting to server = {}'.format(ch_time))