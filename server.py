import grpc
import time
import simple_pb2
import simple_pb2_grpc
from concurrent import futures
from io import BytesIO
from PIL import Image

class SimpleServiceServicer(simple_pb2_grpc.SimpleServiceServicer):
  def __init__(self):
    pass

  def SimpleSend(self, request, context):
    print(f"Received request: name={request.name}, number={request.number}")

    buf = BytesIO(request.img)
    buf.seek(0)
    img_obj = Image.open(buf)
    img_obj.save("plot.png")
    img_obj.close()
    buf.close()

    return simple_pb2.SimpleResponse(
      message=f"Hello {request.name}, you sent me {request.number}!"
    )

# Create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor())
simple_pb2_grpc.add_SimpleServiceServicer_to_server(SimpleServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("Server start.")

time.sleep(3600)
