# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cfg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cfg.proto',
  package='scaii.common',
  syntax='proto2',
  serialized_pb=_b('\n\tcfg.proto\x12\x0cscaii.common\"\xcd\x01\n\x03\x43\x66g\x12)\n\x08\x63ore_cfg\x18\x01 \x01(\x0b\x32\x15.scaii.common.CoreCfgH\x00\x12/\n\x0b\x62\x61\x63kend_cfg\x18\x02 \x01(\x0b\x32\x18.scaii.common.BackendCfgH\x00\x12+\n\tagent_cfg\x18\x03 \x01(\x0b\x32\x16.scaii.common.AgentCfgH\x00\x12-\n\nmodule_cfg\x18\x04 \x01(\x0b\x32\x17.scaii.common.ModuleCfgH\x00\x42\x0e\n\x0cwhich_module\"l\n\nPluginType\x12\'\n\x07sky_rts\x18\x01 \x01(\x0b\x32\x14.scaii.common.SkyRtsH\x00\x12&\n\x03rpc\x18\x02 \x01(\x0b\x32\x17.scaii.common.RpcConfigH\x00\x42\r\n\x0bplugin_type\"8\n\x07\x43oreCfg\x12-\n\x0bplugin_type\x18\x01 \x02(\x0b\x32\x18.scaii.common.PluginType\"m\n\x06InitAs\x12,\n\x07\x62\x61\x63kend\x18\x01 \x01(\x0b\x32\x19.scaii.common.BackendInitH\x00\x12*\n\x06module\x18\x02 \x01(\x0b\x32\x18.scaii.common.ModuleInitH\x00\x42\t\n\x07init_as\"\x08\n\x06SkyRts\"\r\n\x0b\x42\x61\x63kendInit\"\x1a\n\nModuleInit\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x84\x01\n\tRpcConfig\x12\x15\n\x02ip\x18\x01 \x01(\t:\t127.0.0.1\x12\x12\n\x04port\x18\x02 \x01(\r:\x04\x36\x31\x31\x32\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\t\x12\x14\n\x0c\x63ommand_args\x18\x04 \x03(\t\x12%\n\x07init_as\x18\x05 \x02(\x0b\x32\x14.scaii.common.InitAs\"5\n\nBackendCfg\x12\x0f\n\x07\x63\x66g_msg\x18\x01 \x01(\x0c\x12\x16\n\x0eis_replay_mode\x18\x02 \x02(\x08\"\x1b\n\x08\x41gentCfg\x12\x0f\n\x07\x63\x66g_msg\x18\x01 \x01(\x0c\"\x1c\n\tModuleCfg\x12\x0f\n\x07\x63\x66g_msg\x18\x01 \x01(\x0c\"\xbe\x01\n\x11SupportedBehavior\x12\x31\n\x07\x62\x61\x63kend\x18\x01 \x01(\x0b\x32\x1e.scaii.common.BackendSupportedH\x00\x12-\n\x05\x61gent\x18\x02 \x01(\x0b\x32\x1c.scaii.common.AgentSupportedH\x00\x12\x37\n\x0egeneric_module\x18\x05 \x01(\x0b\x32\x1d.scaii.common.ModuleSupportedH\x00\x42\x0e\n\x0cwhich_module\"\xc7\x01\n\x10\x42\x61\x63kendSupported\x12R\n\x15serialization_support\x18\x01 \x02(\x0e\x32\x33.scaii.common.BackendSupported.SerializationSupport\"U\n\x14SerializationSupport\x12\x08\n\x04NONE\x10\x00\x12\x12\n\x0e\x44IVERGING_ONLY\x10\x01\x12\x15\n\x11NONDIVERGING_ONLY\x10\x02\x12\x08\n\x04\x46ULL\x10\x03*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x1a\n\x0e\x41gentSupported*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x1b\n\x0fModuleSupported*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xef\x02\n\x0e\x45nvDescription\x12\x43\n\x0creward_types\x18\x01 \x03(\x0b\x32-.scaii.common.EnvDescription.RewardTypesEntry\x12\\\n\x19possible_discrete_actions\x18\x02 \x03(\x0b\x32\x39.scaii.common.EnvDescription.PossibleDiscreteActionsEntry\x12\x13\n\x0b\x61\x63tion_desc\x18\x03 \x01(\t\x12\x31\n\tsupported\x18\x04 \x02(\x0b\x32\x1e.scaii.common.BackendSupported\x1a\x32\n\x10RewardTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a>\n\x1cPossibleDiscreteActionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01')
)



