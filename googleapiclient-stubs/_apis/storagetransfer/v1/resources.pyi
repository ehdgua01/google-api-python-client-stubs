import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class StoragetransferResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class GoogleServiceAccountsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> GoogleServiceAccountHttpRequest: ...
    @typing.type_check_only
    class TransferJobsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: TransferJob = ..., **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
        def get(
            self, *, jobName: str, projectId: str, **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
        def list(
            self,
            *,
            filter: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListTransferJobsResponseHttpRequest: ...
        def patch(
            self,
            *,
            jobName: str,
            body: UpdateTransferJobRequest = ...,
            **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
        def run(
            self,
            *,
            jobName: str,
            body: RunTransferJobRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    @typing.type_check_only
    class TransferOperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def pause(
            self,
            *,
            name: str,
            body: PauseTransferOperationRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def resume(
            self,
            *,
            name: str,
            body: ResumeTransferOperationRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    def googleServiceAccounts(self) -> GoogleServiceAccountsResource: ...
    def transferJobs(self) -> TransferJobsResource: ...
    def transferOperations(self) -> TransferOperationsResource: ...

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
class GoogleServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleServiceAccount: ...

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
class ListTransferJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTransferJobsResponse: ...

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
class TransferJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TransferJob: ...
