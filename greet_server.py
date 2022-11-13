import grpc
from protos import greet_pb2, greet_pb2_grpc
from concurrent import futures


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(request)
        return greet_pb2.MessageResponse(message=f"{request.name} {request.surname}")

    def ServerRequests(self, request, context):
        print(request)
        for i in range(request.number):
            response = greet_pb2.MessageResponse(message=f"request number: {i+1}")
            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


serve()