_BACKENDSUPPORTED_SERIALIZATIONSUPPORT = _descriptor.EnumDescriptor(
  name='SerializationSupport',
  full_name='scaii.common.BackendSupported.SerializationSupport',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIVERGING_ONLY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONDIVERGING_ONLY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1114,
  serialized_end=1199,
)
_sym_db.RegisterEnumDescriptor(_BACKENDSUPPORTED_SERIALIZATIONSUPPORT)


_CFG = _descriptor.Descriptor(
  name='Cfg',
  full_name='scaii.common.Cfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='core_cfg', full_name='scaii.common.Cfg.core_cfg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backend_cfg', full_name='scaii.common.Cfg.backend_cfg', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agent_cfg', full_name='scaii.common.Cfg.agent_cfg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='module_cfg', full_name='scaii.common.Cfg.module_cfg', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='which_module', full_name='scaii.common.Cfg.which_module',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=28,
  serialized_end=233,
)


_PLUGINTYPE = _descriptor.Descriptor(
  name='PluginType',
  full_name='scaii.common.PluginType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sky_rts', full_name='scaii.common.PluginType.sky_rts', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpc', full_name='scaii.common.PluginType.rpc', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='plugin_type', full_name='scaii.common.PluginType.plugin_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=235,
  serialized_end=343,
)


_CORECFG = _descriptor.Descriptor(
  name='CoreCfg',
  full_name='scaii.common.CoreCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_type', full_name='scaii.common.CoreCfg.plugin_type', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=401,
)


_INITAS = _descriptor.Descriptor(
  name='InitAs',
  full_name='scaii.common.InitAs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backend', full_name='scaii.common.InitAs.backend', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='module', full_name='scaii.common.InitAs.module', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='init_as', full_name='scaii.common.InitAs.init_as',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=403,
  serialized_end=512,
)


_SKYRTS = _descriptor.Descriptor(
  name='SkyRts',
  full_name='scaii.common.SkyRts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=522,
)


_BACKENDINIT = _descriptor.Descriptor(
  name='BackendInit',
  full_name='scaii.common.BackendInit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=537,
)


_MODULEINIT = _descriptor.Descriptor(
  name='ModuleInit',
  full_name='scaii.common.ModuleInit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='scaii.common.ModuleInit.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=565,
)


_RPCCONFIG = _descriptor.Descriptor(
  name='RpcConfig',
  full_name='scaii.common.RpcConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='scaii.common.RpcConfig.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("127.0.0.1").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='scaii.common.RpcConfig.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=6112,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command', full_name='scaii.common.RpcConfig.command', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command_args', full_name='scaii.common.RpcConfig.command_args', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_as', full_name='scaii.common.RpcConfig.init_as', index=4,
      number=5, type=11, cpp_type=10, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=700,
)


_BACKENDCFG = _descriptor.Descriptor(
  name='BackendCfg',
  full_name='scaii.common.BackendCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cfg_msg', full_name='scaii.common.BackendCfg.cfg_msg', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_replay_mode', full_name='scaii.common.BackendCfg.is_replay_mode', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=755,
)


_AGENTCFG = _descriptor.Descriptor(
  name='AgentCfg',
  full_name='scaii.common.AgentCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cfg_msg', full_name='scaii.common.AgentCfg.cfg_msg', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=784,
)


_MODULECFG = _descriptor.Descriptor(
  name='ModuleCfg',
  full_name='scaii.common.ModuleCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cfg_msg', full_name='scaii.common.ModuleCfg.cfg_msg', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=786,
  serialized_end=814,
)


_SUPPORTEDBEHAVIOR = _descriptor.Descriptor(
  name='SupportedBehavior',
  full_name='scaii.common.SupportedBehavior',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backend', full_name='scaii.common.SupportedBehavior.backend', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agent', full_name='scaii.common.SupportedBehavior.agent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generic_module', full_name='scaii.common.SupportedBehavior.generic_module', index=2,
      number=5, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='which_module', full_name='scaii.common.SupportedBehavior.which_module',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=817,
  serialized_end=1007,
)


_BACKENDSUPPORTED = _descriptor.Descriptor(
  name='BackendSupported',
  full_name='scaii.common.BackendSupported',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialization_support', full_name='scaii.common.BackendSupported.serialization_support', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BACKENDSUPPORTED_SERIALIZATIONSUPPORT,
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 536870912), ],
  oneofs=[
  ],
  serialized_start=1010,
  serialized_end=1209,
)


_AGENTSUPPORTED = _descriptor.Descriptor(
  name='AgentSupported',
  full_name='scaii.common.AgentSupported',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 536870912), ],
  oneofs=[
  ],
  serialized_start=1211,
  serialized_end=1237,
)


