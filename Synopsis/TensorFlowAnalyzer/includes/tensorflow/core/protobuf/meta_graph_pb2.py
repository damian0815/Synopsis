# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/meta_graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from tensorflow.core.framework import graph_pb2 as tensorflow_dot_core_dot_framework_dot_graph__pb2
from tensorflow.core.framework import op_def_pb2 as tensorflow_dot_core_dot_framework_dot_op__def__pb2
from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2
from tensorflow.core.protobuf import saver_pb2 as tensorflow_dot_core_dot_protobuf_dot_saver__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/meta_graph.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n)tensorflow/core/protobuf/meta_graph.proto\x12\ntensorflow\x1a\x19google/protobuf/any.proto\x1a%tensorflow/core/framework/graph.proto\x1a&tensorflow/core/framework/op_def.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\x1a$tensorflow/core/protobuf/saver.proto\"\x87\x05\n\x0cMetaGraphDef\x12;\n\rmeta_info_def\x18\x01 \x01(\x0b\x32$.tensorflow.MetaGraphDef.MetaInfoDef\x12\'\n\tgraph_def\x18\x02 \x01(\x0b\x32\x14.tensorflow.GraphDef\x12\'\n\tsaver_def\x18\x03 \x01(\x0b\x32\x14.tensorflow.SaverDef\x12\x43\n\x0e\x63ollection_def\x18\x04 \x03(\x0b\x32+.tensorflow.MetaGraphDef.CollectionDefEntry\x12\x41\n\rsignature_def\x18\x05 \x03(\x0b\x32*.tensorflow.MetaGraphDef.SignatureDefEntry\x12\x30\n\x0e\x61sset_file_def\x18\x06 \x03(\x0b\x32\x18.tensorflow.AssetFileDef\x1a\x8d\x01\n\x0bMetaInfoDef\x12\x1a\n\x12meta_graph_version\x18\x01 \x01(\t\x12,\n\x10stripped_op_list\x18\x02 \x01(\x0b\x32\x12.tensorflow.OpList\x12&\n\x08\x61ny_info\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04tags\x18\x04 \x03(\t\x1aO\n\x12\x43ollectionDefEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.tensorflow.CollectionDef:\x02\x38\x01\x1aM\n\x11SignatureDefEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.tensorflow.SignatureDef:\x02\x38\x01\"\xdf\x03\n\rCollectionDef\x12\x37\n\tnode_list\x18\x01 \x01(\x0b\x32\".tensorflow.CollectionDef.NodeListH\x00\x12\x39\n\nbytes_list\x18\x02 \x01(\x0b\x32#.tensorflow.CollectionDef.BytesListH\x00\x12\x39\n\nint64_list\x18\x03 \x01(\x0b\x32#.tensorflow.CollectionDef.Int64ListH\x00\x12\x39\n\nfloat_list\x18\x04 \x01(\x0b\x32#.tensorflow.CollectionDef.FloatListH\x00\x12\x35\n\x08\x61ny_list\x18\x05 \x01(\x0b\x32!.tensorflow.CollectionDef.AnyListH\x00\x1a\x19\n\x08NodeList\x12\r\n\x05value\x18\x01 \x03(\t\x1a\x1a\n\tBytesList\x12\r\n\x05value\x18\x01 \x03(\x0c\x1a\x1e\n\tInt64List\x12\x11\n\x05value\x18\x01 \x03(\x03\x42\x02\x10\x01\x1a\x1e\n\tFloatList\x12\x11\n\x05value\x18\x01 \x03(\x02\x42\x02\x10\x01\x1a.\n\x07\x41nyList\x12#\n\x05value\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\x06\n\x04kind\"s\n\nTensorInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05\x64type\x18\x02 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x32\n\x0ctensor_shape\x18\x03 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\"\xa0\x02\n\x0cSignatureDef\x12\x34\n\x06inputs\x18\x01 \x03(\x0b\x32$.tensorflow.SignatureDef.InputsEntry\x12\x36\n\x07outputs\x18\x02 \x03(\x0b\x32%.tensorflow.SignatureDef.OutputsEntry\x12\x13\n\x0bmethod_name\x18\x03 \x01(\t\x1a\x45\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.tensorflow.TensorInfo:\x02\x38\x01\x1a\x46\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.tensorflow.TensorInfo:\x02\x38\x01\"M\n\x0c\x41ssetFileDef\x12+\n\x0btensor_info\x18\x01 \x01(\x0b\x32\x16.tensorflow.TensorInfo\x12\x10\n\x08\x66ilename\x18\x02 \x01(\tB0\n\x18org.tensorflow.frameworkB\x0fMetaGraphProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_graph__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_op__def__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,tensorflow_dot_core_dot_protobuf_dot_saver__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_METAGRAPHDEF_METAINFODEF = _descriptor.Descriptor(
  name='MetaInfoDef',
  full_name='tensorflow.MetaGraphDef.MetaInfoDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_graph_version', full_name='tensorflow.MetaGraphDef.MetaInfoDef.meta_graph_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stripped_op_list', full_name='tensorflow.MetaGraphDef.MetaInfoDef.stripped_op_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='any_info', full_name='tensorflow.MetaGraphDef.MetaInfoDef.any_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='tensorflow.MetaGraphDef.MetaInfoDef.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=633,
  serialized_end=774,
)

