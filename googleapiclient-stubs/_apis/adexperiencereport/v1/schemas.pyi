import typing

import typing_extensions
@typing.type_check_only
class PlatformSummary(typing_extensions.TypedDict, total=False):
    betterAdsStatus: typing_extensions.Literal[
        "UNKNOWN", "PASSING", "WARNING", "FAILING"
    ]
    enforcementTime: str
    filterStatus: typing_extensions.Literal["UNKNOWN", "ON", "OFF", "PAUSED", "PENDING"]
    lastChangeTime: str
    region: typing.List[str]
    reportUrl: str
    underReview: bool

@typing.type_check_only
class SiteSummaryResponse(typing_extensions.TypedDict, total=False):
    desktopSummary: PlatformSummary
    mobileSummary: PlatformSummary
    reviewedSite: str

@typing.type_check_only
class ViolatingSitesResponse(typing_extensions.TypedDict, total=False):
    violatingSites: typing.List[SiteSummaryResponse]
