python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. model.proto
To build the docker image:
docker build -t ke4wot .
To run the docker image with input parameters:
docker run -p 8062:8062 --rm -ti ke4wot /bin/bash
