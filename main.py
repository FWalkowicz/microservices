from microservices import greet_client, greet_server
import time

if __name__ == '__main__':
    greet_server.serve()
    start = time.time()
    greet_client.run()
    stop = time.time()
    print(stop - start, " sec")