_MODULESUPPORTED = _descriptor.Descriptor(
  name='ModuleSupported',
  full_name='scaii.common.ModuleSupported',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 536870912), ],
  oneofs=[
  ],
  serialized_start=1239,
  serialized_end=1266,
)


_ENVDESCRIPTION_REWARDTYPESENTRY = _descriptor.Descriptor(
  name='RewardTypesEntry',
  full_name='scaii.common.EnvDescription.RewardTypesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='scaii.common.EnvDescription.RewardTypesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='scaii.common.EnvDescription.RewardTypesEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1522,
  serialized_end=1572,
)

_ENVDESCRIPTION_POSSIBLEDISCRETEACTIONSENTRY = _descriptor.Descriptor(
  name='PossibleDiscreteActionsEntry',
  full_name='scaii.common.EnvDescription.PossibleDiscreteActionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='scaii.common.EnvDescription.PossibleDiscreteActionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='scaii.common.EnvDescription.PossibleDiscreteActionsEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1574,
  serialized_end=1636,
)

_ENVDESCRIPTION = _descriptor.Descriptor(
  name='EnvDescription',
  full_name='scaii.common.EnvDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reward_types', full_name='scaii.common.EnvDescription.reward_types', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='possible_discrete_actions', full_name='scaii.common.EnvDescription.possible_discrete_actions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_desc', full_name='scaii.common.EnvDescription.action_desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supported', full_name='scaii.common.EnvDescription.supported', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENVDESCRIPTION_REWARDTYPESENTRY, _ENVDESCRIPTION_POSSIBLEDISCRETEACTIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1269,
  serialized_end=1636,
)

_CFG.fields_by_name['core_cfg'].message_type = _CORECFG
_CFG.fields_by_name['backend_cfg'].message_type = _BACKENDCFG
_CFG.fields_by_name['agent_cfg'].message_type = _AGENTCFG
_CFG.fields_by_name['module_cfg'].message_type = _MODULECFG
_CFG.oneofs_by_name['which_module'].fields.append(
  _CFG.fields_by_name['core_cfg'])
_CFG.fields_by_name['core_cfg'].containing_oneof = _CFG.oneofs_by_name['which_module']
_CFG.oneofs_by_name['which_module'].fields.append(
  _CFG.fields_by_name['backend_cfg'])
_CFG.fields_by_name['backend_cfg'].containing_oneof = _CFG.oneofs_by_name['which_module']
_CFG.oneofs_by_name['which_module'].fields.append(
  _CFG.fields_by_name['agent_cfg'])
_CFG.fields_by_name['agent_cfg'].containing_oneof = _CFG.oneofs_by_name['which_module']
_CFG.oneofs_by_name['which_module'].fields.append(
  _CFG.fields_by_name['module_cfg'])
_CFG.fields_by_name['module_cfg'].containing_oneof = _CFG.oneofs_by_name['which_module']
_PLUGINTYPE.fields_by_name['sky_rts'].message_type = _SKYRTS
_PLUGINTYPE.fields_by_name['rpc'].message_type = _RPCCONFIG
_PLUGINTYPE.oneofs_by_name['plugin_type'].fields.append(
  _PLUGINTYPE.fields_by_name['sky_rts'])
_PLUGINTYPE.fields_by_name['sky_rts'].containing_oneof = _PLUGINTYPE.oneofs_by_name['plugin_type']
_PLUGINTYPE.oneofs_by_name['plugin_type'].fields.append(
  _PLUGINTYPE.fields_by_name['rpc'])
_PLUGINTYPE.fields_by_name['rpc'].containing_oneof = _PLUGINTYPE.oneofs_by_name['plugin_type']
_CORECFG.fields_by_name['plugin_type'].message_type = _PLUGINTYPE
_INITAS.fields_by_name['backend'].message_type = _BACKENDINIT
_INITAS.fields_by_name['module'].message_type = _MODULEINIT
_INITAS.oneofs_by_name['init_as'].fields.append(
  _INITAS.fields_by_name['backend'])
_INITAS.fields_by_name['backend'].containing_oneof = _INITAS.oneofs_by_name['init_as']
_INITAS.oneofs_by_name['init_as'].fields.append(
  _INITAS.fields_by_name['module'])
