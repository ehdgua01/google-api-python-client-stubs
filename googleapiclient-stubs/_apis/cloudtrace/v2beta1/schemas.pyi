import typing

import typing_extensions
@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListTraceSinksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sinks: typing.List[TraceSink]

@typing.type_check_only
class OutputConfig(typing_extensions.TypedDict, total=False):
    destination: str

@typing.type_check_only
class TraceSink(typing_extensions.TypedDict, total=False):
    name: str
    outputConfig: OutputConfig
    writerIdentity: str
