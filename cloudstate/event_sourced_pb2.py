# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cloudstate/event_sourced.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cloudstate import entity_pb2 as cloudstate_dot_entity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="cloudstate/event_sourced.proto",
    package="cloudstate.eventsourced",
    syntax="proto3",
    serialized_options=b"\n\026io.cloudstate.protocolZ\023cloudstate/protocol",
    serialized_pb=b'\n\x1e\x63loudstate/event_sourced.proto\x12\x17\x63loudstate.eventsourced\x1a\x19google/protobuf/any.proto\x1a\x17\x63loudstate/entity.proto"|\n\x10\x45ventSourcedInit\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x11\n\tentity_id\x18\x02 \x01(\t\x12?\n\x08snapshot\x18\x03 \x01(\x0b\x32-.cloudstate.eventsourced.EventSourcedSnapshot"Y\n\x14\x45ventSourcedSnapshot\x12\x19\n\x11snapshot_sequence\x18\x01 \x01(\x03\x12&\n\x08snapshot\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any"L\n\x11\x45ventSourcedEvent\x12\x10\n\x08sequence\x18\x01 \x01(\x03\x12%\n\x07payload\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any"\xd4\x01\n\x11\x45ventSourcedReply\x12\x12\n\ncommand_id\x18\x01 \x01(\x03\x12/\n\rclient_action\x18\x02 \x01(\x0b\x32\x18.cloudstate.ClientAction\x12,\n\x0cside_effects\x18\x03 \x03(\x0b\x32\x16.cloudstate.SideEffect\x12$\n\x06\x65vents\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any\x12&\n\x08snapshot\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any"\xc1\x01\n\x14\x45ventSourcedStreamIn\x12\x39\n\x04init\x18\x01 \x01(\x0b\x32).cloudstate.eventsourced.EventSourcedInitH\x00\x12;\n\x05\x65vent\x18\x02 \x01(\x0b\x32*.cloudstate.eventsourced.EventSourcedEventH\x00\x12&\n\x07\x63ommand\x18\x03 \x01(\x0b\x32\x13.cloudstate.CommandH\x00\x42\t\n\x07message"\x87\x01\n\x15\x45ventSourcedStreamOut\x12;\n\x05reply\x18\x01 \x01(\x0b\x32*.cloudstate.eventsourced.EventSourcedReplyH\x00\x12&\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x13.cloudstate.FailureH\x00\x42\t\n\x07message2}\n\x0c\x45ventSourced\x12m\n\x06handle\x12-.cloudstate.eventsourced.EventSourcedStreamIn\x1a..cloudstate.eventsourced.EventSourcedStreamOut"\x00(\x01\x30\x01\x42-\n\x16io.cloudstate.protocolZ\x13\x63loudstate/protocolb\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
        cloudstate_dot_entity__pb2.DESCRIPTOR,
    ],
)


_EVENTSOURCEDINIT = _descriptor.Descriptor(
    name="EventSourcedInit",
    full_name="cloudstate.eventsourced.EventSourcedInit",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="service_name",
            full_name="cloudstate.eventsourced.EventSourcedInit.service_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="entity_id",
            full_name="cloudstate.eventsourced.EventSourcedInit.entity_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="snapshot",
            full_name="cloudstate.eventsourced.EventSourcedInit.snapshot",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=111,
    serialized_end=235,
)


_EVENTSOURCEDSNAPSHOT = _descriptor.Descriptor(
    name="EventSourcedSnapshot",
    full_name="cloudstate.eventsourced.EventSourcedSnapshot",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="snapshot_sequence",
            full_name="cloudstate.eventsourced.EventSourcedSnapshot.snapshot_sequence",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="snapshot",
            full_name="cloudstate.eventsourced.EventSourcedSnapshot.snapshot",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=237,
    serialized_end=326,
)


_EVENTSOURCEDEVENT = _descriptor.Descriptor(
    name="EventSourcedEvent",
    full_name="cloudstate.eventsourced.EventSourcedEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="sequence",
            full_name="cloudstate.eventsourced.EventSourcedEvent.sequence",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="cloudstate.eventsourced.EventSourcedEvent.payload",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=328,
    serialized_end=404,
)


