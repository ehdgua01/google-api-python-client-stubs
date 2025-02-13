import typing

import typing_extensions
@typing.type_check_only
class Acl(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[AclRule]
    kind: str
    nextPageToken: str
    nextSyncToken: str

@typing.type_check_only
class AclRule(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    role: str
    scope: typing.Dict[str, typing.Any]

@typing.type_check_only
class Calendar(typing_extensions.TypedDict, total=False):
    conferenceProperties: ConferenceProperties
    description: str
    etag: str
    id: str
    kind: str
    location: str
    summary: str
    timeZone: str

@typing.type_check_only
class CalendarList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[CalendarListEntry]
    kind: str
    nextPageToken: str
    nextSyncToken: str

@typing.type_check_only
class CalendarListEntry(typing_extensions.TypedDict, total=False):
    accessRole: str
    backgroundColor: str
    colorId: str
    conferenceProperties: ConferenceProperties
    defaultReminders: typing.List[EventReminder]
    deleted: bool
    description: str
    etag: str
    foregroundColor: str
    hidden: bool
    id: str
    kind: str
    location: str
    notificationSettings: typing.Dict[str, typing.Any]
    primary: bool
    selected: bool
    summary: str
    summaryOverride: str
    timeZone: str

@typing.type_check_only
class CalendarNotification(typing_extensions.TypedDict, total=False):
    method: str
    type: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: typing.Dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class ColorDefinition(typing_extensions.TypedDict, total=False):
    background: str
    foreground: str

@typing.type_check_only
class Colors(typing_extensions.TypedDict, total=False):
    calendar: typing.Dict[str, typing.Any]
    event: typing.Dict[str, typing.Any]
    kind: str
    updated: str

@typing.type_check_only
class ConferenceData(typing_extensions.TypedDict, total=False):
    conferenceId: str
    conferenceSolution: ConferenceSolution
    createRequest: CreateConferenceRequest
    entryPoints: typing.List[EntryPoint]
    notes: str
    parameters: ConferenceParameters
    signature: str

@typing.type_check_only
class ConferenceParameters(typing_extensions.TypedDict, total=False):
    addOnParameters: ConferenceParametersAddOnParameters

@typing.type_check_only
class ConferenceParametersAddOnParameters(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]

@typing.type_check_only
class ConferenceProperties(typing_extensions.TypedDict, total=False):
    allowedConferenceSolutionTypes: typing.List[str]

@typing.type_check_only
class ConferenceRequestStatus(typing_extensions.TypedDict, total=False):
    statusCode: str

@typing.type_check_only
class ConferenceSolution(typing_extensions.TypedDict, total=False):
    iconUri: str
    key: ConferenceSolutionKey
    name: str

@typing.type_check_only
class ConferenceSolutionKey(typing_extensions.TypedDict, total=False):
    type: str

@typing.type_check_only
class CreateConferenceRequest(typing_extensions.TypedDict, total=False):
    conferenceSolutionKey: ConferenceSolutionKey
    requestId: str
    status: ConferenceRequestStatus

@typing.type_check_only
class EntryPoint(typing_extensions.TypedDict, total=False):
    accessCode: str
    entryPointFeatures: typing.List[str]
    entryPointType: str
    label: str
    meetingCode: str
    passcode: str
    password: str
    pin: str
    regionCode: str
    uri: str

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    domain: str
    reason: str

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    anyoneCanAddSelf: bool
    attachments: typing.List[EventAttachment]
    attendees: typing.List[EventAttendee]
    attendeesOmitted: bool
    colorId: str
    conferenceData: ConferenceData
    created: str
    creator: typing.Dict[str, typing.Any]
    description: str
    end: EventDateTime
    endTimeUnspecified: bool
    etag: str
    eventType: str
    extendedProperties: typing.Dict[str, typing.Any]
    gadget: typing.Dict[str, typing.Any]
    guestsCanInviteOthers: bool
    guestsCanModify: bool
    guestsCanSeeOtherGuests: bool
    hangoutLink: str
    htmlLink: str
    iCalUID: str
    id: str
    kind: str
    location: str
    locked: bool
    organizer: typing.Dict[str, typing.Any]
    originalStartTime: EventDateTime
    privateCopy: bool
    recurrence: typing.List[str]
    recurringEventId: str
    reminders: typing.Dict[str, typing.Any]
    sequence: int
    source: typing.Dict[str, typing.Any]
    start: EventDateTime
    status: str
    summary: str
    transparency: str
    updated: str
    visibility: str

@typing.type_check_only
class EventAttachment(typing_extensions.TypedDict, total=False):
    fileId: str
    fileUrl: str
    iconLink: str
    mimeType: str
    title: str

@typing.type_check_only
class EventAttendee(typing_extensions.TypedDict, total=False):
    additionalGuests: int
    comment: str
    displayName: str
    email: str
    id: str
    optional: bool
    organizer: bool
    resource: bool
    responseStatus: str
    self: bool

@typing.type_check_only
class EventDateTime(typing_extensions.TypedDict, total=False):
    date: str
    dateTime: str
    timeZone: str

@typing.type_check_only
class EventReminder(typing_extensions.TypedDict, total=False):
    method: str
    minutes: int

@typing.type_check_only
class Events(typing_extensions.TypedDict, total=False):
    accessRole: str
    defaultReminders: typing.List[EventReminder]
    description: str
    etag: str
    items: typing.List[Event]
    kind: str
    nextPageToken: str
    nextSyncToken: str
    summary: str
    timeZone: str
    updated: str

@typing.type_check_only
class FreeBusyCalendar(typing_extensions.TypedDict, total=False):
    busy: typing.List[TimePeriod]
    errors: typing.List[Error]

@typing.type_check_only
class FreeBusyGroup(typing_extensions.TypedDict, total=False):
    calendars: typing.List[str]
    errors: typing.List[Error]

@typing.type_check_only
class FreeBusyRequest(typing_extensions.TypedDict, total=False):
    calendarExpansionMax: int
    groupExpansionMax: int
    items: typing.List[FreeBusyRequestItem]
    timeMax: str
    timeMin: str
    timeZone: str

@typing.type_check_only
class FreeBusyRequestItem(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class FreeBusyResponse(typing_extensions.TypedDict, total=False):
    calendars: typing.Dict[str, typing.Any]
    groups: typing.Dict[str, typing.Any]
    kind: str
    timeMax: str
    timeMin: str

@typing.type_check_only
class Setting(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    value: str

@typing.type_check_only
class Settings(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Setting]
    kind: str
    nextPageToken: str
    nextSyncToken: str

@typing.type_check_only
class TimePeriod(typing_extensions.TypedDict, total=False):
    end: str
    start: str
