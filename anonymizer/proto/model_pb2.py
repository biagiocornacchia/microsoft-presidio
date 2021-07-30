# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/model.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11proto/model.proto\"+\n\x07Request\x12\x12\n\nuuidClient\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"-\n\x08\x44\x61taFile\x12\r\n\x05\x63hunk\x18\x01 \x01(\t\x12\x12\n\nuuidClient\x18\x02 \x01(\t\"=\n\x06\x43onfig\x12\x12\n\nuuidClient\x18\x01 \x01(\t\x12\x11\n\toperators\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"=\n\x07\x46ileAck\x12\x12\n\nuuidClient\x18\x01 \x01(\t\x12\x13\n\x06\x63hunks\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\t\n\x07_chunks\"W\n\x04Item\x12\x10\n\x08operator\x18\x01 \x01(\t\x12\x13\n\x0b\x65ntity_type\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x05\x12\x0c\n\x04text\x18\x05 \x01(\t\"f\n\x10RecognizerResult\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x13\n\x0b\x65ntity_type\x18\x04 \x01(\t\x12\x12\n\nuuidClient\x18\x05 \x01(\t\"g\n\x0e\x41nonymizedItem\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\x12\x13\n\x0b\x65ntity_type\x18\x03 \x01(\t\x12\x10\n\x08operator\x18\x04 \x01(\t\x12\x12\n\nuuidClient\x18\x05 \x01(\t2\x83\x02\n\x10\x41nonymizerEntity\x12\x36\n\x15sendRecognizerResults\x12\x11.RecognizerResult\x1a\x08.FileAck(\x01\x12\x32\n\x13sendAnonymizedItems\x12\x0f.AnonymizedItem\x1a\x08.FileAck(\x01\x12\x1f\n\nsendConfig\x12\x07.Config\x1a\x08.FileAck\x12!\n\x08sendFile\x12\t.DataFile\x1a\x08.FileAck(\x01\x12 \n\x07getText\x12\x08.Request\x1a\t.DataFile0\x01\x12\x1d\n\x08getItems\x12\x08.Request\x1a\x05.Item0\x01\x62\x06proto3'
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
    _descriptor.FieldDescriptor(
      name='type', full_name='Request.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=21,
  serialized_end=64,
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
    _descriptor.FieldDescriptor(
      name='uuidClient', full_name='DataFile.uuidClient', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=66,
  serialized_end=111,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuidClient', full_name='Config.uuidClient', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operators', full_name='Config.operators', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Config.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=113,
  serialized_end=174,
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
    _descriptor.OneofDescriptor(
      name='_chunks', full_name='FileAck._chunks',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=176,
  serialized_end=237,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operator', full_name='Item.operator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='Item.entity_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='Item.start', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='Item.end', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='Item.text', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=239,
  serialized_end=326,
)


_RECOGNIZERRESULT = _descriptor.Descriptor(
  name='RecognizerResult',
  full_name='RecognizerResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='RecognizerResult.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='RecognizerResult.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='RecognizerResult.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='RecognizerResult.entity_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuidClient', full_name='RecognizerResult.uuidClient', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=328,
  serialized_end=430,
)


_ANONYMIZEDITEM = _descriptor.Descriptor(
  name='AnonymizedItem',
  full_name='AnonymizedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='AnonymizedItem.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='AnonymizedItem.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='AnonymizedItem.entity_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='AnonymizedItem.operator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuidClient', full_name='AnonymizedItem.uuidClient', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=432,
  serialized_end=535,
)

_FILEACK.oneofs_by_name['_chunks'].fields.append(
  _FILEACK.fields_by_name['chunks'])
_FILEACK.fields_by_name['chunks'].containing_oneof = _FILEACK.oneofs_by_name['_chunks']
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['DataFile'] = _DATAFILE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['FileAck'] = _FILEACK
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['RecognizerResult'] = _RECOGNIZERRESULT
DESCRIPTOR.message_types_by_name['AnonymizedItem'] = _ANONYMIZEDITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'proto.model_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

DataFile = _reflection.GeneratedProtocolMessageType('DataFile', (_message.Message,), {
  'DESCRIPTOR' : _DATAFILE,
  '__module__' : 'proto.model_pb2'
  # @@protoc_insertion_point(class_scope:DataFile)
  })
_sym_db.RegisterMessage(DataFile)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'proto.model_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  })
_sym_db.RegisterMessage(Config)

FileAck = _reflection.GeneratedProtocolMessageType('FileAck', (_message.Message,), {
  'DESCRIPTOR' : _FILEACK,
  '__module__' : 'proto.model_pb2'
  # @@protoc_insertion_point(class_scope:FileAck)
  })
_sym_db.RegisterMessage(FileAck)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'proto.model_pb2'
  # @@protoc_insertion_point(class_scope:Item)
  })
_sym_db.RegisterMessage(Item)

RecognizerResult = _reflection.GeneratedProtocolMessageType('RecognizerResult', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZERRESULT,
  '__module__' : 'proto.model_pb2'
  # @@protoc_insertion_point(class_scope:RecognizerResult)
  })
_sym_db.RegisterMessage(RecognizerResult)

AnonymizedItem = _reflection.GeneratedProtocolMessageType('AnonymizedItem', (_message.Message,), {
  'DESCRIPTOR' : _ANONYMIZEDITEM,
  '__module__' : 'proto.model_pb2'
  # @@protoc_insertion_point(class_scope:AnonymizedItem)
  })
_sym_db.RegisterMessage(AnonymizedItem)



_ANONYMIZERENTITY = _descriptor.ServiceDescriptor(
  name='AnonymizerEntity',
  full_name='AnonymizerEntity',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=538,
  serialized_end=797,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendRecognizerResults',
    full_name='AnonymizerEntity.sendRecognizerResults',
    index=0,
    containing_service=None,
    input_type=_RECOGNIZERRESULT,
    output_type=_FILEACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendAnonymizedItems',
    full_name='AnonymizerEntity.sendAnonymizedItems',
    index=1,
    containing_service=None,
    input_type=_ANONYMIZEDITEM,
    output_type=_FILEACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendConfig',
    full_name='AnonymizerEntity.sendConfig',
    index=2,
    containing_service=None,
    input_type=_CONFIG,
    output_type=_FILEACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendFile',
    full_name='AnonymizerEntity.sendFile',
    index=3,
    containing_service=None,
    input_type=_DATAFILE,
    output_type=_FILEACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getText',
    full_name='AnonymizerEntity.getText',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DATAFILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getItems',
    full_name='AnonymizerEntity.getItems',
    index=5,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_ITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANONYMIZERENTITY)

DESCRIPTOR.services_by_name['AnonymizerEntity'] = _ANONYMIZERENTITY

# @@protoc_insertion_point(module_scope)