_METAGRAPHDEF_COLLECTIONDEFENTRY = _descriptor.Descriptor(
  name='CollectionDefEntry',
  full_name='tensorflow.MetaGraphDef.CollectionDefEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.MetaGraphDef.CollectionDefEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.MetaGraphDef.CollectionDefEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=776,
  serialized_end=855,
)

_METAGRAPHDEF_SIGNATUREDEFENTRY = _descriptor.Descriptor(
  name='SignatureDefEntry',
  full_name='tensorflow.MetaGraphDef.SignatureDefEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.MetaGraphDef.SignatureDefEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.MetaGraphDef.SignatureDefEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=857,
  serialized_end=934,
)

_METAGRAPHDEF = _descriptor.Descriptor(
  name='MetaGraphDef',
  full_name='tensorflow.MetaGraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_info_def', full_name='tensorflow.MetaGraphDef.meta_info_def', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph_def', full_name='tensorflow.MetaGraphDef.graph_def', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='saver_def', full_name='tensorflow.MetaGraphDef.saver_def', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collection_def', full_name='tensorflow.MetaGraphDef.collection_def', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature_def', full_name='tensorflow.MetaGraphDef.signature_def', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asset_file_def', full_name='tensorflow.MetaGraphDef.asset_file_def', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_METAGRAPHDEF_METAINFODEF, _METAGRAPHDEF_COLLECTIONDEFENTRY, _METAGRAPHDEF_SIGNATUREDEFENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=934,
)


_COLLECTIONDEF_NODELIST = _descriptor.Descriptor(
  name='NodeList',
  full_name='tensorflow.CollectionDef.NodeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.CollectionDef.NodeList.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1243,
  serialized_end=1268,
)

_COLLECTIONDEF_BYTESLIST = _descriptor.Descriptor(
  name='BytesList',
  full_name='tensorflow.CollectionDef.BytesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.CollectionDef.BytesList.value', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1270,
  serialized_end=1296,
)

_COLLECTIONDEF_INT64LIST = _descriptor.Descriptor(
  name='Int64List',
  full_name='tensorflow.CollectionDef.Int64List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.CollectionDef.Int64List.value', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1298,
  serialized_end=1328,
)

_COLLECTIONDEF_FLOATLIST = _descriptor.Descriptor(
  name='FloatList',
  full_name='tensorflow.CollectionDef.FloatList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.CollectionDef.FloatList.value', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1330,
  serialized_end=1360,
)

_COLLECTIONDEF_ANYLIST = _descriptor.Descriptor(
  name='AnyList',
  full_name='tensorflow.CollectionDef.AnyList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.CollectionDef.AnyList.value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1362,
  serialized_end=1408,
)

_COLLECTIONDEF = _descriptor.Descriptor(
  name='CollectionDef',
  full_name='tensorflow.CollectionDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_list', full_name='tensorflow.CollectionDef.node_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_list', full_name='tensorflow.CollectionDef.bytes_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64_list', full_name='tensorflow.CollectionDef.int64_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_list', full_name='tensorflow.CollectionDef.float_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='any_list', full_name='tensorflow.CollectionDef.any_list', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTIONDEF_NODELIST, _COLLECTIONDEF_BYTESLIST, _COLLECTIONDEF_INT64LIST, _COLLECTIONDEF_FLOATLIST, _COLLECTIONDEF_ANYLIST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='tensorflow.CollectionDef.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=937,
  serialized_end=1416,
)


_TENSORINFO = _descriptor.Descriptor(
  name='TensorInfo',
  full_name='tensorflow.TensorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.TensorInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow.TensorInfo.dtype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensor_shape', full_name='tensorflow.TensorInfo.tensor_shape', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1418,
  serialized_end=1533,
)


_SIGNATUREDEF_INPUTSENTRY = _descriptor.Descriptor(
  name='InputsEntry',
  full_name='tensorflow.SignatureDef.InputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.SignatureDef.InputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.SignatureDef.InputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1683,
  serialized_end=1752,
)

_SIGNATUREDEF_OUTPUTSENTRY = _descriptor.Descriptor(
  name='OutputsEntry',
  full_name='tensorflow.SignatureDef.OutputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.SignatureDef.OutputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.SignatureDef.OutputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1754,
  serialized_end=1824,
)

