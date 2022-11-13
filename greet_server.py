import grpc
from microservices.protos import greet_pb2, greet_pb2_grpc
from concurrent import futures


class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greet_pb2.MessageResponse(message=f"{request.name}, {request.surname}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
