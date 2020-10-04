import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class VaultResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class MattersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ExportsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, matterId: str, body: Export = ..., **kwargs: typing.Any
            ) -> ExportHttpRequest: ...
            def delete(
                self, *, matterId: str, exportId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, matterId: str, exportId: str, **kwargs: typing.Any
            ) -> ExportHttpRequest: ...
            def list(
                self,
                *,
                matterId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListExportsResponseHttpRequest: ...
        @typing.type_check_only
        class HoldsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AccountsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    matterId: str,
                    holdId: str,
                    body: HeldAccount = ...,
                    **kwargs: typing.Any
                ) -> HeldAccountHttpRequest: ...
                def delete(
                    self,
                    *,
                    matterId: str,
                    holdId: str,
                    accountId: str,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self, *, matterId: str, holdId: str, **kwargs: typing.Any
                ) -> ListHeldAccountsResponseHttpRequest: ...
            def addHeldAccounts(
                self,
                *,
                matterId: str,
                holdId: str,
                body: AddHeldAccountsRequest = ...,
                **kwargs: typing.Any
            ) -> AddHeldAccountsResponseHttpRequest: ...
            def create(
                self, *, matterId: str, body: Hold = ..., **kwargs: typing.Any
            ) -> HoldHttpRequest: ...
            def delete(
                self, *, matterId: str, holdId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                matterId: str,
                holdId: str,
                view: typing_extensions.Literal[
                    "HOLD_VIEW_UNSPECIFIED", "BASIC_HOLD", "FULL_HOLD"
                ] = ...,
                **kwargs: typing.Any
            ) -> HoldHttpRequest: ...
            def list(
                self,
                *,
                matterId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "HOLD_VIEW_UNSPECIFIED", "BASIC_HOLD", "FULL_HOLD"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListHoldsResponseHttpRequest: ...
            def removeHeldAccounts(
                self,
                *,
                matterId: str,
                holdId: str,
                body: RemoveHeldAccountsRequest = ...,
                **kwargs: typing.Any
            ) -> RemoveHeldAccountsResponseHttpRequest: ...
            def update(
                self,
                *,
                matterId: str,
                holdId: str,
                body: Hold = ...,
                **kwargs: typing.Any
            ) -> HoldHttpRequest: ...
            def accounts(self) -> AccountsResource: ...
        @typing.type_check_only
        class SavedQueriesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, matterId: str, body: SavedQuery = ..., **kwargs: typing.Any
            ) -> SavedQueryHttpRequest: ...
            def delete(
                self, *, matterId: str, savedQueryId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, matterId: str, savedQueryId: str, **kwargs: typing.Any
            ) -> SavedQueryHttpRequest: ...
            def list(
                self,
                *,
                matterId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSavedQueriesResponseHttpRequest: ...
        def addPermissions(
            self,
            *,
            matterId: str,
            body: AddMatterPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> MatterPermissionHttpRequest: ...
        def close(self, *, matterId: str, body: CloseMatterRequest = ..., **kwargs: typing.Any) -> CloseMatterResponseHttpRequest: ...  # type: ignore
        def create(
            self, *, body: Matter = ..., **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def delete(
            self, *, matterId: str, **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def get(
            self,
            *,
            matterId: str,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            state: typing_extensions.Literal[
                "STATE_UNSPECIFIED", "OPEN", "CLOSED", "DELETED"
            ] = ...,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> ListMattersResponseHttpRequest: ...
        def removePermissions(
            self,
            *,
            matterId: str,
            body: RemoveMatterPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def reopen(
            self,
            *,
            matterId: str,
            body: ReopenMatterRequest = ...,
            **kwargs: typing.Any
        ) -> ReopenMatterResponseHttpRequest: ...
        def undelete(
            self,
            *,
            matterId: str,
            body: UndeleteMatterRequest = ...,
            **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def update(
            self, *, matterId: str, body: Matter = ..., **kwargs: typing.Any
        ) -> MatterHttpRequest: ...
        def exports(self) -> ExportsResource: ...
        def holds(self) -> HoldsResource: ...
        def savedQueries(self) -> SavedQueriesResource: ...
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
    def matters(self) -> MattersResource: ...
    def operations(self) -> OperationsResource: ...

@typing.type_check_only
class AddHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AddHeldAccountsResponse: ...

@typing.type_check_only
class CloseMatterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CloseMatterResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

@typing.type_check_only
class ExportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Export: ...

@typing.type_check_only
class HeldAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HeldAccount: ...

@typing.type_check_only
class HoldHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Hold: ...

@typing.type_check_only
class ListExportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListExportsResponse: ...

@typing.type_check_only
class ListHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListHeldAccountsResponse: ...

@typing.type_check_only
class ListHoldsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListHoldsResponse: ...

@typing.type_check_only
class ListMattersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMattersResponse: ...

@typing.type_check_only
class ListSavedQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSavedQueriesResponse: ...

@typing.type_check_only
class MatterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Matter: ...

@typing.type_check_only
class MatterPermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MatterPermission: ...

@typing.type_check_only
class RemoveHeldAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RemoveHeldAccountsResponse: ...

@typing.type_check_only
class ReopenMatterResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReopenMatterResponse: ...

@typing.type_check_only
class SavedQueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SavedQuery: ...
