# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: example.proto
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
    'example.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\"*\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x10\n\x08validity\x18\x02 \x01(\t\"\"\n\x10GetStatusRequest\x12\x0e\n\x06status\x18\x01 \x01(\t\"9\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\x1e\n\x0eGetUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\\\n\x0e\x45xampleService\x12!\n\x07GetUser\x12\x0f.GetUserRequest\x1a\x05.User\x12\'\n\tGetStatus\x12\x11.GetStatusRequest\x1a\x07.Statusb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STATUS']._serialized_start=17
  _globals['_STATUS']._serialized_end=59
  _globals['_GETSTATUSREQUEST']._serialized_start=61
  _globals['_GETSTATUSREQUEST']._serialized_end=95
  _globals['_USER']._serialized_start=97
  _globals['_USER']._serialized_end=154
  _globals['_GETUSERREQUEST']._serialized_start=156
  _globals['_GETUSERREQUEST']._serialized_end=186
  _globals['_EXAMPLESERVICE']._serialized_start=188
  _globals['_EXAMPLESERVICE']._serialized_end=280
# @@protoc_insertion_point(module_scope)
