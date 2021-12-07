FROM python:3.8

# Move to a directory inside the image
WORKDIR /opt
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY model.proto model_pb2.py model_pb2_grpc.py ke4wot-server.py Search.py .

# Move a directory where we will execute the script
RUN mkdir /opt/run
WORKDIR /opt/run

ENTRYPOINT [ "python3","-u","/opt/ke4wot-server.py" ]