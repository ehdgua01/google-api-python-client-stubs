import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class AdExchangeBuyerIIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ClientsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InvitationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    body: ClientUserInvitation = ...,
                    **kwargs: typing.Any
                ) -> ClientUserInvitationHttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    invitationId: str,
                    **kwargs: typing.Any
                ) -> ClientUserInvitationHttpRequest: ...
                def list(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListClientUserInvitationsResponseHttpRequest: ...
            @typing.type_check_only
            class UsersResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    userId: str,
                    **kwargs: typing.Any
                ) -> ClientUserHttpRequest: ...
                def list(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListClientUsersResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    userId: str,
                    body: ClientUser = ...,
                    **kwargs: typing.Any
                ) -> ClientUserHttpRequest: ...
            def create(
                self, *, accountId: str, body: Client = ..., **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def get(
                self, *, accountId: str, clientAccountId: str, **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                partnerClientId: str = ...,
                **kwargs: typing.Any
            ) -> ListClientsResponseHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                clientAccountId: str,
                body: Client = ...,
                **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def invitations(self) -> InvitationsResource: ...
            def users(self) -> UsersResource: ...
        @typing.type_check_only
        class CreativesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DealAssociationsResource(googleapiclient.discovery.Resource):
                def add(
                    self,
                    *,
                    accountId: str,
                    creativeId: str,
                    body: AddDealAssociationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    accountId: str,
                    creativeId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    query: str = ...,
                    **kwargs: typing.Any
                ) -> ListDealAssociationsResponseHttpRequest: ...
                def remove(
                    self,
                    *,
                    accountId: str,
                    creativeId: str,
                    body: RemoveDealAssociationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            def create(
                self,
                *,
                accountId: str,
                body: Creative = ...,
                duplicateIdMode: typing_extensions.Literal[
                    "NO_DUPLICATES", "FORCE_ENABLE_DUPLICATE_IDS"
                ] = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def get(
                self, *, accountId: str, creativeId: str, **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                query: str = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
            def stopWatching(
                self,
                *,
                accountId: str,
                creativeId: str,
                body: StopWatchingCreativeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                creativeId: str,
                body: Creative = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def watch(
                self,
                *,
                accountId: str,
                creativeId: str,
                body: WatchCreativeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def dealAssociations(self) -> DealAssociationsResource: ...
        @typing.type_check_only
        class FinalizedProposalsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                filter: str = ...,
                filterSyntax: typing_extensions.Literal[
                    "FILTER_SYNTAX_UNSPECIFIED", "PQL", "LIST_FILTER"
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProposalsResponseHttpRequest: ...
        @typing.type_check_only
        class ProductsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, accountId: str, productId: str, **kwargs: typing.Any
            ) -> ProductHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProductsResponseHttpRequest: ...
        @typing.type_check_only
        class ProposalsResource(googleapiclient.discovery.Resource):
            def accept(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: AcceptProposalRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def addNote(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: AddNoteRequest = ...,
                **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
            def cancelNegotiation(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: CancelNegotiationRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def completeSetup(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: CompleteSetupRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def create(
                self, *, accountId: str, body: Proposal = ..., **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def get(
                self, *, accountId: str, proposalId: str, **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                filter: str = ...,
                filterSyntax: typing_extensions.Literal[
                    "FILTER_SYNTAX_UNSPECIFIED", "PQL", "LIST_FILTER"
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProposalsResponseHttpRequest: ...
            def pause(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: PauseProposalRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def resume(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: ResumeProposalRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: Proposal = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
        @typing.type_check_only
        class PublisherProfilesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, accountId: str, publisherProfileId: str, **kwargs: typing.Any
            ) -> PublisherProfileHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPublisherProfilesResponseHttpRequest: ...
        def clients(self) -> ClientsResource: ...
        def creatives(self) -> CreativesResource: ...
        def finalizedProposals(self) -> FinalizedProposalsResource: ...
        def products(self) -> ProductsResource: ...
        def proposals(self) -> ProposalsResource: ...
        def publisherProfiles(self) -> PublisherProfilesResource: ...
    @typing.type_check_only
    class BiddersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccountsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FilterSetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BidMetricsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListBidMetricsResponseHttpRequest: ...
                @typing.type_check_only
                class BidResponseErrorsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListBidResponseErrorsResponseHttpRequest: ...
                @typing.type_check_only
                class BidResponsesWithoutBidsResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListBidResponsesWithoutBidsResponseHttpRequest: ...
                @typing.type_check_only
                class FilteredBidRequestsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListFilteredBidRequestsResponseHttpRequest: ...
                @typing.type_check_only
                class FilteredBidsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class CreativesResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            filterSetName: str,
                            creativeStatusId: int,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListCreativeStatusBreakdownByCreativeResponseHttpRequest: ...
                    @typing.type_check_only
                    class DetailsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            filterSetName: str,
                            creativeStatusId: int,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListCreativeStatusBreakdownByDetailResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListFilteredBidsResponseHttpRequest: ...
                    def creatives(self) -> CreativesResource: ...
                    def details(self) -> DetailsResource: ...
                @typing.type_check_only
                class ImpressionMetricsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListImpressionMetricsResponseHttpRequest: ...
                @typing.type_check_only
                class LosingBidsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListLosingBidsResponseHttpRequest: ...
                @typing.type_check_only
                class NonBillableWinningBidsResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListNonBillableWinningBidsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    ownerName: str,
                    body: FilterSet = ...,
                    isTransient: bool = ...,
                    **kwargs: typing.Any
                ) -> FilterSetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FilterSetHttpRequest: ...
                def list(
                    self,
                    *,
                    ownerName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListFilterSetsResponseHttpRequest: ...
                def bidMetrics(self) -> BidMetricsResource: ...
                def bidResponseErrors(self) -> BidResponseErrorsResource: ...
                def bidResponsesWithoutBids(
                    self,
                ) -> BidResponsesWithoutBidsResource: ...
                def filteredBidRequests(self) -> FilteredBidRequestsResource: ...
                def filteredBids(self) -> FilteredBidsResource: ...
                def impressionMetrics(self) -> ImpressionMetricsResource: ...
                def losingBids(self) -> LosingBidsResource: ...
                def nonBillableWinningBids(self) -> NonBillableWinningBidsResource: ...
            def filterSets(self) -> FilterSetsResource: ...
        @typing.type_check_only
        class FilterSetsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BidMetricsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListBidMetricsResponseHttpRequest: ...
            @typing.type_check_only
            class BidResponseErrorsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListBidResponseErrorsResponseHttpRequest: ...
            @typing.type_check_only
            class BidResponsesWithoutBidsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListBidResponsesWithoutBidsResponseHttpRequest: ...
            @typing.type_check_only
            class FilteredBidRequestsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListFilteredBidRequestsResponseHttpRequest: ...
            @typing.type_check_only
            class FilteredBidsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CreativesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        creativeStatusId: int,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCreativeStatusBreakdownByCreativeResponseHttpRequest: ...
                @typing.type_check_only
                class DetailsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        creativeStatusId: int,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCreativeStatusBreakdownByDetailResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListFilteredBidsResponseHttpRequest: ...
                def creatives(self) -> CreativesResource: ...
                def details(self) -> DetailsResource: ...
            @typing.type_check_only
            class ImpressionMetricsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListImpressionMetricsResponseHttpRequest: ...
            @typing.type_check_only
            class LosingBidsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListLosingBidsResponseHttpRequest: ...
            @typing.type_check_only
            class NonBillableWinningBidsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListNonBillableWinningBidsResponseHttpRequest: ...
            def create(
                self,
                *,
                ownerName: str,
                body: FilterSet = ...,
                isTransient: bool = ...,
                **kwargs: typing.Any
            ) -> FilterSetHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> FilterSetHttpRequest: ...
            def list(
                self,
                *,
                ownerName: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListFilterSetsResponseHttpRequest: ...
            def bidMetrics(self) -> BidMetricsResource: ...
            def bidResponseErrors(self) -> BidResponseErrorsResource: ...
            def bidResponsesWithoutBids(self) -> BidResponsesWithoutBidsResource: ...
            def filteredBidRequests(self) -> FilteredBidRequestsResource: ...
            def filteredBids(self) -> FilteredBidsResource: ...
            def impressionMetrics(self) -> ImpressionMetricsResource: ...
            def losingBids(self) -> LosingBidsResource: ...
            def nonBillableWinningBids(self) -> NonBillableWinningBidsResource: ...
        def accounts(self) -> AccountsResource: ...
        def filterSets(self) -> FilterSetsResource: ...
    def accounts(self) -> AccountsResource: ...
    def bidders(self) -> BiddersResource: ...

@typing.type_check_only
class ClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Client: ...

@typing.type_check_only
class ClientUserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClientUser: ...

@typing.type_check_only
class ClientUserInvitationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClientUserInvitation: ...

@typing.type_check_only
class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Creative: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

@typing.type_check_only
class FilterSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FilterSet: ...

@typing.type_check_only
class ListBidMetricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBidMetricsResponse: ...

@typing.type_check_only
class ListBidResponseErrorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBidResponseErrorsResponse: ...

@typing.type_check_only
class ListBidResponsesWithoutBidsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBidResponsesWithoutBidsResponse: ...

@typing.type_check_only
class ListClientUserInvitationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListClientUserInvitationsResponse: ...

@typing.type_check_only
class ListClientUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListClientUsersResponse: ...

@typing.type_check_only
class ListClientsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListClientsResponse: ...

@typing.type_check_only
class ListCreativeStatusBreakdownByCreativeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCreativeStatusBreakdownByCreativeResponse: ...

@typing.type_check_only
class ListCreativeStatusBreakdownByDetailResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCreativeStatusBreakdownByDetailResponse: ...

@typing.type_check_only
class ListCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCreativesResponse: ...

@typing.type_check_only
class ListDealAssociationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDealAssociationsResponse: ...

@typing.type_check_only
class ListFilterSetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFilterSetsResponse: ...

@typing.type_check_only
class ListFilteredBidRequestsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFilteredBidRequestsResponse: ...

@typing.type_check_only
class ListFilteredBidsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFilteredBidsResponse: ...

@typing.type_check_only
class ListImpressionMetricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListImpressionMetricsResponse: ...

@typing.type_check_only
class ListLosingBidsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLosingBidsResponse: ...

@typing.type_check_only
class ListNonBillableWinningBidsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNonBillableWinningBidsResponse: ...

@typing.type_check_only
class ListProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProductsResponse: ...

@typing.type_check_only
class ListProposalsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProposalsResponse: ...

@typing.type_check_only
class ListPublisherProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPublisherProfilesResponse: ...

@typing.type_check_only
class NoteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Note: ...

@typing.type_check_only
class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Product: ...

@typing.type_check_only
class ProposalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Proposal: ...

@typing.type_check_only
class PublisherProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublisherProfile: ...
