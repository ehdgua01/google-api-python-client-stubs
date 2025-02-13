import typing

import typing_extensions
@typing.type_check_only
class AggregateBucket(typing_extensions.TypedDict, total=False):
    activity: int
    dataset: typing.List[Dataset]
    endTimeMillis: str
    session: Session
    startTimeMillis: str
    type: typing_extensions.Literal[
        "unknown", "time", "session", "activityType", "activitySegment"
    ]

@typing.type_check_only
class AggregateBy(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    dataTypeName: str

@typing.type_check_only
class AggregateRequest(typing_extensions.TypedDict, total=False):
    aggregateBy: typing.List[AggregateBy]
    bucketByActivitySegment: BucketByActivity
    bucketByActivityType: BucketByActivity
    bucketBySession: BucketBySession
    bucketByTime: BucketByTime
    endTimeMillis: str
    filteredDataQualityStandard: typing.List[str]
    startTimeMillis: str

@typing.type_check_only
class AggregateResponse(typing_extensions.TypedDict, total=False):
    bucket: typing.List[AggregateBucket]

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    detailsUrl: str
    name: str
    packageName: str
    version: str

@typing.type_check_only
class BucketByActivity(typing_extensions.TypedDict, total=False):
    activityDataSourceId: str
    minDurationMillis: str

@typing.type_check_only
class BucketBySession(typing_extensions.TypedDict, total=False):
    minDurationMillis: str

@typing.type_check_only
class BucketByTime(typing_extensions.TypedDict, total=False):
    durationMillis: str
    period: BucketByTimePeriod

@typing.type_check_only
class BucketByTimePeriod(typing_extensions.TypedDict, total=False):
    timeZoneId: str
    type: typing_extensions.Literal["day", "week", "month"]
    value: int

@typing.type_check_only
class DataPoint(typing_extensions.TypedDict, total=False):
    computationTimeMillis: str
    dataTypeName: str
    endTimeNanos: str
    modifiedTimeMillis: str
    originDataSourceId: str
    rawTimestampNanos: str
    startTimeNanos: str
    value: typing.List[Value]

@typing.type_check_only
class DataSource(typing_extensions.TypedDict, total=False):
    application: Application
    dataQualityStandard: typing.List[str]
    dataStreamId: str
    dataStreamName: str
    dataType: DataType
    device: Device
    name: str
    type: typing_extensions.Literal["raw", "derived"]

@typing.type_check_only
class DataType(typing_extensions.TypedDict, total=False):
    field: typing.List[DataTypeField]
    name: str

@typing.type_check_only
class DataTypeField(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal[
        "integer", "floatPoint", "string", "map", "integerList", "floatList", "blob"
    ]
    name: str
    optional: bool

@typing.type_check_only
class Dataset(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    maxEndTimeNs: str
    minStartTimeNs: str
    nextPageToken: str
    point: typing.List[DataPoint]

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    manufacturer: str
    model: str
    type: typing_extensions.Literal[
        "unknown",
        "phone",
        "tablet",
        "watch",
        "chestStrap",
        "scale",
        "headMounted",
        "smartDisplay",
    ]
    uid: str
    version: str

@typing.type_check_only
class ListDataPointChangesResponse(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    deletedDataPoint: typing.List[DataPoint]
    insertedDataPoint: typing.List[DataPoint]
    nextPageToken: str

@typing.type_check_only
class ListDataSourcesResponse(typing_extensions.TypedDict, total=False):
    dataSource: typing.List[DataSource]

@typing.type_check_only
class ListSessionsResponse(typing_extensions.TypedDict, total=False):
    deletedSession: typing.List[Session]
    hasMoreData: bool
    nextPageToken: str
    session: typing.List[Session]

@typing.type_check_only
class MapValue(typing_extensions.TypedDict, total=False):
    fpVal: float

@typing.type_check_only
class Session(typing_extensions.TypedDict, total=False):
    activeTimeMillis: str
    activityType: int
    application: Application
    description: str
    endTimeMillis: str
    id: str
    modifiedTimeMillis: str
    name: str
    startTimeMillis: str

@typing.type_check_only
class Value(typing_extensions.TypedDict, total=False):
    fpVal: float
    intVal: int
    mapVal: typing.List[ValueMapValEntry]
    stringVal: str

@typing.type_check_only
class ValueMapValEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: MapValue
