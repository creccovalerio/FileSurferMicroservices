# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: download.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64ownload.proto\x12\x0c\x64ownloadarff\"\x1e\n\x0f\x44ownloadRequest\x12\x0b\n\x03\x66id\x18\x01 \x01(\t\"2\n\rDownloadReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x32V\n\x08\x44ownload\x12J\n\ndoDownload\x12\x1d.downloadarff.DownloadRequest\x1a\x1b.downloadarff.DownloadReply\"\x00\x42)\n\x10../downloadarff/B\rDownloadProtoP\x01\xa2\x02\x03LOGb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'download_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020../downloadarff/B\rDownloadProtoP\001\242\002\003LOG'
  _globals['_DOWNLOADREQUEST']._serialized_start=32
  _globals['_DOWNLOADREQUEST']._serialized_end=62
  _globals['_DOWNLOADREPLY']._serialized_start=64
  _globals['_DOWNLOADREPLY']._serialized_end=114
  _globals['_DOWNLOAD']._serialized_start=116
  _globals['_DOWNLOAD']._serialized_end=202
# @@protoc_insertion_point(module_scope)