_EVENTSOURCEDREPLY = _descriptor.Descriptor(
    name="EventSourcedReply",
    full_name="cloudstate.eventsourced.EventSourcedReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="command_id",
            full_name="cloudstate.eventsourced.EventSourcedReply.command_id",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="client_action",
            full_name="cloudstate.eventsourced.EventSourcedReply.client_action",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="side_effects",
            full_name="cloudstate.eventsourced.EventSourcedReply.side_effects",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="events",
            full_name="cloudstate.eventsourced.EventSourcedReply.events",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="snapshot",
            full_name="cloudstate.eventsourced.EventSourcedReply.snapshot",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=407,
    serialized_end=619,
)


_EVENTSOURCEDSTREAMIN = _descriptor.Descriptor(
    name="EventSourcedStreamIn",
    full_name="cloudstate.eventsourced.EventSourcedStreamIn",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="init",
            full_name="cloudstate.eventsourced.EventSourcedStreamIn.init",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="event",
            full_name="cloudstate.eventsourced.EventSourcedStreamIn.event",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="command",
            full_name="cloudstate.eventsourced.EventSourcedStreamIn.command",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="message",
            full_name="cloudstate.eventsourced.EventSourcedStreamIn.message",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=622,
    serialized_end=815,
)


_EVENTSOURCEDSTREAMOUT = _descriptor.Descriptor(
    name="EventSourcedStreamOut",
    full_name="cloudstate.eventsourced.EventSourcedStreamOut",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="reply",
            full_name="cloudstate.eventsourced.EventSourcedStreamOut.reply",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="failure",
            full_name="cloudstate.eventsourced.EventSourcedStreamOut.failure",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="message",
            full_name="cloudstate.eventsourced.EventSourcedStreamOut.message",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=818,
    serialized_end=953,
)

