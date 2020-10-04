import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class BooksResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BookshelvesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class VolumesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                userId: str,
                shelf: str,
                maxResults: int = ...,
                showPreorders: bool = ...,
                source: str = ...,
                startIndex: int = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
        def get(
            self, *, userId: str, shelf: str, source: str = ..., **kwargs: typing.Any
        ) -> BookshelfHttpRequest: ...
        def list(
            self, *, userId: str, source: str = ..., **kwargs: typing.Any
        ) -> BookshelvesHttpRequest: ...
        def volumes(self) -> VolumesResource: ...
    @typing.type_check_only
    class CloudloadingResource(googleapiclient.discovery.Resource):
        def addBook(
            self,
            *,
            drive_document_id: str = ...,
            mime_type: str = ...,
            name: str = ...,
            upload_client_token: str = ...,
            **kwargs: typing.Any
        ) -> BooksCloudloadingResourceHttpRequest: ...
        def deleteBook(
            self, *, volumeId: str = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def updateBook(
            self, *, body: BooksCloudloadingResource = ..., **kwargs: typing.Any
        ) -> BooksCloudloadingResourceHttpRequest: ...
    @typing.type_check_only
    class DictionaryResource(googleapiclient.discovery.Resource):
        def listOfflineMetadata(
            self, *, cpksver: str = ..., **kwargs: typing.Any
        ) -> MetadataHttpRequest: ...
    @typing.type_check_only
    class FamilysharingResource(googleapiclient.discovery.Resource):
        def getFamilyInfo(
            self, *, source: str = ..., **kwargs: typing.Any
        ) -> FamilyInfoHttpRequest: ...
        def share(
            self,
            *,
            docId: str = ...,
            source: str = ...,
            volumeId: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def unshare(
            self,
            *,
            docId: str = ...,
            source: str = ...,
            volumeId: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    @typing.type_check_only
    class LayersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnnotationDataResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                volumeId: str,
                layerId: str,
                annotationDataId: str,
                allowWebDefinitions: bool = ...,
                contentVersion: str = ...,
                h: int = ...,
                locale: str = ...,
                scale: int = ...,
                source: str = ...,
                w: int = ...,
                **kwargs: typing.Any
            ) -> DictionaryAnnotationdataHttpRequest: ...
            def list(
                self,
                *,
                volumeId: str,
                layerId: str,
                annotationDataId: typing.Union[str, typing.List[str]] = ...,
                contentVersion: str = ...,
                h: int = ...,
                locale: str = ...,
                maxResults: int = ...,
                pageToken: str = ...,
                scale: int = ...,
                source: str = ...,
                updatedMax: str = ...,
                updatedMin: str = ...,
                w: int = ...,
                **kwargs: typing.Any
            ) -> AnnotationsdataHttpRequest: ...
        @typing.type_check_only
        class VolumeAnnotationsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                volumeId: str,
                layerId: str,
                annotationId: str,
                locale: str = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> VolumeannotationHttpRequest: ...
            def list(
                self,
                *,
                volumeId: str,
                layerId: str,
                contentVersion: str = ...,
                endOffset: str = ...,
                endPosition: str = ...,
                locale: str = ...,
                maxResults: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                source: str = ...,
                startOffset: str = ...,
                startPosition: str = ...,
                updatedMax: str = ...,
                updatedMin: str = ...,
                volumeAnnotationsVersion: str = ...,
                **kwargs: typing.Any
            ) -> VolumeannotationsHttpRequest: ...
        def get(
            self,
            *,
            volumeId: str,
            summaryId: str,
            contentVersion: str = ...,
            source: str = ...,
            **kwargs: typing.Any
        ) -> LayersummaryHttpRequest: ...
        def list(
            self,
            *,
            volumeId: str,
            contentVersion: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            source: str = ...,
            **kwargs: typing.Any
        ) -> LayersummariesHttpRequest: ...
        def annotationData(self) -> AnnotationDataResource: ...
        def volumeAnnotations(self) -> VolumeAnnotationsResource: ...
    @typing.type_check_only
    class MyconfigResource(googleapiclient.discovery.Resource):
        def getUserSettings(
            self, *, country: str = ..., **kwargs: typing.Any
        ) -> UsersettingsHttpRequest: ...
        def releaseDownloadAccess(
            self,
            *,
            cpksver: str = ...,
            locale: str = ...,
            source: str = ...,
            volumeIds: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> DownloadAccessesHttpRequest: ...
        def requestAccess(
            self,
            *,
            cpksver: str = ...,
            licenseTypes: typing_extensions.Literal[
                "LICENSE_TYPES_UNDEFINED", "BOTH", "CONCURRENT", "DOWNLOAD"
            ] = ...,
            locale: str = ...,
            nonce: str = ...,
            source: str = ...,
            volumeId: str = ...,
            **kwargs: typing.Any
        ) -> RequestAccessDataHttpRequest: ...
        def syncVolumeLicenses(
            self,
            *,
            cpksver: str = ...,
            features: typing.Union[
                typing_extensions.Literal["FEATURES_UNDEFINED", "RENTALS"],
                typing.List[typing_extensions.Literal["FEATURES_UNDEFINED", "RENTALS"]],
            ] = ...,
            includeNonComicsSeries: bool = ...,
            locale: str = ...,
            nonce: str = ...,
            showPreorders: bool = ...,
            source: str = ...,
            volumeIds: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> VolumesHttpRequest: ...
        def updateUserSettings(
            self, *, body: Usersettings = ..., **kwargs: typing.Any
        ) -> UsersettingsHttpRequest: ...
    @typing.type_check_only
    class MylibraryResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnnotationsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, annotationId: str, source: str = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def insert(
                self,
                *,
                body: Annotation = ...,
                annotationId: str = ...,
                country: str = ...,
                showOnlySummaryInResponse: bool = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> AnnotationHttpRequest: ...
            def list(
                self,
                *,
                contentVersion: str = ...,
                layerId: str = ...,
                layerIds: typing.Union[str, typing.List[str]] = ...,
                maxResults: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                source: str = ...,
                updatedMax: str = ...,
                updatedMin: str = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> AnnotationsHttpRequest: ...
            def summary(
                self,
                *,
                layerIds: typing.Union[str, typing.List[str]] = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> AnnotationsSummaryHttpRequest: ...
            def update(
                self,
                *,
                annotationId: str,
                body: Annotation = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> AnnotationHttpRequest: ...
        @typing.type_check_only
        class BookshelvesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class VolumesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    shelf: str,
                    country: str = ...,
                    maxResults: int = ...,
                    projection: typing_extensions.Literal[
                        "PROJECTION_UNDEFINED", "FULL", "LITE"
                    ] = ...,
                    q: str = ...,
                    showPreorders: bool = ...,
                    source: str = ...,
                    startIndex: int = ...,
                    **kwargs: typing.Any
                ) -> VolumesHttpRequest: ...
            def addVolume(
                self,
                *,
                shelf: str,
                reason: typing_extensions.Literal[
                    "REASON_UNDEFINED", "IOS_PREX", "IOS_SEARCH", "ONBOARDING"
                ] = ...,
                source: str = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def clearVolumes(
                self, *, shelf: str, source: str = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, shelf: str, source: str = ..., **kwargs: typing.Any
            ) -> BookshelfHttpRequest: ...
            def list(
                self, *, source: str = ..., **kwargs: typing.Any
            ) -> BookshelvesHttpRequest: ...
            def moveVolume(
                self,
                *,
                shelf: str,
                source: str = ...,
                volumeId: str = ...,
                volumePosition: int = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def removeVolume(
                self,
                *,
                shelf: str,
                reason: typing_extensions.Literal[
                    "REASON_UNDEFINED", "ONBOARDING"
                ] = ...,
                source: str = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def volumes(self) -> VolumesResource: ...
        @typing.type_check_only
        class ReadingpositionsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                volumeId: str,
                contentVersion: str = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> ReadingPositionHttpRequest: ...
            def setPosition(
                self,
                *,
                volumeId: str,
                action: typing_extensions.Literal[
                    "ACTION_UNDEFINED",
                    "bookmark",
                    "chapter",
                    "next-page",
                    "prev-page",
                    "scroll",
                    "search",
                ] = ...,
                contentVersion: str = ...,
                deviceCookie: str = ...,
                position: str = ...,
                source: str = ...,
                timestamp: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        def annotations(self) -> AnnotationsResource: ...
        def bookshelves(self) -> BookshelvesResource: ...
        def readingpositions(self) -> ReadingpositionsResource: ...
    @typing.type_check_only
    class NotificationResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            locale: str = ...,
            notification_id: str = ...,
            source: str = ...,
            **kwargs: typing.Any
        ) -> NotificationHttpRequest: ...
    @typing.type_check_only
    class OnboardingResource(googleapiclient.discovery.Resource):
        def listCategories(
            self, *, locale: str = ..., **kwargs: typing.Any
        ) -> CategoryHttpRequest: ...
        def listCategoryVolumes(
            self,
            *,
            categoryId: typing.Union[str, typing.List[str]] = ...,
            locale: str = ...,
            maxAllowedMaturityRating: typing_extensions.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ] = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> Volume2HttpRequest: ...
    @typing.type_check_only
    class PersonalizedstreamResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            locale: str = ...,
            maxAllowedMaturityRating: typing_extensions.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ] = ...,
            source: str = ...,
            **kwargs: typing.Any
        ) -> DiscoveryclustersHttpRequest: ...
    @typing.type_check_only
    class PromoofferResource(googleapiclient.discovery.Resource):
        def accept(
            self,
            *,
            androidId: str = ...,
            device: str = ...,
            manufacturer: str = ...,
            model: str = ...,
            offerId: str = ...,
            product: str = ...,
            serial: str = ...,
            volumeId: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def dismiss(
            self,
            *,
            androidId: str = ...,
            device: str = ...,
            manufacturer: str = ...,
            model: str = ...,
            offerId: str = ...,
            product: str = ...,
            serial: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self,
            *,
            androidId: str = ...,
            device: str = ...,
            manufacturer: str = ...,
            model: str = ...,
            product: str = ...,
            serial: str = ...,
            **kwargs: typing.Any
        ) -> OffersHttpRequest: ...
    @typing.type_check_only
    class SeriesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MembershipResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                page_size: int = ...,
                page_token: str = ...,
                series_id: str = ...,
                **kwargs: typing.Any
            ) -> SeriesmembershipHttpRequest: ...
        def get(
            self,
            *,
            series_id: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> SeriesHttpRequest: ...
        def membership(self) -> MembershipResource: ...
    @typing.type_check_only
    class VolumesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssociatedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                volumeId: str,
                association: typing_extensions.Literal[
                    "ASSOCIATION_UNDEFINED",
                    "end-of-sample",
                    "end-of-volume",
                    "related-for-play",
                ] = ...,
                locale: str = ...,
                maxAllowedMaturityRating: typing_extensions.Literal[
                    "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
                ] = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
        @typing.type_check_only
        class MybooksResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                acquireMethod: typing.Union[
                    typing_extensions.Literal[
                        "ACQUIRE_METHOD_UNDEFINED",
                        "FAMILY_SHARED",
                        "PREORDERED",
                        "PREVIOUSLY_RENTED",
                        "PUBLIC_DOMAIN",
                        "PURCHASED",
                        "RENTED",
                        "SAMPLE",
                        "UPLOADED",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "ACQUIRE_METHOD_UNDEFINED",
                            "FAMILY_SHARED",
                            "PREORDERED",
                            "PREVIOUSLY_RENTED",
                            "PUBLIC_DOMAIN",
                            "PURCHASED",
                            "RENTED",
                            "SAMPLE",
                            "UPLOADED",
                        ]
                    ],
                ] = ...,
                country: str = ...,
                locale: str = ...,
                maxResults: int = ...,
                processingState: typing.Union[
                    typing_extensions.Literal[
                        "PROCESSING_STATE_UNDEFINED",
                        "COMPLETED_FAILED",
                        "COMPLETED_SUCCESS",
                        "RUNNING",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "PROCESSING_STATE_UNDEFINED",
                            "COMPLETED_FAILED",
                            "COMPLETED_SUCCESS",
                            "RUNNING",
                        ]
                    ],
                ] = ...,
                source: str = ...,
                startIndex: int = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
        @typing.type_check_only
        class RecommendedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                locale: str = ...,
                maxAllowedMaturityRating: typing_extensions.Literal[
                    "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
                ] = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
            def rate(
                self,
                *,
                locale: str = ...,
                rating: typing_extensions.Literal[
                    "RATING_UNDEFINED", "HAVE_IT", "NOT_INTERESTED"
                ] = ...,
                source: str = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> BooksVolumesRecommendedRateResponseHttpRequest: ...
        @typing.type_check_only
        class UseruploadedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                locale: str = ...,
                maxResults: int = ...,
                processingState: typing.Union[
                    typing_extensions.Literal[
                        "PROCESSING_STATE_UNDEFINED",
                        "COMPLETED_FAILED",
                        "COMPLETED_SUCCESS",
                        "RUNNING",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "PROCESSING_STATE_UNDEFINED",
                            "COMPLETED_FAILED",
                            "COMPLETED_SUCCESS",
                            "RUNNING",
                        ]
                    ],
                ] = ...,
                source: str = ...,
                startIndex: int = ...,
                volumeId: typing.Union[str, typing.List[str]] = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
        def get(
            self,
            *,
            volumeId: str,
            country: str = ...,
            includeNonComicsSeries: bool = ...,
            partner: str = ...,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "FULL", "LITE"
            ] = ...,
            source: str = ...,
            user_library_consistent_read: bool = ...,
            **kwargs: typing.Any
        ) -> VolumeHttpRequest: ...
        def list(
            self,
            *,
            download: typing_extensions.Literal["DOWNLOAD_UNDEFINED", "EPUB"] = ...,
            filter: typing_extensions.Literal[
                "FILTER_UNDEFINED",
                "ebooks",
                "free-ebooks",
                "full",
                "paid-ebooks",
                "partial",
            ] = ...,
            langRestrict: str = ...,
            libraryRestrict: typing_extensions.Literal[
                "LIBRARY_RESTRICT_UNDEFINED", "my-library", "no-restrict"
            ] = ...,
            maxAllowedMaturityRating: typing_extensions.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ] = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "ORDER_BY_UNDEFINED", "newest", "relevance"
            ] = ...,
            partner: str = ...,
            printType: typing_extensions.Literal[
                "PRINT_TYPE_UNDEFINED", "ALL", "BOOKS", "MAGAZINES"
            ] = ...,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "FULL", "LITE"
            ] = ...,
            q: str = ...,
            showPreorders: bool = ...,
            source: str = ...,
            startIndex: int = ...,
            **kwargs: typing.Any
        ) -> VolumesHttpRequest: ...
        def associated(self) -> AssociatedResource: ...
        def mybooks(self) -> MybooksResource: ...
        def recommended(self) -> RecommendedResource: ...
        def useruploaded(self) -> UseruploadedResource: ...
    def bookshelves(self) -> BookshelvesResource: ...
    def cloudloading(self) -> CloudloadingResource: ...
    def dictionary(self) -> DictionaryResource: ...
    def familysharing(self) -> FamilysharingResource: ...
    def layers(self) -> LayersResource: ...
    def myconfig(self) -> MyconfigResource: ...
    def mylibrary(self) -> MylibraryResource: ...
    def notification(self) -> NotificationResource: ...
    def onboarding(self) -> OnboardingResource: ...
    def personalizedstream(self) -> PersonalizedstreamResource: ...
    def promooffer(self) -> PromoofferResource: ...
    def series(self) -> SeriesResource: ...
    def volumes(self) -> VolumesResource: ...

@typing.type_check_only
class AnnotationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Annotation: ...

@typing.type_check_only
class AnnotationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Annotations: ...

@typing.type_check_only
class AnnotationsSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AnnotationsSummary: ...

@typing.type_check_only
class AnnotationsdataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Annotationsdata: ...

@typing.type_check_only
class BooksCloudloadingResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BooksCloudloadingResource: ...

@typing.type_check_only
class BooksVolumesRecommendedRateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BooksVolumesRecommendedRateResponse: ...

@typing.type_check_only
class BookshelfHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Bookshelf: ...

@typing.type_check_only
class BookshelvesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Bookshelves: ...

@typing.type_check_only
class CategoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Category: ...

@typing.type_check_only
class DictionaryAnnotationdataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DictionaryAnnotationdata: ...

@typing.type_check_only
class DiscoveryclustersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Discoveryclusters: ...

@typing.type_check_only
class DownloadAccessesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DownloadAccesses: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

@typing.type_check_only
class FamilyInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FamilyInfo: ...

@typing.type_check_only
class LayersummariesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Layersummaries: ...

@typing.type_check_only
class LayersummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Layersummary: ...

@typing.type_check_only
class MetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Metadata: ...

@typing.type_check_only
class NotificationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Notification: ...

@typing.type_check_only
class OffersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Offers: ...

@typing.type_check_only
class ReadingPositionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReadingPosition: ...

@typing.type_check_only
class RequestAccessDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RequestAccessData: ...

@typing.type_check_only
class SeriesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Series: ...

@typing.type_check_only
class SeriesmembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Seriesmembership: ...

@typing.type_check_only
class UsersettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Usersettings: ...

@typing.type_check_only
class VolumeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volume: ...

@typing.type_check_only
class Volume2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volume2: ...

@typing.type_check_only
class VolumeannotationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volumeannotation: ...

@typing.type_check_only
class VolumeannotationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volumeannotations: ...

@typing.type_check_only
class VolumesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volumes: ...
