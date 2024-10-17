# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import simple_pb2 as simple__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in simple_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SimpleServiceStub(object):
    """interface
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SimpleSend = channel.unary_unary(
                '/simple.SimpleService/SimpleSend',
                request_serializer=simple__pb2.SimpleRequest.SerializeToString,
                response_deserializer=simple__pb2.SimpleResponse.FromString,
                _registered_method=True)


class SimpleServiceServicer(object):
    """interface
    """

    def SimpleSend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SimpleSend': grpc.unary_unary_rpc_method_handler(
                    servicer.SimpleSend,
                    request_deserializer=simple__pb2.SimpleRequest.FromString,
                    response_serializer=simple__pb2.SimpleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'simple.SimpleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('simple.SimpleService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SimpleService(object):
    """interface
    """

    @staticmethod
    def SimpleSend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/simple.SimpleService/SimpleSend',
            simple__pb2.SimpleRequest.SerializeToString,
            simple__pb2.SimpleResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