_EVENTSOURCEDINIT.fields_by_name["snapshot"].message_type = _EVENTSOURCEDSNAPSHOT
_EVENTSOURCEDSNAPSHOT.fields_by_name[
    "snapshot"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EVENTSOURCEDEVENT.fields_by_name[
    "payload"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EVENTSOURCEDREPLY.fields_by_name[
    "client_action"
].message_type = cloudstate_dot_entity__pb2._CLIENTACTION
_EVENTSOURCEDREPLY.fields_by_name[
    "side_effects"
].message_type = cloudstate_dot_entity__pb2._SIDEEFFECT
_EVENTSOURCEDREPLY.fields_by_name[
    "events"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EVENTSOURCEDREPLY.fields_by_name[
    "snapshot"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EVENTSOURCEDSTREAMIN.fields_by_name["init"].message_type = _EVENTSOURCEDINIT
_EVENTSOURCEDSTREAMIN.fields_by_name["event"].message_type = _EVENTSOURCEDEVENT
_EVENTSOURCEDSTREAMIN.fields_by_name[
    "command"
].message_type = cloudstate_dot_entity__pb2._COMMAND
_EVENTSOURCEDSTREAMIN.oneofs_by_name["message"].fields.append(
    _EVENTSOURCEDSTREAMIN.fields_by_name["init"]
)
_EVENTSOURCEDSTREAMIN.fields_by_name[
    "init"
].containing_oneof = _EVENTSOURCEDSTREAMIN.oneofs_by_name["message"]
_EVENTSOURCEDSTREAMIN.oneofs_by_name["message"].fields.append(
    _EVENTSOURCEDSTREAMIN.fields_by_name["event"]
)
_EVENTSOURCEDSTREAMIN.fields_by_name[
    "event"
].containing_oneof = _EVENTSOURCEDSTREAMIN.oneofs_by_name["message"]
_EVENTSOURCEDSTREAMIN.oneofs_by_name["message"].fields.append(
    _EVENTSOURCEDSTREAMIN.fields_by_name["command"]
)
_EVENTSOURCEDSTREAMIN.fields_by_name[
    "command"
].containing_oneof = _EVENTSOURCEDSTREAMIN.oneofs_by_name["message"]
_EVENTSOURCEDSTREAMOUT.fields_by_name["reply"].message_type = _EVENTSOURCEDREPLY
_EVENTSOURCEDSTREAMOUT.fields_by_name[
    "failure"
].message_type = cloudstate_dot_entity__pb2._FAILURE
_EVENTSOURCEDSTREAMOUT.oneofs_by_name["message"].fields.append(
    _EVENTSOURCEDSTREAMOUT.fields_by_name["reply"]
)
_EVENTSOURCEDSTREAMOUT.fields_by_name[
    "reply"
].containing_oneof = _EVENTSOURCEDSTREAMOUT.oneofs_by_name["message"]
_EVENTSOURCEDSTREAMOUT.oneofs_by_name["message"].fields.append(
    _EVENTSOURCEDSTREAMOUT.fields_by_name["failure"]
)
_EVENTSOURCEDSTREAMOUT.fields_by_name[
    "failure"
].containing_oneof = _EVENTSOURCEDSTREAMOUT.oneofs_by_name["message"]
DESCRIPTOR.message_types_by_name["EventSourcedInit"] = _EVENTSOURCEDINIT
DESCRIPTOR.message_types_by_name["EventSourcedSnapshot"] = _EVENTSOURCEDSNAPSHOT
DESCRIPTOR.message_types_by_name["EventSourcedEvent"] = _EVENTSOURCEDEVENT
DESCRIPTOR.message_types_by_name["EventSourcedReply"] = _EVENTSOURCEDREPLY
DESCRIPTOR.message_types_by_name["EventSourcedStreamIn"] = _EVENTSOURCEDSTREAMIN
DESCRIPTOR.message_types_by_name["EventSourcedStreamOut"] = _EVENTSOURCEDSTREAMOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventSourcedInit = _reflection.GeneratedProtocolMessageType(
    "EventSourcedInit",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTSOURCEDINIT,
        "__module__": "cloudstate.event_sourced_pb2"
        # @@protoc_insertion_point(class_scope:cloudstate.eventsourced.EventSourcedInit)
    },
)
_sym_db.RegisterMessage(EventSourcedInit)

EventSourcedSnapshot = _reflection.GeneratedProtocolMessageType(
    "EventSourcedSnapshot",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTSOURCEDSNAPSHOT,
        "__module__": "cloudstate.event_sourced_pb2"
        # @@protoc_insertion_point(class_scope:cloudstate.eventsourced.EventSourcedSnapshot)
    },
)
_sym_db.RegisterMessage(EventSourcedSnapshot)

EventSourcedEvent = _reflection.GeneratedProtocolMessageType(
    "EventSourcedEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTSOURCEDEVENT,
        "__module__": "cloudstate.event_sourced_pb2"
        # @@protoc_insertion_point(class_scope:cloudstate.eventsourced.EventSourcedEvent)
    },
)
_sym_db.RegisterMessage(EventSourcedEvent)

EventSourcedReply = _reflection.GeneratedProtocolMessageType(
    "EventSourcedReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTSOURCEDREPLY,
        "__module__": "cloudstate.event_sourced_pb2"
        # @@protoc_insertion_point(class_scope:cloudstate.eventsourced.EventSourcedReply)
    },
)
_sym_db.RegisterMessage(EventSourcedReply)

EventSourcedStreamIn = _reflection.GeneratedProtocolMessageType(
    "EventSourcedStreamIn",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTSOURCEDSTREAMIN,
        "__module__": "cloudstate.event_sourced_pb2"
        # @@protoc_insertion_point(class_scope:cloudstate.eventsourced.EventSourcedStreamIn)
    },
)
_sym_db.RegisterMessage(EventSourcedStreamIn)

EventSourcedStreamOut = _reflection.GeneratedProtocolMessageType(
    "EventSourcedStreamOut",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTSOURCEDSTREAMOUT,
        "__module__": "cloudstate.event_sourced_pb2"
        # @@protoc_insertion_point(class_scope:cloudstate.eventsourced.EventSourcedStreamOut)
    },
)
_sym_db.RegisterMessage(EventSourcedStreamOut)


DESCRIPTOR._options = None

_EVENTSOURCED = _descriptor.ServiceDescriptor(
    name="EventSourced",
    full_name="cloudstate.eventsourced.EventSourced",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=955,
    serialized_end=1080,
    methods=[
        _descriptor.MethodDescriptor(
            name="handle",
            full_name="cloudstate.eventsourced.EventSourced.handle",
            index=0,
            containing_service=None,
            input_type=_EVENTSOURCEDSTREAMIN,
            output_type=_EVENTSOURCEDSTREAMOUT,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_EVENTSOURCED)

DESCRIPTOR.services_by_name["EventSourced"] = _EVENTSOURCED

# @@protoc_insertion_point(module_scope)
