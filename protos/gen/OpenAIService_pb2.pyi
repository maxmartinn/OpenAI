from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BasicChatParams(_message.Message):
    __slots__ = ("prompt", "system_message")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    system_message: str
    def __init__(self, prompt: _Optional[str] = ..., system_message: _Optional[str] = ...) -> None: ...

class BasicChatResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...
