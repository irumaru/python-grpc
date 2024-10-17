import grpc
import simple_pb2
import simple_pb2_grpc
import matplotlib.pyplot as plt
from io import BytesIO

plt.scatter([3, 5, 1], [2, 4, 1])
plt.xlabel("Timestamp")
plt.ylabel("Length")

buf = BytesIO()
plt.savefig(buf, format="png", dpi=100)
buf.seek(0)
image_bytes = buf.read()
buf.close()

with grpc.insecure_channel('localhost:50051') as channel:
  stub = simple_pb2_grpc.SimpleServiceStub(channel)
  name = "Iona"
  number = 401
  response = stub.SimpleSend(simple_pb2.SimpleRequest(name=name, number=number, img=image_bytes))

print(f"Received response: {response.message}")
