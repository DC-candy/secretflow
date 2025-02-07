# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secretflow/ic/proto/handshake/algos/sgb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='secretflow/ic/proto/handshake/algos/sgb.proto',
  package='org.interconnection.v2.algos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-secretflow/ic/proto/handshake/algos/sgb.proto\x12\x1corg.interconnection.v2.algos\"\x97\x01\n\x11SgbParamsProposal\x12\x1a\n\x12supported_versions\x18\x01 \x03(\x05\x12\x1e\n\x16support_completely_sgb\x18\x64 \x01(\x08\x12\"\n\x1asupport_row_sample_by_tree\x18\x65 \x01(\x08\x12\"\n\x1asupport_col_sample_by_tree\x18\x66 \x01(\x08\"\xb0\x01\n\x0fSgbParamsResult\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x11\n\tnum_round\x18\x02 \x01(\x05\x12\x11\n\tmax_depth\x18\x03 \x01(\x05\x12\x1a\n\x12row_sample_by_tree\x18\x04 \x01(\x01\x12\x1a\n\x12\x63ol_sample_by_tree\x18\x05 \x01(\x01\x12\x12\n\nbucket_eps\x18\x06 \x01(\x01\x12\x1a\n\x12use_completely_sgb\x18\x64 \x01(\x08\x62\x06proto3'
)




_SGBPARAMSPROPOSAL = _descriptor.Descriptor(
  name='SgbParamsProposal',
  full_name='org.interconnection.v2.algos.SgbParamsProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='supported_versions', full_name='org.interconnection.v2.algos.SgbParamsProposal.supported_versions', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='support_completely_sgb', full_name='org.interconnection.v2.algos.SgbParamsProposal.support_completely_sgb', index=1,
      number=100, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='support_row_sample_by_tree', full_name='org.interconnection.v2.algos.SgbParamsProposal.support_row_sample_by_tree', index=2,
      number=101, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='support_col_sample_by_tree', full_name='org.interconnection.v2.algos.SgbParamsProposal.support_col_sample_by_tree', index=3,
      number=102, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=80,
  serialized_end=231,
)


_SGBPARAMSRESULT = _descriptor.Descriptor(
  name='SgbParamsResult',
  full_name='org.interconnection.v2.algos.SgbParamsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='org.interconnection.v2.algos.SgbParamsResult.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_round', full_name='org.interconnection.v2.algos.SgbParamsResult.num_round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_depth', full_name='org.interconnection.v2.algos.SgbParamsResult.max_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='row_sample_by_tree', full_name='org.interconnection.v2.algos.SgbParamsResult.row_sample_by_tree', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='col_sample_by_tree', full_name='org.interconnection.v2.algos.SgbParamsResult.col_sample_by_tree', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bucket_eps', full_name='org.interconnection.v2.algos.SgbParamsResult.bucket_eps', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_completely_sgb', full_name='org.interconnection.v2.algos.SgbParamsResult.use_completely_sgb', index=6,
      number=100, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=234,
  serialized_end=410,
)

DESCRIPTOR.message_types_by_name['SgbParamsProposal'] = _SGBPARAMSPROPOSAL
DESCRIPTOR.message_types_by_name['SgbParamsResult'] = _SGBPARAMSRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SgbParamsProposal = _reflection.GeneratedProtocolMessageType('SgbParamsProposal', (_message.Message,), {
  'DESCRIPTOR' : _SGBPARAMSPROPOSAL,
  '__module__' : 'secretflow.ic.proto.handshake.algos.sgb_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.algos.SgbParamsProposal)
  })
_sym_db.RegisterMessage(SgbParamsProposal)

SgbParamsResult = _reflection.GeneratedProtocolMessageType('SgbParamsResult', (_message.Message,), {
  'DESCRIPTOR' : _SGBPARAMSRESULT,
  '__module__' : 'secretflow.ic.proto.handshake.algos.sgb_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.algos.SgbParamsResult)
  })
_sym_db.RegisterMessage(SgbParamsResult)


# @@protoc_insertion_point(module_scope)
