import grpc
from concurrent import futures
import time
# import the generated classes :
import model_pb2
import model_pb2_grpc
# import the function we made :
import Search as sm

port = 8062

# create a class to define the server functions, derived from
class SearchServicer(model_pb2_grpc.SearchServicer):
    def getSimilarTopicsFor(self, request, context):
        # define the buffer of the response :
        response = model_pb2.Result()
        # get the value of the response by calling the desired function :
        response.terms = sm.getSimilarTopicsFor(request.inputOntology)
        return response


# create a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
model_pb2_grpc.add_SearchServicer_to_server(SearchServicer(), server)
print("Starting server. Listening on port : " + str(port))
server.add_insecure_port("[::]:{}".format(port))
server.start()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)