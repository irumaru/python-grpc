# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: simple.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'simple.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csimple.proto\x12\x06simple\"-\n\rSimpleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x03\"!\n\x0eSimpleResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2N\n\rSimpleService\x12=\n\nSimpleSend\x12\x15.simple.SimpleRequest\x1a\x16.simple.SimpleResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simple_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SIMPLEREQUEST']._serialized_start=24
  _globals['_SIMPLEREQUEST']._serialized_end=69
  _globals['_SIMPLERESPONSE']._serialized_start=71
  _globals['_SIMPLERESPONSE']._serialized_end=104
  _globals['_SIMPLESERVICE']._serialized_start=106
  _globals['_SIMPLESERVICE']._serialized_end=184
# @@protoc_insertion_point(module_scope)
