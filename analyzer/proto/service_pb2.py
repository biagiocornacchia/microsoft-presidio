# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13proto/service.proto\"\x1d\n\x07Request\x12\x12\n\nuuidClient\x18\x01 \x01(\t\"-\n\x07\x46ileAck\x12\x12\n\nuuidClient\x18\x01 \x01(\t\x12\x0e\n\x06\x63hunks\x18\x02 \x01(\x05\"\x19\n\x08\x44\x61taFile\x12\r\n\x05\x63hunk\x18\x01 \x01(\t\"Q\n\x0f\x41nalyzerResults\x12\x13\n\x0b\x65ntity_type\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x05\x12\r\n\x05score\x18\x04 \x01(\x02\x32t\n\x0e\x41nalyzerEntity\x12,\n\x11sendFileToAnalyze\x12\t.DataFile\x1a\x08.FileAck\"\x00(\x01\x12\x34\n\x12GetAnalyzerResults\x12\x08.Request\x1a\x10.AnalyzerResults\"\x00\x30\x01\x62\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuidClient', full_name='Request.uuidClient', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=52,
)


_FILEACK = _descriptor.Descriptor(
  name='FileAck',
  full_name='FileAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuidClient', full_name='FileAck.uuidClient', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='FileAck.chunks', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=99,
)


_DATAFILE = _descriptor.Descriptor(
  name='DataFile',
  full_name='DataFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='DataFile.chunk', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=126,
)


_ANALYZERRESULTS = _descriptor.Descriptor(
  name='AnalyzerResults',
  full_name='AnalyzerResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='AnalyzerResults.entity_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='AnalyzerResults.start', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='AnalyzerResults.end', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='AnalyzerResults.score', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['FileAck'] = _FILEACK
DESCRIPTOR.message_types_by_name['DataFile'] = _DATAFILE
DESCRIPTOR.message_types_by_name['AnalyzerResults'] = _ANALYZERRESULTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'proto.service_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

FileAck = _reflection.GeneratedProtocolMessageType('FileAck', (_message.Message,), {
  'DESCRIPTOR' : _FILEACK,
  '__module__' : 'proto.service_pb2'
  # @@protoc_insertion_point(class_scope:FileAck)
  })
_sym_db.RegisterMessage(FileAck)

DataFile = _reflection.GeneratedProtocolMessageType('DataFile', (_message.Message,), {
  'DESCRIPTOR' : _DATAFILE,
  '__module__' : 'proto.service_pb2'
  # @@protoc_insertion_point(class_scope:DataFile)
  })
_sym_db.RegisterMessage(DataFile)

AnalyzerResults = _reflection.GeneratedProtocolMessageType('AnalyzerResults', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZERRESULTS,
  '__module__' : 'proto.service_pb2'
  # @@protoc_insertion_point(class_scope:AnalyzerResults)
  })
_sym_db.RegisterMessage(AnalyzerResults)



_ANALYZERENTITY = _descriptor.ServiceDescriptor(
  name='AnalyzerEntity',
  full_name='AnalyzerEntity',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=211,
  serialized_end=327,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendFileToAnalyze',
    full_name='AnalyzerEntity.sendFileToAnalyze',
    index=0,
    containing_service=None,
    input_type=_DATAFILE,
    output_type=_FILEACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAnalyzerResults',
    full_name='AnalyzerEntity.GetAnalyzerResults',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_ANALYZERRESULTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYZERENTITY)

DESCRIPTOR.services_by_name['AnalyzerEntity'] = _ANALYZERENTITY

# @@protoc_insertion_point(module_scope)