_INITAS.fields_by_name['module'].containing_oneof = _INITAS.oneofs_by_name['init_as']
_RPCCONFIG.fields_by_name['init_as'].message_type = _INITAS
_SUPPORTEDBEHAVIOR.fields_by_name['backend'].message_type = _BACKENDSUPPORTED
_SUPPORTEDBEHAVIOR.fields_by_name['agent'].message_type = _AGENTSUPPORTED
_SUPPORTEDBEHAVIOR.fields_by_name['generic_module'].message_type = _MODULESUPPORTED
_SUPPORTEDBEHAVIOR.oneofs_by_name['which_module'].fields.append(
  _SUPPORTEDBEHAVIOR.fields_by_name['backend'])
_SUPPORTEDBEHAVIOR.fields_by_name['backend'].containing_oneof = _SUPPORTEDBEHAVIOR.oneofs_by_name['which_module']
_SUPPORTEDBEHAVIOR.oneofs_by_name['which_module'].fields.append(
  _SUPPORTEDBEHAVIOR.fields_by_name['agent'])
_SUPPORTEDBEHAVIOR.fields_by_name['agent'].containing_oneof = _SUPPORTEDBEHAVIOR.oneofs_by_name['which_module']
_SUPPORTEDBEHAVIOR.oneofs_by_name['which_module'].fields.append(
  _SUPPORTEDBEHAVIOR.fields_by_name['generic_module'])
_SUPPORTEDBEHAVIOR.fields_by_name['generic_module'].containing_oneof = _SUPPORTEDBEHAVIOR.oneofs_by_name['which_module']
_BACKENDSUPPORTED.fields_by_name['serialization_support'].enum_type = _BACKENDSUPPORTED_SERIALIZATIONSUPPORT
_BACKENDSUPPORTED_SERIALIZATIONSUPPORT.containing_type = _BACKENDSUPPORTED
_ENVDESCRIPTION_REWARDTYPESENTRY.containing_type = _ENVDESCRIPTION
_ENVDESCRIPTION_POSSIBLEDISCRETEACTIONSENTRY.containing_type = _ENVDESCRIPTION
_ENVDESCRIPTION.fields_by_name['reward_types'].message_type = _ENVDESCRIPTION_REWARDTYPESENTRY
_ENVDESCRIPTION.fields_by_name['possible_discrete_actions'].message_type = _ENVDESCRIPTION_POSSIBLEDISCRETEACTIONSENTRY
_ENVDESCRIPTION.fields_by_name['supported'].message_type = _BACKENDSUPPORTED
DESCRIPTOR.message_types_by_name['Cfg'] = _CFG
DESCRIPTOR.message_types_by_name['PluginType'] = _PLUGINTYPE
DESCRIPTOR.message_types_by_name['CoreCfg'] = _CORECFG
DESCRIPTOR.message_types_by_name['InitAs'] = _INITAS
DESCRIPTOR.message_types_by_name['SkyRts'] = _SKYRTS
DESCRIPTOR.message_types_by_name['BackendInit'] = _BACKENDINIT
DESCRIPTOR.message_types_by_name['ModuleInit'] = _MODULEINIT
DESCRIPTOR.message_types_by_name['RpcConfig'] = _RPCCONFIG
DESCRIPTOR.message_types_by_name['BackendCfg'] = _BACKENDCFG
DESCRIPTOR.message_types_by_name['AgentCfg'] = _AGENTCFG
DESCRIPTOR.message_types_by_name['ModuleCfg'] = _MODULECFG
DESCRIPTOR.message_types_by_name['SupportedBehavior'] = _SUPPORTEDBEHAVIOR
DESCRIPTOR.message_types_by_name['BackendSupported'] = _BACKENDSUPPORTED
DESCRIPTOR.message_types_by_name['AgentSupported'] = _AGENTSUPPORTED
DESCRIPTOR.message_types_by_name['ModuleSupported'] = _MODULESUPPORTED
DESCRIPTOR.message_types_by_name['EnvDescription'] = _ENVDESCRIPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), dict(
  DESCRIPTOR = _CFG,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.Cfg)
  ))
_sym_db.RegisterMessage(Cfg)

PluginType = _reflection.GeneratedProtocolMessageType('PluginType', (_message.Message,), dict(
  DESCRIPTOR = _PLUGINTYPE,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.PluginType)
  ))
_sym_db.RegisterMessage(PluginType)

CoreCfg = _reflection.GeneratedProtocolMessageType('CoreCfg', (_message.Message,), dict(
  DESCRIPTOR = _CORECFG,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.CoreCfg)
  ))
_sym_db.RegisterMessage(CoreCfg)

InitAs = _reflection.GeneratedProtocolMessageType('InitAs', (_message.Message,), dict(
  DESCRIPTOR = _INITAS,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.InitAs)
  ))
