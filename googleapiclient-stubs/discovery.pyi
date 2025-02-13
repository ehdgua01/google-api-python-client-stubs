from email.generator import Generator as BytesGenerator
from typing import Any, Dict, Optional, TypeVar, Union, overload

import google.auth.credentials  # type: ignore
import httplib2  # type: ignore
import oauth2client  # type: ignore
from google.api_core.client_options import ClientOptions  # type: ignore
from typing_extensions import Literal

import googleapiclient._apis.abusiveexperiencereport.v1.resources
import googleapiclient._apis.acceleratedmobilepageurl.v1.resources
import googleapiclient._apis.accessapproval.v1.resources
import googleapiclient._apis.accesscontextmanager.v1.resources
import googleapiclient._apis.accesscontextmanager.v1beta.resources
import googleapiclient._apis.adexchangebuyer2.v2beta1.resources
import googleapiclient._apis.adexchangebuyer.v1_2.resources
import googleapiclient._apis.adexchangebuyer.v1_3.resources
import googleapiclient._apis.adexchangebuyer.v1_4.resources
import googleapiclient._apis.adexperiencereport.v1.resources
import googleapiclient._apis.admin.datatransfer_v1.resources
import googleapiclient._apis.admin.directory_v1.resources
import googleapiclient._apis.admin.reports_v1.resources
import googleapiclient._apis.admob.v1.resources
import googleapiclient._apis.admob.v1beta.resources
import googleapiclient._apis.adsense.v1_4.resources
import googleapiclient._apis.adsensehost.v4_1.resources
import googleapiclient._apis.alertcenter.v1beta1.resources
import googleapiclient._apis.analytics.v3.resources
import googleapiclient._apis.analyticsadmin.v1alpha.resources
import googleapiclient._apis.analyticsdata.v1alpha.resources
import googleapiclient._apis.analyticsreporting.v4.resources
import googleapiclient._apis.androiddeviceprovisioning.v1.resources
import googleapiclient._apis.androidenterprise.v1.resources
import googleapiclient._apis.androidmanagement.v1.resources
import googleapiclient._apis.androidpublisher.v3.resources
import googleapiclient._apis.apigateway.v1.resources
import googleapiclient._apis.apigateway.v1beta.resources
import googleapiclient._apis.apigee.v1.resources
import googleapiclient._apis.appengine.v1.resources
import googleapiclient._apis.appengine.v1alpha.resources
import googleapiclient._apis.appengine.v1beta.resources
import googleapiclient._apis.area120tables.v1alpha1.resources
import googleapiclient._apis.artifactregistry.v1.resources
import googleapiclient._apis.artifactregistry.v1beta1.resources
import googleapiclient._apis.artifactregistry.v1beta2.resources
import googleapiclient._apis.assuredworkloads.v1.resources
import googleapiclient._apis.bigquery.v2.resources
import googleapiclient._apis.bigqueryconnection.v1beta1.resources
import googleapiclient._apis.bigquerydatatransfer.v1.resources
import googleapiclient._apis.bigqueryreservation.v1.resources
import googleapiclient._apis.bigqueryreservation.v1beta1.resources
import googleapiclient._apis.bigtableadmin.v1.resources
import googleapiclient._apis.bigtableadmin.v2.resources
import googleapiclient._apis.billingbudgets.v1.resources
import googleapiclient._apis.billingbudgets.v1beta1.resources
import googleapiclient._apis.binaryauthorization.v1.resources
import googleapiclient._apis.binaryauthorization.v1beta1.resources
import googleapiclient._apis.blogger.v2.resources
import googleapiclient._apis.blogger.v3.resources
import googleapiclient._apis.books.v1.resources
import googleapiclient._apis.calendar.v3.resources
import googleapiclient._apis.chat.v1.resources
import googleapiclient._apis.chromemanagement.v1.resources
import googleapiclient._apis.chromeuxreport.v1.resources
import googleapiclient._apis.civicinfo.v2.resources
import googleapiclient._apis.classroom.v1.resources
import googleapiclient._apis.cloudasset.v1.resources
import googleapiclient._apis.cloudasset.v1beta1.resources
import googleapiclient._apis.cloudasset.v1p1beta1.resources
import googleapiclient._apis.cloudasset.v1p4beta1.resources
import googleapiclient._apis.cloudasset.v1p5beta1.resources
import googleapiclient._apis.cloudasset.v1p7beta1.resources
import googleapiclient._apis.cloudbilling.v1.resources
import googleapiclient._apis.cloudbuild.v1.resources
import googleapiclient._apis.cloudbuild.v1alpha1.resources
import googleapiclient._apis.cloudbuild.v1alpha2.resources
import googleapiclient._apis.cloudchannel.v1.resources
import googleapiclient._apis.clouddebugger.v2.resources
import googleapiclient._apis.clouderrorreporting.v1beta1.resources
import googleapiclient._apis.cloudfunctions.v1.resources
import googleapiclient._apis.cloudidentity.v1.resources
import googleapiclient._apis.cloudidentity.v1beta1.resources
import googleapiclient._apis.cloudiot.v1.resources
import googleapiclient._apis.cloudkms.v1.resources
import googleapiclient._apis.cloudprofiler.v2.resources
import googleapiclient._apis.cloudresourcemanager.v1.resources
import googleapiclient._apis.cloudresourcemanager.v1beta1.resources
import googleapiclient._apis.cloudresourcemanager.v2.resources
import googleapiclient._apis.cloudresourcemanager.v2beta1.resources
import googleapiclient._apis.cloudresourcemanager.v3.resources
import googleapiclient._apis.cloudscheduler.v1.resources
import googleapiclient._apis.cloudscheduler.v1beta1.resources
import googleapiclient._apis.cloudsearch.v1.resources
import googleapiclient._apis.cloudshell.v1.resources
import googleapiclient._apis.cloudshell.v1alpha1.resources
import googleapiclient._apis.cloudtasks.v2.resources
import googleapiclient._apis.cloudtasks.v2beta2.resources
import googleapiclient._apis.cloudtasks.v2beta3.resources
import googleapiclient._apis.cloudtrace.v1.resources
import googleapiclient._apis.cloudtrace.v2.resources
import googleapiclient._apis.cloudtrace.v2beta1.resources
import googleapiclient._apis.composer.v1.resources
import googleapiclient._apis.composer.v1beta1.resources
import googleapiclient._apis.compute.alpha.resources
import googleapiclient._apis.compute.beta.resources
import googleapiclient._apis.compute.v1.resources
import googleapiclient._apis.container.v1.resources
import googleapiclient._apis.container.v1beta1.resources
import googleapiclient._apis.containeranalysis.v1alpha1.resources
import googleapiclient._apis.containeranalysis.v1beta1.resources
import googleapiclient._apis.content.v2.resources
import googleapiclient._apis.content.v2_1.resources
import googleapiclient._apis.customsearch.v1.resources
import googleapiclient._apis.datacatalog.v1beta1.resources
import googleapiclient._apis.dataflow.v1b3.resources
import googleapiclient._apis.datafusion.v1.resources
import googleapiclient._apis.datafusion.v1beta1.resources
import googleapiclient._apis.datalabeling.v1beta1.resources
import googleapiclient._apis.datamigration.v1beta1.resources
import googleapiclient._apis.dataproc.v1.resources
import googleapiclient._apis.dataproc.v1beta2.resources
import googleapiclient._apis.datastore.v1.resources
import googleapiclient._apis.datastore.v1beta1.resources
import googleapiclient._apis.datastore.v1beta3.resources
import googleapiclient._apis.deploymentmanager.alpha.resources
import googleapiclient._apis.deploymentmanager.v2.resources
import googleapiclient._apis.deploymentmanager.v2beta.resources
import googleapiclient._apis.dfareporting.v3_3.resources
import googleapiclient._apis.dfareporting.v3_4.resources
import googleapiclient._apis.dialogflow.v2.resources
import googleapiclient._apis.dialogflow.v2beta1.resources
import googleapiclient._apis.dialogflow.v3.resources
import googleapiclient._apis.dialogflow.v3beta1.resources
import googleapiclient._apis.digitalassetlinks.v1.resources
import googleapiclient._apis.discovery.v1.resources
import googleapiclient._apis.displayvideo.v1.resources
import googleapiclient._apis.dlp.v2.resources
import googleapiclient._apis.dns.v1.resources
import googleapiclient._apis.dns.v1beta2.resources
import googleapiclient._apis.docs.v1.resources
import googleapiclient._apis.documentai.v1beta2.resources
import googleapiclient._apis.documentai.v1beta3.resources
import googleapiclient._apis.domains.v1alpha2.resources
import googleapiclient._apis.domains.v1beta1.resources
import googleapiclient._apis.domainsrdap.v1.resources
import googleapiclient._apis.doubleclickbidmanager.v1.resources
import googleapiclient._apis.doubleclickbidmanager.v1_1.resources
import googleapiclient._apis.doubleclicksearch.v2.resources
import googleapiclient._apis.drive.v2.resources
import googleapiclient._apis.drive.v3.resources
import googleapiclient._apis.driveactivity.v2.resources
import googleapiclient._apis.eventarc.v1.resources
import googleapiclient._apis.eventarc.v1beta1.resources
import googleapiclient._apis.factchecktools.v1alpha1.resources
import googleapiclient._apis.fcm.v1.resources
import googleapiclient._apis.file.v1.resources
import googleapiclient._apis.file.v1beta1.resources
import googleapiclient._apis.firebase.v1beta1.resources
import googleapiclient._apis.firebasedatabase.v1beta.resources
import googleapiclient._apis.firebasedynamiclinks.v1.resources
import googleapiclient._apis.firebasehosting.v1.resources
import googleapiclient._apis.firebasehosting.v1beta1.resources
import googleapiclient._apis.firebaseml.v1.resources
import googleapiclient._apis.firebaseml.v1beta2.resources
import googleapiclient._apis.firebaserules.v1.resources
import googleapiclient._apis.firestore.v1.resources
import googleapiclient._apis.firestore.v1beta1.resources
import googleapiclient._apis.firestore.v1beta2.resources
import googleapiclient._apis.fitness.v1.resources
import googleapiclient._apis.games.v1.resources
import googleapiclient._apis.gamesConfiguration.v1configuration.resources
import googleapiclient._apis.gameservices.v1.resources
import googleapiclient._apis.gameservices.v1beta.resources
import googleapiclient._apis.gamesManagement.v1management.resources
import googleapiclient._apis.genomics.v1.resources
import googleapiclient._apis.genomics.v1alpha2.resources
import googleapiclient._apis.genomics.v2alpha1.resources
import googleapiclient._apis.gmail.v1.resources
import googleapiclient._apis.gmailpostmastertools.v1.resources
import googleapiclient._apis.gmailpostmastertools.v1beta1.resources
import googleapiclient._apis.groupsmigration.v1.resources
import googleapiclient._apis.groupssettings.v1.resources
import googleapiclient._apis.healthcare.v1.resources
import googleapiclient._apis.healthcare.v1beta1.resources
import googleapiclient._apis.homegraph.v1.resources
import googleapiclient._apis.iam.v1.resources
import googleapiclient._apis.iamcredentials.v1.resources
import googleapiclient._apis.iap.v1.resources
import googleapiclient._apis.iap.v1beta1.resources
import googleapiclient._apis.identitytoolkit.v3.resources
import googleapiclient._apis.indexing.v3.resources
import googleapiclient._apis.jobs.v3.resources
import googleapiclient._apis.jobs.v3p1beta1.resources
import googleapiclient._apis.jobs.v4.resources
import googleapiclient._apis.kgsearch.v1.resources
import googleapiclient._apis.language.v1.resources
import googleapiclient._apis.language.v1beta1.resources
import googleapiclient._apis.language.v1beta2.resources
import googleapiclient._apis.libraryagent.v1.resources
import googleapiclient._apis.licensing.v1.resources
import googleapiclient._apis.lifesciences.v2beta.resources
import googleapiclient._apis.localservices.v1.resources
import googleapiclient._apis.logging.v2.resources
import googleapiclient._apis.managedidentities.v1.resources
import googleapiclient._apis.managedidentities.v1alpha1.resources
import googleapiclient._apis.managedidentities.v1beta1.resources
import googleapiclient._apis.manufacturers.v1.resources
import googleapiclient._apis.memcache.v1.resources
import googleapiclient._apis.memcache.v1beta2.resources
import googleapiclient._apis.metastore.v1alpha.resources
import googleapiclient._apis.metastore.v1beta.resources
import googleapiclient._apis.ml.v1.resources
import googleapiclient._apis.monitoring.v1.resources
import googleapiclient._apis.monitoring.v3.resources
import googleapiclient._apis.mybusinessaccountmanagement.v1.resources
import googleapiclient._apis.networkconnectivity.v1alpha1.resources
import googleapiclient._apis.networkmanagement.v1.resources
import googleapiclient._apis.networkmanagement.v1beta1.resources
import googleapiclient._apis.notebooks.v1.resources
import googleapiclient._apis.oauth2.v2.resources
import googleapiclient._apis.ondemandscanning.v1beta1.resources
import googleapiclient._apis.osconfig.v1.resources
import googleapiclient._apis.osconfig.v1beta.resources
import googleapiclient._apis.oslogin.v1.resources
import googleapiclient._apis.oslogin.v1alpha.resources
import googleapiclient._apis.oslogin.v1beta.resources
import googleapiclient._apis.pagespeedonline.v5.resources
import googleapiclient._apis.people.v1.resources
import googleapiclient._apis.playablelocations.v3.resources
import googleapiclient._apis.playcustomapp.v1.resources
import googleapiclient._apis.policysimulator.v1beta1.resources
import googleapiclient._apis.policytroubleshooter.v1.resources
import googleapiclient._apis.policytroubleshooter.v1beta.resources
import googleapiclient._apis.poly.v1.resources
import googleapiclient._apis.privateca.v1beta1.resources
import googleapiclient._apis.prod_tt_sasportal.v1alpha1.resources
import googleapiclient._apis.pubsub.v1.resources
import googleapiclient._apis.pubsub.v1beta1a.resources
import googleapiclient._apis.pubsub.v1beta2.resources
import googleapiclient._apis.pubsublite.v1.resources
import googleapiclient._apis.realtimebidding.v1.resources
import googleapiclient._apis.realtimebidding.v1alpha.resources
import googleapiclient._apis.recommendationengine.v1beta1.resources
import googleapiclient._apis.recommender.v1.resources
import googleapiclient._apis.recommender.v1beta1.resources
import googleapiclient._apis.redis.v1.resources
import googleapiclient._apis.redis.v1beta1.resources
import googleapiclient._apis.remotebuildexecution.v1.resources
import googleapiclient._apis.remotebuildexecution.v1alpha.resources
import googleapiclient._apis.remotebuildexecution.v2.resources
import googleapiclient._apis.reseller.v1.resources
import googleapiclient._apis.retail.v2.resources
import googleapiclient._apis.retail.v2alpha.resources
import googleapiclient._apis.retail.v2beta.resources
import googleapiclient._apis.run.v1.resources
import googleapiclient._apis.run.v1alpha1.resources
import googleapiclient._apis.runtimeconfig.v1.resources
import googleapiclient._apis.runtimeconfig.v1beta1.resources
import googleapiclient._apis.safebrowsing.v4.resources
import googleapiclient._apis.sasportal.v1alpha1.resources
import googleapiclient._apis.script.v1.resources
import googleapiclient._apis.searchconsole.v1.resources
import googleapiclient._apis.secretmanager.v1.resources
import googleapiclient._apis.secretmanager.v1beta1.resources
import googleapiclient._apis.securitycenter.v1.resources
import googleapiclient._apis.securitycenter.v1beta1.resources
import googleapiclient._apis.securitycenter.v1beta2.resources
import googleapiclient._apis.serviceconsumermanagement.v1.resources
import googleapiclient._apis.serviceconsumermanagement.v1beta1.resources
import googleapiclient._apis.servicecontrol.v1.resources
import googleapiclient._apis.servicecontrol.v2.resources
import googleapiclient._apis.servicedirectory.v1.resources
import googleapiclient._apis.servicedirectory.v1beta1.resources
import googleapiclient._apis.servicemanagement.v1.resources
import googleapiclient._apis.servicenetworking.v1.resources
import googleapiclient._apis.servicenetworking.v1beta.resources
import googleapiclient._apis.serviceusage.v1.resources
import googleapiclient._apis.serviceusage.v1beta1.resources
import googleapiclient._apis.sheets.v4.resources
import googleapiclient._apis.siteVerification.v1.resources
import googleapiclient._apis.slides.v1.resources
import googleapiclient._apis.smartdevicemanagement.v1.resources
import googleapiclient._apis.sourcerepo.v1.resources
import googleapiclient._apis.spanner.v1.resources
import googleapiclient._apis.speech.v1.resources
import googleapiclient._apis.speech.v1p1beta1.resources
import googleapiclient._apis.speech.v2beta1.resources
import googleapiclient._apis.sqladmin.v1beta4.resources
import googleapiclient._apis.storage.v1.resources
import googleapiclient._apis.storagetransfer.v1.resources
import googleapiclient._apis.streetviewpublish.v1.resources
import googleapiclient._apis.sts.v1.resources
import googleapiclient._apis.sts.v1beta.resources
import googleapiclient._apis.tagmanager.v1.resources
import googleapiclient._apis.tagmanager.v2.resources
import googleapiclient._apis.tasks.v1.resources
import googleapiclient._apis.testing.v1.resources
import googleapiclient._apis.texttospeech.v1.resources
import googleapiclient._apis.texttospeech.v1beta1.resources
import googleapiclient._apis.toolresults.v1beta3.resources
import googleapiclient._apis.tpu.v1.resources
import googleapiclient._apis.tpu.v1alpha1.resources
import googleapiclient._apis.trafficdirector.v2.resources
import googleapiclient._apis.transcoder.v1beta1.resources
import googleapiclient._apis.translate.v2.resources
import googleapiclient._apis.translate.v3.resources
import googleapiclient._apis.translate.v3beta1.resources
import googleapiclient._apis.vault.v1.resources
import googleapiclient._apis.vectortile.v1.resources
import googleapiclient._apis.verifiedaccess.v1.resources
import googleapiclient._apis.videointelligence.v1.resources
import googleapiclient._apis.videointelligence.v1beta2.resources
import googleapiclient._apis.videointelligence.v1p1beta1.resources
import googleapiclient._apis.videointelligence.v1p2beta1.resources
import googleapiclient._apis.videointelligence.v1p3beta1.resources
import googleapiclient._apis.vision.v1.resources
import googleapiclient._apis.vision.v1p1beta1.resources
import googleapiclient._apis.vision.v1p2beta1.resources
import googleapiclient._apis.webfonts.v1.resources
import googleapiclient._apis.webmasters.v3.resources
import googleapiclient._apis.webrisk.v1.resources
import googleapiclient._apis.websecurityscanner.v1.resources
import googleapiclient._apis.websecurityscanner.v1alpha.resources
import googleapiclient._apis.websecurityscanner.v1beta.resources
import googleapiclient._apis.workflowexecutions.v1.resources
import googleapiclient._apis.workflowexecutions.v1beta.resources
import googleapiclient._apis.workflows.v1.resources
import googleapiclient._apis.workflows.v1beta.resources
import googleapiclient._apis.youtube.v3.resources
import googleapiclient._apis.youtubeAnalytics.v2.resources
import googleapiclient._apis.youtubereporting.v1.resources
from googleapiclient.discovery_cache.base import Cache
from googleapiclient.http import HttpMock, HttpRequest
from googleapiclient.model import Model

