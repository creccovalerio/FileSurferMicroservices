# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: upload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cupload.proto\x12\tuploadcsv\"/\n\rUploadRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"0\n\x0bUploadReply\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x32H\n\x06Upload\x12>\n\x08\x64oUpload\x12\x18.uploadcsv.UploadRequest\x1a\x16.uploadcsv.UploadReply\"\x00\x42$\n\r../uploadcsv/B\x0bUploadProtoP\x01\xa2\x02\x03LOGb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'upload_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\r../uploadcsv/B\013UploadProtoP\001\242\002\003LOG'
  _globals['_UPLOADREQUEST']._serialized_start=27
  _globals['_UPLOADREQUEST']._serialized_end=74
  _globals['_UPLOADREPLY']._serialized_start=76
  _globals['_UPLOADREPLY']._serialized_end=124
  _globals['_UPLOAD']._serialized_start=126
  _globals['_UPLOAD']._serialized_end=198
# @@protoc_insertion_point(module_scope)