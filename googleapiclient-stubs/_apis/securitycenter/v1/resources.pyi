import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class SecurityCommandCenterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any
            ) -> GroupAssetsResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                compareDuration: str = ...,
                fieldMask: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readTime: str = ...,
                **kwargs: typing.Any
            ) -> ListAssetsResponseHttpRequest: ...
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: SecurityMarks = ...,
                startTime: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SecurityMarksHttpRequest: ...
        @typing.type_check_only
        class SourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FindingsResource(googleapiclient.discovery.Resource):
                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any
                ) -> GroupFindingsResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    compareDuration: str = ...,
                    fieldMask: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    **kwargs: typing.Any
                ) -> ListFindingsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> SecurityMarksHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSourcesResponseHttpRequest: ...
            def findings(self) -> FindingsResource: ...
        def assets(self) -> AssetsResource: ...
        def sources(self) -> SourcesResource: ...
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any
            ) -> GroupAssetsResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                compareDuration: str = ...,
                fieldMask: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readTime: str = ...,
                **kwargs: typing.Any
            ) -> ListAssetsResponseHttpRequest: ...
            def runDiscovery(
                self,
                *,
                parent: str,
                body: RunAssetDiscoveryRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: SecurityMarks = ...,
                startTime: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SecurityMarksHttpRequest: ...
        @typing.type_check_only
        class NotificationConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: NotificationConfig = ...,
                configId: str = ...,
                **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListNotificationConfigsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: NotificationConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def cancel(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
        @typing.type_check_only
        class SourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FindingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Finding = ...,
                    findingId: str = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any
                ) -> GroupFindingsResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    compareDuration: str = ...,
                    fieldMask: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    **kwargs: typing.Any
                ) -> ListFindingsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> SecurityMarksHttpRequest: ...
            def create(
                self, *, parent: str, body: Source = ..., **kwargs: typing.Any
            ) -> SourceHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> SourceHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSourcesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Source = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SourceHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def findings(self) -> FindingsResource: ...
        def getOrganizationSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def updateOrganizationSettings(
            self,
            *,
            name: str,
            body: OrganizationSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def assets(self) -> AssetsResource: ...
        def notificationConfigs(self) -> NotificationConfigsResource: ...
        def operations(self) -> OperationsResource: ...
        def sources(self) -> SourcesResource: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any
            ) -> GroupAssetsResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                compareDuration: str = ...,
                fieldMask: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readTime: str = ...,
                **kwargs: typing.Any
            ) -> ListAssetsResponseHttpRequest: ...
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: SecurityMarks = ...,
                startTime: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SecurityMarksHttpRequest: ...
        @typing.type_check_only
        class SourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FindingsResource(googleapiclient.discovery.Resource):
                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any
                ) -> GroupFindingsResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    compareDuration: str = ...,
                    fieldMask: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    **kwargs: typing.Any
                ) -> ListFindingsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> SecurityMarksHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSourcesResponseHttpRequest: ...
            def findings(self) -> FindingsResource: ...
        def assets(self) -> AssetsResource: ...
        def sources(self) -> SourcesResource: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Finding: ...

@typing.type_check_only
class GroupAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GroupAssetsResponse: ...

@typing.type_check_only
class GroupFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GroupFindingsResponse: ...

@typing.type_check_only
class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListAssetsResponse: ...

@typing.type_check_only
class ListFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListFindingsResponse: ...

@typing.type_check_only
class ListNotificationConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListNotificationConfigsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListSourcesResponse: ...

@typing.type_check_only
class NotificationConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> NotificationConfig: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class OrganizationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> OrganizationSettings: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class SecurityMarksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SecurityMarks: ...

@typing.type_check_only
class SourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Source: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
