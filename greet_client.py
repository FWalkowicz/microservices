import grpc
from protos import greet_pb2, greet_pb2_grpc


def run():
    with grpc.insecure_channel("192.168.0.40:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        rpc_call = input("Which rpc would you like to make: ")
        if rpc_call == "1":
            response = stub.SayHello(greet_pb2.MessageRequest(name="Filip", surname="Walkowicz"))
            print("hello " + response.message)

        if rpc_call == "2":
            response = stub.ServerRequests(greet_pb2.InfoRequest(number=10))
            print(response)
            for responses in response:
                print(responses)

run()
