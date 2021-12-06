To build the docker image:
docker build -t ke4wot .
To run the docker image with input parameters:
docker run -v D:/AI4EU:/opt/run -w /opt/run ke4wot --input "http://vi.uni-klu.ac.at/ontology/DrivingContext.owl" --output "output.csv"