_sym_db.RegisterMessage(InitAs)

SkyRts = _reflection.GeneratedProtocolMessageType('SkyRts', (_message.Message,), dict(
  DESCRIPTOR = _SKYRTS,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.SkyRts)
  ))
_sym_db.RegisterMessage(SkyRts)

BackendInit = _reflection.GeneratedProtocolMessageType('BackendInit', (_message.Message,), dict(
  DESCRIPTOR = _BACKENDINIT,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.BackendInit)
  ))
_sym_db.RegisterMessage(BackendInit)

ModuleInit = _reflection.GeneratedProtocolMessageType('ModuleInit', (_message.Message,), dict(
  DESCRIPTOR = _MODULEINIT,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.ModuleInit)
  ))
_sym_db.RegisterMessage(ModuleInit)

RpcConfig = _reflection.GeneratedProtocolMessageType('RpcConfig', (_message.Message,), dict(
  DESCRIPTOR = _RPCCONFIG,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.RpcConfig)
  ))
_sym_db.RegisterMessage(RpcConfig)

BackendCfg = _reflection.GeneratedProtocolMessageType('BackendCfg', (_message.Message,), dict(
  DESCRIPTOR = _BACKENDCFG,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.BackendCfg)
  ))
_sym_db.RegisterMessage(BackendCfg)

AgentCfg = _reflection.GeneratedProtocolMessageType('AgentCfg', (_message.Message,), dict(
  DESCRIPTOR = _AGENTCFG,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.AgentCfg)
  ))
_sym_db.RegisterMessage(AgentCfg)

ModuleCfg = _reflection.GeneratedProtocolMessageType('ModuleCfg', (_message.Message,), dict(
  DESCRIPTOR = _MODULECFG,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.ModuleCfg)
  ))
_sym_db.RegisterMessage(ModuleCfg)

SupportedBehavior = _reflection.GeneratedProtocolMessageType('SupportedBehavior', (_message.Message,), dict(
  DESCRIPTOR = _SUPPORTEDBEHAVIOR,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.SupportedBehavior)
  ))
_sym_db.RegisterMessage(SupportedBehavior)

BackendSupported = _reflection.GeneratedProtocolMessageType('BackendSupported', (_message.Message,), dict(
  DESCRIPTOR = _BACKENDSUPPORTED,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.BackendSupported)
  ))
_sym_db.RegisterMessage(BackendSupported)

AgentSupported = _reflection.GeneratedProtocolMessageType('AgentSupported', (_message.Message,), dict(
  DESCRIPTOR = _AGENTSUPPORTED,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.AgentSupported)
  ))
_sym_db.RegisterMessage(AgentSupported)

ModuleSupported = _reflection.GeneratedProtocolMessageType('ModuleSupported', (_message.Message,), dict(
  DESCRIPTOR = _MODULESUPPORTED,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.ModuleSupported)
  ))
_sym_db.RegisterMessage(ModuleSupported)

EnvDescription = _reflection.GeneratedProtocolMessageType('EnvDescription', (_message.Message,), dict(

  RewardTypesEntry = _reflection.GeneratedProtocolMessageType('RewardTypesEntry', (_message.Message,), dict(
    DESCRIPTOR = _ENVDESCRIPTION_REWARDTYPESENTRY,
    __module__ = 'cfg_pb2'
    # @@protoc_insertion_point(class_scope:scaii.common.EnvDescription.RewardTypesEntry)
    ))
  ,

  PossibleDiscreteActionsEntry = _reflection.GeneratedProtocolMessageType('PossibleDiscreteActionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ENVDESCRIPTION_POSSIBLEDISCRETEACTIONSENTRY,
    __module__ = 'cfg_pb2'
    # @@protoc_insertion_point(class_scope:scaii.common.EnvDescription.PossibleDiscreteActionsEntry)
    ))
  ,
  DESCRIPTOR = _ENVDESCRIPTION,
  __module__ = 'cfg_pb2'
  # @@protoc_insertion_point(class_scope:scaii.common.EnvDescription)
  ))
_sym_db.RegisterMessage(EnvDescription)
_sym_db.RegisterMessage(EnvDescription.RewardTypesEntry)
_sym_db.RegisterMessage(EnvDescription.PossibleDiscreteActionsEntry)


_ENVDESCRIPTION_REWARDTYPESENTRY.has_options = True
_ENVDESCRIPTION_REWARDTYPESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ENVDESCRIPTION_POSSIBLEDISCRETEACTIONSENTRY.has_options = True
_ENVDESCRIPTION_POSSIBLEDISCRETEACTIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
