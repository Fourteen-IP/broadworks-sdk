# Auto-generated file
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List

from broadworks_sdk.commands.base_command import OCIDataResponse
from broadworks_sdk.commands.oci_types import *  # noqa: F403


@dataclass
class AuthenticationResponse(OCIDataResponse):
    """
    AuthenticationRequest() Response is 1st stage of the 2 stage OCI login process.
    """

    userId: str

    nonce: str

    passwordAlgorithm: str


@dataclass
class AuthenticationVerifyResponse22V4(OCIDataResponse):
    """Response to AuthenticationVerifyRequest22V4

    The following data elements are only returned in AS data mode:
      resellerId

    If a phoneNumber is returned, it will be the primary DN of the user.

    The parameter tokenRevocationTime is represented in the number of milliseconds
    since January 1, 1970, 00:00:00 GMT, and it is set to the more current time between
    the system level token revocation time and user level token revocation time."""

    loginType: str

    locale: str

    encoding: str

    isEnterprise: bool

    userId: str

    groupId: Optional[str] = None

    serviceProviderId: Optional[str] = None

    passwordExpiresDays: Optional[int] = None

    lastName: Optional[str] = None

    firstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    resellerId: Optional[str] = None

    tokenRevocationTime: Optional[int] = None


@dataclass
class DeviceManagementFileAuthLocationGetResponse22V4(OCIDataResponse):
    """This is a response to DeviceManagementFileAuthLocationGetRequest22V4.
    Return the address and credentials of the File Repository hosting the requested access device file.
    Also return the file name and path on the File Repository.
    Also returns the status of the file authentication."""

    fileRepositoryUserName: str

    fileRepositoryPassword: str

    fileReposAccessToken: str

    netAddress: str

    remoteFileFormat: str

    status: Optional[str] = None

    portNumber: Optional[int] = None

    rootDirectory: Optional[str] = None

    cpeFileDirectory: Optional[str] = None

    secure: Optional[bool] = None

    macInNonRequestURI: Optional[bool] = None

    macInCert: Optional[bool] = None

    macFormatInNonRequestURI: Optional[str] = None

    useHttpDigestAuthentication: Optional[bool] = None

    macBasedFileAuthentication: Optional[bool] = None

    userNamePasswordFileAuthentication: Optional[bool] = None

    completionNotification: Optional[bool] = None

    fileCategory: Optional[str] = None

    enableCaching: Optional[bool] = None

    notifyFileUpload: Optional[bool] = None


@dataclass
class EnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAssignmentListResponse(
    OCIDataResponse
):
    """Response to EnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAssignmentListRequest.
    The response contains a table with columns: \"Mobile Number\", \"User Id\",
    \"Last Name\", \"First Name\",\"Phone Number\",\"Extension\", \"Group Id\", \"Department\" and \"Mobile Network\".
    The \"Mobile Number\" column contains a single DN.
    The \"User Id\", \"Last Name\" and \"First Name\" columns contains the corresponding attributes of the user possessing the DN(s).
    The \"Phone Number\" column contains a single DN.
    The \"Group Id\"   column contains the Group Id of the user.
    The \"Department\" column contains the department of the user if it is part of a department.
    The \"Mobile Network\" column contains the Mobile Network the number belongs to."""

    mobileSubscriberDirectoryNumbersAssignmentTable: OCITable


@dataclass
class EnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAssignmentPagedSortedListResponse22(
    OCIDataResponse
):
    """Response to EnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAssignmentPagedSortedListRequest22.
    The response contains the number of entries that would be returned if the response was not page size restricted.
    Contains a table with columns: \"Mobile Number\", \"User Id\", \"Last Name\", \"First Name\", \"Phone Number\", \"Extension\",
    \"Group Id\", \"Department\", \"Department Type\", \"Parent Department\", \"Parent Department Type\", \"Mobile Network\", \"Country Code\",
    \"National Prefix\", \"Available\", \"Mobile Country Code\", \"Mobile National Prefix\".
    The \"Mobile Number\" column contains a single DN.
    The \"User Id\", \"Last Name\" and \"First Name\" columns contains the corresponding attributes of the user possessing the DN(s).
    The \"Phone Number\" column contains a single DN.
    The \"Group Id\" column contains the Group Id of the user.
    The \"Group Name\" column contains the Group Name of the user.
    The \"Department\" column contains the department of the user if it is part of a department.
    The \"Parent Department\" column contains the parent department of the user if it is part of a department.
    The \"Department Type\" and \"Parent Department Type\" columns will contain the values \"Enterprise\" or \"Group\".
    The \"Mobile Network\" column contains the Mobile Network the number belongs to.
    The \"Country Code\" column indicates the dialing prefix for the phone number.
    The \"National Prefix\" column indicates the digit sequence to be dialed before the telephone number.
    The \"Available\" column indicates if the Mobile Number is available.
    The \"Mobile Country Code\" column indicates the dialing prefix for the mobile number.
    The \"Mobile National Prefix\" column indicates the digit sequence to be dialed before the mobile number."""

    mobileSubscriberDirectoryNumbersAssignmentTable: OCITable

    totalNumberOfRows: Optional[int] = None


@dataclass
class EnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAvailableListResponse22(
    OCIDataResponse
):
    """Response to EnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAvailableListRequest22.
    The response contains a table with columns: \"Phone Number\", \"E164 Phone Number\".

    The \"Phone Number\" column contains Mobile Subscriber DNs not yet assigned to any user.
    The \"E164 Phone Number\" column contains Mobile Subscriber DNs not yet assigned to any user in E.164 format."""

    availableMobileSubscriberDirectoryNumberTable: OCITable


@dataclass
class EnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAvailablePagedSortedListResponse22(
    OCIDataResponse
):
    """Response to EnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAvailablePagedSortedListRequest22.
    The response contains the number of entries that would be returned if the response was not page size restricted.
    Contains a table with columns: \"Mobile Number\", \"Mobile Network\", \"Mobile Country Code\", \"Mobile National Prefix\".
    The \"Mobile Number\" column contains a single DN.
    The \"Mobile Network\" column contains the Mobile Network the number belongs to.
    The \"Mobile Country Code\" column indicates the dialing prefix for the mobile number.
    The \"Mobile National Prefix\" column indicates the digit sequence to be dialed before the mobile number."""

    availableMobileSubscriberDirectoryNumberTable: OCITable

    totalNumberOfRows: Optional[int] = None


@dataclass
class EnterpriseCallCenterAgentThresholdDefaultProfileGetResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterAgentThresholdDefaultProfileGetRequest.
    The agent table contains the agents assigned to the profile and
    has column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\";"""

    profileName: str

    enableNotificationEmail: bool

    profileDescription: Optional[str] = None

    thresholdCurrentCallStateIdleTimeYellow: Optional[int] = None

    thresholdCurrentCallStateIdleTimeRed: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeYellow: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeRed: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeYellow: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeRed: Optional[int] = None

    thresholdAverageBusyInTimeYellow: Optional[int] = None

    thresholdAverageBusyInTimeRed: Optional[int] = None

    thresholdAverageBusyOutTimeYellow: Optional[int] = None

    thresholdAverageBusyOutTimeRed: Optional[int] = None

    thresholdAverageWrapUpTimeYellow: Optional[int] = None

    thresholdAverageWrapUpTimeRed: Optional[int] = None

    notificationEmailAddress: List[str] = field(default_factory=list)

    agentTable: Optional[OCITable] = None


@dataclass
class EnterpriseCallCenterAgentThresholdProfileGetAvailableAgentListResponse(
    OCIDataResponse
):
    """Response to the EnterpriseCallCenterAgentThresholdProfileGetAvailableAgentListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"Agent Threshold Profile\";"""

    agentTable: OCITable


@dataclass
class EnterpriseCallCenterAgentThresholdProfileGetAvailableAgentPagedSortedListResponse(
    OCIDataResponse
):
    """Response to the EnterpriseCallCenterAgentThresholdProfileGetAvailableAgentPagedSortedListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"Agent Threshold Profile\";"""

    agentTable: OCITable


@dataclass
class EnterpriseCallCenterAgentThresholdProfileGetListResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterAgentThresholdProfileGetListRequest.
    Contains a table with all the  Call Center Agent Threshold Profiles in the Enterprise.
    The column headings are: \"Default\", \"Name\", \"Description\"."""

    profilesTable: OCITable


@dataclass
class EnterpriseCallCenterAgentThresholdProfileGetPagedSortedResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterAgentThresholdProfileGetPagedSortedRequest.
    The agentTable contains the agents assigned to the profile and has the column headings:
    \"User Id\", \"Group Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\";"""

    enableNotificationEmail: bool

    agentTable: OCITable

    profileDescription: Optional[str] = None

    thresholdCurrentCallStateIdleTimeYellow: Optional[int] = None

    thresholdCurrentCallStateIdleTimeRed: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeYellow: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeRed: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeYellow: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeRed: Optional[int] = None

    thresholdAverageBusyInTimeYellow: Optional[int] = None

    thresholdAverageBusyInTimeRed: Optional[int] = None

    thresholdAverageBusyOutTimeYellow: Optional[int] = None

    thresholdAverageBusyOutTimeRed: Optional[int] = None

    thresholdAverageWrapUpTimeYellow: Optional[int] = None

    thresholdAverageWrapUpTimeRed: Optional[int] = None

    notificationEmailAddress: List[str] = field(default_factory=list)


@dataclass
class EnterpriseCallCenterAgentThresholdProfileGetResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterAgentThresholdProfileGetRequest.
    The agentTable contains the agents assigned to the profile and has the column headings:
    \"User Id\", \"Group Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\";"""

    enableNotificationEmail: bool

    agentTable: OCITable

    profileDescription: Optional[str] = None

    thresholdCurrentCallStateIdleTimeYellow: Optional[int] = None

    thresholdCurrentCallStateIdleTimeRed: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeYellow: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeRed: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeYellow: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeRed: Optional[int] = None

    thresholdAverageBusyInTimeYellow: Optional[int] = None

    thresholdAverageBusyInTimeRed: Optional[int] = None

    thresholdAverageBusyOutTimeYellow: Optional[int] = None

    thresholdAverageBusyOutTimeRed: Optional[int] = None

    thresholdAverageWrapUpTimeYellow: Optional[int] = None

    thresholdAverageWrapUpTimeRed: Optional[int] = None

    notificationEmailAddress: List[str] = field(default_factory=list)


@dataclass
class EnterpriseCallCenterAgentUnavailableCodeGetListResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterAgentUnavailableCodeGetListRequest.
    Contains a table with column headings: \"Is Active\", \"Code\", \"Description\"."""

    unavailableCodesTable: OCITable


@dataclass
class EnterpriseCallCenterAgentUnavailableCodeGetResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterAgentUnavailableCodeGetRequest"""

    isActive: bool

    description: Optional[str] = None


@dataclass
class EnterpriseCallCenterAgentUnavailableCodeSettingsGetResponse17sp4(OCIDataResponse):
    """Response to EnterpriseCallCenterAgentUnavailableCodeSettingsGetRequest17sp4."""

    enableAgentUnavailableCodes: bool

    forceUseOfAgentUnavailableCodes: bool

    defaultAgentUnavailableCodeOnDND: Optional[str] = None

    defaultAgentUnavailableCodeOnPersonalCalls: Optional[str] = None

    defaultAgentUnavailableCodeOnConsecutiveBounces: Optional[str] = None

    defaultAgentUnavailableCodeOnNotReachable: Optional[str] = None

    defaultAgentUnavailableCode: Optional[str] = None


@dataclass
class EnterpriseCallCenterCallDispositionCodeGetListResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterCallDispositionCodeGetListRequest.
    Contains a table with column headings: \"Is Active\", \"Code\", \"Description\"."""

    dispositionCodesTable: OCITable


@dataclass
class EnterpriseCallCenterCallDispositionCodeGetResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterCallDispositionCodeGetRequest"""

    isActive: bool

    description: Optional[str] = None


@dataclass
class EnterpriseCallCenterCallDispositionCodeGetUsageListResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterCallDispositionCodeGetUsageListRequest.
    The Type column contains either \"Call Center\" or \"Route Point\".
    Contains a table with column headings: \"Group Id\", \"Id\", \"Name\" and \"Type\"."""

    callCenterTable: OCITable


@dataclass
class EnterpriseCallCenterCurrentAndPastAgentGetListResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterCurrentAndPastAgentGetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    agentUserTable: OCITable

    deletedAgentUserTable: OCITable


@dataclass
class EnterpriseCallCenterCurrentAndPastCallCenterGetListResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterCurrentAndPastCallCenterGetListRequest."""

    serviceUserId: List[str] = field(default_factory=list)

    deletedServiceUserId: List[str] = field(default_factory=list)


@dataclass
class EnterpriseCallCenterCurrentAndPastDNISGetListResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterCurrentAndPastDNISGetListRequest."""

    name: List[str] = field(default_factory=list)

    deletedName: List[str] = field(default_factory=list)


@dataclass
class EnterpriseCallCenterEnhancedReportingBrandingGetResponse(OCIDataResponse):
    """Response to the EnterpriseCallCenterEnhancedReportingBrandingGetRequest."""

    brandingChoice: str

    brandingFileDescription: Optional[str] = None


@dataclass
class EnterpriseCallCenterEnhancedReportingGetAvailableReportTemplateListResponse(
    OCIDataResponse
):
    """Response to EnterpriseCallCenterEnhancedReportingGetAvailableReportTemplateListRequest.
    Contains a table with column headings: \"Name\", \"Description\" and \"Level\", \"Is Agent Required\",
    \"Is Call Center Required\", \"Is Call Center Dnis Required\", \"Is Real Time Report\", \"Is Sampling Period Required\",
    \"Call Completion Threshold Parameter\", \"Short Duration Threshold Parameter\",
    \"Service Level Threshold Parameter\", \"Service Level Inclusions Parameter\", \"Service Level Objective Threshold Parameter\",
    \"Abandoned Call Threshold Parameter\", \"Service Level Threshold Parameter Number\",
    \"Abandoned Call Threshold Parameter Number\" and \"Scope\".
    The possible values for \"Level\" are \"System\" and \"Enterprise\".
    The possible values for \"Is Agent Required\", \"Is Call Center Required\", \"Is Call Center Dnis Required\", \"Is Real Time Report\" and
    \"Is Sampling Period Required\" are \"true\" and \"false\".
    The possible values for \"Call Completion Threshold Parameter\", \"Short Duration Threshold Parameter\",
    \"Service Level Threshold Parameter\", \"Service Level Inclusions Parameter\", \"Service Level Objective Threshold Parameter\"
    and \"Abandoned Call Threshold Parameter\" are \"Required\", \"Hidden\" and \"Does Not Apply\".
    The possible values for \"Scope\" are \"Supervisor Only\" and \"Supervisor and Agent\"."""

    reportTemplateTable: OCITable


@dataclass
class EnterpriseCallCenterEnhancedReportingGetResponse19(OCIDataResponse):
    """Response to EnterpriseCallCenterEnhancedReportingGetRequest19."""

    reportingServer: str


@dataclass
class EnterpriseCallCenterEnhancedReportingReportTemplateGetListResponse(
    OCIDataResponse
):
    """Response to EnterpriseCallCenterEnhancedReportingReportTemplateGetListRequest.
    Contains a table with column headings: \"Name\", \"Description\", \"Type\" and \"Enabled\"."""

    reportTemplateTable: OCITable


@dataclass
class EnterpriseCallCenterEnhancedReportingReportTemplateGetResponse(OCIDataResponse):
    """Response to EnterpriseCallCenterEnhancedReportingReportTemplateGetRequest."""

    dataTemplate: str

    xsltTemplateDescription: str

    scope: str

    isEnabled: bool

    description: Optional[str] = None

    filterNumber: Optional[int] = None

    isRealtimeReport: Optional[bool] = None

    callCompletionThresholdParam: Optional[str] = None

    shortDurationThresholdParam: Optional[str] = None

    serviceLevelThresholdParam: Optional[str] = None

    serviceLevelInclusionsParam: Optional[str] = None

    serviceLevelObjectiveThresholdParam: Optional[str] = None

    abandonedCallThresholdParam: Optional[str] = None

    serviceLevelThresholdParamNumber: Optional[int] = None

    abandonedCallThresholdParamNumber: Optional[int] = None

    filterValue: List[str] = field(default_factory=list)


@dataclass
class EnterpriseCallCenterEnhancedReportingScheduledReportGetActiveListResponse(
    OCIDataResponse
):
    """Response to EnterpriseCallCenterEnhancedReportingScheduledReportGetActiveListRequest.
    Contains a table with column headings : \"Schedule Name\", \"Description\", \"Created By\",
    \"Is Supervisor Report\", \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Level\" are \"System\" and \"Enterprise\"."""

    scheduledReportTable: OCITable


@dataclass
class EnterpriseCallCenterEnhancedReportingScheduledReportGetCompletedListResponse(
    OCIDataResponse
):
    """Response to EnterpriseCallCenterEnhancedReportingScheduledReportGetCompletedListRequest
    Contains a table with column headings : \"Schedule Name\", \"Description\", \"Created By\",
    \"Is Supervisor Report\", \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Level\" are \"System\" and \"Enterprise\"."""

    scheduledReportTable: OCITable


@dataclass
class EnterpriseCallCenterEnhancedReportingScheduledReportGetListResponse(
    OCIDataResponse
):
    """Response to EnterpriseCallCenterEnhancedReportingScheduledReportGetListRequest.
    Contains a table with column headings : \"Schedule Name\", \"Description\", \"Created By\",
    \"Is Supervisor Report\", \"Status\", \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Status\" are \"Active\", and \"Completed\".
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Level\" are \"System\" and \"Enterprise\"."""

    scheduledReportTable: OCITable


@dataclass
class EnterpriseCallCenterEnhancedReportingScheduledReportGetReportTemplateUsageListResponse(
    OCIDataResponse
):
    """Response to EnterpriseCallCenterEnhancedReportingScheduledReportGetReportTemplateUsageListRequest.
    Contains a table with column headings: \"Schedule Name\", \"Created By\", \"Created By Supervisor\", and
    \"Is Active\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor."""

    scheduleReportTable: OCITable


@dataclass
class EnterpriseCallCenterEnhancedReportingScheduledReportGetResponse(OCIDataResponse):
    """Response to EnterpriseCallCenterEnhancedReportingScheduledReportGetRequest."""

    reportTemplate: CallCenterReportTemplateKey

    schedule: CallCenterReportSchedule

    reportTimeZone: str

    reportDateFormat: str

    reportTimeFormat: str

    reportInterval: CallCenterReportInterval

    reportFormat: str

    callCenter: CallCenterScheduledReportCallCenterSelectionRead

    dnis: CallCenterScheduledReportDNISSelectionRead

    description: Optional[str] = None

    samplingPeriod: Optional[str] = None

    startDayOfWeek: Optional[str] = None

    agent: Optional[CallCenterScheduledReportAgentSelectionAdminRead] = None

    callCompletionThresholdSeconds: Optional[int] = None

    shortDurationThresholdSeconds: Optional[int] = None

    serviceLevelThresholdSeconds: List[int] = field(default_factory=list)

    serviceLevelInclusions: Optional[
        CallCenterScheduledReportServiceLevelInclusions
    ] = None

    serviceLevelObjectivePercentage: Optional[int] = None

    abandonedCallThresholdSeconds: List[int] = field(default_factory=list)

    emailAddress: List[str] = field(default_factory=list)


@dataclass
class EnterpriseCallCenterGetResponse23(OCIDataResponse):
    """Response to EnterpriseCallCenterGetRequest23.

    The following elements are only used in AS data mode and not returned in XS data mode:
      useSystemDefaultUnavailableSettings
      forceAgentUnavailableOnDNDActivation
      forceAgentUnavailableOnPersonalCalls
      forceAgentUnavailableOnBouncedCallLimit
      numberConsecutiveBouncedCallsToForceAgentUnavailable
      forceAgentUnavailableOnNotReachable
      wrapUpDestination"""

    useSystemDefaultGuardTimer: bool

    enableGuardTimer: bool

    guardTimerSeconds: int

    useSystemDefaultUnavailableSettings: Optional[bool] = None

    forceAgentUnavailableOnDNDActivation: Optional[bool] = None

    forceAgentUnavailableOnPersonalCalls: Optional[bool] = None

    forceAgentUnavailableOnBouncedCallLimit: Optional[bool] = None

    numberConsecutiveBouncedCallsToForceAgentUnavailable: Optional[int] = None

    forceAgentUnavailableOnNotReachable: Optional[bool] = None

    wrapUpDestination: Optional[str] = None


@dataclass
class EnterpriseCallCenterGetRoutingPolicyResponse(OCIDataResponse):
    """Response to EnterpriseCallCenterGetRoutingPolicyRequest.
    Contains a table with column headings: \"Service User Id\", \"Name\" and
    \"Priority\"."""

    routingPolicy: str

    callCenterTable: OCITable


@dataclass
class EnterpriseCallCenterMonitoringGetResponse23(OCIDataResponse):
    """Response to EnterpriseCallCenterMonitoringGetRequest23."""

    enableSupervisorCoaching: bool

    bypassEnforcementOfSupervisorAgentRelationship: Optional[bool] = None


@dataclass
class EnterpriseCallRecordingGetResponse(OCIDataResponse):
    """Response to the EnterpriseCallRecordingGetRequest.
    The response contains the enterprise's Call Recording attributes."""

    useCloudPBX: bool

    useEnterpriseSetting: Optional[bool] = None

    FQDN: Optional[str] = None


@dataclass
class EnterpriseCommonPhoneListGetListResponse(OCIDataResponse):
    """Response to the EnterpriseCommonPhoneListGetListRequest.
    The response contains the enterprise's common phone list."""

    entry: List[PhoneListEntry] = field(default_factory=list)


@dataclass
class EnterpriseCommunicationBarringAuthorizationCodeGetListResponse(OCIDataResponse):
    """Response to the EnterpriseCommunicationBarringAuthorizationCodeGetListRequest.
    Contains a list of Communication Barring Authorization Codes assigned to a group."""

    code: List[CommunicationBarringAuthorizationCodeConfiguration] = field(
        default_factory=list
    )


@dataclass
class EnterpriseCommunicationBarringAuthorizationCodeGetResponse(OCIDataResponse):
    """Response to EntepriseCommunicationBarringAuthorizationCodeGetRequest."""

    description: Optional[str] = None

    networkClassOfService: Optional[str] = None


@dataclass
class EnterpriseDepartmentGetAvailableParentListResponse(OCIDataResponse):
    """Response to EnterpriseDepartmentGetAvailableParentListRequest.
    The response includes two parallel arrays of department keys and department display names."""

    departmentKey: List[DepartmentKey] = field(default_factory=list)

    fullPathName: List[str] = field(default_factory=list)


@dataclass
class EnterpriseDepartmentGetListResponse(OCIDataResponse):
    """Response to EnterpriseDepartmentGetListRequest.
    The response includes two parallel arrays of department keys and department display names."""

    departmentKey: List[DepartmentKey] = field(default_factory=list)

    fullPathName: List[str] = field(default_factory=list)


@dataclass
class EnterpriseEnterpriseTrunkGetAvailableTrunkGroupListResponse(OCIDataResponse):
    """Response to EnterpriseEnterpriseTrunkGetAvailableTrunkGroupListRequest."""

    trunkGroup: List[EnterpriseTrunkTrunkGroupKey] = field(default_factory=list)


@dataclass
class EnterpriseEnterpriseTrunkGetAvailableUserListResponse(OCIDataResponse):
    """Response to EnterpriseEnterpriseTrunkGetAvailableUserListRequest.
    The column headings for the enterpriseTrunkUserTable are: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class EnterpriseEnterpriseTrunkGetListResponse(OCIDataResponse):
    """Response to EnterpriseEnterpriseTrunkGetListRequest.
    Contains a table of enterprise trunks defined in the enterprise
    The column headings are: \"Enterprise Trunk Name\", \"Routing Type\" """

    enterpriseTrunkTable: OCITable


@dataclass
class EnterpriseEnterpriseTrunkGetResponse22(OCIDataResponse):
    """Response to EnterpriseEnterpriseTrunkGetRequest22."""

    maximumRerouteAttempts: int

    routeExhaustionAction: str

    orderedRouting: object

    priorityWeightedRouting: object

    enableCapacityManagement: bool

    routeExhaustionForwardAddress: Optional[str] = None

    maxActiveCalls: Optional[int] = None

    capacityExceededTrapInitialCalls: Optional[int] = None

    capacityExceededTrapOffsetCalls: Optional[int] = None

    maximumActiveIncomingCallsAllowed: Optional[int] = None

    maximumActiveOutgoingCallsAllowed: Optional[int] = None

    minimumActiveCallsReserved: Optional[int] = None


@dataclass
class EnterpriseEnterpriseTrunkGetUserListResponse(OCIDataResponse):
    """Response to EnterpriseEnterpriseTrunkGetUserListRequest.
    The column headings for the enterpriseTrunkUserTable are: \"Group Id\", \"User Id\", \"Last Name\", \"First Name\", \"Phone Number\", \"Alternate Trunk Identity\", \"Hiragana Last Name\", \"Hiragana First Name\",
     \"Extension\", \"Department\", \"Email Address\" and \"Route List Assigned\"."""

    enterpriseTrunkUserTable: OCITable


@dataclass
class EnterpriseLocalGatewayGetPagedSortedListResponse(OCIDataResponse):
    """Response to EnterpriseLocalGatewayGetPagedSortedListRequest.
    Contains a table with column headings \"Name\", \"Device Name\", \"Device Level\", \"Group Id\", \"Group Name\"  and \"Group External Id\".
    The \"Device Level\" column contains one of the AccessDeviceLevel enumerated constants.
    The following columns are only populated in AS data mode
    \"Group External Id\" """

    localGatewayTable: OCITable


@dataclass
class EnterpriseLocalGatewayGetUsageResponse(OCIDataResponse):
    """Response to EnterpriseLocalGatewayGetUsageRequest.
    Returns the group ID and group name where the local gateway belongs to, a boolean value to indicate if the local gateway is
    used in the enterprise call processing policy.
    It also returns an OCITable containing the groups using the given local gateway.
    Column headings are: \"Group Id\", \"Group Name\" and \"Group External Id\".
    The following columns are only populated in AS data mode
    \"Group External Id\" """

    gatewayGroupId: str

    usedByEnterprise: bool

    groupTable: OCITable

    gatewayGroupName: Optional[str] = None


@dataclass
class EnterprisePhoneDirectoryGetPagedSortedListResponse(OCIDataResponse):
    """Response to EnterprisePhoneDirectoryGetPagedSortedListRequest.
    Contains a table with  a row for each phone number and column headings :
    \"Name\", \"Number\", \"Extension\", \"Mobile\", \"Email Address\",
    \"Department\", \"Hiragana Name\", \"Group Id\", \"Yahoo Id\", \"User Id\", \"IMP Id\", \"Is Virtual On-Net User\".
    If extended directory information is requested, the following columns are also included:
    \"First Name\", \"Last Name\", \"Pager\", \"Title\", \"Time Zone\",
    \"Location\", \"Address Line 1\", \"Address Line 2\",
    \"City\", \"State\", \"Zip\", \"Country\", \"Service Name\".
    The Service Name represents the localized service name for service instances. The localized values are taken from the BroadworksLabel.properties file.
    Service Name is currently supporting:
    AutoAttendant, AutoAttendantStandard, AutoAttendantVideo, CallCenter, CallCenterStandard, CallCenterPremium
    HuntGroup, InstantGroupCall, VoiceMessagingGroup, RoutePoint, BroadWorksAnywhere, GroupPaging, FindmeFollowme,
    VoiceXML, FlexibleSeatingGuest, CollaborateAudio, MeetMeConferencing.
    For a Regular User or a Virtual On Network Enterprise Extensions, the Service Name is empty.

    The following columns are populated in AS data mode only:
      \"IMP Id\" """

    totalNumberOfRows: int

    directoryTable: OCITable


@dataclass
class EnterprisePreAlertingAnnouncementGetResponse(OCIDataResponse):
    """Get the Enterprise level pre-alerting service settings.
    The response is either a EnterprisePreAlertingAnnouncementGetResponse or an ErrorResponse."""

    announcementInterruption: str

    audioSelection: str

    videoSelection: str

    interruptionDigitSequence: Optional[str] = None

    audioFileDescription: Optional[str] = None

    audioMediaType: Optional[str] = None

    audioFileUrl: Optional[str] = None

    videoFileDescription: Optional[str] = None

    videoMediaType: Optional[str] = None

    videoFileUrl: Optional[str] = None


@dataclass
class EnterpriseRouteListEnterpriseTrunkNumberPrefixGetAvailableListResponse(
    OCIDataResponse
):
    """Response to EnterpriseRouteListEnterpriseTrunkNumberPrefixGetAvailableListRequest.
    Contains a list of number prefixes that are assigned to an enterprise and still available for assignment to users within the enterprise.
    The column headings are \"Number Prefix\" \",\"Is Active\", \"Extension Range Start\" and \"Extension Range End\"."""

    availableNumberPrefixTable: OCITable


@dataclass
class EnterpriseRouteListEnterpriseTrunkNumberPrefixGetSummaryListResponse(
    OCIDataResponse
):
    """Response to EnterpriseRouteListEnterpriseTrunkNumberPrefixGetSummaryListRequest.
    The response contains a table with columns: \"Number Prefix\", \"Group Id\", \"User Id\",
    \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\",
    \"Email Address\", \"Enterprise Trunk\"\",\"Is Active\", \"Extension Range Start\" and \"Extension Range End\".
    The \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\" and \"Email Address\" columns contains the corresponding attributes of the user possessing the number range.
    The \"Enterprise Trunk\" column contains the enterprise trunk the user possessing the number range belongs to.
    The \"Is Active\" column indicates if the number range has been activated.
    The \"Extension Range Start\" column indicates the start for an extension range.
    The \"Extension Range End\" column indicates the end for an extension range."""

    prefixSummaryTable: OCITable


@dataclass
class EnterpriseRouteListEnterpriseTrunkNumberRangeGetAvailableListResponse(
    OCIDataResponse
):
    """Response to EnterpriseRouteListEnterpriseTrunkNumberRangeGetAvailableListRequest.
    Contains a list of number ranges that are assigned to an enterprise and still available for assignment to users within the enterprise.
    The column headings are \"Number Range Start\", \"Number Range End\" ,\"Is Active\" and \"Extension Length\".."""

    availableNumberRangeTable: OCITable


@dataclass
class EnterpriseRouteListEnterpriseTrunkNumberRangeGetSummaryListResponse(
    OCIDataResponse
):
    """Response to EnterpriseRouteListEnterpriseTrunkNumberRangeGetSummaryListRequest.
    The response contains a table with columns: \"Number Range Start\", \"Number Range End\", \"Group Id\", \"User Id\",
    \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\",
    \"Email Address\", \"Enterprise Trunk\", \"Is Active\" and \"Extension Length\".
    The \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\" and \"Email Address\" columns contains the corresponding attributes of the user possessing the number range.
    The \"Enterprise Trunk\" column contains the enterprise trunk the user possessing the number range belongs to.
    The \"Is Active\" column indicates if the number range has been activated.
    The \"Extension Length\" column indicates the length of the extension for the enterpris trunk number range."""

    numberRangeSummaryTable: OCITable


@dataclass
class EnterpriseSecurityClassificationCustomizationGetAvailableListResponse(
    OCIDataResponse
):
    """Response to EnterpriseSecurityClassificationCustomizationGetAvailableListRequest.
    Returns the available group security classifications.
    Contains a table with column headings:
    \"SystemSecurityClassification\", \"CustomizedSecurityClassification\" """

    securityClassificationNameTable: OCITable


@dataclass
class EnterpriseSessionAdmissionControlGetAvailableDeviceListResponse(OCIDataResponse):
    """Response to EnterpriseSessionAdmissionControlGetAvailableDeviceListRequest.
    Contains a table of devices can be assigned to session admission control group in the enterprise."""

    accessDevice: List[EnterpriseAccessDevice] = field(default_factory=list)


@dataclass
class EnterpriseSessionAdmissionControlGroupGetListResponse(OCIDataResponse):
    """Response to EnterpriseSessionAdmissionControlGroupGetListRequest.
    Contains a table of session admission control group configured in the enterprise.
    The column headings are: \"Name\", \"Is Default\", \"Maximum Sessions\", \"Maximum Originating Sessions\", \"Maximum Terminating Sessions\".."""

    sessionAdmissionControlGroupTable: OCITable


@dataclass
class EnterpriseSessionAdmissionControlGroupGetResponse21sp1V2(OCIDataResponse):
    """Response to EnterpriseSessionAdmissionControlGroupGetRequest21sp1V2.
    Returns the profile information for the session admission control group."""

    maxSession: int

    reservedSession: int

    defaultGroup: bool

    countIntraSACGroupSessions: bool

    blockEmergencyAndRepairCallsDueToSACLimits: bool

    maxUserOriginatingSessions: Optional[int] = None

    maxUserTerminatingSessions: Optional[int] = None

    reservedUserOriginatingSessions: Optional[int] = None

    reservedUserTerminatingSessions: Optional[int] = None

    devices: List[EnterpriseAccessDevice] = field(default_factory=list)

    mediaGroupName: Optional[str] = None

    accessInfoPattern: Optional[str] = None


@dataclass
class EnterpriseUserCallForwardingSettingsGetListResponse(OCIDataResponse):
    """Response to the EnterpriseUserCallForwardingSettingsGetListRequest.
    Contains a table with column headings: \"Group Id\", \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", and \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"In Trunk Group\",
    \"Email Address\", \"Is Active\", \"Forwarding Address\".
    \"Is Active\" is \"true\" or \"false\".
    The \"Forwarding Address\" is the Call Forwarding service's forwarding address.
    If the service is Call Forwarding Selective, the default forwarding address is returned.
    \"Phone Number\" field is presented in the E164 format."""

    userCallForwardingTable: OCITable


@dataclass
class EnterpriseUserCallWaitingSettingsGetListResponse(OCIDataResponse):
    """Response to the EnterpriseUserCallWaitingSettingsGetListRequest.
    Contains a table with column headings: \"Group Id\", \"User Id\", \"Last Name\", \"First Name\",
    \"Hiragana Last Name\", and \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\",
    \"In Trunk Group\", \"Email Address\", \"Is Active\".
    \"Is Active\" is \"true\" or \"false\".
    \"Phone Number\" is presented in the E164 format."""

    userCallWaitingTable: OCITable


@dataclass
class EnterpriseUserCallingPlanSettingsGetListResponse(OCIDataResponse):
    """Response to the EnterpriseUserCallingPlanSettingsGetListRequest.
    Contains a table with column headings: \"Group Id\", \"User Id\", \"Last Name\", \"First
    Name\", \"Hiragana Last Name\", and \"Hiragana First Name\", \"Phone
    Number\", \"Extension\", \"Department\", \"In Trunk Group\", \"Email Address\",
    \"Use Custom Settings\".
    \"Use Custom Settings\" is \"true\" or \"false\".
    \"Phone Number\" is presented in the E164 format."""

    userCallingPlanTable: OCITable


@dataclass
class EnterpriseUserHotelingGuestSettingsGetListResponse(OCIDataResponse):
    """Response to the EnterpriseUserHotelingGuestSettingsGetListRequest.
    Contains a table with column headings: \"Group Id\", \"User Id\", \"Last Name\", \"First
    Name\", \"Hiragana Last Name\", and \"Hiragana First Name\", \"Phone
    Number\", \"Extension\", \"Department\", \"In Trunk Group\", \"Email Address\",
    \"Is Active\".
    \"Is Active\" is \"true\" or \"false\".
    \"Phone Number\" is presented in the E164 format."""

    userHotelingGuestTable: OCITable


@dataclass
class EnterpriseVirtualOnNetEnterpriseExtensionsGetUserListResponse(OCIDataResponse):
    """Response to   EnterpriseVirtualOnNetEnterpriseExtensionsGetUserListRequest.
    Contains a table with column headings : \"Group Id\", \"Last Name\", \"First Name\", \"Phone Number\", \"Extension\",
    \"Virtual On-Net Call Type\" in a row for each user."""

    userTable: OCITable


@dataclass
class EnterpriseVoiceVPNGetDefaultResponse(OCIDataResponse):
    """Response to EnterpriseVoiceVPNGetDefaultResponse."""

    policySelection: List[str] = field(default_factory=list)

    digitManipulationOperation: List[str] = field(default_factory=list)

    routeGroupId: List[str] = field(default_factory=list)

    treatment: List[EnterpriseVoiceVPNTreatmentEntry] = field(default_factory=list)


@dataclass
class EnterpriseVoiceVPNGetPolicyListResponse(OCIDataResponse):
    """Response to EnterpriseVoiceVPNGetListResponse.
    Returns a 4 column table with column headings:
      \"Location Code\", \"Min Extension Length\", \"Max Extension Length\", \"Location Selection\"."""

    locationList: OCITable


@dataclass
class EnterpriseVoiceVPNGetPolicyResponse(OCIDataResponse):
    """Response to EnterpriseVoiceVPNGetPolicyRequest."""

    minExtensionLength: int

    maxExtensionLength: int

    policySelection: str

    description: Optional[str] = None

    routeGroupId: Optional[str] = None

    digitManipulation: List[EnterpriseVoiceVPNDigitManipulation] = field(
        default_factory=list
    )

    treatmentId: Optional[str] = None


@dataclass
class EnterpriseVoiceVPNGetResponse14sp3(OCIDataResponse):
    """Response to EnterpriseVoiceVPNGetRequest14sp3."""

    isActive: bool

    defaultSelection: str

    e164Selection: str

    usePhoneContext: bool


@dataclass
class ExternalAuthenticationCreateLoginTokenResponse(OCIDataResponse):
    """Response to ExternalAuthenticationCreateLoginTokenRequest."""

    loginToken: str


@dataclass
class GroupAccessDeviceAvailablePortGetListResponse(OCIDataResponse):
    """Response to GroupAccessDeviceAvailablePortGetListRequest.
    Contains a list of available ports in a device using static mode. The list is empty in case the device is using dynamic mode."""

    portNumber: List[int] = field(default_factory=list)


@dataclass
class GroupAccessDeviceCustomTagGetListResponse(OCIDataResponse):
    """Response to GroupAccessDeviceCustomTagGetListRequest.
    Contains a table of custom configuration tags managed by the Device Management System on a per-device profile basis.
    In AS data mode, the column headings are:
      \"Tag Name\", \"Tag Value\", \"Actual Tag Value\".
    In XS data mode, the column headings are:
      \"Tag Name\", \"Tag Value\", \"Actual Tag Value\" if request is invoked by an admin without system privileges.
      \"Tag Name\", \"Tag Value\", \"Is Encrypted\", \"Actual Tag Value\" if request is invoked by an admin with system privileges."""

    deviceCustomTagsTable: OCITable


@dataclass
class GroupAccessDeviceDeviceActivationGetResponse(OCIDataResponse):
    """Response to GroupAccessDeviceDeviceActivationGetRequest.
    The response contains the activation code (if available), the expiry time (if available) and the activation state.
    The expiryTime is represented as a timestamp, i.e. the number of milliseconds
    since January 1, 1970, 00:00:00 GMT."""

    activationState: str

    activationCode: Optional[str] = None

    expiryTime: Optional[int] = None


@dataclass
class GroupAccessDeviceFileGetListResponse14sp8(OCIDataResponse):
    """Response to GroupAccessDeviceFileGetListRequest14sp8.
    Contains a table of device files managed by the Device Management System on a per-device profile basis.
    The column headings are: \"File Format\", \"Is Authenticated\", \"Access URL\", \"Repository URL\", \"Template URL\", \"Extended Capture URL\", \"Is File Linked\".

    The following column is only populated in AS data mode for leaf devices.
      \"Is File Linked\" """

    deviceFilesTable: OCITable


@dataclass
class GroupAccessDeviceFileGetResponse20(OCIDataResponse):
    """Response to GroupAccessDeviceFileGetRequest20."""

    fileSource: str

    accessUrl: str

    configurationFileName: Optional[str] = None

    repositoryUrl: Optional[str] = None

    templateUrl: Optional[str] = None

    extendedCaptureEnabled: Optional[bool] = None

    extendedCaptureURL: Optional[str] = None


@dataclass
class GroupAccessDeviceGetAvailableCustomTagListResponse(OCIDataResponse):
    """Response to GroupAccessDeviceGetAvailableCustomTagListRequest.
    Contains a table of all available custom tags managed by the Device Management System on a per-device profile basis.

    In AS data mode, the column headings are: \"Tag Name\", \"Tag Value\", \"Tag Level\", \"Tag Set Name\", \"Region Name\".

    In XS data mode:
      the column headings are: \"Tag Name\", \"Tag Value\", \"Tag Level\", \"Tag Set Name\", \"Is Encrypted\" if request is invoked by a System administrator or by an administrator with higher priviledges, otherwise the column headings are: \"Tag Name\", \"Tag Value\", \"Tag Level\", \"Tag Source\", \"Tag Set Name\".

    \"Tag Level\" can take the value: \"System Default\", \"System\", \"Service Provider\", \"Group\" or \"Device Profile\"."""

    deviceAvailableCustomTagsTable: OCITable


@dataclass
class GroupAccessDeviceGetAvailableDetailListResponse19(OCIDataResponse):
    """Response to GroupAccessDeviceGetAvailableDetailListRequest19."""

    availableAccessDevice: List[object] = field(default_factory=list)


@dataclass
class GroupAccessDeviceGetEnhancedConfigurationTypeListResponse(OCIDataResponse):
    """Response to GroupAccessDeviceGetEnhancedConfigurationTypeListRequest."""

    deviceType: List[str] = field(default_factory=list)


@dataclass
class GroupAccessDeviceGetEnhancedConfigurationTypeResponse14(OCIDataResponse):
    """Response to GroupAccessDeviceGetEnhancedConfigurationTypeRequest14."""

    supportsEnhancedConfiguration: bool

    supportsReset: bool

    configurationType: Optional[str] = None

    configurationFileName: Optional[str] = None


@dataclass
class GroupAccessDeviceGetLinkedLeafDeviceListResponse22(OCIDataResponse):
    """Response to GroupAccessDeviceGetLinkedLeafDeviceListRequest22."""

    treeDeviceLinkId: str

    leafDeviceKey: List[AccessDeviceKey] = field(default_factory=list)

    supportLinks: List[str] = field(default_factory=list)


@dataclass
class GroupAccessDeviceGetLinkedTreeDeviceResponse(OCIDataResponse):
    """Response to GroupAccessDeviceGetLinkedTreeDeviceRequest."""

    treeDeviceInfo: Optional[TreeDeviceInfo] = None


@dataclass
class GroupAccessDeviceGetListResponse(OCIDataResponse):
    """Response to GroupAccessDeviceGetListRequest.
    Contains a table of devices configured in the group.
    The column headings are: \"Device Name\", \"Device Type\", \"Available Ports\", \"Net Address\", \"MAC Address\", \"Status\", \"Version\",
    and \"Access Device External Id\".

    The following columns are only populated in AS data mode:
      \"Access Device External Id\" """

    accessDeviceTable: OCITable


@dataclass
class GroupAccessDeviceGetNativeTagsWithLogicListResponse(OCIDataResponse):
    """Response to GroupAccessDeviceGetNativeTagsWithLogicListRequest.
    Contains a table of all native tags with logic managed by the Device Management System on a per-device profile basis.

    The column headings are: \"Tag Name\", \"Tag Value\"."""

    deviceNativeTagsWithLogicTable: OCITable


@dataclass
class GroupAccessDeviceGetPagedSortedListResponse22(OCIDataResponse):
    """Response to GroupAccessDeviceGetPagedSortedListRequest22.
    Contains a table of devices configured in the group.
    The column headings are: \"Device Name\", \"Device Type\", \"Available Ports\", \"Net Address\", \"MAC Address\", \"Status\", \"Version\", and \"Support Visual Device Management API\".
    When CloudPBX is not licensed, the column \"Support Visual Device Management API\" values are not returned."""

    accessDeviceTable: OCITable

    totalNumberOfRows: Optional[int] = None


@dataclass
class GroupAccessDeviceGetResponse24V3(OCIDataResponse):
    """Response to GroupAccessDeviceGetRequest24V3.

    The following elements are only used in AS data mode:
       serviceProviderId
       groupId
       deviceName
       deviceExternalId
       deviceCode
       deviceIPEI
       deviceIndex
       useDeviceCode
       authBearerSubject"""

    deviceType: str

    numberOfPorts: UnboundedPositiveInt

    numberOfAssignedPorts: int

    status: str

    serviceProviderId: str

    groupId: str

    deviceName: str

    protocol: Optional[str] = None

    netAddress: Optional[str] = None

    port: Optional[int] = None

    outboundProxyServerNetAddress: Optional[str] = None

    stunServerNetAddress: Optional[str] = None

    macAddress: Optional[str] = None

    serialNumber: Optional[str] = None

    description: Optional[str] = None

    configurationMode: Optional[str] = None

    configurationFileName: Optional[str] = None

    physicalLocation: Optional[str] = None

    transportProtocol: Optional[str] = None

    useCustomUserNamePassword: Optional[bool] = None

    userName: Optional[str] = None

    version: Optional[str] = None

    deviceExternalId: Optional[str] = None

    deviceCode: Optional[str] = None

    deviceIPEI: Optional[str] = None

    deviceIndex: Optional[int] = None

    useDeviceCode: Optional[bool] = None

    authBearerSubject: Optional[str] = None


@dataclass
class GroupAccessDeviceGetUserListResponse21sp1(OCIDataResponse):
    """Response to GroupAccessDeviceGetUserListRequest21sp1.
    The column headings for the deviceUserTable are: \"Line/Port\", \"Last Name\",
    \"First Name\", \"Phone Number\", \"User Id\", \"User Type\", \"Endpoint Type\", \"Order\", \"Primary Line/Port\", \"Extension\", \"Department\", \"Email Address\", \"Private Identity\".
    In IMS mode, the table will contain a row for each TEL-URI in the Phone Number column.
    In Standalone mode, rows for the alternate numbers are not included.
    The User Type column contains one of the enumerated UserType values.
    The Endpoint Type column contains one of the enumerated EndpointType21sp1 values.
    The value Mobility in Endpoint Type column is only applicable in AS data mode.
    The Private Identity column is empty is AS mode."""

    deviceUserTable: OCITable


@dataclass
class GroupAccessDeviceTagSetGetResponse(OCIDataResponse):
    """Response to GroupAccessDeviceTagSetGetRequest.
    The response includes a tag set name defined in the access device."""

    tagSetName: Optional[str] = None


@dataclass
class GroupAccountAuthorizationCodesGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupAccountAuthorizationCodesGetAvailableUserListRequest.
    The column headings are: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\" and
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupAccountAuthorizationCodesGetListResponse(OCIDataResponse):
    """Response to GroupAccountAuthorizationCodesGetListRequest."""

    codeEntry: List[AccountAuthorizationCodeEntry] = field(default_factory=list)


@dataclass
class GroupAccountAuthorizationCodesGetResponse(OCIDataResponse):
    """Response to GroupAccountAuthorizationCodesGetRequest.
    The tables has the following column headings:
    \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    type: str

    numberOfDigits: int

    allowLocalAndTollFreeCalls: bool

    mandatoryUsageUserTable: OCITable

    optionalUsageUserTable: OCITable


@dataclass
class GroupAdminAlternateIdGetListResponse(OCIDataResponse):
    """Response to GroupAdminAlternateIdGetListRequest.
    Contains a table of the main admin user id and the alternate admin user ids, the column headings are: \"User Id\", \"Description\", \"Alternate\".
    The possible values for \"Alternate\" are \"true\" and \"false\".
    The \"Description\" is only present for alternate admin user Ids."""

    adminUserIdTable: OCITable


@dataclass
class GroupAdminGetListResponse(OCIDataResponse):
    """Response to GroupAdminGetListRequest.
    Contains a 7 column table with column headings \"Administrator ID\",
    \"Last Name\", \"First Name\", \"Department\", \"Language\", \"Locale\" and \"Encoding\".

    The following columns are only returned in AS data mode:
      \"Locale\" and \"Encoding\" """

    groupAdminTable: OCITable


@dataclass
class GroupAdminGetPagedSortedListResponse(OCIDataResponse):
    """Response to GroupAdminGetPagedSortedListRequest.
    Contains a 8 column table with column headings \"Administrator ID\",
    \"Last Name\", \"First Name\", \"Administrator Type\", \"Department\",
    \"Language\", \"Locale\" and \"Encoding\".
    The following columns are only returned in AS data mode:
    \"Locale\" and \"Encoding\"."""

    groupAdminTable: OCITable


@dataclass
class GroupAdminGetPolicyResponse20(OCIDataResponse):
    """Response to GroupAdminGetPolicyRequest20.
    Contains the policy settings for the group administrator.
    The following elements are only used in AS data mode:
        dialableCallerIDAccess
        verifyTranslationAndroutingAccess, value \"None\" is returned in XS data mode

    The following elements are only used in AS data mode and not returned in XS data mode:
        communicationBarringUserProfileAccess (This element is only returned for groups in an enterprise)"""

    profileAccess: str

    userAccess: str

    adminAccess: str

    departmentAccess: str

    accessDeviceAccess: str

    enhancedServiceInstanceAccess: str

    featureAccessCodeAccess: str

    phoneNumberExtensionAccess: str

    callingLineIdNumberAccess: str

    serviceAccess: str

    trunkGroupAccess: str

    sessionAdmissionControlAccess: str

    officeZoneAccess: str

    numberActivationAccess: str

    dialableCallerIDAccess: str

    verifyTranslationAndRoutingAccess: str

    communicationBarringUserProfileAccess: Optional[str] = None


@dataclass
class GroupAdminGetResponse22V3(OCIDataResponse):
    """Response to the GroupAdminGetRequest22V3.
    The response contains the group administrators  profile information.

    The following elements are only used in AS data mode and ignored in XS data mode.
    accountDisabled
    lastAuthenticatedDate
    hasPassword"""

    serviceProviderId: str

    groupId: str

    language: str

    locale: str

    encoding: str

    accountDisabled: bool

    lastAuthenticatedDate: str

    hasPassword: bool

    firstName: Optional[str] = None

    lastName: Optional[str] = None


@dataclass
class GroupAdministratorPasswordRulesGetResponse(OCIDataResponse):
    """Response to GroupAdministratorPasswordRulesGetRequest."""

    useExternalAuthentication: bool

    allowWebAddExternalAuthenticationUsers: bool

    disallowUserId: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    maxFailedLoginAttempts: int

    passwordExpiresDays: int

    sendLoginDisabledNotifyEmail: bool

    disallowPreviousPasswords: bool

    numberOfPreviousPasswords: int

    loginDisabledNotifyEmailAddress: Optional[str] = None


@dataclass
class GroupAdviceOfChargeGetResponse(OCIDataResponse):
    """Response to GroupAdviceOfChargeGetRequest.
    Contains a list of Advice of Charge group parameters."""

    useGroupLevelAoCSettings: bool

    delayBetweenNotificationSeconds: int


@dataclass
class GroupAlternateUserIdGetListResponse(OCIDataResponse):
    """Response to GroupAlternateUserIdGetListRequest.
    The \"User Type\" column contains the corresponding enumerated UserType value.
    Contains a table of alternate user ids, the column headings are:
      \"User Id\", \"Alternate User Id\" and \"User Type\"."""

    alternateUserIdTable: OCITable


@dataclass
class GroupAnnouncementFileGetListResponse(OCIDataResponse):
    """Response to GroupAnnouncementFileGetListRequest.
    When requested, the response contains a table with columns: \"Name\", \"Media Type\", \"File Size\", \"Announcement File External Id\".
    The \"Name\" column contains the name of the announcement file.
    The \"Media Type\" column contains the media type of the announcement
    File with the possible values:
            WMA - Windows Media Audio file
            WAV - A WAV file
            3GP - A 3GP file
            MOV - A MOV file using a H.263 or H.264 codec.
    The \"File Size\" column contains the file size (KB) of the announcement file.
    The \"Announcement File External Id\" column contains the External ID of the announcement file.
    The response also contains the current total file size (KB) for the group across
    all media types and the maximum total file size (MB) allowed for the group.

    The following columns are populated in AS data mode only:
      \"Announcement File External Id\" """

    totalFileSize: int

    maxFileSize: int

    announcementTable: Optional[OCITable] = None


@dataclass
class GroupAnnouncementFileGetPagedSortedListResponse(OCIDataResponse):
    """Response to GroupAnnouncementFileGetPagedSortedListRequest.
    The response contains a table with columns: \"Name\", \"Media Type\", \"File Size\", and \"Announcement File External Id\".
    The \"Name\" column contains the name of the announcement file.
    The \"Media Type\" column contains the media type of the announcement
    File with the possible values:
            WMA - Windows Media Audio file
            WAV - A WAV file
            3GP - A 3GP file
            MOV - A MOV file using a H.263 or H.264 codec.
    The \"File Size\" column contains the file size (KB) of the announcement file.

    The following columns are populated in AS data mode only:
      \"Announcement File External Id\" """

    announcementTable: Optional[OCITable] = None


@dataclass
class GroupAnnouncementFileGetResponse22(OCIDataResponse):
    """Response to GroupAnnouncementFileGetRequest22.
    The response contains the file size, uploaded timestamp, description and usage for
    an announcement file in the user announcement repository.
    The usage table has columns \"Service Name\", and \"Instance Name\".
    The Service Name values correspond to string values of the GroupService and UserService data types.
    With the exception of the string \"Voice Portal\" which is returned when the announcement is being used by Voice Portal Personalized Name.

    The following data elements are only used in AS data mode:
      announcementFileExternalId"""

    description: str

    filesize: int

    lastUploaded: str

    serviceProviderId: str

    groupId: str

    announcementFileKey: AnnouncementFileKey

    usageTable: OCITable

    announcementFileExternalId: Optional[str] = None


@dataclass
class GroupAnnouncementRepositoryGetSettingsResponse(OCIDataResponse):
    """Response to GroupAnnouncementFileGetSettingsRequest.
    The response contains the current total file size (KB) for the group across
    all media types and the maximum total file size (MB) allowed for the group.
    It also indicates the maximum file size for individual audio and video files."""

    totalFileSize: int

    maxAudioFileSize: int

    maxVideoFileSize: int

    maxFileSize: int


@dataclass
class GroupApplicationServerSetGetResponse(OCIDataResponse):
    """Response to the GroupApplicationServerSetGetRequest.
    The response contains the group's Application Server set information."""

    applicationServerSetName: Optional[str] = None


@dataclass
class GroupAutoAttendantGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupAutoAttendantGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Video\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\", \"Type\".
    The column values for \"Video\" and \"Is Active\" can either be true, or false.
    The column values for \"Type\" can either be Basic or Standard.

    In XS Mode the value for the \"Type\" column will always be populated with Basic."""

    autoAttendantTable: OCITable


@dataclass
class GroupAutoAttendantGetInstancePagedSortedListResponse(OCIDataResponse):
    """Response to the GroupAutoAttendantGetInstancePagedSortedListRequest.
    The response contains a table with columns:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Is Phone Number Activated\", \"Country Code\",
    \"National Prefix\", \"Extension\", \"Department\", \"Department Type\", \"Parent Department\",
    \"Parent Department Type\", \"Is Active\", \"Type\".
    The column values for \"Is Active\" can either be true, or false.
    The column values for \"Type\" can either be Basic or Standard.
    The \"Department Type\" and \"Parent Department Type\" columns will contain the values \"Enterprise\" or \"Group\".

    In XS Mode the value for the \"Type\" column will always be populated with Basic."""

    autoAttendantTable: OCITable


@dataclass
class GroupAutoAttendantGetInstanceResponse24(OCIDataResponse):
    """Response to GroupAutoAttendantGetInstanceRequest24.
    Contains the service profile information.

    The following elements are only used in AS data mode and not returned in XS
    datamode:
    transferToOperatorAudioFile,
    transferToOperatorVideoFile,
    type (use AutoAttendantType.BASIC in XS mode),
    holidayMenu.

    The following element is only used in AS data mode:
    transferToOperatorAnnouncementSelection, value \"Default\" is returned in XS data
    mode.

    The following elements are only valid for Standard Auto
    Attendants:
      holidayMenu"""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    type: str

    firstDigitTimeoutSeconds: int

    transferToOperatorAnnouncementSelection: str

    enableVideo: bool

    extensionDialingScope: str

    nameDialingScope: str

    nameDialingEntries: str

    businessHoursMenu: AutoAttendantReadMenu20

    afterHoursMenu: AutoAttendantReadMenu20

    transferToOperatorAudioFile: Optional[AnnouncementFileLevelKey] = None

    transferToOperatorVideoFile: Optional[AnnouncementFileLevelKey] = None

    businessHours: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    holidayMenu: Optional[AutoAttendantReadMenu20] = None

    networkClassOfService: Optional[str] = None


@dataclass
class GroupAutoAttendantSubmenuGetListResponse(OCIDataResponse):
    """Response to the GroupAutoAttendantSubmenuGetListRequest.
    Contains a table with column headings:
    \"Submenu Id\" \"Is Used\".
    The column values for \"Is Used\" can either be true, or false."""

    submenuTable: OCITable


@dataclass
class GroupAutoAttendantSubmenuGetResponse20(OCIDataResponse):
    """Response to GroupAutoAttendantSubmenuGetRequest20.
    Contains AutoAttendant submenu information."""

    announcementSelection: str

    enableLevelExtensionDialing: bool

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    keyConfiguration: List[AutoAttendantKeyReadConfiguration20] = field(
        default_factory=list
    )


@dataclass
class GroupAutoAttendantSubmenuGetUsageListResponse(OCIDataResponse):
    """Response to the GroupAutoAttendantSubmenuGetUsageListRequest.
    Contains a table with column headings:
    \"Type\" and \"Submenu ID\".

    The \"Type\" Column will contain one of the following: Business Hours Menu,
    After Hours Menu, Holiday Menu or Submenu.

    The \"Submenu ID\" Column will be left blank when the \"Type\" Column contains one
    of the base menu types (Business Hours Menu, After Hours Menu or Holiday Menu),
    and will contain the Submenu ID when the \"Type\" Column contains type Submenu."""

    submenuTable: OCITable


@dataclass
class GroupBroadWorksAnywhereGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupBroadWorksAnywhereGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\".
    The column value for \"Is Active\" can either be true, or false."""

    broadWorksAnywhereTable: OCITable


@dataclass
class GroupBroadWorksAnywhereGetInstanceResponse19sp1(OCIDataResponse):
    """Response to GroupBroadWorksAnywhereGetInstanceRequest19sp1.
    Contains the service profile information."""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    broadWorksAnywhereScope: str

    promptForCLID: str

    silentPromptMode: bool

    promptForPasscode: bool

    networkClassOfService: Optional[str] = None


@dataclass
class GroupBroadWorksMobilityGetResponse22V4(OCIDataResponse):
    """The response to a GroupBroadWorksMobilityGetRequest22V4."""

    useSettingLevel: str

    enableLocationServices: bool

    enableMSRNLookup: bool

    enableMobileStateChecking: bool

    denyCallOriginations: bool

    denyCallTerminations: bool

    enableAnnouncementSuppression: bool

    enableInternalCLIDDelivery: bool

    enableInternalCLIDDeliveryAccessLocations: bool

    enableEnhancedUnreachableStateChecking: bool

    enableNetworkCallBarringStatusCheck: bool

    enablePBXRoutePolicy: bool

    networkTranslationIndex: Optional[str] = None

    pbxRouteIdentity: Optional[TrunkGroupKey] = None


@dataclass
class GroupBroadWorksMobilityMobileSubscriberDirectoryNumberGetAssignmentListResponse(
    OCIDataResponse
):
    """Response to the GroupBroadWorksMobilityMobileSubscriberDirectoryNumberGetAssignmentListRequest.
    The response contains a table with columns: \"Mobile Number\", \"User Id\",
    \"Last Name\", \"First Name\",\"Phone Number\", \"Extension\", \"Department\",.
    The \"Mobile Number\" column contains a single DN.
    The \"User Id\", \"Last Name\" and \"First Name\" columns contains the corresponding attributes of the user possessing the DN(s).
    The \"Phone Number\" column contains a single DN.
    The \"Department\" column contains the department of the user if it is part of a department."""

    mobileSubscriberDirectoryNumberTable: OCITable


@dataclass
class GroupBroadWorksMobilityMobileSubscriberDirectoryNumberGetAvailableListResponse(
    OCIDataResponse
):
    """Response to GroupBroadWorksMobilityMobileSubscriberDirectoryNumberGetAvailableListRequest.
    Contains a list of available Mobile Subscriber Directory Numbers not yet assigned to any user."""

    mobileSubscriberDirectoryNumber: List[str] = field(default_factory=list)


@dataclass
class GroupCallCapacityManagementGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupCallCapacityManagementGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallCapacityManagementGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupCallCapacityManagementGetInstanceListRequest.
    Contains a table with column headings: \"Name\", \"Is Default\", \"Maximum Calls\", \"Maximum Incoming Calls\", \"Maximum Outgoing Calls\"."""

    callCapacityGroupTable: OCITable


@dataclass
class GroupCallCapacityManagementGetInstanceResponse(OCIDataResponse):
    """Response to the GroupCallCapacityManagementGetInstanceRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    name: str

    maxActiveCallsAllowed: int

    defaultGroupForNewUsers: bool

    userTable: OCITable

    maxIncomingActiveCallsAllowed: Optional[int] = None

    maxOutgoingActiveCallsAllowed: Optional[int] = None


@dataclass
class GroupCallCenterAgentThresholdDefaultProfileGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterAgentThresholdDefaultProfileGetRequest.
    The agent table contains the agents assigned to the profile and
    has column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\";"""

    profileName: str

    enableNotificationEmail: bool

    profileDescription: Optional[str] = None

    thresholdCurrentCallStateIdleTimeYellow: Optional[int] = None

    thresholdCurrentCallStateIdleTimeRed: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeYellow: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeRed: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeYellow: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeRed: Optional[int] = None

    thresholdAverageBusyInTimeYellow: Optional[int] = None

    thresholdAverageBusyInTimeRed: Optional[int] = None

    thresholdAverageBusyOutTimeYellow: Optional[int] = None

    thresholdAverageBusyOutTimeRed: Optional[int] = None

    thresholdAverageWrapUpTimeYellow: Optional[int] = None

    thresholdAverageWrapUpTimeRed: Optional[int] = None

    notificationEmailAddress: List[str] = field(default_factory=list)

    agentTable: Optional[OCITable] = None


@dataclass
class GroupCallCenterAgentThresholdProfileGetAvailableAgentListResponse(
    OCIDataResponse
):
    """Response to the GroupCallCenterAgentThresholdProfileGetAvailableAgentListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"Agent Threshold Profile\";"""

    agentTable: OCITable


@dataclass
class GroupCallCenterAgentThresholdProfileGetAvailableAgentPagedSortedListResponse(
    OCIDataResponse
):
    """Response to the GroupCallCenterAgentThresholdProfileGetAvailableAgentPagedSortedListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"Agent Threshold Profile\";"""

    agentTable: OCITable


@dataclass
class GroupCallCenterAgentThresholdProfileGetListResponse(OCIDataResponse):
    """Response to the GroupCallCenterAgentThresholdProfileGetListRequest.
    Contains a table with all the  Call Center Agent Threshold Profiles in the Group.
    The column headings are: \"Default\", \"Name\", \"Description\"."""

    profilesTable: OCITable


@dataclass
class GroupCallCenterAgentThresholdProfileGetPagedSortedResponse(OCIDataResponse):
    """Response to the GroupCallCenterAgentThresholdProfileGetPagedSortedRequest.
    The agentTable contains the agents assigned to the profile and has the column headings:
    \"User Id\", \"Group Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\";"""

    enableNotificationEmail: bool

    agentTable: OCITable

    profileDescription: Optional[str] = None

    thresholdCurrentCallStateIdleTimeYellow: Optional[int] = None

    thresholdCurrentCallStateIdleTimeRed: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeYellow: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeRed: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeYellow: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeRed: Optional[int] = None

    thresholdAverageBusyInTimeYellow: Optional[int] = None

    thresholdAverageBusyInTimeRed: Optional[int] = None

    thresholdAverageBusyOutTimeYellow: Optional[int] = None

    thresholdAverageBusyOutTimeRed: Optional[int] = None

    thresholdAverageWrapUpTimeYellow: Optional[int] = None

    thresholdAverageWrapUpTimeRed: Optional[int] = None

    notificationEmailAddress: List[str] = field(default_factory=list)


@dataclass
class GroupCallCenterAgentThresholdProfileGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterAgentThresholdProfileGetRequest.
    The agentTable contains the agents assigned to the profile and has the column headings:
    \"User Id\", \"Group Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\";"""

    enableNotificationEmail: bool

    agentTable: OCITable

    profileDescription: Optional[str] = None

    thresholdCurrentCallStateIdleTimeYellow: Optional[int] = None

    thresholdCurrentCallStateIdleTimeRed: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeYellow: Optional[int] = None

    thresholdCurrentCallStateOnCallTimeRed: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeYellow: Optional[int] = None

    thresholdCurrentAgentStateUnavailableTimeRed: Optional[int] = None

    thresholdAverageBusyInTimeYellow: Optional[int] = None

    thresholdAverageBusyInTimeRed: Optional[int] = None

    thresholdAverageBusyOutTimeYellow: Optional[int] = None

    thresholdAverageBusyOutTimeRed: Optional[int] = None

    thresholdAverageWrapUpTimeYellow: Optional[int] = None

    thresholdAverageWrapUpTimeRed: Optional[int] = None

    notificationEmailAddress: List[str] = field(default_factory=list)


@dataclass
class GroupCallCenterAgentUnavailableCodeGetListResponse(OCIDataResponse):
    """Response to the GroupCallCenterAgentUnavailableCodeGetListRequest.
    Contains a table with column headings: \"Is Active\", \"Code\", \"Description\"."""

    unavailableCodesTable: OCITable


@dataclass
class GroupCallCenterAgentUnavailableCodeGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterAgentUnavailableCodeGetRequest"""

    isActive: bool

    description: Optional[str] = None


@dataclass
class GroupCallCenterAgentUnavailableCodeSettingsGetResponse17sp4(OCIDataResponse):
    """Response to GroupCallCenterAgentUnavailableCodeSettingsGetRequest17sp4."""

    enableAgentUnavailableCodes: bool

    forceUseOfAgentUnavailableCodes: bool

    defaultAgentUnavailableCodeOnDND: Optional[str] = None

    defaultAgentUnavailableCodeOnPersonalCalls: Optional[str] = None

    defaultAgentUnavailableCodeOnConsecutiveBounces: Optional[str] = None

    defaultAgentUnavailableCodeOnNotReachable: Optional[str] = None

    defaultAgentUnavailableCode: Optional[str] = None


@dataclass
class GroupCallCenterBouncedCallGetResponse17(OCIDataResponse):
    """Response to the GroupCallCenterBouncedCallGetRequest17.

    The following elements are only used in AS data mode and not returned in XS data mode:
      enableTransfer
      transferPhoneNumber
      bounceCallWhenAgentUnavailable
      alertCallCenterCallOnHold
      alertCallCenterCallOnHoldSeconds
      bounceCallCenterCallOnHold
      bounceCallCenterCallOnHoldSeconds"""

    isActive: bool

    numberOfRingsBeforeBouncingCall: int

    enableTransfer: Optional[bool] = None

    transferPhoneNumber: Optional[str] = None

    bounceCallWhenAgentUnavailable: Optional[bool] = None

    alertCallCenterCallOnHold: Optional[bool] = None

    alertCallCenterCallOnHoldSeconds: Optional[int] = None

    bounceCallCenterCallOnHold: Optional[bool] = None

    bounceCallCenterCallOnHoldSeconds: Optional[int] = None


@dataclass
class GroupCallCenterCallDispositionCodeGetListResponse(OCIDataResponse):
    """Response to the GroupCallCenterCallDispositionCodeGetListRequest.
    Contains a table with column headings: \"Is Active\", \"Code\", \"Description\"."""

    dispositionCodesTable: OCITable


@dataclass
class GroupCallCenterCallDispositionCodeGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterCallDispositionCodeGetRequest"""

    isActive: bool

    description: Optional[str] = None


@dataclass
class GroupCallCenterCallDispositionCodeGetUsageListResponse(OCIDataResponse):
    """Response to the GroupCallCenterCallDispositionCodeGetUsageListRequest.
    The Type column contains either \"Call Center\" or \"Route Point\".
    Contains a table with column headings: \"Id\", \"Name\" and \"Type\"."""

    callCenterTable: OCITable


@dataclass
class GroupCallCenterComfortMessageBypassGetResponse20(OCIDataResponse):
    """Response to the GroupCallCenterComfortMessageBypassGetRequest20."""

    isActive: bool

    callWaitingAgeThresholdSeconds: int

    playAnnouncementAfterRinging: bool

    ringTimeBeforePlayingAnnouncementSeconds: int

    audioMessageSelection: str

    videoMessageSelection: str

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallCenterCurrentAndPastAgentGetListResponse(OCIDataResponse):
    """Response to the GroupCallCenterCurrentAndPastAgentGetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    agentUserTable: OCITable

    deletedAgentUserTable: OCITable


@dataclass
class GroupCallCenterCurrentAndPastCallCenterGetListResponse(OCIDataResponse):
    """Response to the GroupCallCenterCurrentAndPastCallCenterGetListRequest."""

    serviceUserId: List[str] = field(default_factory=list)

    deletedServiceUserId: List[str] = field(default_factory=list)


@dataclass
class GroupCallCenterCurrentAndPastDNISGetListResponse(OCIDataResponse):
    """Response to the GroupCallCenterCurrentAndPastDNISGetListRequest."""

    name: List[str] = field(default_factory=list)

    deletedName: List[str] = field(default_factory=list)


@dataclass
class GroupCallCenterDistinctiveRingingGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterDistinctiveRingingGetRequest.

    The following element is only used in AS data mode and not returned in XS data mode:
      distinctiveRingingForceDeliveryRingPattern"""

    distinctiveRingingCallCenterCalls: bool

    distinctiveRingingRingPatternForCallCenter: str

    distinctiveRingingForceDeliveryRingPattern: Optional[str] = None


@dataclass
class GroupCallCenterEnhancedReportingBrandingGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterEnhancedReportingBrandingGetRequest."""

    brandingChoice: str

    brandingFileDescription: Optional[str] = None


@dataclass
class GroupCallCenterEnhancedReportingGetAvailableReportTemplateListResponse(
    OCIDataResponse
):
    """Response to GroupCallCenterEnhancedReportingGetAvailableReportTemplateListRequest.
    Contains a table with column headings: \"Name\", \"Description\" and \"Level\", \"Is Agent Required\",
    \"Is Call Center Required\", \"Is Call Center Dnis Required\",\"Is Real Time Report\", \"Is Sampling Period Required\",
    \"Call Completion Threshold Parameter\", \"Short Duration Threshold Parameter\",
    \"Service Level Threshold Parameter\", \"Service Level Inclusions Parameter\", \"Service Level Objective Threshold Parameter\",
    \"Abandoned Call Threshold Parameter\", \"Service Level Threshold Parameter Number\",
    and \"Abandoned Call Threshold Parameter Number\".
    The possible values for \"Level\" are \"System\" and \"Group\".
    The possible values for \"Is Agent Required\", \"Is Call Center Required\", \"Is Call Center Dnis Required\",
    \"Is Real Time Report\" and \"Is Sampling Period Required\" are \"true\" and \"false\".
    The possible values for \"Call Completion Threshold Parameter\", \"Short Duration Threshold Parameter\",
    \"Service Level Threshold Parameter\", \"Service Level Inclusions Parameter\",\"Service Level Objective Threshold Parameter\"
    and \"Abandoned Call Threshold Parameter\" are \"Required\", \"Hidden\" and \"Does Not Apply\"."""

    reportTemplateTable: OCITable


@dataclass
class GroupCallCenterEnhancedReportingGetResponse19(OCIDataResponse):
    """Response to GroupCallCenterEnhancedReportingGetRequest19."""

    reportingServer: str


@dataclass
class GroupCallCenterEnhancedReportingReportTemplateGetListResponse(OCIDataResponse):
    """Response to GroupCallCenterEnhancedReportingReportTemplateGetListRequest.
    Contains a table with column headings: \"Name\", \"Description\", \"Type\" and \"Enabled\" """

    reportTemplateTable: OCITable


@dataclass
class GroupCallCenterEnhancedReportingReportTemplateGetResponse(OCIDataResponse):
    """Response to GroupCallCenterEnhancedReportingReportTemplateGetRequest."""

    dataTemplate: str

    xsltTemplateDescription: str

    scope: str

    isEnabled: bool

    description: Optional[str] = None

    filterNumber: Optional[int] = None

    isRealtimeReport: Optional[bool] = None

    callCompletionThresholdParam: Optional[str] = None

    shortDurationThresholdParam: Optional[str] = None

    serviceLevelThresholdParam: Optional[str] = None

    serviceLevelInclusionsParam: Optional[str] = None

    serviceLevelObjectiveThresholdParam: Optional[str] = None

    abandonedCallThresholdParam: Optional[str] = None

    serviceLevelThresholdParamNumber: Optional[int] = None

    abandonedCallThresholdParamNumber: Optional[int] = None

    filterValue: List[str] = field(default_factory=list)


@dataclass
class GroupCallCenterEnhancedReportingScheduledReportGetActiveListResponse(
    OCIDataResponse
):
    """Response to GroupCallCenterEnhancedReportingScheduledReportGetActiveListRequest
    Contains a table with column headings : \"Schedule Name\", \"Description\", \"Created By\",
    \"Is Supervisor Report\", \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Template Level\" are \"System\" and \"Group\"."""

    scheduledReportTable: OCITable


@dataclass
class GroupCallCenterEnhancedReportingScheduledReportGetCompletedListResponse(
    OCIDataResponse
):
    """Response to GroupCallCenterEnhancedReportingScheduledReportGetCompletedListRequest
    Contains a table with column headings : \"Schedule Name\", \"Description\", \"Created By\",
    \"Is Supervisor Report\", \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Template Level\" are \"System\" and \"Group\"."""

    scheduledReportTable: OCITable


@dataclass
class GroupCallCenterEnhancedReportingScheduledReportGetListResponse(OCIDataResponse):
    """Response to GroupCallCenterEnhancedReportingScheduledReportGetListRequest.
    Contains a table with column headings : \"Schedule Name\", \"Description\", \"Created By\",
    \"Is Supervisor Report\", \"Status\", \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Status\" are \"Active\", and \"Completed\".
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Template Level\" are \"System\" and \"Group\"."""

    scheduledReportTable: OCITable


@dataclass
class GroupCallCenterEnhancedReportingScheduledReportGetReportTemplateUsageListResponse(
    OCIDataResponse
):
    """Response to GroupCallCenterEnhancedReportingScheduledReportGetReportTemplateUsageListRequest.
    Contains a table with column headings: \"Schedule Name\", \"Created By\", \"Created By Supervisor\",
    and \"Is Active\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor."""

    scheduleReportTable: OCITable


@dataclass
class GroupCallCenterEnhancedReportingScheduledReportGetResponse(OCIDataResponse):
    """Response to GroupCallCenterEnhancedReportingScheduledReportGetRequest."""

    reportTemplate: CallCenterReportTemplateKey

    schedule: CallCenterReportSchedule

    reportTimeZone: str

    reportDateFormat: str

    reportTimeFormat: str

    reportInterval: CallCenterReportInterval

    reportFormat: str

    callCenter: CallCenterScheduledReportCallCenterSelectionRead

    dnis: CallCenterScheduledReportDNISSelectionRead

    description: Optional[str] = None

    samplingPeriod: Optional[str] = None

    startDayOfWeek: Optional[str] = None

    agent: Optional[CallCenterScheduledReportAgentSelectionAdminRead] = None

    callCompletionThresholdSeconds: Optional[int] = None

    shortDurationThresholdSeconds: Optional[int] = None

    serviceLevelThresholdSeconds: List[int] = field(default_factory=list)

    serviceLevelInclusions: Optional[
        CallCenterScheduledReportServiceLevelInclusions
    ] = None

    serviceLevelObjectivePercentage: Optional[int] = None

    abandonedCallThresholdSeconds: List[int] = field(default_factory=list)

    emailAddress: List[str] = field(default_factory=list)


@dataclass
class GroupCallCenterForcedForwardingGetResponse20(OCIDataResponse):
    """Response to the GroupCallCenterForcedForwardingGetRequest20."""

    isActive: bool

    allowEnableViaFAC: bool

    playAnnouncementBeforeForwarding: bool

    audioMessageSelection: str

    videoMessageSelection: str

    forwardToPhoneNumber: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallCenterGetAgentListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetAgentListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Weight\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"Skill Level\".

    The following column is only returned in AS data mode:
      \"Skill Level\" """

    agentTable: OCITable


@dataclass
class GroupCallCenterGetAgentPagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetAgentPagedSortedListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Weight\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"Skill Level\"."""

    agentTable: OCITable


@dataclass
class GroupCallCenterGetAnnouncementResponse22(OCIDataResponse):
    """Response to the GroupCallCenterGetAnnouncementRequest22."""

    playEntranceMessage: bool

    mandatoryEntranceMessage: bool

    entranceAudioMessageSelection: str

    playPeriodicComfortMessage: bool

    timeBetweenComfortMessagesSeconds: int

    periodicComfortAudioMessageSelection: str

    enableMediaOnHoldForQueuedCalls: bool

    mediaOnHoldSource: CallCenterMediaOnHoldSourceRead22

    estimatedWaitMessageOptionsRead: EstimatedWaitMessageOptionsRead17sp4

    entranceMessageAudioUrlList: Optional[CallCenterAnnouncementURLList] = None

    entranceMessageAudioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    entranceVideoMessageSelection: Optional[str] = None

    entranceMessageVideoUrlList: Optional[CallCenterAnnouncementURLList] = None

    entranceMessageVideoFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    periodicComfortMessageAudioUrlList: Optional[CallCenterAnnouncementURLList] = None

    periodicComfortMessageAudioFileList: Optional[
        CallCenterAnnouncementFileListRead20
    ] = None

    periodicComfortVideoMessageSelection: Optional[str] = None

    periodicComfortMessageVideoUrlList: Optional[CallCenterAnnouncementURLList] = None

    periodicComfortMessageVideoFileList: Optional[
        CallCenterAnnouncementFileListRead20
    ] = None

    mediaOnHoldUseAlternateSourceForInternalCalls: Optional[bool] = None

    mediaOnHoldInternalSource: Optional[CallCenterMediaOnHoldSourceRead22] = None

    playWhisperMessage: Optional[bool] = None

    whisperAudioMessageSelection: Optional[str] = None

    whisperMessageAudioUrlList: Optional[CallCenterAnnouncementURLList] = None

    whisperMessageAudioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    whisperVideoMessageSelection: Optional[str] = None

    whisperMessageVideoUrlList: Optional[CallCenterAnnouncementURLList] = None

    whisperMessageVideoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallCenterGetAvailableAgentListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetAvailableAgentListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallCenterGetAvailableAgentPagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetAvailableAgentPagedSortedListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallCenterGetAvailableSupervisorListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetAvailableSupervisorListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallCenterGetDNISAgentListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetDNISAgentListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    agentTable: OCITable


@dataclass
class GroupCallCenterGetDNISAnnouncementResponse22(OCIDataResponse):
    """Response to the GroupCallCenterGetDNISAnnouncementRequest22."""

    playEntranceMessage: bool

    mandatoryEntranceMessage: bool

    entranceAudioMessageSelection: str

    playPeriodicComfortMessage: bool

    timeBetweenComfortMessagesSeconds: int

    periodicComfortAudioMessageSelection: str

    enableMediaOnHoldForQueuedCalls: bool

    mediaOnHoldSource: CallCenterMediaOnHoldSourceRead22

    playWhisperMessage: bool

    whisperAudioMessageSelection: str

    estimatedWaitMessageOptionsRead: EstimatedWaitMessageOptionsRead17sp4

    entranceMessageAudioUrlList: Optional[CallCenterAnnouncementURLList] = None

    entranceMessageAudioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    entranceVideoMessageSelection: Optional[str] = None

    entranceMessageVideoUrlList: Optional[CallCenterAnnouncementURLList] = None

    entranceMessageVideoFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    periodicComfortMessageAudioUrlList: Optional[CallCenterAnnouncementURLList] = None

    periodicComfortMessageAudioFileList: Optional[
        CallCenterAnnouncementFileListRead20
    ] = None

    periodicComfortVideoMessageSelection: Optional[str] = None

    periodicComfortMessageVideoUrlList: Optional[CallCenterAnnouncementURLList] = None

    periodicComfortMessageVideoFileList: Optional[
        CallCenterAnnouncementFileListRead20
    ] = None

    whisperMessageAudioUrlList: Optional[CallCenterAnnouncementURLList] = None

    whisperMessageAudioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    whisperVideoMessageSelection: Optional[str] = None

    whisperMessageVideoUrlList: Optional[CallCenterAnnouncementURLList] = None

    whisperMessageVideoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallCenterGetDNISListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetDNISListResponse.
    Contains a table with column headings: \"Name\", \"Phone Number\", \"Extension\", \"Priority\", \"Is Primary DNIS\"."""

    displayDNISNumber: bool

    displayDNISName: bool

    promoteCallsFromPriority1to0: bool

    promoteCallsFromPriority2to1: bool

    promoteCallsFromPriority3to2: bool

    promoteCallsFromPriority1to0Seconds: int

    promoteCallsFromPriority2to1Seconds: int

    promoteCallsFromPriority3to2Seconds: int

    dnisTable: OCITable


@dataclass
class GroupCallCenterGetDNISResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetDNISResponse."""

    useCustomCLIDSettings: bool

    useCustomDnisAnnouncementSettings: bool

    priority: str

    allowOutgoingACDCall: bool

    dnisPhoneNumber: Optional[str] = None

    extension: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None

    callingLineIdLastName: Optional[str] = None

    callingLineIdFirstName: Optional[str] = None


@dataclass
class GroupCallCenterGetDistinctiveRingingResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetDistinctiveRingingRequest."""

    distinctiveRingingCallCenterCalls: bool

    distinctiveRingingRingPatternForCallCenter: str

    distinctiveRingingForceDeliveryRingPattern: Optional[str] = None


@dataclass
class GroupCallCenterGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Video\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\", \"Policy\", \"Type\".
    The column values for \"Video\" and \"Is Active\" can either be true, or false.
    The column values for \"Type\" can be \"Basic\", \"Standard\" or \"Premium\" in AS data mode and \"Basic\" in XS data mode.
    NOTE: prior to release 14, the policy column did not match the HuntPolicy enumerated type."""

    callCenterTable: OCITable


@dataclass
class GroupCallCenterGetInstancePagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetInstancePagedSortedListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Video\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\", \"Policy\", \"Type\".
    The column values for \"Video\" and \"Is Active\" can either be true, or false.
    The column values for \"Type\" can be \"Basic\", \"Standard\" or \"Premium\".
    NOTE: prior to release 14, the policy column did not match the HuntPolicy enumerated type."""

    callCenterTable: OCITable


@dataclass
class GroupCallCenterGetInstanceQueueStatusResponse(OCIDataResponse):
    """Contains Call Center queue status and a table with column headings:
    \"User Id\", \"First Name\", \"Last Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    numberOfCallsQueuedNow: int

    agentsCurrentlyStaffed: OCITable


@dataclass
class GroupCallCenterGetInstanceResponse22(OCIDataResponse):
    """Response to GroupCallCenterGetInstanceRequest22.

    The following elements are only used in AS data mode and not returned in XS data mode:
      routingType
      enableReporting
      allowCallsToAgentsInWrapUp
      overrideAgentWrapUpTime
      wrapUpSeconds
      forceDeliveryOfCalls
      forceDeliveryWaitTimeSeconds
      enableAutomaticStateChangeForAgents
      agentStateAfterCall
      agentUnavailableCode
      callCenterQueueThresholdsIsActive
      networkClassOfService"""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    type: str

    policy: str

    enableVideo: bool

    queueLength: int

    allowCallerToDialEscapeDigit: bool

    escapeDigit: str

    resetCallStatisticsUponEntryInQueue: bool

    allowAgentLogoff: bool

    allowCallWaitingForAgents: bool

    externalPreferredAudioCodec: str

    internalPreferredAudioCodec: str

    playRingingWhenOfferingCall: bool

    routingType: Optional[str] = None

    enableReporting: Optional[bool] = None

    allowCallsToAgentsInWrapUp: Optional[bool] = None

    overrideAgentWrapUpTime: Optional[bool] = None

    wrapUpSeconds: Optional[int] = None

    forceDeliveryOfCalls: Optional[bool] = None

    forceDeliveryWaitTimeSeconds: Optional[int] = None

    enableAutomaticStateChangeForAgents: Optional[bool] = None

    agentStateAfterCall: Optional[str] = None

    agentUnavailableCode: Optional[str] = None

    callCenterQueueThresholdsIsActive: Optional[bool] = None

    networkClassOfService: Optional[str] = None


@dataclass
class GroupCallCenterGetInstanceStatisticsReportingResponse17sp1(OCIDataResponse):
    """Response to GroupCallCenterGetInstanceStatisticsReportingRequest17sp1.
    Contains Call Center statistics reporting settings."""

    generateDailyReport: bool

    collectionPeriodMinutes: int

    statisticsSource: str

    reportingEmailAddress1: Optional[str] = None

    reportingEmailAddress2: Optional[str] = None


@dataclass
class GroupCallCenterGetInstanceStatisticsResponse14sp9(OCIDataResponse):
    """Contains Call Center statistics."""

    statisticsRange: CallCenterStatisticsRange

    queueStatistics: CallCenterQueueStatistics14sp9

    agentStatistics: List[CallCenterAgentStatistics14sp9] = field(default_factory=list)


@dataclass
class GroupCallCenterGetResponse23(OCIDataResponse):
    """Response to GroupCallCenterGetRequest23.

    The following elements are only used in AS data mode and not returned in XS data mode:
      useSystemDefaultUnavailableSettings
      forceAgentUnavailableOnDNDActivation
      forceAgentUnavailableOnPersonalCalls
      forceAgentUnavailableOnBouncedCallLimit
      numberConsecutiveBouncedCallsToForceAgentUnavailable
      forceAgentUnavailableOnNotReachable
      wrapUpDestination"""

    useSystemDefaultGuardTimer: bool

    enableGuardTimer: bool

    guardTimerSeconds: int

    useSystemDefaultUnavailableSettings: Optional[bool] = None

    forceAgentUnavailableOnDNDActivation: Optional[bool] = None

    forceAgentUnavailableOnPersonalCalls: Optional[bool] = None

    forceAgentUnavailableOnBouncedCallLimit: Optional[bool] = None

    numberConsecutiveBouncedCallsToForceAgentUnavailable: Optional[int] = None

    forceAgentUnavailableOnNotReachable: Optional[bool] = None

    wrapUpDestination: Optional[str] = None


@dataclass
class GroupCallCenterGetRoutingPolicyResponse(OCIDataResponse):
    """Response to GroupCallCenterGetRoutingPolicyRequest.
    Contains a table with column headings: \"Service User Id\", \"Name\" and
    \"Priority\"."""

    routingPolicy: str

    callCenterTable: OCITable


@dataclass
class GroupCallCenterGetSupervisorListResponse16(OCIDataResponse):
    """Response to the GroupCallCenterGetSupervisorListRequest16.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    supervisorTable: OCITable


@dataclass
class GroupCallCenterGetUnlicensedAgentListResponse(OCIDataResponse):
    """Response to the GroupCallCenterGetUnlicensedAgentListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\", \"Group Id\",
    \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallCenterHolidayServiceGetResponse20(OCIDataResponse):
    """Response to the GroupCallCenterHolidayServiceGetRequest20."""

    action: str

    playAnnouncementBeforeAction: bool

    audioMessageSelection: str

    videoMessageSelection: str

    holidaySchedule: Optional[HolidaySchedule] = None

    transferPhoneNumber: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallCenterMonitoringGetResponse(OCIDataResponse):
    """Response to GroupCallCenterMonitoringGetRequest."""

    enableSupervisorCoaching: bool


@dataclass
class GroupCallCenterNightServiceGetResponse20(OCIDataResponse):
    """Response to the GroupCallCenterNightServiceGetRequest20."""

    action: str

    forceNightService: bool

    allowManualOverrideViaFAC: bool

    playAnnouncementBeforeAction: bool

    audioMessageSelection: str

    videoMessageSelection: str

    manualAnnouncementMode: str

    manualAudioMessageSelection: str

    manualVideoMessageSelection: str

    businessHours: Optional[TimeSchedule] = None

    transferPhoneNumber: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    manualAudioUrlList: Optional[CallCenterAnnouncementURLList] = None

    manualAudioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    manualVideoUrlList: Optional[CallCenterAnnouncementURLList] = None

    manualVideoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallCenterOverflowGetResponse20(OCIDataResponse):
    """Response to the GroupCallCenterOverflowGetRequest20."""

    action: str

    overflowAfterTimeout: bool

    timeoutSeconds: int

    playAnnouncementBeforeOverflowProcessing: bool

    audioMessageSelection: str

    transferPhoneNumber: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoMessageSelection: Optional[str] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallCenterQueueCallDispositionCodeGetListResponse(OCIDataResponse):
    """Response to the GroupCallCenterQueueCallDispositionCodeGetListRequest.
    Contains a table with column headings: \"Is Active\", \"Code\", \"Description\" and \"Level\".
    Level column can be any of the values in the data type CallDispositionCodeLevel."""

    dispositionCodesTable: OCITable


@dataclass
class GroupCallCenterQueueCallDispositionCodeGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterQueueCallDispositionCodeGetRequest"""

    isActive: bool

    description: Optional[str] = None


@dataclass
class GroupCallCenterQueueCallDispositionCodeSettingsGetResponse(OCIDataResponse):
    """Response to GroupCallCenterQueueCallDispositionCodeSettingsGetRequest."""

    enableCallDispositionCodes: bool

    includeOrganizationCodes: bool

    forceUseOfCallDispositionCodes: bool

    defaultCallDispositionCode: Optional[CallDispositionCodeWithLevel] = None


@dataclass
class GroupCallCenterQueueStatusNotificationGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterQueueStatusNotificationGetRequest.
    The response contains the call center status configuration information."""

    enableQueueStatusNotification: bool

    enableQueueDepthThreshold: bool

    enableWaitingTimeThreshold: bool

    numberOfCallsThreshold: int

    waitingTimeOfCallsThreshold: int


@dataclass
class GroupCallCenterQueueThresholdsGetResponse(OCIDataResponse):
    """Response to the GroupCallCenterQueueThresholdsGetRequest."""

    isActive: bool

    enableNotificationEmail: bool

    thresholdCurrentCallsInQueueYellow: Optional[int] = None

    thresholdCurrentCallsInQueueRed: Optional[int] = None

    thresholdCurrentLongestWaitingCallYellow: Optional[int] = None

    thresholdCurrentLongestWaitingCallRed: Optional[int] = None

    thresholdAverageEstimatedWaitTimeYellow: Optional[int] = None

    thresholdAverageEstimatedWaitTimeRed: Optional[int] = None

    thresholdAverageHandlingTimeYellow: Optional[int] = None

    thresholdAverageHandlingTimeRed: Optional[int] = None

    thresholdAverageSpeedOfAnswerYellow: Optional[int] = None

    thresholdAverageSpeedOfAnswerRed: Optional[int] = None

    notificationEmailAddress: List[str] = field(default_factory=list)


@dataclass
class GroupCallCenterStrandedCallGetResponse20(OCIDataResponse):
    """Response to the GroupCallCenterStrandedCallGetRequest20."""

    action: str

    transferPhoneNumber: Optional[str] = None

    audioMessageSelection: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoMessageSelection: Optional[str] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallCenterStrandedCallUnavailableGetResponse20(OCIDataResponse):
    """Response to the GroupCallCenterStrandedCallUnavailableGetRequest20."""

    conditionPolicyOnNumberOfAgentsWithSpecifiedUnavailableCode: bool

    action: str

    numberOfAgentsWithSpecifiedUnavailableCode: Optional[int] = None

    agentsUnavailableCode: Optional[str] = None

    transferPhoneNumber: Optional[str] = None

    audioMessageSelection: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoMessageSelection: Optional[str] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupCallParkGetAvailableAlternateRecallUserListResponse(OCIDataResponse):
    """Response to the GroupCallParkGetAvailableAlternateRecallUserListResponse.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\"."""

    availableHuntGroupTable: OCITable


@dataclass
class GroupCallParkGetAvailableAlternateRecallUserPagedSortedListResponse(
    OCIDataResponse
):
    """Response to the GroupCallParkGetAvailableAlternateRecallUserPagedSortedListResponse.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\". The Email Address will never be populated, since Hunt Groups don't
    have Email Addresses."""

    availableHuntGroupTable: OCITable


@dataclass
class GroupCallParkGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupCallParkGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallParkGetAvailableUserPagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCallParkGetAvailableUserPagedSortedListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallParkGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupCallParkGetInstanceListRequest."""

    name: List[str] = field(default_factory=list)


@dataclass
class GroupCallParkGetInstancePagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCallParkGetInstancePagedSortedListRequest."""

    name: List[str] = field(default_factory=list)


@dataclass
class GroupCallParkGetInstancePagedSortedResponse(OCIDataResponse):
    """Response to the GroupCallParkGetInstancePagedSortedRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\".
    The users are in the table are in the order they will try to be parked on."""

    recallTo: str

    userTable: OCITable

    recallAlternateUserId: Optional[str] = None


@dataclass
class GroupCallParkGetInstanceResponse16sp2(OCIDataResponse):
    """Response to the GroupCallParkGetInstanceRequest16sp2.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\".
    The users are in the table are in the order they will try to be parked on."""

    recallTo: str

    userTable: OCITable

    recallAlternateUserId: Optional[str] = None


@dataclass
class GroupCallParkGetResponse16sp2(OCIDataResponse):
    """Response to the GroupCallParkGetRequest16sp2.
    Contains the settings that apply to the whole group for Call Park."""

    recallTimerSeconds: int

    displayTimerSeconds: int

    enableDestinationAnnouncement: bool

    recallRingPattern: str

    recallTo: str

    alternateUserRecallTimerSeconds: int

    recallAlternateUserId: Optional[str] = None


@dataclass
class GroupCallPickupGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupCallPickupGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallPickupGetAvailableUserPagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCallPickupGetAvailableUserPagedSortedListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallPickupGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupCallPickupGetInstanceListRequest."""

    name: List[str] = field(default_factory=list)


@dataclass
class GroupCallPickupGetInstancePagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCallPickupGetInstancePagedSortedListRequest."""

    name: List[str] = field(default_factory=list)


@dataclass
class GroupCallPickupGetInstancePagedSortedResponse(OCIDataResponse):
    """Response to the GroupCallPickupGetInstancePagedSortedRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallPickupGetInstanceResponse(OCIDataResponse):
    """Response to the GroupCallPickupGetInstanceRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCallProcessingGetPolicyResponse22V3(OCIDataResponse):
    """Response to GroupCallProcessingGetPolicyRequest22V3.
    The following elements are not returned for a group within a service provider:
      enableGatewayRoutePolicy
      networkCallsGatewayRouteIdentity
      networkURLCallsGatewayRouteIdentity
      emergencyCallsGatewayRouteIdentity
      repairCallsGatewayRouteIdentity
      callTypingErrorsGatewayRouteIdentity

    The following elements are only used in AS data mode:
      useGroupDCLIDSetting
      enableDialableCallerID
      allowConfigurableCLIDForRedirectingIdentity
      allowDepartmentCLIDNameOverride
      enterpriseCallsCLIDPolicy, value \"Use Location Code plus Extension\" is returned in XS data mode.
      groupCallsCLIDPolicy, value \"Use Extension\" is returned in XS data mode.
      useGroupPhoneListLookupSetting, value \"false\" is returned in XS data mode.
      enablePhoneListLookup, value \"false\" is returned in XS data mode.
      useMaxConcurrentTerminatingAlertingRequests, value \"false\" is returned in XS data mode.
      maxConcurrentTerminatingAlertingRequests, value \"10\" is returned in XS data mode.
      includeRedirectionsInMaximumNumberOfConcurrentCalls, value \"false\" is returned in XS data mode.
      useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable, value \"false\" is returned in XS data mode.
      useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable, value \"false\" is returned in XS data mode.
      allowMobileDNForRedirectingIdentity,value \"false\" is returned in XS data mode.

    The following elements are only used in AS data mode and not returned in XS data mode:
      enableGatewayRoutePolicy
      networkCallsGatewayRouteIdentity
      networkURLCallsGatewayRouteIdentity
      emergencyCallsGatewayRouteIdentity
      repairCallsGatewayRouteIdentity
      callTypingErrorsGatewayRouteIdentity

    The following elements are only used in XS data mode and not returned in AS data mode:
      routeOverrideDomain
      routeOverridePrefix"""

    useGroupCLIDSetting: bool

    useGroupMediaSetting: bool

    useGroupCallLimitsSetting: bool

    useGroupTranslationRoutingSetting: bool

    useGroupDCLIDSetting: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    mediaPolicySelection: str

    networkUsageSelection: str

    enforceGroupCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    enableEnterpriseExtensionDialing: bool

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    enableDialableCallerID: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    groupCallsCLIDPolicy: str

    useGroupPhoneListLookupSetting: bool

    enablePhoneListLookup: bool

    useMaxConcurrentTerminatingAlertingRequests: bool

    maxConcurrentTerminatingAlertingRequests: int

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    allowMobileDNForRedirectingIdentity: bool

    supportedMediaSetName: Optional[str] = None

    overrideCLIDRestrictionForPrivateCallCategory: Optional[bool] = None

    useEnterpriseCLIDForPrivateCallCategory: Optional[bool] = None

    routeOverrideDomain: Optional[str] = None

    routeOverridePrefix: Optional[str] = None

    enableGatewayRoutePolicy: Optional[bool] = None

    networkCallsGatewayRouteIdentity: Optional[str] = None

    networkURLCallsGatewayRouteIdentity: Optional[str] = None

    emergencyCallsGatewayRouteIdentity: Optional[str] = None

    repairCallsGatewayRouteIdentity: Optional[str] = None

    callTypingErrorsGatewayRouteIdentity: Optional[str] = None


@dataclass
class GroupCallRecordingGetResponse(OCIDataResponse):
    """Response to the GroupCallRecordingGetRequest.
    The response contains the group's Call Recording platform information."""

    name: Optional[str] = None


@dataclass
class GroupCallingPlanGetDigitPatternListResponse(OCIDataResponse):
    """Response to GroupCallingPlanGetDigitPatternListRequest.
    Contains a table with column headings: \"Name\", \"Digit Pattern\"."""

    digitPatternTable: OCITable


@dataclass
class GroupCollaborateBridgeGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupCollaborateBridgeGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", and \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Department Type\", \"Parent Department\", \"Parent Department Type\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupCollaborateBridgeGetAvailableUserPagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCollaborateBridgeGetAvailableUserPagedSortedListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Is Phone Number Activated\", \"Country Code\",\"National Prefix\", \"Extension\", \"Department\", \"Department Type\",
    \"Parent Department\", \"Parent Department Type\", \"Email Address\", \"IMP Id\", \"Mobile Number\", \"Group Id\", \"Group Name\"."""

    userTable: OCITable


@dataclass
class GroupCollaborateBridgeGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupCollaborateBridgeGetInstanceListRequest.
    Contains a table with column headings: \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Participants\", and \"Is Default\".
    The column values for \"Is default\" can either be true, or false."""

    collaborateBridgeTable: OCITable


@dataclass
class GroupCollaborateBridgeGetInstancePagedSortedListResponse(OCIDataResponse):
    """Response to the GroupCollaborateBridgeGetInstancePagedSortedListRequest.
    Contains a table with column headings: \"Service User Id\", \"Name\", \"Phone Number\", \"Is Phone Number Activated\",
    \"Country Code\",\"National Prefix\", \"Extension\", \"Department\", \"Department Type\",
    \"Parent Department\", \"Parent Department Type\", \"Participants\", \"Is Default\", \"Max Room Participants\",
    \"Is Support Outdial\".
    The column values for \"Is default\", \"Is Support Outdial\" can either be true, or false."""

    collaborateBridgeTable: OCITable


@dataclass
class GroupCollaborateBridgeGetInstanceResponse20sp1(OCIDataResponse):
    """Response to GroupCollaborateBridgeGetInstanceRequest20sp1.
    The system-level collaborate supportOutdial setting is returned in the response when the system-level collaborate
    supportOutdial setting is disabled.
    Contains the service profile information and a table of assigned owners.
    The table has column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", Phone Number\", \"Extension\", \"Department\", \"Email Address\",
    \"Is Phone Number Activated\", \"Country Code\", \"National Prefix\", \"Department Name\",
    \"Department Type\", \"Parent Department\", \"Parent Department Type\", \"Group Id\", \"Group Name\".
    Collaborate bridge maximum participant’s choices unlimited or a quantified number of participants."""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    maximumBridgeParticipants: CollaborateBridgeMaximumParticipants

    isDefault: bool

    maxCollaborateRoomParticipants: int

    supportOutdial: bool

    networkClassOfService: Optional[str] = None

    collaborateOwnerUserTable: Optional[OCITable] = None


@dataclass
class GroupCommonPhoneListGetListResponse(OCIDataResponse):
    """Response to the GroupCommonPhoneListGetListRequest.
    The response contains the group's common phone list."""

    entry: List[PhoneListEntry] = field(default_factory=list)


@dataclass
class GroupCommunicationBarringAuthorizationCodeGetListResponse21sp1(OCIDataResponse):
    """Response to GroupCommunicationBarringAuthorizationCodeGetListRequest21sp1.
    Contains a list of Communication Barring Authorization Codes assigned to the group."""

    code: List[CommunicationBarringAuthorizationCodeConfiguration] = field(
        default_factory=list
    )


@dataclass
class GroupCommunicationBarringAuthorizationCodeGetResponse(OCIDataResponse):
    """Response to GroupCommunicationBarringAuthorizationCodeGetRequest."""

    description: Optional[str] = None

    networkClassOfService: Optional[str] = None


@dataclass
class GroupCommunicationBarringGetResponse(OCIDataResponse):
    """Response to GroupCommunicationBarringGetRequest."""

    useDefaultServiceProviderProfile: bool

    profile: Optional[str] = None


@dataclass
class GroupCommunicationBarringProfileGetAssignedListResponse(OCIDataResponse):
    """Response to the GroupCommunicationBarringProfileGetAssignedListRequest.
    The response contains a simple list of all communication barring profiles assigned to the group."""

    profileName: List[str] = field(default_factory=list)


@dataclass
class GroupConsolidatedAddResponse22(OCIDataResponse):
    """Response to GroupConsolidatedAddRequest22."""

    dnValidationError: List[DNValidationStatusMessage] = field(default_factory=list)


@dataclass
class GroupConsolidatedDnAssignListResponse(OCIDataResponse):
    """Response to GroupConsolidatedDnAssignListRequest."""

    dnValidationError: List[DNValidationStatusMessage] = field(default_factory=list)


@dataclass
class GroupCustomContactDirectoryGetAvailableUserListResponse17(OCIDataResponse):
    """Response to the
    GroupCustomContactDirectoryGetAvailableUserListRequest17.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Virtual On-Net Phone Number\", \"Group Id\", \"Is Virtual On-Net User\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\".

    If the entry represents a Virtual On-Net user then \"User Id\" is blank,
    the \"Virtual On-Net Phone Number\" contains the phone Number of the
    Virtual On-Net user, the \"Group Id\" contains the Virtual On-Net user's
    group and the \"Is Virtual On-Net User\" contains true.

    If the entry represents a BroadWorks user then the \"User Id\" contains
    his BroadWorks userId, the \"Virtual On-Net Phone Number\" and
    \"Group Id\" fields are blank and the \"Is Virtual On-Net User\"
    contains false."""

    userTable: OCITable


@dataclass
class GroupCustomContactDirectoryGetListResponse(OCIDataResponse):
    """Response to the GroupCustomContactDirectoryGetListRequest.
    The response contains all the group's custom contact directory names."""

    name: List[str] = field(default_factory=list)


@dataclass
class GroupCustomContactDirectoryGetResponse17(OCIDataResponse):
    """Response to the GroupCustomContactDirectoryGetRequest17.
    The response contains all the contacts in the group's given custom
    contact directory. Contains a table with column headings: \"User Id\",
    \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Virtual On-Net Phone Number\", \"Group Id\",
    \"Is Virtual On-Net User\", \"Department\", \"Phone Number\", \"Extension\",
    \"Mobile\", \"Email Address\", \"Yahoo Id\", \"Title\", \"IMP Id\", \"Receptionist Note\".
    If the entry represents a Virtual On-Net user then \"User Id\" is blank,
    the \"Virtual On-Net Phone Number\" contains the phone Number of the
    Virtual On-Net user, the \"Group Id\" contains the Virtual On-Net user's
    group and the \"Is Virtual On-Net User\" contains true.
    If the entry represents a BroadWorks user then the \"User Id\" contains
    his BroadWorks userId, the \"Virtual On-Net Phone Number\" and
    \"Group Id\" fields are field is blank and the \"Is Virtual On-Net User\"
    contains false.  The Receptionist Note column is only populated in AS
    Mode, if the user sending the request is the owner of the Receptionist
    Note and a Note exists."""

    userTable: OCITable


@dataclass
class GroupCustomRingbackGroupGetResponse20(OCIDataResponse):
    """Response to the GroupCustomRingbackGroupGetRequest20."""

    isActive: bool

    audioSelection: str

    videoSelection: str

    audioFile: Optional[AnnouncementFileKey] = None

    audioFileUrl: Optional[str] = None

    videoFile: Optional[AnnouncementFileKey] = None

    videoFileUrl: Optional[str] = None


@dataclass
class GroupDepartmentAdminGetListResponse(OCIDataResponse):
    """Response to GroupDepartmentAdminGetListRequest.
    Contains a 5 column table with column headings \"Administrator ID\",
    \"Last Name\", \"First Name\", \"Department\", \"Language\"."""

    departmentAdminTable: OCITable


@dataclass
class GroupDepartmentAdminGetResponse22V2(OCIDataResponse):
    """Response to the GroupDepartmentAdminGetRequest22V2.
    The response contains the group department administrators profile information.

    The following elements are only used in AS data mode and ignored in XS data mode.
    accountDisabled
    lastAuthenticatedDate
    hasPassword"""

    departmentKey: GroupDepartmentKey

    departmentFullPath: str

    language: str

    accountDisabled: bool

    lastAuthenticatedDate: str

    hasPassword: bool

    firstName: Optional[str] = None

    lastName: Optional[str] = None


@dataclass
class GroupDepartmentGetAvailableParentListResponse(OCIDataResponse):
    """Response to GroupDepartmentGetAvailableParentListRequest.
    The response includes two parallel arrays of department keys and department display names."""

    departmentKey: List[DepartmentKey] = field(default_factory=list)

    fullPathName: List[str] = field(default_factory=list)


@dataclass
class GroupDepartmentGetListResponse18(OCIDataResponse):
    """Response to GroupDepartmentGetListRequest18.
    Contains a table of department attributes.
    The column headings are: \"Is Enterprise Department\", \"Department Name\", \"Full Path Name\", \"Calling Line Id Name\", and \"Calling Line Id Phone Number\" """

    departmentTable: OCITable


@dataclass
class GroupDepartmentGetResponse(OCIDataResponse):
    """Response to GroupDepartmentGetRequest.
    The following elements are only used in AS data mode:
      callingLineIdName
      caliingLineIdPhoneNumber"""

    parentDepartmentKey: Optional[DepartmentKey] = None

    callingLineIdName: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class GroupDeviceActivationPolicyGetResponse(OCIDataResponse):
    """Response to GroupDeviceActivationPolicyGetRequest."""

    useGroupSettings: bool

    allowActivationCodeRequestByUser: bool

    sendActivationCodeInEmail: bool


@dataclass
class GroupDeviceManagementEventGetListResponse22(OCIDataResponse):
    """Response to GroupDeviceManagementEventGetListRequest22.
    Contains a table with column headings: \"Event Id\", \"Status\", \"Action\",
    \"Level\", \"Type\", \"Additional Info\", \"Is Local\", \"Completion %\",
    \"Pushed/ Same Hash/ Not Pushed\", \"Login Id\", \"Start Time\",
    \"Process Time\", \"Rx Time\", \"Total Time\", \"Request\", \"Priority\",
    \"Tracking Id\", \"End Time\".
    \"Event Id\" is a unique identifier for the event.
    \"Status\" can be: Pending, Queued, In Progress,
    Process On Other Host, Stale, Completed, Canceled.
    \"Action\" can be: Delete, Download, Rebuild, Reset, Upload.
    \"Level\" can be: Device, Device Type, Device Type Group, Group, User.
    \"Type\" can be: Automatic, Manual.
    \"Additional Info\" includes the affected device type, device or group.
    It depends on the level of the event:
      Device Profile: \"Device Name\" \"Service Provider Id\" \"Group Id\"
      Device Type: \"Device Type Name\"
      Device Type Service Provider: \"Service Provider Id\" \"Device Type Name\"
      Service Provider: \"Service Provider Id\"
      Device Type Group: \"Service Provider Id\" \"Group Id\" \"Device Type Name\"
      Group: \"Service Provider Id\" \"Group Id\"
      User: \"User Id\"
    \"Is Local\" is set to \"yes\" if the event is processed on the server
    who received the request, \"no\" otherwise meaning that the event is
    processed on another server.
    \"Completion %\" provides an estimate of the completion of the event.
    A percentage is given, the current number of completed expanded event,
    and the total number of expanded event.
    \"Pushed/ Same Hash/ Not Pushed\" gives the total number of files that
    were pushed, not pushed because of same hash, and not pushed when
    processing the event.
    \"LoginId\" is the user or admin id who triggered the event.
    \"Start Time\" is the date when the event's processing started.  The
    display shows the month, day, hours, minutes, and seconds (MM-dd hh:mm:ss).
    \"Process Time\" is the time taken to process the event in hours,
    minutes, seconds, and milliseconds (hhhh:mm:ss.SSS).
    \"Rx Time\" is the date when the event was received via OCI-P and
    stored in the system.  The display shows the month, day, hours,
    minutes, and seconds (MM-dd hh:mm:ss).
    \"Total Time\" is the total time the event was in the system, from the
    moment it was received and stored until its processing ended, in
    hours, minutes, seconds, and milliseconds (hhhh:mm:ss.SSS).
    \"Request\" is the name of the OCI-P request that triggered the event.
    \"Priority\" is the priority of the event.
    \"Tracking Id\" is the tracking id of the OCI-P request that triggered the event.
    \"End Time\" is the difference, measured in milliseconds, between the
    event's end time and midnight, January 1, 1970 UTC"""

    eventTable: OCITable


@dataclass
class GroupDeviceManagementGetAccessDeviceCountForDeviceTypeGroupResponse(
    OCIDataResponse
):
    """Response to GroupDeviceManagementGetAccessDeviceCountForDeviceTypeGroupRequest."""

    accessDeviceCount: int


@dataclass
class GroupDeviceTypeCustomTagGetListResponse(OCIDataResponse):
    """Response to GroupDeviceTypeCustomTagGetListRequest.
    Contains a table of custom configuration tags managed by the Device Management System on a per-device type basis for a group.
    In As data mode, the column headings are:
      \"Tag Name\", \"Tag Value\", \"Actual Tag Value\".
    In XS data mode, the column headings are:
      \"Tag Name\", \"Tag Value\", \"Actual Tag Value\" if request is invoked by an admin without system privileges.
      \"Tag Name\", \"Tag Value\", \"Is Encrypted\", \"Actual Tag Value\" if request is invoked by an admin with system privileges."""

    groupDeviceTypeCustomTagsTable: OCITable


@dataclass
class GroupDeviceTypeFileGetListResponse21(OCIDataResponse):
    """Response to GroupDeviceTypeFileGetListRequest21.
    Contains a table of device type files managed by the Device Management System, on a per-group basis.
    The column headings are: \"File Format\", \"Is Authenticated\", \"Access URL\", \"Repository URL\", \"Template URL\"."""

    groupDeviceTypeFilesTable: OCITable

    groupHasCustomizableDynamicFiles: bool


@dataclass
class GroupDeviceTypeFileGetResponse16sp1(OCIDataResponse):
    """Response to GroupDeviceTypeFileGetRequest16sp1."""

    accessUrl: str

    fileSource: Optional[str] = None

    configurationFileName: Optional[str] = None

    repositoryUrl: Optional[str] = None

    templateUrl: Optional[str] = None


@dataclass
class GroupDeviceTypeTagSetGetResponse(OCIDataResponse):
    """Response to GroupDeviceTypeTagSetGetRequest."""

    tagSetName: Optional[str] = None


@dataclass
class GroupDialPlanPolicyGetAccessCodeListResponse(OCIDataResponse):
    """Response to GroupDialPlanPolicyGetAccessCodeListRequest
    Contains a table with column headings: \"Access Code\",
    \"Enable Secondary Dial Tone\", \"Description\" """

    accessCodeTable: OCITable


@dataclass
class GroupDialPlanPolicyGetAccessCodeResponse(OCIDataResponse):
    """Response to GroupDialPlanPolicyGetAccessCodeRequest"""

    includeCodeForNetworkTranslationsAndRouting: bool

    includeCodeForScreeningServices: bool

    enableSecondaryDialTone: bool

    description: Optional[str] = None


@dataclass
class GroupDialPlanPolicyGetResponse22(OCIDataResponse):
    """Response to GroupDialPlanPolicyGetRequest22
    The following elements are only used in AS data mode:
      overrideResolvedDeviceDigitMap
    The following elements are only used in AS data mode and not returned in XS data mode:
      deviceDigitMap"""

    useSetting: str

    requiresAccessCodeForPublicCalls: bool

    allowE164PublicCalls: bool

    preferE164NumberFormatForCallbackServices: bool

    overrideResolvedDeviceDigitMap: bool

    publicDigitMap: Optional[str] = None

    privateDigitMap: Optional[str] = None

    deviceDigitMap: Optional[str] = None


@dataclass
class GroupDialableCallerIDCriteriaGetResponse(OCIDataResponse):
    """Response to the GroupDialableCallerIDCriteriaGetRequest.
    The response contains the Dialable Caller ID Criteria information."""

    matchLocalCategory: bool

    matchNationalCategory: bool

    matchInterlataCategory: bool

    matchIntralataCategory: bool

    matchInternationalCategory: bool

    matchPrivateCategory: bool

    matchEmergencyCategory: bool

    matchOtherCategory: bool

    description: Optional[str] = None

    prefixDigits: Optional[str] = None

    matchCallType: List[str] = field(default_factory=list)

    matchAlternateCallIndicator: List[str] = field(default_factory=list)


@dataclass
class GroupDialableCallerIDGetResponse(OCIDataResponse):
    """Response to the GroupDialableCallerIDGetRequest.
    The criteria table's column headings are \"Active\", \"Name\", \"Description\", \"Prefix Digits\", \"Priority\"."""

    useGroupCriteria: bool

    nsScreeningFailurePolicy: str

    criteriaTable: OCITable


@dataclass
class GroupDigitCollectionGetResponse13mp4(OCIDataResponse):
    """Response to GroupDigitCollectionGetRequest13mp4."""

    useSetting: str

    accessCode: Optional[str] = None

    publicDigitMap: Optional[str] = None

    privateDigitMap: Optional[str] = None


@dataclass
class GroupDirectoryNumberHuntingGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupDirectoryNumberHuntingGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupDirectoryNumberHuntingGetResponse17sp1(OCIDataResponse):
    """Response to the GroupDirectoryNumberHuntingGetRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    agentUserTable: OCITable

    useTerminateCallToAgentFirst: bool

    useOriginalAgentServicesForBusyAndNoAnswerCalls: bool


@dataclass
class GroupDnGetActivationListResponse(OCIDataResponse):
    """Response to the GroupDnGetActivationListRequest.
    The response contains a table with columns: \"Phone Numbers\", and \"Activated\".  \".  Phone Numbers are only returned if assigned to a user.
    The \"Phone Numbers\" column contains either a single DN or a range of DNs.
    The \"Activated\" column indicates if the phone number(s) are activated or not."""

    dnTable: OCITable


@dataclass
class GroupDnGetAssignmentListResponse18(OCIDataResponse):
    """Response to the GroupDnGetAssignmentListRequest18.
    The response contains a table with columns: \"Phone Numbers\", \"Department\", \"Activated\", \"User Id\",
    \"Last Name\", \"First Name\", \"Extension\", \"Email Address\", \"User Type\", \"Country Code\", \"National Prefix\".
    The \"Phone Numbers\" column contains either a single DN or a range of DNs.
    The \"User Id\", \"Last Name\" and \"First Name\" columns contains the corresponding attributes of the user possessing the DN(s).
    For a service instance, \"Last Name\" contains the service instance name and \"First Name\" column contains the corresponding enumerated UserType value.
    The \"Department\" column contains the department of the DN, not the department of the user or service instance.
    The \"Activated\" column indicates if the DN or DN range has been activated.
    The \"User Type\" column contains the corresponding enumerated UserType value.
    The \"Country Code\" column indicates the dialing prefix for the phone number.
    The \"National Prefix\" column indicates the digit sequence to be dialed before the telephone number.
    NOTE: the same phone number can show up in the list twice if the phone number is being used as the group calling line Id."""

    dnTable: OCITable


@dataclass
class GroupDnGetAssignmentPagedSortedListResponse(OCIDataResponse):
    """Response to the GroupDnGetAssignmentPagedSortedListRequest.

    The response contains a table with columns: \"Phone Numbers\", \"Department\", \"Department Type\",
    \"Parent Department\", \"Parent Department Type\", \"Activated\", \"Available\", \"User Id\",
    \"Last Name\", \"First Name\", \"Extension\", \"Email Address\", \"User Type\", \"Country Code\", \"National Prefix\".
    The \"Phone Numbers\" column contains either a single DN or a range of DNs.
    The \"User Id\", \"Last Name\" and \"First Name\" columns contains the corresponding attributes of the user possessing the DN(s).
    For a service instance, \"Last Name\" contains the service instance name and \"First Name\" column contains the corresponding enumerated UserType value.
    The \"Department\" column contains the department of the DN, not the department of the user or service instance.
    The \"Department Type\" and \"Parent Department Type\" columns will contain the values \"Enterprise\" or \"Group\".
    The \"Activated\" column indicates if the DN or DN range has been activated.  Only has a value if the DN(s) is assigned to a user.
    The \"User Type\" column contains the corresponding enumerated UserType value.
    The \"Country Code\" column indicates the dialing prefix for the phone number.
    The \"National Prefix\" column indicates the digit sequence to be dialed before the telephone number.
    NOTE: the same phone number can show up in the list twice if the phone number is being used as the group calling line Id."""

    dnTable: OCITable


@dataclass
class GroupDnGetAvailableListResponse(OCIDataResponse):
    """Response to the GroupDnGetAvailableListRequest.
    The response contains the list of DNs that are assigned to a group and still available for
    assignment to users or service instances within the group."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class GroupDnGetAvailableRangesListResponse(OCIDataResponse):
    """Response to the GroupDnGetAvailableRangesListRequest.
    The response contains the list of group DNs that are not assigned to user, service instances or IMRN pool.
    The Dns are returned in a list of DNs or DN ranges and formated in E164 format for display."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class GroupDnGetDetailedAvailableListResponse(OCIDataResponse):
    """Response to the GroupDnGetDetailedAvailableListRequest.
    The response contains a table with columns: \"Phone Number\", \"Department\".
    The \"Phone Numbers\" column contains a single DN.
    The \"Department\" column contains the department of the DN if the DN is part of the department.
    The \"Activated\" column indicates if the DN has been activated.
    Only has a value if the DN(s) is assigned to a user or if \"Group
    Enable Activation Mode\" is enabled."""

    dnTable: OCITable


@dataclass
class GroupDnGetListResponse(OCIDataResponse):
    """Response to the GroupDnGetListRequest.
    The response contains the list of DNs assigned to the group."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class GroupDnGetStatusListResponse(OCIDataResponse):
    """Response to GroupDnGetStatusListRequest."""

    dnStatus: List[DNValidationStatusMessage] = field(default_factory=list)


@dataclass
class GroupDnGetSummaryListResponse(OCIDataResponse):
    """Response to the GroupDnGetSummaryListRequest.
    The response contains a table with columns: \"Phone Numbers\", \"Assigned\".
    The \"Phone Numbers\" column contains either a single DN or a range of DNs.
    The \"Assigned\" column contains a boolean flag indicating if the DN(s) are
    currently assigned to a user or service instance.
    The \"Activated\" column indicates if the DN or DN range has been activated.
    Only has a value if the DN(s) is assigned to a user or if either “User Enable Activation mode “
    or \"Group and User Enable Activation Mode\" is enabled."""

    dnTable: OCITable


@dataclass
class GroupDomainGetAssignedListResponse(OCIDataResponse):
    """Contains a simple list of all group domain names."""

    groupDefaultDomain: str

    domain: List[str] = field(default_factory=list)


@dataclass
class GroupDomainGetAssignedUserListResponse(OCIDataResponse):
    """Response to GroupDomainGetAssignedUserListRequest.
    The table columns are: \"User Id\", \"Last Name\", \"First Name\", \"Department\", \"Phone Number\", \"Email Address\",
    \"Service Provider Id\", \"Group Id\", \"Hiragana Last Name\" and \"Hiragana First Name\", \"Extension\"."""

    userTable: OCITable


@dataclass
class GroupEmergencyCallNotificationGetResponse(OCIDataResponse):
    """Response to GroupEmergencyCallNotificationGetRequest."""

    sendEmergencyCallNotificationEmail: bool

    emergencyCallNotifyEmailAddress: Optional[str] = None


@dataclass
class GroupEmergencyZonesGetHomeZoneListResponse(OCIDataResponse):
    """Response to GroupEmergencyZonesGetHomeZoneListRequest."""

    homeZoneIpAddress: List[str] = field(default_factory=list)

    homeZoneIpAddressRange: List[IPAddressRange] = field(default_factory=list)


@dataclass
class GroupEmergencyZonesGetResponse(OCIDataResponse):
    """Response to GroupEmergencyZonesGetRequest."""

    isActive: bool

    emergencyZonesProhibition: str

    sendEmergencyCallNotifyEmail: bool

    emergencyCallNotifyEmailAddress: Optional[str] = None


@dataclass
class GroupEndpointGetListResponse(OCIDataResponse):
    """Response to GroupEndpointGetListRequest.
    The column headings for the endpointTable are:
      \"Line/Port\", \"Last Name\", \"First Name\",  \"User Id\", \"User Type\", \"Phone Number\", \"Extension\", \"Device Type\", \"Device Name\", \"Net Address\", \"MAC Address\", \"Department\", \"Email Address\".
      Possible values for User Type are \"User\", \"CCBasic\", \"CCStandard\", \"CCPremium\", \"RP\", \"MOH\", \"MOHVideo\"."""

    endpointTable: OCITable


@dataclass
class GroupEnhancedCallLogsSchemaInstanceGetResponse(OCIDataResponse):
    """Response to GroupEnhancedCallLogsSchemaInstanceGetRequest."""

    name: Optional[str] = None


@dataclass
class GroupEnterpriseTrunkGetAvailableTrunkGroupListResponse(OCIDataResponse):
    """Response to GroupEnterpriseTrunkGetAvailableTrunkGroupListRequest."""

    trunkGroupName: List[str] = field(default_factory=list)


@dataclass
class GroupEnterpriseTrunkGetAvailableUserListResponse(OCIDataResponse):
    """Response to GroupEnterpriseTrunkGetAvailableUserListRequest.
    The column headings for the enterpriseTrunkUserTable are: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupEnterpriseTrunkGetListResponse(OCIDataResponse):
    """Response to GroupEnterpriseTrunkGetListRequest.
    Contains a table of enterprise trunks defined in the enterprise
    The column headings are: \"Enterprise Trunk Name\", \"Routing Type\" """

    enterpriseTrunkTable: OCITable


@dataclass
class GroupEnterpriseTrunkGetResponse22(OCIDataResponse):
    """Response to GroupEnterpriseTrunkGetRequest22."""

    maximumRerouteAttempts: int

    routeExhaustionAction: str

    orderedRouting: object

    priorityWeightedRouting: object

    enableCapacityManagement: bool

    routeExhaustionForwardAddress: Optional[str] = None

    maxActiveCalls: Optional[int] = None

    capacityExceededTrapInitialCalls: Optional[int] = None

    capacityExceededTrapOffsetCalls: Optional[int] = None

    maximumActiveIncomingCallsAllowed: Optional[int] = None

    maximumActiveOutgoingCallsAllowed: Optional[int] = None

    minimumActiveCallsReserved: Optional[int] = None


@dataclass
class GroupEnterpriseTrunkGetUserListResponse(OCIDataResponse):
    """Response to GroupEnterpriseTrunkGetUserListRequest.
    The column headings for the enterpriseTrunkUserTable are: \"User Id\", \"Last Name\", \"First Name\", \"Phone Number\", \"Alternate Trunk Identity\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Extension\", \"Department\", \"Email Address\" and \"Route List Assigned\"."""

    enterpriseTrunkUserTable: OCITable


@dataclass
class GroupExchangeIntegrationGetResponse(OCIDataResponse):
    """Response to GroupExchangeIntegrationGetRequest."""

    enableExchangeIntegration: bool

    exchangeURL: Optional[str] = None

    exchangeUserName: Optional[str] = None


@dataclass
class GroupExtensionLengthGetResponse22(OCIDataResponse):
    """Response to GroupExtensionLengthGetRequest22.

    The following elements are only used in AS data mode and not returned in XS data mode:
       useExterpriseExtensionLengthSetting"""

    minExtensionLength: int

    maxExtensionLength: int

    defaultExtensionLength: int

    useEnterpriseExtensionLengthSetting: Optional[bool] = None


@dataclass
class GroupFeatureAccessCodeGetResponse21(OCIDataResponse):
    """Response to the GroupFeatureAccessCodeGetRequest21.

    In release 20 the \"Call Recording\" FAC name is changed to
    \"Call Recording - Start\"."""

    useFeatureAccessCodeLevel: str

    featureAccessCode: List[FeatureAccessCodeReadEntry] = field(default_factory=list)


@dataclass
class GroupFileRepositoryDeviceUserGetListResponse(OCIDataResponse):
    """Response to GroupFileRepositoryDeviceUserGetListRequest.
    Contains a table with column headings : \"User Name\",\"Allow Delete\",\"Allow Get\",\"Allow Put\" in a row for each file repository service provider user."""

    fileRepositoryUserTable: OCITable


@dataclass
class GroupFindMeFollowMeAlertingGroupGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupFindMeFollowMeAlertingGroupGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupFindMeFollowMeGetAlertingGroupListResponse(OCIDataResponse):
    """Response to the GroupFindMeFollowMeGetAlertingGroupListRequest.
    Contains a table with column headings:
    \"Name\", \"Priority\"."""

    alertingGroupTable: OCITable


@dataclass
class GroupFindMeFollowMeGetAlertingGroupResponse(OCIDataResponse):
    """Response to GroupFindMeFollowMeGetAlertingGroupRequest.
    Contains the alerting group information.
          The user table’s column headings are: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\" and \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\".
    The criteria table's column headings are: \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Blacklisted\", \"Holiday Schedule\"\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - When no extension is available a blank space is provided instead."""

    useDiversionInhibitor: bool

    answerConfirmationRequired: bool

    numberOfRings: int

    userTable: OCITable

    criteriaTable: OCITable

    alertingGroupDescription: Optional[str] = None

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class GroupFindMeFollowMeGetAlertingGroupSelectiveCriteriaResponse21(OCIDataResponse):
    """Response to GroupFindMeFollowMeGetAlertingGroupSelectiveCriteriaRequest21.
    Contains the alerting group selective criteria information."""

    blacklisted: bool

    fromDnCriteria: CriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class GroupFindMeFollowMeGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupFindMeFollowMeGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\".
    The column value for \"Is Active\" can either be true, or false."""

    findMeFollowMeTable: OCITable


@dataclass
class GroupFindMeFollowMeGetInstanceResponse19sp1(OCIDataResponse):
    """Response to GroupFindMeFollowMeGetInstanceRequest19sp1.
    Contains the service profile information."""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    networkClassOfService: Optional[str] = None


@dataclass
class GroupFlexibleSeatingAccessDeviceGetListResponse(OCIDataResponse):
    """Response to GroupFlexibleSeatingAccessDeviceGetListRequest"""

    availableAccessDevice: List[object] = field(default_factory=list)


@dataclass
class GroupFlexibleSeatingHostGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupFlexibleSeatingHostGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\".
    The column value for \"Is Active\" can either be true, or false."""

    flexibleSeatingHostTable: OCITable


@dataclass
class GroupFlexibleSeatingHostGetInstanceResponse22(OCIDataResponse):
    """Response to GroupFlexibleSeatingHostGetInstanceRequest22.
    Contains the service profile and access device information."""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    defaultAlias: str

    accessDeviceEndpoint: Optional[AccessDeviceMultipleContactEndpointRead22] = None

    networkClassOfService: Optional[str] = None


@dataclass
class GroupFlexibleSeatingHostGuestAssociationGetResponse(OCIDataResponse):
    """Response to GroupFlexibleSeatingHostGuestAssociationGetRequest."""

    enforceAssociationLimit: bool

    associationLimitHours: int

    accessLevel: str

    guestLastName: Optional[str] = None

    guestFirstName: Optional[str] = None

    guestPhoneNumber: Optional[str] = None

    guestExtension: Optional[str] = None

    guestLocationDialingCode: Optional[str] = None

    guestAssociationDateTime: Optional[str] = None


@dataclass
class GroupFlexibleSeatingHostRoutingPoliciesGetResponse(OCIDataResponse):
    """Response to the GroupFlexibleSeatingHostRoutingPoliciesGetRequest."""

    allowEmergencyCalls: bool

    allowCallsToVoicePortal: bool


@dataclass
class GroupGetAvailableLeafDeviceListResponse22(OCIDataResponse):
    """Response to GroupGetAvailableLeafDeviceListRequest22."""

    leafDeviceKey: List[AccessDeviceKey] = field(default_factory=list)

    supportLinks: List[str] = field(default_factory=list)


@dataclass
class GroupGetAvailableTreeDeviceListResponse(OCIDataResponse):
    """Response to GroupGetAvailableTreeDeviceListRequest."""

    treeDeviceInfo: List[TreeDeviceInfo] = field(default_factory=list)


@dataclass
class GroupGetDefaultResponse(OCIDataResponse):
    """Response to the GroupGetDefaultRequest. All values are default values for a group's profile."""

    defaultDomain: str

    userLimit: int

    timeZone: str

    timeZoneDisplayName: str


@dataclass
class GroupGetListInServiceProviderPagedSortedListResponse(OCIDataResponse):
    """Response to GroupGetListInServiceProviderPagedSortedListRequest.
    Contains a table with column headings: \"Group Id\", \"Group Name\", \"User Limit\" and \"Group External Id\"
    and a row for each group.

    The following columns are only populated in AS data mode:
      \"Group External Id\"."""

    groupTable: OCITable


@dataclass
class GroupGetListInServiceProviderResponse(OCIDataResponse):
    """Response to GroupGetListInServiceProviderRequest.
    Contains a 3 column table with column headings: \"Group Id\", \"Group Name\", \"User Limit\"
    and a row for each group."""

    groupTable: OCITable


@dataclass
class GroupGetListInSystemResponse(OCIDataResponse):
    """Response to GroupGetListInSystemRequest.
    Contains a table with column headings: \"Group Id\", \"Group Name\", \"User Limit\", \"Organization Id\", \"Organization Type\", \"Reseller Id\"
    and a row for each group.
    The \"Organization Id\" column is populated with either a service provider Id or an enterprise Id.
    The \"Organization Type\" column is populated with one of the enumerated strings defined in the
    OrganizationType OCI data type.  Please see OCISchemaDataTypes.xsd for details on OrganizationType.

    The following columns are only returned in AS data mode:
      Reseller Id"""

    groupTable: OCITable


@dataclass
class GroupGetResponse22V5(OCIDataResponse):
    """Response to the GroupGetRequest22V5.
    The response contains the group's profile information.
    The following elements are not returned in AS and XS data mode:
    servicePolicy,
    callProcessingSliceId,
    provisioningSliceId,
    subscriberPartition,
    preferredDataCenter.

    The following elements are only used in XS data mode and not
    returned in AS data mode:
    preferredDataCenter.

    The following data elements are only used in AS data mode and not returned
    in XS data mode:
    resellerId,
    groupExternalId.

    The following elements are only used in XS data mode and not returned
    in AS data mode:
    defaultUserCallingLineIdPhoneNumber."""

    defaultDomain: str

    userLimit: int

    userCount: int

    timeZone: str

    timeZoneDisplayName: str

    serviceProviderId: str

    groupId: str

    groupName: Optional[str] = None

    callingLineIdName: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None

    callingLineIdDisplayPhoneNumber: Optional[str] = None

    locationDialingCode: Optional[str] = None

    contact: Optional[Contact] = None

    address: Optional[StreetAddress] = None

    servicePolicy: Optional[str] = None

    callProcessingSliceId: Optional[str] = None

    provisioningSliceId: Optional[str] = None

    subscriberPartition: Optional[str] = None

    preferredDataCenter: Optional[str] = None

    resellerId: Optional[str] = None

    defaultUserCallingLineIdPhoneNumber: Optional[str] = None

    groupExternalId: Optional[str] = None


@dataclass
class GroupGetUserServiceAssignedUserListResponse(OCIDataResponse):
    """Return a table containing the list of users assigned the user service
    or service pack.  The table contains columns: \"User Id\", \"Last Name\",
    \"First Name\", \"Department\", \"Phone Number\", \"Email Address\", \"Hiragana Last Name\";
    \"Hiragana First Name\", \"Extension\".
    This is a response to the GroupGetUserServiceAssignedUserListRequest."""

    userListTable: OCITable


@dataclass
class GroupGroupNightForwardingGetResponse(OCIDataResponse):
    """Response to GroupGroupNightForwardingGetRequest."""

    nightForwarding: str

    businessHours: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class GroupGroupPagingGetAvailableOriginatorListResponse(OCIDataResponse):
    """Response to the GroupGroupPagingGetAvailableOriginatorListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\" and \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupGroupPagingGetAvailableTargetListResponse(OCIDataResponse):
    """Response to the GroupGroupPagingGetAvailableTargetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\" and \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupGroupPagingGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupGroupPagingGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\".
    The column value for \"Is Active\" can either be true, or false."""

    pagingGroupTable: OCITable


@dataclass
class GroupGroupPagingGetInstanceResponse19sp1(OCIDataResponse):
    """Response to GroupGroupPagingGetInstanceRequest19sp1.
    Contains the service profile information.

    The following element is only used in AS data mode and not returned in XS data mode :
       networkClassOfService"""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    confirmationToneTimeoutSeconds: int

    deliverOriginatorCLIDInstead: bool

    originatorCLIDPrefix: Optional[str] = None

    networkClassOfService: Optional[str] = None


@dataclass
class GroupGroupPagingGetOriginatorListResponse(OCIDataResponse):
    """Response to the GroupGroupPagingGetOriginatorListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    originatorTable: OCITable


@dataclass
class GroupGroupPagingGetTargetListResponse(OCIDataResponse):
    """Response to the GroupGroupPagingGetTargetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    targetTable: OCITable


@dataclass
class GroupGroupPagingTargetsCapacityGetResponse22(OCIDataResponse):
    """Response to GroupGroupPagingTargetsCapacityGetRequest22."""

    maximumTargetUsersFromServiceProvider: int

    maximumTargetUsers: int


@dataclass
class GroupHuntGroupGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupHuntGroupGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupHuntGroupGetAvailableUserPagedSortedListResponse(OCIDataResponse):
    """Response to the GroupHuntGroupGetAvailableUserPagedSortedListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Is Phone Number Activated\", \"Country Code\",\"National Prefix\", \"Extension\", \"Department\", \"Department Type\",
    \"Parent Department\", \"Parent Department Type\", \"Email Address\", \"IMP Id\", \"Mobile Number\", \"Group Id\", \"Group Name\"."""

    userTable: OCITable


@dataclass
class GroupHuntGroupGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupHuntGroupGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\", \"Policy\".
    The column values for \"Is Active\" can either be true, or false.
    NOTE: prior to release 14, the policy column did not match the HuntPolicy enumerated type."""

    huntGroupTable: OCITable


@dataclass
class GroupHuntGroupGetInstancePagedSortedListResponse(OCIDataResponse):
    """Response to the GroupHuntGroupGetInstancePagedSortedListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Is Phone Number Activated\",
    \"Country Code\",\"National Prefix\", \"Extension\", \"Department\", \"Department Type\",
    \"Parent Department\", \"Parent Department Type\", \"Is Active\", \"Policy\".
    The column values for \"Is Active\" can either be true, or false.
    NOTE: prior to release 14, the policy column did not match the HuntPolicy enumerated type."""

    huntGroupTable: OCITable


@dataclass
class GroupHuntGroupGetInstanceResponse20(OCIDataResponse):
    """Response to GroupHuntGroupGetInstanceRequest20.
    Contains the service profile information and a table of assigned users.
    The table has column headings: \"User Id\", \"Last Name\", \"First Name\",
    \"Hiragana Last Name\", \"Hiragana First Name\", \"Weight\", \"Phone Number\",
    \"Extension\", \"Department\", \"Email Address\", \"Is Phone Number Activated\",
    \"Country Code\",\"National Prefix\", \"Department Name\" ,\"Department Type\",
    \"Parent Department\", \"Parent Department Type\",\"Group Id\",\"Group Name\".
    The following elements are only used in AS data mode:
       useSystemHuntGroupCLIDSetting
       includeHuntGroupNameInCLID
       Is Phone Number Activated
       Country Code
       National Prefix
       Department Name
       Department Type
       Parent Department
       Parent Department Type
       Group Id
       Group Name"""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    policy: str

    huntAfterNoAnswer: bool

    noAnswerNumberOfRings: int

    forwardAfterTimeout: bool

    forwardTimeoutSeconds: int

    agentUserTable: OCITable

    allowCallWaitingForAgents: bool

    useSystemHuntGroupCLIDSetting: bool

    includeHuntGroupNameInCLID: bool

    enableNotReachableForwarding: bool

    makeBusyWhenNotReachable: bool

    allowMembersToControlGroupBusy: bool

    enableGroupBusy: bool

    applyGroupBusyWhenTerminatingToAgent: bool

    forwardToPhoneNumber: Optional[str] = None

    notReachableForwardToPhoneNumber: Optional[str] = None

    networkClassOfService: Optional[str] = None


@dataclass
class GroupIMRNGetListResponse(OCIDataResponse):
    """Response to GroupIMRNGetListRequest."""

    imrn: List[str] = field(default_factory=list)


@dataclass
class GroupIncomingCallingPlanGetListResponse(OCIDataResponse):
    """Response to GroupIncomingCallingPlanGetListRequest."""

    groupPermissions: IncomingCallingPlanPermissions

    departmentPermissions: List[IncomingCallingPlanDepartmentPermissions] = field(
        default_factory=list
    )


@dataclass
class GroupInstantGroupCallGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupInstantGroupCallGetInstanceListRequest.
    Contains a 6 column table with column headings:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\".
    The column values for Is Active can either be true, or false."""

    instantGroupCallTable: OCITable


@dataclass
class GroupInstantGroupCallGetInstanceResponse19sp1(OCIDataResponse):
    """Response to GroupInstantGroupCallGetInstanceRequest19sp1.
    Contains the service profile information and a list of phone numbers."""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    isAnswerTimeoutEnabled: bool

    destinationPhoneNumber: List[str] = field(default_factory=list)

    answerTimeoutMinutes: Optional[int] = None

    networkClassOfService: Optional[str] = None


@dataclass
class GroupIntegratedIMPGetResponse23(OCIDataResponse):
    """Response to the GroupIntegratedIMPGetRequest23.
    The response contains the group Integrated IMP service attributes.

    The following elements are only returned to a reseller administrator or above:
      useServiceProviderMessagingServer
      provisioningUrl
      provisioningUserId"""

    useServiceProviderSetting: bool

    addServiceProviderInIMPUserId: bool

    defaultImpIdType: str

    serviceDomain: Optional[str] = None

    effectiveServiceDomain: Optional[str] = None

    useServiceProviderMessagingServer: Optional[bool] = None

    provisioningUrl: Optional[str] = None

    provisioningUserId: Optional[str] = None


@dataclass
class GroupInterceptGroupGetResponse21sp1(OCIDataResponse):
    """Response to the GroupInterceptGroupGetRequest21sp1.

    The following elements are only used in AS data mode:
      exemptInboundMobilityCalls
      exemptOutboundMobilityCalls
      disableParallelRingingToNetworkLocations"""

    isActive: bool

    announcementSelection: str

    inboundCallMode: str

    alternateBlockingAnnouncement: bool

    exemptInboundMobilityCalls: bool

    disableParallelRingingToNetworkLocations: bool

    routeToVoiceMail: bool

    playNewPhoneNumber: bool

    transferOnZeroToPhoneNumber: bool

    outboundCallMode: str

    exemptOutboundMobilityCalls: bool

    rerouteOutboundCalls: bool

    audioFileDescription: Optional[str] = None

    audioMediaType: Optional[str] = None

    videoFileDescription: Optional[str] = None

    videoMediaType: Optional[str] = None

    newPhoneNumber: Optional[str] = None

    transferPhoneNumber: Optional[str] = None

    outboundReroutePhoneNumber: Optional[str] = None


@dataclass
class GroupInventoryReportGetResponse(OCIDataResponse):
    """Response to GroupInventoryReportGetRequest."""

    inventoryReportTable: OCITable


@dataclass
class GroupMWIDeliveryToMobileEndpointCustomTemplateGetResponse23(OCIDataResponse):
    """Response to the GroupMWIDeliveryToMobileEndpointCustomTemplateGetRequest23."""

    isEnabled: bool

    templateBody: MWIDeliveryToMobileEndpointTemplateBody23

    monthAbbreviations: Optional[str] = None


@dataclass
class GroupMWIDeliveryToMobileEndpointGetResponse(OCIDataResponse):
    """Response to GroupMWIDeliveryToMobileEndpointGetRequest.

    The templateActivationTable contains the list of templates defined for the group.
    The column headings are \"Enable\", \"Language\", \"Type\"."""

    useSettingLevel: str

    templateActivationTable: OCITable


@dataclass
class GroupMeetMeConferencingGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupMeetMeConferencingGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", and \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupMeetMeConferencingGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupMeetMeConferencingGetInstanceListRequest.
    Contains a table with column headings: \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Ports\", and \"Is Active\".
    The column values for \"Is Active\" can either be true, or false."""

    conferenceBridgeTable: OCITable


@dataclass
class GroupMeetMeConferencingGetInstanceResponse19sp1(OCIDataResponse):
    """Response to GroupMeetMeConferencingGetInstanceRequest19sp1.
    Contains the service profile information and a table of assigned hosts.
    The table has column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    allocatedPorts: MeetMeConferencingConferencePorts

    securityPinLength: int

    allowIndividualOutDial: bool

    conferenceHostUserTable: OCITable

    playWarningPrompt: bool

    conferenceEndWarningPromptMinutes: int

    enableMaxConferenceDuration: bool

    maxConferenceDurationMinutes: MeetMeConferencingConferenceDuration

    maxScheduledConferenceDurationMinutes: MeetMeConferencingConferenceDuration

    networkClassOfService: Optional[str] = None

    operatorNumber: Optional[str] = None


@dataclass
class GroupMeetMeConferencingGetResponse(OCIDataResponse):
    """Response to GroupMeetMeConferencingGetRequest."""

    availablePorts: MeetMeConferencingConferencePorts

    allocatedPorts: MeetMeConferencingConferencePorts


@dataclass
class GroupMusicOnHoldGetDepartmentListResponse(OCIDataResponse):
    """Response to the GroupMusicOnHoldGetDepartmentListRequest."""

    hasDepartment: bool

    department: List[DepartmentKey] = field(default_factory=list)

    departmentFullPath: List[str] = field(default_factory=list)


@dataclass
class GroupMusicOnHoldGetInstanceResponse23V2(OCIDataResponse):
    """Response to the GroupMusicOnHoldGetInstanceRequest23V2.
    The following elements are only used in AS data mode:
    - useDynamicMOHDuringCallHold, value \"false\" is returned in XS data mode."""

    serviceUserId: str

    isActiveDuringCallHold: bool

    isActiveDuringCallPark: bool

    isActiveDuringBusyCampOn: bool

    enableVideo: bool

    source: MusicOnHoldSourceRead22V3

    useAlternateSourceForInternalCalls: bool

    internalSource: MusicOnHoldSourceRead22V3

    useDynamicMOHDuringCallHold: bool


@dataclass
class GroupNetworkClassOfServiceGetAssignedListResponse(OCIDataResponse):
    """Response to GroupNetworkClassOfServiceGetAssignedListRequest.
    Contains a table of all Network Classes of Service assigned to
    the group. The column headings are: \"Name\", \"Description\" and \"Default\"."""

    networkClassOfServiceTable: OCITable


@dataclass
class GroupNetworkClassOfServiceGetAssignedUserListResponse21(OCIDataResponse):
    """Response to GroupNetworkClassOfServiceGetAssignedUserListRequest21.
    Contains a table of users that have the Network Class of Service
    assigned. The column headings are: \"User Id\", \"User Type\", \"Last Name\", \"First Name\",
    \"Department\", \"Phone Number\", \"Email Address\", \"Service Provider Id\",
    \"Group Id\", \"Hiragana Last Name\" and \"Hiragana First Name\" , \"Extension\".
    The User type column will display Auto Attendant and the Call Center subtype.
    Call Center - Basic, Call Center - Standard and Call Center - Premium will be displayed instead of Call Center and
    Auto Attendant (for the Basic Auto Attendant) and Auto Attendant - Standard instead of Auto Attendant."""

    userTable: OCITable


@dataclass
class GroupOfficeZoneGetAssignedListResponse(OCIDataResponse):
    """Response to GroupOfficeZoneGetAssignedListRequest.
    Contains a table of all Office Zones assigned to the
    group. The column headings are: \"Name\", \"Description\" and \"Default\"."""

    officeZoneTable: OCITable


@dataclass
class GroupOfficeZoneGetAssignedUserListResponse(OCIDataResponse):
    """Response to GroupOfiiceZoneGetAssignedUserListRequest.
    Contains a table of users that have the Office Zone assigned. The column headings are: \"User Id\", \"User Type\", \"Last Name\",
    \"First Name\", \"Department\", \"Phone Number\", \"Email Address\", \"Hiragana Last Name\" and \"Hiragana First Name\", \"Extension\".
    Office Zones can only be unassigned if the Location-Based Calling Restrictions has been authorized to the group otherwise the request will fail."""

    userTable: OCITable


@dataclass
class GroupOutgoingCallingPlanAuthorizationCodeGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanAuthorizationCodeGetListRequest."""

    groupCodeList: OutgoingCallingPlanGroupAuthorizationCodes

    departmentCodeList: List[OutgoingCallingPlanDepartmentAuthorizationCodes] = field(
        default_factory=list
    )


@dataclass
class GroupOutgoingCallingPlanCallMeNowGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanCallMeNowGetListRequest."""

    groupPermissions: OutgoingCallingPlanCallMeNowPermissions

    departmentPermissions: List[OutgoingCallingPlanCallMeNowDepartmentPermissions] = (
        field(default_factory=list)
    )


@dataclass
class GroupOutgoingCallingPlanDepartmentAuthorizationCodeGetListResponse(
    OCIDataResponse
):
    """Response to GroupOutgoingCallingPlanDepartmentAuthorizationCodeGetListRequest."""

    codeEntry: List[OutgoingCallingPlanAuthorizationCodeEntry] = field(
        default_factory=list
    )


@dataclass
class GroupOutgoingCallingPlanDigitPlanCallMeNowGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanDigitPlanCallMeNowGetListRequest."""

    groupPermissions: Optional[OutgoingCallingPlanDigitPatternCallMeNowPermissions] = (
        None
    )

    departmentPermissions: List[
        OutgoingCallingPlanDigitPatternCallMeNowDepartmentPermissions
    ] = field(default_factory=list)


@dataclass
class GroupOutgoingCallingPlanDigitPlanOriginatingGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanDigitPlanOriginatingGetListRequest."""

    groupPermissions: Optional[
        OutgoingCallingPlanDigitPatternOriginatingPermissions
    ] = None

    departmentPermissions: List[
        OutgoingCallingPlanDigitPatternOriginatingDepartmentPermissions
    ] = field(default_factory=list)


@dataclass
class GroupOutgoingCallingPlanDigitPlanRedirectingGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanDigitPlanRedirectingGetListRequest."""

    groupPermissions: Optional[
        OutgoingCallingPlanDigitPatternRedirectingPermissions
    ] = None

    departmentPermissions: List[
        OutgoingCallingPlanDigitPatternRedirectingDepartmentPermissions
    ] = field(default_factory=list)


@dataclass
class GroupOutgoingCallingPlanOriginatingGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanOriginatingGetListRequest."""

    groupPermissions: OutgoingCallingPlanOriginatingPermissions

    departmentPermissions: List[OutgoingCallingPlanOriginatingDepartmentPermissions] = (
        field(default_factory=list)
    )


@dataclass
class GroupOutgoingCallingPlanPinholeDigitPatternGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanPinholeDigitPatternGetListRequest.
    Contains a table with column headings: \"Name\", \"Digit Pattern\"."""

    digitPatternTable: OCITable


@dataclass
class GroupOutgoingCallingPlanPinholeDigitPlanCallMeNowGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanPinholeDigitPlanCallMeNowGetListRequest."""

    groupPermissions: Optional[
        OutgoingPinholeDigitPlanDigitPatternCallMeNowPermissions
    ] = None

    departmentPermissions: List[
        OutgoingPinholeDigitPlanDigitPatternCallMeNowDepartmentPermissions
    ] = field(default_factory=list)


@dataclass
class GroupOutgoingCallingPlanPinholeDigitPlanOriginatingGetListResponse(
    OCIDataResponse
):
    """Response to GroupOutgoingCallingPlanPinholeDigitPlanOriginatingGetListRequest."""

    groupPermissions: Optional[
        OutgoingPinholeDigitPlanDigitPatternOriginatingPermissions
    ] = None

    departmentPermissions: List[
        OutgoingPinholeDigitPlanDigitPatternOriginatingDepartmentPermissions
    ] = field(default_factory=list)


@dataclass
class GroupOutgoingCallingPlanPinholeDigitPlanRedirectingGetListResponse(
    OCIDataResponse
):
    """Response to GroupOutgoingCallingPlanPinholeDigitPlanRedirectingGetListRequest."""

    groupPermissions: Optional[
        OutgoingPinholeDigitPlanDigitPatternRedirectingPermissions
    ] = None

    departmentPermissions: List[
        OutgoingPinholeDigitPlanDigitPatternRedirectingDepartmentPermissions
    ] = field(default_factory=list)


@dataclass
class GroupOutgoingCallingPlanRedirectedGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanRedirectedGetListRequest."""

    groupPermissions: OutgoingCallingPlanRedirectedPermissions

    departmentPermissions: List[OutgoingCallingPlanRedirectedDepartmentPermissions] = (
        field(default_factory=list)
    )


@dataclass
class GroupOutgoingCallingPlanRedirectingGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanRedirectingGetListRequest."""

    groupPermissions: OutgoingCallingPlanRedirectingPermissions

    departmentPermissions: List[OutgoingCallingPlanRedirectingDepartmentPermissions] = (
        field(default_factory=list)
    )


@dataclass
class GroupOutgoingCallingPlanTransferNumbersGetListResponse(OCIDataResponse):
    """Response to GroupOutgoingCallingPlanTransferNumbersGetListRequest."""

    groupNumbers: OutgoingCallingPlanTransferNumbers

    departmentNumbers: List[OutgoingCallingPlanDepartmentTransferNumbers] = field(
        default_factory=list
    )


@dataclass
class GroupPasswordRulesGetResponseRI(OCIDataResponse):
    """Response to GroupPasswordRulesGetRequestRI.
    Contains the password rules applicable to users within the group.

    The following element is only used in AS data mode:
    forcePasswordChangeAfterReset, value “false” is returned in XS data mode
    reenableLogin
    lockOutInMinutes"""

    disallowUserId: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    maxFailedLoginAttempts: int

    passwordExpiresDays: int

    sendLoginDisabledNotifyEmail: bool

    disallowRulesModification: bool

    disallowPreviousPasswords: bool

    numberOfPreviousPasswords: int

    forcePasswordChangeAfterReset: bool

    usePasswordValidationService: bool

    reenableLogin: bool

    lockOutInMinutes: int

    loginDisabledNotifyEmailAddress: Optional[str] = None


@dataclass
class GroupPhoneDirectoryGetPagedSortedListResponse(OCIDataResponse):
    """Response to GroupPhoneDirectoryGetPagedSortedListRequest.
    Contains a table with a row for each phone number and column headings :
    \"Name\", \"Number\", \"Extension\", \"Mobile\", \"Email Address\",
    \"Department\", \"Hiragana Name\", \"Group Id\", \"Yahoo Id\", \"User Id\", \"IMP Id\" and \"Is Virtual On-Net User\".

    If extended directory information is requested, the following columns are also included:
    \"First Name\", \"Last Name\", \"Pager\", \"Title\", \"Time Zone\",
    \"Location\", \"Address Line 1\", \"Address Line 2\", \"City\", \"State\", \"Zip\", \"Country\".

    Finally \"Service Name\".
    The Service Name represents the localized service name for service instances. The localized values are taken from the BroadworksLabel.properties file.
    Service Name is currently supporting:
    AutoAttendant, AutoAttendantStandard, AutoAttendantVideo, CallCenter, CallCenterStandard, CallCenterPremium
    HuntGroup, InstantGroupCall, VoiceMessagingGroup, MusicOnHold, MusicOnHoldVideo, RoutePoint, BroadWorksAnywhere
    GroupPaging, FindmeFollowme, VoiceXML, FlexibleSeatingGuest, CollaborateSharing, MeetMeConferencing.
    For a Regular User or a Virtual On Network Enterprise Extensions, the Service Name is empty.

    The following columns are populated in AS data mode only:
      \"IMP Id\" """

    totalNumberOfRows: int

    directoryTable: OCITable


@dataclass
class GroupPolicyGetResponse22(OCIDataResponse):
    """Response to GroupPolicyGetRequest22.
    Contains the policy settings for the group.

    The following elements are only used in AS data mode:
      userAutoAttendantNameDialingAccess, value None is returned in XS data mode"""

    callingPlanAccess: str

    extensionAccess: str

    voiceMessagingAccess: str

    departmentAdminUserAccess: str

    departmentAdminTrunkGroupAccess: str

    departmentAdminPhoneNumberExtensionAccess: str

    departmentAdminCallingLineIdNumberAccess: str

    userAuthenticationAccess: str

    userGroupDirectoryAccess: str

    userProfileAccess: str

    userEnhancedCallLogAccess: str

    userAutoAttendantNameDialingAccess: str


@dataclass
class GroupPolycomPhoneServicesGetResponse(OCIDataResponse):
    """Response to GroupPolycomPhoneServicesGetRequest."""

    includeGroupCommonPhoneListInDirectory: bool

    includeGroupCustomContactDirectoryInDirectory: bool

    groupCustomContactDirectory: Optional[str] = None


@dataclass
class GroupPortalPasscodeRulesGetResponseRI(OCIDataResponse):
    """Response to GroupPortalPasscodeRulesGetRequestRI.
    Contains the group's passcode rules setting.

    The following elements are only used in AS data mode:
      numberOfRepeatedDigits
      disallowRepeatedPatterns
      disallowContiguousSequences
      numberOfAscendingDigits
      numberOfDescendingDigits
      numberOfPreviousPasscodes
      reenableLogin
      lockOutInMinutes"""

    useRuleLevel: str

    disallowRepeatedDigits: bool

    numberOfRepeatedDigits: int

    disallowRepeatedPatterns: bool

    disallowContiguousSequences: bool

    numberOfAscendingDigits: int

    numberOfDescendingDigits: int

    disallowUserNumber: bool

    disallowReversedUserNumber: bool

    disallowOldPasscode: bool

    numberOfPreviousPasscodes: int

    disallowReversedOldPasscode: bool

    minCodeLength: int

    maxCodeLength: int

    disableLoginAfterMaxFailedLoginAttempts: bool

    expirePassword: bool

    sendLoginDisabledNotifyEmail: bool

    reenableLogin: bool

    lockOutInMinutes: int

    maxFailedLoginAttempts: Optional[int] = None

    passcodeExpiresDays: Optional[int] = None

    loginDisabledNotifyEmailAddress: Optional[str] = None


@dataclass
class GroupPreAlertingAnnouncementGetResponse20(OCIDataResponse):
    """Response to a GroupPreAlertingAnnouncementGetResponse20."""

    announcementInterruption: str

    audioSelection: str

    videoSelection: str

    interruptionDigitSequence: Optional[str] = None

    audioFile: Optional[AnnouncementFileKey] = None

    audioFileUrl: Optional[str] = None

    videoFile: Optional[AnnouncementFileKey] = None

    videoFileUrl: Optional[str] = None


@dataclass
class GroupPreferredCarrierGroupGetResponse(OCIDataResponse):
    """Response to a GroupPreferredCarrierGroupGetRequest."""

    intraLataCarrier: GroupPreferredCarrierName

    interLataCarrier: GroupPreferredCarrierName

    internationalCarrier: GroupPreferredCarrierName


@dataclass
class GroupRouteListEnterpriseTrunkNumberPrefixGetAvailableListResponse(
    OCIDataResponse
):
    """Response to GroupRouteListEnterpriseTrunkNumberPrefixGetAvailableListRequest.
    Contains a list of number prefixess that are assigned to a group and still available for assignment to users within the group.
    The column headings are \"Number Prefix\"\",\"Is Active\", \"Extension Range Start\" and \"Extension Range End\"."""

    availableNumberPrefixTable: OCITable


@dataclass
class GroupRouteListEnterpriseTrunkNumberPrefixGetSummaryListResponse(OCIDataResponse):
    """Response to GroupRouteListEnterpriseTrunkNumberRangeGetSummaryListRequest.
    The response contains a table with columns: \"Number Prefix\", \"User Id\",
    \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\", \"Extension\",
    \"Department\", \"Email Address\", \"Enterprise Trunk\"\",\"Is Active\", \"Extension Range Start\" and \"Extension Range End\".
    The \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\" and \"Email Address\" columns contains the corresponding attributes of the user possessing the number range.
    The \"Enterprise Trunk\" column contains the enterprise trunk the user possessing the number range belongs to.
    The \"Is Active\" column indicates if the number prefix has been activated.
    The \"Extension Range Start\" column indicates the start for an extension range.
    The \"Extension Range End\" column indicates the end for an extension range."""

    numberPrefixSummaryTable: OCITable


@dataclass
class GroupRouteListEnterpriseTrunkNumberRangeGetAvailableListResponse(OCIDataResponse):
    """Response to GroupRouteListEnterpriseTrunkNumberRangeGetAvailableListRequest.
    Contains a list of number ranges that are assigned to a group and still available for assignment to users within the group.
    The column headings are \"Number Range Start\", \"Number Range End\" ,\"Is Active\" and \"Extension Length\".."""

    availableNumberRangeTable: OCITable


@dataclass
class GroupRouteListEnterpriseTrunkNumberRangeGetSummaryListResponse(OCIDataResponse):
    """Response to GroupRouteListEnterpriseTrunkNumberRangeGetSummaryListRequest.
    The response contains a table with columns: \"Number Range Start\", \"Number Range End\", \"User Id\",
    \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\", \"Extension\",
    \"Department\", \"Email Address\", \"Enterprise Trunk\" and \"Is Active\".
    The \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\" and \"Email Address\" columns contains the corresponding attributes of the user possessing the number range.
    The \"Enterprise Trunk\" column contains the enterprise trunk the user possessing the number range belongs to.
    The \"Is Active\" column indicates if the number range has been activated.
    The \"Extension Length\" column indicates the length of the extension for the enterpris trunk number range."""

    numberRangeSummaryTable: OCITable


@dataclass
class GroupRoutePointBouncedCallGetResponse(OCIDataResponse):
    """Response to the GroupRoutePointBouncedCallGetRequest."""

    isActive: bool

    numberOfRingsBeforeBouncingCall: int

    bounceCallWhenAgentUnavailable: bool

    enableTransfer: Optional[bool] = None

    transferPhoneNumber: Optional[str] = None


@dataclass
class GroupRoutePointDistinctiveRingingGetResponse(OCIDataResponse):
    """Response to the GroupRoutePointDistinctiveRingingGetRequest."""

    enableDistinctiveRinging: bool

    distinctiveRingingRingPattern: str

    distinctiveRingingForceDeliveryRingPattern: str


@dataclass
class GroupRoutePointExternalSystemGetAssignedListResponse(OCIDataResponse):
    """Response to the GroupRoutePointExternalSystemGetAssignedListRequest.
    Contains a table of all Route Point External Systems assigned to the
    group.  The column headings are: \"Name\" and \"Description\"."""

    externalSystemTable: OCITable


@dataclass
class GroupRoutePointExternalSystemGetAssignedRoutePointListResponse(OCIDataResponse):
    """Response to the GroupRoutePointExternalSystemGetAssignedRoutePointListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Video\", \"Phone Number\", \"Extension\", \"Department\".
    The column values for \"Video\" can either be \"true\", or \"false\"."""

    routePointTable: OCITable


@dataclass
class GroupRoutePointForcedForwardingGetResponse20(OCIDataResponse):
    """Response to the GroupRoutePointForcedForwardingGetRequest20."""

    isActive: bool

    playAnnouncementBeforeForwarding: bool

    audioMessageSelection: str

    videoMessageSelection: str

    forwardToPhoneNumber: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupRoutePointGetAnnouncementResponse22(OCIDataResponse):
    """Response to the GroupRoutePointGetAnnouncementRequest22."""

    mediaOnHoldSource: CallCenterMediaOnHoldSourceRead22


@dataclass
class GroupRoutePointGetDNISAgentListResponse(OCIDataResponse):
    """Response to the GroupRoutePointGetDNISAgentListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    agentTable: OCITable


@dataclass
class GroupRoutePointGetDNISAnnouncementResponse22(OCIDataResponse):
    """Response to the GroupRoutePointGetDNISAnnouncementRequest22."""

    mediaOnHoldSource: CallCenterMediaOnHoldSourceRead22


@dataclass
class GroupRoutePointGetDNISListResponse(OCIDataResponse):
    """Response to the GroupRoutePointGetDNISListRequest.
    Contains a table with column headings: \"Name\", \"Phone Number\", \"Extension\"."""

    displayDNISNumber: bool

    displayDNISName: bool

    dnisTable: OCITable


@dataclass
class GroupRoutePointGetDNISResponse(OCIDataResponse):
    """Response to the GroupRoutePointGetDNISRequest."""

    useCustomCLIDSettings: bool

    useCustomDnisAnnouncementSettings: bool

    allowOutgoingACDCall: bool

    dnisPhoneNumber: Optional[str] = None

    extension: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None

    callingLineIdLastName: Optional[str] = None

    callingLineIdFirstName: Optional[str] = None


@dataclass
class GroupRoutePointGetFailoverPolicyResponse(OCIDataResponse):
    """Response to the GroupRoutePointGetFailoverPolicyRequest."""

    enableFailoverSupport: bool

    failoverStatus: str

    perCallEnableFailoverSupport: bool

    perCallCallFailureTimeoutSeconds: int

    perCallOutboundCallFailureTimeoutSeconds: int

    externalSystem: Optional[str] = None

    failoverPhoneNumber: Optional[str] = None

    perCallFailoverPhoneNumber: Optional[str] = None


@dataclass
class GroupRoutePointGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupRoutePointGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Video\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\".
    The column values for \"Video\" and \"Is Active\" can either be true, or false."""

    routePointTable: OCITable


@dataclass
class GroupRoutePointGetInstanceResponse23(OCIDataResponse):
    """Response to GroupRoutePointGetInstanceRequest23."""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    externalPreferredAudioCodec: str

    internalPreferredAudioCodec: str

    queueLength: int

    noAnswerTimeoutRings: int

    enableVideo: bool

    playRingingWhenOfferingCall: bool

    overrideAgentWrapUpTime: bool

    enableAutomaticStateChangeForAgents: bool

    agentStateAfterCall: str

    forceDeliveryOfCalls: bool

    sendCallAdmissionNotification: bool

    callAdmissionTimerSeconds: int

    networkClassOfService: Optional[str] = None

    wrapUpSeconds: Optional[int] = None

    agentUnavailableCode: Optional[str] = None

    forceDeliveryWaitTimeSeconds: Optional[int] = None

    enableUnlimitedQueueLength: Optional[bool] = None


@dataclass
class GroupRoutePointHolidayServiceGetResponse20(OCIDataResponse):
    """Response to the GroupRoutePointHolidayServiceGetRequest20."""

    action: str

    playAnnouncementBeforeAction: bool

    audioMessageSelection: str

    videoMessageSelection: str

    holidaySchedule: Optional[HolidaySchedule] = None

    transferPhoneNumber: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupRoutePointNightServiceGetResponse20(OCIDataResponse):
    """Response to the GroupRoutePointNightServiceGetRequest20."""

    action: str

    forceNightService: bool

    playAnnouncementBeforeAction: bool

    audioMessageSelection: str

    videoMessageSelection: str

    manualAnnouncementMode: str

    manualAudioMessageSelection: str

    manualVideoMessageSelection: str

    businessHours: Optional[TimeSchedule] = None

    transferPhoneNumber: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    manualAudioUrlList: Optional[CallCenterAnnouncementURLList] = None

    manualAudioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    manualVideoUrlList: Optional[CallCenterAnnouncementURLList] = None

    manualVideoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupRoutePointOverflowGetResponse20(OCIDataResponse):
    """Response to the GroupRoutePointOverflowGetRequest20."""

    action: str

    overflowAfterTimeout: bool

    timeoutSeconds: int

    playAnnouncementBeforeOverflowProcessing: bool

    audioMessageSelection: str

    transferPhoneNumber: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    videoMessageSelection: Optional[str] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None


@dataclass
class GroupRoutePointQueueCallDispositionCodeGetListResponse(OCIDataResponse):
    """Response to the GroupRoutePointQueueCallDispositionCodeGetListRequest.
    Contains a table with column headings: \"Is Active\", \"Code\", \"Description\" and \"Level\".
    Level column can be any of the values in the data type CallDispositionCodeLevel."""

    dispositionCodesTable: OCITable


@dataclass
class GroupRoutePointQueueCallDispositionCodeGetResponse(OCIDataResponse):
    """Response to the GroupRoutePointQueueCallDispositionCodeGetRequest"""

    isActive: bool

    description: Optional[str] = None


@dataclass
class GroupRoutePointQueueCallDispositionCodeSettingsGetResponse(OCIDataResponse):
    """Response to GroupRoutePointQueueCallDispositionCodeSettingsGetRequest."""

    enableCallDispositionCodes: bool

    includeOrganizationCodes: bool

    forceUseOfCallDispositionCodes: bool

    defaultCallDispositionCode: Optional[CallDispositionCodeWithLevel] = None


@dataclass
class GroupRoutingProfileGetResponse(OCIDataResponse):
    """Response to GroupRoutingProfileGetRequest."""

    routingProfile: Optional[str] = None


@dataclass
class GroupScheduleGetEventDetailListResponse(OCIDataResponse):
    """Response to GroupScheduleGetEventDetailListRequest.
    The response contains a list of ScheduleEvents.
    If the scheduleKey doesn't refer to an existing schedule on the AS, then the response will be empty."""

    scheduleEventsList: List[ScheduleEvents] = field(default_factory=list)


@dataclass
class GroupScheduleGetEventListResponse(OCIDataResponse):
    """Response to GroupScheduleGetEventListRequest.
    The response contains a list of events."""

    eventName: List[str] = field(default_factory=list)


@dataclass
class GroupScheduleGetEventResponse(OCIDataResponse):
    """Response to GroupScheduleGetEventRequest.
    The response contains the event of the group schedule."""

    startDate: int

    allDayEvent: bool

    startTime: HourMinute

    endTime: HourMinute

    endDate: int

    recurrence: Optional[Recurrence] = None


@dataclass
class GroupScheduleGetListResponse17sp1(OCIDataResponse):
    """Response to GroupScheduleGetListRequest17sp1.
    The response contains a list of group schedules. If the group belongs to an enterprise,
    it also contains the schedules for the enterprise."""

    scheduleGlobalKey: List[ScheduleGlobalKey] = field(default_factory=list)


@dataclass
class GroupScheduleGetPagedSortedListResponse(OCIDataResponse):
    """Response to GroupScheduleGetPagedSortedListRequest.
    Contains a 3 column table with column headings: \"Name\", \"Type\", \"Level\"
    and a row for each schedule."""

    scheduleTable: OCITable


@dataclass
class GroupScheduleUsageResponse(OCIDataResponse):
    """Response to GroupScheduleUsageRequest.
    The response contains a list of service names.
    The response contains the usage for the requested schedule.
    The usage table has columns \"Service Name\", and \"Instance Name\".
    The Service Name values correspond to string values of the GroupService and UserService data types."""

    usageTable: OCITable


@dataclass
class GroupSecurityClassificationCustomizationGetAvailableListResponse(OCIDataResponse):
    """Response to GroupClassificationCustomizationGetAvailableListRequest.
    Returns the available group security classifications.
    Contains a table with column headings:
    \"SystemSecurityClassification\", \"CustomizedSecurityClassification\" """

    securityClassificationNameTable: OCITable


@dataclass
class GroupSeriesCompletionGetAvailableUserListResponse(OCIDataResponse):
    """Response to the GroupSeriesCompletionGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupSeriesCompletionGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupSeriesCompletionGetInstanceListRequest."""

    name: List[str] = field(default_factory=list)


@dataclass
class GroupSeriesCompletionGetInstanceResponse(OCIDataResponse):
    """Response to the GroupSeriesCompletionGetInstanceRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupServiceGetAuthorizationListResponse(OCIDataResponse):
    """Response to GroupServiceGetAuthorizationListRequest.
    Contains three tables, one for the service packs, one for the group services, and one for
    the user services.
    The user table has the following column headings:
      \"Service Name\", \"Authorized\", \"Assigned\", \"Limited\", \"Quantity\", \"Usage\", \"Licensed\", \"Allowed\", \"User Assignable\", \"Group Service Assignable\".
    The group service table has the following column headings:
      \"Service Name\", \"Authorized\", \"Assigned\", \"Limited\", \"Quantity\", \"Usage\", \"Licensed\", \"Allowed\", \"Instance Count\".
    The service pack table's column headings are:
      \"Service Pack Name\", \"Authorized\", \"Assigned\", \"Limited\", \"Allocated\", \"Allowed\", \"Usage\", \"Description\"."""

    servicePacksAuthorizationTable: OCITable

    groupServicesAuthorizationTable: OCITable

    userServicesAuthorizationTable: OCITable


@dataclass
class GroupServiceGetAuthorizationResponse(OCIDataResponse):
    """Response to GroupServiceGetAuthorizationRequest.
    If the feature is not authorized, then \"authorized\" is false and the remaining elements are not returned.
    If the service pack is not available for use or is not authorized, then \"authorized\" is false and the remaining elements are not returned.
    \"authorizedQuantity\" can be unlimited or a quantity. In the case of a service pack, \"authorizedQuantity\" is the service pack's quantity.
    \"authorizable\" is applicable for user services and group services; it is not returned for service packs."""

    authorized: bool

    authorizedQuantity: Optional[UnboundedNonNegativeInt] = None

    usedQuantity: Optional[UnboundedNonNegativeInt] = None

    authorizable: Optional[bool] = None


@dataclass
class GroupServiceGetAuthorizedListResponse(OCIDataResponse):
    """Response to GroupServiceGetAuthorizedListRequest."""

    servicePackName: List[str] = field(default_factory=list)

    groupServiceName: List[str] = field(default_factory=list)

    userServiceName: List[str] = field(default_factory=list)


@dataclass
class GroupServiceInstancePrivacyGetResponse17sp4(OCIDataResponse):
    """Response to GroupServiceInstancePrivacyGetRequest17sp4."""

    enableDirectoryPrivacy: bool

    enableAutoAttendantExtensionDialingPrivacy: bool

    enableAutoAttendantNameDialingPrivacy: bool


@dataclass
class GroupServiceIsAssignedResponse(OCIDataResponse):
    """Returns true if the GroupService is assigned, otherwise false."""

    isAssigned: bool


@dataclass
class GroupServicePhoneNumberLookupResponse(OCIDataResponse):
    """Response to the GroupServicePhoneNumberLookupRequest.
    The column headings for the userTable are: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\" and \"Department\"."""

    userTable: OCITable


@dataclass
class GroupSessionAdmissionControlGetAvailableDeviceListResponse(OCIDataResponse):
    """Response to GroupSessionAdmissionControlGetAvailableDeviceListRequest.
    Contains a table of devices can be assigned to session admission control group in the group."""

    accessDevice: List[AccessDevice] = field(default_factory=list)


@dataclass
class GroupSessionAdmissionControlGetResponse(OCIDataResponse):
    """Response to the GroupSessionAdmissionControlGetRequest.
    The response contains the session admission control capacity allocated for the group."""

    restrictAggregateSessions: bool

    countIntraGroupSessions: bool

    maxSessions: Optional[int] = None

    maxUserOriginatingSessions: Optional[int] = None

    maxUserTerminatingSessions: Optional[int] = None


@dataclass
class GroupSessionAdmissionControlGroupGetListResponse(OCIDataResponse):
    """Response to GroupSessionAdmissionControlGroupGetListRequest.
    Contains a table of session admission control group configured in the group.
    The column headings are: \"Name\", \"Is Default\", \"Maximum Sessions\", \"Maximum Originating Sessions\", \"Maximum Terminating Sessions\"."""

    sessionAdmissionControlGroupTable: OCITable


@dataclass
class GroupSessionAdmissionControlGroupGetResponse21sp1V2(OCIDataResponse):
    """Response to GroupSessionAdmissionControlGroupGetRequest21sp1V2.
    Returns the profile information for the session admission control group."""

    maxSession: int

    reservedSession: int

    defaultGroup: bool

    countIntraSACGroupSessions: bool

    blockEmergencyAndRepairCallsDueToSACLimits: bool

    maxUserOriginatingSessions: Optional[int] = None

    maxUserTerminatingSessions: Optional[int] = None

    reservedUserOriginatingSessions: Optional[int] = None

    reservedUserTerminatingSessions: Optional[int] = None

    devices: List[AccessDevice] = field(default_factory=list)

    mediaGroupName: Optional[str] = None

    accessInfoPattern: Optional[str] = None


@dataclass
class GroupShInterfaceGetUserListResponse21sp1(OCIDataResponse):
    """Response to the GroupShInterfaceGetUserListRequest21sp1.
    The response contains the Sh Non Transparent data and associated Public User Identity
    information for every Public User Identity in the group."""

    entry: List[ShInterfaceUserListEntry21sp1] = field(default_factory=list)


@dataclass
class GroupSpeedDial100GetResponse17sp1(OCIDataResponse):
    """Response to the GroupSpeedDial100GetRequest17sp1."""

    prefix: Optional[str] = None


@dataclass
class GroupStirShakenGetResponse23V2(OCIDataResponse):
    """Response to the GroupStirShakenGetRequest23V2."""

    useParentLevelSettings: bool

    signingPolicy: str

    taggingPolicy: str

    tagFromOrPAI: str

    verstatTag: str

    useOSValueForOrigId: bool

    attestationLevel: str

    enableVerification: bool

    verificationErrorHandling: str

    proxyVerstatToCNAMSubscribe: bool

    useUnknownHeadersFromCNAMNotify: bool

    enableSigningForUnscreenedTrunkGroupOriginations: bool

    enableTaggingForUnscreenedTrunkGroupOriginations: bool

    unscreenedTrunkGroupOriginationAttestationLevel: str

    includeTaggedHeadersToAccessSide: bool

    proxyIdentityHeaderToAccessSide: bool

    checkDirectoryNumbersForAttestation: bool

    matchUnassignedNumbersOnly: bool

    enableTaggingForRedirectedCalls: bool

    preferIngressTagging: bool

    signingServiceURL: Optional[str] = None

    origUUID: Optional[str] = None

    verificationServiceURL: Optional[str] = None


@dataclass
class GroupTemplateOnlyDeviceFileGetListResponse(OCIDataResponse):
    """Response to GroupTemplateOnlyDeviceFileGetListRequest.
    Contains a list of template files used to support a Visual Device Management device."""

    templateFileUrl: List[str] = field(default_factory=list)


@dataclass
class GroupThirdPartyEmergencyCallingGetResponse22(OCIDataResponse):
    """Response to the GroupThirdPartyEmergencyCallingGetRequest22.
    The response contains the third-party emergency call service settings for the Group."""

    enableDeviceManagement: bool

    enableRouting: bool

    customerId: Optional[str] = None

    secretKey: Optional[str] = None


@dataclass
class GroupThirdPartyVoiceMailSupportGetResponse(OCIDataResponse):
    """Response to GroupThirdPartyVoiceMailSupportGetRequest."""

    isActive: bool

    groupServer: Optional[str] = None


@dataclass
class GroupTrunkGroupGetAvailableDetailListResponse(OCIDataResponse):
    """Response to GroupTrunkGroupGetAvailableDetailListRequest."""

    trunkGroup: List[object] = field(default_factory=list)


@dataclass
class GroupTrunkGroupGetAvailableHostedUserListResponse(OCIDataResponse):
    """Response to the GroupTrunkGroupGetAvailableHostedUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    userTable: OCITable


@dataclass
class GroupTrunkGroupGetInstanceListResponse14sp4(OCIDataResponse):
    """Response to GroupTrunkGroupGetInstanceListRequest14sp4.
    Contains a table with column headings \"Name\", \"Department\", \"Device Name\", \"Device Level\",
    \"Group Id\".
    The \"Device Level\" column contains one of the AccessDeviceLevel enumerated constants."""

    trunkGroupTable: OCITable


@dataclass
class GroupTrunkGroupGetInstanceResponse23(OCIDataResponse):
    """Response to GroupTrunkGroupGetInstanceRequest23.
    Returns the profile information for the Trunk Group.
    Contains a hosted user table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\", \"Email Address\".
    Following attributes are only used in IMS mode:
      implicitRegistrationSetSupportPolicy
      useSystemImplicitRegistrationSetSupportPolicy
      sipIdentityForPilotAndProxyTrunkModesPolicy
      useSystemSIPIdentityForPilotAndProxyTrunkModesPolicy"""

    maxActiveCalls: int

    enableBursting: bool

    capacityExceededTrapInitialCalls: int

    capacityExceededTrapOffsetCalls: int

    invitationTimeout: int

    requireAuthentication: bool

    allowTerminationToTrunkGroupIdentity: bool

    allowTerminationToDtgIdentity: bool

    includeTrunkGroupIdentity: bool

    includeDtgIdentity: bool

    includeTrunkGroupIdentityForNetworkCalls: bool

    includeOtgIdentityForNetworkCalls: bool

    enableNetworkAddressIdentity: bool

    allowUnscreenedCalls: bool

    allowUnscreenedEmergencyCalls: bool

    pilotUserCallingLineIdentityForExternalCallsPolicy: str

    pilotUserChargeNumberPolicy: str

    routeToPeeringDomain: bool

    prefixEnabled: bool

    statefulReroutingEnabled: bool

    sendContinuousOptionsMessage: bool

    continuousOptionsSendingIntervalSeconds: int

    failureOptionsSendingIntervalSeconds: int

    failureThresholdCounter: int

    successThresholdCounter: int

    inviteFailureThresholdCounter: int

    inviteFailureThresholdWindowSeconds: int

    trunkGroupState: str

    pilotUserCallingLineAssertedIdentityPolicy: str

    useSystemCallingLineAssertedIdentityPolicy: bool

    totalActiveIncomingCalls: int

    totalActiveOutgoingCalls: int

    pilotUserCallOptimizationPolicy: str

    clidSourceForScreenedCallsPolicy: str

    useSystemCLIDSourceForScreenedCallsPolicy: bool

    userLookupPolicy: str

    useSystemUserLookupPolicy: bool

    pilotUserCallingLineIdentityForEmergencyCallsPolicy: str

    implicitRegistrationSetSupportPolicy: str

    useSystemImplicitRegistrationSetSupportPolicy: bool

    sipIdentityForPilotAndProxyTrunkModesPolicy: str

    useSystemSIPIdentityForPilotAndProxyTrunkModesPolicy: bool

    useSystemSupportConnectedIdentityPolicy: bool

    supportConnectedIdentityPolicy: str

    useSystemOptionsMessageResponseStatusCodes: bool

    pilotUserId: Optional[str] = None

    department: Optional[DepartmentKey] = None

    accessDevice: Optional[AccessDevice] = None

    maxIncomingCalls: Optional[int] = None

    maxOutgoingCalls: Optional[int] = None

    burstingMaxActiveCalls: Optional[int] = None

    burstingMaxIncomingCalls: Optional[int] = None

    burstingMaxOutgoingCalls: Optional[int] = None

    capacityExceededAction: Optional[str] = None

    capacityExceededForwardAddress: Optional[str] = None

    capacityExceededRerouteTrunkGroupKey: Optional[TrunkGroupKey] = None

    unreachableDestinationAction: Optional[str] = None

    unreachableDestinationForwardAddress: Optional[str] = None

    unreachableDestinationRerouteTrunkGroupKey: Optional[TrunkGroupKey] = None

    sipAuthenticationUserName: Optional[str] = None

    hostedUserTable: Optional[OCITable] = None

    trunkGroupIdentity: Optional[str] = None

    otgDtgIdentity: Optional[str] = None

    callForwardingAlwaysAction: Optional[str] = None

    callForwardingAlwaysForwardAddress: Optional[str] = None

    callForwardingAlwaysRerouteTrunkGroupKey: Optional[TrunkGroupKey] = None

    peeringDomain: Optional[str] = None

    prefix: Optional[str] = None

    optionsMessageResponseStatusCode: List[str] = field(default_factory=list)


@dataclass
class GroupTrunkGroupGetInstanceUserListResponse14sp4(OCIDataResponse):
    """Response to GroupTrunkGroupGetInstanceUserListRequest14sp4.
    The response contains a 9 column table with column headings \"User Id\", \"Last Name\",
    \"First Name\", \"Department\", \"Phone Number\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Extension\", \"Email Address\"."""

    trunkGroupUserTable: OCITable


@dataclass
class GroupTrunkGroupGetResponse23(OCIDataResponse):
    """Response to the GroupTrunkGroupGetRequest23.
    The response contains the maximum and bursting maximum permissible active trunk group calls for the group."""

    maxActiveCalls: int

    maxAvailableActiveCalls: UnboundedNonNegativeInt

    burstingMaxActiveCalls: UnboundedNonNegativeInt

    burstingMaxAvailableActiveCalls: UnboundedNonNegativeInt

    maxAvailableNumberOfBurstingBTLUs: UnboundedNonNegativeInt

    numberOfBurstingBTLUs: Optional[int] = None


@dataclass
class GroupTrunkGroupSecurityClassificationGetResponse(OCIDataResponse):
    """Response to the GroupTrunkGroupSecurityClassificationGetRequest."""

    defaultSecurityClassification: Optional[str] = None


@dataclass
class GroupTrunkGroupStirShakenGetResponse23V2(OCIDataResponse):
    """Response to the GroupTrunkGroupStirShakenGetRequest23V2."""

    useParentLevelSettings: bool

    signingPolicy: str

    taggingPolicy: str

    tagFromOrPAI: str

    verstatTag: str

    useOSValueForOrigId: bool

    attestationLevel: str

    enableSigningForUnscreenedTrunkGroupOriginations: bool

    enableTaggingForUnscreenedTrunkGroupOriginations: bool

    unscreenedTrunkGroupOriginationAttestationLevel: str

    checkDirectoryNumbersForAttestation: bool

    matchUnassignedNumbersOnly: bool

    enableTaggingForRedirectedCalls: bool

    signingServiceURL: Optional[str] = None

    origUUID: Optional[str] = None


@dataclass
class GroupTrunkGroupUserCreationTaskGetListResponse14sp4(OCIDataResponse):
    """Response to GroupTrunkGroupUserCreationTaskGetListRequest14sp4.
    Contains a table with a row for each user creation task and column headings :
    \"Name\", \"Status\", \"Users Created\", \"Total Users To Create\", \"Error Count\"."""

    taskTable: OCITable


@dataclass
class GroupTrunkGroupUserCreationTaskGetResponse14sp4(OCIDataResponse):
    """Response to a GroupTrunkGroupUserCreationTaskGetRequest14sp4."""

    userIdFormat: str

    userIdDomain: str

    populateExtension: bool

    linePortFormat: str

    linePortDomain: str

    populateContact: bool

    usersCreated: int

    totalUsersToCreate: int

    errorCount: int

    status: str

    userCreationMode: str

    taskSummary: str

    reportFileKey: str

    contactFormat: Optional[str] = None

    contactDomain: Optional[str] = None

    servicePackName: List[str] = field(default_factory=list)

    userServiceName: List[str] = field(default_factory=list)


@dataclass
class GroupUserCallForwardingSettingsGetListResponse(OCIDataResponse):
    """Response to the GroupUserCallForwardingSettingsGetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\",
    \"Hiragana Last Name\", and \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\", \"In Trunk Group\", \"Email Address\",
    \"Is Active\", \"Forwarding Address\".
    \"Is Active\" is \"true\" or \"false\".
    The \"Forwarding Address\" is the Call Forwarding service's forwarding address.
    If the service is Call Forwarding Selective, the default forwarding address is returned.
    \"Phone Number\" is presented in the E164 format."""

    userCallForwardingTable: OCITable


@dataclass
class GroupUserCallWaitingSettingsGetListResponse(OCIDataResponse):
    """Response to the GroupUserCallWaitingSettingsGetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana
    Last Name\", and \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\", \"In Trunk Group\", \"Email Address\", \"Is Active\".
    \"Is Active\" is \"true\" or \"false\".
    \"Phone Number\" is presented in the E164 format."""

    userCallWaitingTable: OCITable


@dataclass
class GroupUserCallingPlanSettingsGetListResponse(OCIDataResponse):
    """Response to the GroupUserCallingPlanSettingsGetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana
    Last Name\", and \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\", \"In Trunk Group\", \"Email Address\", \"Use Custom Settings\".
    \"Use Custom Settings\" is \"true\" or \"false\".
    \"Phone Number\" is presented in the E164 format."""

    userCallingPlanTable: OCITable


@dataclass
class GroupUserHotelingGuestSettingsGetListResponse(OCIDataResponse):
    """Response to the GroupUserHotelingGuestSettingsGetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\",
    \"Hiragana Last Name\", and \"Hiragana First Name\", \"Phone Number\",
    \"Extension\", \"Department\", \"In Trunk Group\", \"Email Address\", \"Is Active\".
    \"Is Active\" is \"true\" or \"false\".
    \"Phone Number\" is presented in the E164 format."""

    userHotelingGuestTable: OCITable


@dataclass
class GroupVirtualOnNetEnterpriseExtensionsGetUserListResponse(OCIDataResponse):
    """Response to GroupVirtualOnNetEnterpriseExtensionsGetUserListRequest.
    Contains a table with column headings: \"Last Name\",
    \"First Name\", \"Phone Number\", \"Extension\",
    \"Virtual On-Net Call Type Name\"
    in a row for each user."""

    userTable: OCITable


@dataclass
class GroupVirtualOnNetEnterpriseExtensionsGetUserResponse(OCIDataResponse):
    """Response to GroupVirtualOnNetEnterpriseExtensionsGetUserRequest."""

    extension: str

    firstName: str

    lastName: str

    callingLineIdFirstName: str

    callingLineIdLastName: str

    virtualOnNetCallTypeName: str


@dataclass
class GroupVisualDeviceManagementGetDeviceInfoResponse(OCIDataResponse):
    """Response to GroupVisualDeviceManagementGetDeviceInfoRequest."""

    deviceType: str

    supportVisualDeviceManagement: bool

    macAddress: Optional[str] = None

    primaryUser: Optional[PrimaryUserInfo] = None


@dataclass
class GroupVoiceMessagingGroupGetResponse(OCIDataResponse):
    """Response to GroupVoiceMessagingGroupGetRequest.
    Contains the group's voice messaging settings."""

    useMailServerSetting: str

    warnCallerBeforeRecordingVoiceMessage: bool

    allowUsersConfiguringAdvancedSettings: bool

    allowComposeOrForwardMessageToEntireGroup: bool

    mailServerProtocol: str

    realDeleteForImap: bool

    maxMailboxLengthMinutes: int

    doesMessageAge: bool

    holdPeriodDays: int

    mailServerNetAddress: Optional[str] = None


@dataclass
class GroupVoiceMessagingGroupGetVoicePortalBrandingResponse20(OCIDataResponse):
    """Response to the GroupVoiceMessagingGroupGetVoicePortalBrandingRequest20."""

    voicePortalGreetingSelection: str

    voiceMessagingGreetingSelection: str

    voicePortalGreetingFile: Optional[AnnouncementFileKey] = None

    voiceMessagingGreetingFile: Optional[AnnouncementFileKey] = None


@dataclass
class GroupVoiceMessagingGroupGetVoicePortalResponse21sp1(OCIDataResponse):
    """Response to the GroupVoiceMessagingGroupGetVoicePortalRequest21sp1.

    The following elements are only used in XS data mode:
    enableExtendedScope

    The following elements are only used in AS data mode:
    expressMode, value \"false\" is returned in XS data mode."""

    serviceUserId: str

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    isActive: bool

    enableExtendedScope: bool

    allowIdentificationByPhoneNumberOrVoiceMailAliasesOnLogin: bool

    useVoicePortalWizard: bool

    voicePortalExternalRoutingScope: str

    useExternalRouting: bool

    expressMode: bool

    externalRoutingAddress: Optional[str] = None

    homeZoneName: Optional[str] = None

    networkClassOfService: Optional[str] = None


@dataclass
class GroupVoiceXmlGetInstanceListResponse(OCIDataResponse):
    """Response to the GroupVoiceXmlGetInstanceListRequest.
    Contains a table with column headings:
    \"Service User Id\", \"Name\", \"Phone Number\", \"Extension\", \"Department\", \"Is Active\"
    and \"Is Webex Meeting Callback\".
    The column values for \"Is Active\" can either be true, or false."""

    voiceXmlTable: OCITable


@dataclass
class GroupVoiceXmlGetInstanceResponse23(OCIDataResponse):
    """Response to GroupVoiceXmlGetInstanceRequest23.
    Contains the service profile information and possibly access device information."""

    serviceInstanceProfile: ServiceInstanceReadProfile19sp1

    webexMeetingCallback: bool

    networkClassOfService: Optional[str] = None

    accessDeviceEndpoint: Optional[AccessDeviceEndpointWithPortNumberRead22] = None


@dataclass
class GroupXsiPolicyProfileGetAssignedListResponse(OCIDataResponse):
    """Response to GroupXsiPolicyProfileGetAssignedListRequest.
    Contains a table of all Xsi Policy Profile assigned to.
    The column headings are: \"Name\", \"Level\", \"Description\" and \"Default\"."""

    assignedTable: OCITable


@dataclass
class GroupXsiPolicyProfileGetAssignedUserListResponse(OCIDataResponse):
    """Response to GroupXsiPolicyProfileGetAssignedUserListRequest.
    Contains a table of user that have the user Xsi Policy Profile
    assigned. The column headings are: \"User Id\", \"Last Name\", \"First Name\",
    \"Phone Number\" \"Department\" and \"Extension\"."""

    userTable: OCITable


@dataclass
class LoginResponse22V5(OCIDataResponse):
    """Response to the OCI login request.

    The following data elements are only returned in AS data mode:
      resellerId

    The parameter tokenRevocationTime is represented in the number of milliseconds
    since January 1, 1970, 00:00:00 GMT, and it is set to the more current time between
    the system level token revocation time and user level token revocation time."""

    loginType: str

    locale: str

    encoding: str

    isEnterprise: bool

    userDomain: str

    groupId: Optional[str] = None

    serviceProviderId: Optional[str] = None

    passwordExpiresDays: Optional[int] = None

    resellerId: Optional[str] = None

    tokenRevocationTime: Optional[int] = None


@dataclass
class LoginResponse14sp4(OCIDataResponse):
    loginType: str

    locale: str

    encoding: str

    isEnterprise: bool

    userDomain: str

    groupId: Optional[str] = None

    serviceProviderId: Optional[str] = None

    passwordExpiresDays: Optional[int] = None

    resellerId: Optional[str] = None

    tokenRevocationTime: Optional[int] = None


@dataclass
class PasswordGenerateResponse(OCIDataResponse):
    """Response to the PasswordGenerateRequest.
    The response contains the requested passwords."""

    systemAdministratorPassword: Optional[str] = None

    serviceProviderAdministratorPassword: Optional[str] = None

    groupAdministratorPassword: Optional[str] = None

    userPassword: Optional[str] = None

    userPasscode: Optional[str] = None

    userSIPAuthenticationPassword: Optional[str] = None

    accessDeviceAuthenticationPassword: Optional[str] = None

    trunkGroupAuthenticationPassword: Optional[str] = None


@dataclass
class PublicClusterGetFullyQualifiedDomainNameResponse(OCIDataResponse):
    """Response to PublicClusterGetFullyQualifiedDomainNameRequest."""

    publicClusterFQDN: Optional[str] = None


@dataclass
class ResellerAdminAlternateIdGetListResponse(OCIDataResponse):
    """Response to ResellerAdminAlternateIdGetListRequest.
    Contains a table of the main admin user id and the alternate admin user ids, the column headings are: \"User Id\", \"Description\", \"Alternate\".
    The possible values for \"Alternate\" are \"true\" and \"false\".
    The \"Description\" is only present for alternate admin user Ids."""

    adminUserIdTable: OCITable


@dataclass
class ResellerAdminGetListResponse(OCIDataResponse):
    """Response to ResellerAdminGetListRequest.
    Contains a 4 column table with column headings \"Administrator ID\",
    \"Last Name\", \"First Name\", \"Language\"."""

    resellerAdminTable: OCITable


@dataclass
class ResellerAdminGetResponse22V2(OCIDataResponse):
    """Response to the ResellerAdminGetRequest22V2.
    The response contains the reseller administrators profile information."""

    resellerId: str

    language: str

    accountDisabled: bool

    lastAuthenticatedDate: str

    firstName: Optional[str] = None

    lastName: Optional[str] = None


@dataclass
class ResellerCallAdmissionControlPoliciesGetResponse(OCIDataResponse):
    """Response to the ResellerCallAdmissionControlPoliciesGetRequest.
    The response contains the reseller call admission control policies information."""

    enableCallAdmissionControl: bool

    maxConcurrentNetworkSessions: int

    maxNetworkCallsPerSecond: int

    maxConcurrentExternalSIPRECSessions: int

    maxConcurrentNetworkSessionsThreshold: Optional[int] = None

    maxNetworkCallsPerSecondThreshold: Optional[int] = None

    maxConcurrentExternalSIPRECSessionsThreshold: Optional[int] = None


@dataclass
class ResellerCallCenterGetResponse(OCIDataResponse):
    """Response to ResellerCallCenterGetRequest."""

    defaultFromAddress: Optional[str] = None


@dataclass
class ResellerCallNotifyGetResponse(OCIDataResponse):
    """Response to ResellerCallNotifyGetRequest."""

    defaultFromAddress: Optional[str] = None


@dataclass
class ResellerCallPoliciesGetResponse22(OCIDataResponse):
    """Response to ResellerCallPoliciesGetRequest22."""

    forceRedirectingUserIdentityForRedirectedCalls: bool

    applyRedirectingUserIdentityToNetworkLocations: bool


@dataclass
class ResellerCallRecordingGetResponse(OCIDataResponse):
    """Response to the ResellerCallRecordingGetRequest.
    The response contains the reseller’s Call Recording attribute."""

    FQDN: Optional[str] = None


@dataclass
class ResellerCollaborateGetResponse(OCIDataResponse):
    """Response to ResellerCollaborateGetRequest."""

    collaborateFromAddress: Optional[str] = None


@dataclass
class ResellerDeviceActivationPolicyGetResponse(OCIDataResponse):
    """Response to ResellerDeviceActivationPolicyGetRequest."""

    useResellerSettings: bool

    allowActivationCodeRequestByUser: bool

    sendActivationCodeInEmail: bool


@dataclass
class ResellerEmergencyCallNotificationGetResponse(OCIDataResponse):
    """Response to ResellerEmergencyCallNotificationGetRequest."""

    defaultFromAddress: Optional[str] = None


@dataclass
class ResellerEmergencyZonesGetResponse(OCIDataResponse):
    """Response to ResellerEmergencyZonesGetRequest."""

    defaultFromAddress: Optional[str] = None


@dataclass
class ResellerGetListResponse(OCIDataResponse):
    """Response to the ResellerGetListRequest.
    Contains a 2 column table with column headings \"Reseller Id\", \"Reseller Name\" and \"Reseller External Id\". A row for each reseller."""

    resellerTable: OCITable


@dataclass
class ResellerGetResponse22V2(OCIDataResponse):
    """Response to the ResellerGetRequest22V2."""

    resellerId: str

    resellerName: Optional[str] = None

    resellerExternalId: Optional[str] = None


@dataclass
class ResellerIntegratedIMPGetResponse22(OCIDataResponse):
    """Response to the ResellerIntegratedIMPGetRequest22.
    The response contains the reseller Integrated IMP service attributes."""

    useSystemServiceDomain: bool

    useSystemMessagingServer: bool

    defaultImpIdType: str

    serviceDomain: Optional[str] = None

    servicePort: Optional[int] = None

    provisioningUrl: Optional[str] = None

    provisioningUserId: Optional[str] = None

    boshURL: Optional[str] = None


@dataclass
class ResellerMailParametersGetResponse(OCIDataResponse):
    """Response to ResellerMailParametersGetRequest."""

    defaultFromAddress: Optional[str] = None


@dataclass
class ResellerMeetMeConferencingGetResponse22(OCIDataResponse):
    """Response to ResellerMeetMeConferencingGetRequest22."""

    conferenceFromAddress: Optional[str] = None

    maxAllocatedPorts: Optional[int] = None

    disableUnlimitedMeetMePorts: Optional[bool] = None

    enableMaxAllocatedPorts: Optional[bool] = None


@dataclass
class ResellerNetworkClassOfServiceGetAssignedListResponse(OCIDataResponse):
    """Response to ResellerNetworkClassOfServiceGetAssignedListRequest.
    Contains a table of all Network Classes of Service assigned to the
    reseller. The column headings are: \"Name\", \"Description\" and \"Default\"."""

    networkClassOfServiceTable: OCITable


@dataclass
class ResellerNetworkClassOfServiceGetAssignedServiceProviderListResponse(
    OCIDataResponse
):
    """Response to ResellerNetworkClassOfServiceGetAssignedServiceProviderListRequest.
    Contains a table of Service Providers that have the Network Class of Service
    assigned. The column headings are: \"Service Provider Id\" and \"Service Provider Name\"."""

    spTable: OCITable


@dataclass
class ResellerResourcePriorityGetResponse(OCIDataResponse):
    """Response to the ResellerResourcePriorityGetRequest.
    The response contains the reseller Resource Priority service attributes.
    If useSystemSettings is true, the parameters sendResourcePriorityToNetwork and
    resourcePriority will not be returned in the response."""

    useSystemSettings: bool

    sendResourcePriorityToNetwork: bool

    resourcePriority: str


@dataclass
class ResellerServiceAuthorizationGetResponse(OCIDataResponse):
    """Response to the ResellerServiceAuthorizationGetRequest."""

    serviceOffering: Optional[int] = None


@dataclass
class ResellerStirShakenGetResponse23V2(OCIDataResponse):
    """Response to the ResellerStirShakenGetRequest23V2."""

    useParentLevelSettings: bool

    signingPolicy: str

    taggingPolicy: str

    signEmergencyCalls: bool

    tagEmergencyCalls: bool

    tagFromOrPAI: str

    verstatTag: str

    useOSValueForOrigId: bool

    attestationLevel: str

    enableVerification: bool

    verificationErrorHandling: str

    proxyVerstatToCNAMSubscribe: bool

    useUnknownHeadersFromCNAMNotify: bool

    enableSigningForUnscreenedTrunkGroupOriginations: bool

    enableTaggingForUnscreenedTrunkGroupOriginations: bool

    unscreenedTrunkGroupOriginationAttestationLevel: str

    verifyGETSCalls: bool

    includeTaggedHeadersToAccessSide: bool

    proxyIdentityHeaderToAccessSide: bool

    checkDirectoryNumbersForAttestation: bool

    matchUnassignedNumbersOnly: bool

    enableTaggingForRedirectedCalls: bool

    preferIngressTagging: bool

    signingServiceURL: Optional[str] = None

    origUUID: Optional[str] = None

    verificationServiceURL: Optional[str] = None


@dataclass
class ResellerVoiceMessagingGroupGetResponse(OCIDataResponse):
    """Response to ResellerVoiceMessagingGroupGetRequest."""

    deliveryFromAddress: Optional[str] = None

    notificationFromAddress: Optional[str] = None

    voicePortalLockoutFromAddress: Optional[str] = None


@dataclass
class ResellerXsiPolicyProfileGetAssignedListResponse(OCIDataResponse):
    """Response to ResellerXsiPolicyProfileGetAssignedListRequest.
    Contains a table of all Xsi Policy Profile assigned to.
    The column headings are: \"Name\", \"Level\", \"Description\" and \"Default\"."""

    assignedTable: OCITable


@dataclass
class ResellerXsiPolicyProfileGetAssignedServiceProviderListResponse(OCIDataResponse):
    """Response to ResellerXsiPolicyProfileGetAssignedServiceProviderListRequest.
    Contains a table of Service Providers that have the Xsi Policy Profile
    assigned. The column headings are: \"Organization ID\", \"Organization Name\", \"Organization Type\"."""

    svcProviderTable: OCITable


@dataclass
class ServiceProviderAccessDeviceCustomTagGetListResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceCustomTagGetListRequest.
    Contains a table of custom configuration tags managed by the Device Management System on a per-device profile basis.
    In AS data mode, the column headings are:
      \"Tag Name\", \"Tag Value\", \"Actual Tag Value\".
    In XS data mode, the column headings are:
      \"Tag Name\", \"Tag Value\", \"Actual Tag Value\" if request is invoked by an admin without system privileges.
      \"Tag Name\", \"Tag Value\", \"Is Encrypted\", \"Actual Tag Value\" if request is invoked by an admin with system privileges."""

    deviceCustomTagsTable: OCITable


@dataclass
class ServiceProviderAccessDeviceDeviceActivationGetResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceDeviceActivationGetRequest.
    The response contains the activation code (if available), the expiry time (if available) and the activation state.
    The expiryTime is represented as a timestamp, i.e. the number of milliseconds
    since January 1, 1970, 00:00:00 GMT."""

    activationState: str

    activationCode: Optional[str] = None

    expiryTime: Optional[int] = None


@dataclass
class ServiceProviderAccessDeviceFileGetListResponse14sp8(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceFileGetListRequest14sp8.
    Contains a table of device files managed by the Device Management System on a per-device profile basis.
    The column headings are: \"File Format\", \"Is Authenticated\", \"Access URL\", \"Repository URL\", \"Template URL\", \"Extended Capture URL\", \"Is File Linked\".

    The following column is only populated in AS data mode for leaf devices.
      \"Is File Linked\" """

    deviceFilesTable: OCITable


@dataclass
class ServiceProviderAccessDeviceFileGetResponse20(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceFileGetRequest21."""

    fileSource: str

    accessUrl: str

    configurationFileName: Optional[str] = None

    repositoryUrl: Optional[str] = None

    templateUrl: Optional[str] = None

    extendedCaptureEnabled: Optional[bool] = None

    extendedCaptureURL: Optional[str] = None

    allowUploadFromDevice: Optional[bool] = None


@dataclass
class ServiceProviderAccessDeviceGetAvailableCustomTagListResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetAvailableCustomTagListRequest.
    Contains a table of all available custom tags managed by the Device Management System on a per-device profile basis.

    In AS data mode, the column headings are: \"Tag Name\", \"Tag Value\", \"Tag Level\", \"Tag Set Name\", \"Region Name\".

    In XS data mode:
      the column headings are: \"Tag Name\", \"Tag Value\", \"Tag Level\", \"Tag Set Name\", \"Is Encrypted\" if request is invoked by a System administrator or by an administrator with higher priviledges, otherwise the column headings are: \"Tag Name\", \"Tag Value\", \"Tag Level\", \"Tag Source\", \"Tag Set Name\".

    \"Tag Level\" can take the value: \"System Default\", \"System\", \"Service Provider\", \"Group\" or \"Device Profile\"."""

    deviceAvailableCustomTagsTable: OCITable


@dataclass
class ServiceProviderAccessDeviceGetEnhancedConfigurationTypeListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderAccessDeviceGetEnhancedConfigurationTypeListRequest."""

    deviceType: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderAccessDeviceGetEnhancedConfigurationTypeResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetEnhancedConfigurationTypeRequest."""

    supportsEnhancedConfiguration: bool

    supportsReset: bool

    configurationType: Optional[str] = None

    configurationFileName: Optional[str] = None


@dataclass
class ServiceProviderAccessDeviceGetLinkedLeafDeviceListResponse22(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetLinkedLeafDeviceListRequest22."""

    treeDeviceLinkId: str

    leafDeviceKey: List[AccessDeviceKey] = field(default_factory=list)

    supportLinks: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderAccessDeviceGetLinkedTreeDeviceResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetLinkedTreeDeviceRequest."""

    treeDeviceInfo: Optional[TreeDeviceInfo] = None


@dataclass
class ServiceProviderAccessDeviceGetListResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetListRequest.
    Contains a table of devices configured in the service provider.
    The column headings are: \"Device Name\", \"Device Type\", \"Available Ports\",
    \"Net Address\", \"MAC Address\", \"Status\", \"Version\", and \"Access Device External Id\".

    The following columns are only populated in AS data mode:
      \"Access Device External Id\" """

    accessDeviceTable: OCITable


@dataclass
class ServiceProviderAccessDeviceGetNativeTagsWithLogicListResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetNativeTagsWithLogicListRequest.
    Contains a table of all native tags with logic managed by the Device Management System on a per-device profile basis.

    The column headings are: \"Tag Name\", \"Tag Value\"."""

    deviceNativeTagsWithLogicTable: OCITable


@dataclass
class ServiceProviderAccessDeviceGetPagedSortedListResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetPagedSortedListRequest.
    Contains a table of devices configured at service provider level.
    The column headings are: \"Device Name\", \"Device Type\", \"Available Ports\", \"Net Address\", \"MAC Address\", \"Status\", \"Version\", and \"Support Visual Device Management API\".
    When CloudPBX is not licensed, the column \"Support Visual Device Management API\" values are not returned."""

    accessDeviceTable: OCITable


@dataclass
class ServiceProviderAccessDeviceGetResponse24V3(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetRequest24V3.

    The following elements are only used in AS data mode:
       useHotline
       hotlineContact
       serviceProviderId
       deviceName
       deviceExternalId
       deviceCode
       deviceIPEI
       deviceIndex
       useDeviceCode
       authBearerSubject"""

    deviceType: str

    protocol: str

    numberOfPorts: UnboundedPositiveInt

    numberOfAssignedPorts: int

    status: str

    serviceProviderId: str

    deviceName: str

    netAddress: Optional[str] = None

    port: Optional[int] = None

    outboundProxyServerNetAddress: Optional[str] = None

    stunServerNetAddress: Optional[str] = None

    macAddress: Optional[str] = None

    serialNumber: Optional[str] = None

    description: Optional[str] = None

    physicalLocation: Optional[str] = None

    transportProtocol: Optional[str] = None

    useCustomUserNamePassword: Optional[bool] = None

    userName: Optional[str] = None

    version: Optional[str] = None

    deviceExternalId: Optional[str] = None

    deviceCode: Optional[str] = None

    deviceIPEI: Optional[str] = None

    deviceIndex: Optional[int] = None

    useDeviceCode: Optional[bool] = None

    authBearerSubject: Optional[str] = None


@dataclass
class ServiceProviderAccessDeviceGetUserListResponse21sp1(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceGetUserListRequest21sp1.
    The column headings for the deviceUserTable are: \"Line/Port\", \"Last Name\",
    \"First Name\", \"Phone Number\", \"Group Id\", \"User Id\",
    \"User Type\", \"Endpoint Type\", \"Primary Line/Port\", \"Order\", \"Extension\", \"Department\", \"Email Address\", \"Private Identity\".
    In IMS mode, the table will contain a row for each TEL-URI in the Phone Number column.
    In standalone mode, rows for the alternate numbers are not included.
    The User Type column contains one of the enumerated UserType values.
    The Endpoint Type column contains one of the enumerated EndpointType21sp1 values.
    The value Mobility in Endpoint Type column is only applicable in AS data mode.
    The Private Identity column is empty is AS mode."""

    deviceUserTable: OCITable


@dataclass
class ServiceProviderAccessDeviceTagSetGetResponse(OCIDataResponse):
    """Response to ServiceProviderAccessDeviceTagSetGetRequest.
    The response includes a tag set name defined in the access device."""

    tagSetName: Optional[str] = None


@dataclass
class ServiceProviderAdminAlternateIdGetListResponse(OCIDataResponse):
    """Response to ServiceProviderAdminAlternateIdGetListRequest.
    Contains a table of the main admin user id and the alternate admin user ids, the column headings are: \"User Id\", \"Description\", \"Alternate\".
    The possible values for \"Alternate\" are \"true\" and \"false\".
    The \"Description\" is only present for alternate admin user Ids."""

    adminUserIdTable: OCITable


@dataclass
class ServiceProviderAdminGetListResponse14(OCIDataResponse):
    """Response to ServiceProviderAdminGetListRequest14.
    Contains a 7 column table with column headings \"Administrator ID\",
    \"Last Name\", \"First Name\", \"Administrator Type\", \"Language\", \"Locale\" and \"Encoding\".

    The following columns are only returned in AS data mode:
      \"Locale\" and \"Encoding\" """

    serviceProviderAdminTable: OCITable


@dataclass
class ServiceProviderAdminGetPagedSortedListResponse(OCIDataResponse):
    """Response to ServiceProviderAdminGetPagedSortedListRequest.
    Contains a 7 column table with column headings \"Administrator ID\",
    \"Last Name\", \"First Name\", \"Administrator Type\", \"Language\", \"Locale\" and \"Encoding\".
    The following columns are only returned in AS data mode:
    \"Locale\" and \"Encoding\"."""

    serviceProviderAdminTable: OCITable


@dataclass
class ServiceProviderAdminGetPolicyResponse20(OCIDataResponse):
    """Response to ServiceProviderAdminGetPolicyRequest20.
    Contains the policy settings for the service provider administrator.
    The networkPolicyAccess and numberActivationAccess are returned only for the enterprise administrator.
    The following elements are only used in AS data mode:
        dialableCallerIDAccess
        verifyTranslationAndRoutingAccess"""

    profileAccess: str

    groupAccess: str

    userAccess: str

    adminAccess: str

    departmentAccess: str

    accessDeviceAccess: str

    phoneNumberExtensionAccess: str

    callingLineIdNumberAccess: str

    serviceAccess: str

    servicePackAccess: str

    sessionAdmissionControlAccess: str

    webBrandingAccess: str

    officeZoneAccess: str

    communicationBarringAccess: str

    dialableCallerIDAccess: str

    verifyTranslationAndRoutingAccess: str

    networkPolicyAccess: Optional[str] = None

    numberActivationAccess: Optional[str] = None


@dataclass
class ServiceProviderAdminGetResponse22V3(OCIDataResponse):
    """Response to the ServiceProviderAdminGetRequest22V3.
    The response contains the service provider administrators profile information.

    The following elements are only used in AS data mode and ignored in XS data mode.
    accountDisabled
    lastAuthenticatedDate
    hasPassword"""

    serviceProviderId: str

    language: str

    administratorType: str

    locale: str

    encoding: str

    accountDisabled: bool

    lastAuthenticatedDate: str

    hasPassword: bool

    firstName: Optional[str] = None

    lastName: Optional[str] = None


@dataclass
class ServiceProviderAdministratorPasswordRulesGetResponseRI(OCIDataResponse):
    """Response to ServiceProviderAdministratorPasswordRulesGetRequestRI."""

    useExternalAuthentication: bool

    allowWebAddExternalAuthenticationUsers: bool

    disallowUserId: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    maxFailedLoginAttempts: int

    passwordExpiresDays: int

    sendLoginDisabledNotifyEmail: bool

    disallowPreviousPasswords: bool

    numberOfPreviousPasswords: int

    usePasswordValidationService: bool

    reenableLogin: bool

    lockOutInMinutes: int

    loginDisabledNotifyEmailAddress: Optional[str] = None


@dataclass
class ServiceProviderAdviceOfChargeGetResponse(OCIDataResponse):
    """Response to ServiceProviderAdviceOfChargeGetRequest.
    Contains a list of Advice of Charge service provider parameters."""

    useSPLevelAoCSettings: bool

    delayBetweenNotificationSeconds: int


@dataclass
class ServiceProviderAlternateUserIdGetListResponse(OCIDataResponse):
    """Response to ServiceProviderAlternateUserIdGetListRequest.
    The \"User Type\" column contains the corresponding enumerated UserType value.
    Contains a table of alternate user ids, the column headings are:
      \"User Id\", \"Alternate User Id\", \"Group Id\" and \"User Type\"."""

    alternateUserIdTable: OCITable


@dataclass
class ServiceProviderAnswerConfirmationGetResponse16(OCIDataResponse):
    """Response to the ServiceProviderAnswerConfirmationGetRequest16."""

    announcementMessageSelection: str

    confirmationTimoutSeconds: int

    confirmationMessageAudioFileDescription: Optional[str] = None

    confirmationMessageMediaType: Optional[str] = None


@dataclass
class ServiceProviderApplicationServerSetGetResponse(OCIDataResponse):
    """Response to the ServiceProviderApplicationServerSetGetRequest.
    The response contains the service provider or enterprise's Application Server set information."""

    applicationServerSetName: Optional[str] = None


@dataclass
class ServiceProviderBroadWorksCommunicatorGetResponse(OCIDataResponse):
    """Response to ServiceProviderBroadWorksCommunicatorGetRequest."""

    configurationServerURL: Optional[str] = None


@dataclass
class ServiceProviderBroadWorksMobilityGetResponse22V3(OCIDataResponse):
    """The response to a ServiceProviderBroadWorksMobilityGetRequest22V3."""

    useSettingLevel: str

    enableLocationServices: bool

    enableMSRNLookup: bool

    enableMobileStateChecking: bool

    denyCallOriginations: bool

    denyCallTerminations: bool

    enableAnnouncementSuppression: bool

    enableInternalCLIDDelivery: bool

    enableInternalCLIDDeliveryAccessLocations: bool

    enableEnhancedUnreachableStateChecking: bool

    enableNetworkCallBarringStatusCheck: bool

    networkTranslationIndex: Optional[str] = None


@dataclass
class ServiceProviderBroadWorksMobilityMobileSubscriberDirectoryNumberGetAvailableListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderBroadWorksMobilityMobileSubscriberDirectoryNumberGetAvailableListRequest.
    Contains a list of available Mobile Subscriber Directory Numbers not yet assigned to any group."""

    availableMobileSubscriberDirectoryNumber: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderBroadWorksMobilityMobileSubscriberDirectoryNumberGetSummaryListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderBroadWorksMobilityMobileSubscriberDirectoryNumberGetSummaryListRequest.
    The column headings are \"Phone Number\", \"Group Id\" and \"Mobile Network\"."""

    mobileSubscriberDirectoryNumbersSummaryTable: OCITable


@dataclass
class ServiceProviderCallProcessingGetPolicyResponse22V3(OCIDataResponse):
    """Response to ServiceProviderCallProcessingGetPolicyRequest22V3.
     The following elements are not returned for a service provider:
       enableGatewayRoutePolicy
       networkCallsGatewayRouteIdentity
       networkURLCallsGatewayRouteIdentity
       emergencyCallsGatewayRouteIdentity
       repairCallsGatewayRouteIdentity
       callTypingErrorsGatewayRouteIdentity
     The following elements are only used in AS data mode:
       useServiceProviderDCLIDSetting
       enableDialableCallerID
       allowConfigurableCLIDForRedirectingIdentity
       enterpriseCallsCLIDPolicy, value \"Use Location Code plus Extension\" is returned in XS data mode.
       groupCallsCLIDPolicy, value \"Use Extension\" is returned in XS data mode.
       enablePhoneListLookup, value \"false\" is returned in XS data mode.
       useMaxConcurrentTerminatingAlertingRequests, value \"false\" is returned in XS data mode.
       maxConcurrentTerminatingAlertingRequests, value \"10\" is returned in XS data mode.
       includeRedirectionsInMaximumNumberOfConcurrentCalls, value \"false\" is returned in XS data mode.
       useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable, value \"false\" is returned in XS data mode.
       useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable, value \"false\" is returned in XS data mode.
       allowMobileDNForRedirectingIdentity, value \"false\" is returned in XS data mode.
     The following elements are only used in AS data mode and not returned in XS data mode:
       enableGatewayRoutePolicy
       networkCallsGatewayRouteIdentity
       networkURLCallsGatewayRouteIdentity
       emergencyCallsGatewayRouteIdentity
       repairCallsGatewayRouteIdentity
       callTypingErrorsGatewayRouteIdentity

    The following elements are only used in XS data mode and not returned in AS data mode:
       routeOverrideDomain
       routeOverridePrefix"""

    useServiceProviderDCLIDSetting: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    mediaPolicySelection: str

    networkUsageSelection: str

    enforceGroupCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    enableEnterpriseExtensionDialing: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    useSettingLevel: str

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    blockCallingNameForExternalCalls: bool

    enableDialableCallerID: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    enterpriseCallsCLIDPolicy: str

    groupCallsCLIDPolicy: str

    enablePhoneListLookup: bool

    useMaxConcurrentTerminatingAlertingRequests: bool

    maxConcurrentTerminatingAlertingRequests: int

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    allowMobileDNForRedirectingIdentity: bool

    supportedMediaSetName: Optional[str] = None

    conferenceURI: Optional[str] = None

    routeOverrideDomain: Optional[str] = None

    routeOverridePrefix: Optional[str] = None

    enableGatewayRoutePolicy: Optional[bool] = None

    networkCallsGatewayRouteIdentity: Optional[str] = None

    networkURLCallsGatewayRouteIdentity: Optional[str] = None

    emergencyCallsGatewayRouteIdentity: Optional[str] = None

    repairCallsGatewayRouteIdentity: Optional[str] = None

    callTypingErrorsGatewayRouteIdentity: Optional[str] = None


@dataclass
class ServiceProviderCommunicationBarringCriteriaGetAssignedListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderCommunicationBarringCriteriaGetAssignedListRequest.
    Contains a table of all Communication Barring Criteria assigned to the
    service provider. The column headings are: \"Name\" and \"Description\"."""

    criteriaTable: OCITable


@dataclass
class ServiceProviderCommunicationBarringDigitPatternCriteriaGetListResponse(
    OCIDataResponse
):
    """Response to the ServiceProviderCommunicationBarringDigitPatternCriteriaGetListRequest.
    The response contains a table of all Digit Pattern Criteria defined for the service provider. The column headings are \"Name\" and \"Description\" """

    criteriaTable: OCITable


@dataclass
class ServiceProviderCommunicationBarringDigitPatternCriteriaGetPatternListResponse(
    OCIDataResponse
):
    """Response to the ServiceProviderCommunicationBarringDigitPatternCriteriaGetPatternListRequest.
    The response contains the Digit Pattern Criteria information."""

    matchDigitPattern: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderCommunicationBarringDigitPatternCriteriaGetResponse(
    OCIDataResponse
):
    """Response to the ServiceProviderCommunicationBarringDigitPatternCriteriaGetRequest.
    The response contains the Digit Pattern Criteria information."""

    description: Optional[str] = None


@dataclass
class ServiceProviderCommunicationBarringIncomingCriteriaGetAssignedListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderCommunicationBarringIncomingCriteriaGetAssignedListRequest.
    Contains a table of all Communication Barring Incoming Criteria assigned to the
    service provider. The column headings are: \"Name\" and \"Description\"."""

    criteriaTable: OCITable


@dataclass
class ServiceProviderCommunicationBarringProfileGetAssignedGroupListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderCommunicationBarringProfileGetAssignedGroupListRequest.
    Contains a table of groups that have the Communication Barring Profile
    assigned. The column headings are: \"Group Id\" and \"Group Name\"."""

    groupTable: OCITable


@dataclass
class ServiceProviderCommunicationBarringProfileGetCriteriaUsageListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderCommunicationBarring ProfileGetCriteriaUsageListRequest.  Contains a table of profiles that have the Communication Barring Criteria assigned. The column headings are: \"Name\" and \"Description\"."""

    profileTable: OCITable


@dataclass
class ServiceProviderCommunicationBarringProfileGetDigitPatternCriteriaUsageListResponse(
    OCIDataResponse
):
    """Response to the ServiceProviderCommunicationBarringProfileGetDigitPatternCriteriaUsageListRequest.
    The response contains a table of all Profiles that use the specific Digit Pattern Criteria. The column headings are \"Name\" and \"Description\" """

    profileTable: OCITable


@dataclass
class ServiceProviderCommunicationBarringProfileGetIncomingCriteriaUsageListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderCommunicationBarringProfileGetIncomingCriteriaUsageListRequest.
    Contains a table of profiles that have the Communication Barring Incoming Criteria assigned.
    The column headings are: \"Name\" and \"Description\"."""

    profileTable: OCITable


@dataclass
class ServiceProviderCommunicationBarringProfileGetListResponse(OCIDataResponse):
    """Response to the ServiceProviderCommunicationBarringProfileGetListRequest.
    The response contains a table of all Communication Barring Profiles
    for the service provider. The column headings are \"Default\" , \"Name\" and \"Description\" """

    profileTable: OCITable


@dataclass
class ServiceProviderCommunicationBarringProfileGetResponse19sp1V2(OCIDataResponse):
    """Response to the ServiceProviderCommunicationBarringProfileGetRequest19sp1V2.
      The response contains the Communication Barring Profile information.
      The incoming, originating, redirecting and call me now rules are returned in ascending priority order.
    The following elements are only used in AS data mode:
         callMeNowDefaultAction
         callMeNowDefaultCallTimeout
         callMeNowRule
         applyToAttendedCallTransfers"""

    originatingDefaultAction: str

    redirectingDefaultAction: str

    callMeNowDefaultAction: str

    incomingDefaultAction: str

    isDefault: bool

    applyToAttendedCallTransfers: bool

    description: Optional[str] = None

    originatingDefaultTreatmentId: Optional[str] = None

    originatingDefaultTransferNumber: Optional[str] = None

    originatingDefaultCallTimeout: Optional[int] = None

    originatingRule: List[
        ServiceProviderCommunicationBarringHierarchicalOriginatingRule
    ] = field(default_factory=list)

    redirectingDefaultCallTimeout: Optional[int] = None

    redirectingRule: List[
        ServiceProviderCommunicationBarringHierarchicalRedirectingRule
    ] = field(default_factory=list)

    callMeNowDefaultCallTimeout: Optional[int] = None

    callMeNowRule: List[
        ServiceProviderCommunicationBarringHierarchicalCallMeNowRule
    ] = field(default_factory=list)

    incomingDefaultCallTimeout: Optional[int] = None

    incomingRule: List[CommunicationBarringIncomingRule19sp1] = field(
        default_factory=list
    )


@dataclass
class ServiceProviderDeviceActivationPolicyGetResponse(OCIDataResponse):
    """Response to ServiceProviderDeviceActivationPolicyGetRequest."""

    useServiceProviderSettings: bool

    allowActivationCodeRequestByUser: bool

    sendActivationCodeInEmail: bool


@dataclass
class ServiceProviderDeviceManagementEventGetListResponse22(OCIDataResponse):
    """Response to ServiceProviderDeviceManagementEventGetListRequest22.
    Contains a table with column headings: \"Event Id\", \"Status\", \"Action\",
    \"Level\", \"Type\", \"Additional Info\", \"Is Local\", \"Completion %\",
    \"Pushed/ Same Hash/ Not Pushed\", \"Login Id\", \"Start Time\",
    \"Process Time\", \"Rx Time\", \"Total Time\", \"Request\", \"Priority\",
    \"Tracking Id\", \"End Time\".
    \"Event Id\" is a unique identifier for the event.
    \"Status\" can be: Pending, Queued, In Progress,
    Process On Other Host, Stale, Completed, Canceled.
    \"Action\" can be: Delete, Download, Rebuild, Reset, Upload.
    \"Level\" can be: Device, Device Type, Device Type Group, Group, User.
    \"Type\" can be: Automatic, Manual.
    \"Additional Info\" includes the affected device type, device or group.
    It depends on the level of the event:
      Device Profile: \"Device Name\" \"Service Provider Id\" \"Group Id\"
      Device Type: \"Device Type Name\"
      Device Type Service Provider: \"Service Provider Id\" \"Device Type Name\"
      Service Provider: \"Service Provider Id\"
      Device Type Group: \"Service Provider Id\" \"Group Id\" \"Device Type Name\"
      Group: \"Service Provider Id\" \"Group Id\"
      User: \"User Id\"
    \"Is Local\" is set to \"yes\" if the event is processed on the server
    who received the request, \"no\" otherwise meaning that the event is
    processed on another server.
    \"Completion %\" provides an estimate of the completion of the event.
    A percentage is given, the current number of completed expanded event,
    and the total number of expanded event.
    \"Pushed/ Same Hash/ Not Pushed\" gives the total number of files that
    were pushed, not pushed because of same hash, and not pushed when
    processing the event.
    \"LoginId\" is the user or admin id who triggered the event.
    \"Start Time\" is the date when the event's processing started.  The
    display shows the month, day, hours, minutes, and seconds (MM-dd hh:mm:ss).
    \"Process Time\" is the time taken to process the event in hours,
    minutes, seconds, and milliseconds (hhhh:mm:ss.SSS).
    \"Rx Time\" is the date when the event was received via OCI-P and
    stored in the system.  The display shows the month, day, hours,
    minutes, and seconds (MM-dd hh:mm:ss).
    \"Total Time\" is the total time the event was in the system, from the
    moment it was received and stored until its processing ended, in
    hours, minutes, seconds, and milliseconds (hhhh:mm:ss.SSS).
    \"Request\" is the name of the OCI-P request that triggered the event.
    \"Priority\" is the priority of the event.
    \"Tracking Id\" is the tracking id of the OCI-P request that triggered the event.
    \"End Time\" is the difference, measured in milliseconds, between the
    event's end time and midnight, January 1, 1970 UTC"""

    eventTable: OCITable


@dataclass
class ServiceProviderDeviceManagementGetAccessDeviceCountForDeviceTypeServiceProviderResponse(
    OCIDataResponse
):
    """Response to ServiceProviderDeviceManagementGetAccessDeviceCountForDeviceTypeServiceProviderRequest."""

    accessDeviceCount: int


@dataclass
class ServiceProviderDeviceProfileAuthenticationPasswordRulesGetResponseRI(
    OCIDataResponse
):
    """Response to ServiceProviderDeviceProfileAuthenticationPasswordRulesGetRequestRI.
    Contains the device profile authentication password rules for the service provider."""

    useServiceProviderSettings: bool

    disallowAuthenticationName: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    sendPermanentLockoutNotification: bool

    deviceProfileAuthenticationLockoutType: str

    deviceProfileTemporaryLockoutThreshold: int

    deviceProfileWaitAlgorithm: str

    deviceProfileLockoutFixedMinutes: str

    deviceProfilePermanentLockoutThreshold: int

    usePasswordValidationService: bool

    permanentLockoutNotifyEmailAddress: Optional[str] = None


@dataclass
class ServiceProviderDeviceTypeCustomTagGetListResponse(OCIDataResponse):
    """Response to ServiceProviderDeviceTypeCustomTagGetListRequest.
    Contains a table of custom configuration tags managed by the Device Management System on a per-device type basis for a service provider.
    In As data mode, the column headings are:
      \"Tag Name\", \"Tag Value\".
    In XS data mode, the column headings are:
      \"Tag Name\", \"Tag Value\" if request is invoked by an admin without system privileges.
      \"Tag Name\", \"Tag Value\", \"Is Encrypted\" if request is invoked by an admin with system privileges."""

    serviceProviderDeviceTypeCustomTagsTable: OCITable


@dataclass
class ServiceProviderDeviceTypeFileGetListResponse(OCIDataResponse):
    """Response to ServiceProviderDeviceTypeFileGetListRequest.
    Contains a table of device type files managed by the Device Management System, on a per-service provider basis.
    The column headings are: \"File Format\", \"Is Authenticated\", \"Access URL\", \"Repository URL\", \"Template URL\"."""

    serviceProviderDeviceTypeFilesTable: OCITable

    serviceProviderHasCustomizableDynamicFiles: bool


@dataclass
class ServiceProviderDeviceTypeFileGetResponse(OCIDataResponse):
    """Response to ServiceProviderDeviceTypeFileGetRequest."""

    accessUrl: str

    fileSource: Optional[str] = None

    configurationFileName: Optional[str] = None

    repositoryUrl: Optional[str] = None

    templateUrl: Optional[str] = None


@dataclass
class ServiceProviderDeviceTypeTagSetGetResponse(OCIDataResponse):
    """Response to ServiceProviderDeviceTypeGetRequest."""

    tagSetName: Optional[str] = None


@dataclass
class ServiceProviderDialPlanPolicyGetAccessCodeListResponse(OCIDataResponse):
    """Response to ServiceProviderDialPlanPolicyGetAccessCodeListRequest.
    Contains a table with column headings: \"Access Code\",
    \"Enable Secondary Dial Tone\", \"Description\"."""

    accessCodeTable: OCITable


@dataclass
class ServiceProviderDialPlanPolicyGetAccessCodeResponse(OCIDataResponse):
    """Response to ServiceProviderDialPlanPolicyGetAccessCodeRequest"""

    includeCodeForNetworkTranslationsAndRouting: bool

    includeCodeForScreeningServices: bool

    enableSecondaryDialTone: bool

    description: Optional[str] = None


@dataclass
class ServiceProviderDialPlanPolicyGetResponse22(OCIDataResponse):
    """Response to ServiceProviderDialPlanPolicyGetRequest22
    The following elements are only used in AS data mode:
      overrideResolvedDeviceDigitMap
    The following elements are only used in AS data mode and not returned in XS data mode:
      deviceDigitMap"""

    requiresAccessCodeForPublicCalls: bool

    allowE164PublicCalls: bool

    preferE164NumberFormatForCallbackServices: bool

    overrideResolvedDeviceDigitMap: bool

    publicDigitMap: Optional[str] = None

    privateDigitMap: Optional[str] = None

    deviceDigitMap: Optional[str] = None


@dataclass
class ServiceProviderDialableCallerIDCriteriaGetResponse(OCIDataResponse):
    """Response to the ServiceProviderDialableCallerIDCriteriaGetRequest.
    The response contains the Dialable Caller ID Criteria information."""

    matchLocalCategory: bool

    matchNationalCategory: bool

    matchInterlataCategory: bool

    matchIntralataCategory: bool

    matchInternationalCategory: bool

    matchPrivateCategory: bool

    matchEmergencyCategory: bool

    matchOtherCategory: bool

    description: Optional[str] = None

    prefixDigits: Optional[str] = None

    matchCallType: List[str] = field(default_factory=list)

    matchAlternateCallIndicator: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderDialableCallerIDGetResponse(OCIDataResponse):
    """Response to the ServiceProviderDialableCallerIDGetRequest.
    The criteria table?s column headings are ?Active?, \"Name\", \"Description\", ?Prefix Digits?, and ?Priority?."""

    useServiceProviderCriteria: bool

    nsScreeningFailurePolicy: str

    criteriaTable: OCITable


@dataclass
class ServiceProviderDigitCollectionGetResponse13mp4(OCIDataResponse):
    """Response to ServiceProviderDigitCollectionGetRequest13mp4."""

    accessCode: Optional[str] = None

    publicDigitMap: Optional[str] = None

    privateDigitMap: Optional[str] = None


@dataclass
class ServiceProviderDnGetAvailableListResponse(OCIDataResponse):
    """Response to ServiceProviderDnGetAvailableListRequest.
    Contains a list of available DNs not yet assigned to any group."""

    availableDn: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderDnGetStatusListResponse(OCIDataResponse):
    """Response to ServiceProviderDnGetStatusListRequest."""

    dnStatus: List[DNValidationStatusMessage] = field(default_factory=list)


@dataclass
class ServiceProviderDnGetSummaryListResponse(OCIDataResponse):
    """Response to ServiceProviderDnGetSummaryListRequest.
    The column headings are \"Phone Numbers, \"Group Id\" and \"Can Delete\" """

    dnSummaryTable: OCITable


@dataclass
class ServiceProviderDomainGetAssignedGroupListResponse(OCIDataResponse):
    """Response to ServiceProviderDomainGetAssignedGroupListRequest.
    Contains a table with column headings: \"Group Id\", \"Group Name\"
    and a row for each group."""

    groupTable: OCITable


@dataclass
class ServiceProviderDomainGetAssignedListResponse22(OCIDataResponse):
    """Contains a simple list of service provider domain names."""

    serviceProviderDefaultDomain: str

    domain: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderEmergencyCallNotificationGetResponse(OCIDataResponse):
    """Response to ServiceProviderEmergencyCallNotificationGetRequest."""

    sendEmergencyCallNotificationEmail: bool

    allowGroupOverride: bool

    emergencyCallNotifyEmailAddress: Optional[str] = None


@dataclass
class ServiceProviderEndpointGetListResponse(OCIDataResponse):
    """Response to ServiceProviderEndpointGetListRequest.
    The column headings for the endpointTable are:
      \"Group Id\", \"Line/Port\", \"Last Name\", \"First Name\",  \"User Id\", \"User Type\", \"Phone Number\", \"Extension\", \"Device Type\", \"Device Name\", \"Net Address\", \"MAC Address\", \"Department\", \"Email Address\".
            Possible values for User Type are \"User\", \"CCBasic\", \"CCStandard\", \"CCPremium\", \"RP\", \"MOH\", \"MOHVideo\"."""

    endpointTable: OCITable


@dataclass
class ServiceProviderEnhancedCallLogsGetResponse17sp4(OCIDataResponse):
    """Response to ServiceProviderEnhancedCallLogsGetRequest17sp4."""

    maxLoggedCalls: int

    callExpirationDays: int


@dataclass
class ServiceProviderEnhancedCallLogsSchemaInstanceGetResponse(OCIDataResponse):
    """Response to ServiceProviderEnhancedCallLogsSchemaInstanceGetRequest."""

    name: Optional[str] = None


@dataclass
class ServiceProviderExtensionLengthGetResponse(OCIDataResponse):
    """Response to ServiceProviderExtensionLengthGetRequest."""

    defaultExtensionLength: Optional[int] = None

    locationRoutingPrefixDigit: Optional[int] = None

    locationCodeLength: Optional[int] = None


@dataclass
class ServiceProviderExternalCustomRingbackGetResponse(OCIDataResponse):
    """Response to ServiceProviderExternalCustomRingbackGetRequest."""

    timeoutSeconds: int

    prefixDigits: Optional[str] = None

    serverNetAddress: Optional[str] = None

    serverPort: Optional[int] = None


@dataclass
class ServiceProviderFeatureAccessCodeGetListResponse21(OCIDataResponse):
    """Response to the ServiceProviderFeatureAccessCodeGetListRequest21.

    In release 20 the \"Call Recording\" FAC name is changed to
    \"Call Recording - Start\"."""

    featureAccessCode: List[FeatureAccessCodeReadEntry] = field(default_factory=list)


@dataclass
class ServiceProviderFileRepositoryDeviceUserGetListResponse(OCIDataResponse):
    """Response to ServiceProviderFileRepositoryDeviceUserGetListRequest.
    Contains a table with column headings : \"User Name\",\"Allow Delete\",\"Allow Get\",\"Allow Put\" in a row for each file repository service provider user."""

    fileRepositoryUserTable: OCITable


@dataclass
class ServiceProviderGetAvailableLeafDeviceListResponse22(OCIDataResponse):
    """Response to ServiceProviderGetAvailableLeafDeviceListRequest22."""

    leafDeviceKey: List[AccessDeviceKey] = field(default_factory=list)

    supportLinks: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderGetAvailableTreeDeviceListResponse(OCIDataResponse):
    """Response to ServiceProviderGetAvailableTreeDeviceListRequest."""

    treeDeviceInfo: List[TreeDeviceInfo] = field(default_factory=list)


@dataclass
class ServiceProviderGetDefaultResponse(OCIDataResponse):
    """Response to the ServiceProviderGetDefaultRequest. All values are default values for
    a service provider or enterprise's profile."""

    isEnterprise: bool

    defaultDomain: Optional[str] = None


@dataclass
class ServiceProviderGetListResponse(OCIDataResponse):
    """Response to ServiceProviderGetListRequest.
    Contains a 3 column table with column headings \"Service Provider Id\", \"Service Provider Name\",
    \"Is Enterprise\" and \"Reseller Id\" and a row for each service provider or enterprise.

    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    serviceProviderTable: OCITable


@dataclass
class ServiceProviderGetPagedSortedListResponse(OCIDataResponse):
    """Response to ServiceProviderGetPagedSortedListRequest.
    Contains a table with column headings \"Service Provider Id\", \"Service Provider Name\"
    and \"Is Enterprise\", \"Reseller Id\" and \"Service Provider External Id\" and a row for each service provider or enterprise.

    The following columns are only populated in AS data mode:
      \"Reseller Id\",
      \"Service Provider External Id"""

    serviceProviderTable: OCITable


@dataclass
class ServiceProviderGetResponse22V4(OCIDataResponse):
    """Response to the ServiceProviderGetRequest22V4.
    The response contains the service provider or enterprise's profile information.
    The following elements are not returned in AS and XS data mode:
    servicePolicy,
    callProcessingSliceId,
    subscriberPartition.

    The following data elements are only used in AS data mode and not returned
    in XS data mode:
    resellerId,
    serviceProviderExternalId,
    provisioningSliceId."""

    isEnterprise: bool

    useCustomRoutingProfile: bool

    defaultDomain: str

    useServiceProviderLanguages: bool

    serviceProviderId: str

    serviceProviderName: Optional[str] = None

    supportEmail: Optional[str] = None

    contact: Optional[Contact] = None

    address: Optional[StreetAddress] = None

    servicePolicy: Optional[str] = None

    callProcessingSliceId: Optional[str] = None

    provisioningSliceId: Optional[str] = None

    subscriberPartition: Optional[str] = None

    preferredDataCenter: Optional[str] = None

    resellerId: Optional[str] = None

    serviceProviderExternalId: Optional[str] = None


@dataclass
class ServiceProviderGroupPagingTargetsCapacityGetResponse22(OCIDataResponse):
    """Response to ServiceProviderGroupPagingTargetsCapacityGetRequest22."""

    maximumTargetUsers: int


@dataclass
class ServiceProviderHPBXAlternateCarrierSelectionGetResponse(OCIDataResponse):
    """Response to the ServiceProviderHPBXAlternateCarrierSelectionGetRequest."""

    processCbcCarrierSelection: bool

    preselectedLocalCarrier: Optional[str] = None

    preselectedDistantCarrier: Optional[str] = None


@dataclass
class ServiceProviderIMRNGetListResponse(OCIDataResponse):
    """Response to ServiceProviderIMRNGetListRequest."""

    imrn: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderInCallServiceActivationGetResponse17(OCIDataResponse):
    """Response to ServiceProviderInCallServiceActivationGetRequest17."""

    flashActivationDigits: str

    callTransferActivationDigits: str


@dataclass
class ServiceProviderIntegratedIMPGetResponse22(OCIDataResponse):
    """Response to the ServiceProviderIntegratedIMPGetRequest22.
    The response contains the service provider Integrated IMP service attributes.
    If the service provider is within a reseller, useSystemServiceDomain means using reseller level service
    domain setting. And useSystemMessagingServer means using the reseller level messaging server setting.
    The element useResellerIMPIdSetting means using the reseller level IMP User ID setting."""

    useSystemServiceDomain: bool

    useSystemMessagingServer: bool

    defaultImpIdType: str

    useResellerIMPIdSetting: bool

    serviceDomain: Optional[str] = None

    servicePort: Optional[int] = None

    provisioningUrl: Optional[str] = None

    provisioningUserId: Optional[str] = None

    boshURL: Optional[str] = None


@dataclass
class ServiceProviderLanguageGetAvailableListResponse(OCIDataResponse):
    """Response to ServiceProviderLanguageGetAvailableListRequest.
    The language table column headings are: \"Language\", \"Locale\" and \"Encoding\"."""

    defaultLanguage: str

    languageTable: OCITable


@dataclass
class ServiceProviderLanguageGetListResponse(OCIDataResponse):
    """Response to ServiceProviderLanguageGetListRequest."""

    language: List[str] = field(default_factory=list)

    defaultLanguage: Optional[str] = None


@dataclass
class ServiceProviderMWIDeliveryToMobileEndpointCustomTemplateGetResponse23(
    OCIDataResponse
):
    """Response to the ServiceProviderMWIDeliveryToMobileEndpointCustomTemplateGetRequest23."""

    isEnabled: bool

    templateBody: MWIDeliveryToMobileEndpointTemplateBody23

    monthAbbreviations: Optional[str] = None


@dataclass
class ServiceProviderMWIDeliveryToMobileEndpointGetResponse(OCIDataResponse):
    """Response to ServiceProviderMWIDeliveryToMobileEndpointGetRequest.

    The templateActivationTable contains the list of templates defined for the service provider.
    The column headings are \"Enable\", \"Language\", \"Type\"."""

    templateActivationTable: OCITable


@dataclass
class ServiceProviderMaliciousCallTraceGetResponse(OCIDataResponse):
    """Response to the ServiceProviderMaliciousCallTraceGetRequest.
    The response contains the service provider Malicious Call Trace
    settings."""

    useSystemPlayMCTWarningAnnouncement: bool

    playMCTWarningAnnouncement: bool


@dataclass
class ServiceProviderMeetMeConferencingGetResponse(OCIDataResponse):
    """Response to ServiceProviderMeetMeConferencingGetRequest."""

    allocatedPorts: MeetMeConferencingConferencePorts


@dataclass
class ServiceProviderNetworkClassOfServiceGetAssignedGroupListResponse(OCIDataResponse):
    """Response to ServiceProviderNetworkClassOfServiceGetAssignedGroupListRequest.
    Contains a table of groups that have the Network Class of Service
    assigned. The column headings are: \"Group Id\" and \"Group Name\"."""

    groupTable: OCITable


@dataclass
class ServiceProviderNetworkClassOfServiceGetAssignedListResponse(OCIDataResponse):
    """Response to ServiceProviderNetworkClassOfServiceGetAssignedListRequest.
    Contains a table of all Network Classes of Service assigned to the
    service provider. The column headings are: \"Name\", \"Description\" and \"Default\"."""

    networkClassOfServiceTable: OCITable


@dataclass
class ServiceProviderNumberPortabilityQueryGetResponse(OCIDataResponse):
    """Response to the ServiceProviderNumberPortabilityQueryGetRequest.
    The response contains the service provider number portability query information."""

    enableNumberPortabilityQueryForOutgoingCalls: bool

    enableNumberPortabilityQueryForIncomingCalls: bool

    enableNumberPortabilityQueryForNetworkCallsOnly: bool

    digitPattern: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderOfficeZoneGetAssignedGroupListResponse(OCIDataResponse):
    """Response to ServiceProviderOfficeZoneGetAssignedGroupListRequest.  Contains a table of groups that have the Office Zone assigned. The column headings are: \"Group Id\" and \"Group Name\"."""

    groupTable: OCITable


@dataclass
class ServiceProviderOfficeZoneGetAssignedListResponse(OCIDataResponse):
    """Response to ServiceProviderOfficeZoneGetAssignedListRequest.
    Contains a table of all Office Zones assigned to the
    service provider. The column headings are: \"Name\", \"Description\" and \"Default\"."""

    officeZoneTable: OCITable


@dataclass
class ServiceProviderPasswordRulesGetResponseRI(OCIDataResponse):
    """Response to ServiceProviderPasswordRulesGetRequestRI.
    Contains the group, department administrator and/or user password
    rules setting.

    The following element is only used in AS data mode:
    forcePasswordChangeAfterReset, value \"false\" is returned in XS data mode
    reenableLogin
    lockOutInMinutes"""

    rulesApplyTo: str

    allowWebAddExternalAuthenticationUsers: bool

    disallowUserId: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    maxFailedLoginAttempts: int

    passwordExpiresDays: int

    sendLoginDisabledNotifyEmail: bool

    disallowRulesModification: bool

    disallowPreviousPasswords: bool

    numberOfPreviousPasswords: int

    forcePasswordChangeAfterReset: bool

    usePasswordValidationService: bool

    reenableLogin: bool

    lockOutInMinutes: int

    loginDisabledNotifyEmailAddress: Optional[str] = None


@dataclass
class ServiceProviderPortalPasscodeRulesGetResponseRI(OCIDataResponse):
    """Response to ServiceProviderPortalPasscodeRulesGetRequestRI.
    Contains the service provider's passcode rules setting.

    The following elements are only used in AS data mode:
      numberOfRepeatedDigits
      disallowRepeatedPatterns
      disallowContiguousSequences
      numberOfAscendingDigits
      numberOfDescendingDigits
      numberOfPreviousPasscodes
      enableDefaultPasscode
      defaultPasscode
      reenableLogin
      lockOutInMinutes"""

    disallowRepeatedDigits: bool

    numberOfRepeatedDigits: int

    disallowRepeatedPatterns: bool

    disallowContiguousSequences: bool

    numberOfAscendingDigits: int

    numberOfDescendingDigits: int

    disallowUserNumber: bool

    disallowReversedUserNumber: bool

    disallowOldPasscode: bool

    numberOfPreviousPasscodes: int

    disallowReversedOldPasscode: bool

    minCodeLength: int

    maxCodeLength: int

    disableLoginAfterMaxFailedLoginAttempts: bool

    expirePassword: bool

    sendLoginDisabledNotifyEmail: bool

    enableDefaultPasscode: bool

    reenableLogin: bool

    lockOutInMinutes: int

    maxFailedLoginAttempts: Optional[int] = None

    passcodeExpiresDays: Optional[int] = None

    loginDisabledNotifyEmailAddress: Optional[str] = None

    defaultPasscode: Optional[str] = None


@dataclass
class ServiceProviderPreferredCarrierGetAvailableCountryCodeListResponse(
    OCIDataResponse
):
    """Response to a ServiceProviderPreferredCarrierGetAvailableCountryCodeListRequest.
    Contains the default country code and the list of unused country codes for a service provider / enterprise."""

    defaultCountryCode: Optional[str] = None

    countryCode: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderPreferredCarrierGetCarrierListResponse(OCIDataResponse):
    """Response to a ServiceProviderPreferredCarrierGetCarrierListRequest.
    Contains the lists of carriers for a specified country code for a service provider / enterprise."""

    intraLataCarrier: List[str] = field(default_factory=list)

    interLataCarrier: List[str] = field(default_factory=list)

    internationalCarrier: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderPreferredCarrierGetListResponse(OCIDataResponse):
    """Response to a ServiceProviderPreferredCarrierGetListRequest. Contains a table with one row per carrier.
    The table columns are: \"Country Code\", \"Intra-Lata PIC\", \"Inter-Lata PIC\", \"International PIC\"."""

    serviceProviderCarrierTable: OCITable


@dataclass
class ServiceProviderPreferredCarrierGetResponse(OCIDataResponse):
    """Response to a ServiceProviderPreferredCarrierGetRequest.
    Contains the currently configured carriers for a specified country code for a service provider / enterprise."""

    intraLataCarrier: Optional[str] = None

    interLataCarrier: Optional[str] = None

    internationalCarrier: Optional[str] = None


@dataclass
class ServiceProviderRouteListEnterpriseTrunkNumberPrefixGetAvailableListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderRouteListEnterpriseTrunkNumberPrefixGetAvailableListRequest.
    Contains a list of available number prefixes not yet assigned to any group.
    The column headings are \"Number Prefix\"\",\"Is Active\", \"Extension Range Start\" and \"Extension Range End\"."""

    availableNumberPrefixTable: OCITable


@dataclass
class ServiceProviderRouteListEnterpriseTrunkNumberPrefixGetSummaryListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderRouteListEnterpriseTrunkPrefixGetSummaryListRequest.
    The column headings are \"Number Prefix\", \"Group Id\" \",\"Is Active\", \"Extension Range Start\" and \"Extension Range End\"."""

    prefixSummaryTable: OCITable


@dataclass
class ServiceProviderRouteListEnterpriseTrunkNumberRangeGetAvailableListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderRouteListEnterpriseTrunkNumberRangeGetAvailableListRequest. Contains a list of available number ranges not yet assigned to any group.
    The column headings are \"Number Range Start\", \"Number Range End\",\"Is Active\" and \"Extension Length\"."""

    availableNumberRangeTable: OCITable


@dataclass
class ServiceProviderRouteListEnterpriseTrunkNumberRangeGetSummaryListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderRouteListEnterpriseTrunkNumberRangeGetSummaryListRequest.
    The column headings are \"Number Range Start\", \"Number Range End\", \"Group Id\", \"Is Active\" and \"Extension Length\"."""

    numberRangeSummaryTable: OCITable


@dataclass
class ServiceProviderRoutePointExternalSystemGetAssignedGroupListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderRoutePointExternalSystemGetAssignedGroupListRequest.
    Contains a table with column headings: \"Group Id\", \"Group Name\"
    and a row for each group."""

    groupTable: OCITable


@dataclass
class ServiceProviderRoutePointExternalSystemGetAssignedListResponse(OCIDataResponse):
    """Response to the ServiceProviderRoutePointExternalSystemGetAssignedListRequest.
    Contains a table of all Route Point External Systems assigned to the
    service provider.  The column headings are: \"Name\" and \"Description\"."""

    externalSystemTable: OCITable


@dataclass
class ServiceProviderRoutingProfileGetResponse(OCIDataResponse):
    """Response to ServiceProviderRoutingProfileGetRequest."""

    routingProfile: Optional[str] = None


@dataclass
class ServiceProviderSIPAuthenticationPasswordRulesGetResponseRI(OCIDataResponse):
    """Response to ServiceProviderSIPAuthenticationPasswordRulesGetRequestRI.
    Contains the SIP authentication password rules for the service provider."""

    useServiceProviderSettings: bool

    disallowAuthenticationName: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    sendPermanentLockoutNotification: bool

    endpointAuthenticationLockoutType: str

    endpointTemporaryLockoutThreshold: int

    endpointWaitAlgorithm: str

    endpointLockoutFixedMinutes: str

    endpointPermanentLockoutThreshold: int

    trunkGroupTemporaryLockoutThreshold: int

    trunkGroupAuthenticationLockoutType: str

    trunkGroupWaitAlgorithm: str

    trunkGroupLockoutFixedMinutes: str

    trunkGroupPermanentLockoutThreshold: int

    usePasswordValidationService: bool

    permanentLockoutNotifyEmailAddress: Optional[str] = None


@dataclass
class ServiceProviderScheduleGetEventDetailListResponse(OCIDataResponse):
    """Response to ServiceProviderScheduleGetEventDetailListRequest.
    The response contains a list of ScheduleEvents.
    If the scheduleKey doesn't refer to an existing schedule on the AS, then the response will be empty."""

    scheduleEventsList: List[ScheduleEvents] = field(default_factory=list)


@dataclass
class ServiceProviderScheduleGetEventListResponse(OCIDataResponse):
    """Response to ServiceProviderScheduleGetEventListRequest.
    The response contains a list of events."""

    eventName: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderScheduleGetEventResponse(OCIDataResponse):
    """Response to ServiceProviderScheduleGetEventRequest.
    The response contains the event of the service provider schedule."""

    startDate: int

    allDayEvent: bool

    startTime: HourMinute

    endTime: HourMinute

    endDate: int

    recurrence: Optional[Recurrence] = None


@dataclass
class ServiceProviderScheduleGetListResponse(OCIDataResponse):
    """Response to ServiceProviderScheduleGetListRequest.
    The response contains a list of service provider schedules."""

    scheduleKey: List[ScheduleKey] = field(default_factory=list)


@dataclass
class ServiceProviderServiceGetAuthorizationListResponse(OCIDataResponse):
    """Response to ServiceProviderServiceGetAuthorizationListRequest.
    Contains two tables, one for the group services and one for the user services.
    The Group Service table has column headings:
    \"Service Name\", \"Authorized\", \"Assigned\", \"Limited\", \"Quantity\", \"Allocated\", \"Licensed\", \"Service Pack Allocation\"
    The User Service table has column headings:
    \"Service Name\", \"Authorized\", \"Assigned\", \"Limited\", \"Quantity\", \"Allocated\", \"Licensed\", \"Service Pack Allocation\", \"User Assignable\", \"Service Pack Assignable\"."""

    groupServicesAuthorizationTable: OCITable

    userServicesAuthorizationTable: OCITable


@dataclass
class ServiceProviderServiceGetAuthorizationResponse(OCIDataResponse):
    """Response to ServiceProviderServiceGetAuthorizationRequest.
    If the feature was never licensed, then \"authorized\" is false and the remaining elements are not returned.
    If the service pack is available for use, \"authorized\" is true.
    \"authorizedQuantity\" can be unlimited or a quantity. In the case of a service pack, \"authorizedQuantity\" is the service pack's quantity.
    \"authorizable\" is applicable for user services and group services; it is not returned for service packs."""

    authorized: bool

    authorizedQuantity: Optional[UnboundedNonNegativeInt] = None

    usedQuantity: Optional[UnboundedNonNegativeInt] = None

    authorizable: Optional[bool] = None


@dataclass
class ServiceProviderServiceGetUserAssignableListResponse(OCIDataResponse):
    """Response to ServiceProviderServiceGetUserAssignableListRequest."""

    serviceName: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderServicePackGetDetailListResponse(OCIDataResponse):
    """Response to ServiceProviderServicePackGetDetailListRequest. It contains the service pack details
    and the list of services in a table format. The column headings are \"Service\", \"Authorized\"
    \"Allocated\" and \"Available\"."""

    servicePackName: str

    isAvailableForUse: bool

    servicePackQuantity: UnboundedPositiveInt

    assignedQuantity: UnboundedNonNegativeInt

    allowedQuantity: UnboundedPositiveInt

    userServiceTable: OCITable

    servicePackDescription: Optional[str] = None


@dataclass
class ServiceProviderServicePackGetListResponse(OCIDataResponse):
    """Response to ServiceProviderServicePackGetListRequest."""

    servicePackName: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderServicePackGetServiceUsageListResponse(OCIDataResponse):
    """Response to ServiceProviderServicePackGetServiceUsageListRequest.
    The column headings are \"Service Pack Name\", \"Total Packs\" and \"Allocated to Groups\" """

    serviceUsageTable: OCITable


@dataclass
class ServiceProviderServicePackGetUtilizationListResponse(OCIDataResponse):
    """Response to ServiceProviderServicePackGetUtilizationListRequest.
    For each service pack, a table of groups utilizing the pack is returned.
    The utilization table column headings are \"Group\", \"Total Packs\" and \"Assigned\"."""

    servicePackName: List[str] = field(default_factory=list)

    serviceUtilizationTable: List[OCITable] = field(default_factory=list)


@dataclass
class ServiceProviderServicePackMigrationTaskGetAvailableGroupListResponse(
    OCIDataResponse
):
    """Response to ServiceProviderServicePackMigrationTaskGetAvailableGroupListRequest.
    The groupTable column headings are: \"Group Id\", \"Group Name\", \"User Count\"."""

    groupTable: OCITable


@dataclass
class ServiceProviderServicePackMigrationTaskGetListResponse21(OCIDataResponse):
    """Response to ServiceProviderServicePackMigrationTaskGetListRequest21.
    Contains a table with  a row for each service pack migration task and column headings :
    \"Start Timestamp Milliseconds\", \"Name\", \"Status\", \"Error Count\", \"Users Processed\", \"Users Total\".
    The start timestamp column is the number of milliseconds since the standard base time known as \"the epoch\",
    namely January 1, 1970, 00:00:00 GMT. The status column is the task status which can be Awaiting edit, Pending,
    Processing, Terminating, Terminated, Stopped by system, Completed, or Expired."""

    taskTable: OCITable


@dataclass
class ServiceProviderServicePackMigrationTaskGetResponse21(OCIDataResponse):
    """Response to ServiceProviderServicePackMigrationTaskGetRequest21.
    The groupTable column headings are: \"Group Id\", \"Group Name\", and \"User Count\"."""

    taskName: str

    expireAfterNumHours: int

    maxDurationHours: int

    sendReportEmail: bool

    abortOnError: bool

    reportAllUsers: bool

    automaticallyIncrementServiceQuantity: bool

    errorCount: int

    status: str

    groupsProcessed: int

    groupsTotal: int

    usersProcessed: int

    usersTotal: int

    userSelectionType: str

    reportFilePathName: str

    migrateAllGroups: bool

    groupTable: OCITable

    startTimestamp: Optional[str] = None

    actualStartTimestamp: Optional[str] = None

    reportDeliveryEmailAddress: Optional[str] = None

    abortErrorThreshold: Optional[int] = None

    userSelectionServicePackName: List[str] = field(default_factory=list)

    userSelectionServiceName: List[str] = field(default_factory=list)

    removeServicePackName: List[str] = field(default_factory=list)

    removeServiceName: List[str] = field(default_factory=list)

    assignServicePackName: List[str] = field(default_factory=list)

    assignServiceName: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderServicePhoneNumberLookupResponse(OCIDataResponse):
    """Response to the ServiceProviderServicePhoneNumberLookupRequest.
    The column headings for the userTable are: \"Group Id\", \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\" and \"Department\"."""

    userTable: OCITable


@dataclass
class ServiceProviderSessionAdmissionControlGetResponse(OCIDataResponse):
    """Response to the ServiceProviderSessionAdmissionControlGetRequest.
    The response contains the session admission control capacity allocated for the service provider."""

    restrictAggregateSessions: bool

    countIntraServiceProviderSessions: bool

    maxSessions: Optional[int] = None

    maxUserOriginatingSessions: Optional[int] = None

    maxUserTerminatingSessions: Optional[int] = None


@dataclass
class ServiceProviderSessionAdmissionControlWhiteListGetResponse(OCIDataResponse):
    """Response to the ServiceProviderSessionAdmissionControlWhiteListGetRequest.
    The response contains the White List information."""

    enableWhiteList: bool

    matchDigitPattern: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderStirShakenGetResponse23V2(OCIDataResponse):
    """Response to the ServiceProviderStirShakenGetRequest23V2."""

    useParentLevelSettings: bool

    signingPolicy: str

    taggingPolicy: str

    tagFromOrPAI: str

    verstatTag: str

    useOSValueForOrigId: bool

    attestationLevel: str

    enableVerification: bool

    verificationErrorHandling: str

    proxyVerstatToCNAMSubscribe: bool

    useUnknownHeadersFromCNAMNotify: bool

    enableSigningForUnscreenedTrunkGroupOriginations: bool

    enableTaggingForUnscreenedTrunkGroupOriginations: bool

    unscreenedTrunkGroupOriginationAttestationLevel: str

    includeTaggedHeadersToAccessSide: bool

    proxyIdentityHeaderToAccessSide: bool

    checkDirectoryNumbersForAttestation: bool

    matchUnassignedNumbersOnly: bool

    enableTaggingForRedirectedCalls: bool

    preferIngressTagging: bool

    signingServiceURL: Optional[str] = None

    origUUID: Optional[str] = None

    verificationServiceURL: Optional[str] = None


@dataclass
class ServiceProviderTemplateOnlyDeviceFileGetListResponse(OCIDataResponse):
    """Response to ServiceProviderTemplateOnlyDeviceFileGetListRequest.
    Contains a list of template files used to support a Visual Device Management device."""

    templateFileUrl: List[str] = field(default_factory=list)


@dataclass
class ServiceProviderThirdPartyEmergencyCallingGetResponse22(OCIDataResponse):
    """Response to the ServiceProviderThirdPartyEmergencyCallingGetRequest22.
    The response contains the third-party emergency call service settings for the service provider."""

    allowActivation: bool

    hasGroupEnabled: bool

    customerId: Optional[str] = None

    secretKey: Optional[str] = None


@dataclass
class ServiceProviderTrunkGroupGetResponse23(OCIDataResponse):
    """Response to the ServiceProviderTrunkGroupGetRequest23.
    The response contains the maximum and bursting maximum permissible active trunk group calls for the service provider."""

    maxActiveCalls: UnboundedNonNegativeInt

    burstingMaxActiveCalls: UnboundedNonNegativeInt

    numberOfBurstingBTLUs: UnboundedNonNegativeInt


@dataclass
class ServiceProviderVisualDeviceManagementGetDeviceInfoResponse(OCIDataResponse):
    """Response to ServiceProviderVisualDeviceManagementGetDeviceInfoRequest."""

    deviceType: str

    supportVisualDeviceManagement: bool

    macAddress: Optional[str] = None

    primaryUser: Optional[PrimaryUserInfo] = None


@dataclass
class ServiceProviderVoiceMessagingGroupGetResponse(OCIDataResponse):
    """Response to ServiceProviderVoiceMessagingGroupGetRequest.
    Contains the service provider's or enterprise's voice messaging settings."""

    useSystemDefaultDeliveryFromAddress: bool

    useSystemDefaultNotificationFromAddress: bool

    useSystemDefaultVoicePortalLockoutFromAddress: bool

    deliveryFromAddress: Optional[str] = None

    notificationFromAddress: Optional[str] = None

    voicePortalLockoutFromAddress: Optional[str] = None


@dataclass
class ServiceProviderVoiceMessagingGroupGetVoicePortalBrandingResponse16(
    OCIDataResponse
):
    """Response to the ServiceProviderVoiceMessagingGroupGetVoicePortalBrandingRequest16."""

    voicePortalGreetingSelection: str

    voiceMessagingGreetingSelection: str

    voicePortalGreetingFileDescription: Optional[str] = None

    voicePortalGreetingMediaFileType: Optional[str] = None

    voiceMessagingGreetingFileDescription: Optional[str] = None

    voiceMessagingGreetingMediaFileType: Optional[str] = None


@dataclass
class ServiceProviderVoiceMessagingGroupGetVoicePortalResponse(OCIDataResponse):
    """Response to ServiceProviderVoiceMessagingGroupGetVoicePortalRequest."""

    voicePortalScope: str


@dataclass
class ServiceProviderXsiPolicyProfileGetAssignedGroupListResponse(OCIDataResponse):
    """Response to ServiceProviderXsiPolicyProfileGetAssignedGroupListRequest.
    Contains a table of group that have the group Xsi Policy Profile
    assigned. The column headings are: \"Group Id\", \"Group Name\"."""

    groupTable: OCITable


@dataclass
class ServiceProviderXsiPolicyProfileGetAssignedListResponse(OCIDataResponse):
    """Response to ServiceProviderXsiPolicyProfileGetAssignedListRequest.
    Contains a table of all Xsi Policy Profile assigned to.
    The column headings are: \"Name\", \"Level\", \"Description\" and \"Default\"."""

    assignedTable: OCITable


@dataclass
class ServiceProviderZoneCallingRestrictionsGetResponse(OCIDataResponse):
    """Response to ServiceProviderZoneCallingRestrictionsGetRequest"""

    enableZoneCallingRestrictions: bool

    enableOriginationRoamingRestrictions: bool

    enableEmergencyOriginationRoamingRestrictions: bool

    enableTerminationRoamingRestrictions: bool


@dataclass
class SystemASRParametersGetResponse23(OCIDataResponse):
    """Response to SystemASRParametersGetRequest23.
    Contains a list of system Application Server Registration parameters.

    The following elements are only used in AS data mode:
      enableCustomMessageControl, value \"false\" is returned in XS data mode
      customNumberOfUsersPerMessage, value \"10\" is returned in XS data mode
      customMessageIntervalMilliseconds, value \"100000\" is returned in XS data mode"""

    maxTransmissions: int

    retransmissionDelayMilliSeconds: int

    listeningPort: int

    enableCustomMessageControl: bool

    customNumberOfUsersPerMessage: int

    customMessageIntervalMilliseconds: int


@dataclass
class SystemAccessDeviceCustomTagGetListResponse(OCIDataResponse):
    """Response to SystemAccessDeviceCustomTagGetListRequest.
    Contains a table of custom configuration tags managed by the Device Management System on a per-device profile basis.

    In AS data mode, the column headings are: \"Tag Name\", \"Tag Value\", \"Actual Tag Value\".
    In XS data mode, the column headings are: \"Tag Name\", \"Tag Value\", \"Is Encrypted\", \"Actual Tag Value\"."""

    deviceCustomTagsTable: OCITable


@dataclass
class SystemAccessDeviceDeviceActivationGetResponse(OCIDataResponse):
    """Response to SystemAccessDeviceDeviceActivationGetRequest.
    The response contains the activation code (if available), the expiry time (if available) and the activation state.
    The expiryTime is represented as a timestamp, i.e. the number of milliseconds
    since January 1, 1970, 00:00:00 GMT."""

    activationState: str

    activationCode: Optional[str] = None

    expiryTime: Optional[int] = None


@dataclass
class SystemAccessDeviceFileGetListResponse14sp8(OCIDataResponse):
    """Response to SystemAccessDeviceFileGetListRequest14sp8.
    Contains a table of device files managed by the Device Management System on a per-device profile basis.
    The column headings are: \"File Format\", \"Is Authenticated\", \"Access URL\", \"Repository URL\", \"Template URL\", \"Extended Capture URL\", \"Is File Linked\".

    The following column is only populated in AS data mode for leaf devices.
      \"Is File Linked\" """

    deviceFilesTable: OCITable


@dataclass
class SystemAccessDeviceFileGetResponse20(OCIDataResponse):
    """Response to SystemAccessDeviceFileGetRequest20."""

    fileSource: str

    accessUrl: str

    configurationFileName: Optional[str] = None

    repositoryUrl: Optional[str] = None

    templateUrl: Optional[str] = None

    extendedCaptureEnabled: Optional[bool] = None

    extendedCaptureURL: Optional[str] = None


@dataclass
class SystemAccessDeviceGetAllResponse(OCIDataResponse):
    """Response to SystemAccessDeviceGetAllRequest.
    Contains a table of devices configured in the entire system.
    The column headings are: \"Service Provider Id\", \"Is Enterprise\", \"Group Id\",
    \"Device Name\", \"Device Type\", \"Net Address\", \"MAC Address\", \"Status\", \"Reseller Id\",
    \"Access Device External Id\".

    The following columns are only returned in AS data mode:
      \"Reseller Id\"
      \"Access Device External Id\" """

    accessDeviceTable: OCITable


@dataclass
class SystemAccessDeviceGetAvailableCustomTagListResponse(OCIDataResponse):
    """Response to SystemAccessDeviceGetAvailableCustomTagListRequest.
    Contains a table of all available custom tags managed by the Device Management System on a per-device profile basis.

    In AS data mode, the column headings are: \"Tag Name\", \"Tag Value\", \"Tag Level\", \"Tag Set Name\", \"Region Name\".

    In XS data mode, the column headings are: \"Tag Name\", \"Tag Value\", \"Tag Level\", \"Tag Set Name\", \"Is Encrypted\".

    \"Tag Level\" can take the value: \"System Default\", \"System\", \"Service Provider\", \"Group\" or \"Device Profile\"."""

    deviceAvailableCustomTagsTable: OCITable


@dataclass
class SystemAccessDeviceGetLinkedLeafDeviceListResponse22(OCIDataResponse):
    """Response to SystemAccessDeviceGetLinkedLeafDeviceListRequest22."""

    treeDeviceLinkId: str

    leafDeviceKey: List[AccessDeviceKey] = field(default_factory=list)

    supportLinks: List[str] = field(default_factory=list)


@dataclass
class SystemAccessDeviceGetLinkedTreeDeviceResponse(OCIDataResponse):
    """Response to SystemAccessDeviceGetLinkedTreeDeviceRequest."""

    treeDeviceInfo: Optional[TreeDeviceInfo] = None


@dataclass
class SystemAccessDeviceGetListResponse14(OCIDataResponse):
    """Response to SystemAccessDeviceGetListRequest14.
    Contains a table of devices defined at the System-level.
    The column headings are:
    \"Device Name\", \"Device Type\", \"Available Ports\", \"Net Address\" and \"MAC Address\", \"Status\", \"Version\", and \"Access Device External Id\".

    The following columns are only returned in AS data mode:
      \"Access Device External Id\" """

    accessDeviceTable: OCITable


@dataclass
class SystemAccessDeviceGetNativeTagsWithLogicListResponse(OCIDataResponse):
    """Response to SystemAccessDeviceGetNativeTagsWithLogicListRequest.
    Contains a table of all native tags with logic managed by the Device Management System on a per-device profile basis.

    The column headings are: \"Tag Name\", \"Tag Value\"."""

    deviceNativeTagsWithLogicTable: OCITable


@dataclass
class SystemAccessDeviceGetPagedSortedListResponse(OCIDataResponse):
    """Response to SystemAccessDeviceGetPagedSortedListRequest.
    Contains a table of devices configured at system level.
    The column headings are: \"Device Name\", \"Device Type\", \"Available Ports\", \"Net Address\", \"MAC Address\", \"Status\", \"Version\", and \"Support Visual Device Management API\".
    When CloudPBX is not licensed, the column \"Support Visual Device Management API\" values are not returned."""

    accessDeviceTable: OCITable


@dataclass
class SystemAccessDeviceGetResponse24V3(OCIDataResponse):
    """Response to SystemAccessDeviceGetRequest24V3

    The following elements are only used in AS data mode:
       version
       deviceName
       deviceExternalId

    The following elements are only used in AS data mode and not returned in XS data mode:
       isWebexTeamsDevice
       defaultPathHeader
       deviceCode
       deviceIPEI
       deviceIndex
       useDeviceCode
       authBearerSubject"""

    deviceType: str

    protocol: str

    numberOfPorts: UnboundedPositiveInt

    numberOfAssignedPorts: int

    status: str

    deviceName: str

    netAddress: Optional[str] = None

    port: Optional[int] = None

    outboundProxyServerNetAddress: Optional[str] = None

    stunServerNetAddress: Optional[str] = None

    macAddress: Optional[str] = None

    serialNumber: Optional[str] = None

    description: Optional[str] = None

    physicalLocation: Optional[str] = None

    transportProtocol: Optional[str] = None

    useCustomUserNamePassword: Optional[bool] = None

    userName: Optional[str] = None

    version: Optional[str] = None

    isWebexTeamsDevice: Optional[bool] = None

    defaultPathHeader: Optional[str] = None

    deviceExternalId: Optional[str] = None

    deviceCode: Optional[str] = None

    deviceIPEI: Optional[str] = None

    deviceIndex: Optional[int] = None

    useDeviceCode: Optional[bool] = None

    authBearerSubject: Optional[str] = None


@dataclass
class SystemAccessDeviceGetUserListResponse21sp1(OCIDataResponse):
    """Response to SystemAccessDeviceGetUserListRequest21sp1.
    The column headings for the deviceUserTable are: \"Line/Port\", \"Last Name\",
    \"First Name\", \"Phone Number\", \"Service Provider Id\", \"Group Id\", \"User Id\",
    \"User Type\", \"Endpoint Type\", \"Primary Line/Port\", \"Order\", \"Extension\", \"Department\", \"Email Address\", \"Private Identity\".
    If the identity/device profile is an identity, the table will contain a row for each TEL-URI in the Phone Number column.
    If the identity/device profile is a real device, rows for the alternate numbers are not included.
    The User Type column contains one of the enumerated UserType values.
    The Endpoint Type column contains one of the enumerated EndpointType21sp1 values.
    The value Mobility in Endpoint Type column is only applicable in AS data mode.
    The Private Identity column is empty is AS mode."""

    deviceUserTable: OCITable


@dataclass
class SystemAccessDeviceMonitorGetDeviceTypeListResponse(OCIDataResponse):
    """Response to SystemAccessDeviceMonitorGetDeviceTypeListRequest."""

    deviceType: List[str] = field(default_factory=list)


@dataclass
class SystemAccessDeviceMonitorParametersGetResponse(OCIDataResponse):
    """Response to SystemAccessDeviceMonitorParametersGetListRequest.
    Contains a list of system Access Device Monitor parameters."""

    pollingIntervalMinutes: int


@dataclass
class SystemAccessDeviceTagSetGetResponse(OCIDataResponse):
    """Response to SystemAccessDeviceTagSetGetRequest.
    The response includes a tag set name defined in the access device."""

    tagSetName: Optional[str] = None


@dataclass
class SystemAccessDeviceTypeGetEnhancedConfigurableListResponse(OCIDataResponse):
    """Response to SystemAccessDeviceTypeGetEnhancedConfigurableListRequest.
    Contains a table with columns: \"Access Device Type\", \"Enhanced Configuration Type\", \"Supports Reset\".
    The \"Enhanced Configuration Type\" column contains one of the AccessDeviceEnhancedConfigurationType14
    enumerated values.
    The \"Supports Reset\" column is a boolean flag indicating the device can be remotely reset."""

    deviceTypeTable: OCITable


@dataclass
class SystemAccessDeviceTypeGetListResponse(OCIDataResponse):
    """Response to SystemAccessDeviceTypeGetListRequest."""

    deviceType: List[str] = field(default_factory=list)


@dataclass
class SystemAccountingGetChargingFunctionElementServerListResponse(OCIDataResponse):
    """Response to SystemAccountingGetChargingFunctionElementServerListRequest. The accounting charging function element Server table column
    headings are: \"Address\", \"Extended Net Address\", \"Type\", \"Description\"."""

    chargingFunctionElementServerTable: OCITable


@dataclass
class SystemAccountingGetRadiusServerListResponse(OCIDataResponse):
    """Response to SystemAccountingGetRadiusServerListRequest. The Radius Server table
    column headings are: \"Net Address\", \"Port\", \"Description\" """

    radiusServerTable: OCITable


@dataclass
class SystemAccountingInhibitedAttributeValuePairCodeGetListResponse(OCIDataResponse):
    """Response to
    SystemAccountingInhibitedAttributeValuePairCodeGetListRequest. Contains a 2 column
    table with column headings \"Attribute Value Pair Code\" and \"Vendor Id\"."""

    inhibitedAttributeValuePairCodeTable: OCITable


@dataclass
class SystemAdminGetListResponse(OCIDataResponse):
    """Response to SystemAdminGetListRequest.
    Contains a 6 column table with column headings \"Administrator ID\",
    \"Last Name\", \"First Name\", \"Type\", \"Read Only\", \"Language\"."""

    systemAdminTable: OCITable


@dataclass
class SystemAdminGetResponse22(OCIDataResponse):
    """Response to the SystemAdminGetRequest22.
    The response contains the system or provisioning administrators profile information.

    The following elements are only used in AS data mode and ignored in XS data mode.
    accountDisabled
    lastAuthenticatedDate"""

    language: str

    adminType: str

    readOnly: bool

    accountDisabled: bool

    lastAuthenticatedDate: str

    firstName: Optional[str] = None

    lastName: Optional[str] = None


@dataclass
class SystemAdviceOfChargeCostInformationSourceGetListResponse(OCIDataResponse):
    """Response to SystemAdviceOfChargeCostInformationSourceGetListRequest.
    Contains a table with column headings: \"PeerIdentity\", \"Priority\" """

    costInformationSourceTable: OCITable


@dataclass
class SystemAdviceOfChargeGetResponse25(OCIDataResponse):
    """Response to SystemAdviceOfChargeGetRequest25.
    Contains a list of system Advice of Charge parameters."""

    delayBetweenNotificationSeconds: int

    incomingAocHandling: str

    useOCSEnquiry: bool

    OCSEnquiryType: str

    proxyAoCBody: bool


@dataclass
class SystemAliasGetListResponse(OCIDataResponse):
    """Response to SystemAliasGetListRequest. Contains the list of all network alias' for
    the Application Server."""

    aliasNetAddress: List[str] = field(default_factory=list)


@dataclass
class SystemAlternateUserIdGetListResponse(OCIDataResponse):
    """Response to SystemAlternateUserIdGetListRequest.
    The \"User Type\" column contains the corresponding enumerated UserType value.
    Contains a table of alternate user ids, the column headings are:
      \"User Id\", \"Alternate User Id\", \"Group Id\", \"Organization Id\", \"Reseller Id\" and \"User Type\".

    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    alternateUserIdTable: OCITable


@dataclass
class SystemAnonymousCallRejectionGetResponse(OCIDataResponse):
    """Response to the SystemAnonymousCallRejectionGetRequest.
    The response contains the anonymous call rejection system.\"."""

    paiRequired: bool

    screenOnlyLocalCalls: bool


@dataclass
class SystemApplicationControllerGetListResponse(OCIDataResponse):
    """Response to the SystemApplicationControllerGetListRequest.
    Contains a table with column headings: \"Name\", \"Subscriber Id\", \"Channel Set Id\", \"Status\".
    The column values for \"Status\" can either be \"ready\" or \"notReady\"."""

    applicationControllerTable: OCITable


@dataclass
class SystemAuthenticationLockoutSettingsGetResponse(OCIDataResponse):
    """Response to SystemAuthenticationLockoutSettingsGetRequest.
    Contains the authentication lockout settings in the system."""

    counterResetIntervalDays: int

    counterResetHour: int

    counterResetMinute: int

    emergencySIPBypassAllowed: bool


@dataclass
class SystemAutoDisableAccountsGetResponse(OCIDataResponse):
    """Response to the SystemAutoDisableAccountsGetRequest."""

    accountInactivityTimeoutDays: int

    enableAutoDisableAccounts: bool

    enableAutoDisableAccountsSystemAdminLevel: bool

    enableAutoDisableAccountsProvisioningAdminLevel: bool

    enableAutoDisableAccountsResellerAdminLevel: bool

    enableAutoDisableAccountsSvcProviderAdminLevel: bool

    enableAutoDisableAccountsGroupAdminLevel: bool

    enableAutoDisableAccountsDepartmentAdminLevel: bool


@dataclass
class SystemAutomaticCallbackGetReleaseCauseListResponse(OCIDataResponse):
    """Response to SystemAutomaticCallbackGetReleaseCauseListRequest."""

    releaseCause: List[str] = field(default_factory=list)


@dataclass
class SystemAutomaticCallbackGetResponse17(OCIDataResponse):
    """Response to SystemAutomaticCallbackGetRequest17."""

    monitorMinutes: int

    maxMonitorsPerOriginator: int

    maxCallbackRings: int

    maxMonitorsPerTerminator: int

    terminatorIdleGuardSeconds: int

    callbackMethod: str

    pollingIntervalSeconds: int

    activationDigit: int


@dataclass
class SystemAutomaticCollectCallGetResponse22(OCIDataResponse):
    """Response to the SystemAutomaticCollectCallGetRequest22.
    Returns system Automatic Collect Call service settings."""

    enableAutomaticCollectCall: bool

    enableConnectTone: bool

    includeCountryCodeInCic: bool


@dataclass
class SystemAutomaticCollectCallPrefixDigitsGetListResponse(OCIDataResponse):
    """Response to the SystemAutomaticCollectCallPrefixDigitsGetListRequest.
    Contains a table with column headings: \"Country Code\", \"Prefix\"."""

    prefixTable: OCITable


@dataclass
class SystemBroadCloudGetResponse22(OCIDataResponse):
    """Response to the SystemBroadCloudGetRequest22.
    The response contains the system interface attributes for Messaging Server/BroadCloud."""

    enableSynchronization: bool

    proxyPort: int

    provisioningUrl: Optional[str] = None

    provisioningUserId: Optional[str] = None

    proxyHost: Optional[str] = None


@dataclass
class SystemBroadWorksAnywhereGetResponse(OCIDataResponse):
    """The response to a SystemBroadWorksAnywhereGetRequest."""

    enableTransferNotification: bool


@dataclass
class SystemBroadWorksMobilityGeographicalPoolGetListResponse(OCIDataResponse):
    """Response to the SystemBroadWorksMobilityGeographicalPoolGetListRequest.
    Contains a table with column headings: \"Pool\", \"Country Code\", \"Is Default\", \"Description\"."""

    geographicalPoolTable: OCITable


@dataclass
class SystemBroadWorksMobilityGeographicalPoolIMRNGetListResponse(OCIDataResponse):
    """Response to SystemBroadWorksMobilityGeographicalPoolIMRNGetListRequest."""

    countryCode: str

    imrnNumber: List[str] = field(default_factory=list)


@dataclass
class SystemBroadWorksMobilityGeographicalPoolPrefixGetListResponse(OCIDataResponse):
    """Response to the SystemBroadWorksMobilityGetGeographicalPoolPrefixListRequest."""

    countryCode: str

    prefix: List[str] = field(default_factory=list)


@dataclass
class SystemBroadWorksMobilityGetIMRNListResponse(OCIDataResponse):
    """Response to SystemBroadWorksMobilityDnGetListRequest."""

    imrnNumber: List[str] = field(default_factory=list)


@dataclass
class SystemBroadWorksMobilityGetMobileNetworkIMRNListResponse(OCIDataResponse):
    """Response to SystemBroadWorksMobilityGetMobileNetworkIMRNListRequest."""

    imrnNumber: List[str] = field(default_factory=list)


@dataclass
class SystemBroadWorksMobilityGetResponse22V3(OCIDataResponse):
    """The response to a SystemBroadWorksMobilityGetRequest22V3."""

    enableLocationServices: bool

    enableMSRNLookup: bool

    enableMobileStateChecking: bool

    denyCallOriginations: bool

    denyCallTerminations: bool

    imrnTimeoutMillisecnds: int

    enableInternalCLIDDelivery: bool

    includeRedirectForMobilityTermination: bool

    enableInternalCLIDDeliveryAccessLocations: bool

    enableEnhancedUnreachableStateChecking: bool

    enableNetworkCallBarringStatusCheck: bool

    networkTranslationIndex: Optional[str] = None


@dataclass
class SystemBroadWorksMobilityMobileNetworkGetListResponse(OCIDataResponse):
    """The response to a SystemBroadWorksMobilityMobileNetworkGetListRequest.
    Contains a table with column headings: \"Name\", \"SCF Signaling Net Address\", \"SCF Signaling Port\" """

    mobileNetworkTable: OCITable


@dataclass
class SystemBroadWorksMobilityMobileNetworkGetResponse(OCIDataResponse):
    """The response to a SystemBroadWorksMobilityMobileNetworkGetRequest."""

    refreshPeriodSeconds: int

    maxConsecutiveFailures: int

    maxResponseWaitTimeMilliseconds: int

    enableAnnouncementSuppression: bool

    scfSignalingNetAddress: Optional[str] = None

    scfSignalingPort: Optional[int] = None

    serviceAccessCodeListName: Optional[str] = None


@dataclass
class SystemBroadWorksMobilityMobileSubscriberDirectoryNumberGetSummaryListResponse(
    OCIDataResponse
):
    """Response to SystemBroadWorksMobilityMobileSubscriberDirectoryNumberGetSummaryListRequest.
    The response contains a table with columns: \"Mobile Number\", \"Mobile Network\", \"Service Provider Id\",
    \"Is Enterprise\", \"Group Id\", \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\" and \"Reseller Id\".

    The following columns are only returned in AS data mode:
         \"Reseller Id\" """

    mobileSubscriberDirectoryNumbersSummaryTable: OCITable


@dataclass
class SystemBroadWorksMobilityServiceAccessCodeGetListResponse21(OCIDataResponse):
    """Response to SystemBroadWorksMobilityServiceAccessCodeGetListRequest21.
    Contains a table with column headings: \"Country Code\", \"Service Access Code\", \"Description\" """

    serviceAccessCodeTable: OCITable


@dataclass
class SystemBroadWorksMobilityServiceAccessCodeListGetListResponse(OCIDataResponse):
    """Response to SystemBroadWorksMobilityServiceAccessCodeListGetListRequest."""

    name: List[str] = field(default_factory=list)


@dataclass
class SystemBroadWorksMobilityServiceAccessCodeListUsageGetResponse(OCIDataResponse):
    """Response to SystemBroadWorksMobilityServiceAccessCodeListUsageGetRequest."""

    mobileNetworkName: List[str] = field(default_factory=list)


@dataclass
class SystemBroadWorksReceptionistEnterpriseGetResponse(OCIDataResponse):
    """Response to SystemBroadWorksReceptionistEnterpriseGetRequest.
    Contains a list of BroadWorks Receptionist - Enterprise parameters."""

    maxMonitoredUsers: int


@dataclass
class SystemBusyLampFieldGetResponse23V2(OCIDataResponse):
    """Response to SystemBusyLampFieldGetRequest23V2.

    The following elements are only used in AS data mode:
     forceUseOfTCP
     enableRedundancy, value \"false\" is returned in XS data mode
     redundancyTaskDelayMilliseconds, value \"10000\" is returned in XS data mode
     redundancyTaskIntervalMilliseconds, value of \"1000\" is returned in XS data mode
     maxNumberOfSubscriptionsPerRedundancyTaskInterval, value of \"50\" is returned in XS data mode
     ignoreUnansweredTerminatingCalls, value \"false\" is returned in XS data mode"""

    displayLocalUserIdentityLastNameFirst: bool

    forceUseOfTCP: bool

    enableRedundancy: bool

    redundancyTaskDelayMilliseconds: int

    redundancyTaskIntervalMilliseconds: int

    maxNumberOfSubscriptionsPerRedundancyTaskInterval: int

    ignoreUnansweredTerminatingCalls: bool


@dataclass
class SystemBwDiameterBaseDataGetResponse22(OCIDataResponse):
    """Response to SystemBwDiameterBaseDataGetRequest22.
    Contains a list of System Diameter base parameters."""

    xsListeningPort: int

    xsListeningPortEnabled: bool

    xsListeningSecurePort: int

    xsListeningSecurePortEnabled: bool

    psListeningPort: int

    psListeningPortEnabled: bool

    psListeningSecurePort: int

    psListeningSecurePortEnabled: bool

    psRelayThroughXs: bool

    xsRelayListeningPort: int

    tcTimerSeconds: int

    twTimerSeconds: int

    requestTimerSeconds: int

    busyPeerDetectionOutstandingTxnCount: int

    busyPeerRestoreOutstandingTxnCount: int

    dynamicEntryInactivityTimerHours: int

    advertisedOfflineBillingApplication: str

    advertisedOnlineBillingApplication: str

    peerDiscoveryMode: str

    defaultPort: int

    defaultSecurePort: int

    xsRealm: Optional[str] = None

    psRealm: Optional[str] = None


@dataclass
class SystemBwDiameterPeerGetListResponse(OCIDataResponse):
    """Contains a 6 column table with column headings 'Instance', 'Identity', 'IP Address', 'Port', 'Enabled' and 'Secure'. One row is present for each peer."""

    peerTable: OCITable


@dataclass
class SystemBwDiameterRoutingPeerGetListResponse(OCIDataResponse):
    """Contains a 6 column table with column headings 'Instance', 'Realm',  'ApplicationID', 'Identity, 'Priority', and 'Weight'.  One row is present for each Diameter Routing Peer."""

    routingPeerTable: OCITable


@dataclass
class SystemBwDiameterRoutingRealmGetListResponse(OCIDataResponse):
    """Contains a 4 column table with column headings 'Instance', 'Realm', 'ApplicationID', and 'Default'.  One row is present for each Diameter routing realm."""

    routingRealmTable: OCITable


@dataclass
class SystemCLIDDeliveryPrefixGetListResponse(OCIDataResponse):
    """Response to SystemCLIDDeliveryPrefixGetListRequest."""

    prefix: List[str] = field(default_factory=list)


@dataclass
class SystemCPEConfigGetFileServerListResponse14sp6(OCIDataResponse):
    """Response to SystemCPEConfigGetFileServerListRequest14sp6. The table columns are:
    \"Device Type\", \"File Repository Name\", \"Directory\", \"Extended File Repository Name\"."""

    fileServerTable: OCITable


@dataclass
class SystemCPEConfigParametersGetResponse21(OCIDataResponse):
    """Response to SystemCPEConfigParametersGetRequest21.
    Contains a list of system CPE Config parameters.

    The following elements are only used in AS data mode:
      allowDeviceCredentialsRetrieval, value \"false\" is returned in XS data mode"""

    enableIPDeviceManagement: bool

    ftpConnectTimeoutSeconds: int

    ftpFileTransferTimeoutSeconds: int

    pauseBetweenFileRebuildMilliseconds: int

    minTimeBetweenResetMilliseconds: int

    alwaysPushFilesOnRebuild: bool

    maxFileOperationRetryAttempts: int

    enableAutoRebuildConfig: bool

    eventQueueSize: int

    allowDeviceCredentialsRetrieval: bool

    deviceAccessAppServerClusterName: Optional[str] = None


@dataclass
class SystemCallCenterEnhancedReportingBrandingGetResponse(OCIDataResponse):
    """Response to the SystemCallCenterEnhancedReportingBrandingGetRequest."""

    brandingChoice: str

    customBrandingFileDescription: Optional[str] = None


@dataclass
class SystemCallCenterEnhancedReportingDataTemplateGetListResponse(OCIDataResponse):
    """Response to SystemCallCenterEnhancedReportingDataTemplateGetListRequest."""

    info: List[CallCenterReportDataTemplateInfo] = field(default_factory=list)


@dataclass
class SystemCallCenterEnhancedReportingGetResponse(OCIDataResponse):
    """Response to SystemCallCenterEnhancedReportingGetRequest."""

    archiveReports: bool

    reportApplicationURL: Optional[str] = None

    repositoryApplicationURL: Optional[str] = None


@dataclass
class SystemCallCenterEnhancedReportingReportTemplateGetListResponse(OCIDataResponse):
    """Response to SystemCallCenterEnhancedReportingReportTemplateGetListRequest.
    Contains a table with column headings: \"Name\", \"Description\", \"Is Custom\", \"Type\" and \"Enabled\" """

    reportTemplateTable: OCITable


@dataclass
class SystemCallCenterEnhancedReportingReportTemplateGetResponse(OCIDataResponse):
    """Response to SystemCallCenterEnhancedReportingReportTemplateGetRequest."""

    dataTemplate: str

    xsltTemplateDescription: str

    scope: str

    isEnabled: bool

    description: Optional[str] = None

    filterNumber: Optional[int] = None

    isRealtimeReport: Optional[bool] = None

    callCompletionThresholdParam: Optional[str] = None

    shortDurationThresholdParam: Optional[str] = None

    serviceLevelThresholdParam: Optional[str] = None

    serviceLevelInclusionsParam: Optional[str] = None

    serviceLevelObjectiveThresholdParam: Optional[str] = None

    abandonedCallThresholdParam: Optional[str] = None

    serviceLevelThresholdParamNumber: Optional[int] = None

    abandonedCallThresholdParamNumber: Optional[int] = None

    filterValue: List[str] = field(default_factory=list)


@dataclass
class SystemCallCenterEnhancedReportingScheduledReportGetActiveListResponse(
    OCIDataResponse
):
    """Response to SystemCallCenterEnhancedReportingScheduledReportGetActiveListRequest
    Contains a table with column headings : \"Scheduled Report Name\", \"Description\",
    \"Service Provider Id\", \"Is Enterprise\", \"Group Id\", \"Created By\", \"Is Supervisor Report\",
    \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Template Level\" are \"System\", \"Enterprise\" and \"Group\".
    For the rows with \"Is Enterprise\" column value \"true\", the \"Group Id\" column will be empty."""

    scheduledReportTable: OCITable


@dataclass
class SystemCallCenterEnhancedReportingScheduledReportGetCompletedListResponse(
    OCIDataResponse
):
    """Response to SystemCallCenterEnhancedReportingScheduledReportGetCompletedListRequest
    Contains a table with column headings : \"Scheduled Report Name\", \"Description\",
    \"Service Provider Id\", \"Is Enterprise\", \"Group Id\", \"Created By\", \"Is Supervisor Report\",
    \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Template Level\" are \"System\", \"Enterprise\" and \"Group\".
    For the rows with \"Is Enterprise\" column value \"true\", the \"Group Id\" column will be empty."""

    scheduledReportTable: OCITable


@dataclass
class SystemCallCenterEnhancedReportingScheduledReportGetListResponse(OCIDataResponse):
    """Response to SystemCallCenterEnhancedReportingScheduledReportGetListRequest.
    Contains a table with column headings : \"Scheduled Report Name\", \"Description\",
    \"Service Provider Id\", \"Is Enterprise\", \"Group Id\", \"Created By\", \"Is Supervisor Report\",  \"Status\",
    \"Report Template Name\", \"Report Template Level\" and \"Recurring\".
    The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
    The possible values for \"Status\" are \"Active\", and \"Completed\".
    The possible values for \"Recurring\" are \"None\", \"Daily\", \"Weekly\", \"Monthly\" and \"Yearly\".
    The possible values for \"Report Template Level\" are \"System\", \"Enterprise\" and \"Group\".
    For the rows with \"Is Enterprise\" column value \"true\", the \"Group Id\" column will be empty."""

    scheduledReportTable: OCITable


@dataclass
class SystemCallCenterEnhancedReportingScheduledReportGetReportTemplateUsageListResponse(
    OCIDataResponse
):
    """Response to SystemCallCenterEnhancedReportingScheduledReportGetReportTemplateUsageListRequest.
    Contains a table with column headings: \"Schedule Name\", \"Organization Type\", \"Service Provider Id\",
    \"Group Id\", \"Created By\", \"Created By Supervisor\", and \"Is Active\".
     The \"Organization Type\" is either \"Service Provider\" or \"Enterprise\".
     The \"Created By\" can be either \"Administrator\" or user id if created by supervisor.
     The possible values for \"Created By Supervisor\" are \"true\" and \"false\"."""

    scheduleReportTable: OCITable


@dataclass
class SystemCallCenterEnhancedReportingScheduledTaskParametersGetResponse25(
    OCIDataResponse
):
    """Response to SystemCallCenterEnhancedReportingScheduledTaskParametersGetRequest25."""

    scheduledReportSearchIntervalMinutes: int

    maximumScheduledReportsPerInterval: int

    deleteScheduledReportDaysAfterCompletion: int

    callCenterEventMode: str

    useDialedAddressForRemoteNumber: bool


@dataclass
class SystemCallCenterEventRecordingFileParametersGetResponse(OCIDataResponse):
    """Response to SystemCallCenterEventRecordingFileParametersGetRequest.
    Contains a list of system Call Center Event Recording File parameters."""

    fileRetentionTimeDays: int

    fileRotationPeriodMinutes: str

    fileRotationOffsetMinutes: int

    remoteUrl: Optional[str] = None

    remoteUserId: Optional[str] = None


@dataclass
class SystemCallCenterGetResponse21(OCIDataResponse):
    """Response to SystemCallCenterGetRequest21."""

    defaultFromAddress: str

    statisticsSamplingPeriodMinutes: int

    defaultEnableGuardTimer: bool

    defaultGuardTimerSeconds: int

    forceAgentUnavailableOnDNDActivation: bool

    forceAgentUnavailableOnPersonalCalls: bool

    forceAgentUnavailableOnBouncedCallLimit: bool

    numberConsecutiveBouncedCallsToForceAgentUnavailable: int

    forceAgentUnavailableOnNotReachable: bool

    defaultPlayRingWhenOfferCall: bool

    uniformCallDistributionPolicyScope: str

    callHandlingSamplingPeriodMinutes: int

    callHandlingMinimumSamplingSize: int

    playToneToAgentForEmergencyCall: bool

    emergencyCallCLIDPrefix: str

    thresholdCrossingNotificationEmailGuardTimerSeconds: int

    allowAgentDeviceInitiatedForward: bool


@dataclass
class SystemCallMeNowGetResponse(OCIDataResponse):
    """Response to SystemCallMeNowGetRequest."""

    passcodeLength: int

    passcodeTimeoutSeconds: int


@dataclass
class SystemCallNotifyGetResponse(OCIDataResponse):
    """Response to SystemCallNotifyGetRequest."""

    defaultFromAddress: str

    useShortSubjectLine: bool

    useDnInMailBody: bool


@dataclass
class SystemCallProcessingGetPolicyResponse24V2(OCIDataResponse):
    """Response to SystemCallProcessingGetPolicyRequest24V2.
    The following elements are only used in AS data mode:
        enableDialableCallerID
        allowConfigurableCLIDForRedirectingIdentity
        enterpriseCallsCLIDPolicy, value \"Use Location Code plus Extension\" is returned in XS data mode.
        enterpriseGroupCallsCLIDPolicy, value \"Use Location\" is returned in XS data mode.
        serviceProviderGroupCallsCLIDPolicy, value \"Use Location\" is returned in XS data mode.
        enablePhoneListLookup, value \"false\" is returned in XS data mode.
        useMaxConcurrentTerminatingAlertingRequests, value \"false\" is returned in XS data mode.
        maxConcurrentTerminatingAlertingRequests, value \"10\" is returned in XS data mode.
        delayTimerToRemoveCancelledCallsInSeconds, value \"4\" is returned in XS data mode.
        includeRedirectionsInMaximumNumberOfConcurrentCalls, value \"false\" is returned in XS data mode.
        useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable, value \"false\" is returned in XS data mode.
        useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable, value \"false\" is returned in XS data mode.
        allowMobileDNForRedirectingIdentity, value \"false\" is returned in XS data mode.
        conferenceDisableClampTones, value \"false\" is returned in XS data mode.
        useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
        maxCallsPerSecond, value \"1\" is returned in XS data mode.
        forceTreatmentOnMaximumRedirectionDepth, value \"false\" is returned in XS data mode.
        enableUserSelectionOfExternalCLIDPolicy, value \"false\" is returned in XS data mode.
        enableUserConfigurableCLIDModification, value \"false\" is returned in XS data mode.
    The following elements are only used in XS data mode and not returned in AS data mode:
       routeOverrideDomain
       routeOverridePrefix"""

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    mediaPolicySelection: str

    networkUsageSelection: str

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    enableEnterpriseExtensionDialing: bool

    maxConferenceParties: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    blockCallingNameForExternalCalls: bool

    enableDialableCallerID: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    enablePhoneListLookup: bool

    useMaxConcurrentTerminatingAlertingRequests: bool

    maxConcurrentTerminatingAlertingRequests: int

    delayTimerToRemoveCancelledCallsInSeconds: int

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    allowMobileDNForRedirectingIdentity: bool

    conferenceDisableClampTones: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int

    forceTreatmentOnMaximumRedirectionDepth: bool

    enableUserSelectionOfExternalCLIDPolicy: bool

    enableUserConfigurableCLIDModification: bool

    supportedMediaSetName: Optional[str] = None

    conferenceURI: Optional[str] = None

    routeOverrideDomain: Optional[str] = None

    routeOverridePrefix: Optional[str] = None


@dataclass
class SystemCallProcessingPolicyProfileAutoAttendantProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileAutoAttendantProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallProcessingPolicyProfileBroadWorksAnywhereProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileBroadWorksAnywhereProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallProcessingPolicyProfileCallCenterProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileCallCenterProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallProcessingPolicyProfileCollaborateProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileCollaborateProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallProcessingPolicyProfileFindMeFollowMeProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileFindMeFollowMeProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallProcessingPolicyProfileFlexibleSeatingHostProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileFlexibleSeatingHostProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode"""

    useCLIDPolicy: bool

    clidPolicy: str

    emergencyClidPolicy: str

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int

    allowConfigurableCLIDForRedirectingIdentity: Optional[bool] = None


@dataclass
class SystemCallProcessingPolicyProfileGetAssignedNCOSListResponse(OCIDataResponse):
    """Response to the
    SystemCallProcessingPolicyProfileGetAssignedNCOSListRequest.
    The response contains a table of all Network Classes of Service that
    contain the specific CAllP Policy Profile. The column headings
    are \"Name\" and \"Description\"."""

    networkClassOfServiceTable: OCITable


@dataclass
class SystemCallProcessingPolicyProfileGetListResponse(OCIDataResponse):
    """Response to the SystemCallProcessingPolicyProfileGetListRequest.
    The response contains a table of all Call Processing Policy Profiles
    in the system. The column headings are \"Name\" and \"Description\"."""

    callProcessingPolicyProfilesTable: OCITable


@dataclass
class SystemCallProcessingPolicyProfileGetResponse21(OCIDataResponse):
    """Response to a SystemCallProcessingPolicyProfileGetRequest21."""

    description: Optional[str] = None

    assignedSubscriberType: List[str] = field(default_factory=list)


@dataclass
class SystemCallProcessingPolicyProfileGroupPagingProfileGetResponse22(OCIDataResponse):
    """Response to SystemCallProcessingPolicyProfileGroupPagingProfileGetRequest22."""

    useCLIDPolicy: bool

    clidPolicy: str

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool


@dataclass
class SystemCallProcessingPolicyProfileHuntGroupProfileGetResponse22V2(OCIDataResponse):
    """Response to SystemCallProcessingPolicyProfileHuntGroupProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallProcessingPolicyProfileInstantGroupCallProfileGetResponse22(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileInstantGroupCallProfileGetRequest22."""

    useCLIDPolicy: bool

    clidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool


@dataclass
class SystemCallProcessingPolicyProfileMeetMeConferencingProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileMeetMeConferencingProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallProcessingPolicyProfileRoutePointProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileRoutePointProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallProcessingPolicyProfileTrunkGroupPilotProfileGetResponse22V3(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileTrunkGroupPilotProfileGetRequest22V3.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useMediaPolicy: bool

    mediaPolicySelection: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    useMaxConcurrentTerminatingAlertingRequests: bool

    maxConcurrentTerminatingAlertingRequests: int

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    allowMobileDNForRedirectingIdentity: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int

    supportedMediaSetName: Optional[str] = None


@dataclass
class SystemCallProcessingPolicyProfileUserProfileGetResponse22V3(OCIDataResponse):
    """Response to SystemCallProcessingPolicyProfileUserProfileGetRequest22V3.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useMediaPolicy: bool

    mediaPolicySelection: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    usePhoneListLookupPolicy: bool

    enablePhoneListLookup: bool

    useMaxConcurrentTerminatingAlertingRequests: bool

    maxConcurrentTerminatingAlertingRequests: int

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    allowMobileDNForRedirectingIdentity: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int

    supportedMediaSetName: Optional[str] = None


@dataclass
class SystemCallProcessingPolicyProfileVoicePortalProfileGetResponse22V2(
    OCIDataResponse
):
    """Response to SystemCallProcessingPolicyProfileVoicePortalProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: Optional[bool] = None

    maxCallsPerSecond: Optional[int] = None


@dataclass
class SystemCallProcessingPolicyProfileVoiceXMLProfileGetResponse22V2(OCIDataResponse):
    """Response to SystemCallProcessingPolicyProfileVoiceXMLProfileGetRequest22V2.
    The following elements are only used in AS data mode:
      useMaxCallsPerSecond, value \"false\" is returned in XS data mode.
      maxCallsPerSecond, value \"1\" is returned in XS data mode."""

    useCLIDPolicy: bool

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    enterpriseCallsCLIDPolicy: str

    enterpriseGroupCallsCLIDPolicy: str

    serviceProviderGroupCallsCLIDPolicy: str

    useCallLimitsPolicy: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    maxRedirectionDepth: int

    useTranslationRoutingPolicy: bool

    networkUsageSelection: str

    enableEnterpriseExtensionDialing: bool

    enforceGroupCallingLineIdentityRestriction: bool

    enforceEnterpriseCallingLineIdentityRestriction: bool

    allowEnterpriseGroupCallTypingForPrivateDialingPlan: bool

    allowEnterpriseGroupCallTypingForPublicDialingPlan: bool

    overrideCLIDRestrictionForPrivateCallCategory: bool

    useEnterpriseCLIDForPrivateCallCategory: bool

    useIncomingCLIDPolicy: bool

    enableDialableCallerID: bool

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    useUserPhoneNumberForGroupCallsWhenInternalCLIDUnavailable: bool

    useUserPhoneNumberForEnterpriseCallsWhenInternalCLIDUnavailable: bool

    useMaxCallsPerSecond: bool

    maxCallsPerSecond: int


@dataclass
class SystemCallRecordingGetPlatformListResponse22V2(OCIDataResponse):
    """Response to SystemCallRecordingGetPlatformListRequest22V2.
        Contains the default system Call Recording platform, default reseller Call Recording Platform (when applicable in AS data mode) and a table with columns headings
    \"Name\", \"Net Address\", \"Port\", \"Transport Type\", \"Media Stream\", \"Description\", \"Schema Version\", \"Support Video Rec\", \"Reseller Id\", \"Route\".
        The system default recording platform also appears in the table with the other platforms.

        The port can be empty if it is not defined in the recording platform.
        The possible values for \"Support Video Rec\" can be either true or false.
        Schema version values include: 1.0, 2.0, 3.0"""

    callRecordingPlatformTable: OCITable

    systemDefault: Optional[str] = None

    resellerDefault: Optional[str] = None


@dataclass
class SystemCallRecordingGetPlatformUsageResponse22(OCIDataResponse):
    """Response to SystemCallRecordingGetPlatformUsageRequest.
    The response contains a table with columns headings \"Organization Id\",
    \"Organization Type\", \"Group Id\"."""

    groupTable: OCITable


@dataclass
class SystemCallRecordingGetResponse23(OCIDataResponse):
    """Response to SystemCallRecordingGetRequest23.

    The following elements are only used in AS data mode:
      continueCallAfterRecordingFailure, value \"false\" is returned in XS data mode
      maxResponseWaitTimeMilliseconds, value \"50\" is returned in XS data mode
      continueCallAfterVideoRecordingFailure, value \"false\" is returned in XS data mode
      useContinueCallAfterRecordingFailureForOnDemandMode, value \"false\" is returned in XS data mode
      useContinueCallAfterRecordingFailureForOnDemandUserInitiatedStartMode, value \"false\" is returned in XS data mode"""

    continueCallAfterRecordingFailure: bool

    maxResponseWaitTimeMilliseconds: int

    continueCallAfterVideoRecordingFailure: bool

    useContinueCallAfterRecordingFailureForOnDemandMode: bool

    useContinueCallAfterRecordingFailureForOnDemandUserInitiatedStartMode: bool

    restrictCallRecordingProvisioningAccess: bool


@dataclass
class SystemCallReturnGetResponse(OCIDataResponse):
    """Response to SystemCallReturnGetRequest."""

    twoLevelActivation: bool

    provideDate: bool

    lastUnansweredCallOnly: bool

    allowRestrictedNumber: bool

    deleteNumberAfterAnsweredCallReturn: bool

    confirmationKey: Optional[str] = None


@dataclass
class SystemCallTypeGetListResponse(OCIDataResponse):
    """Response to SystemCallTypeGetListRequest."""

    callType: List[str] = field(default_factory=list)


@dataclass
class SystemCallTypeGetMappingListResponse(OCIDataResponse):
    """Response to SystemCallTypeGetMappingListRequest. The table columns are:
    \"Country Code\", \"Digit Map\", \"Call Type\" and \"Ignore AS Emergency Route\".
    The following column is returned only in AS Mode:
    \"Ignore AS Emergency Route\" """

    callTypeMapping: OCITable


@dataclass
class SystemCallWaitingGetResponse(OCIDataResponse):
    """Response to SystemCallWaitingGetRequest."""

    playDistinctiveRingback: bool


@dataclass
class SystemCallingNameRetrievalGetResponse24(OCIDataResponse):
    """Response to SystemCallingNameRetrievalGetRequest24."""

    triggerCNAMQueriesForAllNetworkCalls: bool

    triggerCNAMQueriesForGroupAndEnterpriseCalls: bool

    queryProtocol: str

    queryTimeoutMilliseconds: int

    sipExternalDatabaseTransport: str

    callingNameSource: str

    routeAdvanceTimer: int

    retryFailedCNAMServerInterval: int

    ignoreRestrictedPresentationIndicator: bool

    supportsDNSSRV: bool

    sipExternalDatabaseNetAddress: Optional[str] = None

    sipExternalDatabasePort: Optional[int] = None

    soapExternalDatabaseNetAddress: Optional[str] = None


@dataclass
class SystemCallingPartyCategoryGetListResponse(OCIDataResponse):
    """Response to SystemCallingPartyCategoryGetListRequest.
    Contains a table of Calling Party Category defined in system.
    The column headings are: \"Category Name\", \"User Category\", \"Collect Call\", \"Default\" and \"Web Display Key\"."""

    callingPartyCategoryTable: OCITable


@dataclass
class SystemCallingPartyCategoryGetResponse(OCIDataResponse):
    """Response to SystemCallingPartyCategoryGetRequest.
    Contains information of a Calling Party Category defined in system."""

    userCategory: bool

    payPhone: bool

    operator: bool

    default: bool

    collectCall: bool

    cpcValue: Optional[str] = None

    isupOliValue: Optional[int] = None

    gtdOliValue: Optional[str] = None

    webDisplayKey: Optional[str] = None


@dataclass
class SystemClassmarkGetListResponse(OCIDataResponse):
    """Response to SystemClassmarkGetListRequest.
    Contains a table of with the column headings: \"Class Mark\", \"Value\" and \"Web Display Key\"."""

    classmarkTable: OCITable


@dataclass
class SystemClassmarkGetUtilizationListResponse(OCIDataResponse):
    """Response to SystemClassmarkGetUtilizationListRequest.
    Contains a table with the column headings: \"User Id\", \"Group Id\", \"Service Provider Id\",
    \"Last Name\", \"First Name\", and \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    classmarkUserTable: OCITable


@dataclass
class SystemClientIdentityGetListResponse(OCIDataResponse):
    """Response to SystemClientIdentityGetListRequest.
    Returns a table with column headings:
     \"Client Identity\"."""

    clientIdentityTable: OCITable


@dataclass
class SystemClientSessionParametersGetResponse(OCIDataResponse):
    """Response to SystemClientSessionParametersGetRequest.
    Contains a list of system Client Session (web and CLI) parameters."""

    enableInactivityTimeout: bool

    inactivityTimeoutMinutes: int


@dataclass
class SystemCodecGetListResponse(OCIDataResponse):
    """Response to SystemCodecGetListRequest."""

    codec: List[str] = field(default_factory=list)


@dataclass
class SystemCollaborateGetResponse20sp1V2(OCIDataResponse):
    """Response to SystemCollaborateGetRequest20sp1V2."""

    collaborateRoomIdLength: int

    instantRoomIdleTimeoutSeconds: int

    collaborateRoomMaximumDurationMinutes: int

    supportOutdial: bool

    maxCollaborateRoomParticipants: int

    collaborateActiveTalkerRefreshIntervalSeconds: int

    terminateCollaborateAfterGracePeriod: bool

    collaborateGracePeriod: CollaborateGracePeriodDuration

    enableActiveCollaborateNotification: bool

    collaborateFromAddress: Optional[str] = None


@dataclass
class SystemCommunicationBarringAlternateCallIndicatorGetListResponse(OCIDataResponse):
    """Response to a SystemCommunicationBarringAlternateCallIndicatorGetListRequest. Contains a table with one row per Communication Barring Alternate Call Indicator.  The table column headings are: \"Alternate Call Indicator\" and \"Network Server Alternate Call Indicator\"."""

    alternateCallIndicatorTable: OCITable


@dataclass
class SystemCommunicationBarringCallTypeGetListResponse(OCIDataResponse):
    """Response to a SystemCommunicationBarringCallTypeGetListRequest. Contains a table with one row per Communication Barring Call Type.  The table column headings are: \"Call Type\" and \"Network Server Call Type\"."""

    callTypeTable: OCITable


@dataclass
class SystemCommunicationBarringCriteriaGetListResponse(OCIDataResponse):
    """Response to the SystemCommunicationBarringCriteriaGetListRequest.
    The response contains a table of all Communication Barring Criteria
    in the system. The column headings are \"Name\" and \"Description\"."""

    criteriaTable: OCITable


@dataclass
class SystemCommunicationBarringCriteriaGetResponse19sp1(OCIDataResponse):
    """Response to the SystemCommunicationBarringCriteriaGetRequest19sp1.
    The response contains the Communication Barring Criteria information."""

    matchPublicNetwork: bool

    matchPrivateNetwork: bool

    matchLocalCategory: bool

    matchNationalCategory: bool

    matchInterlataCategory: bool

    matchIntralataCategory: bool

    matchInternationalCategory: bool

    matchPrivateCategory: bool

    matchEmergencyCategory: bool

    matchOtherCategory: bool

    matchInterNetwork: bool

    matchInterHostingNE: bool

    matchInterAS: bool

    matchIntraAS: bool

    matchChargeCalls: bool

    matchNoChargeCalls: bool

    matchGroupCalls: bool

    matchEnterpriseCalls: bool

    matchNetworkCalls: bool

    matchNetworkURLCalls: bool

    matchRepairCalls: bool

    matchEmergencyCalls: bool

    matchInternalCalls: bool

    matchLocation: str

    matchRoaming: str

    description: Optional[str] = None

    matchCallType: List[str] = field(default_factory=list)

    matchAlternateCallIndicator: List[str] = field(default_factory=list)

    matchVirtualOnNetCallType: List[str] = field(default_factory=list)

    timeSchedule: Optional[str] = None

    holidaySchedule: Optional[str] = None

    matchNumberPortabilityStatus: List[str] = field(default_factory=list)


@dataclass
class SystemCommunicationBarringDigitPatternCriteriaGetListResponse(OCIDataResponse):
    """Response to the SystemCommunicationBarringDigitPatternCriteriaGetListRequest.
    The response contains a table of all Digit Pattern Criteria defined at the system level. The column headings are \"Name\" and \"Description\" """

    criteriaTable: OCITable


@dataclass
class SystemCommunicationBarringDigitPatternCriteriaGetPatternListResponse(
    OCIDataResponse
):
    """Response to the SystemCommunicationBarringDigitPatternCriteriaGetPatternListRequest.
    The response contains the Digit Pattern Criteria information."""

    matchDigitPattern: List[str] = field(default_factory=list)


@dataclass
class SystemCommunicationBarringDigitPatternCriteriaGetResponse(OCIDataResponse):
    """The response to a SystemCommunicationBarringDigitPatternCriteriaGetRequest."""

    description: Optional[str] = None

    digitPattern: List[str] = field(default_factory=list)


@dataclass
class SystemCommunicationBarringGetResponse21sp1(OCIDataResponse):
    """Response to SystemCommunicationBarringGetRequest21sp1.
    The following elements are only used in AS data mode:
    vmCallbackScreening, value \"false\" is returned in XS data mode."""

    directTransferScreening: bool

    vmCallbackScreening: bool


@dataclass
class SystemCommunicationBarringIncomingCriteriaGetListResponse(OCIDataResponse):
    """Response to the SystemCommunicationBarringIncomingCriteriaGetListRequest.
    The response contains a table of all Communication Barring Incoming Criteria
    in the system. The column headings are \"Name\" and \"Description\"."""

    criteriaTable: OCITable


@dataclass
class SystemCommunicationBarringIncomingCriteriaGetResponse22(OCIDataResponse):
    """Response to the SystemCommunicationBarringIncomingCriteriaGetRequest.
    The response contains the Communication Barring Incoming Criteria information."""

    callTaggedAsSpam: bool

    description: Optional[str] = None

    timeSchedule: Optional[str] = None

    holidaySchedule: Optional[str] = None

    matchNumberPortabilityStatus: List[str] = field(default_factory=list)


@dataclass
class SystemCommunicationBarringProfileGetCriteriaUsageListResponse(OCIDataResponse):
    """Response to the SystemCommunicationBarringProfileGetCriteriaUsageListRequest.
    The response contains a table of system Communication Barring Profiles that
    use the specific Communication Barring Criteria. The column headings
    are \"Name\" and \"Description\" """

    profileTable: OCITable


@dataclass
class SystemCommunicationBarringProfileGetDigitPatternCriteriaUsageListResponse(
    OCIDataResponse
):
    """Response to the SystemCommunicationBarringProfileGetDigitPatternCriteriaUsageListRequest.
    The response contains a table of all Profiles that use the specific Digit Pattern Criteria. The column headings are \"Name\" and \"Description\" """

    profileTable: OCITable


@dataclass
class SystemCommunicationBarringProfileGetIncomingCriteriaUsageListResponse(
    OCIDataResponse
):
    """Response to the SystemCommunicationBarringProfileGetIncomingCriteriaUsageListRequest.
    The response contains a table of system Communication Barring Profiles that
    use the specific Communication Barring Incoming Criteria. The column headings
    are \"Name\" and \"Description\" """

    profileTable: OCITable


@dataclass
class SystemCommunicationBarringProfileGetListResponse(OCIDataResponse):
    """Response to the SystemCommunicationBarringProfileGetListRequest.
    The response contains a table of all Communication Barring Profiles
    in the system. The column headings are \"Name\" and \"Description\" """

    profileTable: OCITable


@dataclass
class SystemCommunicationBarringProfileGetResponse19sp1V2(OCIDataResponse):
    """Response to the SystemCommunicationBarringProfileGetRequest19sp1V2.
     The response contains the Communication Barring Profile information.
     The incoming rules are returned in ascending priority order.
     The following elements are only used in AS data mode:
        callMeNowDefaultAction
        callMeNowDefaultCallTimeout
        callMeNowRule
    applyToAttendedCallTransfers"""

    originatingDefaultAction: str

    redirectingDefaultAction: str

    incomingDefaultAction: str

    callMeNowDefaultAction: str

    applyToAttendedCallTransfers: bool

    description: Optional[str] = None

    originatingDefaultTreatmentId: Optional[str] = None

    originatingDefaultTransferNumber: Optional[str] = None

    originatingDefaultCallTimeout: Optional[int] = None

    originatingRule: List[CommunicationBarringOriginatingRule] = field(
        default_factory=list
    )

    redirectingDefaultCallTimeout: Optional[int] = None

    redirectingRule: List[CommunicationBarringRedirectingRule] = field(
        default_factory=list
    )

    incomingDefaultCallTimeout: Optional[int] = None

    incomingRule: List[CommunicationBarringIncomingRule19sp1] = field(
        default_factory=list
    )

    callMeNowDefaultCallTimeout: Optional[int] = None

    callMeNowRule: List[CommunicationBarringCallMeNowRule] = field(default_factory=list)


@dataclass
class SystemCommunicationBarringServiceProviderGetCriteriaUsageListResponse(
    OCIDataResponse
):
    """Response to the SystemCommunicationBarringServiceProviderGetCriteriaUsageListRequest.
    The response contains a table of all Service Providers that use the specific Communication Barring criteria. The column headings are \"Service Provider Id\", \"Service Provider Name\" and \"Is Enterprise\" """

    serviceProviderTable: OCITable


@dataclass
class SystemCommunicationBarringServiceProviderGetIncomingCriteriaUsageListResponse(
    OCIDataResponse
):
    """Response to the SystemCommunicationBarringServiceProviderGetIncomingCriteriaUsageListRequest.
    The response contains a table of all Service Providers that use the specific Communication Barring Incoming criteria. The column headings are \"Service Provider Id\", \"Service Provider Name\" and \"Is Enterprise\" """

    serviceProviderTable: OCITable


@dataclass
class SystemCommunicationBarringUserControlGetResponse(OCIDataResponse):
    """Response to the SystemCommunicationBarringUserControlGetRequest.
    Contains the settings to whole system for Communication Barring User-Control"""

    enableLockout: bool

    maxNumberOfFailedAttempts: int

    lockoutMinutes: int


@dataclass
class SystemConfigurableFileSystemGetResponse23V2(OCIDataResponse):
    """Response to SystemConfigurableFileSystemGetRequest23V2.
    Contains the File System parameters.
    The following elements are only used in AS data mode:
        protocolFile-secure
    value \"false\" is returned in XS data mode"""

    mediaDirectory: str

    protocolFile: object

    protocolWebDAV: object


@dataclass
class SystemConfigurableTreatmentGetListResponse(OCIDataResponse):
    """Response to a SystemConfigurableTreatmentGetListRequest. Contains a table with one row per treatment.
    The table columns are: \"Treatment Id\", \"Description\"."""

    treatmentTable: OCITable


@dataclass
class SystemConfigurableTreatmentGetResponse24(OCIDataResponse):
    """Response to the SystemConfigurableTreatmentGetRequest24.
    The response contains the treatment configurable information.

    The following elements are only used in AS data mode and not returned in XS data mode:
      warnCode
      warnText

    The following elements are only used in AS data mode:
      accessSendWarningHeader, value \"false\" is returned in XS data mode
      networkSendWarningHeader, value \"false\" is returned in XS data mode"""

    chargeIndicator: str

    routeAdvance: bool

    accessSendReasonHeader: bool

    networkSendReasonHeader: bool

    accessSendWarningHeader: bool

    networkSendWarningHeader: bool

    description: Optional[str] = None

    accessSIPStatusCode: Optional[int] = None

    accessSIPStatusMessage: Optional[str] = None

    networkSIPStatusCode: Optional[int] = None

    networkSIPStatusMessage: Optional[str] = None

    q850CauseValue: Optional[int] = None

    q850Text: Optional[str] = None

    accessTreatmentAudioFile: Optional[str] = None

    accessTreatmentVideoFile: Optional[str] = None

    networkTreatmentAudioFile: Optional[str] = None

    networkTreatmentVideoFile: Optional[str] = None

    cdrTerminationCause: Optional[str] = None

    internalReleaseCause: Optional[str] = None

    warnCode: Optional[int] = None

    warnText: Optional[str] = None


@dataclass
class SystemConnectedLineIdentificationPresentationGetResponse(OCIDataResponse):
    """Response to SystemConnectedLineIdentificationPresentationGetRequest."""

    enforceUserServiceAssignment: bool


@dataclass
class SystemCountryCodeGetListResponse(OCIDataResponse):
    """Response to a SystemCountryCodeGetListRequest. Contains the default country code
    and a table with one row per country code.  The table columns are
    \"Country Code\", \"Country Name\", \"Off Hook Warning Seconds\",
    \"Ring Period Milliseconds\", \"National Prefix\", \"Use Prefix\",
    \"Maximum Call Waiting Tones\", \"Time Between Call Waiting Tones Milliseconds\"
    and \"Disable National Prefix for OffNet Calls\".

    The following columns are only returned in AS data mode:
      \"Disable National Prefix for OffNet Calls\" """

    defaultCountryCode: str

    countryCodeTable: OCITable


@dataclass
class SystemCrInterfaceGetResponse22(OCIDataResponse):
    """Response to the SystemCrInterfaceGetRequest22."""

    crAuditEnabled: bool

    crAuditIntervalMilliseconds: int

    crAuditTimeoutMilliseconds: int

    crConnectionEnabled: bool

    crConnectionTimeoutMilliseconds: int

    crTcpConnectionTimeoutSeconds: int

    crNumberOfReconnectionAttempts: int


@dataclass
class SystemCustomerOriginatedTraceGetResponse(OCIDataResponse):
    """Response to SystemCustomerOriginatedTraceGetRequest."""

    screenMaliciousCallers: bool


@dataclass
class SystemDTMFTransmissionGetResponse(OCIDataResponse):
    """Response to the SystemDTMFTransmissionGetRequest."""

    transmissionMethod: str

    signalingContentType: Optional[str] = None


@dataclass
class SystemDeviceActivationPolicyGetResponse(OCIDataResponse):
    """Response to SystemDeviceActivationPolicyGetRequest."""

    allowActivationCodeRequestByUser: bool

    sendActivationCodeInEmail: bool


@dataclass
class SystemDeviceFamilyExportResponse(OCIDataResponse):
    """Response to SystemDeviceFamilyExportRequest."""

    file: str


@dataclass
class SystemDeviceFamilyGetListResponse(OCIDataResponse):
    """Response to SystemDeviceFamilyGetListRequest.
    The response includes a table of device family defined in the system.
    Column headings are: \"Device Family Name\", \"Reseller Id\".

    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    deviceFamilyTable: OCITable


@dataclass
class SystemDeviceFamilyGetResponse(OCIDataResponse):
    """Response to SystemDeviceFamilyGetRequest.
    The response includes the tag sets and device types associated to a device family defined in the system.
    Column headings for deviceTypeTable are : Device Type(s)
    Column headings for tagSetTable are :Tag Set(s)"""

    deviceTypeTable: OCITable

    tagSetTable: OCITable


@dataclass
class SystemDeviceFamilyImportDryRunResponse(OCIDataResponse):
    """Response to SystemDeviceFamilyImportDryRunRequest."""

    file: str

    differenceFound: bool


@dataclass
class SystemDeviceManagementAutoRebuildConfigGetListResponse(OCIDataResponse):
    """Response to SystemDeviceManagementAutoRebuildConfigGetListRequest.
    Contains a table with column headings: \"OCI Request Prefix\", \"Auto Rebuild Enabled\".
    \"OCI Request Prefix\" is the prefix of the OCI request name.  It does
    not include the request's version '17.sp4, 18...' since the disabled
    flag applies to the whole series of requests, independent of the
    version.
    \"Auto Rebuild Enabled\": 'True' if the request prefix triggers DM events
    automatically.  Otherwise, automatic DM events are not generated."""

    autoRebuildConfigTable: OCITable


@dataclass
class SystemDeviceManagementEventGetListResponse22(OCIDataResponse):
    """Response to SystemDeviceManagementEventGetListRequest22.
    Contains a table with column headings: \"Event Id\", \"Status\", \"Action\",
    \"Level\", \"Type\", \"Additional Info\", \"Is Local\", \"Completion %\",
    \"Pushed/ Same Hash/ Not Pushed\", \"Login Id\", \"Start Time\",
    \"Process Time\", \"Rx Time\", \"Total Time\", \"Request\", \"Priority\",
    \"Tracking Id\", \"End Time\".
    \"Event Id\" is a unique identifier for the event.
    \"Status\" can be: Pending, Queued, In Progress,
    Process On Other Host, Stale, Completed, Canceled.
    \"Action\" can be: Delete, Download, Rebuild, Reset, Upload.
    \"Level\" can be: Device, Device Type, Device Type Group, Group, User.
    \"Type\" can be: Automatic, Manual.
    \"Additional Info\" includes the affected device type, device or group.
    It depends on the level of the event:
      Device Profile: \"Device Name\" \"Service Provider Id\" \"Group Id\"
      Device Type: \"Device Type Name\"
      Device Type Service Provider: \"Service Provider Id\" \"Device Type Name\"
      Service Provider: \"Service Provider Id\"
      Device Type Group: \"Service Provider Id\" \"Group Id\" \"Device Type Name\"
      Group: \"Service Provider Id\" \"Group Id\"
      User: \"User Id\"
    \"Is Local\" is set to \"yes\" if the event is processed on the server
    who received the request, \"no\" otherwise meaning that the event is
    processed on another server.
    \"Completion %\" provides an estimate of the completion of the event.
    A percentage is given, the current number of completed expanded event,
    and the total number of expanded event.
    \"Pushed/ Same Hash/ Not Pushed\" gives the total number of files that
    were pushed, not pushed because of same hash, and not pushed when
    processing the event.
    \"LoginId\" is the user or admin id who triggered the event.
    \"Start Time\" is the date when the event's processing started.  The
    display shows the month, day, hours, minutes, and seconds (MM-dd hh:mm:ss).
    \"Process Time\" is the time taken to process the event in hours,
    minutes, seconds, and milliseconds (hhhh:mm:ss.SSS).
    \"Rx Time\" is the date when the event was received via OCI-P and
    stored in the system.  The display shows the month, day, hours,
    minutes, and seconds (MM-dd hh:mm:ss).
    \"Total Time\" is the total time the event was in the system, from the
    moment it was received and stored until its processing ended, in
    hours, minutes, seconds, and milliseconds (hhhh:mm:ss.SSS).
    \"Request\" is the name of the OCI-P request that triggered the event.
    \"Priority\" is the priority of the event.
    \"Tracking Id\" is the tracking id of the OCI-P request that triggered the event.
    \"End Time\" is the difference, measured in milliseconds, between the
    event's end time and midnight, January 1, 1970 UTC"""

    eventTable: OCITable


@dataclass
class SystemDeviceManagementGetAccessDeviceCountForDeviceTypeResponse(OCIDataResponse):
    """Response to SystemDeviceManagementGetAccessDeviceCountForDeviceTypeRequest."""

    accessDeviceCount: int


@dataclass
class SystemDeviceManagementGetEventStatusSummaryCountResponse(OCIDataResponse):
    """Response to SystemDeviceManagementGetEventStatusSummaryCountRequest.
    The column headings are \"Action, \"Pending\", \"Queued Internally\", and \"Completed\" """

    statusCountTable: OCITable


@dataclass
class SystemDeviceManagementTagGetListResponse(OCIDataResponse):
    """Response to SystemDeviceManagementTagGetListRequest.
    Contains a table of custom configuration tags managed by the Device Management System.
    In AS data mode, the column headings are: \"Tag Name\", \"Tag Value\", \"Is Overridable\".
    In XS data mode, the column headings are: \"Tag Name\", \"Tag Value\", \"Is Overridable\", \"Is Encrypted\"."""

    tagsTable: OCITable


@dataclass
class SystemDeviceManagementTagSetCountryGetListResponse(OCIDataResponse):
    """Response to SystemDeviceManagementTagSetCountryGetListRequest.
    The response includes the list of countries defined in a region of a specified tag set."""

    countryName: List[str] = field(default_factory=list)


@dataclass
class SystemDeviceManagementTagSetExportResponse(OCIDataResponse):
    """Response to SystemDeviceManagementTagSetExportRequest."""

    file: str


@dataclass
class SystemDeviceManagementTagSetGetListResponse22(OCIDataResponse):
    """Response to SystemDeviceManagementTagSetGetListRequest22.
    The response includes a table of tag set names defined in the system.
    Column headings are: \"Tag Set Name\", \"Reseller Id\".

    The following columns are only returned in AS data mode:
      \"Reseller Id\"
    The system default tag set name is not part of this response."""

    tagSetTable: OCITable


@dataclass
class SystemDeviceManagementTagSetImportDryRunResponse(OCIDataResponse):
    """Response to SystemDeviceManagementTagSetImportDryRunRequest."""

    file: str

    differenceFound: bool


@dataclass
class SystemDeviceManagementTagSetRegionGetListResponse(OCIDataResponse):
    """Response to SystemDeviceManagementTagSetGetListRequest.
    The response includes the list of region names defined in the specified tag set."""

    regionName: List[str] = field(default_factory=list)


@dataclass
class SystemDeviceManagementTagSetRegionTagGetListResponse(OCIDataResponse):
    """Response to SystemDeviceManagementTagSetRegionTagGetListRequest.
    The column headings for the tagsTable are: \"Tag Name\", \"Tag Value\"."""

    tagsTable: OCITable


@dataclass
class SystemDeviceProfileAuthenticationLockoutGetResponse(OCIDataResponse):
    """Response to SystemDeviceProfileAuthenticationLockoutGetRequest.
    The column headings for the lockoutTable are: \"Organization Id\", \"Organization Type\", \"Group Id\", \"Identity/Device Profile Name\",  \" Identity/Device Profile Type\",  \"Lockout Started\", \"Lockout Expires\", \"Lockout Count\". Lockout times are shown in the system GMT time. When a permanent lockout is shown, the \"Lockout Expires\" column is empty and the \"Lockout Count\" column contains the word Permanent."""

    lockoutTable: OCITable


@dataclass
class SystemDeviceProfileAuthenticationPasswordRulesGetResponseRI(OCIDataResponse):
    """Response to SystemDeviceProfileAuthenticationPasswordRulesGetRequestRI.
    Contains the device profile authentication password rules for the system."""

    disallowAuthenticationName: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    sendPermanentLockoutNotification: bool

    deviceProfileAuthenticationLockoutType: str

    deviceProfileTemporaryLockoutThreshold: int

    deviceProfileWaitAlgorithm: str

    deviceProfileLockoutFixedMinutes: str

    deviceProfilePermanentLockoutThreshold: int

    usePasswordValidationService: bool

    permanentLockoutNotifyEmailAddress: Optional[str] = None


@dataclass
class SystemDeviceTypeExportResponse(OCIDataResponse):
    """Response to SystemDeviceTypeExportRequest."""

    file: str


@dataclass
class SystemDeviceTypeGetAvailableListResponse22V2(OCIDataResponse):
    """Response to SystemDeviceTypeGetAvailableListRequest22V2.

    Note: element numberOfPorts is only used by devices types with static line ordering enabled"""

    deviceType: List[str] = field(default_factory=list)

    typeInfo: List[object] = field(default_factory=list)


@dataclass
class SystemDeviceTypeGetResponse22V7(OCIDataResponse):
    """Response to SystemDeviceTypeGetRequest22V7.

    The following elements are only used in AS data mode:
      resellerId"""

    isObsolete: bool

    profile: str

    staticRegistrationCapable: bool

    isIpAddressOptional: bool

    useDomain: bool

    isMobilityManagerDevice: bool

    webBasedConfigURL: Optional[str] = None

    cpeDeviceOptions: Optional[CPEDeviceOptionsRead22V6] = None

    protocolChoice: List[str] = field(default_factory=list)

    deviceTypeConfigurationOption: Optional[str] = None

    staticLineOrdering: Optional[bool] = None

    resellerId: Optional[str] = None


@dataclass
class SystemDeviceTypeImportDryRunResponse(OCIDataResponse):
    """Response to SystemDeviceTypeImportDryRunRequest."""

    file: str

    differenceFound: bool


@dataclass
class SystemDialPlanPolicyGetAccessCodeListResponse(OCIDataResponse):
    """Response to SystemDialPlanPolicyGetAccessCodeListRequest.
    Contains a table with column headings: \"Access Code\", \"Enable Secondary Dial Tone\", \"Description\" """

    accessCodeTable: OCITable


@dataclass
class SystemDialPlanPolicyGetAccessCodeResponse(OCIDataResponse):
    """Response to SystemDialPlanPolicyGetAccessCodeRequest"""

    includeCodeForNetworkTranslationsAndRouting: bool

    includeCodeForScreeningServices: bool

    enableSecondaryDialTone: bool

    description: Optional[str] = None


@dataclass
class SystemDialPlanPolicyGetResponse22V2(OCIDataResponse):
    """Response to SystemDialPlanPolicyGetRequest22V2
    The following elements are only used in AS data mode:
      overrideResolvedDeviceDigitMap
    The following elements are only used in AS data mode and not returned in XS data mode:
      deviceDigitMap
      performInternalTranslationsWithOAC
      permissiveOACDialing"""

    requiresAccessCodeForPublicCalls: bool

    allowE164PublicCalls: bool

    preferE164NumberFormatForCallbackServices: bool

    publicDigitMap: str

    overrideResolvedDeviceDigitMap: bool

    privateDigitMap: Optional[str] = None

    deviceDigitMap: Optional[str] = None

    performInternalTranslationsWithOAC: Optional[bool] = None

    permissiveOACDialing: Optional[bool] = None


@dataclass
class SystemDialableCallerIDCriteriaGetResponse(OCIDataResponse):
    """Response to the SystemDialableCallerIDCriteriaGetRequest.
    The response contains the Dialable Caller ID Criteria information."""

    matchLocalCategory: bool

    matchNationalCategory: bool

    matchInterlataCategory: bool

    matchIntralataCategory: bool

    matchInternationalCategory: bool

    matchPrivateCategory: bool

    matchEmergencyCategory: bool

    matchOtherCategory: bool

    description: Optional[str] = None

    prefixDigits: Optional[str] = None

    matchCallType: List[str] = field(default_factory=list)

    matchAlternateCallIndicator: List[str] = field(default_factory=list)


@dataclass
class SystemDialableCallerIDGetResponse(OCIDataResponse):
    """Response to the SystemDialableCallerIDGetRequest.
    The criteria table?s column headings are ?Active?, \"Name\", \"Description\", ?Prefix Digits?, and ?Priority?."""

    criteriaTable: OCITable


@dataclass
class SystemDigitCollectionGetResponse13mp4(OCIDataResponse):
    """Response to SystemDigitCollectionGetRequest13mp4."""

    publicDigitMap: str

    accessCode: Optional[str] = None

    privateDigitMap: Optional[str] = None


@dataclass
class SystemDnGetSummaryListResponse(OCIDataResponse):
    """Response to SystemDnGetSummaryListRequest.
    The column headings are \"Phone Numbers, \"Service Provider Id\", \"Is Enterprise\" and \"Reseller Id\".

    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    dnSummaryTable: OCITable


@dataclass
class SystemDnGetUtilizationListResponse(OCIDataResponse):
    """Response to SystemDnUtilizationGetListRequest.
    The table columns are: \"Service Provider Id\", \"Phone Numbers\", \"Assigned to Groups\",
    \"Percentage Assigned\", \"Is Enterprise\", \"Activated on Groups\", \"Reseller Id\".

        The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    dnUtilizationTable: OCITable


@dataclass
class SystemDnGetUtilizationResponse14sp3(OCIDataResponse):
    """Response to SystemDnGetUtilizationRequest14sp3.
          The isActivated element is only included when the DN is
    assigned to a user."""

    serviceProviderId: str

    isGroupCallingLineId: bool

    groupId: Optional[str] = None

    userId: Optional[str] = None

    userType: Optional[str] = None

    isActivated: Optional[bool] = None


@dataclass
class SystemDomainGetAssignedServiceProviderListResponse(OCIDataResponse):
    """Response to SystemDomainGetAssignedServiceProviderListRequest.
    The table columns are: \"Service Provider Id\", \"Service Provider Name\", \"Is Enterprise\" and \"Reseller Id\".
    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    serviceProviderTable: OCITable


@dataclass
class SystemDomainGetListResponse22V2(OCIDataResponse):
    """Contains a table of all matching system-level domain names and all matching reseller level domains.
    The column headings are: \"Domain Name\" and \"Reseller Id\"."""

    domainTable: OCITable

    systemDefaultDomain: Optional[str] = None


@dataclass
class SystemDomainParametersGetResponse(OCIDataResponse):
    """Response to SystemDomainParametersGetRequest.
    Contains the system Domain parameters.

    The following elements are only used in AS data mode:
      useAliasForDomain, value \"false\" is returned in XS data mode."""

    useAliasForDomain: bool

    defaultDomain: Optional[str] = None


@dataclass
class SystemEmergencyCallDDoSProtectionGetResponse(OCIDataResponse):
    """Response to the SystemEmergencyCallDDoSProtectionGetRequest."""

    enabled: bool

    sampleIntervalSeconds: int

    protectionAction: str

    protectionRate: Optional[int] = None


@dataclass
class SystemEmergencyCallNotificationGetResponse(OCIDataResponse):
    """Response to SystemEmergencyCallNotificationGetResponse."""

    defaultFromAddress: str


@dataclass
class SystemEmergencyZonesGetResponse(OCIDataResponse):
    """Response to SystemEmergencyZonesGetRequest."""

    defaultFromAddress: str


@dataclass
class SystemEndpointGetListResponse(OCIDataResponse):
    """Response to SystemEndpointGetListRequest.
    The column headings for the endpointTable are: \"Organization Id\", \"Organization Type\", \"Group Id\", \"Line/Port\", \"Last Name\",\"First Name\", \"User Id\", \"User Type\", \"Phone Number\", \"Extension\", \"Device Type\", \"Device Name\", \"Net Address\", \"MAC Address\", \"Department\", \"Email Address\", \"Reseller Id\".
    Possible values for User Type are \"User\", \"CCBasic\", \"CCStandard\", \"CCPremium\", \"RP\", \"MOH\", \"MOHVideo\".

    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    endpointTable: OCITable


@dataclass
class SystemEnhancedCallLogsActiveSchemaInstanceGetListResponse(OCIDataResponse):
    """Response to SystemEnhancedCallLogsSchemaInstanceActualUsageGetListRequest.
    Contains a table with column headings: \"Instance Name\", \"Active Users\"."""

    schemaInstanceUsageTable: OCITable


@dataclass
class SystemEnhancedCallLogsGetResponse22V2(OCIDataResponse):
    """Response to SystemEnhancedCallLogsGetRequest22V2."""

    maxNonPagedResponseSize: int

    defaultSchema: Optional[str] = None

    eclQueryApplicationURL: Optional[str] = None

    eclQueryDataRepositoryURL: Optional[str] = None


@dataclass
class SystemEnhancedCallLogsSchemaInstanceGetListResponse(OCIDataResponse):
    """Response to SystemEnhancedCallLogsSchemaInstanceGetListRequest.
    Contains a table with column headings: \"Instance Name\", \"Actual Users\", \"Potential Users\"."""

    schemaInstanceUsageTable: OCITable


@dataclass
class SystemEnterpriseTrunkGetResponse(OCIDataResponse):
    """Response to SystemEnterpriseTrunkGetRequest."""

    enableHoldoverOfHighwaterCallCounts: bool

    holdoverPeriod: str

    timeZoneOffsetMinutes: str


@dataclass
class SystemExecutiveGetResponse24(OCIDataResponse):
    """Response to SystemExecutiveGetRequest."""

    treatVirtualOnNetCallsAsInternal: bool

    considerExecutiveOnHookForAssistantCalls: bool


@dataclass
class SystemExpensiveCallNotificationGetResponse(OCIDataResponse):
    """Response to SystemExpensiveCallNotificationGetRequest."""

    enablePostAnnouncementDelayTimer: bool

    postAnnouncementDelaySeconds: int


@dataclass
class SystemExpensiveCallTypeGetListResponse16sp1(OCIDataResponse):
    """Response to SystemExpensiveCallTypeGetListRequest16sp1.
    The column headings are:
    \"Alternate Call Indicator\", \"Treatment Audio File\"."""

    alternateCallIndicatorTable: OCITable


@dataclass
class SystemExtensionLengthGetResponse(OCIDataResponse):
    """Response to SystemExtensionLengthGetRequest."""

    minExtensionLength: int

    maxExtensionLength: int


@dataclass
class SystemExternalAuthenticationGetACLListResponse(OCIDataResponse):
    """Response to SystemExternalAuthenticationGetACLListRequest. The table columns are:
    \"Net Address\" and \"Description\"."""

    aclTable: OCITable


@dataclass
class SystemExternalEmergencyRoutingParametersGetResponse13mp13(OCIDataResponse):
    """Response to SystemExternalEmergencyRoutingParametersGetRequest13mp13.
    Contains a list of system External Emergency Routing parameters."""

    isActive: bool

    supportsDNSSRV: bool

    connectionTimeoutSeconds: int

    serviceURI: Optional[str] = None

    defaultEmergencyNumber: Optional[str] = None


@dataclass
class SystemFaxMessagingGetResponse(OCIDataResponse):
    """Response to SystemFAXMessagingGetRequest.

    The following elements are only used in AS data mode:
       statusDurationHours
       statusAuditIntervalHours"""

    statusDurationHours: int

    statusAuditIntervalHours: int

    maximumConcurrentFaxesPerUser: int


@dataclass
class SystemFeatureAccessCodeGetListResponse21(OCIDataResponse):
    """Response to the SystemFeatureAccessCodeGetListRequest21.

    In release 20 the \"Call Recording\" FAC name is changed to
    \"Call Recording - Start\"."""

    featureAccessCode: List[FeatureAccessCodeReadEntry] = field(default_factory=list)


@dataclass
class SystemFileGetContentResponse(OCIDataResponse):
    """Response to a SystemFileGetContentRequest. The fileContent length returned is limited to 128KBytes."""

    fileContent: int


@dataclass
class SystemFileRepositoryDeviceGetListResponse(OCIDataResponse):
    """Response to SystemFileRepositoryDeviceGetListRequest.
    Contains a table with column headings : \"Name\",\"Protocol\", \"Root Directory\", \"Extended File Capture Support\" in a row for each file repository."""

    fileRepositoryTable: OCITable


@dataclass
class SystemFileRepositoryDeviceGetResponse22(OCIDataResponse):
    """Response to SystemFileRepositoryDeviceGetRequest22."""

    protocolWebDAV: FileRepositoryProtocolWebDAV20

    protocolFTP: FileRepositoryProtocolFTP16

    protocolSFTP: FileRepositoryProtocolFTP16

    protocolFTPS: FileRepositoryProtocolFTP16

    rootDirectory: Optional[str] = None

    port: Optional[int] = None


@dataclass
class SystemFileRepositoryDeviceUserGetListResponse(OCIDataResponse):
    """Response to SystemFileRepositoryDeviceUserGetListRequest.
    Contains a table with column headings : \"User Name\",\"Allow Get\",\"Allow Delete\",\"Allow Put\" in a row for each file repository user."""

    fileRepositoryUserTable: OCITable


@dataclass
class SystemFileRepositoryDeviceUserGetResponse(OCIDataResponse):
    """Response to SystemFileRepositoryDeviceUserGetRequest."""

    allowPut: bool

    allowDelete: bool

    allowGet: bool


@dataclass
class SystemGETSAvpCodeMapGetListResponse(OCIDataResponse):
    """Response to SystemGETSAvpCodeMapGetListRequest.
    The table columns are: \"AVP Code\" and \"Vendor ID\"."""

    avpCodeTable: OCITable


@dataclass
class SystemGETSGetResponse22(OCIDataResponse):
    """Response to SystemGETSGetRequest22."""

    enabled: bool

    enableRequireResourcePriority: bool

    sendAccessResourcePriority: bool

    callIdentifierMode: str

    defaultPriorityAVP: int

    signalingDSCP: int

    defaultRValue: str

    bypassRoRelease: bool

    ignoreResourcePrioritiesWhenGETSDisabled: bool


@dataclass
class SystemGETSNumberGetListResponse(OCIDataResponse):
    """Response to SystemGETSNumberGetListRequest.
    The table columns are: \"Number\", \"Type\" and \"Description\"."""

    reservedNumberTable: OCITable


@dataclass
class SystemGETSReservedFeatureAccessCodeGetListResponse(OCIDataResponse):
    """Response to SystemGETSReservedFeatureAccessCodeGetListRequest.
    The table columns are: \"Code\" and \"Description\"."""

    reservedCodeTable: OCITable


@dataclass
class SystemGETSResourcePriorityGetListResponse(OCIDataResponse):
    """Response to SystemGETSResourcePriorityGetListRequest.
    The table columns are: \"Priority Value\", \"Priority Level\" and \"Priority Class\"."""

    resourcePriorityTable: OCITable


@dataclass
class SystemGETSSessionPriorityMapGetListResponse(OCIDataResponse):
    """Response to SystemGETSSessionPriorityMapGetListRequest.
    The table columns are: \"Priority Level\" and \"Session Priority Value\"."""

    sessionPriorityTable: OCITable


@dataclass
class SystemGeographicRedundancyPeerSipConnectionMonitoringGetResponse(OCIDataResponse):
    """Response to SystemGeographicRedundancyPeerSipConnectionMonitoringGetRequest.
    Contains a list of Peer SIP Connection Monitoring system parameters."""

    enabled: bool

    heartbeatInterval: int

    heartbeatTimeout: int


@dataclass
class SystemGeographicRedundancyProxyGetResponse(OCIDataResponse):
    """Response to SystemGeographicRedundancyProxyGetRequest.
    Contains a list of Geographic Redundancy Proxy system parameters."""

    enabled: bool


@dataclass
class SystemGeographicRedundancyUnreachableFromPrimaryGetUserListResponse22(
    OCIDataResponse
):
    """Response to SystemGeographicRedundancyUnreachableFromPrimaryGetUserListRequest22.
    The Unreachable From Primary User table column headings are: \"User ID\", \"Lineport\".
    The optional totalNumberOfUnreachableFromPrimaryUsers is returned only when the userListSizeLimit is set in the request and
    if the total number of unreachable from primary users is greater than the value of userListSizeLimit."""

    unreachableFromPrimaryUserTable: OCITable

    totalNumberOfUnreachableFromPrimaryUsers: Optional[int] = None


@dataclass
class SystemGetAvailableLeafDeviceListResponse22(OCIDataResponse):
    """Response to SystemGetAvailableLeafDeviceListRequest22."""

    leafDeviceKey: List[AccessDeviceKey] = field(default_factory=list)

    supportLinks: List[str] = field(default_factory=list)


@dataclass
class SystemGetAvailableTreeDeviceListResponse(OCIDataResponse):
    """Response to SystemGetAvailableTreeDeviceListRequest."""

    treeDeviceInfo: List[TreeDeviceInfo] = field(default_factory=list)


@dataclass
class SystemGetRegistrationContactListResponse21sp1(OCIDataResponse):
    """Response to SystemGetRegistrationContactListRequest. The table columns are: \"Service Provider Id\", \"Group Id\", \"User Id\", \"Line/Port\",
    \"Endpoint Type\", \"Order\", \"URI\", \"Expiration\", \"Contact\", \"Device Level\", \"Device Name\", \"Public Net Address\",
    \"Public Port\", \"Private Net Address\", \"Private Port\", \"User Agent\", \"Reseller Id\", \"Path Header\".
    The Endpoint Type column contains one of the enumerated RegistrationEndpointType21sp1 values.
    The value Mobility in Endpoint Type column is only applicable in AS data mode.
    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    registrationTable: OCITable


@dataclass
class SystemGroupNightForwardingGetResponse(OCIDataResponse):
    """Response to SystemGroupNightForwardingGetRequest."""

    nightForwardInterGroupCallsWithinEnterprise: bool


@dataclass
class SystemHPBXAlternateCarrierSelectionGetCarrierListResponse(OCIDataResponse):
    """Response to the SystemHPBXAlternateCarrierSelectionGetCarrierListRequest.
    Contains a table with column headings:
     \"Carrier Name\", \"Carrier Prefix\", \"Carrier Domain\", \"Carrier Type\"
    The possible values for Carrier Type are \"Local And Distant\" and \"Distant\"."""

    HPBXAlternateCarriersTable: OCITable


@dataclass
class SystemHPBXMobileTerminationGetResponse(OCIDataResponse):
    """Response to the SystemHPBXMobileTerminationGetRequest.
    Contains the hPBX mobile termination related configuration parameters."""

    routingPrefix: Optional[str] = None


@dataclass
class SystemHomeNetworkGetListResponse(OCIDataResponse):
    """Response to the SystemHomeNetworkGetListRequest."""

    mscAddress: List[str] = field(default_factory=list)


@dataclass
class SystemHuntGroupGetResponse21(OCIDataResponse):
    """Response to SystemHuntGroupGetRequest21."""

    removeHuntGroupNameFromCLID: bool

    uniformCallDistributionPolicyScope: str

    allowAgentDeviceInitiatedForward: bool


@dataclass
class SystemInCallServiceActivationGetResponse17(OCIDataResponse):
    """Response to SystemInCallServiceActivationGetRequest17."""

    defaultFlashActivationDigits: str

    defaultCallTransferActivationDigits: str


@dataclass
class SystemIntegratedIMPGetResponse25(OCIDataResponse):
    """Response to the SystemIntegratedIMPGetRequest25.
    The response contains the system Integrated IMP service attributes.

    The following elements are only used in AS data mode:
      boshURL
      propagateImpErrorDetails"""

    addServiceProviderInIMPUserId: bool

    allowImpPasswordRetrieval: bool

    propagateImpErrorDetails: bool

    serviceDomain: Optional[str] = None

    servicePort: Optional[int] = None

    boshURL: Optional[str] = None


@dataclass
class SystemInterceptUserGetDnListResponse(OCIDataResponse):
    """Response to SystemInterceptUserGetDnListRequest.
    The Intercept User DN List."""

    interceptUserList: List[InterceptDNListEntry] = field(default_factory=list)


@dataclass
class SystemInterceptUserGetResponse(OCIDataResponse):
    """Response to the SystemInterceptUserGetRequest."""

    emergencyAndRepairIntercept: bool


@dataclass
class SystemInventoryReportGetResponse(OCIDataResponse):
    """Response to SystemInventoryReportGetRequest."""

    defaultFromAddress: str


@dataclass
class SystemLanguageGetListResponse(OCIDataResponse):
    """Response to SystemLanguageGetListRequest.
    The language table column headings are: \"Language\", \"Locale\" and \"Encoding\"."""

    defaultLanguage: str

    languageTable: OCITable


@dataclass
class SystemLegacyAutomaticCallbackGetLineTypeListResponse(OCIDataResponse):
    """Response to SystemLegacyAutomaticCallbackGetLineTypeListRequest. Returns a 3 column
    table with column headings: \"Line Type\", \"Match\" and \"No Match\". The possible values
    for the \"Match\" and \"No Match\" columns are \"Accept\" and \"Deny\"."""

    lineTypeTable: OCITable


@dataclass
class SystemLegacyAutomaticCallbackGetResponse(OCIDataResponse):
    """Response to SystemLegacyAutomaticCallbackGetRequest."""

    maxMonitorsPerOriginator: int

    maxMonitorsPerTerminator: int

    t2Minutes: int

    t4Seconds: int

    t5Seconds: int

    t6Minutes: int

    t7Minutes: int

    t8Seconds: int

    tRingSeconds: int

    t10OMinutes: int

    t10TMinutes: int


@dataclass
class SystemLicensingGetResponse21sp1(OCIDataResponse):
    """Response to SystemLicensingGetRequest21sp1. The subscriber license table columns are: \"Name\", \"Licensed\", \"Used\" and \"Available\".
    The group service license table columns are: \"Name\", \"Licensed\", \"Used\" and \"Available\".
    The virtual service license table columns are: \"Name\", \"Licensed\", \"Used\" and \"Available\".
    The user service license table columns are: \"Name\", \"Licensed\", \"Used\", \"Available\", \"Used By Hosted Users\", \"Used By Trunk Users\", and \"Expiration Date\".
    The system param license table columns are: \"Name\", \"Licensed\", \"Used\", Available\"."""

    licenseStrictness: str

    groupUserlimit: int

    numberOfTrunkUsers: int

    subscriberLicenseTable: OCITable

    groupServiceLicenseTable: OCITable

    virtualServiceLicenseTable: OCITable

    userServiceLicenseTable: OCITable

    systemParamLicenseTable: OCITable

    expirationDate: Optional[str] = None

    hostId: List[str] = field(default_factory=list)

    licenseName: List[str] = field(default_factory=list)

    systemId: Optional[str] = None


@dataclass
class SystemLicensingGetSystemLicenseListResponse22V2(OCIDataResponse):
    """Response to SystemLicensingGetSystemLicenseListRequest22V2."""

    license: List[str] = field(default_factory=list)


@dataclass
class SystemLocationBasedCallingRestrictionsGetResponse24(OCIDataResponse):
    """Response to SystemLocationBasedCallingRestrictionsGetRequest24."""

    physicalLocationIndicator: str

    enforceMscValidation: bool

    enableOfficeZoneAnnouncement: bool

    enhanceOfficeZone: bool

    enableMccMncBasedLocation: bool

    defaultMccMncBasedLocation: str

    mccMncRoamingNetworkTranslationIndex: Optional[str] = None


@dataclass
class SystemMGCPDeviceTypeGetListResponse(OCIDataResponse):
    """Response to SystemMGCPDeviceTypeGetListRequest.
    Contains a table of identity/ device profile types configured in the system.
    The column headings are: \"Device Type\", \"Profile\", \"Is Obsolete\"."""

    deviceTypeTable: OCITable


@dataclass
class SystemMGCPDeviceTypeGetResponse(OCIDataResponse):
    """Response to SystemMGCPDeviceTypeGetRequest."""

    isObsolete: bool

    profile: str

    numberOfPorts: UnboundedPositiveInt

    protocolChoice: List[str] = field(default_factory=list)


@dataclass
class SystemMailParametersGetResponse22(OCIDataResponse):
    """Response to SystemMailParametersGetListRequest22.
    Contains a list of system Mail parameters."""

    defaultFromAddress: str

    supportDNSSRVForMailServerAccess: bool

    secureMode: str

    primaryServerNetAddress: Optional[str] = None

    secondaryServerNetAddress: Optional[str] = None

    defaultSubject: Optional[str] = None

    port: Optional[int] = None


@dataclass
class SystemMaliciousCallTraceGetResponse(OCIDataResponse):
    """Response to the SystemMaliciousCallTraceGetRequest.
    The response contains the Malicious Call Trace system parameters and the list of users
    that use the Malicious Call Trace feature.

    The column headings are \"Service Provider Id\",
    \"Group Id\", \"User Id\", \"Last Name\", \"First Name\", \"Phone Number\", \"Trace Type\", \"Status\",
    \"Hiragana Last Name\" and \"Hiragana First Name\", \"Extension\", \"Department\", \"Email Address\"."""

    playMCTWarningAnnouncement: bool

    userTable: OCITable


@dataclass
class SystemMccMncHomeNetworkGetListResponse(OCIDataResponse):
    """Response to SystemMccMncHomeNetworkGetListRequest.
    The table column is: \"Home Networks\"."""

    homeNetworksTable: OCITable


@dataclass
class SystemMediaGetListResponse(OCIDataResponse):
    """Response to SystemMediaGetListRequest. The column headings are
    \"Media Name\", \"Codec\", \"Media Type\", \"Bandwidth Enforcement Type\" and \"Bandwidth\"."""

    mediaTable: OCITable


@dataclass
class SystemMediaGroupCodecGetListResponse(OCIDataResponse):
    """Response to SystemMediaGroupCodecGetListRequest.
    Contains a table of media assigned to the media group.
    The column headings are: \"Codec Name\", \"Codec Weight\"."""

    codecTable: OCITable


@dataclass
class SystemMediaGroupGetListResponse(OCIDataResponse):
    """Response to SystemMediaGroupGetListRequest.
    The response includes an array of media groups defined in the system."""

    name: List[str] = field(default_factory=list)


@dataclass
class SystemMediaGroupUsageListResponse(OCIDataResponse):
    """Response to SystemMediaGroupUsageListRequest.
    Contains a table of SAC groups associated with the media group.
    The column headings are: \"SAC Group Name\", \"Organization Id\", \"Organization Type\", and \"Group Id\".
    The \"Group Id\" will be empty for enterprise SAC groups."""

    usageTable: OCITable


@dataclass
class SystemMediaServerGetListResponse(OCIDataResponse):
    """Response to SystemMediaServerGetListRequest. The Media Server table column
    headings are: \"Net Address\", \"Port\", \"Transport\", \"Description\"."""

    mediaServerTable: OCITable


@dataclass
class SystemMediaServerParametersGetResponse(OCIDataResponse):
    """Response to SystemMediaServerParametersGetListRequest.
    Contains a list of system Media Server parameters."""

    mediaServerResponseTimerMilliseconds: int

    mediaServerSelectionRouteTimerMilliseconds: int

    useStaticMediaServerDevice: bool


@dataclass
class SystemMediaSetGetListResponse(OCIDataResponse):
    """Response to SystemMediaSetGetRequest."""

    mediaSetName: List[str] = field(default_factory=list)


@dataclass
class SystemMediaSetGetResponse(OCIDataResponse):
    """Response to SystemMediaSetGetRequest.
    Returns a list of media names in the set."""

    mediaName: List[str] = field(default_factory=list)


@dataclass
class SystemMeetMeConferencingGetResponse19(OCIDataResponse):
    """Response to SystemMeetMeConferencingGetRequest19."""

    conferenceIdLength: int

    moderatorPinLength: int

    enableConferenceEndDateRestriction: bool

    conferenceEndDateRestrictionMonths: int

    deleteExpiredConferencesAfterHoldPeriod: bool

    expiredConferenceHoldPeriodDays: int

    recordingFileFormat: str

    terminateAfterGracePeriod: bool

    conferenceGracePeriodMinutes: MeetMeConferencingConferenceDuration

    conferenceParticipantEarlyEntryMinutes: int

    enableConferenceExpiryNotification: bool

    enableActiveConferenceNotification: bool

    conferenceFromAddress: str

    conferenceActiveTalkerRefreshIntervalSeconds: int

    recordingWebAppURL: Optional[str] = None


@dataclass
class SystemMigratedUsersGetListResponse22(OCIDataResponse):
    """Response to SystemMigratedUsersGetListRequest22.
    The optional totalNumberOfMigratedUsers is returned only when the userListSizeLimit is set in the request and
    if the total number of migrated users is greater than the value of userListSizeLimit."""

    userId: List[str] = field(default_factory=list)

    totalNumberOfMigratedUsers: Optional[int] = None


@dataclass
class SystemMultimediaPolicyGetResponse(OCIDataResponse):
    """Response to SystemMultimediaPolicyGetRequest"""

    restrictNonAudioVideoMediaTypes: bool


@dataclass
class SystemMusicOnHoldGetResponse(OCIDataResponse):
    """Response to SystemMusicOnHoldGetRequest."""

    delayMilliseconds: int


@dataclass
class SystemNetworkAdministratorParametersGetResponse(OCIDataResponse):
    """Response to the SystemNetworkAdministratorParametersGetRequest.
    The response contains the network administrator settings for the system."""

    enabled: bool

    cacheRefreshIntervalInMinutes: int


@dataclass
class SystemNetworkClassOfServiceGetAssignedServiceProviderListResponse(
    OCIDataResponse
):
    """Response to the
    SystemNetworkClassOfServiceGetAssignedServiceProviderListRequest.
    The response contains a table of all Service Providers that have
    the given Network Class of Service assigned. The column headings are
    \"Service Provider Id\", \"Service Provider Name\" and \"Is Enterprise\"."""

    serviceProviderTable: OCITable


@dataclass
class SystemNetworkClassOfServiceGetAssignedSystemVoicePortalListResponse(
    OCIDataResponse
):
    """Response to the
    SystemNetworkClassOfServiceGetAssignedSystemVoicePortalListRequest.
    The response contains a table of system voice portals that have
    the given Network Class of Service assigned. The column headings are
    \"System Voice Portal Id\" and \"Name\"."""

    systemVoicePortalTable: OCITable


@dataclass
class SystemNetworkClassOfServiceGetCommunicationBarringProfileUsageListResponse(
    OCIDataResponse
):
    """Response to the SystemNetworkClassOfServiceGetCommunicationBarringProfileUsageListRequest.
    The response contains a table of all Network Classes of Service that
    contain the specific Communication Barring Profile. The column headings
    are \"Name\" and \"Description\" """

    networkClassOfServiceTable: OCITable


@dataclass
class SystemNetworkClassOfServiceGetListResponse(OCIDataResponse):
    """Response to the SystemNetworkClassOfServiceGetListRequest.
    The response contains a table of all Network Classes of Service
    in the system. The column headings are \"Name\" and \"Description\" """

    networkClassOfServiceTable: OCITable


@dataclass
class SystemNetworkClassOfServiceGetResponse19sp1(OCIDataResponse):
    """Response to the SystemNetworkClassOfServiceGetRequest19sp1.
    The response contains the Network Class of Service information."""

    description: Optional[str] = None

    communicationBarringProfile0: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile1: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile2: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile3: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile4: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile5: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile6: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile7: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile8: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    communicationBarringProfile9: Optional[
        NetworkClassOfServiceCommunicationBarringProfile
    ] = None

    networkTranslationIndex: Optional[str] = None

    callProcessingPolicyProfileName: Optional[str] = None


@dataclass
class SystemNetworkDeviceMonitorParametersGetResponse(OCIDataResponse):
    """Response to SystemNetworkDeviceMonitorParametersGetListRequest.
    Contains a list of system Network Device Polling parameters."""

    pollingIntervalMinutes: int

    failedPollingIntervalMinutes: int


@dataclass
class SystemNetworkProgressionGetResponse(OCIDataResponse):
    """Response to SystemNetworkProgressionGetRequest."""

    isActive: bool

    waitPeriodSeconds: int


@dataclass
class SystemNetworkRoutingServerGetListResponse(OCIDataResponse):
    """Response to SystemNetworkRoutingServerGetListRequest. The routing Network Server table column
    headings are: \"Net Address\", \"Port\", \"Transport\", \"Poll\", \"OpState\", \"Description\"."""

    networkRoutingServerTable: OCITable


@dataclass
class SystemNetworkServerSyncParametersGetResponse24V2(OCIDataResponse):
    """Response to SystemNetworkServerSyncParametersGetRequest24V2.
    Contains a list of system Network Server Sync parameters.
    The following elements are only used in AS data mode:
      syncTrunkGroups"""

    enableSync: bool

    syncLinePorts: bool

    syncDeviceManagementInfo: bool

    syncTrunkGroups: bool

    syncEnterpriseNumbers: bool

    syncConnectionTimeoutSeconds: Optional[int] = None


@dataclass
class SystemNetworkSynchingServerGetListResponse(OCIDataResponse):
    """Response to SystemNetworkSynchingServerGetListRequest. The Network Server table column
    headings are: \"Net Address\", \"Port\", \"Secure\", \"Description\", \"Order\".
    The following columns are only used in XS data mode and not returned in AS data mode:
      Order
    The following elements are only used in AS data mode and not returned in XS data mode:
      preferredNetworkServerNetAddress"""

    networkSynchingServerTable: OCITable

    preferredNetworkServerNetAddress: Optional[str] = None


@dataclass
class SystemNotificationOfReachabilityParametersGetResponse(OCIDataResponse):
    """Response to SystemNotificationOfReachabilityParametersGetRequest.
    Contains the system Notification of Reachability parameters."""

    enableNoR: bool

    alwaysSendThirdPartyVMforUnreachable: bool

    disableFACforThirdPartyVoiceMail: bool


@dataclass
class SystemNumberActivationGetResponse21(OCIDataResponse):
    """Response to SystemNumberActivationGetRequest21.
    Contains the system number activation and enterprise trunk number range activation setting."""

    numberActivationMode: str

    enableEnterpriseTrunkNumberRangeActivation: bool


@dataclass
class SystemNumberFormattingParametersGetResponse(OCIDataResponse):
    """Response to SystemNumberFormattingParametersGetRequest.
    Contains the system number formatting parameter."""

    applyFormattingToE164Numbers: bool


@dataclass
class SystemNumberPortabilityQueryDigitPatternGetListResponse(OCIDataResponse):
    """Response to the SystemNumberPortabilityQueryDigitPatternGetListRequest.
    Contains a table with column headings:
    \"Digit Pattern\", \"Status\"."""

    statusDigitPatternTable: OCITable


@dataclass
class SystemNumberPortabilityQueryDigitPatternGetResponse(OCIDataResponse):
    """Response to the SystemNumberPortabilityQueryDigitPatternGetRequest."""

    status: str


@dataclass
class SystemNumberPortabilityQueryGetResponse(OCIDataResponse):
    """Response to the SystemNumberPortabilityQueryGetRequest.
    Returns system Number Portability Query Parameters."""

    continueCallAsDialedOnTimeoutOrError: bool

    numberPortabilityNameLookupTimeoutMilliseconds: int


@dataclass
class SystemNumberPortabilityQueryStatusGetListResponse(OCIDataResponse):
    """Response to the SystemNumberPortabilityQueryStatusGetListRequest.
    Contains a table with column headings:
    \"Status and Treatment File Name\"."""

    statusTable: OCITable


@dataclass
class SystemNumberPortabilityQueryStatusGetResponse(OCIDataResponse):
    """Response to the SystemNumberPortabilityQueryStatusGetRequest."""

    treatmentFileName: Optional[str] = None


@dataclass
class SystemOCICallControlApplicationGetACLListResponse(OCIDataResponse):
    """Response to SystemOCICallControlApplicationGetACLListRequest. The table columns are:
    \"Net Address\" and \"Description\"."""

    aclTable: OCITable


@dataclass
class SystemOCICallControlApplicationGetListResponse(OCIDataResponse):
    """Response to SystemOCICallControlApplicationGetListRequest. The table columns are:
    \"Application Id\", \"Enabled System Wide\", \"Description\" \"Notification Timeout Seconds\", \"Max Event Channels Per Set\"
    and \"Channel Set Grace Period Seconds\"."""

    appTable: OCITable


@dataclass
class SystemOCICallControlGetACLListResponse(OCIDataResponse):
    """Response to SystemOCICallControlGetACLListRequest. The table columns are:
    \"Net Address\" and \"Description\"."""

    aclTable: OCITable


@dataclass
class SystemOCIGetACLListResponse(OCIDataResponse):
    """Response to SystemOCIGetACLListRequest.
    Returns a 2 coulmn table with column headings:
      \"Net Address\" and \"Description\"."""

    aclTable: OCITable


@dataclass
class SystemOCIReportingGetACLListResponse(OCIDataResponse):
    """Response to SystemOCIReportingACLListGetRequest.
    Contains a table with one row per access control list entry.
    The table columns are \"Net Address\", \"Description\" and \"Restrict Messages\"."""

    ociReportingACLTable: OCITable


@dataclass
class SystemOCIReportingGetMessageNameListResponse(OCIDataResponse):
    """Response to SystemOCIReportingGetMessageNameListRequest."""

    messageNameStartsWith: List[str] = field(default_factory=list)


@dataclass
class SystemOCIReportingParametersGetResponse22(OCIDataResponse):
    """Response to SystemOCIReportingParametersGetRequest22.
    Contains a list of system OCI Reporting parameters."""

    serverPort: int

    enableConnectionPing: bool

    connectionPingIntervalSeconds: int

    alterPasswords: bool

    enablePublicIdentityReporting: bool

    secure: bool


@dataclass
class SystemOfficeZoneGetAssignedServiceProviderListResponse(OCIDataResponse):
    """Response to the
    SystemOfficeZoneGetAssignedServiceProviderListRequest.
    The response contains a table of all Service Providers that have the given Office Zone assigned. The column headings are
    \"Service Provider Id\", \"Service Provider Name\" and \"Is Enterprise\"."""

    serviceProviderTable: OCITable


@dataclass
class SystemOfficeZoneGetListResponse(OCIDataResponse):
    """Response to the SystemOfficeZoneGetListRequest.
    The response contains a table of all Office Zones
    in the system. The column headings are \"Name\" and \"Description\" """

    officeZoneTable: OCITable


@dataclass
class SystemOfficeZoneGetResponse(OCIDataResponse):
    """Response to the SystemOfficeZoneGetRequest.
    The response contains the Office Zone information."""

    primaryZoneName: str

    description: Optional[str] = None

    zoneName: List[str] = field(default_factory=list)


@dataclass
class SystemOfficeZoneGetZoneUsageListResponse(OCIDataResponse):
    """Response to the SystemOfficeZoneGetZoneUsageListRequest.
    The response contains a table of all Office Zones that
    contain the specific Zone. The column headings
    are \"Name\" and \"Description\" """

    officeZoneTable: OCITable


@dataclass
class SystemOutboundProxyCacheParametersGetResponse(OCIDataResponse):
    """Response to SystemOutboundProxyCacheParametersGetRequest.
    Contains a list of Outbound Proxy Cache system parameters."""

    evictionTimeoutMinutes: int

    refreshTimeoutMinutes: int

    auditIntervalMinutes: int

    maximumCacheSize: int

    dnsTypeDefaultValue: Optional[str] = None

    useDnsSrvDefaultValue: Optional[str] = None

    srvPrefixDefaultValue: Optional[str] = None

    outboundProxyDefaultValue: Optional[str] = None

    transportTypeDefaultValue: Optional[str] = None

    secureRtpDefaultValue: Optional[str] = None


@dataclass
class SystemOutgoingCallingPlanCallTypeGetListResponse(OCIDataResponse):
    """Response to SystemOutgoingCallingPlanCallTypeGetListRequest."""

    callType: List[str] = field(default_factory=list)


@dataclass
class SystemOutgoingCallingPlanCallTypeGetMappingListResponse(OCIDataResponse):
    """Response to SystemOutgoingCallingPlanCallTypeGetMappingListRequest. The table columns are:
    \"Country Code\", \"Digit Map\" and \"Call Type\"."""

    callTypeMapping: OCITable


@dataclass
class SystemOutgoingCallingPlanGetResponse17sp3(OCIDataResponse):
    """Response to SystemOutgoingCallingPlanGetRequest17sp3."""

    directTransferScreening: bool

    enableEnhancedTollCallTyping: bool


@dataclass
class SystemPasswordRulesGetResponseRI(OCIDataResponse):
    """Response to SystemPasswordRulesGetRequestRI.
    Contains the password rules for System administrator, Provisioning Administrator,
    and/or Service Provider Administrator, Group Administrator, Department Administrator, user.
    The following element is only used in AS data mode:
    forcePasswordChangeAfterReset, value \"false\" is returned in XS data mode

    The two following enumeration values are only application in AS data mode:
    System, Provisioning Administrator. All other administrators and users use external authentication
    System, Provisioning Administrator. All other administrators and users use their organization's password rules
    In XS data mode
    only System, Provisioning Administrator. All other administrators and users use external authentication
    will be returned and it behave the same as
    System, Provisioning, Service Provider Administrator
    from the data type SystemPasswordRulesApplyTo

    The following element is only returned in AS data mode:
    enforceExternalAuthForRoutePoint
    reenableLogin
    lockOutInMinutes"""

    rulesApplyTo: str

    allowWebAddExternalAuthenticationUsers: bool

    disallowUserId: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    maxFailedLoginAttempts: int

    passwordExpiresDays: int

    sendLoginDisabledNotifyEmail: bool

    disallowRulesModification: bool

    disallowPreviousPasswords: bool

    numberOfPreviousPasswords: int

    forcePasswordChangeAfterReset: bool

    usePasswordValidationService: bool

    reenableLogin: bool

    lockOutInMinutes: int

    loginDisabledNotifyEmailAddress: Optional[str] = None

    enforceExternalAuthForRoutePoint: Optional[bool] = None


@dataclass
class SystemPasswordSecurityParametersGetResponse(OCIDataResponse):
    """Response to the SystemPasswordSecurityParametersGetResponse.
    The response contains the password security parameters for the system."""

    useExistingHashing: bool

    enforcePasswordChangeOnExpiry: bool


@dataclass
class SystemPerformanceMeasurementReportingGetFileServerListResponse22(OCIDataResponse):
    """Response to SystemPerformanceMeasurementReportingGetFileServerListRequest22. The table columns are:
    \"Repository URL\", \"User Id\", \"Passive\"."""

    fileServerTable: OCITable


@dataclass
class SystemPerformanceMeasurementReportingGetResponse24(OCIDataResponse):
    """Response to SystemPerformanceMeasurementReportingGetRequest24."""

    isActive: bool

    reportingInterval: int

    resetMeasurementsAfterEachReport: bool

    reportEnterprise: bool

    reportServiceProvider: bool

    reportDevice: bool

    reportTable: bool

    reportEncoding: str


@dataclass
class SystemPersonalAssistantGetResponse(OCIDataResponse):
    """Response to the SystemPersonalAssistantGetRequest.
    Returns system Personal Assistant Parameters."""

    transferToAttendantKey: str

    transferToVoiceMessagingKey: str


@dataclass
class SystemPhoneListsGetResponse(OCIDataResponse):
    """Response to the SystemPhoneListsGetRequest."""

    allowSpecialNumbersInPhoneLists: bool


@dataclass
class SystemPhysicalLocationGetResponse(OCIDataResponse):
    """Response to SystemPhysicalLocationGetRequest.
    Contains a list of system Physical Location parameters."""

    alwaysAllowEmergencyCalls: bool


@dataclass
class SystemPolicyGetDefaultResponse22(OCIDataResponse):
    """Response to SystemPolicyGetDefaultRequest22.
    Contains the default policy settings for the system.
    The following elements are only used in AS data mode:
        GroupAdminCommunicationBarringUserProfileAccess (This element is only used for groups in an Enterprise), value None is returned in XS mode
        GroupAdminVerifyTranslationAndRoutingAccess, value None is returned in XS mode
        ServiceProviderAdminVerifyTranslationAndRoutingAccess, value None is returned in XS mode
        GroupUserAutoAttendantNameDialingAccess, value None is returned in XS mode
    The following elements are only used in XS data mode:
        serviceProviderAdminCommunicationBarringAccess"""

    groupCallingPlanAccess: str

    groupExtensionAccess: str

    groupVoiceMessagingAccess: str

    groupDepartmentAdminUserAccess: str

    groupDepartmentAdminTrunkGroupAccess: str

    groupDepartmentAdminPhoneNumberExtensionAccess: str

    groupDepartmentAdminCallingLineIdNumberAccess: str

    groupUserAuthenticationAccess: str

    groupUserGroupDirectoryAccess: str

    groupUserProfileAccess: str

    groupUserEnhancedCallLogsAccess: str

    groupUserAutoAttendantNameDialingAccess: str

    groupAdminProfileAccess: str

    groupAdminUserAccess: str

    groupAdminAdminAccess: str

    groupAdminDepartmentAccess: str

    groupAdminAccessDeviceAccess: str

    groupAdminEnhancedServiceInstanceAccess: str

    groupAdminFeatureAccessCodeAccess: str

    groupAdminPhoneNumberExtensionAccess: str

    groupAdminCallingLineIdNumberAccess: str

    groupAdminServiceAccess: str

    groupAdminTrunkGroupAccess: str

    groupAdminVerifyTranslationAndRoutingAccess: str

    groupAdminSessionAdmissionControlAccess: str

    groupAdminOfficeZoneAccess: str

    groupAdminNumberActivationAccess: str

    groupAdminDialableCallerIDAccess: str

    groupAdminCommunicationBarringUserProfileAccess: str

    serviceProviderAdminProfileAccess: str

    serviceProviderAdminGroupAccess: str

    serviceProviderAdminUserAccess: str

    serviceProviderAdminAdminAccess: str

    serviceProviderAdminDepartmentAccess: str

    serviceProviderAdminAccessDeviceAccess: str

    serviceProviderAdminPhoneNumberExtensionAccess: str

    serviceProviderAdminCallingLineIdNumberAccess: str

    serviceProviderAdminServiceAccess: str

    serviceProviderAdminServicePackAccess: str

    serviceProviderAdminSessionAdmissionControlAccess: str

    serviceProviderAdminVerifyTranslationAndRoutingAccess: str

    serviceProviderAdminWebBrandingAccess: str

    serviceProviderAdminOfficeZoneAccess: str

    serviceProviderAdminCommunicationBarringAccess: str

    enterpriseAdminNetworkPolicyAccess: str

    enterpriseAdminNumberActivationAccess: str

    serviceProviderAdminDialableCallerIDAccess: str


@dataclass
class SystemPortalPasscodeRulesGetResponseRI(OCIDataResponse):
    """Response to SystemPortalPasscodeRulesGetRequestRI.
    Contains the system passcode rules setting.

    The following elements are only used in AS data mode:
      numberOfRepeatedDigits
      disallowRepeatedPatterns
      disallowContiguousSequences
      numberOfAscendingDigits
      numberOfDescendingDigits
      numberOfPreviousPasscodes
      reenableLogin
      lockOutInMinutes"""

    disallowRepeatedDigits: bool

    numberOfRepeatedDigits: int

    disallowRepeatedPatterns: bool

    disallowContiguousSequences: bool

    numberOfAscendingDigits: int

    numberOfDescendingDigits: int

    disallowUserNumber: bool

    disallowReversedUserNumber: bool

    disallowOldPasscode: bool

    numberOfPreviousPasscodes: int

    disallowReversedOldPasscode: bool

    minCodeLength: int

    maxCodeLength: int

    disableLoginAfterMaxFailedLoginAttempts: bool

    expirePassword: bool

    sendLoginDisabledNotifyEmail: bool

    defaultPassword: str

    reenableLogin: bool

    lockOutInMinutes: int

    maxFailedLoginAttempts: Optional[int] = None

    passcodeExpiresDays: Optional[int] = None

    loginDisabledNotifyEmailAddress: Optional[str] = None


@dataclass
class SystemPreferredCarrierGetGroupListResponse(OCIDataResponse):
    """Response to a SystemPreferredCarrierGetGroupListRequest.
    Contains a table with one row per group.
    The table columns are: \"Group Id\", \"Group Name\", \"Organization Id\", \"Organization Type\".
    The \"Organization Id\" column is populated with either a service provider Id or an enterprise Id.
    The \"Organization Type\" column is populated with one of the enumerated strings defined in the
    OrganizationType OCI data type.  Please see OCISchemaDataTypes.xsd for details on OrganizationType."""

    groupsUsingCarrierTable: OCITable


@dataclass
class SystemPreferredCarrierGetListResponse(OCIDataResponse):
    """Response to a SystemPreferredCarrierGetListRequest. Contains a table with one row per carrier.
    The table columns are: \"Carrier\", \"Country Code\", \"CIC\", \"Is Intra-Lata\", \"Is Inter-Lata\", \"Is International\".
    The value in the \"Is Intra-Lata\", \"Is Inter-Lata\", and \"Is International\" columns is one of \"true\" or \"false\"."""

    systemCarrierTable: OCITable


@dataclass
class SystemPreferredCarrierGetResponse(OCIDataResponse):
    """Response to a SystemPreferredCarrierGetRequest.
    Contains the attributes of a carrier."""

    cic: str

    countryCode: str

    isIntraLata: bool

    isInterLata: bool

    isInternational: bool


@dataclass
class SystemPreferredCarrierGetUserListResponse(OCIDataResponse):
    """Response to a SystemPreferredCarrierGetUserListRequest.
    Contains a table with one row per user.
    The table columns are: \"User Id\", \"Service Provider Id\", \"Group Id\", \"Last Name\", \"First Name\", \"Phone Number\", \"Email Address\",
    \"Hiragana Last Name\", and \"Hiragana First Name\", \"Extension\", \"Department\"."""

    usersUsingCarrierTable: OCITable


@dataclass
class SystemProvisioningValidationGetResponse25(OCIDataResponse):
    """Response to the SystemProvisioningValidationGetRequest25."""

    isActive: bool

    isNetworkServerQueryActive: bool

    timeoutSeconds: int

    denyMobilityNumberAsRedirectionDestination: bool

    denyEnterpriseNumberAsNetworkLocationDestination: bool

    denyAutoAttendantIdentityAsAutoAttendantTransferNumber: bool


@dataclass
class SystemPushNotificationAllowedApplicationGetListResponse(OCIDataResponse):
    """Response to SystemPushNotificationAllowedApplicationGetListRequest.
    Contains a table with a row for each allowed push notification application with columns:
    \"Application Id\", \"Description\" """

    applicationTable: OCITable


@dataclass
class SystemPushNotificationParametersGetResponse(OCIDataResponse):
    """Response to SystemPushNotificationParametersGetRequest.

    Contains a list of system push notification parameters."""

    enforceAllowedApplicationList: bool

    maximumRegistrationsPerUser: int

    maximumRegistrationAgeDays: int

    newCallTimeout: int

    subscriptionEventsPerSecond: int


@dataclass
class SystemRedundancyParametersGetResponse16sp2(OCIDataResponse):
    """Response to SystemRedundancyParametersGetRequest16sp2.
    Contains a list of system Redundancy parameters."""

    rollBackTimerMinutes: int

    sendSipOptionMessageUponMigration: bool


@dataclass
class SystemResourcePriorityGetResponse(OCIDataResponse):
    """Response to the SystemResourcePriorityGetRequest.
    The response contains the system Resource Priority service attributes."""

    sendResourcePriorityToNetwork: bool

    resourcePriority: str


@dataclass
class SystemRoamingNetworkGetListResponse(OCIDataResponse):
    """Response to the SystemRoamingNetworkGetListRequest.
    Contains a table with columns: \"MSC Address\", \"Network Translation Index\"."""

    roamingNetworkTable: OCITable


@dataclass
class SystemRouteListEnterpriseTrunkNumberPrefixGetSummaryListResponse(OCIDataResponse):
    """Response to SystemRouteListEnterpriseTrunkNumberPrefixGetSummaryListRequest.
    The column headings are \"Number Prefix\", \"Service Provider Id\", \"Is Enterprise\", \"User Id\", \"Enterprise Trunk\",
    \"Is Active\", \"Reseller Id\" \", \"Extension Range Start\" and \"Extension Range End\"."""

    prefixSummaryTable: OCITable


@dataclass
class SystemRouteListEnterpriseTrunkNumberRangeGetSummaryListResponse(OCIDataResponse):
    """Response to SystemRouteListEnterpriseTrunkNumberRangeGetSummaryListRequest.
    The column headings are \"Number Range Start\", \"Number Range End\", \"Service Provider Id\", \"Is Enterprise\", \"User Id\", \"Enterprise Trunk\",
    \"Is Active\", \"Reseller Id\" and \"Extension Length\"."""

    numberRangeSummaryTable: OCITable


@dataclass
class SystemRoutePointExternalSystemApplicationControllerGetResponse(OCIDataResponse):
    """Response to the SystemRoutePointExternalSystemApplicationControllerGetRequest."""

    applicationController: List[str] = field(default_factory=list)


@dataclass
class SystemRoutePointExternalSystemGetListResponse(OCIDataResponse):
    """Response to the SystemRoutePointExternalSystemGetListRequest.

    Contains a table with column headings:
    \"External System\", \"Description\"."""

    externalSystemTable: OCITable


@dataclass
class SystemRoutePointExternalSystemGetRoutePointListResponse(OCIDataResponse):
    """Response to the SystemRoutePointExternalSystemGetRoutePointListRequest."""

    serviceUserId: List[str] = field(default_factory=list)


@dataclass
class SystemRoutingGetResponse(OCIDataResponse):
    """Response to SystemRoutingGetRequest."""

    isRouteRoundRobin: bool

    routeTimerSeconds: int

    dnsResolvedAddressSelectionPolicy: str

    statefulExpirationMinutes: int

    maxAddressesPerHostname: int

    maxAddressesDuringSetup: int


@dataclass
class SystemRoutingGetRouteDeviceListResponse(OCIDataResponse):
    """Response to SystemRoutingGetRouteDeviceListRequest. The column headings are \"Net Address\",
    \"Port\", \"Transport\" and \"Description\"."""

    routeDeviceTable: OCITable


@dataclass
class SystemRoutingGetRouteListResponse(OCIDataResponse):
    """Response to SystemRoutingGetRouteListRequest."""

    routeName: List[str] = field(default_factory=list)


@dataclass
class SystemRoutingGetTranslationListResponse(OCIDataResponse):
    """Response to SystemRoutingGetTranslationListRequest. The column headings are \"Routing Digits\"
    and \"Route\"."""

    routingTable: OCITable


@dataclass
class SystemRoutingProfileGetListResponse(OCIDataResponse):
    """Response to SystemRoutingProfileGetListRequest.
    Returns a list of routing profiles defined in the system."""

    routingProfile: List[str] = field(default_factory=list)


@dataclass
class SystemRoutingProfileParametersGetResponse(OCIDataResponse):
    """Response to SystemRoutingProfileParametersGetRequest.
    Contains a list of Routing Profile parameters."""

    enablePermissiveRouting: bool


@dataclass
class SystemRuntimeDataPublicationGetResponse(OCIDataResponse):
    """Response to the SystemRuntimeDataPublicationGetRequest.
    The response contains the system call admission control parameters information.
    The following elements are only used in AS data mode:
      enableRuntimeDataSync, value \"false\" is returned in XS data mode.
      runtimeDataSyncIntervalInMilliSeconds value \"1000\" is returned in XS data mode."""

    enableRuntimeDataSync: bool

    runtimeDataSyncIntervalInMilliSeconds: int


@dataclass
class SystemSIPAuthenticationEndpointLockoutGetResponse(OCIDataResponse):
    """Response to SystemSIPAuthenticationEndpointLockoutGetRequest.
    The column headings for the lockoutTable are:
       \"Organization Id\", \"Organization Type\", \"Group Id\", \"Line/Port\", \"User ID\", \"First Name\", \"Last Name\", \"Lockout Started\", \"Lockout Expires\", \"Lockout Count\". Lockout times are shown in the system GMT time. When a permanent lockout is shown, the \"Lockout Expires\" column is empty and the \"Lockout Count\" column contains the word Permanent."""

    lockoutTable: OCITable


@dataclass
class SystemSIPAuthenticationPasswordRulesGetResponseRI(OCIDataResponse):
    """Response to SystemSIPAuthenticationPasswordRulesGetRequestRI.
    Contains the SIP authentication password rules for the system."""

    disallowAuthenticationName: bool

    disallowOldPassword: bool

    disallowReversedOldPassword: bool

    restrictMinDigits: bool

    minDigits: int

    restrictMinUpperCaseLetters: bool

    minUpperCaseLetters: int

    restrictMinLowerCaseLetters: bool

    minLowerCaseLetters: int

    restrictMinNonAlphanumericCharacters: bool

    minNonAlphanumericCharacters: int

    minLength: int

    sendPermanentLockoutNotification: bool

    endpointAuthenticationLockoutType: str

    endpointTemporaryLockoutThreshold: int

    endpointWaitAlgorithm: str

    endpointLockoutFixedMinutes: str

    endpointPermanentLockoutThreshold: int

    trunkGroupAuthenticationLockoutType: str

    trunkGroupTemporaryLockoutThreshold: int

    trunkGroupWaitAlgorithm: str

    trunkGroupLockoutFixedMinutes: str

    trunkGroupPermanentLockoutThreshold: int

    usePasswordValidationService: bool

    permanentLockoutNotifyEmailAddress: Optional[str] = None


@dataclass
class SystemSIPAuthenticationTrunkGroupLockoutGetResponse(OCIDataResponse):
    """Response to SystemSIPAuthenticationTrunkGroupLockoutGetRequest.
    The column headings for the lockoutTable are:
       \"Organization Id\", \"Organization Type\", \"Group Id\", \"Trunk Group Name\", \"Lockout Started\", \"Lockout Expires\", \"Lockout Count\". Lockout times are shown in the system GMT time. When a permanent lockout is shown, the \"Lockout Expires\" column is empty and the \"Lockout Count\" column contains the word Permanent."""

    lockoutTable: OCITable


@dataclass
class SystemSIPDeviceTypeFileGetListResponse14sp8(OCIDataResponse):
    """Response to SystemSIPDeviceTypeFileGetListRequest14sp8.
    Contains a table of device files managed by the Device Management System on a per-device type basis.
    The column headings are: \"File Format\", \"Is Authenticated\", \"Access URL\", \"Repository URL\", \"Template URL\"."""

    deviceTypeFilesTable: OCITable


@dataclass
class SystemSIPDeviceTypeFileGetResponse22V2(OCIDataResponse):
    """Response to SystemSIPDeviceTypeFileGetRequest22V2.
    Take note:

    1. accessUrl may have undefined content.
    When it is the case, undefined content is put between [].
    It may also be set to \"Error Access FQDN Not Provisioned\" when the access FQDN is not set,
    or \"Error Access Context Name Not Provisioned\" when the context name is not set.

    2. repositoryUrl may be set to \"DEVICE_CONFIGURATION_FILE_REPOSITORY_MISSING\", if there is no file repository defined."""

    remoteFileFormat: str

    fileCategory: str

    fileCustomization: str

    fileSource: str

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    bearerFileAuthentication: bool

    macInCert: bool

    macInNonRequestURI: bool

    allowHttp: bool

    allowHttps: bool

    allowTftp: bool

    enableCaching: bool

    allowUploadFromDevice: bool

    configurationFileName: Optional[str] = None

    macFormatInNonRequestURI: Optional[str] = None

    accessUrl: Optional[str] = None

    repositoryUrl: Optional[str] = None

    templateUrl: Optional[str] = None

    defaultExtendedFileCaptureMode: Optional[bool] = None


@dataclass
class SystemSIPDeviceTypeGetListResponse(OCIDataResponse):
    """Response to SystemSIPDeviceTypeGetListRequest.
    Contains a table of identity/ device profile types configured in the system.
    The column headings are: \"Device Type\", \"Profile\", \"Is Obsolete\" and \"Reseller Id\".

    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    deviceTypeTable: OCITable


@dataclass
class SystemSIPDeviceTypeGetResponse23V13(OCIDataResponse):
    """Response to SystemSIPDeviceTypeGetRequest23V13.
    The following elements are only used in AS data mode:
      supportClientSessionInfo, should be set to \"false\" if not used
      supportCallInfoConferenceSubscriptionURI, should be set to \"false\" if not used
      supportRemotePartyInfo,should be set to \"false\" if not used
      supportVisualDeviceManagementRedirectLink, should be set to \"false\" if not used
      bypassMediaTreatment, should be set to \"false\" if not used
      supportCauseParameter, should be set to \"false\" if not used
      supportCallingPartyCategoryInOutboundFromHeader, should be set to \"true\" if not used
      resellerId
      supportVisualDeviceManagementAPI, should be set to \"false\" if not used
      supportPreferredAutoAndForcedAnswer, should be set to \"false\" if not used
      supportCiscoCallerIdDispositionHeader

    The following elements are only used in AS data mode and not returned in XS data mode:
      deviceCategory
      deviceFamily

    The following elements are only used in XS data mode:
      enhancedForICS, should be set to \"false\" if not used
      supports3G4GContinuity, should be set to \"false\" if not used
      publishesOwnPresence, should be set to \"false\" if not used
      locationNetwork, should be set to \"Fixed\" if not used
      allowTerminationBasedOnICSI, should be set to \"false\" if not used
      roamingMode, should be set to \"None\" if not used"""

    isObsolete: bool

    numberOfPorts: UnboundedPositiveInt

    profile: str

    registrationCapable: bool

    isConferenceDevice: bool

    isMobilityManagerDevice: bool

    isMusicOnHoldDevice: bool

    holdNormalization: str

    holdAnnouncementMethod: str

    isTrusted: bool

    E164Capable: bool

    routeAdvance: bool

    forwardingOverride: bool

    wirelessIntegration: bool

    isVideoCapable: bool

    PBXIntegration: bool

    staticRegistrationCapable: bool

    earlyMediaSupport: str

    authenticateRefer: bool

    autoConfigSoftClient: bool

    authenticationMode: str

    requiresBroadWorksDigitCollection: bool

    requiresBroadWorksCallWaitingTone: bool

    requiresMWISubscription: bool

    useHistoryInfoHeaderOnAccessSide: bool

    adviceOfChargeCapable: bool

    supportCallCenterMIMEType: bool

    trunkMode: str

    addPCalledPartyId: bool

    supportIdentityInUpdateAndReInvite: bool

    unscreenedPresentationIdentityPolicy: str

    enhancedForICS: bool

    supportEmergencyDisconnectControl: bool

    deviceTypeConfigurationOption: str

    supportRFC3398: bool

    staticLineOrdering: bool

    supportClientSessionInfo: bool

    supportCallInfoConferenceSubscriptionURI: bool

    supportRemotePartyInfo: bool

    supportVisualDeviceManagementRedirectLink: bool

    bypassMediaTreatment: bool

    supports3G4GContinuity: bool

    publishesOwnPresence: bool

    supportCauseParameter: bool

    locationNetwork: str

    allowTerminationBasedOnICSI: bool

    roamingMode: str

    supportCallingPartyCategoryInOutboundFromHeader: bool

    supportPreferredAutoAndForcedAnswer: bool

    webBasedConfigURL: Optional[str] = None

    cpeDeviceOptions: Optional[CPEDeviceOptionsRead22V6] = None

    protocolChoice: List[str] = field(default_factory=list)

    resetEvent: Optional[str] = None

    resetString: Optional[str] = None

    resellerId: Optional[str] = None

    supportVisualDeviceManagementAPI: Optional[bool] = None

    deviceCategory: Optional[str] = None

    deviceFamily: Optional[str] = None

    verstatInPAIHeader: Optional[bool] = None

    verstatInFromHeader: Optional[bool] = None

    supportCiscoCallerIdDispositionHeader: Optional[bool] = None


@dataclass
class SystemSIPDeviceTypeLanguageMappingGetListResponse(OCIDataResponse):
    """Response to SystemSIPDeviceTypeLanguageMappingGetListRequest.
    Contains a table of device type languages mapped to equivalent BroadWorks languages.
    The column headings are: \"BroadWorks Language\", \"Device Language\"."""

    deviceTypeLanguagesTable: OCITable


@dataclass
class SystemSIPDeviceTypeServiceGetResponse(OCIDataResponse):
    """Response to SystemSIPDeviceTypeServiceGetRequest.
    Contains the list of device type services integrated to BroadWorks."""

    supportsPolycomPhoneServices: bool


@dataclass
class SystemSIPDiversionReasonGetResponse(OCIDataResponse):
    """Response to SystemSIPDiversionReasonGetRequest.
    Contains a table containing a list of diversion reasons and associated cause values.
    The column headings are: \"Diversion Reaon\", \"Cause Value\"."""

    diversionReasonTable: OCITable


@dataclass
class SystemSIPGetACLListResponse(OCIDataResponse):
    """Response to SystemSIPGetACLListRequest. The table columns are:
    \"Net Address\", \"Transport\" and \"Description\"."""

    aclTable: OCITable


@dataclass
class SystemSIPGetContentTypeListResponse(OCIDataResponse):
    """Response to SystemSIPGetContentTypeListRequest.
    Returns a 2 column table with column headings:
      \"Content Type\" and \"Supported Interface\"."""

    contentTypeTable: OCITable


@dataclass
class SystemSMDIGetACLListResponse(OCIDataResponse):
    """Response to SystemSMDIGetACLListRequest. The table columns are:
    \"Net Address\" and \"Description\"."""

    aclTable: OCITable


@dataclass
class SystemSMDIMessageDeskGetServerListResponse(OCIDataResponse):
    """Response to SystemMediaServerGetListRequest. The SMDI Server table column
    headings are: \"Device Name\", \"Net Address\", \"Port\" and \"Description\"."""

    smdiServerTable: OCITable


@dataclass
class SystemSMDIMessageDeskGetServerRouteListResponse(OCIDataResponse):
    """Response to SystemSMDIMessageDeskGetServerRouteListRequest.
    The SMDI Server route table column headings are: \"Destination\" and \"SMDI Servers\"."""

    smdiServerRouteTable: OCITable


@dataclass
class SystemSMDIParametersGetResponse(OCIDataResponse):
    """Response to SystemSMDIParametersGetListRequest.
    Contains a list of system SMDI parameters."""

    enableSMDI: bool

    listeningPort: int

    maxConnections: int


@dataclass
class SystemSMPPGetResponse22(OCIDataResponse):
    """Response to SystemSMPPGetRequest22."""

    primarySMPPPort: int

    secondarySMPPPort: int

    version: str

    enableMWICustomizedMessage: bool

    supportMessagePayload: bool

    maxShortMessageLength: int

    useGsmMwiUcs2Encoding: bool

    includeOnlyNewMessageCount: bool

    primarySMPPServerNetAddress: Optional[str] = None

    secondarySMPPServerNetAddress: Optional[str] = None

    systemId: Optional[str] = None

    password: Optional[str] = None

    systemType: Optional[str] = None


@dataclass
class SystemScheduleGetEventListResponse(OCIDataResponse):
    """Response to SystemScheduleGetEventListRequest.
    The response contains a list of events."""

    eventName: List[str] = field(default_factory=list)


@dataclass
class SystemScheduleGetEventResponse(OCIDataResponse):
    """Response to SystemScheduleGetEventRequest.
    The response contains the event of the system schedulable."""

    startDate: int

    allDayEvent: bool

    startTime: HourMinute

    endTime: HourMinute

    endDate: int

    recurrence: Optional[Recurrence] = None


@dataclass
class SystemScheduleGetListResponse(OCIDataResponse):
    """Response to SystemScheduleGetListRequest.
    The response contains a list of system schedules."""

    scheduleName: List[str] = field(default_factory=list)

    scheduleType: List[str] = field(default_factory=list)


@dataclass
class SystemSecurityClassificationGetClassificationResponse(OCIDataResponse):
    """Response to the SystemSecurityClassificationGetClassificationRequest."""

    audioAnnouncementFileDescription: str

    audioAnnouncementFileType: str


@dataclass
class SystemSecurityClassificationGetClassificationTrunkGroupUsageListResponse(
    OCIDataResponse
):
    """Response to the SystemSecurityClassificationGetClassificationTrunkGroupUsageListRequest.
    Contains a table with column headings:
    \"Trunk Group Name\",\"Group ID\",\"Organization ID\" and \"Organization Type\" """

    usageTable: OCITable


@dataclass
class SystemSecurityClassificationGetClassificationUserUsageListResponse(
    OCIDataResponse
):
    """Response to the SystemSecurityClassificationGetClassificationUserUsageListRequest.
    Contains a table with column headings:
    \"User ID\", \"Last Name\", \"First Name\", \"Phone Number\", \"Extension\", \"Service Provider Id\", \"Group Id\"."""

    usageTable: OCITable


@dataclass
class SystemSecurityClassificationGetResponse21(OCIDataResponse):
    """Response to the SystemSecurityClassificationGetRequest21.
    Contains a table with column headings:
    \"Name\", \"Priority\"."""

    meetMeAnncThreshold: int

    playTrunkUserSecurityClassificationAnnouncement: bool

    SecurityClassificationTable: OCITable


@dataclass
class SystemSelectiveServicesGetResponse22(OCIDataResponse):
    """Response to SystemSelectiveServicesGetRequest22."""

    scheduleCombination: str

    screenPrivateNumber: bool

    emptyHolidayScheduleIsOutOfSchedule: bool


@dataclass
class SystemServerAddressesGetResponse(OCIDataResponse):
    """Response to SystemServerAddressesGetRequest.
    Contains a list of system Server Addresses.
    See also:
      PrimaryInfoGetResponse
      PublicClusterGetFullyQualifiedDomainNameResponse
      ServingInfoGetResponse"""

    webServerClusterPublicFQDN: Optional[str] = None

    applicationServerClusterPrimaryPublicFQDN: Optional[str] = None

    applicationServerClusterSecondaryPublicFQDN: Optional[str] = None

    applicationServerClusterPrimaryPrivateFQDN: Optional[str] = None

    applicationServerClusterSecondaryPrivateFQDN: Optional[str] = None


@dataclass
class SystemServiceActivationAccessCodeGetResponse(OCIDataResponse):
    """Response to SystemServiceActivationAccessCodeGetRequest.
    Contains Service Activation Access Code system parameters."""

    isActive: bool

    terminatingAccessCode: Optional[str] = None

    redirectingAccessCode: Optional[str] = None

    clickToDialAccessCode: Optional[str] = None


@dataclass
class SystemServiceAttributeDefaultGetListResponse(OCIDataResponse):
    """Response to SystemServiceAttributeDefaultGetListRequest.
    Contains an array Service Attribute entries."""

    serviceAttributeEntry: List[ServiceAttributeEntryRead] = field(default_factory=list)


@dataclass
class SystemServiceCodeGetListResponse(OCIDataResponse):
    """Response to SystemServiceCodeGetListRequest.
    Contains a table of defined service codes
    The column headings are: \"Service Code\", and \"Description\"."""

    serviceCodeTable: OCITable


@dataclass
class SystemServicePackMigrationGetResponse(OCIDataResponse):
    """Response to the SystemServicePackMigrationGetRequest.
    The response contains the Service Pack Migration system level settings."""

    maxSimultaneousMigrationTasks: int


@dataclass
class SystemServicePhoneNumberLookupResponse(OCIDataResponse):
    """Response to the SystemServicePhoneNumberLookupRequest.
    The column headings for the userTable are: \"Service Provider Id\", \"Is Enterprise\", \"Group Id\", \"User Id\",
    \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\" and \"Extension\"."""

    userTable: OCITable


@dataclass
class SystemSessionAdmissionControlGetResponse25(OCIDataResponse):
    """Response to the SystemSessionAdmissionControlGetRequest22V3.
    The response contains the session admission control settings for the system."""

    countLongConnectionsToMediaServer: bool

    sacHandlingForMoH: str

    blockVMDepositDueToSACLimits: bool

    sacCodecSelectionPolicy: str

    countCallToMobileNumberForSACSubscriber: bool

    countBWAnywhereForSACSubscriber: bool

    countROForSACSubscriber: bool

    excludeBWMobilityForSACSubscriber: bool

    enableHoldoverOfHighwaterSessionCounts: bool

    holdoverPeriodMinutes: str

    timeZoneOffsetMinutes: str

    countCallsRedirectedToExternalDestination: bool

    releaseBWAnywhereDevicesOnly: bool


@dataclass
class SystemSessionAuditGetResponse23(OCIDataResponse):
    """Response to SystemSessionAuditGetRequest23.
    The following elements are only used in AS data mode:
    msAuditIntervalSeconds, value 1200 is returned in XS data mode"""

    isAuditActive: bool

    auditIntervalSeconds: int

    auditTimeoutSeconds: int

    releaseCallOnAuditFailure: bool

    isSIPRefreshAllowedOnAudit: bool

    allowUpdateForSIPRefresh: bool

    isSIPSessionTimerActive: bool

    sipSessionExpiresMinimumSeconds: int

    enforceSIPSessionExpiresMaximum: bool

    sipSessionExpiresMaximumSeconds: int

    sipSessionExpiresTimerSeconds: int

    alwaysUseSessionTimerWhenSupported: bool

    preferredSessionTimerRefresher: str

    enableEmergencyCallAlarmTimer: bool

    emergencyCallAlarmMinutes: int

    enableEmergencyCallCleanupTimer: bool

    emergencyCallCleanupMinutes: int

    alwaysAllowRefreshForMS: bool

    msAuditIntervalSeconds: int


@dataclass
class SystemShInterfaceParametersGetResponse17(OCIDataResponse):
    """Response to SystemShInterfaceParametersGetRequest.  Contains the Sh Interface system parameters."""

    publicIdentityRefreshDelaySeconds: int

    hssRealm: Optional[str] = None


@dataclass
class SystemShInterfaceRefreshTaskGetResponse(OCIDataResponse):
    """Response to SystemShInterfaceRefreshTaskGetRequest.  Provides the status of the system refresh task.  If isRunning is false, numberPublicIdentityRefreshStarted and numberPublicIdentities are omitted.  If isRunning is true, numberPublicIdentities indicates the total number of public identities in the system that will be refreshed by the system refresh task; numberPublicIdentityRefreshesStarted indicates the total number of public identities for which a refresh has been started."""

    isRunning: bool

    numberPublicIdentityRefreshesStarted: Optional[int] = None

    numberPublicIdentities: Optional[int] = None


@dataclass
class SystemSoftwareVersionGetResponse(OCIDataResponse):
    """Response to the SystemSoftwareVersionGetRequest."""

    version: str


@dataclass
class SystemSpeedDial100GetResponse17sp1(OCIDataResponse):
    """Response to the SystemSpeedDial100GetRequest17sp1."""

    prefix: Optional[str] = None


@dataclass
class SystemStateOrProvinceGetListResponse(OCIDataResponse):
    """Contains a 2 column table with column headings 'Key' and 'Display Name' and a row
    for each state or province."""

    stateOrProvinceTable: OCITable


@dataclass
class SystemStirShakenCallerIdDispositionMappingGetResponse(OCIDataResponse):
    """Response to SystemStirShakenCallerIdDispositionMappingModifyRequest.
    Contains a table of Caller Id Disposition mapping.
    The column headings are: \"Verstat\", \"Attestation\", \"Disposition\"."""

    callerIdDispositionMappingTable: OCITable


@dataclass
class SystemStirShakenGetResponse23V2(OCIDataResponse):
    """Response to the SystemStirShakenGetRequest23V2."""

    signingPolicy: str

    taggingPolicy: str

    signEmergencyCalls: bool

    tagEmergencyCalls: bool

    tagFromOrPAI: str

    verstatTag: str

    useOSValueForOrigId: bool

    attestationLevel: str

    enableVerification: bool

    verificationErrorHandling: str

    proxyVerstatToCNAMSubscribe: bool

    useUnknownHeadersFromCNAMNotify: bool

    useTS24229Headers: bool

    enableSigningForUnscreenedTrunkGroupOriginations: bool

    enableTaggingForUnscreenedTrunkGroupOriginations: bool

    unscreenedTrunkGroupOriginationAttestationLevel: str

    verifyGETSCalls: bool

    allowPartialIngressTagging: bool

    includeVerstatToMobileNetworkLocations: bool

    allowVerstatInSIPURIWithPhoneCorrection: bool

    includeTaggedHeadersToAccessSide: bool

    proxyIdentityHeaderToAccessSide: bool

    checkDirectoryNumbersForAttestation: bool

    matchUnassignedNumbersOnly: bool

    enableTaggingForRedirectedCalls: bool

    preferIngressTagging: bool

    signingServiceURL: Optional[str] = None

    origUUID: Optional[str] = None

    verificationServiceURL: Optional[str] = None


@dataclass
class SystemSubscriberGetCallProcessingParametersResponse18sp1(OCIDataResponse):
    """Response to the SystemSubscriberGetCallProcessingParametersRequest18sp1."""

    isExtendedCallingLineIdActive: bool

    isRingTimeOutActive: bool

    ringTimeoutSeconds: int

    allowEmergencyRemoteOfficeOriginations: bool

    maxNoAnswerNumberOfRings: int

    incomingCallToUserAliasMode: str

    bypassTerminationLoopDetection: bool

    honorCLIDBlockingForEmergencyCalls: bool

    useUnicodeIdentityName: bool


@dataclass
class SystemSubscriberGetLoginParametersResponse(OCIDataResponse):
    """Response to the SystemSubscriberGetLoginParametersRequest."""

    maxFailedLoginAttempts: int

    minLoginIdLength: int


@dataclass
class SystemSubscriberGetProvisioningParametersResponse24V2(OCIDataResponse):
    """Response to the SystemSubscriberGetProvisioningParametersRequest24V2."""

    configurableCLIDNormalization: bool

    includeDefaultDomain: bool

    minAuthLevelToProvisionAltUserID: str


@dataclass
class SystemSubscriptionLicenseReportingGetResponse(OCIDataResponse):
    """Response to SystemSubscriptionLicenseReportingGetRequest."""

    dailyReportScheduledTime: HourMinute


@dataclass
class SystemSystemServiceCallProcessingPoliciesGetResponse(OCIDataResponse):
    """Response to SystemSystemServiceCallProcessingPoliciesGetRequest."""

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int


@dataclass
class SystemSystemServiceDnGetAvailableListResponse(OCIDataResponse):
    """Response to SystemSystemServiceDnGetAvailableListRequest.
    Contains a list of available DNs not yet assigned to any instance of system service."""

    availableDn: List[str] = field(default_factory=list)


@dataclass
class SystemSystemServiceDnGetSummaryListResponse(OCIDataResponse):
    """Response to SystemSystemServiceDnGetSummaryListRequest.
    The column headings are \"Phone Numbers\" and \"Assigned\".
    The possible values for \"Assigned\" are true, false."""

    dnSummaryTable: OCITable


@dataclass
class SystemSystemServiceDnGetUsageListResponse(OCIDataResponse):
    """Response to SystemSystemServiceDnGetUsageListRequest.
    The table columns are:  \"Phone Number\", \"Id\",
    \"Name\", and \"System Service\".
    The possible values for \"System Service\" is \"System Voice Portal\"."""

    dnUtilizationTable: OCITable


@dataclass
class SystemSystemVoicePortalGetListResponse(OCIDataResponse):
    """Response to SystemSystemVoicePortalGetListRequest.
    The column headings are \"Default\", \"System Voice Portal Id\", \"Name\", \"Network Voice Portal Number\", \"System Voice Portal Number\" and \"Language\".
    The possible values for \"Default\" are true, false."""

    systemVoicePortalsTable: OCITable


@dataclass
class SystemSystemVoicePortalGetResponse23(OCIDataResponse):
    """Response to SystemSystemVoicePortalGetRequest23.

    The following elements are only used in AS data mode and ignored in XS data mode:
        networkClassOfService"""

    name: str

    callingLineIdName: str

    language: str

    timeZone: str

    allowIdentificationByPhoneNumberOrVoiceMailAliasesOnLogin: bool

    useVoicePortalWizard: bool

    isDefault: bool

    useVoicePortalDefaultGreeting: bool

    useVoiceMessagingDefaultGreeting: bool

    expressMode: bool

    phoneNumber: Optional[str] = None

    publicUserIdentity: Optional[str] = None

    networkVoicePortalNumber: Optional[str] = None

    voicePortalGreetingFileDescription: Optional[str] = None

    voicePortalGreetingMediaFileType: Optional[str] = None

    voiceMessagingGreetingFileDescription: Optional[str] = None

    voiceMessagingGreetingMediaFileType: Optional[str] = None

    networkClassOfService: Optional[str] = None


@dataclass
class SystemTemplateOnlyDeviceFileGetListResponse(OCIDataResponse):
    """Response to SystemTemplateOnlyDeviceFileGetListRequest.
    Contains a list of template files used to support a Visual Device Management device."""

    templateFileUrl: List[str] = field(default_factory=list)


@dataclass
class SystemThirdPartyEmergencyCallingGetResponse24(OCIDataResponse):
    """Response to the SystemThirdPartyEmergencyCallingGetRequest24.
    The response contains the third-party emergency call service settings for the system."""

    primaryHELDServerURL: Optional[str] = None

    secondaryHELDServerURL: Optional[str] = None

    emergencyRouteNetAddress: Optional[str] = None

    emergencyRoutePort: Optional[int] = None

    emergencyRouteTransport: Optional[str] = None


@dataclass
class SystemThirdPartyIMPGetResponse19(OCIDataResponse):
    """Response to the SystemThirdPartyIMPGetRequest19.
    The response contains the system Third-Party IMP service attributes."""

    serviceNetAddress: Optional[str] = None

    servicePort: Optional[int] = None

    boshURL: Optional[str] = None


@dataclass
class SystemThirdPartyVoiceMailSupportGetDnListResponse(OCIDataResponse):
    """Response to SystemThirdPartyVoiceMailSupportGetDnListRequest.
    Contains a table with a row for each ThirdPartyVoiceMailSupport User DN and column headings:
    \"Phone Number\", \"Description\" """

    thirdPartyVoiceMailSupportTable: OCITable


@dataclass
class SystemThirdPartyVoiceMailSupportGetResponse17sp4(OCIDataResponse):
    """Response to SystemThirdPartyVoiceMailSupportGetRequest17sp4."""

    overrideAltCallerIdForVMRetrieval: bool

    stripDiversionOnVMDestinationRetrieval: bool


@dataclass
class SystemTimeZoneGetListResponse20(OCIDataResponse):
    """Response to SystemTimeZoneGetListRequest20.
    Contains the configured time zone of the server processing the request and
    contains a 2 column table with column headings 'Key' and 'Display Name' and a row
    for each time zone."""

    serverTimeZone: str

    timeZoneTable: OCITable


@dataclass
class SystemTreatmentMappingAccessSIPStatusGetListResponse(OCIDataResponse):
    """Response to a SystemTreatmentMappingAccessSIPStatusGetListRequest. Contains a table with one row per mapping.
    The table columns are: \"SIP Status Code\", \"Treatment Id\"."""

    treatmentMappingTable: OCITable


@dataclass
class SystemTreatmentMappingCallBlockingServiceGetListResponse24V2(OCIDataResponse):
    """Response to a SystemTreatmentMappingCallBlockingServiceGetListRequest24V2.
    Contains a table with one row per mapping.
    The table columns are: \"Service\", \"Treatment Id\".

    The Service column list the service or policy which is using corresponding treatment, and can be OCP, EOCP, ICP, ACR, SCR, SCA, AAC, Intercept, PTT, CommBarring, SAC, IncomingCommBarring, HierCommBarring, IncomHierCommBarring, BWMobilityDenyOrig, BWMobilityDenyTerm, ETRouteExhaust, CallPark, NumberPortability, ConcTerminatingAlertingPolicy, AutomaticCollectCall, ETRouteExhaustUnreachable, TCUG, RPAdmission, MaximumRedirectionDepthOnBusy, MaximumRedirectionDepthOnDiversion, ETRouteExhaustBusy."""

    treatmentMappingTable: OCITable


@dataclass
class SystemTreatmentMappingInternalReleaseCauseGetListResponse(OCIDataResponse):
    """Response to a SystemTreatmentMappingInternalReleaseCauseGetListRequest. Contains a table with one row per mapping.
    The table columns are: \"Internal Release Cause\", \"Treatment Id\"."""

    treatmentMappingTable: OCITable


@dataclass
class SystemTreatmentMappingNetworkSIPStatusGetListResponse(OCIDataResponse):
    """Response to a SystemTreatmentMappingNetworkSIPStatusGetListRequest. Contains a table with one row per mapping.
    The table columns are: \"SIP Status Code\", \"Treatment Id\"."""

    treatmentMappingTable: OCITable


@dataclass
class SystemTreatmentMappingNetworkServerTreatmentGetListResponse(OCIDataResponse):
    """Response to a SystemTreatmentMappingNetworkServerTreatmentGetListRequest. Contains a table with one row per mapping.
    The table columns are: \"NS Treatment\", \"Treatment Id\"."""

    treatmentMappingTable: OCITable


@dataclass
class SystemTreatmentMappingQ850CauseGetListResponse(OCIDataResponse):
    """Response to a SystemTreatmentMappingQ850CauseGetListRequest. Contains a table with one row per mapping.
    The table columns are: \"Q850 Cause Value\", \"Treatment Id\"."""

    treatmentMappingTable: OCITable


@dataclass
class SystemTrunkGroupGetResponse24(OCIDataResponse):
    """Response to SystemTrunkGroupGetRequest24.
    Following attributes are only used in IMS mode:
      implicitRegistrationSetSupportPolicy
      sipIdentityForPilotAndProxyTrunkModesPolicy
      useMostRecentEntryOnDeflection"""

    enforceCLIDServiceAssignmentForPilotUser: bool

    terminateUnreachableTriggerDetectionOnReceiptOf18x: bool

    pilotUserCallingLineAssertedIdentityPolicy: str

    enforceOutOfDialogPBXRedirectionPolicies: bool

    unscreenedRedirectionHandling: str

    enableHoldoverOfHighwaterCallCounts: bool

    holdoverPeriod: int

    timeZoneOffsetMinutes: int

    clidSourceForScreenedCallsPolicy: str

    userLookupPolicy: str

    outOfDialogPBXRedirectionCLIDMapping: str

    enforceOutOfDialogPBXRedirectionTrunkGroupCapacity: bool

    implicitRegistrationSetSupportPolicy: str

    sipIdentityForPilotAndProxyTrunkModesPolicy: str

    supportConnectedIdentityPolicy: str

    useUnmappedSessionsForTrunkUsers: bool

    allowPAILookupForOutOfDialogPBXRedirection: bool

    outOfDialogPBXRedirectionOriginatorLookupPolicy: str

    allowTrunkIdentityForAllOriginations: bool

    useMostRecentEntryOnDeflection: bool


@dataclass
class SystemTrunkGroupOptionsMessageResponseStatusCodeGetListResponse(OCIDataResponse):
    """Response to the SystemTrunkGroupOptionsMessageResponseStatusCodeGetListRequest.
    The response contains of the list of system level successful SIP OPTIONS message respoonse status codes."""

    statusCode: List[str] = field(default_factory=list)


@dataclass
class SystemTrunkGroupUserCreationTaskGetListResponse14sp4(OCIDataResponse):
    """Response to SystemTrunkGroupUserCreationTaskGetListRequest14sp4.
    Contains a table with a row for each user creation task and column headings :
    \"Trunk Group Name\", \"Group Id\", \"Organization Id\", \"Organization Type\", \"Name\", \"Status\", \"Users Created\", \"Total Users To Create\", \"Error Count\".
    The \"Organization Id\" column is populated with either a service provider Id or an enterprise Id.
    The \"Organization Type\" column is populated with one of the enumerated strings defined in the
    OrganizationType OCI data type.  Please see OCISchemaDataTypes.xsd for details on OrganizationType."""

    taskTable: OCITable


@dataclass
class SystemTwoStageDialingGetDnListResponse(OCIDataResponse):
    """Response to SystemTwoStageDialingGetDnListRequest.
    The Two Stage Dialing DN List table column
    headings are: \"Phone Number\",  \"Description\"."""

    phoneNumberTable: OCITable


@dataclass
class SystemVerifyTranslationAndRoutingResponse(OCIDataResponse):
    """Represents a Verify Translation and Routing Test Call Result."""

    Result: str


# The Verify Translation and Routing log created by the request.


@dataclass
class SystemVideoServerGetListResponse(OCIDataResponse):
    """Response to SystemVideoServerGetListRequest. The Video Server table column
    headings are: \"Net Address\", \"Port\", \"Transport\", \"Description\".
    Transport types: udp, tcp, unspecified"""

    videoServerTable: OCITable


@dataclass
class SystemVideoServerParametersGetResponse(OCIDataResponse):
    """Response to SystemVideoServerParametersGetRequest.
    Contains a list of system video server parameters."""

    videoServerResponseTimerMilliseconds: int

    videoServerSelectionRouteTimerMilliseconds: int

    useStaticVideoServerDevice: bool


@dataclass
class SystemVirtualOnNetCallTypeGetListResponse(OCIDataResponse):
    """Response to SystemVirtualOnNetCallTypeGetListRequest.
    Contains a table with column headings:
    \"Virtual On-Net Call Type Name\", \"Virtual On-Net Call Type CDR Value\"
    in a row for each Virtual On-Net Call Type."""

    virtualOnNetCallTypeTable: OCITable


@dataclass
class SystemVisualDeviceManagementGetDeviceInfoResponse(OCIDataResponse):
    """Response to SystemVisualDeviceManagementGetDeviceInfoRequest."""

    deviceType: str

    supportVisualDeviceManagement: bool

    macAddress: Optional[str] = None

    primaryUser: Optional[PrimaryUserInfo] = None


@dataclass
class SystemVoiceMessageSummaryUpdateGetResponse25(OCIDataResponse):
    """Response to SystemVoiceMessageSummaryUpdateGetRequest25."""

    sendSavedAndUrgentMWIOnNotification: bool

    sendMessageSummaryUpdateOnRegister: bool

    minTimeBetweenMWIOnRegister: int

    allowMultipleUsersPerAccount: bool


@dataclass
class SystemVoiceMessagingGroupGetResponseRI(OCIDataResponse):
    """Response to SystemVoiceMessagingGroupGetRequestRI.

    The following elements are only used in AS data mode:
       realDeleteForImap
       useDnInMailBody
       useShortSubjectLine
       maxMessageLengthMinutes
       maxMailboxLengthMinutes
       doesMessageAge
       holdPeriodDays
       mailServerNetAddress
       mailServerProtocol
       defaultDeliveryFromAddress
       defaultNotificationFromAddress
       useOutgoingMWIOnSMDI
       mwiDelayInSeconds
       voicePortalScope
       enterpriseVoicePortalLicensed
       networkWideMessaging
       useExternalRouting
       defaultExternalRoutingAddress
       vmOnlySystem
       clientInitiatedMailServerSessionTimeoutMinutes
       recordingAudioFileFormat
       allowVoicePortalAccessFromVMDepositMenu
       allowVoicePortalAutoLoginForMobileDevicesOnly
       selectMwiTemplatePerCaller"""

    realDeleteForImap: bool

    useDnInMailBody: bool

    useShortSubjectLine: bool

    maxMessageLengthMinutes: int

    maxMailboxLengthMinutes: int

    doesMessageAge: bool

    holdPeriodDays: int

    mailServerProtocol: str

    defaultDeliveryFromAddress: str

    defaultNotificationFromAddress: str

    defaultVoicePortalLockoutFromAddress: str

    useOutgoingMWIOnSMDI: bool

    mwiDelayInSeconds: int

    voicePortalScope: str

    enterpriseVoicePortalLicensed: bool

    networkWideMessaging: bool

    useExternalRouting: bool

    vmOnlySystem: bool

    clientInitiatedMailServerSessionTimeoutMinutes: int

    recordingAudioFileFormat: str

    allowVoicePortalAccessFromVMDepositMenu: bool

    allowVoicePortalAutoLoginForMobileDevicesOnly: bool

    selectMwiTemplatePerCaller: bool

    mailServerNetAddress: Optional[str] = None

    defaultExternalRoutingAddress: Optional[str] = None


@dataclass
class SystemVoiceMessagingGroupGetVoicePortalMenusResponse21(OCIDataResponse):
    """Response to SystemVoiceMessagingGroupGetVoicePortalMenusRequest21."""

    useVoicePortalCustomization: bool

    voicePortalMainMenuKeys: object

    announcementMenuKeys: object

    announcementRecordingMenuKeys: object

    greetingsMenuKeys: object

    conferenceGreetingMenuKeys: object

    voiceMessagingMenuKeys: object

    playGreetingMenuKeys: object

    changeBusyOrNoAnswerGreetingMenuKeys: object

    changeExtendedAwayGreetingMenuKeys: object

    recordNewGreetingOrPersonalizedNameMenuKeys: object

    deleteAllMessagesMenuKeys: object

    commPilotExpressProfileMenuKeys: object

    personalizedNameMenuKeys: object

    callForwardingOptionsMenuKeys: object

    changeCallForwardingDestinationMenuKeys: object

    voicePortalCallingMenuKeys: object

    hotelingMenuKeys: object

    passcodeMenuKeys: object

    playMessagesMenuKeys: object

    playMessageMenuKeys: object

    additionalMessageOptionsMenuKeys: object

    forwardOrComposeMessageMenuKeys: object

    replyMessageMenuKeys: object

    sendToDistributionListMenuKeys: object

    selectDistributionListMenuKeys: object

    reviewSelectedDistributionListMenuKeys: object

    sendMessageToSelectedDistributionListMenuKeys: object

    sendToAllGroupMembersMenuKeys: object

    sendToPersonMenuKeys: object

    changeCurrentIntroductionOrMessageOrReplyMenuKeys: object

    voicePortalLoginMenuKeys: object

    faxMessagingMenuKeys: object

    messageDepositMenuKeys: object

    disableMessageDepositMenuKeys: object

    greetingOnlyForwardingDestinationMenuKeys: object

    personalAssistantMenuKeys: object


@dataclass
class SystemWebexMeetingsCallTypeGetListResponse(OCIDataResponse):
    """Response to a SystemWebexMeetingsCallTypeGetListRequest. Contains a table with one row per Webex Meetings call type entry.  The table column headings are: \"Name\", \"NS Call Type\", \"Enforce NS Charge Field\" and \"Process As Internal For SAC-Subscriber\"."""

    callTypeTable: OCITable


@dataclass
class SystemXsiApplicationIdGetListResponse(OCIDataResponse):
    """Response to the SystemXsiApplicationIdGetListRequest
    Contains a table with column headings: \"Xsi Application Id\", \"Description\"."""

    xsiApplicationIdTable: OCITable


@dataclass
class SystemXsiApplicationIdParameterGetResponse(OCIDataResponse):
    """Response to SystemXsiApplictionIdParameterGetRequest.
    Contains the Xsi application id system parameters."""

    screenXsiApplicationId: bool


@dataclass
class SystemXsiPolicyProfileGetAssignedServiceProviderListResponse(OCIDataResponse):
    """Response to SystemXsiPolicyProfileUsageGetListRequest.
    Contains a table with column headings: \"Organization ID\", \"Organization Name\", \"Organization Type\" and \"Reseller Id\"."""

    spTable: OCITable


@dataclass
class SystemXsiPolicyProfileGetListResponse(OCIDataResponse):
    """Response to the SystemXsiPolicyProfileGetListRequest
    Contains a table with column headings: \"Name\", \"Level\", \"Description\", \"Default\"."""

    xsiPolicyProfileTable: OCITable


@dataclass
class SystemXsiPolicyProfileGetResponse(OCIDataResponse):
    """Response to the SystemXsiPolicyProfileGetRequest.
    The response contains the Xsi policy profile."""

    maxTargetSubscription: int

    default: bool

    description: Optional[str] = None


@dataclass
class SystemZoneCallingZonePhysicalLocationGetResponse(OCIDataResponse):
    """Response to SystemZoneCallingZonePhysicalLocationGetRequest."""

    physicalLocation: Optional[str] = None


@dataclass
class SystemZoneGetListResponse(OCIDataResponse):
    """Response to the SystemZoneGetListRequest."""

    zoneName: List[str] = field(default_factory=list)


@dataclass
class SystemZoneLocationBasedPhysicalLocationGetListResponse(OCIDataResponse):
    """Response to SystemZoneLocationBasedPhysicalLocationGetListRequest."""

    physicalLocation: List[str] = field(default_factory=list)


@dataclass
class SystemZoneNetAddressGetListResponse(OCIDataResponse):
    """Response to SystemZoneNetAddressGetListRequest."""

    netAddress: List[str] = field(default_factory=list)

    netAddressRange: List[IPAddressRange] = field(default_factory=list)


@dataclass
class TutorialFlagGetResponse(OCIDataResponse):
    """Response to the TutorialFlagGetRequest."""

    enableTutorial: bool


@dataclass
class UserAccessDeviceDeviceActivationGetListResponse(OCIDataResponse):
    """Response to UserAccessDeviceDeviceActivationGetListRequest.
    Contains a table of devices supporting device activation associated to a user.
    The column headings are: \"Device Name\", \"Device Level\", \"Device SP\", \"Device Group\", \"Endpoint Type\", \"Line Port\", \"Activation Status\", \"Activation Code\", \"Expiration Time\" and \"MAC Address\"."""

    accessDeviceTable: OCITable


@dataclass
class UserAccessDeviceFileGetListResponse(OCIDataResponse):
    """Response to UserAccessDeviceFileGetListRequest.
    Contains a table of user modifiable Device Management files.
    The column headings are: \"File Format\", \"Template URL\"."""

    deviceFilesTable: OCITable


@dataclass
class UserAccessDeviceFileGetResponse(OCIDataResponse):
    """Response to UserAccessDeviceFileGetRequest."""

    templateUrl: Optional[str] = None


@dataclass
class UserAccessDeviceTagsGetResponse(OCIDataResponse):
    """Response to UserAccessDeviceTagsGetRequest.
    The response contains a table with columns: \"Tag Name\", and \"Tag Value\"."""

    deviceTagsTable: OCITable


@dataclass
class UserAdviceOfChargeGetResponse(OCIDataResponse):
    """Response to UserAdviceOfChargeGetRequest."""

    isActive: bool

    aocType: str


@dataclass
class UserAlternateNumbersGetResponse21(OCIDataResponse):
    """Response to UserAlternateNumbersGetRequest21."""

    distinctiveRing: bool

    alternateEntry01: Optional[AlternateNumberEntry21] = None

    alternateEntry02: Optional[AlternateNumberEntry21] = None

    alternateEntry03: Optional[AlternateNumberEntry21] = None

    alternateEntry04: Optional[AlternateNumberEntry21] = None

    alternateEntry05: Optional[AlternateNumberEntry21] = None

    alternateEntry06: Optional[AlternateNumberEntry21] = None

    alternateEntry07: Optional[AlternateNumberEntry21] = None

    alternateEntry08: Optional[AlternateNumberEntry21] = None

    alternateEntry09: Optional[AlternateNumberEntry21] = None

    alternateEntry10: Optional[AlternateNumberEntry21] = None


@dataclass
class UserAlternateUserIdGetListResponse(OCIDataResponse):
    """Response to UserAlternateUserIdGetListRequest.
    Contains a table of the main user id and the alternate user ids, the column headings are: \"User Id\", \"Description\", \"Alternate\".
    The possible values for \"Alternate\" are \"true\" and \"false\".
    The \"Description\" is only present for alternate user Ids."""

    userIdTable: OCITable


@dataclass
class UserAnnouncementFileGetAvailableListResponse(OCIDataResponse):
    """Response to UserAnnouncementFileGetAvailableListRequest.
    The response contains a table with columns: \"Name\", \"Media Type\", \"File Size\", \"Repository Type\", and \"Announcement File External Id\".
    The \"Name\" column contains the name of the announcement file.
    The \"Media Type\" column contains the media type of the announcement file with the possible values:
            WMA - Windows Media Audio file
            WAV - A WAV file
            3GP - A 3GP file
            MOV - A MOV file using a H.263 or H.264 codec.
    The \"File Size\" is in Kilobytes.
    The \"Repository Type\" column contains the type of repository for the announcement file such as \"User\" or \"Group\"
    The \"File Size\" column contains the file size in kB of the announcement file.
    The \"Announcement File External Id\" column contains the External Id of the announcement file.

    The following columns are populated in AS data mode only:
      \"Announcement File External Id\" """

    announcementTable: OCITable


@dataclass
class UserAnnouncementFileGetListResponse(OCIDataResponse):
    """Response to UserAnnouncementFileGetListRequest.
    When requested, the response contains a table with columns: \"Name\",
    \"Media Type\", \"File Size\", \"Announcement File External Id\".
    The \"Name\" column contains the name of the announcement file.
    The \"Media Type\" column contains the media type of the announcement file with the possible values:
            WMA - Windows Media Audio file
            WAV - A WAV file
            3GP - A 3GP file
            MOV - A MOV file using a H.263 or H.264 codec.
    The \"File Size\" column contains the file size in kB of the announcement file.
    The \"Announcement File External Id\" column contains the external ID of the announcement file.

    The following columns are populated in AS data mode only:
      \"Announcement File External Id\"

    The response also contains the current total file size (KB) for the user across
    all media types and the maximum total file size (MB) allowed for the user."""

    totalFileSize: int

    maxFileSize: int

    announcementTable: Optional[OCITable] = None


@dataclass
class UserAnnouncementFileGetPagedSortedListResponse(OCIDataResponse):
    """Response to UserAnnouncementFileGetPagedSortedListRequest.
    The response contains a table with columns: \"Name\", \"Media Type\", \"File Size\", and \"Announcement File External Id\".
    The \"Name\" column contains the name of the announcement file.
    The \"Media Type\" column contains the media type of the announcement.
    File with the possible values:
            WMA - Windows Media Audio file
            WAV - A WAV file
            3GP - A 3GP file
            MOV - A MOV file using a H.263 or H.264 codec.
    The \"File Size\" column contains the file size (KB) of the announcement file."""

    announcementTable: Optional[OCITable] = None


@dataclass
class UserAnnouncementFileGetResponse22(OCIDataResponse):
    """Response to UserAnnouncementFileGetRequest22.
    The response contains the file size (KB), uploaded timestamp, description and usage for
    an announcement file in the user announcement repository.
    The usage table has columns \"Service Name\", \"Criteria Name\"
    The \"Service Name\"\" values correspond to string values of the UserService data types.
    With the exception of the string \"Voice Portal\" which is returned when the announcement is being used by Voice Portal Personalized Name.
    For Call Center and Route Point users the \"Instance Name\" column contains the instance id and
    when the announcement is being used by a DNIS, \"Intance Name\" column contans the instance id and the DNIS id.
    For Auto Attendants with submenus and the announcement is used by a submenu the \"Instance Name\" column will contain the submenu name

    The following data elements are only used in AS data mode:
      announcementFileExternalId"""

    description: str

    filesize: int

    lastUploaded: str

    userId: str

    announcementFileKey: AnnouncementFileKey

    usageTable: OCITable

    announcementFileExternalId: Optional[str] = None


@dataclass
class UserAnnouncementRepositoryGetSettingsResponse(OCIDataResponse):
    """Response to UserAnnouncementRepositoryGetSettingsRequest.
    The response contains the current total file size (KB) for the user across
    all media types and the maximum total file size (MB) allowed for the user.
    It also indicates the maximum file size for individual audio and video files."""

    totalFileSize: int

    maxAudioFileSize: int

    maxVideoFileSize: int

    maxFileSize: int


@dataclass
class UserAnonymousCallRejectionGetResponse(OCIDataResponse):
    """Response to UserAnonymousCallRejectionGetRequest."""

    isActive: bool


@dataclass
class UserAssignedServicesGetListResponse(OCIDataResponse):
    """Response to UserAssignedServicesGetListRequest.
    A user can have both user services and group services because of music on hold."""

    groupServiceEntry: List[AssignedGroupServicesEntry] = field(default_factory=list)

    userServiceEntry: List[AssignedUserServicesEntry] = field(default_factory=list)


@dataclass
class UserAuthenticationGetResponse(OCIDataResponse):
    """Response to the UserAuthenticationGetRequest."""

    userName: Optional[str] = None


@dataclass
class UserAutomaticCallbackGetResponse(OCIDataResponse):
    """Response to UserAutomaticCallbackGetRequest."""

    isActive: bool


@dataclass
class UserAutomaticCollectCallGetResponse(OCIDataResponse):
    """Response to the UserAutomaticCollectCallGetRequest.
    Returns user Automatic Collect Call service settings."""

    enableAutomaticCollectCall: bool


@dataclass
class UserAutomaticHoldRetrieveGetResponse(OCIDataResponse):
    """Response to UserAutomaticHoldRetrieveGetRequest."""

    isActive: bool

    recallTimerSeconds: int


@dataclass
class UserBargeInExemptGetResponse(OCIDataResponse):
    """Response to UserBargeInExemptGetRequest."""

    isActive: bool


@dataclass
class UserBasicCallLogsGetListResponse14sp4(OCIDataResponse):
    """Response to UserBasicCallLogsGetListRequest14sp4."""

    placed: List[CallLogsEntry] = field(default_factory=list)

    received: List[CallLogsEntry] = field(default_factory=list)

    missed: List[CallLogsEntry] = field(default_factory=list)


@dataclass
class UserBroadWorksAnywhereGetAvailablePortalListResponse21sp1(OCIDataResponse):
    """Response to the UserBroadWorksAnywhereGetAvailablePortalListRequest21sp1.
    Contains a table with column headings: \"Portal ID\", \"Portal Name\", \"Phone Number\", \"Extension\", \"Language\"."""

    portalTable: OCITable


@dataclass
class UserBroadWorksAnywhereGetPhoneNumberPagedSortedListResponse(OCIDataResponse):
    """Response to the UserBroadWorksAnywhereGetPhoneNumberPagedSortedListRequest.
    The phoneNumberTable contains columns: \"Phone Number\", \"Description\", \"Activated\" """

    phoneNumberTable: OCITable


@dataclass
class UserBroadWorksAnywhereGetPhoneNumberResponse(OCIDataResponse):
    """Response to the UserBroadWorksAnywhereGetPhoneNumberRequest.
    The criteria table's column headings are: \"Is Active\", \"Criteria Name\", \"Time Schedule\",
    \"Calls From\", \"Blacklisted\", \"Holiday Schedule\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The following columns are only returned in AS data mode:
      \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\"

    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      - Mobility
    The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a caombination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - For Mobility Calls To Type, this is always blank.
      - When no exension is available a blank space is provided instead."""

    isActive: bool

    broadworksCallControl: bool

    useDiversionInhibitor: bool

    answerConfirmationRequired: bool

    criteriaTable: OCITable

    description: Optional[str] = None

    outboundAlternateNumber: Optional[str] = None


@dataclass
class UserBroadWorksAnywhereGetResponse16sp2(OCIDataResponse):
    """Response to the UserBroadWorksAnywhereGetRequest16sp2.
    The phoneNumberTable contains columns: \"Phone Number\", \"Description\" """

    alertAllLocationsForClickToDialCalls: bool

    alertAllLocationsForGroupPagingCalls: bool

    phoneNumberTable: OCITable


@dataclass
class UserBroadWorksAnywhereGetSelectiveCriteriaResponse21(OCIDataResponse):
    """Response to the UserBroadWorksAnywhereGetSelectiveCriteriaRequest21."""

    blacklisted: bool

    fromDnCriteria: CriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserBroadWorksCommunicatorGetResponse(OCIDataResponse):
    """Response to UserBroadWorksCommunicatorGetRequest."""

    configurationServerURL: Optional[str] = None


@dataclass
class UserBroadWorksMobilityGetResponse21sp1(OCIDataResponse):
    """Response to a UserBroadWorksMobilityGetRequest21sp1.
    Columns for the profileIdentityMobileNumberAlerted table are as follows: \"Mobile Number\", \"Country Code\", \"National Prefix\".
    Columns for the mobileIdentity table are as follows: \"Mobile Number\", \"Description\", \"Country Code\", \"National Prefix\", \"Is Primary\", \"Enable Alerting\"."""

    isActive: bool

    useMobileIdentityCallAnchoring: bool

    preventCallsToOwnMobiles: bool

    profileIdentityDevicesToRing: str

    profileIdentityIncludeSharedCallAppearance: bool

    profileIdentityIncludeBroadworksAnywhere: bool

    profileIdentityIncludeExecutiveAssistant: bool

    profileIdentityMobileNumberAlertedTable: OCITable

    mobileIdentityTable: OCITable


@dataclass
class UserBroadWorksMobilityMobileIdentityGetResponse22V3(OCIDataResponse):
    """Response to a UserBroadWorksMobilityMobileIdentityGetRequest22V3.


    Columns for the mobileNumberAlertedTable are as follows: \"Mobile Number\", \"Country Code\", \"National Prefix\" """

    isPrimary: bool

    enableAlerting: bool

    alertAgentCalls: bool

    alertClickToDialCalls: bool

    alertGroupPagingCalls: bool

    useMobilityCallingLineID: bool

    enableDiversionInhibitor: bool

    requireAnswerConfirmation: bool

    broadworksCallControl: bool

    useSettingLevel: str

    denyCallOriginations: bool

    denyCallTerminations: bool

    effectiveEnableLocationServices: bool

    effectiveEnableMSRNLookup: bool

    effectiveEnableMobileStateChecking: bool

    effectiveEnableAnnouncementSuppression: bool

    effectiveDenyCallOriginations: bool

    effectiveDenyCallTerminations: bool

    devicesToRing: str

    includeSharedCallAppearance: bool

    includeBroadworksAnywhere: bool

    includeExecutiveAssistant: bool

    enableCallAnchoring: bool

    enableDirectRouting: bool

    markCDRAsEnterpriseGroupCalls: bool

    useMobilityConnectedIdentity: bool

    mobileNumberAlertedTable: OCITable

    description: Optional[str] = None

    timeSchedule: Optional[ScheduleGlobalKey] = None

    holidaySchedule: Optional[ScheduleGlobalKey] = None

    accessDeviceEndpoint: Optional[AccessDeviceEndpointWithPortNumberRead22V2] = None

    outboundAlternateNumber: Optional[str] = None

    networkTranslationIndex: Optional[str] = None


@dataclass
class UserBroadWorksReceptionistEnterpriseGetAvailableUserListResponse(OCIDataResponse):
    """Response to the UserBroadWorksReceptionistEnterpriseGetAvailableUserListRequest.
    Returns a 12 column table with column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Group Id\", \"Phone Number\", \"Extension\", \"Mobile\", \"Email Address\", \"Department\", \"IMP Id\", \"Title\",
      \"Receptionist Note\".  The Receptionist Note column is only populated, if the user sending
      the request is the owner of the Receptionist Note and a Note exists."""

    userTable: OCITable


@dataclass
class UserBroadWorksReceptionistEnterpriseGetResponse(OCIDataResponse):
    """Response to UserBroadWorksReceptionistEnterpriseGetRequest.
    Returns a 12 column table with column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Group Id\", \"Phone Number\", \"Extension\", \"Mobile\", \"Email Address\", \"Department\", \"IMP Id\", \"Title\",
      \"Receptionist Note\".
    The Receptionist Note column is only populated, if the user sending the request is the owner
    of the Receptionist Note and a Note exists."""

    monitoredUserTable: OCITable


@dataclass
class UserBroadWorksReceptionistEnterpriseNoteGetResponse(OCIDataResponse):
    """Response to UserBroadWorksReceptionistEnterpriseNoteGetRequest."""

    receptionistNote: Optional[str] = None


@dataclass
class UserBroadWorksReceptionistOfficeGetAvailableUserListResponse(OCIDataResponse):
    """Response to the UserBroadWorksReceptionistOfficeGetAvailableUserListRequest.
    Returns a 12 column table with column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Group Id\", \"Phone Number\", \"Extension\", \"Mobile\", \"Email Address\", \"Department\", \"IMP Id\", \"Title\"."""

    userTable: OCITable


@dataclass
class UserBroadWorksReceptionistOfficeGetResponse(OCIDataResponse):
    """Response to UserBroadWorksReceptionistOfficeGetRequest.
    Returns a 11 column table with column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Group Id\", \"Phone Number\", \"Extension\", \"Mobile\", \"Email Address\", \"Department\", \"IMP Id\", \"Title\"."""

    monitoredUserTable: OCITable


@dataclass
class UserBroadWorksReceptionistSmallBusinessGetAvailableUserListResponse(
    OCIDataResponse
):
    """Response to the UserBroadWorksReceptionistSmallBusinessGetAvailableUserListRequest.
    Returns a 11 column table with column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Group Id\", \"Phone Number\", \"Extension\", \"Mobile\", \"Email Address\", \"Department\", \"IMP Id\", \"Title\"."""

    userTable: OCITable


@dataclass
class UserBroadWorksReceptionistSmallBusinessGetResponse(OCIDataResponse):
    """Response to UserBroadWorksReceptionistSmallBusinessGetRequest.
    Returns a 12 column table with column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Group Id\", \"Phone Number\", \"Extension\", \"Mobile\", \"Email Address\", \"Department\", \"IMP Id\", \"Title\"."""

    monitoredUserTable: OCITable


@dataclass
class UserBusyLampFieldGetAvailableUserListResponse(OCIDataResponse):
    """Response to the BusyLampFieldGetAvailableUserListRequest.
    Returns a table with column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"IMP Id\",
      \"User External Id\", and \"User Place Type\".
    The following columns are supported in AS data mode only:
      \"User External Id\", \"User Place Type\"
    The possible values for \"User Place Type\" are: User, Place."""

    userTable: OCITable


@dataclass
class UserBusyLampFieldGetResponse16sp2(OCIDataResponse):
    """Response to UserBusyLampFieldGetRequest16sp2.
    The table has column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"IMP Id\",
      \"User External Id\", and \"User Place Type\".
    The possible values for \"User Place Type\" are: User, Place."""

    enableCallParkNotification: bool

    monitoredUserTable: OCITable

    listURI: Optional[str] = None


@dataclass
class UserCallCenterAgentDetailsGetResponse(OCIDataResponse):
    """Response to the UserCallCenterAgentDetailsGetRequest.
    Contains the detail information for a Call Center Agent."""

    isCallCenterBasicAssigned: bool

    isCallCenterStandardAssigned: bool

    isCallCenterPremiumAssigned: bool


@dataclass
class UserCallCenterAgentSignOutResponse(OCIDataResponse):
    """Response to the UserCallCenterAgentSignOutRequest.
    It contains a list of call centers for which the agent is the last signed-in agent.
    Contains a table with column headings: \"Service User Id\" and \"Call Center Name\"."""

    callCenterTable: OCITable


@dataclass
class UserCallCenterCallDispositionCodeGetAvailableListResponse(OCIDataResponse):
    """Response to the UserCallCenterCallDispositionCodeGetAvailableListRequest.
    This list may include Group/Enterprise level codes in addition to the Call Center level codes,
    depending on the call center disposition codes settings.
    Only active codes are included in the list.
    Contains a table with column headings: \"Code\", \"Description\" and \"Level\".
    Level column can be any of the values in the data type CallDispositionCodeLevel."""

    dispositionCodesTable: OCITable


@dataclass
class UserCallCenterEnhancedReportingReportTemplateParamInfoGetResponse(
    OCIDataResponse
):
    """Response to UserCallCenterEnhancedReportingReportTemplateParamInfoGetRequest."""

    isRealtimeReport: bool

    requireAgentParam: bool

    requireCallCenterParam: bool

    requireCallCenterDnisParam: bool

    requireSamplingPeriodParam: bool

    callCompletionThresholdParam: Optional[str] = None

    shortDurationThresholdParam: Optional[str] = None

    serviceLevelThresholdParam: Optional[str] = None

    serviceLevelInclusionsParam: Optional[str] = None

    serviceLevelObjectiveThresholdParam: Optional[str] = None

    abandonedCallThresholdParam: Optional[str] = None

    serviceLevelThresholdParamNumber: Optional[int] = None

    abandonedCallThresholdParamNumber: Optional[int] = None


@dataclass
class UserCallCenterEnhancedReportingScheduledReportGetResponse(OCIDataResponse):
    """Response to UserCallCenterEnhancedReportingScheduledReportGetRequest."""

    reportTemplate: CallCenterReportTemplateKey

    schedule: CallCenterReportSchedule

    reportTimeZone: str

    reportDateFormat: str

    reportTimeFormat: str

    reportInterval: CallCenterReportInterval

    reportFormat: str

    callCenter: CallCenterScheduledReportCallCenterSelection

    dnis: CallCenterScheduledReportDNISSelection

    description: Optional[str] = None

    samplingPeriod: Optional[str] = None

    startDayOfWeek: Optional[str] = None

    agent: Optional[CallCenterScheduledReportAgentSelectionRead] = None

    callCompletionThresholdSeconds: Optional[int] = None

    shortDurationThresholdSeconds: Optional[int] = None

    serviceLevelThresholdSeconds: List[int] = field(default_factory=list)

    serviceLevelInclusions: Optional[
        CallCenterScheduledReportServiceLevelInclusions
    ] = None

    serviceLevelObjectivePercentage: Optional[int] = None

    abandonedCallThresholdSeconds: List[int] = field(default_factory=list)

    emailAddress: List[str] = field(default_factory=list)


@dataclass
class UserCallCenterGetAgentSupervisorListResponse(OCIDataResponse):
    """Response to the UserCallCenterGetAgentSupervisorListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"IMP Id\",
            \"Location Code\"."""

    supervisorTable: OCITable


@dataclass
class UserCallCenterGetAvailableCallCenterListResponse(OCIDataResponse):
    """Response to the UserCallCenterGetAvailableCallCenterListRequest.
    Contains a table with column heading: \"Service User Id\"."""

    callCenterTable: OCITable


@dataclass
class UserCallCenterGetAvailableCallCenterPagedSortedListResponse(OCIDataResponse):
    """Response to the UserCallCenterGetAvailableCallCenterPagedSortedListRequest.
    Contains a table with column heading: \"Service User Id\"."""

    callCenterTable: OCITable


@dataclass
class UserCallCenterGetAvailableDNISListResponse(OCIDataResponse):
    """Response to UserCallCenterGetAvailableDNISListRequest.
    Contains a list of available DNIS for agent to select."""

    availableDNIS: List[DNISKey] = field(default_factory=list)


@dataclass
class UserCallCenterGetResponse23(OCIDataResponse):
    """Response to the UserCallCenterGetRequest23.
    Contains the user's call center settings.
    Indicates whether the agent is current available (logged in) to each call center in the list.
    Contains a table with column headings: \"Service User Id\", \"Phone Number\", \"Extension\", \"Available\", \"Logoff Allowed\", \"Type\",
     \"Priority\",\"Routing Policy\" and \"Skill Level\".
    The valid \"Routing Type\" values are \"Priority Based\" and \"Skill Based\". This column is only populated for Premium Call Centers.
    The valid \"Skill Level\" values are of from 1-20. This column is only populated for Premium Skill Based Call Centers.

    The following elements are only used in AS data mode and not returned in XS data mode:
      agentACDState
      agentThresholdProfileName
      agentUnavailableCode
      useSystemDefaultUnavailableSettings
      forceAgentUnavailableOnDNDActivation
      forceAgentUnavailableOnPersonalCalls
      forceAgentUnavailableOnBouncedCallLimit
      numberConsecutiveBouncedCallsToForceAgentUnavailable
      forceAgentUnavailableOnNotReachable
      makeOutgoingCallsAsCallCenter
      outgoingCallDNIS
      useSystemDefaultWrapUpDestination
      wrapUpDestination

    The following columns are only used in AS data mode and not returned in XS data mode:
      \"Routing Policy\"
      \"Skill Level\" """

    useDefaultGuardTimer: bool

    enableGuardTimer: bool

    guardTimerSeconds: int

    callCenterTable: OCITable

    agentACDState: Optional[str] = None

    agentThresholdProfileName: Optional[str] = None

    agentUnavailableCode: Optional[str] = None

    useSystemDefaultUnavailableSettings: Optional[bool] = None

    forceAgentUnavailableOnDNDActivation: Optional[bool] = None

    forceAgentUnavailableOnPersonalCalls: Optional[bool] = None

    forceAgentUnavailableOnBouncedCallLimit: Optional[bool] = None

    numberConsecutiveBouncedCallsToForceAgentUnavailable: Optional[int] = None

    forceAgentUnavailableOnNotReachable: Optional[bool] = None

    makeOutgoingCallsAsCallCenter: Optional[bool] = None

    outgoingCallDNIS: Optional[DNISKey] = None

    useSystemDefaultWrapUpDestination: Optional[bool] = None

    wrapUpDestination: Optional[str] = None


@dataclass
class UserCallCenterGetSupervisedAgentListResponse(OCIDataResponse):
    """Response to the UserCallCenterGetSupervisedAgentListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\", \"Extension\",
    \"Department\", \"Email Address\", \"IMP Id\", \"Location Code\"."""

    agentUserTable: OCITable


@dataclass
class UserCallCenterGetSupervisorCallCenterListResponse(OCIDataResponse):
    """Response to the UserCallCenterGetSupervisorCallCenterListRequest.
    Contains a table with column headings: \"Service User Id\", \"Phone Number\",
    \"Extension\", \"Type\" and \"Priority\"."""

    callCenterTable: OCITable


@dataclass
class UserCallCenterMonitoringGetResponse23(OCIDataResponse):
    """Response to UserCallCenterMonitoringGetRequest23."""

    playToneToAgentForSilentMonitoring: bool

    playToneToAgentForSupervisorCoaching: bool


@dataclass
class UserCallForwardingAlwaysGetResponse(OCIDataResponse):
    """Response to UserCallForwardingAlwaysGetRequest."""

    isActive: bool

    isRingSplashActive: bool

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class UserCallForwardingAlwaysSecondaryGetResponse(OCIDataResponse):
    """Response to UserCallForwardingAlwaysSecondaryGetRequest."""

    isActive: bool

    isRingSplashActive: bool

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class UserCallForwardingBusyGetResponse(OCIDataResponse):
    """Response to UserCallForwardingBusyGetRequest."""

    isActive: bool

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class UserCallForwardingNoAnswerGetResponse13mp16(OCIDataResponse):
    """Response to UserCallForwardingNoAnswerGetRequest13mp16."""

    isActive: bool

    numberOfRings: int

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class UserCallForwardingNotReachableGetResponse(OCIDataResponse):
    """Response to UserCallForwardingNotReachableGetRequest."""

    isActive: bool

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class UserCallForwardingSelectiveGetCriteriaResponse21(OCIDataResponse):
    """Response to the UserCallForwardingSelectiveGetCriteriaRequest21."""

    forwardToNumberSelection: str

    fromDnCriteria: CriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    forwardToPhoneNumber: Optional[str] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserCallForwardingSelectiveGetResponse16(OCIDataResponse):
    """Response to the UserCallForwardingSelectiveGetRequest16. The criteria table's column headings are:
    \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Forward To\", \"Blacklisted\", \"Holiday Schedule\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The following columns are only returned in AS data mode:
      \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\"

    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      - Mobility
    The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - For Mobility Calls To Type, this is always blank.
      - When no extension is available a blank space is provided instead."""

    isActive: bool

    playRingReminder: bool

    criteriaTable: OCITable

    defaultForwardToPhoneNumber: Optional[str] = None


@dataclass
class UserCallMeNowGetCriteriaResponse(OCIDataResponse):
    """Response to the UserCallMeNowGetCriteriaRequest."""

    rejectCall: bool

    toDnCriteria: CallMeNowToDnCriteria

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None


@dataclass
class UserCallMeNowGetResponse(OCIDataResponse):
    """Response to the UserCallMeNowGetRequest. The criteria table's column headings are:
    \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Call To\", \"Reject Call\" and \"Holiday Schedule\"."""

    isActive: bool

    answerConfirmation: str

    criteriaTable: OCITable


@dataclass
class UserCallNotifyGetCriteriaResponse21(OCIDataResponse):
    """Response to the UserCallNotifyGetCriteriaRequest21."""

    blacklisted: bool

    fromDnCriteria: CriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserCallNotifyGetResponse(OCIDataResponse):
    """Response to the UserCallNotifyGetRequest. The criteria table's column headings are: \"Is Active\",
    \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Blacklisted\" ,\"Holiday Schedule\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The following columns are only returned in AS data mode:
      \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\"

    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      - Mobility
    The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - For Mobility Calls To Type, this is always blank.
      - When no extension is available a blank space is provided instead."""

    criteriaTable: OCITable

    callNotifyEmailAddress: Optional[str] = None


@dataclass
class UserCallParkGetResponse(OCIDataResponse):
    """Response to the UserCallParkGetRequest.
    Identifies which Call Park group the user belongs to and the list of users in the group.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"User External Id\", and \"User Place Type\".
    The following columns are supported in AS data mode only:
      \"User External Id\", \"User Place Type\"
    The possible values for \"User Place Type\" are: User, Place.
    The users are in the table in the order they will try to be parked on."""

    userTable: OCITable

    name: Optional[str] = None


@dataclass
class UserCallPickupGetResponse(OCIDataResponse):
    """Response to the UserCallPickupGetRequest.
    Identifies which Call Pickup group the user belongs to and the list of users in the group.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Department\", \"Phone Number\", \"Extension\", \"Email Address\"."""

    userTable: OCITable

    name: Optional[str] = None


@dataclass
class UserCallPoliciesGetResponse19sp1(OCIDataResponse):
    """Response to UserCallPoliciesGetRequest19sp1."""

    redirectedCallsCOLPPrivacy: str

    callBeingForwardedResponseCallType: str

    callingLineIdentityForRedirectedCalls: str


@dataclass
class UserCallProcessingGetPolicyResponse23(OCIDataResponse):
    """Response to UserCallProcessingGetPolicyRequest23.
    The useUserCLIDSetting attribute controls the CLID settings
    (clidPolicy, emergencyClidPolicy, allowAlternateNumbersForRedirectingIdentity, useGroupName, allowConfigurableCLIDForRedirectingIdentity, allowDepartmentCLIDNameOverride)

       The useUserMediaSetting attribute controls the Media settings
       (medisPolicySelection, supportedMediaSetName)

       The useUserCallLimitsSetting attribute controls the Call Limits setting
       (useMaxSimultaneousCalls, maxSimultaneousCalls, useMaxSimultaneousVideoCalls, maxSimultaneousVideoCalls,
       useMaxCallTimeForAnsweredCalls, maxCallTimeForAnsweredCallsMinutes, useMaxCallTimeForUnansweredCalls,
       maxCallTimeForUnansweredCallsMinutes, useMaxConcurrentRedirectedCalls, useMaxFindMeFollowMeDepth,
       maxRedirectionDepth, useMaxConcurrentFindMeFollowMeInvocations, maxConcurrentFindMeFollowMeInvocations,
       useMaxConcurrentTerminatingAlertingRequests, maxConcurrentTerminatingAlertingRequests,
       includeRedirectionsInMaximumNumberOfConcurrentCalls)

       The useUserDCLIDSetting controls the Dialable Caller ID settings (enableDialableCallerID)

       The useUserPhoneListLookupSetting controls whether or not to use the group setting for the Phone List Lookup policy (enablePhoneListLookup)

       The useUserTranslationRoutingSetting attribute controls the routing and translation settings (routeOverrideDomain, routeOverridePrefix)

       The following elements are only used in AS data mode:
        useUserDCLIDSetting
        enableDialableCallerID
        allowConfigurableCLIDForRedirectingIdentity
        allowDepartmentCLIDNameOverride
        useUserPhoneListLookupSetting, value \"false\" is returned in XS data mode.
        enablePhoneListLookup, value \"false\" is returned in XS data mode.
        useMaxConcurrentTerminatingAlertingRequests, value \"false\" is returned in XS data mode.
        maxConcurrentTerminatingAlertingRequests, value \"10\" is returned in XS data mode.
        includeRedirectionsInMaximumNumberOfConcurrentCalls, value \"false\" is returned in XS data mode.
        allowMobileDNForRedirectingIdentity,value \"false\" is returned in XS data mode.
        allowUserSelectionOfExternalCLIDPolicy,value \"false\" is returned in XS data mode.
        allowUserConfigurableCLIDModification,value \"false\" is returned in XS data mode.

       The following elements are only used in XS data mode and ignored in AS data mode:
          routeOverrideDomain
          routeOverridePrefix

       The following elements are only used in XS data mode:
          useUserTranslationRoutingSetting, value \"false\" is returned in AS data mode."""

    useUserCLIDSetting: bool

    useUserMediaSetting: bool

    useUserCallLimitsSetting: bool

    useUserDCLIDSetting: bool

    useUserTranslationRoutingSetting: bool

    useMaxSimultaneousCalls: bool

    maxSimultaneousCalls: int

    useMaxSimultaneousVideoCalls: bool

    maxSimultaneousVideoCalls: int

    useMaxCallTimeForAnsweredCalls: bool

    maxCallTimeForAnsweredCallsMinutes: int

    useMaxCallTimeForUnansweredCalls: bool

    maxCallTimeForUnansweredCallsMinutes: int

    mediaPolicySelection: str

    useMaxConcurrentRedirectedCalls: bool

    maxConcurrentRedirectedCalls: int

    useMaxFindMeFollowMeDepth: bool

    maxFindMeFollowMeDepth: int

    maxRedirectionDepth: int

    useMaxConcurrentFindMeFollowMeInvocations: bool

    maxConcurrentFindMeFollowMeInvocations: int

    clidPolicy: str

    emergencyClidPolicy: str

    allowAlternateNumbersForRedirectingIdentity: bool

    useGroupName: bool

    blockCallingNameForExternalCalls: bool

    enableDialableCallerID: bool

    allowConfigurableCLIDForRedirectingIdentity: bool

    allowDepartmentCLIDNameOverride: bool

    useUserPhoneListLookupSetting: bool

    enablePhoneListLookup: bool

    useMaxConcurrentTerminatingAlertingRequests: bool

    maxConcurrentTerminatingAlertingRequests: int

    includeRedirectionsInMaximumNumberOfConcurrentCalls: bool

    allowMobileDNForRedirectingIdentity: bool

    allowUserSelectionOfExternalCLIDPolicy: bool

    allowUserConfigurableCLIDModification: bool

    supportedMediaSetName: Optional[str] = None

    routeOverrideDomain: Optional[str] = None

    routeOverridePrefix: Optional[str] = None


@dataclass
class UserCallRecordingGetResponse23(OCIDataResponse):
    """Response to the UserCallRecordingGetRequest23.
    The response contains the user's Call Recording option information.

    The following parameters are not returned for service instance:
      - pauseResumeNotification
      - enableCallRecordingAnnouncement
      - enableRecordCallRepeatWarningTone
      - recordCallRepeatWarningToneTimerSeconds

    The enableVoiceMailRecording parameter is only returned if the Voice
    Messaging User service is assigned to the user.  This applies to both
    users and service instances.

    The recordingOption and enableCallRecordingAnnouncement which elements can
    only be modified by a System or a Provisioning administrator when
    restrictCallRecordingProvisioningAccess system param is set to true. Both the element
    values will be ignored when group admin or lower runs this.
    The following elements are only used in AS data mode and not returned in XS data mode:
       mediaStream"""

    recordingOption: str

    pauseResumeNotification: Optional[str] = None

    enableCallRecordingAnnouncement: Optional[bool] = None

    enableRecordCallRepeatWarningTone: Optional[bool] = None

    recordCallRepeatWarningToneTimerSeconds: Optional[int] = None

    enableVoiceMailRecording: Optional[bool] = None

    mediaStream: Optional[str] = None


@dataclass
class UserCallToNumberGetAvailableListResponse(OCIDataResponse):
    """Response to the UserCallToNumberGetAvailableListRequest.
    Contains a list of the user available Call to Numbers\"."""

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserCallTransferGetResponse14sp4(OCIDataResponse):
    """Response to UserCallTransferGetRequest14sp4."""

    isRecallActive: bool

    recallNumberOfRings: int

    useDiversionInhibitorForBlindTransfer: bool

    useDiversionInhibitorForConsultativeCalls: bool

    enableBusyCampOn: bool

    busyCampOnSeconds: int


@dataclass
class UserCallWaitingGetResponse17sp4(OCIDataResponse):
    """Response to UserCallWaitingGetRequest17sp4.

    The following elements are only used in AS data mode:
      disableCallingLineIdDelivery"""

    isActive: bool

    disableCallingLineIdDelivery: bool


@dataclass
class UserCallingLineIDBlockingOverrideGetResponse(OCIDataResponse):
    """Response to UserCallingLineIDBlockingOverrideGetRequest."""

    isActive: bool


@dataclass
class UserCallingLineIDDeliveryBlockingGetResponse(OCIDataResponse):
    """Response to UserCallingLineIDDeliveryBlockingGetRequest."""

    isActive: bool


@dataclass
class UserCallingNameDeliveryGetResponse(OCIDataResponse):
    """Response to UserCallingNameDeliveryGetRequest."""

    isActiveForExternalCalls: bool

    isActiveForInternalCalls: bool


@dataclass
class UserCallingNameRetrievalGetResponse(OCIDataResponse):
    """Response to UserCallingNameRetrievalGetRequest."""

    isActive: bool


@dataclass
class UserCallingNumberDeliveryGetResponse(OCIDataResponse):
    """Response to UserCallingNumberDeliveryGetRequest."""

    isActiveForExternalCalls: bool

    isActiveForInternalCalls: bool


@dataclass
class UserCallingPartyCategoryGetResponse16(OCIDataResponse):
    """Response to UserCallingPartyCategoryGetRequest16."""

    category: str


@dataclass
class UserChargeNumberGetResponse14sp9(OCIDataResponse):
    """Response to UserChargeNumberGetRequest14sp9."""

    useChargeNumberForEnhancedTranslations: bool

    sendChargeNumberToNetwork: bool

    phoneNumber: Optional[str] = None


@dataclass
class UserClassmarkGetResponse(OCIDataResponse):
    """Response to UserClassmarkGetRequest.
    Contains the Class Mark data"""

    classmark: Optional[str] = None


@dataclass
class UserCollaborateBridgeGetResponse20sp1(OCIDataResponse):
    """The system-level collaborate supportOutdial setting is returned in the response when the system-level collaborate supportOutdial setting is disabled.
    Response to UserCollaborateBridgeGetRequest20sp1."""

    bridgeId: str

    bridgeName: str

    supportOutDial: bool

    maxCollaborateRoomParticipants: int

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    alternateNumberEntry: List[AlternateNumberEntry21] = field(default_factory=list)


@dataclass
class UserCollaborateInstantRoomAddResponse(OCIDataResponse):
    """Response to UserCollaborateInstantRoomAddRequest."""

    roomId: str


@dataclass
class UserCollaborateInstantRoomGetResponse(OCIDataResponse):
    """Response to UserCollaborateInstantRoomGetRequest."""

    instantRoomStartTime: str

    instantRoomEndTime: str

    roomName: Optional[str] = None


@dataclass
class UserCollaborateInstantRoomParametersGetResponse(OCIDataResponse):
    """Response to UserCollaborateInstantRoomParametersGetRequest."""

    attendeeNotification: str

    endCollaborateRoomSessionOnOwnerExit: bool

    ownerRequired: bool


@dataclass
class UserCollaborateMyRoomGetResponse(OCIDataResponse):
    """Response to UserCollaborateMyRoomGetRequest."""

    roomId: str

    roomName: str

    attendeeNotification: str

    endCollaborateRoomSessionOnOwnerExit: bool

    ownerRequired: bool


@dataclass
class UserCollaborateProjectRoomAddResponse(OCIDataResponse):
    """Response to UserCollaborateProjectRoomAddRequest."""

    roomId: str


@dataclass
class UserCollaborateProjectRoomGetResponse(OCIDataResponse):
    """Response to UserCollaborateProjectRoomGetRequest."""

    roomName: str

    attendeeNotification: str

    endCollaborateRoomSessionOnOwnerExit: bool

    ownerRequired: bool

    roomSchedule: CollaborateRoomSchedule


@dataclass
class UserCollaborateRoomGetResponse(OCIDataResponse):
    """Response to UserCollaborateRoomGetRequest.
    The roomType and roomName parameters are returned for all rooms.
    The following parameters are returned for My room and Project Room:
    attendeeNotification, endCollaborateRoomSessionOnOwnerExit and
    ownerRequired. In addition, the roomSchedule is returned for
    Project Room and the instantRoomStartTime and instantRoomEndTime
    are returned for Instant Room."""

    roomType: str

    roomName: str

    attendeeNotification: Optional[str] = None

    endCollaborateRoomSessionOnOwnerExit: Optional[bool] = None

    ownerRequired: Optional[bool] = None

    instantRoomStartTime: Optional[str] = None

    instantRoomEndTime: Optional[str] = None

    roomSchedule: Optional[CollaborateRoomSchedule] = None


@dataclass
class UserCollaborateRoomIDRegenerateResponse(OCIDataResponse):
    """Response to UserCollaborateRoomIDRegenerateRequest."""

    roomId: str


@dataclass
class UserCollaborateRoomListGetResponse(OCIDataResponse):
    """Response to UserCollaborateRoomListGetRequest.
    Contains a table with column headings :  \"Room Type\", \"Name\", \"Room Id\",
    in a row for each collaborate room instance.
    Possible values for Room Type column are MyRoom, Project Room and
    Instant Room."""

    roomInstanceTable: OCITable


@dataclass
class UserCommPilotExpressGetResponse(OCIDataResponse):
    """Response to the UserCommPilotExpressGetRequest."""

    availableInOffice: CommPilotExpressAvailableInOffice

    availableOutOfOffice: CommPilotExpressAvailableOutOfOffice

    busy: CommPilotExpressBusy

    unavailable: CommPilotExpressUnavailable

    profile: Optional[str] = None


@dataclass
class UserCommunicationBarringAuthorizationCodeGetListResponse(OCIDataResponse):
    """Response to UserCommunicationBarringAuthorizationCodeGetListRequest.
    Contains a list of Communication Barring Authorization Codes
    assigned to the user."""

    code: List[CommunicationBarringAuthorizationCodeEntry] = field(default_factory=list)


@dataclass
class UserCommunicationBarringGetResponse(OCIDataResponse):
    """Response to UserCommunicationBarringGetRequest.
    This command only applies to users in an Enterprise."""

    useGroupSetting: bool

    profileName: Optional[str] = None


@dataclass
class UserCommunicationBarringUserControlGetResponse(OCIDataResponse):
    """Response to the UserCommunicationBarringUserControlGetRequest.
    Identifies the profiles available to the user and which one if any
    is active as well as the lockout status.
    Contains a table with column headings: \"Name\", \"Code\", \"Activated\" and \"Primary\"."""

    lockoutStatus: bool

    profileTable: OCITable


@dataclass
class UserConnectedLineIdentificationRestrictionGetResponse(OCIDataResponse):
    """Response to UserConnectedLineIdentificationRestrictionGetRequest."""

    isActive: bool


@dataclass
class UserCustomRingbackUserGetCriteriaListResponse(OCIDataResponse):
    """Response to the UserCustomRingbackUserGetCriteriaListRequest.
    The criteria table's column headings are: \"Is Active\", \"Criteria Name\",
    \"Time Schedule\", \"Calls From\", \"Blacklisted\", \"Holiday Schedule\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The following columns are only returned in AS data mode:
      \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\"

    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      - Mobility
    The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - For Mobility Calls To Type, this is always blank.
      - When no extension is available a blank space is provided instead."""

    criteriaTable: OCITable


@dataclass
class UserCustomRingbackUserGetCriteriaResponse21(OCIDataResponse):
    """Response to the UserCustomRingbackUserGetCriteriaRequest21."""

    blacklisted: bool

    fromDnCriteria: CriteriaFromDn

    audioSelection: str

    videoSelection: str

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)

    audioFile: Optional[AnnouncementFileLevelKey] = None

    audioFileUrl: Optional[str] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    videoFileUrl: Optional[str] = None

    callWaitingAudioSelection: Optional[str] = None

    callWaitingAudioFile: Optional[AnnouncementFileLevelKey] = None

    callWaitingAudioFileUrl: Optional[str] = None

    callWaitingVideoSelection: Optional[str] = None

    callWaitingVideoFile: Optional[AnnouncementFileLevelKey] = None

    callWaitingVideoFileUrl: Optional[str] = None


@dataclass
class UserDeviceActivationPolicyInEffectGetResponse(OCIDataResponse):
    """Response to UserDeviceActivationPolicyInEffectGetRequest."""

    allowActivationCodeRequestByUser: bool

    sendActivationCodeInEmail: bool


@dataclass
class UserDevicePoliciesGetResponse21(OCIDataResponse):
    """Response to UserDevicePoliciesGetRequest21. enableDeviceFeatureSynchronization and
      enableCallDecline are ignored by the application server in Multiple User Shared mode.
    The following element is only used in AS data mode:
      lineMode, value \"Single User Private and Shared\" is returned in XS data mode
    The following elements are only used in AS data mode:
      enableDeviceFeatureSynchronization, value \"false\" is returned in XS data mode
      enableDnd, value \"false\" is returned in XS data mode
      enableCallForwardingAlways, value \"false\" is returned in XS data mode
      enableCallForwardingBusy, value \"false\" is returned in XS data mode
      enableCallForwardingNoAnswer, value \"false\" is returned in XS data mode
      enableAcd, value \"false\" is returned in XS data mode
      enableExecutive, value \"false\" is returned in XS data mode
      enableExecutiveAssistant, value \"false\" is returned in XS data mode
      enableSecurityClassification, value \"false\" is returned in XS data mode
      enableCallRecording, value \"false\" is returned in XS data mode"""

    lineMode: str

    enableDeviceFeatureSynchronization: bool

    enableDnd: bool

    enableCallForwardingAlways: bool

    enableCallForwardingBusy: bool

    enableCallForwardingNoAnswer: bool

    enableAcd: bool

    enableExecutive: bool

    enableExecutiveAssistant: bool

    enableSecurityClassification: bool

    enableCallRecording: bool

    enableCallDecline: bool


@dataclass
class UserDirectRouteGetResponse(OCIDataResponse):
    """Response to UserDirectRouteGetRequest.
    Contains the direct route setting and the list of DTGs/Trunk Identities assigned to a user."""

    outgoingDTGPolicy: str

    outgoingTrunkIdentityPolicy: str

    directRouteIdentityList: Optional[DirectRouteIdentifiers] = None


@dataclass
class UserDirectedCallPickupWithBargeInGetResponse14sp7(OCIDataResponse):
    """Response to UserDirectedCallPickupWithBargeInGetRequest14sp7."""

    enableBargeInWarningTone: bool

    enableAutomaticTargetSelection: bool


@dataclass
class UserDnGetActivationListResponse(OCIDataResponse):
    """Response to UserDnGetActivationListRequest.
    The response contains a table with columns: \"Phone Number\", and \"Activated\".
    The \"Phone Number\" column contains a single DN.
    The \"Activated\" column indicates if the phone number is activated or not."""

    dnTable: OCITable


@dataclass
class UserDoNotDisturbGetResponse(OCIDataResponse):
    """Response to UserDoNotDisturbGetRequest."""

    isActive: bool

    ringSplash: bool


@dataclass
class UserEnhancedCallLogsGetListResponse23(OCIDataResponse):
    """Response to UserEnhancedCallLogsGetListRequest23.
    Total numbers of rows is:
    - the total number of retrievable logs of the call log type that was specified in the UserEnhancedCallLogsGetListRequest22,
      if a call log type was specified in the request.
    - the total number of retrievable logs, if no call log type was specified in the request.
    A list of MixedCallLogsEntry will be returned if the call logs are stored on CDS
    A list of ExtendedMixedCallLogsEntry22 will be returned if the call logs are stored on DBS or Couchbase
    The logs are sorted by date/time of the call."""

    totalNumberOfRows: int

    legacyEntry: object

    extendedEntry: object


@dataclass
class UserEnterpriseCommonPhoneListGetPagedSortedListResponse(OCIDataResponse):
    """Response to the UserEnterpriseCommonPhoneListGetPagedSortedListRequest. The response
    contains the enterprise's common phone list. The response contains a
    table with column headings: \"Name\" and \"Phone Number\"."""

    totalNumberOfRows: int

    enterpriseCommonPhoneListTable: OCITable


@dataclass
class UserExecutiveAssistantGetResponse(OCIDataResponse):
    """Response to the UserExecutiveAssistantGetRequest.
    Contains the executive assistant setting and a table of executives this assistant has been assigned to.
    The criteria table's column headings are: \"User Id\", \"Last Name\", \"First Name\", \", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\",
    \"Assistant Opt-in Status\" and \"Executive Allow Opt-in\".
    The possible values for \"Assistant Opt-in Status\" and \"Executive Allow Opt-in\" columns are \"true\" and \"false\"."""

    enableDivert: bool

    executiveTable: OCITable

    divertToPhoneNumber: Optional[str] = None


@dataclass
class UserExecutiveGetAssistantResponse(OCIDataResponse):
    """Response to the UserExecutiveGetAssistantsRequest.
    Contains the assistant setting and a table of assigned assistants.
    The table has column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"Opt-in\",
    \"User External Id\" and \"User Place Type\".
    The possible values for \"Opt-in\" column are \"true\" and \"false\".
    The possible values for \"User Place Type\" are: User, Place."""

    allowOptInOut: bool

    assistantUserTable: OCITable


@dataclass
class UserExecutiveGetAvailableAssistantListResponse(OCIDataResponse):
    """Response to the UserExecutiveGetAvailableAssistantListResponse.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\",
    \"User External Id\" and \"User Place Type\".
    The possible values for \"User Place Type\" are: User, Place."""

    userTable: OCITable


@dataclass
class UserExecutiveGetFilteringResponse(OCIDataResponse):
    """Response to the UserExecutiveGetFilteringRequest.
    Contains the filtering setting and a table of filtering criteria.
    The criteria table's column headings are: \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\",
    \"Filter\", \"Holiday Schedule\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The \"Filter\" column can contain \"true\" or \"false\".
    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      - Mobility
    The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - For Mobility Calls To Type, this is always blank.
      - When no extension is available a blank space is provided instead."""

    enableFiltering: bool

    filteringMode: str

    simpleFilterType: str

    criteriaTable: OCITable


@dataclass
class UserExecutiveGetFilteringSelectiveCriteriaResponse21(OCIDataResponse):
    """Response to the UserExecutiveGetFilteringSelectiveCriteriaRequest21."""

    filter: bool

    fromDnCriteria: ExecutiveCallFilteringCriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserExecutiveGetScreeningAlertingResponse(OCIDataResponse):
    """Response to the UserExecutiveGetScreeningAlertingRequest.
    Contains the screening and alerting settings for an executive."""

    enableScreening: bool

    screeningAlertType: str

    alertBroadWorksMobilityLocation: bool

    alertBroadWorksAnywhereLocations: bool

    alertSharedCallAppearanceLocations: bool

    alertingMode: str

    alertingCallingLineIdNameMode: str

    alertingCallingLineIdPhoneNumberMode: str

    callPushRecallNumberOfRings: int

    nextAssistantNumberOfRings: int

    enableRollover: bool

    rolloverAction: str

    alertingCustomCallingLineIdName: Optional[str] = None

    unicodeAlertingCustomCallingLineIdName: Optional[str] = None

    alertingCustomCallingLineIdPhoneNumber: Optional[str] = None

    rolloverWaitTimeSeconds: Optional[int] = None

    rolloverForwardToPhoneNumber: Optional[str] = None


@dataclass
class UserExternalCallingLineIDDeliveryGetResponse(OCIDataResponse):
    """Response to UserExternalCallingLineIDDeliveryGetRequest."""

    isActive: bool


@dataclass
class UserExternalCustomRingbackGetResponse(OCIDataResponse):
    """Response to UserExternalCustomRingbackGetRequest."""

    isActive: bool

    useSettingLevel: str

    sipRequestURI: Optional[str] = None


@dataclass
class UserFaxMessagingGetResponse17sp1(OCIDataResponse):
    """Response to UserFaxMessagingGetRequest17sp1."""

    isActive: bool

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    alias: List[str] = field(default_factory=list)


@dataclass
class UserFeatureAccessCodeGetListResponse21(OCIDataResponse):
    """Response to the UserFeatureAccessCodeGetListRequest21.

    In release 20 the \"Call Recording\" FAC name is changed to
    \"Call Recording Start\"."""

    featureAccessCode: List[FeatureAccessCodeReadEntry] = field(default_factory=list)


@dataclass
class UserFlexibleSeatingGuestGetAvailableHostListResponse(OCIDataResponse):
    """Response to the UserFlexibleSeatingGuestGetAvailableHostListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"Association Limit Hours\", \"Enable Association Limit\","""

    hostUserTable: OCITable


@dataclass
class UserFlexibleSeatingGuestGetResponse22(OCIDataResponse):
    """Response to UserFlexibleSeatingGuestGetRequest22."""

    isActive: bool

    enableAssociationLimit: bool

    associationLimitHours: int

    unlockPhonePINCode: Optional[str] = None

    accessDeviceEndpoint: Optional[AccessDeviceMultipleContactEndpointRead22] = None

    hostUserId: Optional[str] = None

    hostLastName: Optional[str] = None

    hostFirstName: Optional[str] = None

    hostAssociationDateTime: Optional[str] = None

    hostEnforcesAssociationLimit: Optional[bool] = None

    hostAssociationLimitHours: Optional[int] = None


@dataclass
class UserGetListInGroupPagedSortedListResponse(OCIDataResponse):
    """Response to UserGetListInGroupPagedSortedListRequest.
    Contains a table with column headings : \"User Id\",
    \"Last Name\", \"First Name\", \"Department\", \"Department Type\",
    \"Parent Department\",\"Parent Department Type\", \"Phone Number\",
    \"Phone Number Activated\", \"Email Address\",  \"Hiragana Last Name\",
    \"Hiragana First Name\", \"In Trunk Group\", \"Extension\", \"Country Code\",
    \"National Prefix\", \"User External Id\" in a row for each user.

    The \"Department Type\" and \"Parent Department Type\" columns
    will contain the values \"Enterprise\" or \"Group\".

    The following columns are only populated in AS data mode:
      \"Country Code\", \"National Prefix\", \"User External Id\" """

    userTable: OCITable


@dataclass
class UserGetListInGroupResponse(OCIDataResponse):
    """Response to UserGetListInGroupRequest.
    Contains a table with column headings : \"User Id\",
    \"Last Name\", \"First Name\", \"Department\", \"Phone Number\", \"Phone Number Activated\", \"Email Address\",  \"Hiragana Last Name\", \"Hiragana First Name\", \"In Trunk Group\", \"Extension\", \"Country Code\", \"National Prefix\"
    in a row for each user.

    The following columns are only returned in AS data mode:
      \"Country Code\", \"National Prefix"""

    userTable: OCITable


@dataclass
class UserGetListInServiceProviderResponse(OCIDataResponse):
    """Response to UserGetListInServiceProviderRequest.
    Contains a table with column headings : \"User Id\", \"Group Id\",
    \"Last Name\", \"First Name\", \"Department\", \"Phone Number\", \"Phone Number Activated\", \"Email Address\", \"Hiragana Last Name\", \"Hiragana First Name\", \"In Trunk Group\", \"Extension\", \"User External Id\"
    in a row for each user.
    The following columns are populated in AS data mode only:
      \"User External Id\" """

    userTable: OCITable


@dataclass
class UserGetListInSystemResponse(OCIDataResponse):
    """Response to UserGetListInSystemRequest.
    Contains a table with column headings : \"User Id\", \"Group Id\", \"Service Provider Id\", \"Last Name\", \"First Name\",
    \"Department\", \"Phone Number\", \"Phone Number Activated\", \"Email Address\",  \"Hiragana Last Name\", \"Hiragana First Name\", \"In Trunk Group\", \"Extension\", \"Reseller Id\", \"User External Id\"
    in a row for each user.

    The following columns are only returned in AS data mode:
      \"Reseller Id\"
      \"User External Id\" """

    userTable: OCITable


@dataclass
class UserGetLoginInfoResponseRI(OCIDataResponse):
    """Response to UserGetLoginInfoRequestRI

    The following data elements are only used in AS data mode:
      resellerId
      lockoutPeriodExpiry

    If a phoneNumber is returned, it will be the primary DN of the user
    The parameter
     tokenRevocationTime is represented in the number of milliseconds
    since January 1, 1970, 00:00:00 GMT, and it is set to the more current time between
    the system level token revocation time and user level token revocation time.

    The parameter lockoutPeriodExpiry represents the time remaining (in minutes) to re-enable the locked user."""

    loginType: str

    locale: str

    encoding: str

    isEnterprise: bool

    userId: str

    groupId: Optional[str] = None

    serviceProviderId: Optional[str] = None

    passwordExpiresDays: Optional[int] = None

    lastName: Optional[str] = None

    firstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    resellerId: Optional[str] = None

    tokenRevocationTime: Optional[int] = None

    lockoutPeriodExpiry: Optional[int] = None


@dataclass
class UserGetRegistrationListResponse(OCIDataResponse):
    """Response to UserGetRegistrationListRequest.

    The registrationTable table column headings are:
      \"Device Level\", \"Device Name\", \"Order\", \"URI\", \"Expiration\", \"Line/Port\", \"Endpoint Type\", \"Public Net Address\", \"Public Port\", \"Private Net Address\", \"Private Port\", \"User Agent\", \"Lockout Started\", \"Lockout Expires\", \"Lockout Count\", \"Access Info\",
      \"Private Identity\", \"SIP Instance ID\", \"Supports Only CS Media\", \"Feature Parameters\", \"Supports Voice Over PS\", \"Path Header\", \"Registration Active\", \"P-Access-Network-Info\"
    The following columns are only used in AS data mode:
      \"Order\", \"Public Net Address\", \"Public Port\", \"Private Net Address\", \"Private Port\", \"Lockout Started\", \"Lockout Expires\", \"Lockout Count\", \"Path Header\", \"P-Access-Network-Info\".
    The following columns are only used in XS data mode:
      \"Private Identity\", \"SIP Instance ID\", \"Supports Only CS Media\", \"Feature Parameters\", \"Supports Voice Over PS\".
    The following columns are only used in AS data mode:
      \"Registration Active\".
    The \"Device Level\" column contains one of the AccessDeviceLevel enumerated constants.
    The expiration column will be empty when the registration is static. In XS data mode, its value will be 0 when the registration is dynamic regardless of the registration's actual expiration date.
    The Endpoint Type column contains one of the enumerated EndpointType values.
    The Endpoint Type is empty when the registration is against a TELURI.
    The table is sorted by: telURI (after SIPURI), Line/Port, static (after dynamic), order.
    Lockout times are shown in GMT offset. When a permanent lockout is shown, the \"Lockout Expires\" column is empty and the \"Lockout Count\" column contains the word Permanent."""

    registrationTable: OCITable


@dataclass
class UserGetResponse23V2(OCIDataResponse):
    """Response to UserGetRequest23V2.
    It is possible that the TrunkAddressingRead element is present with nothing populated in it which means the user is a trunk user.

    The following data elements are only used in AS data mode and not returned in XS data mode:
      contact[2]-contact[5]
      userId
      nameDialingName
      alternateUserId
      resellerId
      serviceProviderExternalId
      groupExternalId
      userExternalId
      userPersonId
      isPlace
      locationDialingCode

    The following data elements are only used in XS data mode:
      alternateTrunkIdentityDomain

    The following data elements are only used in AS data mode:
      userId
      resellerId

    The following data elements are only used in XS data mode:
      alternateTrunkIdentityDomain
      allowVideo, value \"true\" is returned in AS data mode.

    The userId returned in this response is the user's primary userId and may not be the userId passed in the request.

    The country code (countryCode) included is the user's phone number country code when the user has a phone number assigned, or the
    user's Group associated country code when the user does not have a phone number assigned, or the system default country code when the
    user's Group does not have an associated country code.

    The nationalPrefix in this response is the one associated to the included countryCode.

    The callingLineIdPhoneNumber is no longer being formatted for display purpose. The value is returned exactly the same as being stored."""

    serviceProviderId: str

    groupId: str

    userId: str

    lastName: str

    firstName: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    language: str

    timeZone: str

    timeZoneDisplayName: str

    defaultAlias: str

    countryCode: str

    allowVideo: bool

    nameDialingName: Optional[NameDialingName] = None

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None

    department: Optional[DepartmentKey] = None

    departmentFullPath: Optional[str] = None

    alias: List[str] = field(default_factory=list)

    accessDeviceEndpoint: Optional[
        AccessDeviceMultipleIdentityAndContactEndpointRead22V2
    ] = None

    trunkAddressing: Optional[TrunkAddressingMultipleContactRead22] = None

    title: Optional[str] = None

    pagerPhoneNumber: Optional[str] = None

    mobilePhoneNumber: Optional[str] = None

    emailAddress: Optional[str] = None

    yahooId: Optional[str] = None

    addressLocation: Optional[str] = None

    address: Optional[StreetAddress] = None

    nationalPrefix: Optional[str] = None

    networkClassOfService: Optional[str] = None

    officeZoneName: Optional[str] = None

    primaryZoneName: Optional[str] = None

    impId: Optional[str] = None

    alternateUserId: List[AlternateUserIdEntry] = field(default_factory=list)

    resellerId: Optional[str] = None

    serviceProviderExternalId: Optional[str] = None

    groupExternalId: Optional[str] = None

    userExternalId: Optional[str] = None

    userPersonId: Optional[str] = None

    isPlace: Optional[bool] = None

    locationDialingCode: Optional[str] = None


@dataclass
class UserGetServiceInstanceListInServiceProviderResponse(OCIDataResponse):
    """Response to UserGetServiceInstanceListInServiceProviderRequest.
    Contains a table with column headings :  \"User Id\", \"Group Id\", \"Service Type\",
    \"Name\", \"Phone Number\", \"Extension\", \"Department\" in a row for each Service Instance.  Possible values for Service Type column are ServiceType enums."""

    serviceInstanceTable: OCITable


@dataclass
class UserGetServiceInstanceListInSystemResponse(OCIDataResponse):
    """Response to UserGetServiceInstanceListInSystemRequest.
    Contains a table with column headings : \"User Id\", \"Group Id\", \"Service Provider Id\", \"Service Type\", \"Name\", \"Phone Number\",
    \"Extension\", \"Reseller Id\" in a row for each Service Instance. Possible values for Service Type column are ServiceType enums.
    The following columns are only returned in AS data mode:
      \"Reseller Id\" """

    serviceInstanceTable: OCITable


@dataclass
class UserGroupCommonPhoneListGetPagedSortedListResponse(OCIDataResponse):
    """Response to the UserGroupCommonPhoneListGetPagedSortedListRequest.
    The response contains the group's common phone list. The response
    contains a table with column headings: \"Name\" and \"Phone Number\"."""

    totalNumberOfRows: int

    groupCommonPhoneListTable: OCITable


@dataclass
class UserGroupCustomContactDirectoryGetPagedSortedListResponse(OCIDataResponse):
    """Response to the UserGroupCustomContactDirectoryGetPagedSortedListRequest.

                            Returns the number of entries that would be returned if the response
                            Was not page size restricted.

                            The response contains all the contacts in the group's given custom
                            contact directory. Contains a table with column headings: \"User Id\",
                            \"Last Name\", \"First Name\", \"Hiragana Last Name\",
                            \"Hiragana First Name\", \"Virtual On-Net Phone Number\", \"Group Id\",
                            \"Is Virtual On-Net User\", \"Department\", \"Phone Number\", \"Extension\",
                            \"Mobile\", \"Email Address\", \"Yahoo Id\", \"Title\", \"IMP Id\", \"Receptionist Note\".
                            If the entry represents a Virtual On-Net user then \"User Id\" is blank,
                            the \"Virtual On-Net Phone Number\" contains the phone Number of the
                            Virtual On-Net user, the \"Group Id\" contains the Virtual On-Net
                            user's
                            group and the \"Is Virtual On-Net User\" contains true.
                            If the entry represents a BroadWorks user then the \"User Id\" contains
                            his BroadWorks userId, the \"Virtual On-Net Phone Number\" and
                            \"Group Id\" fields are field is blank and the \"Is Virtual On-Net User\"
                            contains false.  The Receptionist Note column is only populated, if the
    user sending the request is the owner of this Receptionist Note and a
    Note exists."""

    totalNumberOfRows: int

    userTable: OCITable


@dataclass
class UserGroupNightForwardingGetResponse(OCIDataResponse):
    """Response to UserGroupNightForwardingGetRequest.
    businessHours and holidaySchedule are returned in the response only when groupNightForwarding is ‘Auto On’."""

    nightForwarding: str

    groupNightForwarding: str

    businessHours: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None


@dataclass
class UserGroupPagingGetListResponse(OCIDataResponse):
    """Response to the UserGroupPagingGetListRequest.
    The groupPagingTable contains columns: \"Name\", \"Phone Number\", \"Extension\" and \"Is Active\"
    The column value for \"Is Active\" can either be true, or false."""

    pagingGroupTable: OCITable


@dataclass
class UserHotelingGuestGetAvailableUserListResponse(OCIDataResponse):
    """Response to the UserHotelingGuestGetAvailableUserListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Association Limit Hours\", \"Enable Association Limit\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\"."""

    hostUserTable: OCITable


@dataclass
class UserHotelingGuestGetResponse14sp4(OCIDataResponse):
    """Response to UserHotelingGuestGetRequest14sp4"""

    isActive: bool

    enableAssociationLimit: bool

    associationLimitHours: int

    hostUserId: Optional[str] = None

    hostLastName: Optional[str] = None

    hostFirstName: Optional[str] = None

    hostAssociationDateTime: Optional[str] = None

    hostEnforcesAssociationLimit: Optional[bool] = None

    hostAssociationLimitHours: Optional[int] = None


@dataclass
class UserHotelingHostGetResponse17(OCIDataResponse):
    """Response to UserHotelingHostGetRequest17."""

    isActive: bool

    enforceAssociationLimit: bool

    associationLimitHours: int

    accessLevel: str

    guestLastName: Optional[str] = None

    guestFirstName: Optional[str] = None

    guestPhoneNumber: Optional[str] = None

    guestExtension: Optional[str] = None

    guestLocationDialingCode: Optional[str] = None

    guestAssociationDateTime: Optional[str] = None


@dataclass
class UserINIntegrationGetResponse(OCIDataResponse):
    """Response to UserINIntegrationGetRequest"""

    originatingServiceKey: Optional[int] = None

    terminatingServiceKey: Optional[int] = None


@dataclass
class UserInCallServiceActivationGetResponse(OCIDataResponse):
    """Response to UserInCallServiceActivationGetRequest."""

    isActive: bool


@dataclass
class UserIncomingCallingPlanGetResponse(OCIDataResponse):
    """Response to UserIncomingCallingPlanGetRequest."""

    useCustomSettings: bool

    userPermissions: IncomingCallingPlanPermissions


@dataclass
class UserIntegratedIMPGetResponse21sp1(OCIDataResponse):
    """Response to the UserIntegratedIMPGetRequest21sp1.
    The response contains the Integrated IMP specific service attributes for the user.
    The following elements are only used in AS data mode and not returned in XS data mode:
      impId
      isAlternateImpId"""

    isActive: bool

    impId: Optional[str] = None

    isAlternateImpId: Optional[bool] = None


@dataclass
class UserInterceptUserGetResponse21sp1(OCIDataResponse):
    """Response to the UserInterceptUserGetRequest21sp1.

    The following elements are only used in AS data mode:
      exemptInboundMobilityCalls
      exemptOutboundMobilityCalls
      disableParallelRingingToNetworkLocations"""

    isActive: bool

    announcementSelection: str

    inboundCallMode: str

    alternateBlockingAnnouncement: bool

    exemptInboundMobilityCalls: bool

    disableParallelRingingToNetworkLocations: bool

    routeToVoiceMail: bool

    playNewPhoneNumber: bool

    transferOnZeroToPhoneNumber: bool

    outboundCallMode: str

    exemptOutboundMobilityCalls: bool

    rerouteOutboundCalls: bool

    audioFileDescription: Optional[str] = None

    audioMediaType: Optional[str] = None

    videoFileDescription: Optional[str] = None

    videoMediaType: Optional[str] = None

    newPhoneNumber: Optional[str] = None

    transferPhoneNumber: Optional[str] = None

    outboundReroutePhoneNumber: Optional[str] = None


@dataclass
class UserInternalCallingLineIDDeliveryGetResponse(OCIDataResponse):
    """Response to UserInternalCallingLineIDDeliveryGetRequest."""

    isActive: bool


@dataclass
class UserLegacyAutomaticCallbackGetResponse(OCIDataResponse):
    """Response to UserLegacyAutomaticCallbackGetRequest."""

    isActive: bool


@dataclass
class UserLinePortGetListResponse(OCIDataResponse):
    """Response to UserLinePortGetListRequest.
    Contains a table of line ports configured for a user
    The column headings are: \"Line Port\", \"Line Port Type\", \"In Trunk Group\",
    \"Contact\", \"Contact2\", \"Contact3\", \"Contact4\", \"Contact5\", \"Authentication Mode\",
    and \"Auto-Config Soft Client\"."""

    linePortTable: OCITable


@dataclass
class UserMWIDeliveryToMobileEndpointGetResponse23(OCIDataResponse):
    """Response to UserMWIDeliveryToMobileEndpointGetRequest23."""

    isActive: bool

    sendMissedCallAlert: bool

    mobilePhoneNumber: Optional[str] = None


@dataclass
class UserMaliciousCallTraceGetResponse(OCIDataResponse):
    """Response to UserMaliciousCallTraceGetRequest."""

    isActive: bool

    traceTypeSelection: str

    traceForTimePeriod: bool

    traceTimePeriod: Optional[MaliciousCallTraceTimePeriod] = None


@dataclass
class UserMeetMeConferencingAddConferenceResponse23(OCIDataResponse):
    """Response to UserMeetMeConferencingAddConferenceRequest23.
    Contains the information of a conference."""

    conferenceId: str

    moderatorPin: str

    securityPin: Optional[str] = None


@dataclass
class UserMeetMeConferencingGetAvailableDelegateListResponse(OCIDataResponse):
    """Response to UserMeetMeConferencingGetAvailableDelegateListRequest.
    Contains all hosts assigned on a bridge.
    The table has column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\" and \"Email Address\"."""

    conferenceDelegateUserTable: OCITable


@dataclass
class UserMeetMeConferencingGetBridgeListResponse(OCIDataResponse):
    """Response to the UserMeetMeConferencingGetBridgeListRequest.
    Contains a table with column headings: \"Bridge Id\", \"Name\", \"Phone Number\", \"Extension\", \"Ports\", \"Is Active\",
    \"Allow Individual OutDial\", \"Country Code\", and \"National Prefix\".
    The column values for \"Is Active\" can either be true, or false."""

    conferenceBridgeTable: OCITable


@dataclass
class UserMeetMeConferencingGetConferenceDelegateListResponse(OCIDataResponse):
    """Response to UserMeetMeConferencingGetConferenceDelegateListRequest.
    Contains a table with table heading:\"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\",\"Phone Number\", \"Extension\", \"Department\" and \"Email Address\"."""

    conferenceDelegateUserTable: OCITable


@dataclass
class UserMeetMeConferencingGetConferenceGreetingResponse20(OCIDataResponse):
    """Response to UserMeetMeConferencingGetConferenceGreetingRequest20.
    Contains the information of a conference custom greeting."""

    playEntranceGreeting: bool

    entranceGreetingFile: Optional[AnnouncementFileKey] = None


@dataclass
class UserMeetMeConferencingGetConferenceListResponse(OCIDataResponse):
    """Response to the UserMeetMeConferencingGetConferenceListRequest.
    Contains a table with column headings: \"Bridge Id\", \"Conference Id\", \"Title\", \"Bridge Name\", \"Status\", \"Type\", \"Start Time\", \"Host Last Name\", \"Host First Name\" and \"Host\".
    The column values for \"Status\" can be Active, Inactive, or Expired.
    The column values for \"Type\" can be Reservationless, One Time, Recurring Daily, Recurring Weekly, Recurring Monthly, or Recurring Yearly.
    Start Time is in the format \"yyyy-MM-dd'T'HH:mm:ss:SSSZ\". Example: 2010-10-01T09:30:00:000-0400."""

    conferenceTable: OCITable


@dataclass
class UserMeetMeConferencingGetConferenceRecordingListResponse(OCIDataResponse):
    """Response to the UserMeetMeConferencingGetConferenceRecordingListRequest.
    Contains a table with column headings: \"Bridge Id\", \"Conference Id\", \"Conference Title\", \"Bridge Name\", \"Start Time\", \"File Size\", and \"URL\".
    Start Time is in the format \"yyyy-MM-dd'T'HH:mm:ss:SSSZ\". Example: 2010-10-01T09:30:00:000-0400."""

    conferenceRecordingTable: OCITable


@dataclass
class UserMeetMeConferencingGetConferenceResponse23(OCIDataResponse):
    """Response to UserMeetMeConferencingGetConferenceRequest23.
    Contains the information of a conference."""

    title: str

    restrictParticipants: bool

    maxParticipants: int

    muteAllAttendeesOnEntry: bool

    endConferenceOnModeratorExit: bool

    moderatorRequired: bool

    requireSecurityPin: bool

    allowUniqueIdentifier: bool

    attendeeNotification: str

    conferenceSchedule: MeetMeConferencingConferenceSchedule

    moderatorPin: str

    hostTimeZone: str

    allowParticipantUnmuteInAutoLectureMode: bool

    estimatedParticipants: Optional[int] = None

    accountCode: Optional[str] = None

    securityPin: Optional[str] = None


@dataclass
class UserModifyGroupIdResponse(OCIDataResponse):
    """Response to UserModifyGroupIdRequest.
    error indicates the failing conditions preventing the user move.
    impact indicates any change to user and group as the result of a user move."""

    error: List[UserMoveMessage] = field(default_factory=list)

    impact: List[UserMoveMessage] = field(default_factory=list)


@dataclass
class UserMusicOnHoldGetResponse(OCIDataResponse):
    """Response to UserMusicOnHoldGetRequest."""

    isActive: bool


@dataclass
class UserMusicOnHoldUserGetResponse20(OCIDataResponse):
    """Response to UserMusicOnHoldUserGetRequest20."""

    enableVideo: bool

    source: MusicOnHoldUserSourceRead20

    useAlternateSourceForInternalCalls: bool

    internalSource: Optional[MusicOnHoldUserSourceRead20] = None


@dataclass
class UserNetworkConferencingGetResponse(OCIDataResponse):
    """Response to UserNetworkConferencingGetRequest."""

    maxConferenceParties: int

    conferenceURI: Optional[str] = None


@dataclass
class UserNumberPortabilityAnnouncementGetResponse(OCIDataResponse):
    """Response to the UserNumberPortabilityAnnouncementGetRequest.
    The response contains the user Number Portability attributes."""

    enable: bool


@dataclass
class UserOCICallControlApplicationGetListResponse(OCIDataResponse):
    """Response to UserOCICallControlApplicationGetListRequest."""

    applicationId: List[str] = field(default_factory=list)


@dataclass
class UserOutgoingCallingPlanAuthorizationCodeGetListResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanAuthorizationCodeGetListRequest."""

    codeEntry: List[OutgoingCallingPlanAuthorizationCodeEntry] = field(
        default_factory=list
    )


@dataclass
class UserOutgoingCallingPlanAuthorizationCodeGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanAuthorizationCodeGetRequest."""

    useCustomSettings: bool


@dataclass
class UserOutgoingCallingPlanCallMeNowGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanCallMeNowGetRequest."""

    useCustomSettings: bool

    userPermissions: OutgoingCallingPlanCallMeNowPermissions


@dataclass
class UserOutgoingCallingPlanDigitPlanCallMeNowGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanDigitPlanCallMeNowGetRequest."""

    useCustomSettings: bool

    userPermissions: Optional[OutgoingCallingPlanDigitPatternCallMeNowPermissions] = (
        None
    )


@dataclass
class UserOutgoingCallingPlanDigitPlanOriginatingGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanDigitPlanOriginatingGetRequest."""

    useCustomSettings: bool

    userPermissions: Optional[OutgoingCallingPlanDigitPatternOriginatingPermissions] = (
        None
    )


@dataclass
class UserOutgoingCallingPlanDigitPlanRedirectingGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanDigitPlanRedirectingGetRequest."""

    useCustomSettings: bool

    userPermissions: Optional[OutgoingCallingPlanDigitPatternRedirectingPermissions] = (
        None
    )


@dataclass
class UserOutgoingCallingPlanOriginatingGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanOriginatingGetRequest."""

    useCustomSettings: bool

    userPermissions: OutgoingCallingPlanOriginatingPermissions


@dataclass
class UserOutgoingCallingPlanPinholeDigitPlanCallMeNowGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanPinholeDigitPlanCallMeNowGetRequest."""

    useCustomSettings: bool

    userPermissions: Optional[
        OutgoingPinholeDigitPlanDigitPatternCallMeNowPermissions
    ] = None


@dataclass
class UserOutgoingCallingPlanPinholeDigitPlanOriginatingGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanPinholeDigitPlanOriginatingGetRequest."""

    useCustomSettings: bool

    userPermissions: Optional[
        OutgoingPinholeDigitPlanDigitPatternOriginatingPermissions
    ] = None


@dataclass
class UserOutgoingCallingPlanPinholeDigitPlanRedirectingGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanPinholeDigitPlanRedirectingGetRequest."""

    useCustomSettings: bool

    userPermissions: Optional[
        OutgoingPinholeDigitPlanDigitPatternRedirectingPermissions
    ] = None


@dataclass
class UserOutgoingCallingPlanRedirectedGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanRedirectedGetRequest."""

    useCustomSettings: bool

    userPermissions: OutgoingCallingPlanRedirectedPermissions


@dataclass
class UserOutgoingCallingPlanRedirectingGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanRedirectingGetRequest."""

    useCustomSettings: bool

    userPermissions: OutgoingCallingPlanRedirectingPermissions


@dataclass
class UserOutgoingCallingPlanSustainedAuthorizationCodeGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanAuthorizationCodeGetRequest."""

    code: Optional[str] = None


@dataclass
class UserOutgoingCallingPlanTransferNumbersGetResponse(OCIDataResponse):
    """Response to UserOutgoingCallingPlanTransferNumbersGetRequest."""

    useCustomSettings: bool

    userNumbers: OutgoingCallingPlanTransferNumbers


@dataclass
class UserPBXIntegrationGetResponse(OCIDataResponse):
    """Response to UserPBXIntegrationGetRequest."""

    proxyToHeaderFromNetwork: bool


@dataclass
class UserPasswordInfoGetResponse22(OCIDataResponse):
    """Response to UserPasswordInfoGetRequest22.

    The following elements are only used in AS data mode and ignored in XS data mode.
    hasPassword"""

    isLoginDisabled: bool

    expirationDays: int

    doesNotExpire: bool

    hasPassword: bool


@dataclass
class UserPersonalAssistantCallToNumberGetListResponse(OCIDataResponse):
    """Response to the UserPersonalAssistantCallToNumberGetListRequest.
    Contains a list of assigned Call to Numbers\"."""

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserPersonalAssistantExclusionNumberGetListResponse(OCIDataResponse):
    """Response to the UserPersonalAssistantExclusionNumberGetListRequest.
    Contains a table with column headings:
    \"Number\", \"Description\"."""

    exclusionNumberTable: OCITable


@dataclass
class UserPersonalAssistantExclusionNumberGetResponse(OCIDataResponse):
    """Response to the UserPersonalAssistantExclusionNumberGetRequest"""

    description: Optional[str] = None


@dataclass
class UserPersonalAssistantGetCriteriaResponse(OCIDataResponse):
    """Response to the UserPersonalAssistantGetCriteriaRequest."""

    presence: str

    enableTransferToAttendant: bool

    enableRingSplash: bool

    alertMeFirst: bool

    alertMeFirstNumberOfRings: int

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    attendantNumber: Optional[str] = None


@dataclass
class UserPersonalAssistantGetResponse24(OCIDataResponse):
    """Response to the UserPersonalAssistantGetRequest24.
    The response contains the user Personal Assistant information and a table of Schedule Selective Criteria entries.
    The schedule table's column headings are: \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Holiday Schedule\",
    \"Presence\", \"Transfer to Attendant\", \"Attendant Number\", \"Play Ring Splash\", \"Alert Me First\", \"Number of Rings\"."""

    presence: str

    enableTransferToAttendant: bool

    enableRingSplash: bool

    enableExpirationTime: bool

    alertMeFirst: bool

    alertMeFirstNumberOfRings: int

    attendantNumber: Optional[str] = None

    expirationTime: Optional[str] = None

    scheduleTable: Optional[OCITable] = None


@dataclass
class UserPersonalPhoneListGetListResponse(OCIDataResponse):
    """Response to the UserPersonalPhoneListGetListRequest.
    The response contains a user's personal phone list."""

    entry: List[PhoneListEntry] = field(default_factory=list)


@dataclass
class UserPersonalPhoneListGetPagedSortedListResponse(OCIDataResponse):
    """Response to the UserPersonalPhoneListGetPagedSortedListRequest.
    The response contains a user's personal phone list. The response
    contains a table with column headings: \"Name\" and \"Phone Number\"."""

    totalNumberOfRows: int

    personalPhoneListTable: OCITable


@dataclass
class UserPhoneDirectoryGetListResponse(OCIDataResponse):
    """Response to UserPhoneDirectoryGetListRequest.
    The \"My Room Room Id\" and \"My Room Bridge Id\" are only populated for users assigned the \"Collaborate-Audio\" service.
    Contains a table with  a row for each phone number and column headings :
    \"Name\", \"Number\", \"Extension\", \"Mobile\", \"Email Address\", \"Department\", \"First Name\", \"Last Name\",
    \"User Id\", \"Title\", \"IMP Id\", \"My Room Room Id\", \"My Room Bridge Id\", \"Service Name\".
    The Service Name represents the localized service name for service instances. The localized values are taken from the BroadworksLabel.properties file.
    Service Name is currently supporting:
    AutoAttendant, AutoAttendantStandard, AutoAttendantVideo, CallCenter, CallCenterStandard, CallCenterPremium
    HuntGroup, InstantGroupCall, VoiceMessagingGroup, RoutePoint, BroadWorksAnywhere, GroupPaging, FindmeFollowme,
    VoiceXML, FlexibleSeatingGuest, CollaborateAudio, MeetMeConferencing.
    For a Regular User or a Virtual On Network Enterprise Extensions, the Service Name is empty.

    The following columns are only returned in AS data mode:
      \"My Room Room Id\", \"My Room Bridge Id\", \"Service Name\" """

    directoryTable: OCITable


@dataclass
class UserPhoneDirectoryGetPagedListResponse(OCIDataResponse):
    """Response to UserPhoneDirectoryGetPagedListRequest.
    Returns the number of entries that would be returned if the response
    Was not page size restricted.
    The \"My Room Room Id\" and \"My Room Bridge Id\" are only populated for
          users assigned the \"Collaborate-Audio\" service.
    Contains a table with a row for each user and column headings:
    \"User Id\", \"First Name\", \"Last Name\", \"First Name Unicode\",
    \"Last Name Unicode\", \"Hiragana First Name\", \"Hiragana Last Name\",
    \"Title\", \"Phone Number\", \"Extension\", \"Mobile\", \"Pager\",
    \"Email Address\", \"Yahoo Id\", \"Department\", \"Group Id\", \"Location\",
    \"Address Line 1\", \"Address Line 2\", \"City\", \"State\", \"Zip\", \"Country\",
    \"IMP Id\", \"Location Code\", \"My Room Room Id\", \"My Room Bridge Id\", \"Service Name\",
    and \"Receptionist Note\".
    The Service Name represents the localized service name for service instances. The localized values are taken from the BroadworksLabel.properties file.
    Service Name is currently supporting:
    AutoAttendant, AutoAttendantStandard, AutoAttendantVideo, CallCenter, CallCenterStandard, CallCenterPremium
    HuntGroup, InstantGroupCall, VoiceMessagingGroup, RoutePoint, BroadWorksAnywhere, GroupPaging, FindmeFollowme,
    VoiceXML, FlexibleSeatingGuest, CollaborateAudio, MeetMeConferencing.
    For a Regular User or a Virtual On Network Enterprise Extensions, the Service Name is empty.
    The response entries are sorted by \"Last Name Unicode\" first and
    \"First Name unicode\" secondarily.

    The following columns are only returned in AS data mode:
    \"Location Code\", \"My Room Room Id\", \"My Room Bridge Id\", \"Service Name\", \"Receptionist Note\"
    The Receptionist Note column is only populated, if the user sending
    the request is the owner of the Receptionist Note and a Note exists."""

    totalNumberOfRows: int

    directoryTable: OCITable


@dataclass
class UserPhoneDirectoryGetPagedSortedListResponse(OCIDataResponse):
    """Response to UserPhoneDirectoryGetPagedSortedListRequest.
    Returns the number of entries that would be returned if the response
    Was not page size restricted.
    The \"My Room Room Id\" and \"My Room Bridge Id\" are only populated for
    users assigned the \"Collaborate-Audio\" service.
    Contains a table with a row for each user and column headings:
    \"User Id\", \"CLID First Name\", \"CLID Last Name\", \"First Name\",
    \"Last Name\", \"Hiragana First Name\", \"Hiragana Last Name\",
    \"Title\", \"Phone Number\", \"Extension\", \"Mobile\", \"Pager\",
    \"Email Address\", \"Yahoo Id\", \"Department\", \"Group Id\", \"Location\",
    \"Address Line 1\", \"Address Line 2\", \"City\", \"State\", \"Zip\",
    \"Country\", \"IMP Id\", \"Location Code\", \"My Room Room Id\",
    \"My Room Bridge Id\", \"Service Name\", \"Receptionist Note\",
    \"User External Id\", and \"User Place Type\".
    The Service Name represents the localized service name for service instances.
    The localized values are taken from the BroadworksLabel.properties file.
    Service Name is currently supporting:
    AutoAttendant, AutoAttendantStandard, AutoAttendantVideo, CallCenter,
    CallCenterStandard, CallCenterPremium, HuntGroup, InstantGroupCall,
    VoiceMessagingGroup, RoutePoint, BroadWorksAnywhere, GroupPaging, FindmeFollowme,
    VoiceXML, FlexibleSeatingGuest, CollaborateAudio, MeetMeConferencing.
    For a Regular User or a Virtual On Network Enterprise Extensions, the
    Service Name is empty.
    The Receptionist Note column is only populated, if the user sending
    the request is the owner of the Receptionist Note and a Note exists.

    The following columns are returned in AS data mode only:
      \"Service Name\", \"Receptionist Notes\", \"User External Id\", \"User Place Type\"."""

    totalNumberOfRows: int

    directoryTable: OCITable


@dataclass
class UserPhoneDirectoryGetSearchedListResponse(OCIDataResponse):
    """Response to UserPhoneDirectoryGetSearchedListRequest.
    The \"My Room Room Id\" and \"My Room Bridge Id\" are only populated for
        users assigned the \"Collaborate-Audio\" service.
    Contains a table with  a row for each phone number and column headings :
    \"Name\", \"Number\", \"Extension\", \"Mobile\", \"Email Address\", \"Department\",
    \"Hiragana Name\", \"Group Id\", \"Yahoo Id\", \"User Id\", \"IMP Id\", \"First Name\", \"Last Name\",
    \"My Room Room Id\", \"My Room Bridge Id\", \"Service Name\".
    The Service Name represents the localized service name for service instances. The localized values are taken from the BroadworksLabel.properties file.
    Service Name is currently supporting:
    AutoAttendant, AutoAttendantStandard, AutoAttendantVideo, CallCenter, CallCenterStandard, CallCenterPremium
    HuntGroup, InstantGroupCall, VoiceMessagingGroup, RoutePoint, BroadWorksAnywhere, GroupPaging, FindmeFollowme,
    VoiceXML, FlexibleSeatingGuest, CollaborateAudio, MeetMeConferencing.
    For a Regular User or a Virtual On Network Enterprise Extensions, the Service Name is empty.

    The following columns are only returned in AS data mode:
      \"My Room Room Id\", \"My Room Bridge Id\", \"Service Name\" """

    directoryTable: OCITable


@dataclass
class UserPhysicalLocationGetResponse(OCIDataResponse):
    """Response to UserPhysicalLocationGetRequest."""

    isActive: bool


@dataclass
class UserPolycomPhoneServicesGetPrimaryEndpointListResponse(OCIDataResponse):
    """Response to UserPolycomPhoneServicesGetPrimaryEndpointListRequest.
    The column headings for the deviceUserTable are: \"Device Level\", \"Device Name\", \"Line/Port\"."""

    deviceUserTable: OCITable


@dataclass
class UserPolycomPhoneServicesGetResponse(OCIDataResponse):
    """Response to UserPolycomPhoneServicesGetRequest."""

    integratePhoneDirectoryWithBroadWorks: bool

    includeUserPersonalPhoneListInDirectory: bool

    includeGroupCustomContactDirectoryInDirectory: bool

    groupCustomContactDirectory: Optional[str] = None


@dataclass
class UserPortalPasscodeGetInfoResponse(OCIDataResponse):
    """Response to UserPortalPasscodeGetInfoRequest."""

    isLoginDisabled: bool

    expirationDays: int

    doesNotExpire: bool

    passcode: str


@dataclass
class UserPortalPasscodeRulesGetResponse(OCIDataResponse):
    """Response to UserPortalPasscodeRulesGetRequest."""

    disallowRepeatedDigits: bool

    numberOfRepeatedDigits: int

    disallowRepeatedPatterns: bool

    disallowContiguousSequences: bool

    numberOfAscendingDigits: int

    numberOfDescendingDigits: int

    disallowUserNumber: bool

    disallowReversedUserNumber: bool

    disallowOldPasscode: bool

    numberOfPreviousPasscodes: int

    disallowReversedOldPasscode: bool

    minCodeLength: int

    maxCodeLength: int

    disableLoginAfterMaxFailedLoginAttempts: bool

    expirePassword: bool

    sendLoginDisabledNotifyEmail: bool

    maxFailedLoginAttempts: Optional[int] = None

    passcodeExpiresDays: Optional[int] = None

    loginDisabledNotifyEmailAddress: Optional[str] = None


@dataclass
class UserPreAlertingAnnouncementGetCriteriaResponse21(OCIDataResponse):
    """Response to the UserPreAlertingAnnouncementGetCriteriaRequest21."""

    blacklisted: bool

    fromDnCriteria: CriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserPreAlertingAnnouncementGetResponse20(OCIDataResponse):
    """Response to a UserPreAlertingAnnouncementGetRequest20.
      The criteria table's column headings are: \"Is Active\", \"Criteria Name\", \"Blacklisted\", \"Calls From\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
       - Primary
       - Alternate X (where x is a number between 1 and 10)
       - Mobility
     The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
       - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
       - When no number is available a blank space is provided instead.
     The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
       - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
       - For Mobility Calls To Type, this is always blank.
       - When no extension is available a blank space is provided instead."""

    isActive: bool

    audioSelection: str

    videoSelection: str

    criteriaTable: OCITable

    audioFile: Optional[AnnouncementFileLevelKey] = None

    audioFileUrl: Optional[str] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    videoFileUrl: Optional[str] = None


@dataclass
class UserPreferredAnswerEndpointGetListResponse(OCIDataResponse):
    """Response to UserPreferredAnswerEndpointGetListRequest.
    Contains a table of devices associated to a user that can be configured
    as Preferred Answer Endpoint.
    The column headings are: \"Line Port\", \"Endpoint Type\", \"Is Preferred Answer Endpoint\", \"Device Name\", \"Device Level\", \"Device Type\".
    The value of the \"Endpoint Type\" column is either Primary, Shared Call Appearance or Flexible Seating Guest."""

    accessDeviceTable: OCITable


@dataclass
class UserPreferredCarrierUserGetResponse(OCIDataResponse):
    """Response to a UserPreferredCarrierUserGetRequest."""

    intraLataCarrier: UserPreferredCarrierName

    interLataCarrier: UserPreferredCarrierName

    internationalCarrier: UserPreferredCarrierName


@dataclass
class UserPrepaidGetResponse(OCIDataResponse):
    """Response to UserPrepaidGetRequest."""

    isActive: bool


@dataclass
class UserPrimaryEndpointAdvancedSettingGetResponse(OCIDataResponse):
    """Response to the UserPrimaryEndpointAdvancedSettingGetRequest."""

    allowOrigination: bool

    allowTermination: bool


@dataclass
class UserPriorityAlertGetCriteriaListResponse(OCIDataResponse):
    """Response to the UserPriorityAlertGetCriteriaListRequest. The criteria table's column headings are:
    \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Blacklisted\", \"Holiday Schedule\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The following columns are only returned in AS data mode:
      \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\"

    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      - Mobility
    The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - For Mobility Calls To Type, this is always blank.
      - When no extension is available a blank space is provided instead."""

    criteriaTable: OCITable


@dataclass
class UserPriorityAlertGetCriteriaResponse21(OCIDataResponse):
    """Response to the UserPriorityAlertGetCriteriaRequest21."""

    blacklisted: bool

    fromDnCriteria: PriorityAlertCriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserPrivacyGetAvailableMonitorsUserListResponse(OCIDataResponse):
    """Response to the UserPrivacyGetAvailableMonitorsUserListRequest.
    Returns a 10 column table with column headings:
    \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"IMP Id\"."""

    availableMonitorsTable: OCITable


@dataclass
class UserPrivacyGetResponse13mp17(OCIDataResponse):
    """Response to UserPrivacyGetRequest13mp17.  The
    permittedMonitorUserIdTable contains the members of
    the enterprise or group allowed to monitor the phone
    status of the user specified in the request.  Members
    of this table are allowed to monitor the user even if
    enablePhoneStatusPrivacy is set to true.  The table
    contains column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"IMP Id\"."""

    enableDirectoryPrivacy: bool

    enableAutoAttendantExtensionDialingPrivacy: bool

    enableAutoAttendantNameDialingPrivacy: bool

    enablePhoneStatusPrivacy: bool

    permittedMonitorUserIdTable: OCITable


@dataclass
class UserPushNotificationGetResponse24(OCIDataResponse):
    """Response to UserPushNotificationGetRequest24."""

    sendPushNotificationForClickToDial: bool

    sendPushNotificationForGroupPaging: bool


@dataclass
class UserPushNotificationRegistrationGetListResponse23(OCIDataResponse):
    """Response to UserPushNotificationRegistrationGetListRequest23.

    A registration has more than one row in the response when the registration includes more than one token
    and/or one or more event.  There can be one more tokens per registration ID and there can be one or more
    events per token.

    Registration Date uses the format \"yyyy-MM-dd'T'HH:mm:ss.SSSZ\" in the time zone of the requested user.
    Example: 2010-10-01T09:30:00:000-0400."""

    userId: str

    pushNotificationRegistrationData: List[PushNotificationRegistrationData23] = field(
        default_factory=list
    )


@dataclass
class UserPushToTalkGetAvailableUserListResponse(OCIDataResponse):
    """Response to the UserPushToTalkGetAvailableUserListRequest.
    Returns a 10 column table with column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"IMP Id\"."""

    userTable: OCITable


@dataclass
class UserPushToTalkGetResponse(OCIDataResponse):
    """Response to UserPushToTalkGetRequest.  It returns the service settings and a
    9 column selected user table with the following column headings:
      \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
      \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"IMP Id\"."""

    allowAutoAnswer: bool

    outgoingConnectionSelection: str

    accessListSelection: str

    selectedUserTable: OCITable


@dataclass
class UserRemoteOfficeGetResponse(OCIDataResponse):
    """Response to UserRemoteOfficeGetRequest."""

    isActive: bool

    remoteOfficePhoneNumber: Optional[str] = None


@dataclass
class UserResourcePriorityGetResponse(OCIDataResponse):
    """Response to UserResourcePriorityGetRequest.
    Contains the Resource Priority settings of a user.
    If useDefaultResourcePriority is true, parameter resourcePriority will not be returned."""

    useDefaultResourcePriority: bool

    defaultResourcePriority: str

    userResourcePriority: str


@dataclass
class UserRouteListGetResponse24(OCIDataResponse):
    """Response to UserRouteListGetRequest24.
    Contains the route list setting and a list of assigned number ranges and number prefixes.
    The column headings for assignedNumberRangeTable are \"Number Range Start\", \"Number Range End\", \"Is Active\" and \"Extension Length\".
    The column headings for assignedNumberPrefixTable are \"Number Prefix\" \",\"Is Active\", \"Extension Range Start\" and \"Extension Range End\"."""

    treatOriginationsAndPBXRedirectionsAsScreened: bool

    useRouteListIdentityForNonEmergencyCalls: bool

    useRouteListIdentityForEmergencyCalls: bool

    ignoreCallingNameForCallProcessing: bool

    assignedNumberRangeTable: OCITable

    assignedNumberPrefixTable: OCITable


@dataclass
class UserRoutePointCallDispositionCodeGetAvailableListResponse(OCIDataResponse):
    """Response to the UserRoutePointCallDispositionCodeGetAvailableListRequest.
    This list may include Group/Enterprise level codes in addition to the Route Point level codes,
    depending on the call center disposition codes settings.
    Only active codes are included in the list.
    Contains a table with column headings: \"Code\", \"Description\" and \"Level\".
    Level column can be any of the values in the data type CallDispositionCodeLevel."""

    dispositionCodesTable: OCITable


@dataclass
class UserRoutePointSupervisorGetListResponse(OCIDataResponse):
    """Response to the UserRoutePointSupervisorGetListRequest.
    Contains a table with column headings: \"User Id\", \"Last Name\",
    \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\",
            \"Location Code\"."""

    supervisorTable: OCITable


@dataclass
class UserSMDIMessageDeskGetResponse(OCIDataResponse):
    """Response to the UserSMDIMessageDeskGetRequest."""

    isActive: bool

    messageDeskNumber: Optional[str] = None


@dataclass
class UserSMDIMessageDeskGetServerListResponse(OCIDataResponse):
    """Response to the UserSMDIMessageDeskGetServerListRequest.
    The SMDI Server table column headings are: \"Device Name\", \"Net Address\", \"Port\"."""

    smdiServerTable: OCITable


@dataclass
class UserScheduleGetEventDetailListResponse(OCIDataResponse):
    """Response to UserScheduleGetEventRequest.
    The response contains collection of event details of a requested schedule."""

    scheduleEvents: List[ScheduleEvents] = field(default_factory=list)


@dataclass
class UserScheduleGetEventListResponse(OCIDataResponse):
    """Response to UserScheduleGetEventListRequest.
    The response contains a list of events."""

    eventName: List[str] = field(default_factory=list)


@dataclass
class UserScheduleGetEventResponse(OCIDataResponse):
    """Response to UserScheduleGetEventRequest.
    The response contains the event of the user schedule."""

    startDate: int

    allDayEvent: bool

    startTime: HourMinute

    endTime: HourMinute

    endDate: int

    recurrence: Optional[Recurrence] = None


@dataclass
class UserScheduleGetListResponse17sp1(OCIDataResponse):
    """Response to UserScheduleGetListRequest17sp1.
    The response contains a list of schedules viewable by the user. It contains the schedules
    defined for the user and the group the user belongs to. If the user belongs to an enterprise,
    the list also contains the schedules defined for the enterprise."""

    scheduleGlobalKey: List[ScheduleGlobalKey] = field(default_factory=list)


@dataclass
class UserScheduleGetPagedSortedListResponse(OCIDataResponse):
    """Response to UserScheduleGetPagedSortedListRequest.
    Contains a 3 column table with column headings: \"Name\", \"Type\", \"Level\"
    and a row for each schedule."""

    scheduleTable: OCITable


@dataclass
class UserSecurityClassificationGetResponse22(OCIDataResponse):
    """Response to the UserSecurityClassificationGetRequest22.
    The following elements are not returned in AS and XS data mode:
      customizedSecurityClassification"""

    securityClassification: Optional[str] = None

    customizedSecurityClassification: Optional[str] = None


@dataclass
class UserSelectiveCallAcceptanceGetCriteriaListResponse(OCIDataResponse):
    """Response to the UserSelectiveCallAcceptanceGetCriteriaListRequest.
    The criteria table's column headings are:
    \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Blacklisted\", \"Holiday Schedule\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The following columns are only returned in AS data mode:
      \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\"

    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      - Mobility
    The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - For Mobility Calls To Type, this is always blank.
      - When no extension is available a blank space is provided instead."""

    criteriaTable: OCITable


@dataclass
class UserSelectiveCallAcceptanceGetCriteriaResponse21(OCIDataResponse):
    """Response to the UserSelectiveCallAcceptanceGetCriteriaRequest21."""

    blacklisted: bool

    fromDnCriteria: CriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserSelectiveCallRejectionGetCriteriaListResponse(OCIDataResponse):
    """Response to the UserSelectiveCallRejectionGetCriteriaListRequest.
    The criteria table's column headings are:
    \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Blacklisted\", \"Holiday Schedule\", \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\".
    The following columns are only returned in AS data mode:
      \"Calls To Type\", \"Calls To Number\" and \"Calls To Extension\"

    The possible values for the \"Calls To Type\" column are the following or a combination of them separated by comma:
      - Primary
      - Alternate X (where x is a number between 1 and 10)
      - Mobility
    The possible values for the \"Calls To Number\" column are the following or a combination of them separated by comma:
      - The value of the phone number for the corresponding Calls To Type, when the number is available. i.e. Alternate 1 may have extension, but no number.
      - When no number is available a blank space is provided instead.
    The possible values for the \"Calls To Extension\" column are the following or a combination of them separated by comma:
      - The value of the extension for the corresponding Calls To Type, when the extension is available. i.e. Primary may have number, but no extension.
      - For Mobility Calls To Type, this is always blank.
      - When no extension is available a blank space is provided instead."""

    criteriaTable: OCITable


@dataclass
class UserSelectiveCallRejectionGetCriteriaResponse21(OCIDataResponse):
    """Response to the UserSelectiveCallRejectionGetCriteriaRequest21.
    Private Phone Numbers are omitted from the fromDnCriteria."""

    fromDnCriteria: SelectiveCallRejectionCriteriaCallType

    blacklisted: bool

    private: bool

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class UserSequentialRingGetCriteriaResponse23(OCIDataResponse):
    """Response to the UserSequentialRingGetCriteriaRequest23."""

    blacklisted: bool

    fromDnCriteria23: CriteriaFromDn23

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None


@dataclass
class UserSequentialRingGetResponse14sp4(OCIDataResponse):
    """Response to the UserSequentialRingGetRequest14sp4. The criteria table's column headings are:
    \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Blacklisted\" and \"Holiday Schedule\"."""

    ringBaseLocationFirst: bool

    baseLocationNumberOfRings: int

    continueIfBaseLocationIsBusy: bool

    callerMayStopSearch: bool

    Location01: SequentialRingLocation14sp4

    Location02: SequentialRingLocation14sp4

    Location03: SequentialRingLocation14sp4

    Location04: SequentialRingLocation14sp4

    Location05: SequentialRingLocation14sp4

    criteriaTable: OCITable


@dataclass
class UserSeriesCompletionGetResponse(OCIDataResponse):
    """Response to the UserSeriesCompletionGetRequest.
    Identifies which Series Completion group the user belongs to and the list of users in the group.
    Contains a table with column headings: \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\",
    \"Hiragana First Name\", \"Department\", \"Phone Number\", \"Extension\", \"Email Address\"."""

    userTable: OCITable

    name: Optional[str] = None


@dataclass
class UserServiceGetAssignmentListResponse(OCIDataResponse):
    """Response to UserServiceGetAssignmentListRequest.
    Contains two tables, one for the service packs, and one for the user services.
    The user table has the column headings: \"Service Name\", \"Assigned\",
    The service pack table's column headings are: \"Service Pack Name\", \"Assigned\", \"Description\".
    The \"Assigned\" column has either a true or false value"""

    servicePacksAssignmentTable: OCITable

    userServicesAssignmentTable: OCITable


@dataclass
class UserServiceIsAssignedResponse(OCIDataResponse):
    """Returns true if the UserService or service pack is assigned, otherwise false."""

    isAssigned: bool


@dataclass
class UserShInterfaceGetPublicIdDataResponse21sp1(OCIDataResponse):
    """Response to the UserShInterfaceGetPublicIdDataRequest21sp1.
    The response contains the Sh non-transparent data for the specified Public User Identity.
    The data also includes a userId, userType, and endpointType.
    The value Mobility in Endpoint Type is only applicable in AS data mode."""

    userId: str

    userType: str

    endpointType: str

    IMSUserState: str

    SCSCFName: Optional[str] = None


@dataclass
class UserShInterfaceGetUserIdDataResponse21sp1(OCIDataResponse):
    """Response to the UserShInterfaceGetUserIdDataRequest21sp1.
    The response contains the Sh non-transparent data for the specified userId.
    The data also includes a userType, publicUserIdentity and endpointType.
    The value Mobility in Endpoint Type is only applicable in AS data mode."""

    entry: List[ShInterfaceUserIdDataEntry21sp1] = field(default_factory=list)


@dataclass
class UserSharedCallAppearanceGetEndpointResponse22(OCIDataResponse):
    """Response to the UserSharedCallAppearanceGetEndpointRequest.

    The following elements are only used in AS data mode and not returned in XS data mode:
      hotlineContact

    The following elements are only used in AS data mode and a value false is returned in the XS mode:
      useHotline"""

    isActive: bool

    allowOrigination: bool

    allowTermination: bool

    useHotline: bool

    hotlineContact: Optional[str] = None


@dataclass
class UserSharedCallAppearanceGetResponse21sp1(OCIDataResponse):
    """Response to the UserSharedCallAppearanceGetRequest21sp1.
    The endpointTable contains columns:
      \"Device Level\", \"Device Name\", \"Device Type\", \"Line/Port\", \"SIP Contact\", \"Port Number\", \"Device Support Visual Device Management\", \"Is Active\", \"Allow Origination\", \"Allow Termination\", \"Mac Address\", \"Path Header\".
    The \"Device Level\" column contains one of the AccessDeviceLevel enumerated constants.
    The \"SIP Contact\" column does not contain \"sip:\" in 21sp1.
    Port numbers are only used by devices with static line ordering."""

    alertAllAppearancesForClickToDialCalls: bool

    alertAllAppearancesForGroupPagingCalls: bool

    maxAppearances: int

    allowSCACallRetrieve: bool

    enableMultipleCallArrangement: bool

    multipleCallArrangementIsActive: bool

    endpointTable: OCITable

    allowBridgingBetweenLocations: bool

    bridgeWarningTone: str

    enableCallParkNotification: bool


@dataclass
class UserSilentAlertingGetResponse(OCIDataResponse):
    """Response to UserSilentAlertingGetRequest."""

    isActive: bool


@dataclass
class UserSimultaneousRingFamilyGetCriteriaResponse(OCIDataResponse):
    """Response to the UserSimultaneousRingFamilyGetCriteriaRequest."""

    blacklisted: bool

    fromDnCriteria: CriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None


@dataclass
class UserSimultaneousRingFamilyGetResponse17(OCIDataResponse):
    """Response to the UserSimultaneousRingFamilyGetRequest17.
    Contains a criteria table wich column heading: \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Holiday Schedule\", \"Calls From\" and \"Blacklisted\"."""

    isActive: bool

    doNotRingIfOnCall: bool

    criteriaTable: OCITable

    simultaneousRingNumber: List[SimultaneousRingNumber] = field(default_factory=list)


@dataclass
class UserSimultaneousRingPersonalGetCriteriaResponse(OCIDataResponse):
    """Response to the UserSimultaneousRingPersonalGetCriteriaRequest."""

    blacklisted: bool

    fromDnCriteria: CriteriaFromDn

    timeSchedule: Optional[TimeSchedule] = None

    holidaySchedule: Optional[HolidaySchedule] = None


@dataclass
class UserSimultaneousRingPersonalGetResponse17(OCIDataResponse):
    """Response to the UserSimultaneousRingPersonalGetRequest17.
    Contains a criteria table with column heading: \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Holiday Schedule\", \"Calls From\" and \"Blacklisted\"."""

    isActive: bool

    doNotRingIfOnCall: bool

    criteriaTable: OCITable

    simultaneousRingNumber: List[SimultaneousRingNumber] = field(default_factory=list)


@dataclass
class UserSingleSignOnCreateDeviceTokenResponse(OCIDataResponse):
    """Response to UserSingleSignOnCreateDeviceTokenRequest."""

    deviceToken: str


@dataclass
class UserSpeedDial100GetListResponse17sp1(OCIDataResponse):
    """Response to the UserSpeedDial100GetListRequest17sp1."""

    prefix: Optional[str] = None

    speedDialEntry: List[SpeedDial100Entry] = field(default_factory=list)


@dataclass
class UserSpeedDial100GetResponse(OCIDataResponse):
    """Response to the UserSpeedDial100GetRequest."""

    phoneNumber: str

    description: Optional[str] = None


@dataclass
class UserSpeedDial8GetListResponse(OCIDataResponse):
    """Response to the UserSpeedDial8GetListRequest."""

    speedDialEntry: List[SpeedDial8Entry] = field(default_factory=list)


@dataclass
class UserTerminatingAlternateTrunkIdentityGetResponse(OCIDataResponse):
    """Response to UserTerminatingAlternateTrunkIdentityGetRequest."""

    terminatingTrunkIdentity: Optional[str] = None


@dataclass
class UserTerminatingClosedUserGroupGetResponse(OCIDataResponse):
    """Response to the UserTerminatingClosedUserGroupGetRequest.
    Returns user Terminating CUG service settings."""

    userInterlockCode: Optional[str] = None


@dataclass
class UserThirdPartyVoiceMailSupportGetResponse17(OCIDataResponse):
    """Response to UserThirdPartyVoiceMailSupportGetRequest17."""

    isActive: bool

    busyRedirectToVoiceMail: bool

    noAnswerRedirectToVoiceMail: bool

    serverSelection: str

    mailboxIdType: str

    noAnswerNumberOfRings: int

    alwaysRedirectToVoiceMail: bool

    outOfPrimaryZoneRedirectToVoiceMail: bool

    userServer: Optional[str] = None

    mailboxURL: Optional[str] = None


@dataclass
class UserTwoStageDialingGetResponse13Mp20(OCIDataResponse):
    """Response to UserTwoStageDialingGetRequest13Mp20."""

    isActive: bool

    allowActivationWithUserAddresses: bool


@dataclass
class UserVideoAddOnGetResponse22(OCIDataResponse):
    """Response to the UserVideoAddOnGetRequest22."""

    isActive: bool

    maxOriginatingCallDelaySeconds: int

    accessDeviceEndpoint: Optional[AccessDeviceEndpointWithPortNumberRead22] = None


@dataclass
class UserVoiceMessagingUserGetAdvancedVoiceManagementResponse14sp3(OCIDataResponse):
    """Response to the UserVoiceMessagingUserGetAdvancedVoiceManagementRequest14sp3."""

    mailServerSelection: str

    useGroupDefaultMailServerFullMailboxLimit: bool

    groupMailServerFullMailboxLimit: int

    personalMailServerProtocol: str

    personalMailServerRealDeleteForImap: bool

    groupMailServerEmailAddress: Optional[str] = None

    groupMailServerUserId: Optional[str] = None

    personalMailServerNetAddress: Optional[str] = None

    personalMailServerEmailAddress: Optional[str] = None

    personalMailServerUserId: Optional[str] = None


@dataclass
class UserVoiceMessagingUserGetAliasListResponse(OCIDataResponse):
    """Response to UserVoiceMessagingUserGetAliasListRequest."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class UserVoiceMessagingUserGetDistributionListResponse(OCIDataResponse):
    """Response to UserVoiceMessagingUserGetDistributionListRequest."""

    description: Optional[str] = None

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class UserVoiceMessagingUserGetGreetingResponse20(OCIDataResponse):
    """Response to UserVoiceMessagingUserGetGreetingRequest20.
    Contains the greeting configuration for a user's voice messaging.
    The following elements are only used in AS data mode:
      disableMessageDeposit
      disableMessageDepositAction
      greetingOnlyForwardDestination
      extendedAwayEnabled
      extendedAwayDisableMessageDeposit
      extendedAwayAudioFile
      extendedAwayAudioMediaType
      extendedAwayVideoFile
      extendedAwayVideoMediaTyp"""

    busyAnnouncementSelection: str

    noAnswerAnnouncementSelection: str

    extendedAwayEnabled: bool

    extendedAwayDisableMessageDeposit: bool

    noAnswerNumberOfRings: int

    disableMessageDeposit: bool

    disableMessageDepositAction: str

    busyPersonalAudioFile: Optional[AnnouncementFileLevelKey] = None

    busyPersonalVideoFile: Optional[AnnouncementFileLevelKey] = None

    noAnswerPersonalAudioFile: Optional[AnnouncementFileLevelKey] = None

    noAnswerPersonalVideoFile: Optional[AnnouncementFileLevelKey] = None

    noAnswerAlternateGreeting01: Optional[
        VoiceMessagingAlternateNoAnswerGreetingRead20
    ] = None

    noAnswerAlternateGreeting02: Optional[
        VoiceMessagingAlternateNoAnswerGreetingRead20
    ] = None

    noAnswerAlternateGreeting03: Optional[
        VoiceMessagingAlternateNoAnswerGreetingRead20
    ] = None

    extendedAwayAudioFile: Optional[AnnouncementFileLevelKey] = None

    extendedAwayVideoFile: Optional[AnnouncementFileLevelKey] = None

    greetingOnlyForwardDestination: Optional[str] = None


@dataclass
class UserVoiceMessagingUserGetOutgoingSMDIMWIResponse(OCIDataResponse):
    """Response to the UserVoiceMessagingUserGetOutgoingSMDIMWIRequest."""

    isActive: bool

    outgoingSMDIMWIPhoneNumber: List[str] = field(default_factory=list)


@dataclass
class UserVoiceMessagingUserGetVoiceManagementResponse23(OCIDataResponse):
    """Response to the UserVoiceMessagingUserGetVoiceManagementRequest23."""

    isActive: bool

    processing: str

    usePhoneMessageWaitingIndicator: bool

    sendVoiceMessageNotifyEmail: bool

    sendCarbonCopyVoiceMessage: bool

    transferOnZeroToPhoneNumber: bool

    alwaysRedirectToVoiceMail: bool

    busyRedirectToVoiceMail: bool

    noAnswerRedirectToVoiceMail: bool

    outOfPrimaryZoneRedirectToVoiceMail: bool

    voiceMessageDeliveryEmailAddress: Optional[EmailAddressList] = None

    voiceMessageNotifyEmailAddress: Optional[str] = None

    voiceMessageCarbonCopyEmailAddress: Optional[str] = None

    transferPhoneNumber: Optional[str] = None


@dataclass
class UserVoiceMessagingUserGetVoicePortalResponse20(OCIDataResponse):
    """Response to UserVoiceMessagingUserGetVoicePortalRequest20."""

    usePersonalizedName: bool

    voicePortalAutoLogin: bool

    personalizedNameAudioFile: Optional[AnnouncementFileLevelKey] = None


@dataclass
class UserVoicePortalCallingGetResponse(OCIDataResponse):
    """Response to UserVoicePortalCallingGetRequest."""

    isActive: bool


@dataclass
class UserXsiPolicyProfileGetResponse(OCIDataResponse):
    """Response to UserXsiPolicyProfileGetRequest."""

    xsiPolicyProfile: str


@dataclass
class UserZoneCallingRestrictionsGetResponse(OCIDataResponse):
    """Gets the home zone for a user
    Response to a UserZoneCallingRestrictionsGetRequest"""

    homeZoneName: Optional[str] = None
