import grpc
import simple_pb2
import simple_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
  stub = simple_pb2_grpc.SimpleServiceStub(channel)
  name = "Iona"
  number = 401
  response = stub.SimpleSend(simple_pb2.SimpleRequest(name=name, number=number))

print(f"Received response: {response.message}")