_SIGNATUREDEF = _descriptor.Descriptor(
  name='SignatureDef',
  full_name='tensorflow.SignatureDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='tensorflow.SignatureDef.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='tensorflow.SignatureDef.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='tensorflow.SignatureDef.method_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREDEF_INPUTSENTRY, _SIGNATUREDEF_OUTPUTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1536,
  serialized_end=1824,
)


_ASSETFILEDEF = _descriptor.Descriptor(
  name='AssetFileDef',
  full_name='tensorflow.AssetFileDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_info', full_name='tensorflow.AssetFileDef.tensor_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='tensorflow.AssetFileDef.filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1826,
  serialized_end=1903,
)

_METAGRAPHDEF_METAINFODEF.fields_by_name['stripped_op_list'].message_type = tensorflow_dot_core_dot_framework_dot_op__def__pb2._OPLIST
_METAGRAPHDEF_METAINFODEF.fields_by_name['any_info'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_METAGRAPHDEF_METAINFODEF.containing_type = _METAGRAPHDEF
_METAGRAPHDEF_COLLECTIONDEFENTRY.fields_by_name['value'].message_type = _COLLECTIONDEF
_METAGRAPHDEF_COLLECTIONDEFENTRY.containing_type = _METAGRAPHDEF
_METAGRAPHDEF_SIGNATUREDEFENTRY.fields_by_name['value'].message_type = _SIGNATUREDEF
_METAGRAPHDEF_SIGNATUREDEFENTRY.containing_type = _METAGRAPHDEF
_METAGRAPHDEF.fields_by_name['meta_info_def'].message_type = _METAGRAPHDEF_METAINFODEF
_METAGRAPHDEF.fields_by_name['graph_def'].message_type = tensorflow_dot_core_dot_framework_dot_graph__pb2._GRAPHDEF
_METAGRAPHDEF.fields_by_name['saver_def'].message_type = tensorflow_dot_core_dot_protobuf_dot_saver__pb2._SAVERDEF
_METAGRAPHDEF.fields_by_name['collection_def'].message_type = _METAGRAPHDEF_COLLECTIONDEFENTRY
_METAGRAPHDEF.fields_by_name['signature_def'].message_type = _METAGRAPHDEF_SIGNATUREDEFENTRY
_METAGRAPHDEF.fields_by_name['asset_file_def'].message_type = _ASSETFILEDEF
_COLLECTIONDEF_NODELIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_BYTESLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_INT64LIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_FLOATLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_ANYLIST.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_COLLECTIONDEF_ANYLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF.fields_by_name['node_list'].message_type = _COLLECTIONDEF_NODELIST
_COLLECTIONDEF.fields_by_name['bytes_list'].message_type = _COLLECTIONDEF_BYTESLIST
_COLLECTIONDEF.fields_by_name['int64_list'].message_type = _COLLECTIONDEF_INT64LIST
_COLLECTIONDEF.fields_by_name['float_list'].message_type = _COLLECTIONDEF_FLOATLIST
_COLLECTIONDEF.fields_by_name['any_list'].message_type = _COLLECTIONDEF_ANYLIST
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['node_list'])
_COLLECTIONDEF.fields_by_name['node_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['bytes_list'])
_COLLECTIONDEF.fields_by_name['bytes_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['int64_list'])
_COLLECTIONDEF.fields_by_name['int64_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['float_list'])
_COLLECTIONDEF.fields_by_name['float_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['any_list'])
_COLLECTIONDEF.fields_by_name['any_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_TENSORINFO.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_TENSORINFO.fields_by_name['tensor_shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_SIGNATUREDEF_INPUTSENTRY.fields_by_name['value'].message_type = _TENSORINFO
_SIGNATUREDEF_INPUTSENTRY.containing_type = _SIGNATUREDEF
_SIGNATUREDEF_OUTPUTSENTRY.fields_by_name['value'].message_type = _TENSORINFO
_SIGNATUREDEF_OUTPUTSENTRY.containing_type = _SIGNATUREDEF
_SIGNATUREDEF.fields_by_name['inputs'].message_type = _SIGNATUREDEF_INPUTSENTRY
_SIGNATUREDEF.fields_by_name['outputs'].message_type = _SIGNATUREDEF_OUTPUTSENTRY
_ASSETFILEDEF.fields_by_name['tensor_info'].message_type = _TENSORINFO
DESCRIPTOR.message_types_by_name['MetaGraphDef'] = _METAGRAPHDEF
DESCRIPTOR.message_types_by_name['CollectionDef'] = _COLLECTIONDEF
DESCRIPTOR.message_types_by_name['TensorInfo'] = _TENSORINFO
DESCRIPTOR.message_types_by_name['SignatureDef'] = _SIGNATUREDEF
DESCRIPTOR.message_types_by_name['AssetFileDef'] = _ASSETFILEDEF

MetaGraphDef = _reflection.GeneratedProtocolMessageType('MetaGraphDef', (_message.Message,), dict(

  MetaInfoDef = _reflection.GeneratedProtocolMessageType('MetaInfoDef', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_METAINFODEF,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.MetaGraphDef.MetaInfoDef)
    ))
  ,

  CollectionDefEntry = _reflection.GeneratedProtocolMessageType('CollectionDefEntry', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_COLLECTIONDEFENTRY,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.MetaGraphDef.CollectionDefEntry)
    ))
  ,

  SignatureDefEntry = _reflection.GeneratedProtocolMessageType('SignatureDefEntry', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_SIGNATUREDEFENTRY,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.MetaGraphDef.SignatureDefEntry)
    ))
  ,
  DESCRIPTOR = _METAGRAPHDEF,
  __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MetaGraphDef)
  ))