T = TypeVar("T")

class _BytesGenerator(BytesGenerator): ...

def fix_method_name(name: Any): ...
def key2param(key: Any): ...

class ResourceMethodParameters:
    argmap: Any = ...
    required_params: Any = ...
    repeated_params: Any = ...
    pattern_params: Any = ...
    query_params: Any = ...
    path_params: Any = ...
    param_types: Any = ...
    enum_params: Any = ...
    def __init__(self, method_desc: Any) -> None: ...
    def set_parameters(self, method_desc: Any) -> None: ...

class Resource:
    def __init__(
        self,
        http: Any,
        baseUrl: Any,
        model: Any,
        requestBuilder: Any,
        developerKey: Any,
        resourceDesc: Any,
        rootDesc: Any,
        schema: Any,
    ) -> None: ...
    def __enter__(self: T) -> T: ...
    def __exit__(self, exc_type: Any, exc: Any, exc_tb: Any) -> None: ...
    def close(self) -> None: ...

@overload
def build(
    serviceName: Literal["abusiveexperiencereport"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.abusiveexperiencereport.v1.resources.AbusiveExperienceReportResource: ...
@overload
def build(
    serviceName: Literal["acceleratedmobilepageurl"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.acceleratedmobilepageurl.v1.resources.AcceleratedmobilepageurlResource: ...
@overload
def build(
    serviceName: Literal["accessapproval"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.accessapproval.v1.resources.AccessApprovalResource: ...
@overload
def build(
    serviceName: Literal["accesscontextmanager"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.accesscontextmanager.v1beta.resources.AccessContextManagerResource: ...
@overload
def build(
    serviceName: Literal["accesscontextmanager"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.accesscontextmanager.v1.resources.AccessContextManagerResource: ...
@overload
def build(
    serviceName: Literal["adexchangebuyer"],
    version: Literal["v1_2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.adexchangebuyer.v1_2.resources.AdExchangeBuyerResource: ...
@overload
def build(
    serviceName: Literal["adexchangebuyer"],
    version: Literal["v1_3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.adexchangebuyer.v1_3.resources.AdExchangeBuyerResource: ...
@overload
def build(
    serviceName: Literal["adexchangebuyer"],
    version: Literal["v1_4"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.adexchangebuyer.v1_4.resources.AdExchangeBuyerResource: ...
@overload
def build(
    serviceName: Literal["adexchangebuyer2"],
    version: Literal["v2beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.adexchangebuyer2.v2beta1.resources.AdExchangeBuyerIIResource: ...
@overload
def build(
    serviceName: Literal["adexperiencereport"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.adexperiencereport.v1.resources.AdExperienceReportResource: ...
@overload
def build(
    serviceName: Literal["admin"],
    version: Literal["datatransfer_v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.admin.datatransfer_v1.resources.DataTransferResource: ...
@overload
def build(
    serviceName: Literal["admin"],
    version: Literal["directory_v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.admin.directory_v1.resources.DirectoryResource: ...
@overload
def build(
    serviceName: Literal["admin"],
    version: Literal["reports_v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.admin.reports_v1.resources.ReportsResource: ...
@overload
def build(
    serviceName: Literal["admob"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.admob.v1beta.resources.AdMobResource: ...
@overload
def build(
    serviceName: Literal["admob"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.admob.v1.resources.AdMobResource: ...
@overload
def build(
    serviceName: Literal["adsense"],
    version: Literal["v1_4"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.adsense.v1_4.resources.AdSenseResource: ...
@overload
def build(
    serviceName: Literal["adsensehost"],
    version: Literal["v4_1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.adsensehost.v4_1.resources.AdSenseHostResource: ...
@overload
def build(
    serviceName: Literal["alertcenter"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.alertcenter.v1beta1.resources.AlertCenterResource: ...
@overload
def build(
    serviceName: Literal["analytics"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.analytics.v3.resources.AnalyticsResource: ...
@overload
def build(
    serviceName: Literal["analyticsadmin"],
    version: Literal["v1alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.analyticsadmin.v1alpha.resources.GoogleAnalyticsAdminResource: ...
@overload
def build(
    serviceName: Literal["analyticsdata"],
    version: Literal["v1alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.analyticsdata.v1alpha.resources.AnalyticsDataResource: ...
@overload
def build(
    serviceName: Literal["analyticsreporting"],
    version: Literal["v4"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.analyticsreporting.v4.resources.AnalyticsReportingResource: ...
@overload
def build(
    serviceName: Literal["androiddeviceprovisioning"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.androiddeviceprovisioning.v1.resources.AndroidProvisioningPartnerResource: ...
@overload
def build(
    serviceName: Literal["androidenterprise"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.androidenterprise.v1.resources.AndroidEnterpriseResource: ...
@overload
def build(
    serviceName: Literal["androidmanagement"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.androidmanagement.v1.resources.AndroidManagementResource: ...
@overload
def build(
    serviceName: Literal["androidpublisher"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.androidpublisher.v3.resources.AndroidPublisherResource: ...
@overload
def build(
    serviceName: Literal["apigateway"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.apigateway.v1beta.resources.ApigatewayResource: ...
@overload
def build(
    serviceName: Literal["apigateway"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.apigateway.v1.resources.ApigatewayResource: ...
@overload
def build(
    serviceName: Literal["apigee"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.apigee.v1.resources.ApigeeResource: ...
@overload
def build(
    serviceName: Literal["appengine"],
    version: Literal["v1alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.appengine.v1alpha.resources.AppengineResource: ...
@overload
def build(
    serviceName: Literal["appengine"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.appengine.v1beta.resources.AppengineResource: ...
@overload
def build(
    serviceName: Literal["appengine"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.appengine.v1.resources.AppengineResource: ...
@overload
def build(
    serviceName: Literal["area120tables"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.area120tables.v1alpha1.resources.Area120TablesResource: ...
@overload
def build(
    serviceName: Literal["artifactregistry"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.artifactregistry.v1beta1.resources.ArtifactRegistryResource: ...
@overload
def build(
    serviceName: Literal["artifactregistry"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.artifactregistry.v1beta2.resources.ArtifactRegistryResource: ...
@overload
def build(
    serviceName: Literal["artifactregistry"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.artifactregistry.v1.resources.ArtifactRegistryResource: ...
@overload
def build(
    serviceName: Literal["assuredworkloads"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.assuredworkloads.v1.resources.AssuredworkloadsResource: ...
@overload
def build(
    serviceName: Literal["bigquery"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.bigquery.v2.resources.BigqueryResource: ...
@overload
def build(
    serviceName: Literal["bigqueryconnection"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.bigqueryconnection.v1beta1.resources.BigQueryConnectionServiceResource: ...
@overload
def build(
    serviceName: Literal["bigquerydatatransfer"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.bigquerydatatransfer.v1.resources.BigQueryDataTransferResource: ...
@overload
def build(
    serviceName: Literal["bigqueryreservation"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.bigqueryreservation.v1beta1.resources.BigQueryReservationResource: ...
@overload
def build(
    serviceName: Literal["bigqueryreservation"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.bigqueryreservation.v1.resources.BigQueryReservationResource: ...
@overload
def build(
    serviceName: Literal["bigtableadmin"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.bigtableadmin.v1.resources.BigtableAdminResource: ...
@overload
def build(
    serviceName: Literal["bigtableadmin"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.bigtableadmin.v2.resources.BigtableAdminResource: ...
@overload
def build(
    serviceName: Literal["billingbudgets"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.billingbudgets.v1beta1.resources.CloudBillingBudgetResource: ...
@overload
def build(
    serviceName: Literal["billingbudgets"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.billingbudgets.v1.resources.CloudBillingBudgetResource: ...
@overload
def build(
    serviceName: Literal["binaryauthorization"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.binaryauthorization.v1beta1.resources.BinaryAuthorizationResource: ...
@overload
def build(
    serviceName: Literal["binaryauthorization"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.binaryauthorization.v1.resources.BinaryAuthorizationResource: ...
@overload
def build(
    serviceName: Literal["blogger"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.blogger.v2.resources.BloggerResource: ...
@overload
def build(
    serviceName: Literal["blogger"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.blogger.v3.resources.BloggerResource: ...
@overload
def build(
    serviceName: Literal["books"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.books.v1.resources.BooksResource: ...
@overload
def build(
    serviceName: Literal["calendar"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.calendar.v3.resources.CalendarResource: ...
@overload
def build(
    serviceName: Literal["chat"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.chat.v1.resources.HangoutsChatResource: ...
@overload
def build(
    serviceName: Literal["chromemanagement"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.chromemanagement.v1.resources.ChromeManagementResource: ...
@overload
def build(
    serviceName: Literal["chromeuxreport"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.chromeuxreport.v1.resources.ChromeUXReportResource: ...
@overload
def build(
    serviceName: Literal["civicinfo"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.civicinfo.v2.resources.CivicInfoResource: ...
@overload
def build(
    serviceName: Literal["classroom"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.classroom.v1.resources.ClassroomResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1p1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudasset.v1p1beta1.resources.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1p4beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudasset.v1p4beta1.resources.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1p5beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudasset.v1p5beta1.resources.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1p7beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudasset.v1p7beta1.resources.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudasset.v1beta1.resources.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudasset"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudasset.v1.resources.CloudAssetResource: ...
@overload
def build(
    serviceName: Literal["cloudbilling"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudbilling.v1.resources.CloudbillingResource: ...
@overload
def build(
    serviceName: Literal["cloudbuild"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudbuild.v1alpha1.resources.CloudBuildResource: ...
@overload
def build(
    serviceName: Literal["cloudbuild"],
    version: Literal["v1alpha2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudbuild.v1alpha2.resources.CloudBuildResource: ...
@overload
def build(
    serviceName: Literal["cloudbuild"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudbuild.v1.resources.CloudBuildResource: ...
@overload
def build(
    serviceName: Literal["cloudchannel"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudchannel.v1.resources.CloudchannelResource: ...
@overload
def build(
    serviceName: Literal["clouddebugger"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.clouddebugger.v2.resources.CloudDebuggerResource: ...
@overload
def build(
    serviceName: Literal["clouderrorreporting"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.clouderrorreporting.v1beta1.resources.ClouderrorreportingResource: ...
@overload
def build(
    serviceName: Literal["cloudfunctions"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudfunctions.v1.resources.CloudFunctionsResource: ...
@overload
def build(
    serviceName: Literal["cloudidentity"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudidentity.v1beta1.resources.CloudIdentityResource: ...
@overload
def build(
    serviceName: Literal["cloudidentity"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudidentity.v1.resources.CloudIdentityResource: ...
@overload
def build(
    serviceName: Literal["cloudiot"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudiot.v1.resources.CloudIotResource: ...
@overload
def build(
    serviceName: Literal["cloudkms"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudkms.v1.resources.CloudKMSResource: ...
@overload
def build(
    serviceName: Literal["cloudprofiler"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudprofiler.v2.resources.CloudProfilerResource: ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudresourcemanager.v1beta1.resources.CloudResourceManagerResource: ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v2beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudresourcemanager.v2beta1.resources.CloudResourceManagerResource: ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudresourcemanager.v1.resources.CloudResourceManagerResource: ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudresourcemanager.v2.resources.CloudResourceManagerResource: ...
@overload
def build(
    serviceName: Literal["cloudresourcemanager"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudresourcemanager.v3.resources.CloudResourceManagerResource: ...
@overload
def build(
    serviceName: Literal["cloudscheduler"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudscheduler.v1beta1.resources.CloudSchedulerResource: ...
@overload
def build(
    serviceName: Literal["cloudscheduler"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudscheduler.v1.resources.CloudSchedulerResource: ...
@overload
def build(
    serviceName: Literal["cloudsearch"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudsearch.v1.resources.CloudSearchResource: ...
@overload
def build(
    serviceName: Literal["cloudshell"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudshell.v1alpha1.resources.CloudShellResource: ...
@overload
def build(
    serviceName: Literal["cloudshell"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudshell.v1.resources.CloudShellResource: ...
@overload
def build(
    serviceName: Literal["cloudtasks"],
    version: Literal["v2beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudtasks.v2beta2.resources.CloudTasksResource: ...
@overload
def build(
    serviceName: Literal["cloudtasks"],
    version: Literal["v2beta3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudtasks.v2beta3.resources.CloudTasksResource: ...
@overload
def build(
    serviceName: Literal["cloudtasks"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudtasks.v2.resources.CloudTasksResource: ...
@overload
def build(
    serviceName: Literal["cloudtrace"],
    version: Literal["v2beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudtrace.v2beta1.resources.CloudTraceResource: ...
@overload
def build(
    serviceName: Literal["cloudtrace"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudtrace.v1.resources.CloudTraceResource: ...
@overload
def build(
    serviceName: Literal["cloudtrace"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.cloudtrace.v2.resources.CloudTraceResource: ...
@overload
def build(
    serviceName: Literal["composer"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.composer.v1beta1.resources.CloudComposerResource: ...
@overload
def build(
    serviceName: Literal["composer"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.composer.v1.resources.CloudComposerResource: ...
@overload
def build(
    serviceName: Literal["compute"],
    version: Literal["alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.compute.alpha.resources.ComputeResource: ...
@overload
def build(
    serviceName: Literal["compute"],
    version: Literal["beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.compute.beta.resources.ComputeResource: ...
@overload
def build(
    serviceName: Literal["compute"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.compute.v1.resources.ComputeResource: ...
@overload
def build(
    serviceName: Literal["container"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.container.v1beta1.resources.ContainerResource: ...
@overload
def build(
    serviceName: Literal["container"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.container.v1.resources.ContainerResource: ...
@overload
def build(
    serviceName: Literal["containeranalysis"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.containeranalysis.v1alpha1.resources.ContainerAnalysisResource: ...
@overload
def build(
    serviceName: Literal["containeranalysis"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.containeranalysis.v1beta1.resources.ContainerAnalysisResource: ...
@overload
def build(
    serviceName: Literal["content"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.content.v2.resources.ShoppingContentResource: ...
@overload
def build(
    serviceName: Literal["content"],
    version: Literal["v2_1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.content.v2_1.resources.ShoppingContentResource: ...
@overload
def build(
    serviceName: Literal["customsearch"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.customsearch.v1.resources.CustomSearchAPIResource: ...
@overload
def build(
    serviceName: Literal["datacatalog"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.datacatalog.v1beta1.resources.DataCatalogResource: ...
@overload
def build(
    serviceName: Literal["dataflow"],
    version: Literal["v1b3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dataflow.v1b3.resources.DataflowResource: ...
@overload
def build(
    serviceName: Literal["datafusion"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.datafusion.v1beta1.resources.DataFusionResource: ...
@overload
def build(
    serviceName: Literal["datafusion"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.datafusion.v1.resources.DataFusionResource: ...
@overload
def build(
    serviceName: Literal["datalabeling"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.datalabeling.v1beta1.resources.DataLabelingResource: ...
@overload
def build(
    serviceName: Literal["datamigration"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.datamigration.v1beta1.resources.DatabaseMigrationServiceResource: ...
@overload
def build(
    serviceName: Literal["dataproc"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dataproc.v1beta2.resources.DataprocResource: ...
@overload
def build(
    serviceName: Literal["dataproc"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dataproc.v1.resources.DataprocResource: ...
@overload
def build(
    serviceName: Literal["datastore"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.datastore.v1beta1.resources.DatastoreResource: ...
@overload
def build(
    serviceName: Literal["datastore"],
    version: Literal["v1beta3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.datastore.v1beta3.resources.DatastoreResource: ...
@overload
def build(
    serviceName: Literal["datastore"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.datastore.v1.resources.DatastoreResource: ...
@overload
def build(
    serviceName: Literal["deploymentmanager"],
    version: Literal["alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.deploymentmanager.alpha.resources.DeploymentManagerResource: ...
@overload
def build(
    serviceName: Literal["deploymentmanager"],
    version: Literal["v2beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.deploymentmanager.v2beta.resources.DeploymentManagerResource: ...
@overload
def build(
    serviceName: Literal["deploymentmanager"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.deploymentmanager.v2.resources.DeploymentManagerResource: ...
@overload
def build(
    serviceName: Literal["dfareporting"],
    version: Literal["v3_3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dfareporting.v3_3.resources.DfareportingResource: ...
@overload
def build(
    serviceName: Literal["dfareporting"],
    version: Literal["v3_4"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dfareporting.v3_4.resources.DfareportingResource: ...
@overload
def build(
    serviceName: Literal["dialogflow"],
    version: Literal["v2beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dialogflow.v2beta1.resources.DialogflowResource: ...
@overload
def build(
    serviceName: Literal["dialogflow"],
    version: Literal["v3beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dialogflow.v3beta1.resources.DialogflowResource: ...
@overload
def build(
    serviceName: Literal["dialogflow"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dialogflow.v2.resources.DialogflowResource: ...
@overload
def build(
    serviceName: Literal["dialogflow"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dialogflow.v3.resources.DialogflowResource: ...
@overload
def build(
    serviceName: Literal["digitalassetlinks"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.digitalassetlinks.v1.resources.DigitalassetlinksResource: ...
@overload
def build(
    serviceName: Literal["discovery"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.discovery.v1.resources.DiscoveryResource: ...
@overload
def build(
    serviceName: Literal["displayvideo"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.displayvideo.v1.resources.DisplayVideoResource: ...
@overload
def build(
    serviceName: Literal["dlp"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dlp.v2.resources.DLPResource: ...
@overload
def build(
    serviceName: Literal["dns"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dns.v1beta2.resources.DnsResource: ...
@overload
def build(
    serviceName: Literal["dns"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.dns.v1.resources.DnsResource: ...
@overload
def build(
    serviceName: Literal["docs"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.docs.v1.resources.DocsResource: ...
@overload
def build(
    serviceName: Literal["documentai"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.documentai.v1beta2.resources.DocumentResource: ...
@overload
def build(
    serviceName: Literal["documentai"],
    version: Literal["v1beta3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.documentai.v1beta3.resources.DocumentResource: ...
@overload
def build(
    serviceName: Literal["domains"],
    version: Literal["v1alpha2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.domains.v1alpha2.resources.CloudDomainsResource: ...
@overload
def build(
    serviceName: Literal["domains"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.domains.v1beta1.resources.CloudDomainsResource: ...
@overload
def build(
    serviceName: Literal["domainsrdap"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.domainsrdap.v1.resources.DomainsRDAPResource: ...
@overload
def build(
    serviceName: Literal["doubleclickbidmanager"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.doubleclickbidmanager.v1.resources.DoubleClickBidManagerResource: ...
@overload
def build(
    serviceName: Literal["doubleclickbidmanager"],
    version: Literal["v1_1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.doubleclickbidmanager.v1_1.resources.DoubleClickBidManagerResource: ...
@overload
def build(
    serviceName: Literal["doubleclicksearch"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.doubleclicksearch.v2.resources.DoubleclicksearchResource: ...
@overload
def build(
    serviceName: Literal["drive"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.drive.v2.resources.DriveResource: ...
@overload
def build(
    serviceName: Literal["drive"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.drive.v3.resources.DriveResource: ...
@overload
def build(
    serviceName: Literal["driveactivity"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.driveactivity.v2.resources.DriveActivityResource: ...
@overload
def build(
    serviceName: Literal["eventarc"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.eventarc.v1beta1.resources.EventarcResource: ...
@overload
def build(
    serviceName: Literal["eventarc"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.eventarc.v1.resources.EventarcResource: ...
@overload
def build(
    serviceName: Literal["factchecktools"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.factchecktools.v1alpha1.resources.FactCheckToolsResource: ...
@overload
def build(
    serviceName: Literal["fcm"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.fcm.v1.resources.FirebaseCloudMessagingResource: ...
@overload
def build(
    serviceName: Literal["file"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.file.v1beta1.resources.CloudFilestoreResource: ...
@overload
def build(
    serviceName: Literal["file"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.file.v1.resources.CloudFilestoreResource: ...
@overload
def build(
    serviceName: Literal["firebase"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firebase.v1beta1.resources.FirebaseManagementResource: ...
@overload
def build(
    serviceName: Literal["firebasedatabase"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firebasedatabase.v1beta.resources.FirebaseRealtimeDatabaseResource: ...
@overload
def build(
    serviceName: Literal["firebasedynamiclinks"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firebasedynamiclinks.v1.resources.FirebaseDynamicLinksResource: ...
@overload
def build(
    serviceName: Literal["firebasehosting"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firebasehosting.v1beta1.resources.FirebaseHostingResource: ...
@overload
def build(
    serviceName: Literal["firebasehosting"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firebasehosting.v1.resources.FirebaseHostingResource: ...
@overload
def build(
    serviceName: Literal["firebaseml"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firebaseml.v1beta2.resources.FirebaseMLResource: ...
@overload
def build(
    serviceName: Literal["firebaseml"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firebaseml.v1.resources.FirebaseMLResource: ...
@overload
def build(
    serviceName: Literal["firebaserules"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firebaserules.v1.resources.FirebaseRulesResource: ...
@overload
def build(
    serviceName: Literal["firestore"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firestore.v1beta1.resources.FirestoreResource: ...
@overload
def build(
    serviceName: Literal["firestore"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firestore.v1beta2.resources.FirestoreResource: ...
@overload
def build(
    serviceName: Literal["firestore"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.firestore.v1.resources.FirestoreResource: ...
@overload
def build(
    serviceName: Literal["fitness"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.fitness.v1.resources.FitnessResource: ...
@overload
def build(
    serviceName: Literal["games"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.games.v1.resources.GamesResource: ...
@overload
def build(
    serviceName: Literal["gamesConfiguration"],
    version: Literal["v1configuration"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.gamesConfiguration.v1configuration.resources.GamesConfigurationResource: ...
@overload
def build(
    serviceName: Literal["gamesManagement"],
    version: Literal["v1management"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.gamesManagement.v1management.resources.GamesManagementResource: ...
@overload
def build(
    serviceName: Literal["gameservices"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.gameservices.v1beta.resources.GameServicesResource: ...
@overload
def build(
    serviceName: Literal["gameservices"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.gameservices.v1.resources.GameServicesResource: ...
@overload
def build(
    serviceName: Literal["genomics"],
    version: Literal["v1alpha2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.genomics.v1alpha2.resources.GenomicsResource: ...
@overload
def build(
    serviceName: Literal["genomics"],
    version: Literal["v2alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.genomics.v2alpha1.resources.GenomicsResource: ...
@overload
def build(
    serviceName: Literal["genomics"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.genomics.v1.resources.GenomicsResource: ...
@overload
def build(
    serviceName: Literal["gmail"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.gmail.v1.resources.GmailResource: ...
@overload
def build(
    serviceName: Literal["gmailpostmastertools"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.gmailpostmastertools.v1beta1.resources.PostmasterToolsResource: ...
@overload
def build(
    serviceName: Literal["gmailpostmastertools"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.gmailpostmastertools.v1.resources.PostmasterToolsResource: ...
@overload
def build(
    serviceName: Literal["groupsmigration"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.groupsmigration.v1.resources.GroupsMigrationResource: ...
@overload
def build(
    serviceName: Literal["groupssettings"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.groupssettings.v1.resources.GroupssettingsResource: ...
@overload
def build(
    serviceName: Literal["healthcare"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.healthcare.v1beta1.resources.CloudHealthcareResource: ...
@overload
def build(
    serviceName: Literal["healthcare"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.healthcare.v1.resources.CloudHealthcareResource: ...
@overload
def build(
    serviceName: Literal["homegraph"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.homegraph.v1.resources.HomeGraphServiceResource: ...
@overload
def build(
    serviceName: Literal["iam"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.iam.v1.resources.IamResource: ...
@overload
def build(
    serviceName: Literal["iamcredentials"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.iamcredentials.v1.resources.IAMCredentialsResource: ...
@overload
def build(
    serviceName: Literal["iap"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.iap.v1beta1.resources.CloudIAPResource: ...
@overload
def build(
    serviceName: Literal["iap"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.iap.v1.resources.CloudIAPResource: ...
@overload
def build(
    serviceName: Literal["identitytoolkit"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.identitytoolkit.v3.resources.IdentityToolkitResource: ...
@overload
def build(
    serviceName: Literal["indexing"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.indexing.v3.resources.IndexingResource: ...
@overload
def build(
    serviceName: Literal["jobs"],
    version: Literal["v3p1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.jobs.v3p1beta1.resources.CloudTalentSolutionResource: ...
@overload
def build(
    serviceName: Literal["jobs"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.jobs.v3.resources.CloudTalentSolutionResource: ...
@overload
def build(
    serviceName: Literal["jobs"],
    version: Literal["v4"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.jobs.v4.resources.CloudTalentSolutionResource: ...
@overload
def build(
    serviceName: Literal["kgsearch"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.kgsearch.v1.resources.KgsearchResource: ...
@overload
def build(
    serviceName: Literal["language"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.language.v1beta1.resources.CloudNaturalLanguageResource: ...
@overload
def build(
    serviceName: Literal["language"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.language.v1beta2.resources.CloudNaturalLanguageResource: ...
@overload
def build(
    serviceName: Literal["language"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.language.v1.resources.CloudNaturalLanguageResource: ...
@overload
def build(
    serviceName: Literal["libraryagent"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.libraryagent.v1.resources.LibraryagentResource: ...
@overload
def build(
    serviceName: Literal["licensing"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.licensing.v1.resources.LicensingResource: ...
@overload
def build(
    serviceName: Literal["lifesciences"],
    version: Literal["v2beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.lifesciences.v2beta.resources.CloudLifeSciencesResource: ...
@overload
def build(
    serviceName: Literal["localservices"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.localservices.v1.resources.LocalservicesResource: ...
@overload
def build(
    serviceName: Literal["logging"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.logging.v2.resources.LoggingResource: ...
@overload
def build(
    serviceName: Literal["managedidentities"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.managedidentities.v1alpha1.resources.ManagedServiceForMicrosoftActiveDirectoryConsumerAPIResource: ...
@overload
def build(
    serviceName: Literal["managedidentities"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.managedidentities.v1beta1.resources.ManagedServiceForMicrosoftActiveDirectoryConsumerAPIResource: ...
@overload
def build(
    serviceName: Literal["managedidentities"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.managedidentities.v1.resources.ManagedServiceForMicrosoftActiveDirectoryConsumerAPIResource: ...
@overload
def build(
    serviceName: Literal["manufacturers"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.manufacturers.v1.resources.ManufacturerCenterResource: ...
@overload
def build(
    serviceName: Literal["memcache"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.memcache.v1beta2.resources.CloudMemorystoreForMemcachedResource: ...
@overload
def build(
    serviceName: Literal["memcache"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.memcache.v1.resources.CloudMemorystoreForMemcachedResource: ...
@overload
def build(
    serviceName: Literal["metastore"],
    version: Literal["v1alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.metastore.v1alpha.resources.DataprocMetastoreResource: ...
@overload
def build(
    serviceName: Literal["metastore"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.metastore.v1beta.resources.DataprocMetastoreResource: ...
@overload
def build(
    serviceName: Literal["ml"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.ml.v1.resources.CloudMachineLearningEngineResource: ...
@overload
def build(
    serviceName: Literal["monitoring"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.monitoring.v1.resources.MonitoringResource: ...
@overload
def build(
    serviceName: Literal["monitoring"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.monitoring.v3.resources.MonitoringResource: ...
@overload
def build(
    serviceName: Literal["mybusinessaccountmanagement"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.mybusinessaccountmanagement.v1.resources.MyBusinessAccountManagementResource: ...
@overload
def build(
    serviceName: Literal["networkconnectivity"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.networkconnectivity.v1alpha1.resources.NetworkconnectivityResource: ...
@overload
def build(
    serviceName: Literal["networkmanagement"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.networkmanagement.v1beta1.resources.NetworkManagementResource: ...
@overload
def build(
    serviceName: Literal["networkmanagement"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.networkmanagement.v1.resources.NetworkManagementResource: ...
@overload
def build(
    serviceName: Literal["notebooks"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.notebooks.v1.resources.AIPlatformNotebooksResource: ...
@overload
def build(
    serviceName: Literal["oauth2"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.oauth2.v2.resources.Oauth2Resource: ...
@overload
def build(
    serviceName: Literal["ondemandscanning"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.ondemandscanning.v1beta1.resources.OnDemandScanningResource: ...
@overload
def build(
    serviceName: Literal["osconfig"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.osconfig.v1beta.resources.OSConfigResource: ...
@overload
def build(
    serviceName: Literal["osconfig"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.osconfig.v1.resources.OSConfigResource: ...
@overload
def build(
    serviceName: Literal["oslogin"],
    version: Literal["v1alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.oslogin.v1alpha.resources.CloudOSLoginResource: ...
@overload
def build(
    serviceName: Literal["oslogin"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.oslogin.v1beta.resources.CloudOSLoginResource: ...
@overload
def build(
    serviceName: Literal["oslogin"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.oslogin.v1.resources.CloudOSLoginResource: ...
@overload
def build(
    serviceName: Literal["pagespeedonline"],
    version: Literal["v5"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.pagespeedonline.v5.resources.PagespeedInsightsResource: ...
@overload
def build(
    serviceName: Literal["people"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.people.v1.resources.PeopleServiceResource: ...
@overload
def build(
    serviceName: Literal["playablelocations"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.playablelocations.v3.resources.PlayableLocationsResource: ...
@overload
def build(
    serviceName: Literal["playcustomapp"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.playcustomapp.v1.resources.PlaycustomappResource: ...
@overload
def build(
    serviceName: Literal["policysimulator"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.policysimulator.v1beta1.resources.PolicySimulatorResource: ...
@overload
def build(
    serviceName: Literal["policytroubleshooter"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.policytroubleshooter.v1beta.resources.PolicyTroubleshooterResource: ...
@overload
def build(
    serviceName: Literal["policytroubleshooter"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.policytroubleshooter.v1.resources.PolicyTroubleshooterResource: ...
@overload
def build(
    serviceName: Literal["poly"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.poly.v1.resources.PolyServiceResource: ...
@overload
def build(
    serviceName: Literal["privateca"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.privateca.v1beta1.resources.CertificateAuthorityServiceResource: ...
@overload
def build(
    serviceName: Literal["prod_tt_sasportal"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.prod_tt_sasportal.v1alpha1.resources.SASPortalTestingResource: ...
@overload
def build(
    serviceName: Literal["pubsub"],
    version: Literal["v1beta1a"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.pubsub.v1beta1a.resources.PubsubResource: ...
@overload
def build(
    serviceName: Literal["pubsub"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.pubsub.v1beta2.resources.PubsubResource: ...
@overload
def build(
    serviceName: Literal["pubsub"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.pubsub.v1.resources.PubsubResource: ...
@overload
def build(
    serviceName: Literal["pubsublite"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.pubsublite.v1.resources.PubsubLiteResource: ...
@overload
def build(
    serviceName: Literal["realtimebidding"],
    version: Literal["v1alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.realtimebidding.v1alpha.resources.RealTimeBiddingResource: ...
@overload
def build(
    serviceName: Literal["realtimebidding"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.realtimebidding.v1.resources.RealTimeBiddingResource: ...
@overload
def build(
    serviceName: Literal["recommendationengine"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.recommendationengine.v1beta1.resources.RecommendationsAIResource: ...
@overload
def build(
    serviceName: Literal["recommender"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.recommender.v1beta1.resources.RecommenderResource: ...
@overload
def build(
    serviceName: Literal["recommender"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.recommender.v1.resources.RecommenderResource: ...
@overload
def build(
    serviceName: Literal["redis"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.redis.v1beta1.resources.CloudRedisResource: ...
@overload
def build(
    serviceName: Literal["redis"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.redis.v1.resources.CloudRedisResource: ...
@overload
def build(
    serviceName: Literal["remotebuildexecution"],
    version: Literal["v1alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.remotebuildexecution.v1alpha.resources.RemoteBuildExecutionResource: ...
@overload
def build(
    serviceName: Literal["remotebuildexecution"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.remotebuildexecution.v1.resources.RemoteBuildExecutionResource: ...
@overload
def build(
    serviceName: Literal["remotebuildexecution"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.remotebuildexecution.v2.resources.RemoteBuildExecutionResource: ...
@overload
def build(
    serviceName: Literal["reseller"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.reseller.v1.resources.ResellerResource: ...
@overload
def build(
    serviceName: Literal["retail"],
    version: Literal["v2alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.retail.v2alpha.resources.CloudRetailResource: ...
@overload
def build(
    serviceName: Literal["retail"],
    version: Literal["v2beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.retail.v2beta.resources.CloudRetailResource: ...
@overload
def build(
    serviceName: Literal["retail"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.retail.v2.resources.CloudRetailResource: ...
@overload
def build(
    serviceName: Literal["run"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.run.v1alpha1.resources.CloudRunResource: ...
@overload
def build(
    serviceName: Literal["run"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.run.v1.resources.CloudRunResource: ...
@overload
def build(
    serviceName: Literal["runtimeconfig"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.runtimeconfig.v1beta1.resources.CloudRuntimeConfigResource: ...
@overload
def build(
    serviceName: Literal["runtimeconfig"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.runtimeconfig.v1.resources.CloudRuntimeConfigResource: ...
@overload
def build(
    serviceName: Literal["safebrowsing"],
    version: Literal["v4"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.safebrowsing.v4.resources.SafebrowsingResource: ...
@overload
def build(
    serviceName: Literal["sasportal"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.sasportal.v1alpha1.resources.SasportalResource: ...
@overload
def build(
    serviceName: Literal["script"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.script.v1.resources.ScriptResource: ...
@overload
def build(
    serviceName: Literal["searchconsole"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.searchconsole.v1.resources.SearchConsoleResource: ...
@overload
def build(
    serviceName: Literal["secretmanager"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.secretmanager.v1beta1.resources.SecretManagerResource: ...
@overload
def build(
    serviceName: Literal["secretmanager"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.secretmanager.v1.resources.SecretManagerResource: ...
@overload
def build(
    serviceName: Literal["securitycenter"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.securitycenter.v1beta1.resources.SecurityCommandCenterResource: ...
@overload
def build(
    serviceName: Literal["securitycenter"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.securitycenter.v1beta2.resources.SecurityCommandCenterResource: ...
@overload
def build(
    serviceName: Literal["securitycenter"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.securitycenter.v1.resources.SecurityCommandCenterResource: ...
@overload
def build(
    serviceName: Literal["serviceconsumermanagement"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.serviceconsumermanagement.v1beta1.resources.ServiceConsumerManagementResource: ...
@overload
def build(
    serviceName: Literal["serviceconsumermanagement"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.serviceconsumermanagement.v1.resources.ServiceConsumerManagementResource: ...
@overload
def build(
    serviceName: Literal["servicecontrol"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.servicecontrol.v1.resources.ServiceControlResource: ...
@overload
def build(
    serviceName: Literal["servicecontrol"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.servicecontrol.v2.resources.ServiceControlResource: ...
@overload
def build(
    serviceName: Literal["servicedirectory"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.servicedirectory.v1beta1.resources.ServiceDirectoryResource: ...
@overload
def build(
    serviceName: Literal["servicedirectory"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.servicedirectory.v1.resources.ServiceDirectoryResource: ...
@overload
def build(
    serviceName: Literal["servicemanagement"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.servicemanagement.v1.resources.ServiceManagementResource: ...
@overload
def build(
    serviceName: Literal["servicenetworking"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.servicenetworking.v1beta.resources.ServiceNetworkingResource: ...
@overload
def build(
    serviceName: Literal["servicenetworking"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.servicenetworking.v1.resources.ServiceNetworkingResource: ...
@overload
def build(
    serviceName: Literal["serviceusage"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.serviceusage.v1beta1.resources.ServiceUsageResource: ...
@overload
def build(
    serviceName: Literal["serviceusage"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.serviceusage.v1.resources.ServiceUsageResource: ...
@overload
def build(
    serviceName: Literal["sheets"],
    version: Literal["v4"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.sheets.v4.resources.SheetsResource: ...
@overload
def build(
    serviceName: Literal["siteVerification"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.siteVerification.v1.resources.SiteVerificationResource: ...
@overload
def build(
    serviceName: Literal["slides"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.slides.v1.resources.SlidesResource: ...
@overload
def build(
    serviceName: Literal["smartdevicemanagement"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.smartdevicemanagement.v1.resources.SmartDeviceManagementResource: ...
@overload
def build(
    serviceName: Literal["sourcerepo"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.sourcerepo.v1.resources.CloudSourceRepositoriesResource: ...
@overload
def build(
    serviceName: Literal["spanner"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.spanner.v1.resources.SpannerResource: ...
@overload
def build(
    serviceName: Literal["speech"],
    version: Literal["v1p1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.speech.v1p1beta1.resources.SpeechResource: ...
@overload
def build(
    serviceName: Literal["speech"],
    version: Literal["v2beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.speech.v2beta1.resources.SpeechResource: ...
@overload
def build(
    serviceName: Literal["speech"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.speech.v1.resources.SpeechResource: ...
@overload
def build(
    serviceName: Literal["sqladmin"],
    version: Literal["v1beta4"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.sqladmin.v1beta4.resources.SQLAdminResource: ...
@overload
def build(
    serviceName: Literal["storage"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.storage.v1.resources.StorageResource: ...
@overload
def build(
    serviceName: Literal["storagetransfer"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.storagetransfer.v1.resources.StoragetransferResource: ...
@overload
def build(
    serviceName: Literal["streetviewpublish"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.streetviewpublish.v1.resources.StreetViewPublishResource: ...
@overload
def build(
    serviceName: Literal["sts"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.sts.v1beta.resources.CloudSecurityTokenResource: ...
@overload
def build(
    serviceName: Literal["sts"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.sts.v1.resources.CloudSecurityTokenResource: ...
@overload
def build(
    serviceName: Literal["tagmanager"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.tagmanager.v1.resources.TagManagerResource: ...
@overload
def build(
    serviceName: Literal["tagmanager"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.tagmanager.v2.resources.TagManagerResource: ...
@overload
def build(
    serviceName: Literal["tasks"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.tasks.v1.resources.TasksResource: ...
@overload
def build(
    serviceName: Literal["testing"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.testing.v1.resources.TestingResource: ...
@overload
def build(
    serviceName: Literal["texttospeech"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.texttospeech.v1beta1.resources.TexttospeechResource: ...
@overload
def build(
    serviceName: Literal["texttospeech"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.texttospeech.v1.resources.TexttospeechResource: ...
@overload
def build(
    serviceName: Literal["toolresults"],
    version: Literal["v1beta3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.toolresults.v1beta3.resources.ToolResultsResource: ...
@overload
def build(
    serviceName: Literal["tpu"],
    version: Literal["v1alpha1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.tpu.v1alpha1.resources.TPUResource: ...
@overload
def build(
    serviceName: Literal["tpu"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.tpu.v1.resources.TPUResource: ...
@overload
def build(
    serviceName: Literal["trafficdirector"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.trafficdirector.v2.resources.TrafficDirectorServiceResource: ...
@overload
def build(
    serviceName: Literal["transcoder"],
    version: Literal["v1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.transcoder.v1beta1.resources.TranscoderResource: ...
@overload
def build(
    serviceName: Literal["translate"],
    version: Literal["v3beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.translate.v3beta1.resources.TranslateResource: ...
@overload
def build(
    serviceName: Literal["translate"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.translate.v2.resources.TranslateResource: ...
@overload
def build(
    serviceName: Literal["translate"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.translate.v3.resources.TranslateResource: ...
@overload
def build(
    serviceName: Literal["vault"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.vault.v1.resources.VaultResource: ...
@overload
def build(
    serviceName: Literal["vectortile"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.vectortile.v1.resources.SemanticTileResource: ...
@overload
def build(
    serviceName: Literal["verifiedaccess"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.verifiedaccess.v1.resources.VerifiedaccessResource: ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1p1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.videointelligence.v1p1beta1.resources.CloudVideoIntelligenceResource: ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1p2beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.videointelligence.v1p2beta1.resources.CloudVideoIntelligenceResource: ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1p3beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.videointelligence.v1p3beta1.resources.CloudVideoIntelligenceResource: ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1beta2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.videointelligence.v1beta2.resources.CloudVideoIntelligenceResource: ...
@overload
def build(
    serviceName: Literal["videointelligence"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.videointelligence.v1.resources.CloudVideoIntelligenceResource: ...
@overload
def build(
    serviceName: Literal["vision"],
    version: Literal["v1p1beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.vision.v1p1beta1.resources.VisionResource: ...
@overload
def build(
    serviceName: Literal["vision"],
    version: Literal["v1p2beta1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.vision.v1p2beta1.resources.VisionResource: ...
@overload
def build(
    serviceName: Literal["vision"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.vision.v1.resources.VisionResource: ...
@overload
def build(
    serviceName: Literal["webfonts"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.webfonts.v1.resources.WebfontsResource: ...
@overload
def build(
    serviceName: Literal["webmasters"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.webmasters.v3.resources.WebmastersResource: ...
@overload
def build(
    serviceName: Literal["webrisk"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.webrisk.v1.resources.WebRiskResource: ...
@overload
def build(
    serviceName: Literal["websecurityscanner"],
    version: Literal["v1alpha"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.websecurityscanner.v1alpha.resources.WebSecurityScannerResource: ...
@overload
def build(
    serviceName: Literal["websecurityscanner"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.websecurityscanner.v1beta.resources.WebSecurityScannerResource: ...
@overload
def build(
    serviceName: Literal["websecurityscanner"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.websecurityscanner.v1.resources.WebSecurityScannerResource: ...
@overload
def build(
    serviceName: Literal["workflowexecutions"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.workflowexecutions.v1beta.resources.WorkflowExecutionsResource: ...
@overload
def build(
    serviceName: Literal["workflowexecutions"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.workflowexecutions.v1.resources.WorkflowExecutionsResource: ...
@overload
def build(
    serviceName: Literal["workflows"],
    version: Literal["v1beta"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.workflows.v1beta.resources.WorkflowsResource: ...
@overload
def build(
    serviceName: Literal["workflows"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.workflows.v1.resources.WorkflowsResource: ...
@overload
def build(
    serviceName: Literal["youtube"],
    version: Literal["v3"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.youtube.v3.resources.YouTubeResource: ...
@overload
def build(
    serviceName: Literal["youtubeAnalytics"],
    version: Literal["v2"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.youtubeAnalytics.v2.resources.YouTubeAnalyticsResource: ...
@overload
def build(
    serviceName: Literal["youtubereporting"],
    version: Literal["v1"],
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> googleapiclient._apis.youtubereporting.v1.resources.YouTubeReportingResource: ...
@overload
def build(
    serviceName: str,
    version: str,
    http: Optional[Union[httplib2.Http, HttpMock]] = ...,
    discoveryServiceUrl: str = ...,
    developerKey: Optional[str] = ...,
    model: Optional[Model] = ...,
    requestBuilder: HttpRequest = ...,
    credentials: Optional[
        Union[oauth2client.Credentials, google.auth.credentials.Credentials]
    ] = ...,
    cache_discovery: bool = ...,
    cache: Optional[Cache] = ...,
    client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    adc_cert_path: Optional[str] = ...,
    adc_key_path: Optional[str] = ...,
    num_retries: int = ...,
) -> Resource: ...