_sym_db.RegisterMessage(MetaGraphDef)
_sym_db.RegisterMessage(MetaGraphDef.MetaInfoDef)
_sym_db.RegisterMessage(MetaGraphDef.CollectionDefEntry)
_sym_db.RegisterMessage(MetaGraphDef.SignatureDefEntry)

CollectionDef = _reflection.GeneratedProtocolMessageType('CollectionDef', (_message.Message,), dict(

  NodeList = _reflection.GeneratedProtocolMessageType('NodeList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_NODELIST,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CollectionDef.NodeList)
    ))
  ,

  BytesList = _reflection.GeneratedProtocolMessageType('BytesList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_BYTESLIST,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CollectionDef.BytesList)
    ))
  ,

  Int64List = _reflection.GeneratedProtocolMessageType('Int64List', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_INT64LIST,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CollectionDef.Int64List)
    ))
  ,

  FloatList = _reflection.GeneratedProtocolMessageType('FloatList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_FLOATLIST,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CollectionDef.FloatList)
    ))
  ,

  AnyList = _reflection.GeneratedProtocolMessageType('AnyList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_ANYLIST,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CollectionDef.AnyList)
    ))
  ,
  DESCRIPTOR = _COLLECTIONDEF,
  __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CollectionDef)
  ))
_sym_db.RegisterMessage(CollectionDef)
_sym_db.RegisterMessage(CollectionDef.NodeList)
_sym_db.RegisterMessage(CollectionDef.BytesList)
_sym_db.RegisterMessage(CollectionDef.Int64List)
_sym_db.RegisterMessage(CollectionDef.FloatList)
_sym_db.RegisterMessage(CollectionDef.AnyList)

TensorInfo = _reflection.GeneratedProtocolMessageType('TensorInfo', (_message.Message,), dict(
  DESCRIPTOR = _TENSORINFO,
  __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TensorInfo)
  ))
_sym_db.RegisterMessage(TensorInfo)

SignatureDef = _reflection.GeneratedProtocolMessageType('SignatureDef', (_message.Message,), dict(

  InputsEntry = _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATUREDEF_INPUTSENTRY,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.SignatureDef.InputsEntry)
    ))
  ,

  OutputsEntry = _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATUREDEF_OUTPUTSENTRY,
    __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.SignatureDef.OutputsEntry)
    ))
  ,
  DESCRIPTOR = _SIGNATUREDEF,
  __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.SignatureDef)
  ))
_sym_db.RegisterMessage(SignatureDef)
_sym_db.RegisterMessage(SignatureDef.InputsEntry)
_sym_db.RegisterMessage(SignatureDef.OutputsEntry)

AssetFileDef = _reflection.GeneratedProtocolMessageType('AssetFileDef', (_message.Message,), dict(
  DESCRIPTOR = _ASSETFILEDEF,
  __module__ = 'tensorflow.core.protobuf.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.AssetFileDef)
  ))
_sym_db.RegisterMessage(AssetFileDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\017MetaGraphProtosP\001\370\001\001'))
_METAGRAPHDEF_COLLECTIONDEFENTRY.has_options = True
_METAGRAPHDEF_COLLECTIONDEFENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_METAGRAPHDEF_SIGNATUREDEFENTRY.has_options = True
_METAGRAPHDEF_SIGNATUREDEFENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_COLLECTIONDEF_INT64LIST.fields_by_name['value'].has_options = True
_COLLECTIONDEF_INT64LIST.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_COLLECTIONDEF_FLOATLIST.fields_by_name['value'].has_options = True
_COLLECTIONDEF_FLOATLIST.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SIGNATUREDEF_INPUTSENTRY.has_options = True
_SIGNATUREDEF_INPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SIGNATUREDEF_OUTPUTSENTRY.has_options = True
_SIGNATUREDEF_OUTPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
