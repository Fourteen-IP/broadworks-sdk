# Auto-generated file
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List

from broadworks_sdk.commands.base_command import OCIType, OCICommand


@dataclass
class PasswordForAccessDevice(OCIType):
    """Passwords to be generated for an access device.
    The combination of serviceProviderId, groupId, and deviceName will be used
    to find the device if it exists. If the device doesn't exist yet, then
    the serviceProviderId and groupId will be used to choose the password
    rules with which to generate the device password."""

    generateDeviceAuthenticationPassword: bool

    serviceProviderId: Optional[str] = None

    groupId: Optional[str] = None

    deviceName: Optional[str] = None


@dataclass
class PasswordForGroupAdministrator(OCIType):
    """Password to be generated for a group administrator. If the administratorId is not included, or included but
    is not an exiting administrator for the group, a password will be generated based on only the rules applicable
    for a new user."""

    serviceProviderId: str

    groupId: str

    generatePassword: bool

    administratorId: Optional[str] = None


@dataclass
class PasswordForServiceProviderAdministrator(OCIType):
    """Password to be generated for a service provider administrator. If the administratorId is not included,
    or included but is not an exiting administrator for the service provider, a password will be generated
    based on only the rules applicable for a new user."""

    serviceProviderId: str

    generatePassword: bool

    administratorId: Optional[str] = None


@dataclass
class PasswordForSystemAdministrator(OCIType):
    """Password to be generated for a System or Provisioning administrator. If the administratorId is
    not included, or included but is not an exiting administrator for the
    service provider, a password will be generated
    based on only the rules applicable for a new user."""

    generatePassword: bool

    administratorId: Optional[str] = None


@dataclass
class PasswordForTrunkGroup(OCIType):
    """Passwords to be generated for a trunk group.
    The combination of serviceProviderId, groupId, and name will be used to
    find the trunk group if it exists. If the trunk group doesn't exist yet,
    then the serviceProviderId and groupId will be used to choose the password
    rules with which to generate the trunk group password."""

    serviceProviderId: str

    groupId: str

    generateTrunkGroupAuthenticationPassword: bool

    name: Optional[str] = None


@dataclass
class PasswordForUser(OCIType):
    """Passwords, passcode and SIP authentication passwords to be generated for a user. If the userId is not
    included or included but is not an existing user in the group, a password will be generated based on only
    the rules applicable for a new user."""

    serviceProviderId: str

    groupId: str

    userId: Optional[str] = None

    generatePassword: Optional[bool] = None

    generatePasscode: Optional[bool] = None

    generateSipPassword: Optional[bool] = None


@dataclass
class AccessDevice(OCIType):
    """Uniquely identifies an Identity/device profile created anywhere in the system."""

    deviceLevel: str

    deviceName: str


@dataclass
class AccessDeviceKey(OCIType):
    """Key to uniquely identify a system, service provider, or group device."""

    deviceName: str

    serviceProviderId: Optional[str] = None

    groupId: Optional[str] = None


@dataclass
class AccessDeviceReorderEndpointIdentity(OCIType):
    """Access device end point identity in the context of a reorder command.
    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity"""

    linePort: str

    privateIdentity: Optional[str] = None


@dataclass
class AccessDeviceTypeRename(OCIType):
    """Pair of DeviceManagementTagSetName"""

    originalDeviceTypeName: str

    newDeviceTypeName: str


@dataclass
class ActivatableDN(OCIType):
    """Activatable directory Number in E164 Format."""

    DN: str

    activate: Optional[bool] = None


@dataclass
class ActivatableDNRange(OCIType):
    """Activatable directory number range. The minimum and maximum values are inclusive."""

    minPhoneNumber: str

    maxPhoneNumber: str

    activate: Optional[bool] = None


@dataclass
class AlternateNumberEntry21(OCIType):
    """Alternate Number Entry."""

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    ringPattern: Optional[str] = None

    description: Optional[str] = None


@dataclass
class AlternateUserIdEntry(OCIType):
    """Alternate user id."""

    alternateUserId: str

    description: Optional[str] = None


@dataclass
class AnnouncementFileKey(OCIType):
    """Uniquely identifies a file within a group or user repository."""

    name: str

    mediaFileType: str


@dataclass
class AnnouncementFileLevelKey(OCIType):
    """Uniquely identifies a file within a group or user repository.
    Includes level to distinguish between group and user announcements
    in scenarios where both are listed."""

    name: str

    mediaFileType: str

    level: str


@dataclass
class AssignedGroupServicesEntry(OCIType):
    """Assigned Group Services List Entry.
    The isActive element is true, false, or could be missing completely."""

    serviceName: str

    isActive: Optional[bool] = None


@dataclass
class AssignedUserServicesEntry(OCIType):
    """Assigned User Services List Entry.
    The isActive element is true, false, or could be missing completely."""

    serviceName: str

    isActive: Optional[bool] = None


@dataclass
class AutoAttendantKeyConfigurationReadEntry19(OCIType):
    """The read configuration entry of a key for Auto
    Attendant.
    The following
    data elements are only valid for Standard Auto
    Attendants:
    submenuId"""

    action: str

    description: Optional[str] = None

    phoneNumber: Optional[str] = None

    audioFileDescription: Optional[str] = None

    audioMediaType: Optional[str] = None

    videoFileDescription: Optional[str] = None

    videoMediaType: Optional[str] = None

    submenuId: Optional[str] = None


@dataclass
class BCCTMaxConnections(OCIType):
    """Maximum number of BCCT Server Connections.
    Can either be unlimited or a bounded int quantity."""

    unlimited: bool

    quantity: int


@dataclass
class BroadWorksMobilityAlertingMobileNumberReplacementList(OCIType):
    """A list of Mobile Numbers to be alerted.
    By convention, an element of this type may be set nil to clear the list."""

    mobileNumber: List[str] = field(default_factory=list)


@dataclass
class CallCenterAnnouncementDescriptionList(OCIType):
    """Contains list of file descriptions for audio or video files"""

    fileDescription1: Optional[str] = None

    fileDescription2: Optional[str] = None

    fileDescription3: Optional[str] = None

    fileDescription4: Optional[str] = None


@dataclass
class CallCenterAnnouncementMediaFileTypeList(OCIType):
    """Contains list of file media types for audio or video files"""

    mediaType1: Optional[str] = None

    mediaType2: Optional[str] = None

    mediaType3: Optional[str] = None

    mediaType4: Optional[str] = None


@dataclass
class CallCenterAnnouncementURLList(OCIType):
    """Contains list of urls"""

    url1: Optional[str] = None

    url2: Optional[str] = None

    url3: Optional[str] = None

    url4: Optional[str] = None


@dataclass
class CallCenterAnnouncementURLListModify(OCIType):
    """Contains a list of URLs for modify."""

    url1: Optional[str] = None

    url2: Optional[str] = None

    url3: Optional[str] = None

    url4: Optional[str] = None


@dataclass
class CallCenterReportTemplateKey(OCIType):
    """Uniquely identifies a call center report template created in the system."""

    templateLevel: str

    templateName: str


@dataclass
class CallingNameRetrievalWhiteListReplacementList(OCIType):
    """A list of DNs to add to the CNAM call filtering DN white list.
    By convention, an element of this type may be set nil to clear the list."""

    number: List[str] = field(default_factory=list)


@dataclass
class CallLogsEntry(OCIType):
    """Call Log entry describing a placed, received, or missed call."""

    callLogId: str

    phoneNumber: str

    name: str

    time: str

    countryCode: Optional[str] = None


@dataclass
class CallLogsEntry22(OCIType):
    """Call Log entry describing a placed, received, or missed call."""

    callLogId: str

    phoneNumber: str

    name: str

    time: str

    countryCode: Optional[str] = None

    callFilteringDisposition: Optional[str] = None


@dataclass
class CallToNumber(OCIType):
    """Call to Number."""

    type: str

    number: Optional[str] = None

    extension: Optional[str] = None


@dataclass
class CollaborateBridgeMaximumParticipants(OCIType):
    """Maximum number of Collaborate bridge participants. Can either be unlimited or limited to a value between 3 and 999999."""

    unlimited: bool

    quantity: int


@dataclass
class CollaborateGracePeriodDuration(OCIType):
    """Collaborate grace period duration."""

    hours: int

    minutes: int


@dataclass
class CollaborateRoomSchedule(OCIType):
    """Collaborate room schedule."""

    scheduleReservationless: object

    scheduleOneTime: object

    scheduleRecurring: object


@dataclass
class CollaborateRoomScheduleDuration(OCIType):
    """Collaborate room schedule duration."""

    hours: int

    minutes: int


@dataclass
class CommunicationBarringAuthorizationCodeConfiguration(OCIType):
    """Communication Barring Authorization Code add entry."""

    code: str

    description: Optional[str] = None

    networkClassOfService: Optional[str] = None


@dataclass
class CommunicationBarringAuthorizationCodeEntry(OCIType):
    """Communication Barring Authorization Code entry."""

    code: str

    description: Optional[str] = None


@dataclass
class CommunicationBarringCallMeNowRule(OCIType):
    """Communication Barring Call Me Now Rule"""

    criteria: str

    action: str

    callTimeoutSeconds: Optional[int] = None


@dataclass
class CommunicationBarringIncomingRule(OCIType):
    """Communication Barring Incoming Rule"""

    digitPatternCriteria: str

    action: str

    priority: float

    callTimeoutSeconds: Optional[int] = None

    timeSchedule: Optional[str] = None

    holidaySchedule: Optional[str] = None


@dataclass
class CommunicationBarringIncomingRule19sp1(OCIType):
    """Communication Barring Incoming Rule"""

    digitPatternCriteria: str

    incomingCriteria: str

    action: str

    priority: float

    callTimeoutSeconds: Optional[int] = None

    timeSchedule: Optional[str] = None

    holidaySchedule: Optional[str] = None


@dataclass
class CommunicationBarringOriginatingRule(OCIType):
    """Communication Barring Originating Rule"""

    criteria: str

    action: str

    treatmentId: Optional[str] = None

    transferNumber: Optional[str] = None

    callTimeoutSeconds: Optional[int] = None


@dataclass
class CommunicationBarringProfileReplacementList(OCIType):
    """A list of communication barring profiles that replaces a previously configured list.
    By convention, an element of this type may be set nil to clear the list."""

    profileName: List[str] = field(default_factory=list)


@dataclass
class CommunicationBarringRedirectingRule(OCIType):
    """Communication Barring Redirecting Rule"""

    criteria: str

    action: str

    callTimeoutSeconds: Optional[int] = None


@dataclass
class Contact(OCIType):
    """Contact information."""

    contactName: Optional[str] = None

    contactNumber: Optional[str] = None

    contactEmail: Optional[str] = None


@dataclass
class CriteriaActivation(OCIType):
    """Criteria active status indicator"""

    criteriaName: str

    isActive: bool


@dataclass
class CriteriaFromDn(OCIType):
    """The from dn criteria used within an add/get request."""

    fromDnCriteriaSelection: str

    includeAnonymousCallers: bool

    includeUnavailableCallers: bool

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class CriteriaFromDn23(OCIType):
    """The from dn criteria added with the option for selecting internal and external callers, used within an add/get request."""

    fromDnCriteriaSelection: str

    includeAnonymousCallers: bool

    includeUnavailableCallers: bool

    includeInternalCallers: bool

    includeExternalCallers: bool

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class CriteriaReplacementDNList(OCIType):
    """A list of criteria DNs that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class DefaultNetworkClassOfService(OCIType):
    """The default Network Class of Service to set during assignation/unassignation."""

    useExisting: bool

    networkClassOfServiceName: str


@dataclass
class DepartmentKey(OCIType):
    """Uniquely identifies a department system-wide.
    Departments are contained in either an enterprise or a group. Enterprise departments can be
    used by any or all groups within the enterprise. Department names are unique within a group and
    within an enterprise, but the same department name can exist in 2 different groups or in both
    a group and its parent enterprise. Therefore, to uniquely identify a department, we must know
    the department name and which enterprise or group contains the department.
    This type is extended by group and enterprise department keys."""


@dataclass
class DeviceManagementDeviceTypeOptionsRead22V2(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[str] = None

    macFormatInNonRequestURI: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeOptionsRead22V3(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          bearerFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI

    The following data elements are only used in AS data mode:
          enableDeviceActivation, value ‘false’ is returned

    The following elements are only used in AS data mode and not returned in XS data mode
          deviceModel"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    enableDeviceActivation: bool

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[str] = None

    macFormatInNonRequestURI: Optional[str] = None

    deviceModel: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeOptionsRead22V4(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI

    The following data elements are only used in AS data mode:
          enableDeviceActivation, value ‘false’ is returned
          supportLinks, value ‘Not Supported’ is returned

    The following elements are only used in AS data mode and not returned in XS data mode
          deviceModel"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    enableDeviceActivation: bool

    supportLinks: str

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[str] = None

    macFormatInNonRequestURI: Optional[str] = None

    deviceModel: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeOptionsRead22V5(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI

    The following data elements are only used in AS data mode:
          enableDeviceActivation, value \"false\" is returned
          supportLinks, value \"Not Supported\" is returned

    The following elements are only used in AS data mode and not returned in XS data mode
          deviceModel
          autoLinkingDeviceType
          autoCreateDevicesLevel"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    enableDeviceActivation: bool

    supportLinks: str

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[str] = None

    macFormatInNonRequestURI: Optional[str] = None

    deviceModel: Optional[str] = None

    autoLinkingDeviceType: Optional[str] = None

    autoCreateDevicesLevel: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeOptionsRead22V6(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files except bearerFileAuthentication which is not supported.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI

    The following data elements are only used in AS data mode:
          enableDeviceActivation, value ‘false’ is returned
          supportLinks, value ‘Not Supported’ is returned

    The following elements are only used in AS data mode and not returned in XS data mode
          deviceModel
          autoLinkingDeviceType
          autoCreateDevicesLevel
          isActivationCodeThroughMessagingServer
          bearerFileAuthentication"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    enableDeviceActivation: bool

    supportLinks: str

    bearerFileAuthentication: bool

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[str] = None

    macFormatInNonRequestURI: Optional[str] = None

    deviceModel: Optional[str] = None

    autoLinkingDeviceType: Optional[str] = None

    autoCreateDevicesLevel: Optional[str] = None

    isActivationCodeThroughMessagingServer: Optional[bool] = None


@dataclass
class DeviceManagementLanguageMapping(OCIType):
    """Maps a BroadWorks language to a device-equivalent language."""

    broadWorksLanguage: str

    deviceLanguage: str


@dataclass
class DeviceManagementTag(OCIType):
    """Represents a tag name with its associated value."""

    tagName: str

    tagValue: Optional[str] = None


@dataclass
class DeviceManagementTagSetRename(OCIType):
    """Pair of DeviceManagementTagSetName"""

    originalTagSetName: str

    newTagSetName: str


@dataclass
class DeviceManagementUserNamePassword16(OCIType):
    """Access device credentials."""

    userName: str

    password: str


@dataclass
class DialableCallerIDCriteriaPriorityOrder(OCIType):
    """Dialable Caller ID routing order"""

    criteriaName: str

    priority: float


@dataclass
class DialPlanPolicy(OCIType):
    """Dial Plan Access Code attributes."""

    useSetting: Optional[str] = None

    requiresAccessCodeForPublicCalls: Optional[bool] = None

    allowE164PublicCalls: Optional[bool] = None

    preferE164NumberFormatForCallbackServices: Optional[bool] = None

    publicDigitMap: Optional[str] = None

    privateDigitMap: Optional[str] = None


@dataclass
class DialPlanPolicyAccessCode(OCIType):
    """Dial Plan Access Code attributes."""

    accessCode: str

    description: Optional[str] = None

    includeCodeForNetworkTranslationsAndRouting: Optional[bool] = None

    includeCodeForScreeningServices: Optional[bool] = None

    enableSecondaryDialTone: Optional[bool] = None


@dataclass
class DNISKey(OCIType):
    """Uniquely identifies a Call Center DNIS."""

    serviceUserId: str

    name: str


@dataclass
class DNRange(OCIType):
    """Directory number range. The minimum and maximum values are inclusive."""

    minPhoneNumber: str

    maxPhoneNumber: str


@dataclass
class DNValidationStatusMessage(OCIType):
    """The message contains the status and error reason that prevents DN to be assigned/validated"""

    dn: str

    status: str

    messageCode: Optional[int] = None

    summary: Optional[str] = None

    summaryEnglish: Optional[str] = None


@dataclass
class EmailAddressList(OCIType):
    """A list of 50 email addresses is configured in the \"Forward it to these e-mail addresses\" section
     on the Voice Management configuration page

    Change History:
    R25.0 - Added"""

    emailAddress: List[str] = field(default_factory=list)


@dataclass
class EnhancedCallLogsAccountAuthorizationCodeFilter(OCIType):
    """Filter criteria based on the account code.
    When \"callsWithCodes\" is set to true, all call logs with account/authorization codes are returned.
    When it set to false, all call logs without account/authorization codes are returned."""

    callsWithCodes: bool

    accountAuthorizationCode: str


@dataclass
class EnhancedCallLogsCallAuthorizationCodeFilter(OCIType):
    """Filter criteria based on call authorization code. Note that this code
    filter is different than EnhancedCallLogsAccountAuthorizationCodeFilter,
    which applies strictly to codes entered using the account/authorization
    code service.
    When \"callsWithCodes\" is set to true, all call logs with authorization
    codes are returned.
    When it set to false, all call logs without authorization codes are
    returned.
    If \"authorizationCode\" is set, all call logs matching that specific
    authorization code are returned."""

    callsWithCodes: bool

    authorizationCode: str


@dataclass
class EnhancedCallLogsResponsePagingControl(OCIType):
    """Used in enhanced call logs group and enterprise queries to restrict the set of result
    rows when making a request that can result in a large dataset. The client specifies the
    starting row and the number of rows requested.
    The server only provides those rows in results, if available."""

    responseStartIndex: int

    responsePageSize: int


@dataclass
class EnhancedCallLogsTimeRange(OCIType):
    """Time range used to filter call logs."""

    startDateTime: str

    endDateTime: str


@dataclass
class EnterpriseTrunkNumberRangeModify(OCIType):
    """Directory number range for modification."""

    dnRangeStart: str

    extensionLength: Optional[int] = None


@dataclass
class EstimatedWaitMessageOptionsModify(OCIType):
    """Estimated Wait Message Options"""

    enabled: Optional[bool] = None

    operatingMode: Optional[str] = None

    playPositionHighVolume: Optional[bool] = None

    playTimeHighVolume: Optional[bool] = None

    maximumPositions: Optional[int] = None

    maximumWaitingMinutes: Optional[int] = None

    defaultCallHandlingMinutes: Optional[int] = None

    playUpdatedEWM: Optional[bool] = None

    timeBetweenEWMUpdatesSeconds: Optional[int] = None


@dataclass
class EstimatedWaitMessageOptionsRead17sp4(OCIType):
    """Estimated Wait Message Options"""

    enabled: bool

    operatingMode: str

    playPositionHighVolume: bool

    playTimeHighVolume: bool

    maximumPositions: int

    maximumWaitingMinutes: int

    defaultCallHandlingMinutes: int

    playUpdatedEWM: bool

    timeBetweenEWMUpdatesSeconds: Optional[int] = None


@dataclass
class ExchangeUserNamePassword(OCIType):
    """Exchange server user name and password."""

    userName: str

    password: str


@dataclass
class ExecutiveCallFilteringCriteriaFromDn(OCIType):
    """The from dn criteria used within an executive call filtering criteria add/get request."""

    fromDnCriteriaSelection: str

    includeAnonymousCallers: bool

    includeUnavailableCallers: bool

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class ExtensionRange17(OCIType):
    """Extension range. The minimum and maximum values are inclusive."""

    minExtension: str

    maxExtension: str


@dataclass
class FeatureAccessCodeEntry(OCIType):
    """Feature Access Code Entry"""

    featureAccessCodeName: str

    mainCode: Optional[str] = None

    alternateCode: Optional[str] = None


@dataclass
class FeatureAccessCodeModifyEntry(OCIType):
    """Feature Access Code Entry to be used in all the system, service provider and
    group modify commands."""

    featureAccessCodeName: str

    mainCode: Optional[str] = None

    alternateCode: Optional[str] = None

    enableFAC: Optional[bool] = None


@dataclass
class FeatureAccessCodeReadEntry(OCIType):
    """Feature Access Code Entry to be used in all GET commands."""

    featureAccessCodeName: str

    mainCode: Optional[str] = None

    alternateCode: Optional[str] = None

    enableFAC: Optional[bool] = None


@dataclass
class FileRepositoryProtocolFTP16(OCIType):
    """Attributes of the FTP protocol when the file repository interface is using FTP."""

    ftpPassive: bool

    netAddress: str

    ftpRemoteVerification: bool


@dataclass
class FileRepositoryProtocolWebDAV(OCIType):
    """Attributes of the WebDav protocol when the file repository interface is using WebDav."""

    secure: bool

    netAddress: str


@dataclass
class FileResource(OCIType):
    """Represents either an existing file for the application server to use, or
    the contents of a file to transfer."""

    sourceFileName: str

    fileContent: int


@dataclass
class GroupAdmin(OCIType):
    """The common Group Admin elements."""

    userId: str

    firstName: Optional[str] = None

    lastName: Optional[str] = None

    password: Optional[str] = None

    language: Optional[str] = None


@dataclass
class GroupExtensionLengthSettings(OCIType):
    """Group extension length settings"""

    minExtensionLength: Optional[int] = None

    maxExtensionLength: Optional[int] = None

    defaultExtensionLength: Optional[int] = None

    useEnterpriseExtensionLengthSetting: Optional[bool] = None


@dataclass
class HolidaySchedule(OCIType):
    """Holiday Schedule."""

    type: str

    name: str


@dataclass
class HourMinute(OCIType):
    """Represents a specific time with hour and minute granularity"""

    hour: int

    minute: int


@dataclass
class HuntAgentWeight(OCIType):
    """The weighted call distribution weight for an agent."""

    agentUserId: str

    weight: int


@dataclass
class IPAddressRange(OCIType):
    """IP Address Range."""

    minIpAddress: str

    maxIpAddress: str


@dataclass
class LabeledFileNameResource(OCIType):
    """Represents an existing file for the application server to use, along with
    a description and mediaType."""

    description: str

    mediaType: str

    sourceFileName: str


@dataclass
class LabeledFileResource(OCIType):
    """Represents either an existing file for the application server to use, or
    the contents of a file to transfer with a description."""

    description: str

    sourceFileName: str

    content: int


@dataclass
class LabeledMediaFileResource(OCIType):
    """Represents either an existing file for the application server to use, or
    the contents of a file to transfer with a description."""

    description: str

    mediaType: str

    sourceFileName: str

    content: int


@dataclass
class MeetMeConferencingConferenceKey(OCIType):
    """Identifier for conference."""

    bridgeId: str

    conferenceId: str


@dataclass
class MeetMeConferencingConferencePorts(OCIType):
    """Number of conference ports. Can either be unlimited or limited to a value between 0 and 999999."""

    unlimited: bool

    quantity: int


@dataclass
class MixedCallLogsEntry(OCIType):
    """Call Log entry describing a placed, received, or missed call."""

    callLogType: str

    callLogId: str

    phoneNumber: str

    name: str

    time: str

    countryCode: Optional[str] = None


@dataclass
class MusicOnHoldSourceAdd21(OCIType):
    """Contains the music on hold source configuration.
    The following elements are only used in HSS data mode and ignored in AS data mode:
      labeledMediaFiles
    The following elements are only used in AS data mode and ignored in HSS data mode:
      announcementMediaFiles"""

    audioFilePreferredCodec: str

    messageSourceSelection: str

    labeledCustomSourceMediaFiles: object

    announcementCustomSourceMediaFiles: object

    externalSource: Optional[object] = None


@dataclass
class MusicOnHoldSourceAdd22(OCIType):
    """Contains the music on hold source configuration.
    The following elements are only used in HSS data mode and ignored in AS data mode:
      labeledMediaFiles
    The following elements are only used in AS data mode and ignored in HSS data mode:
      announcementMediaFiles
      authenticationRequired
      authenticationUserName
      authenticationPassword"""

    audioFilePreferredCodec: str

    messageSourceSelection: str

    labeledCustomSourceMediaFiles: object

    announcementCustomSourceMediaFiles: object

    externalSource: Optional[object] = None


@dataclass
class MusicOnHoldSourceModify21(OCIType):
    """Contains the music on hold source configuration.
    The following elements are only used in HSS data mode and ignored in AS data mode:
      labeledMediaFiles
    The following elements are only used in AS data mode and ignored in HSS data mode:
      announcementMediaFiles"""

    labeledCustomSourceMediaFiles: object

    announcementCustomSourceMediaFiles: object

    audioFilePreferredCodec: Optional[str] = None

    messageSourceSelection: Optional[str] = None

    externalSource: Optional[object] = None


@dataclass
class MusicOnHoldSourceModify22(OCIType):
    """Contains the music on hold source configuration.
    The following elements are only used in HSS data mode and ignored in AS data mode:
      labeledMediaFiles
    The following elements are only used in AS data mode and ignored in HSS data mode:
      announcementMediaFiles
      authenticationRequired
      authenticationUserName
      authenticationPassword"""

    labeledCustomSourceMediaFiles: object

    announcementCustomSourceMediaFiles: object

    audioFilePreferredCodec: Optional[str] = None

    messageSourceSelection: Optional[str] = None

    externalSource: Optional[object] = None


@dataclass
class MusicOnHoldSourceRead21(OCIType):
    """Contains the music on hold source configuration.
    The following elements are only used in XS data mode and not returned in AS data mode:
      labeledCustomSourceMediaFiles
    The following elements are only used in AS data mode and not returned in XS data mode:
      announcementMediaFiles"""

    audioFilePreferredCodec: str

    messageSourceSelection: str

    labeledCustomSourceMediaFiles: object

    announcementCustomSourceMediaFiles: object

    externalSource: Optional[object] = None


@dataclass
class MusicOnHoldSourceRead22(OCIType):
    """Contains the music on hold source configuration.
    The following elements are only used in XS data mode and not returned in AS data mode:
      labeledCustomSourceMediaFiles
    The following elements are only used in AS data mode and not returned in XS data mode:
      announcementMediaFiles"""

    audioFilePreferredCodec: str

    messageSourceSelection: str

    labeledCustomSourceMediaFiles: object

    announcementCustomSourceMediaFiles: object

    externalSource: Optional[object] = None


@dataclass
class MusicOnHoldSourceRead22V2(OCIType):
    """Contains the music on hold source configuration.
    The following elements are only used in XS data mode and not returned in AS data mode:
      labeledCustomSourceMediaFiles
    The following elements are only used in AS data mode and not returned in XS data mode:
      announcementMediaFiles"""

    audioFilePreferredCodec: str

    messageSourceSelection: str

    labeledCustomSourceMediaFiles: object

    announcementCustomSourceMediaFiles: object

    externalSource: Optional[object] = None


@dataclass
class MusicOnHoldSourceRead22V3(OCIType):
    """Contains the music on hold source configuration.
    The following elements are only used in XS data mode and not returned in AS data mode:
      labeledCustomSourceMediaFiles
    The following elements are only used in AS data mode and not returned in XS data mode:
      announcementMediaFiles
      authenticationUserName
    The following element is only used in AS data mode:
      authenticationRequired, value \"false\" is returned in XS data mode"""

    audioFilePreferredCodec: str

    messageSourceSelection: str

    labeledCustomSourceMediaFiles: object

    announcementCustomSourceMediaFiles: object

    externalSource: Optional[object] = None


@dataclass
class MusicOnHoldUserSourceRead16(OCIType):
    """Contains the music on hold user source configuration."""

    messageSourceSelection: str

    customSource: Optional[object] = None


@dataclass
class MWIDeliveryToMobileEndpointTemplateActivation(OCIType):
    """MWI Delivery To Mobile Endpoint enabled status indicator"""

    language: str

    type: str

    isEnabled: bool


@dataclass
class MWIDeliveryToMobileEndpointTemplateLine(OCIType):
    """MWI Delivery To Mobile Endpoint template section associated with a specific tag."""

    prefix: Optional[str] = None

    tag: Optional[str] = None

    postfix: Optional[str] = None


@dataclass
class NameDialingName(OCIType):
    """Name dialing last and first names."""

    nameDialingLastName: str

    nameDialingFirstName: str


@dataclass
class NetworkClassOfServiceCommunicationBarringProfile(OCIType):
    """Communication Barring Profile defined as part of the Network Class
    Of Service. There can be only one primary profile within a Network
    Class Of Service."""

    name: str

    isPrimary: bool


@dataclass
class PhoneListEntry(OCIType):
    """Phone list entry."""

    entryName: str

    phoneNumber: str


@dataclass
class PrimaryUserInfo(OCIType):
    """Primary user information."""

    userId: Optional[str] = None

    serviceProviderId: Optional[str] = None

    groupId: Optional[str] = None

    userFirstName: Optional[str] = None

    userLastName: Optional[str] = None

    userPhoneNumber: Optional[str] = None

    userExtension: Optional[str] = None

    endPointType: Optional[str] = None


@dataclass
class PriorityAlertCriteriaFromDn(OCIType):
    """The from dn criteria used within an add/get request."""

    fromDnCriteriaSelection: str

    includeAnonymousCallers: bool

    includeUnavailableCallers: bool

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class PublicUserIdentity(OCIType):
    """Public User Identity"""

    sipURI: str

    telURI: str


@dataclass
class PushNotificationEventData23(OCIType):
    """The common push notification event elements.
    The mobileNumber element is only returned for MOBILE_CALL_INFO events."""

    eventName: str

    silent: bool

    mutableContent: bool

    pushNotificationEventParameters: Optional[str] = None

    mobileNumber: Optional[str] = None


@dataclass
class RandomPort(OCIType):
    """Represents either a random port number, or a specific port number."""

    random: str

    port: int


@dataclass
class Recurrence(OCIType):
    """Defines recurrence."""

    recurDaily: object

    recurWeekly: object

    recurMonthlyByDay: object

    recurMonthlyByWeek: object

    recurYearlyByDay: object

    recurYearlyByWeek: object

    recurForEver: bool

    recurEndDate: int

    recurEndOccurrence: int


@dataclass
class ReplacementCallProcessingPolicyProfileSubscriberTypeList21(OCIType):
    """A list of CallProcessingPolicyProfileSubscriberType21. The list replaces a previously configured list."""

    subscriberType: List[str] = field(default_factory=list)


@dataclass
class ReplacementCombinedNetworkClassOfServiceList(OCIType):
    """A list of network class of services that replaces a previously network class of services."""

    networkClassOfService: List[str] = field(default_factory=list)


@dataclass
class ReplacementCommunicationBarringAlternateCallIndicatorList(OCIType):
    """A list of Communication Barring Alternate Call Indicator that replaces
    a previously configured list. By convention, an element of this type
    may be set nill to clear the list."""

    alternateCallIndicator: List[str] = field(default_factory=list)


@dataclass
class ReplacementCommunicationBarringCallTypeList(OCIType):
    """A list of Communication Barring Call Types that replaces a previously
    configured list. By convention, an element of this type may be set
    nill to clear the list."""

    callType: List[str] = field(default_factory=list)


@dataclass
class ReplacementContactList(OCIType):
    """A list of SIP contacts that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    contact: List[str] = field(default_factory=list)


@dataclass
class ReplacementDeviceTypeList(OCIType):
    """A list of device types that replaces the previously assigned list.
    By convention, an element of this type may be set nill to clear the list."""

    deviceType: List[str] = field(default_factory=list)


@dataclass
class ReplacementNumberPortabilityStatusList(OCIType):
    """A list of Number Portability Query Statuses that replaces a previously
    configured list. By convention, an element of this type may be set
    to nill to clear the list."""

    status: List[str] = field(default_factory=list)


@dataclass
class ReplacementOutgoingDNList(OCIType):
    """A list of outgoing dns that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class ReplacementOutgoingDNorSIPURIList(OCIType):
    """A list of phone numbers or sipuris that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class ReplacementServicePackNameList(OCIType):
    """A list of service packs that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    servicePackName: List[str] = field(default_factory=list)


@dataclass
class ReplacementSIPAliasList(OCIType):
    """A list of SIP aliases that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    sipAlias: List[str] = field(default_factory=list)


@dataclass
class ReplacementTagSetList(OCIType):
    """A list of tag sets that replaces the previously assigned list.
    By convention, an element of this type may be set nill to clear the list."""

    tagSet: List[str] = field(default_factory=list)


@dataclass
class ReplacementUserIdList(OCIType):
    """A list of userIds that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    userId: List[str] = field(default_factory=list)


@dataclass
class ReplacementUserServiceList(OCIType):
    """A list of user services that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    serviceName: List[str] = field(default_factory=list)


@dataclass
class ReplacementVirtualOnNetCallTypeNameList(OCIType):
    """A list of Virtual On-Net Call Types that replaces a previously
    configured list. By convention, an element of this type may be set
    to nill to clear the list."""

    virtualOnNetCallTypeName: List[str] = field(default_factory=list)


@dataclass
class ResponsePagingControl(OCIType):
    """Used in queries to restrict the set of result rows when making a request that can result in
    a large dataset. The client specifies the starting row and the number of rows requested.
    The server only provides those rows in results, if available."""

    responseStartIndex: int

    responsePageSize: int


@dataclass
class ScheduleKey(OCIType):
    """Uniquely identifies Holiday and Time Schedules within a level(System, Service Provider, Group or User level)."""

    scheduleName: str

    scheduleType: str


@dataclass
class SelectiveCallRejectionCriteriaCallType(OCIType):
    """The call type criteria used within an add/get request."""

    fromDnCriteriaSelection: str

    includeAnonymousCallers: bool

    includeUnavailableCallers: bool

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class ServiceActivation(OCIType):
    """Service Instance active status indicator"""

    serviceUserId: str

    isActive: bool


@dataclass
class ServiceProviderAdmin(OCIType):
    """The common Service Provider Admin elements."""

    userId: str

    administratorType: str

    firstName: Optional[str] = None

    lastName: Optional[str] = None

    password: Optional[str] = None

    language: Optional[str] = None


@dataclass
class ServiceProviderCommunicationBarringHierarchicalCallMeNowRule(OCIType):
    """Service Provider Communication Barring Hierarchical Call Me Now Rule"""

    criteria: str

    digitPatternCriteria: str

    action: str

    priority: float

    callTimeoutSeconds: Optional[int] = None

    timeSchedule: Optional[str] = None

    holidaySchedule: Optional[str] = None


@dataclass
class ServiceProviderCommunicationBarringHierarchicalOriginatingRule(OCIType):
    """Service Provider Communication Barring Hierarchical Originating Rule"""

    criteria: str

    digitPatternCriteria: str

    action: str

    priority: float

    treatmentId: Optional[str] = None

    transferNumber: Optional[str] = None

    callTimeoutSeconds: Optional[int] = None

    timeSchedule: Optional[str] = None

    holidaySchedule: Optional[str] = None


@dataclass
class ServiceProviderCommunicationBarringHierarchicalRedirectingRule(OCIType):
    """Service Provider Communication Barring Hierarchical Redirecting Rule"""

    criteria: str

    digitPatternCriteria: str

    action: str

    priority: float

    callTimeoutSeconds: Optional[int] = None

    timeSchedule: Optional[str] = None

    holidaySchedule: Optional[str] = None


@dataclass
class SimultaneousRingNumber(OCIType):
    """Simultaneous Ring number entry."""

    phoneNumber: str

    answerConfirmationRequired: bool


@dataclass
class SIPAuthenticationUserNamePassword(OCIType):
    """User's authentication service information."""

    sipAuthenticationUserName: str

    sipAuthenticationPassword: str


@dataclass
class SIPContactInfo(OCIType):
    """A SIP Contact info contains the SIP registration Contact and its associated Header path
    The following element is only used in AS data mode and ignored in XS data mode:
      pathHeader"""

    sipContact: str

    pathHeader: Optional[str] = None


@dataclass
class SpeedDial100Entry(OCIType):
    """Modify the speed dial 100 prefix setting for a group.
    The response is either a SuccessResponse or an ErrorResponse."""

    speedCode: int

    phoneNumber: str

    description: Optional[str] = None


@dataclass
class SpeedDial100EntryModify(OCIType):
    """Modify the speed dial 100 prefix setting for a group.
    The response is either a SuccessResponse or an ErrorResponse."""

    speedCode: int

    phoneNumber: Optional[str] = None

    description: Optional[str] = None


@dataclass
class SpeedDial8Entry(OCIType):
    """Modify the speed dial 8 prefix setting for a group.
    The response is either a SuccessResponse or an ErrorResponse."""

    speedCode: int

    phoneNumber: Optional[str] = None

    description: Optional[str] = None


@dataclass
class StreetAddress(OCIType):
    """Street address information."""

    addressLine1: Optional[str] = None

    addressLine2: Optional[str] = None

    city: Optional[str] = None

    stateOrProvince: Optional[str] = None

    stateOrProvinceDisplayName: Optional[str] = None

    zipOrPostalCode: Optional[str] = None

    country: Optional[str] = None


@dataclass
class TimeSchedule(OCIType):
    """The from dn criteria."""

    type: str

    name: str


@dataclass
class TrunkGroupDeviceEndpointAdd(OCIType):
    """Trunk group device endpoint used in the context of modify."""

    name: str

    linePort: str

    contact: Optional[str] = None


@dataclass
class TrunkGroupDeviceEndpointModify(OCIType):
    """Trunk group device endpoint used in the context of modify."""

    name: str

    linePort: str

    contact: Optional[str] = None


@dataclass
class TrunkGroupDeviceEndpointRead14sp4(OCIType):
    """Trunk group device endpoint."""

    name: str

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    isPilotUser: bool

    contact: Optional[str] = None


@dataclass
class TrunkGroupDeviceMultipleContactEndpointAdd(OCIType):
    """Trunk group device endpoint used in the context of modify that can have multiple contacts."""

    name: str

    linePort: str

    contact: List[str] = field(default_factory=list)


@dataclass
class TrunkGroupDeviceMultipleContactEndpointRead(OCIType):
    """Trunk group device endpoint that can have multiple contacts."""

    name: str

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    isPilotUser: bool

    contact: List[str] = field(default_factory=list)


@dataclass
class TrunkGroupKey(OCIType):
    """Uniquely identifies a Trunk Group system-wide.
    The trunkGroupName is unique within a group, but not unique system-wide."""

    serviceProviderId: str

    groupId: str

    name: str


@dataclass
class UnboundedNonNegativeInt(OCIType):
    """Unbounded Quantity. Can either be unlimited or a non-negative int quantity."""

    unlimited: bool

    quantity: int


@dataclass
class UnboundedPositiveInt(OCIType):
    """Unbounded Quantity. Can either be unlimited or a positive int quantity."""

    unlimited: bool

    quantity: int


@dataclass
class UserDisplayNames(OCIType):
    """The parts of a user's display name that a client can display in whatever way is appropriate
    for the client application."""

    lastName: str

    firstName: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None


@dataclass
class UserDNExtension(OCIType):
    """User's DN and extension. Used in SearchCriteriaComposedOrDnExtension when either a DN
    or an extension can be used as a search criteria."""

    dn: Optional[str] = None

    extension: Optional[str] = None


@dataclass
class UserEndpointKey(OCIType):
    """Key to uniquely identify a user endpoint."""

    userId: str

    linePort: str


@dataclass
class UserFeatureAccessCodeModifyEntry(OCIType):
    """Feature Access Code Entry to be used in all user modify command."""

    featureAccessCodeName: str

    enableFAC: Optional[bool] = None


@dataclass
class VerifyTranslationAndRoutingOrigination(OCIType):
    """Verification Translation and Routing origination
    value.

     The following element is only used in AS mode:
      userId"""

    linePort: str

    phone: str

    userId: str

    url: str


@dataclass
class VirtualOnNetUserKey(OCIType):
    """Virtual On-Net User identifier which is the Service Provider ID, Group ID,
    and phone number (in E.164 format)."""

    serviceProviderId: str

    groupId: str

    phoneNumber: str


@dataclass
class VoiceMessagingAlternateNoAnswerGreetingRead16(OCIType):
    """The configuration of a alternate no answer greeting.
    It is used when geting a user's voice messaging greeting."""

    name: str

    audioFile: Optional[str] = None

    audioMediaType: Optional[str] = None

    videoFile: Optional[str] = None

    videoMediaType: Optional[str] = None


@dataclass
class XsiPolicyProfileAssignEntry(OCIType):
    """The Xsi policy profile assign entry contains multiple Xsi policy profile
    and one default xsi policy profile."""

    name: List[str] = field(default_factory=list)

    default: Optional[str] = None


@dataclass
class XsiPolicyProfileKey(OCIType):
    """The system Xsi policy profile key."""

    name: str

    level: str


@dataclass
class XsiPolicyProfileUnassignEntry(OCIType):
    """The Xsi policy profile unassign entry contains mutiltipe Xsi policy profile
    and a new replacement default xsi policy profile."""

    name: List[str] = field(default_factory=list)

    newDefault: Optional[str] = None


@dataclass
class SearchCriteria(OCIType):
    """Abstract base type for specifying search criteria. A search criteria is an optional element
    used to restrict the number of rows returned when requesting a potentially large set of
    data from the provisioning server."""


@dataclass
class SearchCriteriaComposedOr(OCIType):
    """Abstract base type for specifying search criteria where the search criteria params are OR'ed.
    A search criteria is an optional element
    used to restrict the number of rows returned when requesting a potentially large set of
    data from the provisioning server."""


@dataclass
class DeviceManagementAutoRebuildConfigEntry(OCIType):
    """Contains one automatic rebuild configuration list entry."""

    ociRequestPrefix: str

    autoRebuildEnabled: Optional[bool] = None


@dataclass
class FileRepositoryProtocolWebDAV20(OCIType):
    """Attributes of the WebDav protocol when the file repository interface is using WebDav."""

    secure: bool

    netAddress: str

    extendedFileCaptureSupport: bool


@dataclass
class ReplacementMediaNameList(OCIType):
    """A list of media that replaces a previously configured list."""

    mediaName: List[str] = field(default_factory=list)


@dataclass
class ReplacementZoneList(OCIType):
    """Contains an ordered list of zones to use to replace the current list of zones in an Office Zone."""

    zoneName: List[str] = field(default_factory=list)


@dataclass
class ServiceAttributeEntry(OCIType):
    """The service attributes name and value pair."""

    name: str

    value: str


@dataclass
class ServiceAttributeEntryRead(OCIType):
    """The service attributes name and value pair."""

    name: str

    value: Optional[str] = None


@dataclass
class XsiApplicationIdEntry(OCIType):
    """The system application Id entry."""

    xsiApplicationId: str

    description: Optional[str] = None


@dataclass
class SortCriteria(OCIType):
    """The sort criteria specifies whether sort is ascending or descending,
    and	whether the sort is case sensitive. Sort order defaults to
    ascending and case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortCriteriaNumeric(OCIType):
    """The sort criteria specifies whether sort is
    ascending or descending.
    Sort order defaults to ascending."""

    isAscending: bool = True


@dataclass
class EnterpriseVoiceVPNDigitManipulation(OCIType):
    """Enterprise Voice VPN Digit Manipulation Entry."""


@dataclass
class EnterpriseVoiceVPNTreatmentEntry(OCIType):
    """Enterprise Voice VPN Treatment entry"""

    id: str

    description: Optional[str] = None


@dataclass
class CustomContactDirectoryEntry(OCIType):
    """Represents either an existing user's Id or an existing Virtual
    On-Net user's DN. For a DN the groupId is used to make it unique
    within an Enterprise, however the groupId is not used with Service
    Providers."""

    userId: str

    virtualOnNetPhoneNumber: str

    groupId: Optional[str] = None


@dataclass
class ServiceProviderVoiceMessagingGroupSettingsAdd(OCIType):
    """A service provider's or enterprise's voice messaging settings used in the context of add."""

    useSystemDefaultDeliveryFromAddress: bool

    useSystemDefaultNotificationFromAddress: bool

    useSystemDefaultVoicePortalLockoutFromAddress: bool

    deliveryFromAddress: Optional[str] = None

    notificationFromAddress: Optional[str] = None

    voicePortalLockoutFromAddress: Optional[str] = None


@dataclass
class ProfileAndServiceAnonymousCallRejectionInfo(OCIType):
    """This is the configuration parameters for anonymous Call Rejection service"""

    isActive: bool


@dataclass
class ProfileAndServiceAutomaticCallbackInfo(OCIType):
    """This is the configuration parameters for anonymous Call Rejection service"""

    isActive: bool


@dataclass
class ProfileAndServiceCallForwardAlwaysInfo(OCIType):
    """This is the configuration parameters for Call Forward Always service"""

    isActive: bool

    isRingSplashActive: bool

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class ProfileAndServiceCallForwardingBusyInfo(OCIType):
    """This is the configuration parameters for Call Forwarding Busy service"""

    isActive: bool

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class ProfileAndServiceCallForwardingNoAnswerInfo(OCIType):
    """This is the configuration parameters for Call Forwarding No Answer service"""

    isActive: bool

    numberOfRings: int

    forwardToPhoneNumber: Optional[str] = None


@dataclass
class ProfileAndServiceCallingLineIDDeliveryBlockingInfo(OCIType):
    """This is the configuration parameters for Calling Line ID Delivery Blocking service"""

    isActive: bool


@dataclass
class ProfileAndServiceCallTransferInfo(OCIType):
    """This is the configuration parameters for Call Transfer service"""

    isRecallActive: bool

    recallNumberOfRings: int

    useDiversionInhibitorForBlindTransfer: bool

    useDiversionInhibitorForConsultativeCalls: bool

    enableBusyCampOn: bool

    busyCampOnSeconds: int


@dataclass
class ProfileAndServiceCallWaitingInfo(OCIType):
    """This is the configuration parameters for Call Transfer service"""

    isActive: bool

    disableCallingLineIdDelivery: bool


@dataclass
class ProfileAndServiceDirectedCallPickupWithBargeInInfo(OCIType):
    """This is the configuration parameters for Directed Call Pickup With Barge In service"""

    enableBargeInWarningTone: bool

    enableAutomaticTargetSelection: bool


@dataclass
class ProfileAndServiceDoNotDisturbInfo(OCIType):
    """This is the configuration parameters for Do Not Disturb service"""

    isActive: bool

    ringSplash: bool


@dataclass
class ProfileAndServiceExternalLineIDDeliveryInfo(OCIType):
    """This is the configuration parameters for External Line ID Delivery service"""

    isActive: bool


@dataclass
class ProfileAndServiceInternalCallingLineIDDeliveryInfo(OCIType):
    """This is the configuration parameters for Internal Calling Line ID Delivery service"""

    isActive: bool


@dataclass
class ProfileAndServiceThirdPartyVoiceMailInfo(OCIType):
    """This is the configuration parameters for Third Party Voice Mail service"""

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
class ReplacementOCICallControlApplicationIdList(OCIType):
    """A list of applicationIds that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    applicationId: List[str] = field(default_factory=list)


@dataclass
class UserMoveMessage(OCIType):
    """The message describes the impact made when moving a user from one group to another group within the enterprise. The message could also contain the error condition that prevents the user move."""

    messageCode: int

    summary: str

    summaryEnglish: str


@dataclass
class AccountAuthorizationCodeEntry(OCIType):
    """Account/Authorization Code."""

    code: str

    description: Optional[str] = None


@dataclass
class AutomaticCollectCallPrefixDigitsEntry(OCIType):
    """The Automatic Collect Call prefix digits entry."""

    countryCode: str

    prefixDigits: str


@dataclass
class BroadWorksMobilityUserMobileIdentityModifyEntry(OCIType):
    """User's Mobile Identity Modify Entry"""

    mobileNumber: str

    description: Optional[str] = None

    isPrimary: Optional[bool] = None

    enableAlerting: Optional[bool] = None


@dataclass
class AgentStatistics(OCIType):
    """Contains Call Center Agent statistics for a given time frame."""

    numberOfCallsHandled: int

    numberOfCallsUnanswered: int

    averageCallSeconds: int

    totalTalkSeconds: int

    totalStaffedSeconds: int


@dataclass
class CallCenterAgentThresholdProfileReplacementNotificationEmailList(OCIType):
    """List of email addresses to which the Agent Threshold Profile email is sent. The list replaces a previously configured list."""

    emailAddress: List[str] = field(default_factory=list)


@dataclass
class CallCenterAgentUnavailableCodeStateModify(OCIType):
    """Contains a Call Center Agent Unavailable Code and its active state"""

    code: str

    isActive: bool


@dataclass
class CallCenterQueueStatistics14sp9(OCIType):
    """Contains Call Center Queue statistics."""

    numberOfBusyOverflows: int

    numberOfCallsAnswered: int

    numberOfCallsAbandoned: int

    numberOfCallsTransferred: int

    numberOfCallsTimedout: int

    averageNumberOfAgentsTalking: float

    averageNumberOfAgentsStaffed: float

    averageWaitSeconds: int

    averageAbandonmentSeconds: int


@dataclass
class CallCenterQueueThresholdReplacementNotificationEmailList(OCIType):
    """List of email addresses to which the Call Center Queue Threshold email is sent. The list replaces a previously configured list."""

    emailAddress: List[str] = field(default_factory=list)


@dataclass
class CallCenterReportAbandonedCallThresholdReplacementList(OCIType):
    """A list of call center reporting abandoned call threshold seconds that replaces a previously configured list."""

    abandonedCallThresholdSeconds: List[int] = field(default_factory=list)


@dataclass
class CallCenterReportCurrentInterval(OCIType):
    """The call center enhanced reporting report current interval, for example, current week."""

    timeUnit: str


@dataclass
class CallCenterReportDataTemplateInfo(OCIType):
    """Call center reporting data template info."""

    dataTemplate: str

    reportType: str

    isRealtimeReport: bool

    isAgentParamRequired: str

    isCallCenterParamRequired: str

    isCallCenterDnisParamRequired: str

    isSamplingPeriodParamRequired: str

    isCallCompletionThresholdParamRequired: str

    isShortDurationThresholdParamRequired: str

    isServiceLevelThresholdParamRequired: str

    isServiceLevelInclusionsParamRequired: str

    isServiceLevelObjectiveThresholdParamRequired: str

    isAbandonedCallThresholdParamRequired: str


@dataclass
class CallCenterReportDataTemplateQueryFilterValueReplacementList(OCIType):
    """A list of call center reporting data template query filter values that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    filterValue: List[str] = field(default_factory=list)


@dataclass
class CallCenterReportPastInterval(OCIType):
    """The call center enhanced reporting report past interval, for example, last 24 month."""

    number: int

    timeUnit: str


@dataclass
class CallCenterReportReplacementEmailList(OCIType):
    """A list of call center reporting email addresses that replaces a previously configured list."""

    emailAddress: List[str] = field(default_factory=list)


@dataclass
class CallCenterReportServiceLevelThresholdReplacementList(OCIType):
    """A list of call center reporting service level threshold seconds that replaces a previously configured list."""

    serviceLevelThresholdSeconds: List[int] = field(default_factory=list)


@dataclass
class CallCenterRoutingPriorityOrder(OCIType):
    """Call center routing order"""

    serviceUserId: str

    priority: float


@dataclass
class CallCenterScheduledReportAgentSelection(OCIType):
    """Either all agents or list of agents."""

    allAgent: bool

    agentUserId: List[str] = field(default_factory=list)


@dataclass
class CallCenterScheduledReportCallCenterSelection(OCIType):
    """Either all call centers or list of call centers."""

    allCallCenter: bool

    serviceUserId: List[str] = field(default_factory=list)


@dataclass
class CallCenterScheduledReportCallCenterSelectionRead(OCIType):
    """User for admin read. Either all call centers or 2 lists of call centers: one for current and one for deleted call centers."""

    allCallCenter: bool

    currentUserId: List[str] = field(default_factory=list)

    pastUserId: List[str] = field(default_factory=list)


@dataclass
class CallCenterScheduledReportDNISSelection(OCIType):
    """Either all DNIS under the specified Call Center or list of DNIS."""

    serviceUserId: str

    allDNIS: bool

    name: List[str] = field(default_factory=list)


@dataclass
class CallCenterScheduledReportDNISSelectionRead(OCIType):
    """Either all DNIS under the specified Call Center or 2 lists of DNIS, one for current one for past (deleted)."""

    serviceUserId: str

    allDNIS: bool

    deleted: Optional[bool] = None

    currentName: List[str] = field(default_factory=list)

    pastName: List[str] = field(default_factory=list)


@dataclass
class CallCenterScheduledReportServiceLevelInclusions(OCIType):
    """The call center enhanced reporting scheduled report inclusions related to the Service Level thresholds"""

    includeOverflowTimeTransferedInServiceLevel: bool

    includeOtherTransfersInServiceLevel: bool

    abandonedCallsInServiceLevel: str

    abandonedCallIntervalSeconds: Optional[int] = None


@dataclass
class CallCenterScheduledReportServiceLevelInclusionsModify(OCIType):
    """The call center enhanced reporting scheduled report modified inclusions related to the Service Level thresholds"""

    includeOverflowTimeTransferedInServiceLevel: Optional[bool] = None

    includeOtherTransfersInServiceLevel: Optional[bool] = None

    abandonedCallsInServiceLevel: Optional[str] = None

    abandonedCallIntervalSeconds: Optional[int] = None


@dataclass
class CallCenterSkillAgentList(OCIType):
    """A list of agents for a particular skill Level."""

    skillLevel: int

    agent: List[str] = field(default_factory=list)


@dataclass
class CallCenterStatisticsRange(OCIType):
    """Statistics Range"""

    start: str

    end: Optional[str] = None


@dataclass
class CallDispositionCodeActivation(OCIType):
    """Contains a Call Center Call Disposition Code and its active state"""

    code: str

    isActive: bool


@dataclass
class CallDispositionCodeWithLevel(OCIType):
    """Contains a Call Center Call Disposition Code and its Level"""

    code: str

    level: str


@dataclass
class CallMeNowToDnCriteria(OCIType):
    """The To dn criteria used on the call me now external number."""

    toDnCriteriaSelection: str

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class CommPilotExpressEmailNotify(OCIType):
    """CommPilot Express Email Notify configuration used in the context of a get."""

    sendEmail: bool

    emailAddress: Optional[str] = None


@dataclass
class CommPilotExpressEmailNotifyModify(OCIType):
    """CommPilot Express Email Notify configuration used in the context of a modify."""

    sendEmail: Optional[bool] = None

    emailAddress: Optional[str] = None


@dataclass
class CommPilotExpressRedirection(OCIType):
    """CommPilot Express type to transfer to voice Mail or forward to a number
    used in the context of a get."""

    action: str

    forwardingPhoneNumber: Optional[str] = None


@dataclass
class CommPilotExpressRedirectionModify(OCIType):
    """CommPilot Express type to transfer to voice Mail or forward to a number
    used in the context of a modify."""

    action: Optional[str] = None

    forwardingPhoneNumber: Optional[str] = None


@dataclass
class CommPilotExpressRedirectionWithException(OCIType):
    """CommPilot Express type to transfer to voice mail or forward to a number
    with certain exceptions used in the context of a get."""

    sendCallsToVoiceMailExceptExcludedNumbers: bool

    excludedPhoneNumber01: Optional[str] = None

    excludedPhoneNumber02: Optional[str] = None

    excludedPhoneNumber03: Optional[str] = None

    forwardExcludedNumbersTo: Optional[str] = None


@dataclass
class CommPilotExpressRedirectionWithExceptionModify(OCIType):
    """CommPilot Express type to transfer to voice mail or forward to a number
    with certain exceptions used in the context of a modify."""

    sendCallsToVoiceMailExceptExcludedNumbers: Optional[bool] = None

    excludedPhoneNumber01: Optional[str] = None

    excludedPhoneNumber02: Optional[str] = None

    excludedPhoneNumber03: Optional[str] = None

    forwardExcludedNumbersTo: Optional[str] = None


@dataclass
class DirectRouteIdentifiers(OCIType):
    """Direct Route identifiers."""

    dtgIdentity: str

    trunkIdentity: str


@dataclass
class DirectRouteReplacementIdentityList(OCIType):
    """A replacement list of direct route parameters."""

    dtgIdentity: str

    trunkIdentity: str


@dataclass
class EnhancedCallLogsRedirectedCallSelection23(OCIType):
    """Redirected call selection.
    When \" redirectedCall \" is set to true, all call logs with redirected call are returned. When it
    set to false, all call logs without redirected call are returned.
    The redirected call can be defined by including a subset of Service Invocation Disposition here.
    If none included, any call has a ServiceInvocationDisposition value defined in ServiceInvocationDisposition21sp1
    is considered as a redirected call."""

    redirectedCall: bool

    redirectType: List[str] = field(default_factory=list)


@dataclass
class ExtendedMixedCallLogsEntry23(OCIType):
    """Extended Call Log entry describing a placed, received, or missed call.
    \"countryCode\" is the user's country code
    The following time elements are represented as timestamp, i.e., the number of milliseconds
    since January 1, 1970, 00:00:00 GMT.
    \"startTime\" represents the time when the system sends out a call invitation message (e.g. for
    placed calls) or receives a call invitation message (e.g. for missed/received calls).
    \"answerTime\" represents the time when the call is answered by the terminating party.
    \"detachedTime\" represents the time when the call is successfully redirected by the system.
    \"releaseTime\" represents the time when the call is released. This time corresponds to the
    moment the call is released by the system, and not necessarily when one party hangs up, since this
    does not always mean the call is released (e.g. Emergency/911 calls).
    The elements \"userGroupId\", \"userId\",\"userPrimaryDn\" and \"userPrimaryExtension\"
    are only returned when the enterprise or group level requests are used.
    The following elements are only used in AS data mode:
      callAuthorizationCode
      securityClassification

    ExtendedMixedCallLogsEntry21sp1 version: only the ServiceInvocationDisposition21sp1 name changed."""

    callLogType: str

    countryCode: str

    callLogId: str

    callId: str

    subscriberType: str

    callingPresentationIndicator: str

    basicCallType: str

    time: str

    startTime: int

    dialedNumber: Optional[str] = None

    calledNumber: Optional[str] = None

    networkTranslatedAddress: Optional[str] = None

    callingAssertedNumber: Optional[str] = None

    callingPresentationNumber: Optional[str] = None

    callingPresentationNumberSource: Optional[str] = None

    callingPresentationName: Optional[str] = None

    callingGroupId: Optional[str] = None

    calledDirectoryName: Optional[str] = None

    calledGroupId: Optional[str] = None

    connectedNumber: Optional[str] = None

    connectedNumberSource: Optional[str] = None

    connectedName: Optional[str] = None

    connectedPresentationIndicator: Optional[str] = None

    typeOfNetwork: Optional[str] = None

    callCategory: Optional[str] = None

    configurableCallType: Optional[str] = None

    alternateCallIndicator: Optional[str] = None

    virtualOnNetCallType: Optional[str] = None

    answerTime: Optional[int] = None

    releaseTime: Optional[int] = None

    detachedTime: Optional[int] = None

    detachedAnswerTime: Optional[int] = None

    outgoingDnis: Optional[str] = None

    serviceInvocationDisposition: Optional[str] = None

    serviceInvocationDialedNumber: Optional[str] = None

    serviceInvocationCalledNumber: Optional[str] = None

    serviceInvocationNetworkTranslatedAddress: Optional[str] = None

    serviceInvocationTypeOfNetwork: Optional[str] = None

    serviceInvocationCallCategory: Optional[str] = None

    serviceInvocationBasicCallType: Optional[str] = None

    serviceInvocationConfigurableCallType: Optional[str] = None

    serviceInvocationAlternateCallIndicator: Optional[str] = None

    serviceInvocationVirtualOnNetCallType: Optional[str] = None

    serviceInvocationCalledDirectoryName: Optional[str] = None

    serviceInvocationCalledGroupId: Optional[str] = None

    redirectingNumber: Optional[str] = None

    redirectingName: Optional[str] = None

    redirectingPresentationIndicator: Optional[str] = None

    RedirectingReason: Optional[str] = None

    accountAuthorizationCode: Optional[str] = None

    callAuthorizationCode: Optional[str] = None

    userGroupId: Optional[str] = None

    userId: Optional[str] = None

    userPrimaryDn: Optional[str] = None

    userPrimaryExtension: Optional[str] = None

    securityClassification: Optional[str] = None

    directRouteNumber: Optional[str] = None

    routeListDN: Optional[str] = None


@dataclass
class ExecutiveAssistantOptInStatus(OCIType):
    """Executive assistant Opt-in status with executive."""

    executiveUserId: str

    optIn: bool


@dataclass
class FindMeFollowMeAlertingGroupReplacementOutgoingDNSIPURIorUserIdList(OCIType):
    """A list of phone numbers/sipuris or user ids that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    phoneNumber: str

    userId: str


@dataclass
class IncomingCallingPlanDigitPatternPermission(OCIType):
    """Indicates whether calls from specified digit patterns are permitted."""

    digitPatternName: str

    allow: bool


@dataclass
class InterceptDNListEntry(OCIType):
    """Intercept User Entry containing the phone number and a Description."""

    phoneNumber: str

    description: Optional[str] = None


@dataclass
class MaliciousCallTraceTimePeriod(OCIType):
    """Modify the user level data associated with Malicious Call Trace.
    The response is either a SuccessResponse or an ErrorResponse."""

    startDateTime: str

    stopDateTime: str


@dataclass
class MeetMeConferencingConferenceDuration(OCIType):
    """Conference duration."""

    hours: int

    minutes: int


@dataclass
class MeetMeConferencingConferenceRecordingKey(OCIType):
    """Identifier for conference recording. startTime is the recording start timestamp."""

    bridgeId: str

    conferenceId: str

    startTime: str


@dataclass
class MeetMeConferencingConferenceSchedule(OCIType):
    """Conference schedule."""

    scheduleReservationless: object

    scheduleOneTime: object

    scheduleRecurring: object


@dataclass
class MusicOnHoldUserSourceModify20(OCIType):
    """Contains the music on hold user source configuration."""

    messageSourceSelection: Optional[str] = None

    customSource: Optional[object] = None


@dataclass
class MusicOnHoldUserSourceRead20(OCIType):
    """Contains the music on hold user source configuration."""

    messageSourceSelection: str

    customSource: Optional[object] = None


@dataclass
class MWIDeliveryToMobileEndpointTemplateActivation23(OCIType):
    """MWI Delivery To Mobile Endpoint enabled status indicator"""

    language: str

    type: str

    isEnabled: bool


@dataclass
class MWIDeliveryToMobileEndpointTemplateLine23(OCIType):
    """MWI Delivery To Mobile Endpoint template section associated with a specific tag."""

    prefix: Optional[str] = None

    tag: Optional[str] = None

    postfix: Optional[str] = None


@dataclass
class OutgoingCallingPlanAuthorizationCodeEntry(OCIType):
    """Outgoing Calling Plan Authorization Code."""

    code: str

    description: Optional[str] = None


@dataclass
class OutgoingCallingPlanCallMeNowPermissions(OCIType):
    """Outgoing Calling Plan for Call Me Now call permissions."""

    group: bool

    local: bool

    tollFree: bool

    toll: bool

    international: bool

    operatorAssisted: bool

    chargeableDirectoryAssisted: bool

    specialServicesI: bool

    specialServicesII: bool

    premiumServicesI: bool

    premiumServicesII: bool

    casual: bool

    urlDialing: bool

    unknown: bool


@dataclass
class OutgoingCallingPlanCallMeNowPermissionsModify(OCIType):
    """Modify outgoing Calling Plan for Call Me Now call permissions."""

    group: Optional[bool] = None

    local: Optional[bool] = None

    tollFree: Optional[bool] = None

    toll: Optional[bool] = None

    international: Optional[bool] = None

    operatorAssisted: Optional[bool] = None

    chargeableDirectoryAssisted: Optional[bool] = None

    specialServicesI: Optional[bool] = None

    specialServicesII: Optional[bool] = None

    premiumServicesI: Optional[bool] = None

    premiumServicesII: Optional[bool] = None

    casual: Optional[bool] = None

    urlDialing: Optional[bool] = None

    unknown: Optional[bool] = None


@dataclass
class OutgoingCallingPlanDigitPatternCallMeNowPermission(OCIType):
    """Indicates whether Call Me Now calls using specified digit patterns are permitted."""

    digitPatternName: str

    permission: bool


@dataclass
class OutgoingCallingPlanDigitPatternOriginatingPermission(OCIType):
    """Indicates whether originating calls using specified digit patterns are permitted."""

    digitPatternName: str

    permission: str


@dataclass
class OutgoingCallingPlanDigitPatternRedirectingPermission(OCIType):
    """Indicates whether redirecting calls using specified digit patterns are permitted."""

    digitPatternName: str

    permission: bool


@dataclass
class OutgoingCallingPlanOriginatingPermissions(OCIType):
    """Outgoing Calling Plan originating call permissions."""

    group: str

    local: str

    tollFree: str

    toll: str

    international: str

    operatorAssisted: str

    chargeableDirectoryAssisted: str

    specialServicesI: str

    specialServicesII: str

    premiumServicesI: str

    premiumServicesII: str

    casual: str

    urlDialing: str

    unknown: str


@dataclass
class OutgoingCallingPlanOriginatingPermissionsModify(OCIType):
    """Outgoing Calling Plan originating call permissions."""

    group: Optional[str] = None

    local: Optional[str] = None

    tollFree: Optional[str] = None

    toll: Optional[str] = None

    international: Optional[str] = None

    operatorAssisted: Optional[str] = None

    chargeableDirectoryAssisted: Optional[str] = None

    specialServicesI: Optional[str] = None

    specialServicesII: Optional[str] = None

    premiumServicesI: Optional[str] = None

    premiumServicesII: Optional[str] = None

    casual: Optional[str] = None

    urlDialing: Optional[str] = None

    unknown: Optional[str] = None


@dataclass
class OutgoingCallingPlanRedirectedPermissions(OCIType):
    """Outgoing Calling Plan being forwarded/transferred permissions."""

    outsideGroup: bool


@dataclass
class OutgoingCallingPlanRedirectedPermissionsModify(OCIType):
    """Outgoing Calling Plan being forwarded/transferred permissions."""

    outsideGroup: Optional[bool] = None


@dataclass
class OutgoingCallingPlanRedirectingPermissions(OCIType):
    """Outgoing Calling Plan initiating call forwards/transfer permissions."""

    group: bool

    local: bool

    tollFree: bool

    toll: bool

    international: bool

    operatorAssisted: bool

    chargeableDirectoryAssisted: bool

    specialServicesI: bool

    specialServicesII: bool

    premiumServicesI: bool

    premiumServicesII: bool

    casual: bool

    urlDialing: bool

    unknown: bool


@dataclass
class OutgoingCallingPlanRedirectingPermissionsModify(OCIType):
    """Outgoing Calling Plan initiating call forwards/transfer permissions."""

    group: Optional[bool] = None

    local: Optional[bool] = None

    tollFree: Optional[bool] = None

    toll: Optional[bool] = None

    international: Optional[bool] = None

    operatorAssisted: Optional[bool] = None

    chargeableDirectoryAssisted: Optional[bool] = None

    specialServicesI: Optional[bool] = None

    specialServicesII: Optional[bool] = None

    premiumServicesI: Optional[bool] = None

    premiumServicesII: Optional[bool] = None

    casual: Optional[bool] = None

    urlDialing: Optional[bool] = None

    unknown: Optional[bool] = None


@dataclass
class OutgoingCallingPlanTransferNumbers(OCIType):
    """Outgoing Calling Plan transfer numbers."""

    phoneNumber01: Optional[str] = None

    phoneNumber02: Optional[str] = None

    phoneNumber03: Optional[str] = None


@dataclass
class OutgoingCallingPlanTransferNumbersModify(OCIType):
    """Outgoing Calling Plan transfer numbers."""

    phoneNumber01: Optional[str] = None

    phoneNumber02: Optional[str] = None

    phoneNumber03: Optional[str] = None


@dataclass
class OutgoingPinholeDigitPlanDigitPatternCallMeNowPermission(OCIType):
    """Indicates whether Call Me Now calls using specified Pinhole digit patterns are permitted."""

    digitPatternName: str

    permission: str


@dataclass
class OutgoingPinholeDigitPlanDigitPatternOriginatingPermission(OCIType):
    """Indicates whether originating calls using specified Pinhole digit patterns are permitted."""

    digitPatternName: str

    permission: str


@dataclass
class OutgoingPinholeDigitPlanDigitPatternRedirectingPermission(OCIType):
    """Indicates whether redirecting calls using specified Pinhole digit patterns are permitted."""

    digitPatternName: str

    permission: str


@dataclass
class OrderedCriteriaList(OCIType):
    """A list of criteria names that defines the order priority."""

    criteriaName: List[str] = field(default_factory=list)


@dataclass
class GroupPreferredCarrierName(OCIType):
    """Group can either use it's service provider/enterprise's preferred carrier or use it's own.
    The group carrier name is exposed if it was previously configured."""

    useServiceProviderPreferredCarrier: bool

    carrier: Optional[str] = None


@dataclass
class GroupPreferredCarrierNameModify(OCIType):
    """Group can either use it's service provider/enterprise's preferred carrier or use it's own.
    You can use the Service Provider preferred carrier without clearing the group
    carrier name -- in this case, the group carrier name is retained."""

    useServiceProviderPreferredCarrier: bool

    carrier: Optional[str] = None


@dataclass
class UserPreferredCarrierName(OCIType):
    """User can either use it's group's preferred carrier or use it's own.
    The user carrier name is exposed if it was previously configured."""

    useGroupPreferredCarrier: bool

    carrier: Optional[str] = None


@dataclass
class UserPreferredCarrierNameModify(OCIType):
    """User can either use it's group's preferred carrier or use it's own.
    You can use the group's preferred carrier without clearing the user carrier name --
    in this case, the user carrier name is retained."""

    useGroupPreferredCarrier: bool

    carrier: Optional[str] = None


@dataclass
class EnterpriseTrunkReplacementNumberPrefixList(OCIType):
    """A list of prefixes that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    numberPrefix: List[str] = field(default_factory=list)


@dataclass
class ReplacementDNList(OCIType):
    """A list of dns that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class SequentialRingLocation14sp4(OCIType):
    """Sequential Ring Location."""

    numberOfRings: int

    answerConfirmationRequired: bool

    phoneNumber: Optional[str] = None


@dataclass
class SequentialRingLocationModify(OCIType):
    """Sequential Ring Location."""

    phoneNumber: Optional[str] = None

    numberOfRings: Optional[int] = None

    answerConfirmationRequired: Optional[bool] = None


@dataclass
class EnterpriseTrunkTrunkGroupKey(OCIType):
    """Identifies a trunk group within an Enterprise Trunk where the service provider id is already known."""

    groupId: str

    trunkGroupName: str


@dataclass
class GroupEnterpriseTrunkPriorityWeightedTrunkGroup(OCIType):
    """Trunk group details (order and weight) for each trunk group"""

    trunkGroup: str

    priority: int

    weight: int


@dataclass
class ReplacementEnterpriseTrunkTrunkGroupList(OCIType):
    """A list of Group Trunk Krunk Group Names that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    trunkGroup: List[str] = field(default_factory=list)


@dataclass
class ReplacementGroupEnterpriseTrunkTrunkGroupList(OCIType):
    """A list of Group Trunk Krunk Group Names that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    trunkGroup: List[str] = field(default_factory=list)


@dataclass
class VirtualOnNetUser(OCIType):
    """Virtual On-Net User."""

    phoneNumber: str

    extension: str

    firstName: str

    lastName: str

    callingLineIdFirstName: str

    callingLineIdLastName: str

    virtualOnNetCallTypeName: str


@dataclass
class AdditionalMessageOptionsMenuKeysModifyEntry(OCIType):
    """The voice portal additional message options modify entry."""

    saveMessage: Optional[str] = None

    deleteMessage: Optional[str] = None

    playEnvelope: Optional[str] = None

    callbackCaller: Optional[str] = None

    composeMessage: Optional[str] = None

    replyMessage: Optional[str] = None

    forwardMessage: Optional[str] = None

    personalizedName: Optional[str] = None

    passcode: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class AdditionalMessageOptionsMenuKeysReadEntry(OCIType):
    """The voice portal additional message options menu keys."""

    returnToPreviousMenu: str

    saveMessage: Optional[str] = None

    deleteMessage: Optional[str] = None

    playEnvelope: Optional[str] = None

    callbackCaller: Optional[str] = None

    composeMessage: Optional[str] = None

    replyMessage: Optional[str] = None

    forwardMessage: Optional[str] = None

    personalizedName: Optional[str] = None

    passcode: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class AnnouncementMenuKeysModifyEntry(OCIType):
    """The voice portal announcement menu keys modify entry."""

    recordAudio: Optional[str] = None

    recordAudioVideo: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class AnnouncementMenuKeysReadEntry(OCIType):
    """The voice portal announcement menu keys."""

    returnToPreviousMenu: str

    recordAudio: Optional[str] = None

    recordAudioVideo: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class AnnouncementRecordingMenuKeysModifyEntry(OCIType):
    """The voice portal announcement recording menu keys modify entry."""

    acceptRecording: Optional[str] = None

    rejectRerecord: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None

    end: Optional[str] = None


@dataclass
class AnnouncementRecordingMenuKeysReadEntry(OCIType):
    """The voice portal announcement recording menu keys."""

    acceptRecording: str

    rejectRerecord: str

    returnToPreviousMenu: str

    end: str

    repeatMenu: Optional[str] = None


@dataclass
class CallForwardingOptionsMenuKeysModifyEntry(OCIType):
    """The voice portal call forwarding option menu keys modify entry."""

    activateCallForwarding: Optional[str] = None

    deactivateCallForwarding: Optional[str] = None

    changeCallForwardingDestination: Optional[str] = None

    listenToCallForwardingStatus: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class CallForwardingOptionsMenuKeysReadEntry(OCIType):
    """"""

    returnToPreviousMenu: str

    activateCallForwarding: Optional[str] = None

    deactivateCallForwarding: Optional[str] = None

    changeCallForwardingDestination: Optional[str] = None

    listenToCallForwardingStatus: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ChangeBusyOrNoAnswerGreetingMenuKeysModifyEntry(OCIType):
    """The voice portal change busy or not answer greeting menu keys modify entry."""

    recordNewGreeting: Optional[str] = None

    listenToCurrentGreeting: Optional[str] = None

    revertToSystemDefaultGreeting: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ChangeBusyOrNoAnswerGreetingMenuKeysReadEntry(OCIType):
    """The voice portal change busy or not answer greeting menu keys."""

    returnToPreviousMenu: str

    recordNewGreeting: Optional[str] = None

    listenToCurrentGreeting: Optional[str] = None

    revertToSystemDefaultGreeting: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ChangeCallForwardingDestinationMenuKeysModifyEntry(OCIType):
    """The voice portal change call forwarding destination menu keys modify entry."""

    finishEnteringNewDestinationNumber: Optional[str] = None


@dataclass
class ChangeCallForwardingDestinationMenuKeysReadEntry(OCIType):
    """The voice portal change call forwarding destination menu keys."""

    finishEnteringNewDestinationNumber: str


@dataclass
class ChangeCurrentIntroductionOrMessageOrReplyMenuKeysModifyEntry(OCIType):
    """The voice portal change current introduction or message or reply menu keys modify entry."""

    endRecording: Optional[str] = None


@dataclass
class ChangeCurrentIntroductionOrMessageOrReplyMenuKeysReadEntry(OCIType):
    """The voice portal change current introduction or message or reply menu keys."""

    endRecording: str


@dataclass
class ChangeExtendedAwayGreetingMenuKeysModifyEntry(OCIType):
    """The voice portal change extended away greeting menu keys modify entry."""

    activateExtendedAwayGreeting: Optional[str] = None

    deactivateExtendedAwayGreeting: Optional[str] = None

    recordNewGreeting: Optional[str] = None

    listenToCurrentGreeting: Optional[str] = None

    enableMessageDeposit: Optional[str] = None

    disableMessageDeposit: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ChangeExtendedAwayGreetingMenuKeysReadEntry(OCIType):
    """The voice portal change extended away greeting menu keys."""

    returnToPreviousMenu: str

    activateExtendedAwayGreeting: Optional[str] = None

    deactivateExtendedAwayGreeting: Optional[str] = None

    recordNewGreeting: Optional[str] = None

    listenToCurrentGreeting: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class CommPilotExpressProfileMenuKeysModifyEntry(OCIType):
    """The voice portal commPilot express profile menu keys modify entry."""

    activateAvailableInOfficeProfile: Optional[str] = None

    activateAvailableOutOfOfficeProfile: Optional[str] = None

    activateBusyProfile: Optional[str] = None

    activateUnavailableProfile: Optional[str] = None

    noProfile: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class CommPilotExpressProfileMenuKeysReadEntry(OCIType):
    """The voice portal commPilot express profile menu keys."""

    returnToPreviousMenu: str

    activateAvailableInOfficeProfile: Optional[str] = None

    activateAvailableOutOfOfficeProfile: Optional[str] = None

    activateBusyProfile: Optional[str] = None

    activateUnavailableProfile: Optional[str] = None

    noProfile: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ConferenceGreetingMenuKeysModifyEntry(OCIType):
    """The voice portal greeting menu keys modify entry."""

    activateConfGreeting: Optional[str] = None

    deactivateConfGreeting: Optional[str] = None

    recordNewConfGreeting: Optional[str] = None

    listenToCurrentConfGreeting: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ConferenceGreetingMenuKeysReadEntry(OCIType):
    """The voice portal conference greeting menu keys."""

    returnToPreviousMenu: str

    activateConfGreeting: Optional[str] = None

    deactivateConfGreeting: Optional[str] = None

    recordNewConfGreeting: Optional[str] = None

    listenToCurrentConfGreeting: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class DeleteAllMessagesMenuKeysModifyEntry(OCIType):
    """The voice portal delete all messages menu keys modify entry modify entry."""

    confirmDeletion: Optional[str] = None

    cancelDeletion: Optional[str] = None


@dataclass
class DeleteAllMessagesMenuKeysReadEntry(OCIType):
    """The voice portal delete all messages menu keys."""

    confirmDeletion: str

    cancelDeletion: str


@dataclass
class DisableMessageDepositMenuKeysModifyEntry(OCIType):
    """The voice portal disable message deposit menu keys modify entry."""

    disconnectAfterGreeting: Optional[str] = None

    forwardAfterGreeting: Optional[str] = None

    changeForwardingDestination: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class DisableMessageDepositMenuKeysReadEntry(OCIType):
    """The voice portal disable message deposit menu keys."""

    returnToPreviousMenu: str

    disconnectAfterGreeting: Optional[str] = None

    forwardAfterGreeting: Optional[str] = None

    changeForwardingDestination: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class FaxMessagingMenuKeysModifyEntry(OCIType):
    """The voice portal fax messaging menu keys modify entry."""

    saveFaxMessageAndSkipToNext: Optional[str] = None

    previousFaxMessage: Optional[str] = None

    playEnvelope: Optional[str] = None

    nextFaxMessage: Optional[str] = None

    deleteFaxMessage: Optional[str] = None

    printFaxMessage: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None


@dataclass
class FaxMessagingMenuKeysReadEntry(OCIType):
    """The voice portal fax messaging menu keys."""

    saveFaxMessageAndSkipToNext: Optional[str] = None

    previousFaxMessage: Optional[str] = None

    playEnvelope: Optional[str] = None

    nextFaxMessage: Optional[str] = None

    deleteFaxMessage: Optional[str] = None

    printFaxMessage: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None


@dataclass
class ForwardOrComposeMessageMenuKeysModifyEntry(OCIType):
    """The voice portal forward or compose message menu keys modify entry."""

    sendToPerson: Optional[str] = None

    sendToAllGroupMembers: Optional[str] = None

    sendToDistributionList: Optional[str] = None

    changeCurrentIntroductionOrMessage: Optional[str] = None

    listenToCurrentIntroductionOrMessage: Optional[str] = None

    setOrClearUrgentIndicator: Optional[str] = None

    setOrClearConfidentialIndicator: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ForwardOrComposeMessageMenuKeysReadEntry(OCIType):
    """The voice portal forward or compose message menu keys."""

    returnToPreviousMenu: str

    sendToPerson: Optional[str] = None

    sendToAllGroupMembers: Optional[str] = None

    sendToDistributionList: Optional[str] = None

    changeCurrentIntroductionOrMessage: Optional[str] = None

    listenToCurrentIntroductionOrMessage: Optional[str] = None

    setOrClearUrgentIndicator: Optional[str] = None

    setOrClearConfidentialIndicator: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class GreetingOnlyForwardingDestinationMenuKeysModifyEntry(OCIType):
    """The voice portal greeting only forwarding destination menu keys modify entry."""

    greetingOnlyForwardingDestination: Optional[str] = None


@dataclass
class GreetingOnlyForwardingDestinationMenuKeysReadEntry(OCIType):
    """The voice portal greeting only forwarding destination menu keys."""

    greetingOnlyForwardingDestination: Optional[str] = None


@dataclass
class GreetingsMenuKeysModifyEntry(OCIType):
    """The voice portal greeting menu keys modify entry."""

    personalizedName: Optional[str] = None

    conferenceGreeting: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class GreetingsMenuKeysReadEntry(OCIType):
    """The voice portal greeting menu keys."""

    returnToPreviousMenu: str

    personalizedName: Optional[str] = None

    conferenceGreeting: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class HotelingMenuKeysModifyEntry(OCIType):
    """The voice portal hoteling menu keys modify entry."""

    checkHostStatus: Optional[str] = None

    associateWithHost: Optional[str] = None

    disassociateFromHost: Optional[str] = None

    disassociateFromRemoteHost: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class HotelingMenuKeysReadEntry(OCIType):
    """The voice portal hoteling menu keys."""

    returnToPreviousMenu: str

    checkHostStatus: Optional[str] = None

    associateWithHost: Optional[str] = None

    disassociateFromHost: Optional[str] = None

    disassociateFromRemoteHost: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class MessageDepositMenuKeysModifyEntry(OCIType):
    """The voice portal message deposit menu keys modify entry."""

    enableMessageDeposit: Optional[str] = None

    disableMessageDeposit: Optional[str] = None

    listenToMessageDepositStatus: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class MessageDepositMenuKeysReadEntry(OCIType):
    """The voice portal message deposit menu keys."""

    returnToPreviousMenu: str

    enableMessageDeposit: Optional[str] = None

    disableMessageDeposit: Optional[str] = None

    listenToMessageDepositStatus: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class PasscodeMenuKeysModifyEntry(OCIType):
    """The voice portal passcode menu keys modify entry."""

    finishEnteringOrReenteringPasscode: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None


@dataclass
class PasscodeMenuKeysReadEntry(OCIType):
    """The voice portal passcode menu keys."""

    finishEnteringOrReenteringPasscode: str

    returnToPreviousMenu: str


@dataclass
class PersonalAssistantMenuKeysModifyEntry(OCIType):
    """The voice portal personal assistant menu keys modify entry."""

    setPresenceToNone: Optional[str] = None

    setPresenceToBusinessTrip: Optional[str] = None

    setPresenceToGoneForTheDay: Optional[str] = None

    setPresenceToLunch: Optional[str] = None

    setPresenceToMeeting: Optional[str] = None

    setPresenceToOutOfOffice: Optional[str] = None

    setPresenceToTemporarilyOut: Optional[str] = None

    setPresenceToTraining: Optional[str] = None

    setPresenceToUnavailable: Optional[str] = None

    setPresenceToVacation: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class PersonalAssistantMenuKeysReadEntry(OCIType):
    """The voice portal personal assistant menu keys."""

    returnToPreviousMenu: str

    setPresenceToNone: Optional[str] = None

    setPresenceToBusinessTrip: Optional[str] = None

    setPresenceToGoneForTheDay: Optional[str] = None

    setPresenceToLunch: Optional[str] = None

    setPresenceToMeeting: Optional[str] = None

    setPresenceToOutOfOffice: Optional[str] = None

    setPresenceToTemporarilyOut: Optional[str] = None

    setPresenceToTraining: Optional[str] = None

    setPresenceToUnavailable: Optional[str] = None

    setPresenceToVacation: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class PersonalizedNameMenuKeysModifyEntry(OCIType):
    """The voice portal personalized name menu keys modify entry."""

    recordNewPersonalizedName: Optional[str] = None

    listenToCurrentPersonalizedName: Optional[str] = None

    deletePersonalizedName: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class PersonalizedNameMenuKeysReadEntry(OCIType):
    """The voice portal personalized name menu keys."""

    returnToPreviousMenu: str

    recordNewPersonalizedName: Optional[str] = None

    listenToCurrentPersonalizedName: Optional[str] = None

    deletePersonalizedName: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class PlayGreetingMenuKeysModifyEntry(OCIType):
    """The voice portal play greeting menu keys modify entry."""

    skipBackward: Optional[str] = None

    pauseOrResume: Optional[str] = None

    skipForward: Optional[str] = None

    jumpToBegin: Optional[str] = None

    jumpToEnd: Optional[str] = None


@dataclass
class PlayGreetingMenuKeysReadEntry(OCIType):
    """The voice portal play greeting menu keys."""

    skipBackward: Optional[str] = None

    pauseOrResume: Optional[str] = None

    skipForward: Optional[str] = None

    jumpToBegin: Optional[str] = None

    jumpToEnd: Optional[str] = None


@dataclass
class PlayMessageMenuKeysModifyEntry(OCIType):
    """The voice portal play message menu keys modify entry."""

    skipBackward: Optional[str] = None

    pauseOrResume: Optional[str] = None

    skipForward: Optional[str] = None

    jumpToBegin: Optional[str] = None

    jumpToEnd: Optional[str] = None


@dataclass
class PlayMessageMenuKeysReadEntry(OCIType):
    """The voice portal play message menu keys."""

    skipBackward: Optional[str] = None

    pauseOrResume: Optional[str] = None

    skipForward: Optional[str] = None

    jumpToBegin: Optional[str] = None

    jumpToEnd: Optional[str] = None


@dataclass
class PlayMessagesMenuKeysModifyEntry(OCIType):
    """The voice portal play message menu keys modify entry."""

    saveMessage: Optional[str] = None

    deleteMessage: Optional[str] = None

    playMessage: Optional[str] = None

    previousMessage: Optional[str] = None

    playEnvelope: Optional[str] = None

    nextMessage: Optional[str] = None

    callbackCaller: Optional[str] = None

    composeMessage: Optional[str] = None

    replyMessage: Optional[str] = None

    forwardMessage: Optional[str] = None

    additionalMessageOptions: Optional[str] = None

    personalizedName: Optional[str] = None

    passcode: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class PlayMessagesMenuKeysReadEntry(OCIType):
    """The voice portal play message menu keys."""

    returnToPreviousMenu: str

    saveMessage: Optional[str] = None

    deleteMessage: Optional[str] = None

    playMessage: Optional[str] = None

    previousMessage: Optional[str] = None

    playEnvelope: Optional[str] = None

    nextMessage: Optional[str] = None

    callbackCaller: Optional[str] = None

    composeMessage: Optional[str] = None

    replyMessage: Optional[str] = None

    forwardMessage: Optional[str] = None

    additionalMessageOptions: Optional[str] = None

    personalizedName: Optional[str] = None

    passcode: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class RecordNewGreetingOrPersonalizedNameMenuKeysModifyEntry(OCIType):
    """The voice portal record new greeting or personalized name menu keys modify entry."""

    endRecording: Optional[str] = None


@dataclass
class RecordNewGreetingOrPersonalizedNameMenuKeysReadEntry(OCIType):
    """The voice portal record new greeting or personalized name menu keys."""

    endRecording: str


@dataclass
class ReplyMessageMenuKeysModifyEntry(OCIType):
    """The voice portal reply message menu keys modify entry."""

    sendReplyToCaller: Optional[str] = None

    changeCurrentReply: Optional[str] = None

    listenToCurrentReply: Optional[str] = None

    setOrClearUrgentIndicator: Optional[str] = None

    setOrClearConfidentialIndicator: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ReplyMessageMenuKeysReadEntry(OCIType):
    """The voice portal reply message menu keys."""

    sendReplyToCaller: str

    returnToPreviousMenu: str

    changeCurrentReply: Optional[str] = None

    listenToCurrentReply: Optional[str] = None

    setOrClearUrgentIndicator: Optional[str] = None

    setOrClearConfidentialIndicator: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class ReviewSelectedDistributionListMenuKeysModifyEntry(OCIType):
    """The voice portal review selected distribution list menu keys modify entry."""

    interruptPlaybackAndReturnToPreviousMenu: Optional[str] = None


@dataclass
class ReviewSelectedDistributionListMenuKeysReadEntry(OCIType):
    """The voice portal review selected distribution list menu keys."""

    interruptPlaybackAndReturnToPreviousMenu: str


@dataclass
class SelectDistributionListMenuKeysModifyEntry(OCIType):
    """The voice portal select distribution list menu keys modify entry."""

    returnToPreviousMenu: Optional[str] = None

    repeatMenuOrFinishEnteringDistributionListNumber: Optional[str] = None


@dataclass
class SelectDistributionListMenuKeysReadEntry(OCIType):
    """The voice portal select distribution list menu keys."""

    returnToPreviousMenu: str

    repeatMenuOrFinishEnteringDistributionListNumber: Optional[str] = None


@dataclass
class SendMessageToSelectedDistributionListMenuKeysModifyEntry(OCIType):
    """The voice portal send message to selected distribution list menu keys modify entry."""

    confirmSendingToDistributionList: Optional[str] = None

    cancelSendingToDistributionList: Optional[str] = None


@dataclass
class SendMessageToSelectedDistributionListMenuKeysReadEntry(OCIType):
    """The voice portal send message to selected distribution list menu keys."""

    cancelSendingToDistributionList: str

    confirmSendingToDistributionList: Optional[str] = None


@dataclass
class SendToAllGroupMembersMenuKeysModifyEntry(OCIType):
    """The voice portal send to all group memeber menu keys modify entry."""

    confirmSendingToEntireGroup: Optional[str] = None

    cancelSendingToEntireGroup: Optional[str] = None


@dataclass
class SendToAllGroupMembersMenuKeysReadEntry(OCIType):
    """The voice portal send to all group memeber menu keys."""

    confirmSendingToEntireGroup: str

    cancelSendingToEntireGroup: str


@dataclass
class SendToDistributionListMenuKeysModifyEntry(OCIType):
    """The voice portal send to distribution list menu keys modify entry."""

    sendMessageToSelectedDistributionList: Optional[str] = None

    selectDistributionList: Optional[str] = None

    reviewSelectedDistributionList: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class SendToDistributionListMenuKeysReadEntry(OCIType):
    """The voice portal send to distribution list menu keys."""

    sendMessageToSelectedDistributionList: str

    returnToPreviousMenu: str

    selectDistributionList: Optional[str] = None

    reviewSelectedDistributionList: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class SendToPersonMenuKeysModifyEntry(OCIType):
    """The voice portal send to person menu keys modify entry."""

    confirmSendingMessage: Optional[str] = None

    cancelSendingMessage: Optional[str] = None

    finishEnteringNumberWhereToSendMessageTo: Optional[str] = None

    finishForwardingOrSendingMessage: Optional[str] = None


@dataclass
class SendToPersonMenuKeysReadEntry(OCIType):
    """The voice portal send to person menu keys."""

    confirmSendingMessage: str

    cancelSendingMessage: str

    finishEnteringNumberWhereToSendMessageTo: str

    finishForwardingOrSendingMessage: str


@dataclass
class VoiceMessagingAliasReplacementList(OCIType):
    """A list of dns that that replaces a previously configured list.
    By convention, an element of this type may be set nil to clear the list."""

    phoneNumber: List[str] = field(default_factory=list)


@dataclass
class VoiceMessagingMenuKeysModifyEntry(OCIType):
    """The voice portal voice messaging menu keys modify entry."""

    playMessages: Optional[str] = None

    changeBusyGreeting: Optional[str] = None

    changeNoAnswerGreeting: Optional[str] = None

    changeExtendedAwayGreeting: Optional[str] = None

    composeMessage: Optional[str] = None

    deleteAllMessages: Optional[str] = None

    passcode: Optional[str] = None

    personalizedName: Optional[str] = None

    messageDeposit: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class VoiceMessagingMenuKeysReadEntry(OCIType):
    """The voice portal voice messaging menu keys."""

    returnToPreviousMenu: str

    playMessages: Optional[str] = None

    changeBusyGreeting: Optional[str] = None

    changeNoAnswerGreeting: Optional[str] = None

    changeExtendedAwayGreeting: Optional[str] = None

    composeMessage: Optional[str] = None

    deleteAllMessages: Optional[str] = None

    passcode: Optional[str] = None

    personalizedName: Optional[str] = None

    messageDeposit: Optional[str] = None

    repeatMenu: Optional[str] = None


@dataclass
class VoicePortalCallingMenuKeysModifyEntry(OCIType):
    """The voice portal calling menu keys modify entry."""

    endCurrentCallAndGoBackToPreviousMenu: Optional[str] = None

    returnToPreviousMenu: Optional[str] = None


@dataclass
class VoicePortalCallingMenuKeysReadEntry(OCIType):
    """The voice portal change calling menu keys."""

    endCurrentCallAndGoBackToPreviousMenu: str

    returnToPreviousMenu: str


@dataclass
class VoicePortalLoginMenuKeysModifyEntry(OCIType):
    """The voice portal voice portal login menu keys modify entry."""

    accessUsingOtherMailboxId: Optional[str] = None


@dataclass
class VoicePortalLoginMenuKeysReadEntry(OCIType):
    """The voice portal login menu keys."""

    accessUsingOtherMailboxId: Optional[str] = None


@dataclass
class VoicePortalMainMenuKeysModifyEntry(OCIType):
    """The voice portal main menu keys modify entry."""

    voiceMessaging: Optional[str] = None

    commPilotExpressProfile: Optional[str] = None

    greetings: Optional[str] = None

    callForwardingOptions: Optional[str] = None

    voicePortalCalling: Optional[str] = None

    hoteling: Optional[str] = None

    passcode: Optional[str] = None

    exitVoicePortal: Optional[str] = None

    repeatMenu: Optional[str] = None

    externalRouting: Optional[str] = None

    announcement: Optional[str] = None

    personalAssistant: Optional[str] = None


@dataclass
class VoicePortalMainMenuKeysReadEntry(OCIType):
    """The voice portal main menu keys."""

    voiceMessaging: Optional[str] = None

    commPilotExpressProfile: Optional[str] = None

    greetings: Optional[str] = None

    callForwardingOptions: Optional[str] = None

    voicePortalCalling: Optional[str] = None

    hoteling: Optional[str] = None

    passcode: Optional[str] = None

    exitVoicePortal: Optional[str] = None

    repeatMenu: Optional[str] = None

    externalRouting: Optional[str] = None

    announcement: Optional[str] = None

    personalAssistant: Optional[str] = None


@dataclass
class OCITableRow(OCIType):
    """The OCITableRow type is used in responses only, never in requests. It occurs
    inside the OCITable type. The OCITableRow consists columns of strings.
    Clients should not assume any particular column order as future
    revisions of the protocol may move or add columns. See the OCITable data type
    for more information."""

    col: List[str] = field(default_factory=list)


@dataclass
class ExternalUserIdentity(OCIType):
    """External user identity id identifies pre-authenticated user/admin id performing a session-less OCI request.
    id can be a user/admin’s primary Id/alternate Id/external Id.
    organizationId identifies organization id the user/admin belongs to."""

    id: str
    # The ID of the user or administrator initiating the OCI-P request.
    # The ID must match a primary, alternate or external ID configured on the AS for
    # a user or administrator

    organizationId: str
    # The ID of the user or administrator's organization
    # The ID must match a service provider or enterprise external id

    role: str


# The role of the external user identity.


@dataclass
class GroupCallQueueAnnouncementDescriptionList(OCIType):
    """Contains a list of file descriptions for audio files."""

    fileDescription1: Optional[str] = None

    fileDescription2: Optional[str] = None

    fileDescription3: Optional[str] = None

    fileDescription4: Optional[str] = None


@dataclass
class GroupCallQueueAnnouncementMediaFileTypeList(OCIType):
    """Contains a list of file media types for audio files."""

    mediaType1: Optional[str] = None

    mediaType2: Optional[str] = None

    mediaType3: Optional[str] = None

    mediaType4: Optional[str] = None


@dataclass
class GroupCallQueueMusicOnHoldSourceRead(OCIType):
    """Contains the Group Call Queue music on hold source configuration."""

    audioMessageSourceSelection: str

    audioFileDescription: Optional[str] = None

    audioMediaType: Optional[str] = None


@dataclass
class AccessDeviceEndpointAndHotlineModify(OCIType):
    """Access device end point used in the context of modify.
    Port numbers are only used by devices with static line ordering.
    The following element is only used in AS data mode and ignored in XS data mode:
      pathHeader
      useHotline
      hotlineContact"""

    accessDevice: AccessDevice

    linePort: str

    contact: Optional[str] = None

    pathHeader: Optional[str] = None

    portNumber: Optional[int] = None

    useHotline: Optional[bool] = None

    hotlineContact: Optional[str] = None


@dataclass
class AccessDeviceMultipleIdentityAndContactEndpointAdd(OCIType):
    """Access device end point used in the context of add that can have more than one contact defined.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Only Static Registration capabable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity"""

    accessDevice: AccessDevice

    linePort: str

    privateIdentity: Optional[str] = None

    contact: List[str] = field(default_factory=list)

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceEndpointWithPortNumberRead(OCIType):
    """Access device end point.
    Port numbers are only used by devices with static line ordering."""

    accessDevice: AccessDevice

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    contact: Optional[str] = None

    portNumber: Optional[int] = None


@dataclass
class EnterpriseAccessDevice(OCIType):
    """Uniquely identifies an access device accessible for an enterprise. It could be a system level device, an enterprise level device or a group level device."""

    accessDevice: AccessDevice

    groupId: Optional[str] = None


@dataclass
class AccessDeviceEndpointModify(OCIType):
    """Access device end point used in the context of modify.
    Port numbers are only used by devices with static line ordering.
    The following element is only used in AS data mode and ignored in XS data mode:
      pathHeader"""

    accessDevice: AccessDevice

    linePort: str

    contact: Optional[str] = None

    pathHeader: Optional[str] = None

    portNumber: Optional[int] = None


@dataclass
class ReplacementDeviceList(OCIType):
    """A list of devices that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    device: List[AccessDevice] = field(default_factory=list)


@dataclass
class AccessDeviceMultipleIdentityAndContactEndpointRead(OCIType):
    """Access device end point that can have multiple contacts.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
          Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and not returned in AS data mode:
      privateIdentity
    The following elements are only used in AS data mode and a value false is returned in the XS mode:
      supportVisualDeviceManagement"""

    accessDevice: AccessDevice

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    supportVisualDeviceManagement: bool

    privateIdentity: Optional[str] = None

    contact: List[str] = field(default_factory=list)

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceEndpointWithPortNumberRead22V2(OCIType):
    """Access device end point.
    Port numbers are only used by devices with static line ordering.
    The following element is only used in AS data mode and ignored in XS data mode:
      pathHeader
      hotlineContact

    The following elements are only used in AS data mode and a value false is returned in the XS mode:
      useHotline"""

    accessDevice: AccessDevice

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    useHotline: bool

    contact: Optional[str] = None

    pathHeader: Optional[str] = None

    portNumber: Optional[int] = None

    hotlineContact: Optional[str] = None


@dataclass
class AccessDeviceEndpointKey(OCIType):
    """Access device end point in the context of a modify or delete command."""

    accessDevice: AccessDevice

    linePort: str


@dataclass
class ProfileAndServiceDeviceEndpointInfo(OCIType):
    """Represents information about an endpoint device"""

    accessDevice: AccessDevice

    linePort: str

    privateIdentity: Optional[str] = None

    accessDeviceMacAddress: Optional[str] = None


@dataclass
class AccessDeviceEndpointAdd(OCIType):
    """Access device end point used in the context of add.
    Port numbers are only used by devices with static line ordering.
    The following element is only used in AS data mode and ignored in XS data mode:
      pathHeader"""

    accessDevice: AccessDevice

    linePort: str

    contact: Optional[str] = None

    pathHeader: Optional[str] = None

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceMultipleIdentityEndpointWithType(OCIType):
    """Access device end point that can have multiple contacts.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Port numbers are only used by devices with static line ordering."""

    accessDevice: AccessDevice

    deviceType: str

    linePort: str

    privateIdentity: Optional[str] = None

    contact: Optional[str] = None

    portNumber: Optional[int] = None

    macAddress: Optional[str] = None


@dataclass
class AccessDeviceMultipleIdentityEndpointAdd(OCIType):
    """Access device end point used in the context of add.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity"""

    accessDevice: AccessDevice

    linePort: str

    privateIdentity: Optional[str] = None

    contact: Optional[str] = None

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceEndpointWithPortNumberRead22(OCIType):
    """Access device end point.
    Port numbers are only used by devices with static line ordering.
    The following element is only used in AS data mode and ignored in XS data mode:
      pathHeader"""

    accessDevice: AccessDevice

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    contact: Optional[str] = None

    pathHeader: Optional[str] = None

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceMultipleIdentityEndpointKey(OCIType):
    """Access device end point in the context of a modify or delete command.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity"""

    accessDevice: AccessDevice

    linePort: str

    privateIdentity: Optional[str] = None


@dataclass
class AccessDeviceEndpointAndHotlineAdd(OCIType):
    """Access device end point used in the context of add.
    Port numbers are only used by devices with static line ordering.
    The following element is only used in AS data mode and ignored in XS data mode:
      pathHeader
      useHotline, use value false in XS data mode
      hotlineContact

    The following element is only used in XS data mode and ignored in AS data mode:
      privateIdentity"""

    accessDevice: AccessDevice

    linePort: str

    useHotline: bool

    privateIdentity: Optional[str] = None

    contact: Optional[str] = None

    pathHeader: Optional[str] = None

    portNumber: Optional[int] = None

    hotlineContact: Optional[str] = None


@dataclass
class TreeDeviceInfo(OCIType):
    """Information related to a tree device.
    A tree device is a device associated with a device type that has the option
    supportLinks set to \"Support Links from Devices\"..  Many leaf devices can link to it.
    When a tree device is created, it is assigned a system-wide unique linkId."""

    treeDeviceKey: AccessDeviceKey

    linkId: str


@dataclass
class ReplacementAlternateUserIdEntryList(OCIType):
    """A list of alternate user ids that that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    alternateUserId: List[AlternateUserIdEntry] = field(default_factory=list)


@dataclass
class ExtendedMediaFileResource20(OCIType):
    """Represents either an existing file for the application server to use, or
    the contents of a file to transfer and an URL."""

    file: Optional[AnnouncementFileKey] = None

    url: Optional[str] = None


@dataclass
class AutoAttendantKeyConfigurationModifyEntry20(OCIType):
    """The modify configuration entry of a key for Auto Attendant.
    The following data elements are only used in AS data mode:
      audioFile
      videoFile
      submenuId
    The following data elements are only valid for Standard Auto
    Attendants:
      submenuId"""

    action: str

    description: Optional[str] = None

    phoneNumber: Optional[str] = None

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    submenuId: Optional[str] = None


@dataclass
class AutoAttendantKeyConfigurationReadEntry20(OCIType):
    """The read configuration entry of a key for Auto Attendant.
    The following data elements are only used in AS data mode:
      submenuId
    The following data elements are only valid for Standard Auto
    Attendants:
      submenuId"""

    action: str

    description: Optional[str] = None

    phoneNumber: Optional[str] = None

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    submenuId: Optional[str] = None


@dataclass
class AutoAttendantKeyConfigurationEntry20(OCIType):
    """The configuration entry of a key for Auto Attendant.
    The following data elements are only used in AS data mode:
      audioFile
      videoFile
      submenuId
    The following data elements are only valid for Standard Auto
    Attendants:
      submenuId"""

    action: str

    description: Optional[str] = None

    phoneNumber: Optional[str] = None

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    submenuId: Optional[str] = None


@dataclass
class VoiceMessagingAlternateNoAnswerGreetingRead20(OCIType):
    """The configuration of a alternate no answer greeting.
    It is used when geting a user's voice messaging greeting."""

    name: str

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None


@dataclass
class CallCenterAnnouncementFileListRead20(OCIType):
    """Contains a list of announcement repository files"""

    file1: Optional[AnnouncementFileLevelKey] = None

    file2: Optional[AnnouncementFileLevelKey] = None

    file3: Optional[AnnouncementFileLevelKey] = None

    file4: Optional[AnnouncementFileLevelKey] = None


@dataclass
class VoiceMessagingAlternateNoAnswerGreetingModify20(OCIType):
    """The configuration of a alternate no answer greeting.
    It is used when modifying a user's voice messaging greeting."""

    name: Optional[str] = None

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None


@dataclass
class CallCenterAnnouncementFileListModify20(OCIType):
    """Contains a list of announcement repository files"""

    file1: Optional[AnnouncementFileLevelKey] = None

    file2: Optional[AnnouncementFileLevelKey] = None

    file3: Optional[AnnouncementFileLevelKey] = None

    file4: Optional[AnnouncementFileLevelKey] = None


@dataclass
class ExtendedMediaFileLevelResource20(OCIType):
    """Represents either an existing file for the application server to use, or
    the contents of a file to transfer and an URL."""

    file: Optional[AnnouncementFileLevelKey] = None

    url: Optional[str] = None


@dataclass
class AutoAttendantKeyReadConfiguration19(OCIType):
    """The read configuration of a key for Auto
    Attendant."""

    key: str

    entry: AutoAttendantKeyConfigurationReadEntry19


@dataclass
class ReplacementCallToNumberList(OCIType):
    """A list of Call to Numbers that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list.
    For the callToNumbers, the extension element is not used and the number element is only used when the type is BroadWorks Mobility."""

    callToNumber: List[CallToNumber] = field(default_factory=list)


@dataclass
class ReplacementCommunicationBarringCallMeNowRuleList(OCIType):
    """A list of Communication Barring CallMeNow Rules that replaces a
    previously configured list. By convention, an element of this type
    may be set nill to clear the list."""

    rule: List[CommunicationBarringCallMeNowRule] = field(default_factory=list)


@dataclass
class ReplacementCommunicationBarringIncomingRuleList19sp1(OCIType):
    """A list of Communication Barring Incoming Rules that replaces a
    previously configured list. By convention, an element of this type
    may be set nill to clear the list."""

    rule: List[CommunicationBarringIncomingRule19sp1] = field(default_factory=list)


@dataclass
class ReplacementCommunicationBarringOriginatingRuleList(OCIType):
    """A list of Communication Barring Originating Rules that replaces a
    previously configured list. By convention, an element of this type
    may be set nill to clear the list."""

    rule: List[CommunicationBarringOriginatingRule] = field(default_factory=list)


@dataclass
class ReplacementCommunicationBarringRedirectingRuleList(OCIType):
    """A list of Communication Barring Redirecting Rules that replaces a
    previously configured list. By convention, an element of this type
    may be set nill to clear the list."""

    rule: List[CommunicationBarringRedirectingRule] = field(default_factory=list)


@dataclass
class CriteriaFromDnModify(OCIType):
    """The from dn criteria used within a modify request."""

    fromDnCriteriaSelection: Optional[str] = None

    includeAnonymousCallers: Optional[bool] = None

    includeUnavailableCallers: Optional[bool] = None

    phoneNumberList: Optional[CriteriaReplacementDNList] = None


@dataclass
class CriteriaFromDnModify23(OCIType):
    """The from dn criteria added with the option for selecting internal and external callers, used within a modify request."""

    fromDnCriteriaSelection: Optional[str] = None

    includeAnonymousCallers: Optional[bool] = None

    includeUnavailableCallers: Optional[bool] = None

    includeInternalCallers: Optional[bool] = None

    includeExternalCallers: Optional[bool] = None

    phoneNumberList: Optional[CriteriaReplacementDNList] = None


@dataclass
class PriorityAlertCriteriaFromDnModify(OCIType):
    """The from dn criteria used within a modify request."""

    fromDnCriteriaSelection: Optional[str] = None

    includeAnonymousCallers: Optional[bool] = None

    includeUnavailableCallers: Optional[bool] = None

    phoneNumberList: Optional[CriteriaReplacementDNList] = None


@dataclass
class ExecutiveCallFilteringCriteriaFromDnModify(OCIType):
    """The from dn criteria used within an executive call filtering criteria modify request."""

    fromDnCriteriaSelection: Optional[str] = None

    includeAnonymousCallers: Optional[bool] = None

    includeUnavailableCallers: Optional[bool] = None

    phoneNumberList: Optional[CriteriaReplacementDNList] = None


@dataclass
class CallMeNowToDnCriteriaModify(OCIType):
    """The To dn criteria used on the call me now external number to be modified."""

    toDnCriteriaSelection: Optional[str] = None

    phoneNumberList: Optional[CriteriaReplacementDNList] = None


@dataclass
class SelectiveCallRejectionCriteriaCallTypeModify(OCIType):
    """The call type criteria used within a modify request."""

    fromDnCriteriaSelection: Optional[str] = None

    includeAnonymousCallers: Optional[bool] = None

    includeUnavailableCallers: Optional[bool] = None

    phoneNumberList: Optional[CriteriaReplacementDNList] = None


@dataclass
class ServiceInstanceAddProfile(OCIType):
    """Service Profile Information for group service."""

    name: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    alias: List[str] = field(default_factory=list)

    publicUserIdentity: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class ServiceInstanceAddProfileFlexibleSeatingHost(OCIType):
    """Service Profile Information for a flexible seating host."""

    name: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class ServiceInstanceReadProfile19sp1(OCIType):
    """Service Profile Information for group service.

    The callingLineIdPhoneNumber is no longer being formatted for display purpose. The value is returned exactly the same as being stored."""

    name: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    countryCode: Optional[str] = None

    nationalPrefix: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    timeZoneDisplayName: Optional[str] = None

    alias: List[str] = field(default_factory=list)

    publicUserIdentity: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class TrunkGroupMultipleContactPilotUser(OCIType):
    """Trunk Group pilot user information used when adding a Trunk Group."""

    userId: str

    lastName: str

    firstName: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    linePort: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    contact: List[str] = field(default_factory=list)

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class TrunkGroupPilotUser(OCIType):
    """Trunk Group pilot user information used when adding a Trunk Group."""

    userId: str

    lastName: str

    firstName: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    linePort: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    contact: Optional[str] = None


@dataclass
class ServiceInstanceReadProfile17(OCIType):
    """Service Profile Information for group service.
    It is identical to the ServiceInstanceAddProfile, but without the password.

    Replaced by: ServiceInstanceReadProfile17sp4"""

    name: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    timeZoneDisplayName: Optional[str] = None

    alias: List[str] = field(default_factory=list)

    publicUserIdentity: Optional[str] = None


@dataclass
class CombinedServiceInstanceAddProfile(OCIType):
    """Service Profile Information for group service.

    When name, callingLineIdLastName and callingLineIdFirstName are not included, the values
    in the corresponding service instance template (if this is used to add a Hunt Group, for
    example, the name will come from the Hunt Group template) will be used. Otherwise, the
    request will fail.

    If the phoneNumber has not been assigned to the group, it will be added to group and
    service provider if needed."""

    name: Optional[str] = None

    callingLineIdLastName: Optional[str] = None

    callingLineIdFirstName: Optional[str] = None

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    alias: List[str] = field(default_factory=list)

    publicUserIdentity: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class ServiceInstanceModifyProfileFlexibleSeatingHost(OCIType):
    """Service Profile Information for a flexible seating host"""

    name: Optional[str] = None

    callingLineIdLastName: Optional[str] = None

    callingLineIdFirstName: Optional[str] = None

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class ServiceInstanceReadProfile17sp4(OCIType):
    """Service Profile Information for group service.

    Replaced by: ServiceInstanceReadProfile19sp1"""

    name: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    countryCode: Optional[str] = None

    nationalPrefix: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    timeZoneDisplayName: Optional[str] = None

    alias: List[str] = field(default_factory=list)

    publicUserIdentity: Optional[str] = None


@dataclass
class GroupDepartmentKey(DepartmentKey):
    """Uniquely identifies a department defined within a group.
    To uniquely identify a group department, we must know the department name and which
    group contains the department."""

    serviceProviderId: str

    groupId: str

    name: str


@dataclass
class EnterpriseDepartmentKey(DepartmentKey):
    """Uniquely identifies a department defined within an enterprise.
    To uniquely identify an enterprise department, we must know the department name and which
    enterprise contains the department."""

    serviceProviderId: str

    name: str


@dataclass
class CPEDeviceOptionsRead22V2(OCIType):
    """CPE device's options."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptionsRead22V2
    ] = None


@dataclass
class CPEDeviceOptionsRead22V3(OCIType):
    """CPE device's options."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptionsRead22V3
    ] = None


@dataclass
class CPEDeviceOptionsRead22V4(OCIType):
    """CPE device's options."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptionsRead22V4
    ] = None


@dataclass
class CPEDeviceOptionsRead22V5(OCIType):
    """CPE device's options."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptionsRead22V5
    ] = None


@dataclass
class CPEDeviceOptionsRead22V6(OCIType):
    """CPE device's options."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptionsRead22V6
    ] = None


@dataclass
class ConsolidatedAccessDeviceMultipleIdentityEndpointAndContactAdd22(OCIType):
    """Access device end point used in the context of add.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    In XS data mode, only one contact can be defined.
    Only Static Registration capable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.

    In the case an access device referenced by accessDevice does not exist, the device will be added.

    The device attributes deviceType, protocol, netAddress, port, outboundProxyServerNetAddress,
    stunServerNetAddress, macAddress, serialNumber, description, physicalLocation, transportProtocol,
    useCustomUserNamePassword and accessDeviceCredentials will be ignored if the access device already
    exists.

    The following elements are only used in AS data mode and ignored in XS data mode:
      useHotline, use value false in XS data mode
      hotlineContact"""

    accessDevice: AccessDevice

    linePort: str

    useHotline: bool

    privateIdentity: Optional[str] = None

    contact: List[str] = field(default_factory=list)

    portNumber: Optional[int] = None

    deviceType: Optional[str] = None

    protocol: Optional[str] = None

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

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    hotlineContact: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeModifyOptions22V3(OCIType):
    """Device Management System device type options during a modify request.

    The following data elements are only used in AS data mode and ignored in XS data mode:
      enableDeviceActivation
      deviceModel
      autoLinkingDeviceType
      autoCreateDevicesLevel
      isActivationCodeThroughMessagingServer
      bearerFileAuthentication"""

    deviceAccessProtocol: Optional[str] = None

    tagMode: Optional[str] = None

    tagSet: Optional[str] = None

    allowDeviceProfileCustomTagSet: Optional[bool] = None

    allowGroupCustomTagSet: Optional[bool] = None

    allowSpCustomTagSet: Optional[bool] = None

    sendEmailUponResetFailure: Optional[bool] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    useHttpDigestAuthentication: Optional[bool] = None

    macBasedFileAuthentication: Optional[bool] = None

    userNamePasswordFileAuthentication: Optional[bool] = None

    macInNonRequestURI: Optional[bool] = None

    macInCert: Optional[bool] = None

    macFormatInNonRequestURI: Optional[str] = None

    enableDeviceActivation: Optional[bool] = None

    deviceModel: Optional[str] = None

    autoLinkingDeviceType: Optional[str] = None

    autoCreateDevicesLevel: Optional[str] = None

    isActivationCodeThroughMessagingServer: Optional[bool] = None

    bearerFileAuthentication: Optional[bool] = None


@dataclass
class ConsolidatedSharedCallAppearanceAccessDeviceMultipleIdentityEndpointAdd22(
    OCIType
):
    """Access device end point for Shared Call Appearance Service used in the context of add.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Port numbers are only used by devices with static line ordering.

    In the case an access device referenced by accessDevice does not exist, the device will be added.

    The device attributes deviceType, protocol, netAddress, port, outboundProxyServerNetAddress,
    stunServerNetAddress, macAddress, serialNumber, description, physicalLocation, transportProtocol,
    useCustomUserNamePassword and accessDeviceCredentials will be ignored if the access device already
    exists.

    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity

    The following elements are only used in AS data mode and ignored in XS data mode:
      useHotline, use value false in XS data mode
      hotlineContact"""

    accessDevice: AccessDevice

    linePort: str

    isActive: bool

    allowOrigination: bool

    allowTermination: bool

    useHotline: bool

    privateIdentity: Optional[str] = None

    contact: Optional[str] = None

    portNumber: Optional[int] = None

    deviceType: Optional[str] = None

    protocol: Optional[str] = None

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

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    hotlineContact: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeOptions22V4(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI

    The following data elements are only used in AS data mode and ignored in XS data mode:
          enableDeviceActivation
          deviceModel
          supportLinks"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    enableDeviceActivation: bool

    supportLinks: str

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    macFormatInNonRequestURI: Optional[str] = None

    deviceModel: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeOptions22V6(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files except bearerFileAuthentication which is not supported.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI
          bearerFileAuthentication

    The following data elements are only used in AS data mode and ignored in XS data mode:
          enableDeviceActivation
          deviceModel
          supportLinks
          autoLinkingDeviceType
          autoCreateDevicesLevel
          isActivationCodeThroughMessagingServer
          bearerFileAuthentication"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    enableDeviceActivation: bool

    supportLinks: str

    bearerFileAuthentication: bool

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    macFormatInNonRequestURI: Optional[str] = None

    deviceModel: Optional[str] = None

    autoLinkingDeviceType: Optional[str] = None

    autoCreateDevicesLevel: Optional[str] = None

    isActivationCodeThroughMessagingServer: Optional[bool] = None


@dataclass
class DeviceManagementDeviceTypeOptions22V3(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI

    The following data elements are only used in AS data mode and ignored in XS data mode:
          enableDeviceActivation
          deviceModel"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    enableDeviceActivation: bool

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    macFormatInNonRequestURI: Optional[str] = None

    deviceModel: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeModifyOptions22V2(OCIType):
    """Device Management System device type options during a modify request.

    The following data elements are only used in AS data mode and ignored in XS data mode:
      enableDeviceActivation
      deviceModel
      autoLinkingDeviceType
      autoCreateDevicesLevel"""

    deviceAccessProtocol: Optional[str] = None

    tagMode: Optional[str] = None

    tagSet: Optional[str] = None

    allowDeviceProfileCustomTagSet: Optional[bool] = None

    allowGroupCustomTagSet: Optional[bool] = None

    allowSpCustomTagSet: Optional[bool] = None

    sendEmailUponResetFailure: Optional[bool] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    useHttpDigestAuthentication: Optional[bool] = None

    macBasedFileAuthentication: Optional[bool] = None

    userNamePasswordFileAuthentication: Optional[bool] = None

    macInNonRequestURI: Optional[bool] = None

    macInCert: Optional[bool] = None

    macFormatInNonRequestURI: Optional[str] = None

    enableDeviceActivation: Optional[bool] = None

    deviceModel: Optional[str] = None

    autoLinkingDeviceType: Optional[str] = None

    autoCreateDevicesLevel: Optional[str] = None


@dataclass
class DeviceManagementDeviceTypeOptions22V5(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI

    The following data elements are only used in AS data mode and ignored in XS data mode:
          enableDeviceActivation
          deviceModel
          supportLinks
          autoLinkingDeviceType
          autoCreateDevicesLevel"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    enableDeviceActivation: bool

    supportLinks: str

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    macFormatInNonRequestURI: Optional[str] = None

    deviceModel: Optional[str] = None

    autoLinkingDeviceType: Optional[str] = None

    autoCreateDevicesLevel: Optional[str] = None


@dataclass
class CombinedAccessDeviceMultipleIdentityEndpointAdd(OCIType):
    """Access device end point used in the context of add.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Only Static Registration capable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.

    In the case an access device referenced by accessDevice does not exist, the device will be added.

    The device attributes deviceType, protocol, netAddress, port, outboundProxyServerNetAddress,
    stunServerNetAddress, macAddress, serialNumber, description, physicalLocation, transportProtocol,
    useCustomUserNamePassword and accessDeviceCredentials will be ignored if the access device already
    exists."""

    accessDevice: AccessDevice

    linePort: str

    privateIdentity: Optional[str] = None

    contact: Optional[str] = None

    portNumber: Optional[int] = None

    deviceType: Optional[str] = None

    protocol: Optional[str] = None

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

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None


@dataclass
class DeviceManagementDeviceTypeOptions22V2(OCIType):
    """Device Management System device type options.

    Note: For the elements listed below, when device configuration is set to deviceManagement, those elements apply to the creation of the Polycom Phone Services directory file only.
          For all other files, they are not used. Those elements are instead configured on a per-file basis at the Device Type File level.
          When device configuration is set to legacy, those elements apply to all configuration files.

          useHttpDigestAuthentication
          macBasedFileAuthentication
          userNamePasswordFileAuthentication
          macInNonRequestURI
          macInCert
          macFormatInNonRequestURI"""

    deviceAccessProtocol: str

    tagMode: str

    allowDeviceProfileCustomTagSet: bool

    allowGroupCustomTagSet: bool

    allowSpCustomTagSet: bool

    sendEmailUponResetFailure: bool

    useHttpDigestAuthentication: bool

    macBasedFileAuthentication: bool

    userNamePasswordFileAuthentication: bool

    macInNonRequestURI: bool

    macInCert: bool

    tagSet: Optional[str] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    deviceAccessURI: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    macFormatInNonRequestURI: Optional[str] = None


@dataclass
class ConsolidatedAccessDeviceMultipleIdentityEndpointAndContactAdd(OCIType):
    """Access device end point used in the context of add.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    In XS data mode, only one contact can be defined.
    Only Static Registration capable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.

    In the case an access device referenced by accessDevice does not exist, the device will be added.

    The device attributes deviceType, protocol, netAddress, port, outboundProxyServerNetAddress,
    stunServerNetAddress, macAddress, serialNumber, description, physicalLocation, transportProtocol,
    useCustomUserNamePassword and accessDeviceCredentials will be ignored if the access device already
    exists."""

    accessDevice: AccessDevice

    linePort: str

    privateIdentity: Optional[str] = None

    contact: List[str] = field(default_factory=list)

    portNumber: Optional[int] = None

    deviceType: Optional[str] = None

    protocol: Optional[str] = None

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

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None


@dataclass
class ConsolidatedSharedCallAppearanceAccessDeviceMultipleIdentityEndpoint(OCIType):
    """Access device end point for Shared Call Appearance Service used in the context of add.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Port numbers are only used by devices with static line ordering.

    In the case an access device referenced by accessDevice does not exist, the device will be added.

    The device attributes deviceType, protocol, netAddress, port, outboundProxyServerNetAddress,
    stunServerNetAddress, macAddress, serialNumber, description, physicalLocation, transportProtocol,
    useCustomUserNamePassword and accessDeviceCredentials will be ignored if the access device already
    exists.

    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity"""

    accessDevice: AccessDevice

    linePort: str

    isActive: bool

    allowOrigination: bool

    allowTermination: bool

    privateIdentity: Optional[str] = None

    contact: Optional[str] = None

    portNumber: Optional[int] = None

    deviceType: Optional[str] = None

    protocol: Optional[str] = None

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

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    useHotline: Optional[bool] = None

    hotlineContact: Optional[str] = None


@dataclass
class CombinedAccessDeviceMultipleIdentityEndpointModify(OCIType):
    """Access device end point used in the context of modify.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Only Static Registration capable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.

    In the case an access device referenced by accessDevice does not exist, the device will be added.
    When the device needs to be added, if the linePort is not specified, the request will fail

    The device attributes deviceType, protocol, netAddress, port, outboundProxyServerNetAddress,
    stunServerNetAddress, macAddress, serialNumber, description, physicalLocation, transportProtocol,
    useCustomUserNamePassword and accessDeviceCredentials will be ignored if the access device already
    exists."""

    accessDevice: Optional[AccessDevice] = None

    linePort: Optional[str] = None

    privateIdentity: Optional[str] = None

    contact: Optional[str] = None

    portNumber: Optional[int] = None

    deviceType: Optional[str] = None

    protocol: Optional[str] = None

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

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None


@dataclass
class DeviceManagementDeviceTypeModifyOptions22(OCIType):
    """Device Management System device type options during a modify request.

    The following data elements are only used in AS data mode and ignored in XS data mode:
      enableDeviceActivation
      deviceModel"""

    deviceAccessProtocol: Optional[str] = None

    tagMode: Optional[str] = None

    tagSet: Optional[str] = None

    allowDeviceProfileCustomTagSet: Optional[bool] = None

    allowGroupCustomTagSet: Optional[bool] = None

    allowSpCustomTagSet: Optional[bool] = None

    sendEmailUponResetFailure: Optional[bool] = None

    deviceAccessNetAddress: Optional[str] = None

    deviceAccessPort: Optional[int] = None

    deviceAccessContext: Optional[str] = None

    defaultDeviceLanguage: Optional[str] = None

    defaultDeviceEncoding: Optional[str] = None

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    useHttpDigestAuthentication: Optional[bool] = None

    macBasedFileAuthentication: Optional[bool] = None

    userNamePasswordFileAuthentication: Optional[bool] = None

    macInNonRequestURI: Optional[bool] = None

    macInCert: Optional[bool] = None

    macFormatInNonRequestURI: Optional[str] = None

    enableDeviceActivation: Optional[bool] = None

    deviceModel: Optional[str] = None


@dataclass
class CombinedSharedCallAppearanceAccessDeviceMultipleIdentityEndpoint(OCIType):
    """Access device end point for Shared Call Appearance Service used in the context of add.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Port numbers are only used by devices with static line ordering.

    In the case an access device referenced by accessDevice does not exist, the device will be added.

    When elements for isActive, allowOrigination, allowTermination and allowVideo are not included in the request,
    the values for them will come for the Shared Call Appearance endpoints template. If the template
    does not exist, the request using this data type will fail.

    The device attributes deviceType, protocol, netAddress, port, outboundProxyServerNetAddress,
    stunServerNetAddress, macAddress, serialNumber, description, physicalLocation, transportProtocol,
    useCustomUserNamePassword and accessDeviceCredentials will be ignored if the access device already
    exists."""

    accessDevice: AccessDevice

    linePort: str

    privateIdentity: Optional[str] = None

    contact: Optional[str] = None

    portNumber: Optional[int] = None

    isActive: Optional[bool] = None

    allowOrigination: Optional[bool] = None

    allowTermination: Optional[bool] = None

    allowVideo: Optional[bool] = None

    deviceType: Optional[str] = None

    protocol: Optional[str] = None

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

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None


@dataclass
class EnterpriseTrunkNumberRange(OCIType):
    """Directory number range. The minimum and maximum values are inclusive."""

    dnRange: DNRange

    extensionLength: Optional[int] = None


@dataclass
class VirtualOnNetUserRange(OCIType):
    """Virtual On-Net User Range."""

    dnRange: DNRange

    extensionRange: ExtensionRange17

    firstName: str

    lastName: str

    callingLineIdFirstName: str

    callingLineIdLastName: str

    virtualOnNetCallTypeName: str


@dataclass
class EnterpriseTrunkNumberPrefixModify(OCIType):
    """Enterprise Trunk Number Prefix for modify."""

    numberPrefix: str

    extensionRange: Optional[ExtensionRange17] = None


@dataclass
class EnterpriseTrunkNumberPrefix22(OCIType):
    """Enterprise Trunk Number Prefix"""

    numberPrefix: str

    extensionRange: Optional[ExtensionRange17] = None


@dataclass
class CallCenterReportIntervalDates(OCIType):
    """The call center enhanced reporting report interval, using dates."""

    startDate: int

    startTime: HourMinute

    endDate: int

    endTime: HourMinute


@dataclass
class CallCenterReportScheduleTime(OCIType):
    """A scheduled time for call center enhanced reporting scheduled report."""

    timeZone: str

    scheduleDate: int

    scheduleTime: HourMinute


@dataclass
class ReplacementAgentWeightList(OCIType):
    """A list of agent userIds and hunt agent weights that replaces the previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    agentWeight: List[HuntAgentWeight] = field(default_factory=list)


@dataclass
class AutoAttendantModifyMenuExecutionServer(OCIType):
    """The configuration of an auto attendant menu greeting prompt.
    Engineering Note: This command can only be executed from the Execution Server"""

    announcementSelection: Optional[str] = None

    audioFile: Optional[LabeledFileNameResource] = None

    videoFile: Optional[LabeledFileNameResource] = None


@dataclass
class ExtendedFileResource(OCIType):
    """Represents either an existing file for the application server to use, or
    the contents of a file to transfer and an URL."""

    file: Optional[LabeledFileResource] = None

    url: Optional[str] = None


@dataclass
class VoiceMessagingAlternateNoAnswerGreetingModify16(OCIType):
    """The configuration of a alternate no answer
    greeting.
    It is used when modifying a user's voice
    messaging
    greeting."""

    name: Optional[str] = None

    audioFile: Optional[LabeledMediaFileResource] = None

    videoFile: Optional[LabeledMediaFileResource] = None


@dataclass
class AutoAttendantKeyConfigurationEntry19(OCIType):
    """The configuration entry of a key for Auto
    Attendant.
    The following data elements are only valid for Standard Auto
    Attendants:
    submenuId"""

    action: str

    description: Optional[str] = None

    phoneNumber: Optional[str] = None

    audioFile: Optional[LabeledMediaFileResource] = None

    videoFile: Optional[LabeledMediaFileResource] = None

    submenuId: Optional[str] = None


@dataclass
class CallCenterAnnouncementFileListModify(OCIType):
    """Contains a list of audio or video files to modify."""

    file1: Optional[LabeledMediaFileResource] = None

    file2: Optional[LabeledMediaFileResource] = None

    file3: Optional[LabeledMediaFileResource] = None

    file4: Optional[LabeledMediaFileResource] = None


@dataclass
class AutoAttendantKeyConfigurationModifyEntry(OCIType):
    """The modify configuration entry of a key for Auto
    Attendant.
    The following data elements are only valid for Standard Auto
    Attendants:
    submenuId"""

    action: str

    description: Optional[str] = None

    phoneNumber: Optional[str] = None

    audioFile: Optional[LabeledMediaFileResource] = None

    videoFile: Optional[LabeledMediaFileResource] = None

    submenuId: Optional[str] = None


@dataclass
class GroupCallQueueAnnouncementFileListModify(OCIType):
    """Contains a list of audio files to modify."""

    file1: Optional[LabeledMediaFileResource] = None

    file2: Optional[LabeledMediaFileResource] = None

    file3: Optional[LabeledMediaFileResource] = None

    file4: Optional[LabeledMediaFileResource] = None


@dataclass
class ExtendedMediaFileResource(OCIType):
    """Represents either an existing file for the application server to use, or
    the contents of a file to transfer and an URL."""

    file: Optional[LabeledMediaFileResource] = None

    url: Optional[str] = None


@dataclass
class GroupCallQueueMusicOnHoldSourceModify(OCIType):
    """Contains the Group Call Queue music on hold source configuration."""

    audioMessageSourceSelection: Optional[str] = None

    audioFile: Optional[LabeledMediaFileResource] = None


@dataclass
class ProfileAndServiceMusicOnHoldInfo(OCIType):
    """This is the configuration parameters for Music On Hold service"""

    enableVideo: bool

    source: MusicOnHoldUserSourceRead16

    useAlternateSourceForInternalCalls: bool

    internalSource: Optional[MusicOnHoldUserSourceRead16] = None


@dataclass
class MWIDeliveryToMobileEndpointTemplateBody(OCIType):
    """MWI Delivery To Mobile Endpoint template body."""

    line: List[MWIDeliveryToMobileEndpointTemplateLine] = field(default_factory=list)


@dataclass
class ShInterfaceUserListEntry21sp1(OCIType):
    """ShInterface User List Entry."""

    userId: str

    userType: str

    publicUserIdentity: PublicUserIdentity

    endpointType: str

    IMSUserState: str

    SCSCFName: Optional[str] = None


@dataclass
class ShInterfaceUserListEntry(OCIType):
    """ShInterface User List Entry."""

    userId: str

    userType: str

    publicUserIdentity: PublicUserIdentity

    endpointType: str

    IMSUserState: str

    SCSCFName: Optional[str] = None


@dataclass
class ShInterfaceUserIdDataEntry(OCIType):
    """ShInterface User Id Data Entry."""

    userType: str

    publicUserIdentity: PublicUserIdentity

    endpointType: str

    IMSUserState: str

    SCSCFName: Optional[str] = None


@dataclass
class ShInterfaceUserIdDataEntry21sp1(OCIType):
    """ShInterface User Id Data Entry."""

    userType: str

    publicUserIdentity: PublicUserIdentity

    endpointType: str

    IMSUserState: str

    SCSCFName: Optional[str] = None


@dataclass
class PushNotificationTokenData23(OCIType):
    """The common push notification token elements."""

    pushNotificationToken: str

    pushNotificationType: str

    pushNotificationEventData: List[PushNotificationEventData23] = field(
        default_factory=list
    )


@dataclass
class ScheduleEvents(OCIType):
    """Retrives all Holiday or Time Event details for a given schedulel Level."""

    eventname: str

    startDate: int

    allDayEvent: bool

    startTime: HourMinute

    endTime: HourMinute

    endDate: int

    recurrence: Optional[Recurrence] = None


@dataclass
class CallCenterReportScheduleRecurrence(OCIType):
    """A recurring schedule for call center enhanced reporting scheduled report."""

    timeZone: str

    startDate: int

    scheduleTime: HourMinute

    recurrence: Recurrence


@dataclass
class TrunkGroupDeviceMultipleContactEndpointModify(OCIType):
    """Trunk group device endpoint used in the context of modify that can have multiple contacts."""

    name: Optional[str] = None

    linePort: Optional[str] = None

    contactList: Optional[ReplacementContactList] = None


@dataclass
class ConsolidatedAccessDeviceMultipleIdentityEndpointAndContactModify(OCIType):
    """Access device end point used in the context of modify. .
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Only Static Registration capable devices may have more than one contact defined.
    Only the first contact in contactList is used in XS data mode.
    Port numbers are only used by devices with static line ordering.

    In the case an access device referenced by accessDevice does not exist, the device will be added.
    When the device needs to be added, if the linePort is not specified, the request will fail

    If the deviceType is included in the request a new device will be created using the type unless a
    device with the same name already exists.

    The device attributes protocol, netAddress, port, outboundProxyServerNetAddress,
    stunServerNetAddress, macAddress, serialNumber, description, physicalLocation, transportProtocol,
    useCustomUserNamePassword and accessDeviceCredentials will be ignored if the access device already
    exists.

    The following elements are only used in AS data mode and ignored in XS data mode:
      useHotline
      hotlineContact"""

    accessDevice: Optional[AccessDevice] = None

    linePort: Optional[str] = None

    privateIdentity: Optional[str] = None

    contactList: Optional[ReplacementContactList] = None

    portNumber: Optional[int] = None

    deviceType: Optional[str] = None

    protocol: Optional[str] = None

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

    accessDeviceCredentials: Optional[DeviceManagementUserNamePassword16] = None

    useHotline: Optional[bool] = None

    hotlineContact: Optional[str] = None


@dataclass
class AccessDeviceMultipleContactEndpointModify(OCIType):
    """Access device end point used in the context of modify that can have more than one contact defined.
    Only Static Registration capable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering."""

    accessDevice: Optional[AccessDevice] = None

    linePort: Optional[str] = None

    contactList: Optional[ReplacementContactList] = None

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceMultipleIdentityAndContactEndpointModify(OCIType):
    """Access device end point used in the context of modify that can have more than one contact defined.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Only Static Registration capabable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity"""

    accessDevice: Optional[AccessDevice] = None

    linePort: Optional[str] = None

    privateIdentity: Optional[str] = None

    contactList: Optional[ReplacementContactList] = None

    portNumber: Optional[int] = None


@dataclass
class VoiceMessagingDistributionListModify(OCIType):
    """A list of voice mail distribution lists
    It is used when setting a user's voice messaging distribution lists"""

    listId: int

    description: Optional[str] = None

    phoneNumberList: Optional[ReplacementOutgoingDNorSIPURIList] = None


@dataclass
class ServiceInstanceModifyProfile(OCIType):
    """Service Profile Information for group service used when modifying an existing service instance."""

    name: Optional[str] = None

    callingLineIdLastName: Optional[str] = None

    callingLineIdFirstName: Optional[str] = None

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    sipAliasList: Optional[ReplacementSIPAliasList] = None

    publicUserIdentity: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class CallCenterReplacementSkilledAgents(OCIType):
    """A list of agents grouped by skill levels."""

    skillLevel: int

    agents: ReplacementUserIdList


@dataclass
class ScheduleGlobalKey(OCIType):
    """Uniquely identifies Holiday and Time Schedules throughout all System, Service Provider, Group and User level."""

    scheduleKey: ScheduleKey

    scheduleLevel: str


@dataclass
class ServiceProviderReplacementCommunicationBarringHierarchicalCallMeNowRuleList(
    OCIType
):
    """A list of Service Provider Communication Barring Hierarchical Call Me Now Rules that replaces a previously configured list. By convention, an element of this type
    may be set nill to clear the list."""

    rule: List[ServiceProviderCommunicationBarringHierarchicalCallMeNowRule] = field(
        default_factory=list
    )


@dataclass
class ServiceProviderReplacementCommunicationBarringHierarchicalOriginatingRuleList(
    OCIType
):
    """A list of Service Provider Communication Barring Hierarchical Originating Rules that replaces a previously configured list. By convention, an element of this type
    may be set nill to clear the list."""

    rule: List[ServiceProviderCommunicationBarringHierarchicalOriginatingRule] = field(
        default_factory=list
    )


@dataclass
class ServiceProviderReplacementCommunicationBarringHierarchicalRedirectingRuleList(
    OCIType
):
    """A list of Service Provider Communication Barring Hierarchical Redirecting Rules that replaces a previously configured list. By convention, an element of this type
    may be set nill to clear the list."""

    rule: List[ServiceProviderCommunicationBarringHierarchicalRedirectingRule] = field(
        default_factory=list
    )


@dataclass
class SimultaneousRingReplacementNumberList(OCIType):
    """A list of Simultaneous Ring numbers that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    simultaneousRingNumber: List[SimultaneousRingNumber] = field(default_factory=list)


@dataclass
class AccessDeviceMultipleIdentityAndContactEndpointAdd22V2(OCIType):
    """Access device end point used in the context of add that can have more than one contact defined.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Only Static Registration capabable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity

    The following elements are only used in AS data mode and ignored in XS data mode:
      useHotline, use value false in XS data mode
      hotlineContact"""

    accessDevice: AccessDevice

    linePort: str

    useHotline: bool

    privateIdentity: Optional[str] = None

    contact: List[SIPContactInfo] = field(default_factory=list)

    portNumber: Optional[int] = None

    hotlineContact: Optional[str] = None


@dataclass
class AccessDeviceMultipleContactEndpointAdd22(OCIType):
    """Access device end point used in the context of add that can have more than one contact defined.
    Only Static Registration capabable devices may have more than one contact defined.
                Port numbers are only used by devices with static line ordering."""

    accessDevice: AccessDevice

    linePort: str

    contact: List[SIPContactInfo] = field(default_factory=list)

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceMultipleContactEndpointRead22(OCIType):
    """Access device end point that can have multiple contacts.
    Port numbers are only used by devices with static line ordering."""

    accessDevice: AccessDevice

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    supportVisualDeviceManagement: bool

    contact: List[SIPContactInfo] = field(default_factory=list)

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceMultipleIdentityAndContactEndpointRead22(OCIType):
    """Access device end point that can have multiple contacts.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
          Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and not returned in AS data mode:
      privateIdentity
    The following elements are only used in AS data mode and a value false is returned in the XS mode:
      supportVisualDeviceManagement"""

    accessDevice: AccessDevice

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    supportVisualDeviceManagement: bool

    privateIdentity: Optional[str] = None

    contact: List[SIPContactInfo] = field(default_factory=list)

    portNumber: Optional[int] = None


@dataclass
class ReplacementContactList22(OCIType):
    """A list of SIP contacts that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    contact: List[SIPContactInfo] = field(default_factory=list)


@dataclass
class TrunkGroupDeviceMultipleContactEndpointAdd22(OCIType):
    """Trunk group device endpoint used in the context of modify that can have multiple contacts."""

    name: str

    linePort: str

    contact: List[SIPContactInfo] = field(default_factory=list)


@dataclass
class TrunkGroupMultipleContactPilotUser22(OCIType):
    """Trunk Group pilot user information used when adding a Trunk Group."""

    userId: str

    lastName: str

    firstName: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    linePort: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    contact: List[SIPContactInfo] = field(default_factory=list)

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class AccessDeviceMultipleIdentityAndContactEndpointAdd22(OCIType):
    """Access device end point used in the context of add that can have more than one contact defined.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Only Static Registration capabable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity"""

    accessDevice: AccessDevice

    linePort: str

    privateIdentity: Optional[str] = None

    contact: List[SIPContactInfo] = field(default_factory=list)

    portNumber: Optional[int] = None


@dataclass
class AccessDeviceMultipleIdentityAndContactEndpointRead22V2(OCIType):
    """Access device end point that can have multiple contacts.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
      Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and not returned in AS data mode:
      privateIdentity
    The following elements are only used in AS data mode and a value false is returned in the XS mode:
      supportVisualDeviceManagement
      useHotline
    The following elements are only used in AS data mode and not returned in XS data mode:
      hotlineContact"""

    accessDevice: AccessDevice

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    supportVisualDeviceManagement: bool

    useHotline: bool

    privateIdentity: Optional[str] = None

    contact: List[SIPContactInfo] = field(default_factory=list)

    portNumber: Optional[int] = None

    hotlineContact: Optional[str] = None


@dataclass
class TrunkGroupDeviceMultipleContactEndpointRead22(OCIType):
    """Trunk group device endpoint that can have multiple contacts."""

    name: str

    linePort: str

    staticRegistrationCapable: bool

    useDomain: bool

    isPilotUser: bool

    contact: List[SIPContactInfo] = field(default_factory=list)


@dataclass
class ProfileAndServiceSpeedDial100Info(OCIType):
    """This is the configuration parameters for Speed Dial 100 service"""

    prefix: Optional[str] = None

    speedDialEntry: List[SpeedDial100Entry] = field(default_factory=list)


@dataclass
class ProfileAndServiceSpeedDial8Info(OCIType):
    """This is the configuration parameters for Speed Dial 8 service"""

    speedDialEntry: List[SpeedDial8Entry] = field(default_factory=list)


@dataclass
class TrunkAddressingAdd(OCIType):
    """Trunk group endpoint."""

    trunkGroupDeviceEndpoint: Optional[TrunkGroupDeviceEndpointAdd] = None

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None


@dataclass
class TrunkAddressingModify(OCIType):
    """Trunk group endpoint."""

    trunkGroupDeviceEndpoint: Optional[TrunkGroupDeviceEndpointModify] = None

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None


@dataclass
class TrunkAddressingRead(OCIType):
    """Trunk group endpoint."""

    trunkGroupDeviceEndpoint: Optional[TrunkGroupDeviceEndpointRead14sp4] = None

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None


@dataclass
class TrunkAddressingMultipleContactAdd(OCIType):
    """Trunk group endpoint that can have multiple contacts.
    alternateTrunkIdentityDomain is only used in XS mode and the AS when deployed in IMS mode.
    Both alternateTrunkIdentity and AlternateTrunkIdentityDomain should be set at the same time if one is set in XS mode.
    The following elements are only used in AS data mode and are ignored in XS data mode:
     physicalLocation"""

    trunkGroupDeviceEndpoint: Optional[TrunkGroupDeviceMultipleContactEndpointAdd] = (
        None
    )

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None

    alternateTrunkIdentityDomain: Optional[str] = None

    physicalLocation: Optional[str] = None


@dataclass
class TrunkAddressingMultipleContactRead21sp1(OCIType):
    """Trunk group endpoint that can have multiple contacts.
    alternateTrunkIdentityDomain is only used in XS mode and the AS when deployed in IMS mode.
    The following elements are only used in AS data mode and are ignored in XS data mode:
      physicalLocation"""

    trunkGroupDeviceEndpoint: Optional[TrunkGroupDeviceMultipleContactEndpointRead] = (
        None
    )

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None

    alternateTrunkIdentityDomain: Optional[str] = None

    physicalLocation: Optional[str] = None


@dataclass
class TrunkAddressingMultipleContactRead21(OCIType):
    """Trunk group endpoint that can have multiple contacts.
    alternateTrunkIdentityDomain is only used in XS mode and the AS when deployed in IMS mode.
    The following elements are only used in AS data mode and ignored in XS data mode:
      alternateTrunkIdentityDomain"""

    trunkGroupDeviceEndpoint: Optional[TrunkGroupDeviceMultipleContactEndpointRead] = (
        None
    )

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None

    alternateTrunkIdentityDomain: Optional[str] = None


@dataclass
class CombinedUserServiceAuthorization(OCIType):
    """Authorize a user service."""

    serviceName: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None


@dataclass
class CombinedServicePackAuthorization(OCIType):
    """Authorize a service pack."""

    servicePackName: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None


@dataclass
class CombinedUserServiceAssignment(OCIType):
    """Assign a service user. If the service has not been authorized to service provider or group, it will
    be authorized.

    If the service needs to be authorized at group/service provider levels, the authorizedQuantity
    will be used. Otherwise, it will be ignored. If the authorizedQuantity is not included, the
    quantity will come from the group template for the service. If a template does
    not exist, the service quantity will be set to unlimited."""

    userService: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None


@dataclass
class CombinedGroupServiceAuthorization(OCIType):
    """Authorize a group service."""

    serviceName: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None


@dataclass
class ConsolidatedUserServiceAssignment(OCIType):
    """Assign a user service. If the service has not been authorized to the group, it will be authorized.
    The authorizedQuantity will be used at the group level if provided; otherwise, the service quantity will be set to unlimited.
    The command will fail if the authorized quantity set at the service provider level is insufficient."""

    userServiceName: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None


@dataclass
class ServicePackAuthorization(OCIType):
    """Authorize (with quantity) or unauthorize a service pack."""

    servicePackName: str

    authorizedQuantity: UnboundedPositiveInt

    unauthorized: bool


@dataclass
class UserServiceAuthorization(OCIType):
    """Authorize (with quantity) or unauthorize a user service."""

    serviceName: str

    authorizedQuantity: UnboundedPositiveInt

    unauthorized: bool


@dataclass
class CombinedServicePackAssignment(OCIType):
    """Assign a service pack to user. If the service pack has not been authorized to service provider or
    group, it will be authorized.

    If the service pack needs to be authorized at group/service provider levels, the authorizedQuantity
    will be used. Otherwise, it will be ignored. If the authorizedQuantity is not included, the
    quantity will come from the group template for the service pack. If a template does
    not exist, the service quantity will be set to unlimited."""

    servicePackName: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None


@dataclass
class GroupServiceAuthorization(OCIType):
    """Authorize (with quantity) or unauthorize a group service."""

    serviceName: str

    authorizedQuantity: UnboundedPositiveInt

    unauthorized: bool


@dataclass
class ConsolidatedServicePackAssignment(OCIType):
    """Assign a service pack to user. If the service pack has not been authorized to
    the group, it will be authorized.
    The authorizedQuantity will be used at the group level if provided; otherwise, the service quantity will be set to unlimited.
    The command will fail if the authorized quantity set at the service provider level is insufficient."""

    servicePackName: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None


@dataclass
class ConsolidatedGroupServiceAssignment(OCIType):
    """Authorize and assign a group service.

    The authorizedQuantity will be used at the group level if provided; otherwise, the service quantity will be set to unlimited.
    The command will fail if the authorized quantity set at the service provider level is insufficient."""

    groupServiceName: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None


@dataclass
class GroupServiceAuthorizationAndAssignment(OCIType):
    """Authorize (with quantity) a group service, and optionally
    assign the service."""

    serviceName: str

    authorizedQuantity: Optional[UnboundedPositiveInt] = None

    assign: Optional[bool] = None


@dataclass
class ServicePack(OCIType):
    """The common Service Pack elements."""

    servicePackName: str

    isAvailableForUse: bool

    servicePackQuantity: UnboundedPositiveInt

    servicePackDescription: Optional[str] = None

    serviceName: List[str] = field(default_factory=list)


@dataclass
class VerifyTranslationAndRoutingParameters(OCIType):
    """Verification Translation and Routing parameters
    for creating a Verify Translation and Routing request from
    parameters.

    The following data elements are only used in AS data mode and ignored in XS data mode:
      contact
      diversion

    The following data elements are only used in XS data mode and ignored in AS data mode:
      imsCallType
      sipInstance
      viaAddress"""

    origination: VerifyTranslationAndRoutingOrigination

    destination: str

    contact: Optional[str] = None

    diversion: Optional[str] = None

    imsCallType: Optional[str] = None

    sipInstance: Optional[str] = None

    viaAddress: Optional[str] = None


@dataclass
class ReceptionistContactUserAndNote(OCIType):
    """The Receptionist User (or VON User) and Receptionist Notes."""

    contactUserId: str

    vonUser: VirtualOnNetUserKey

    note: str


@dataclass
class SearchCriteriaServiceCode(SearchCriteria):
    """Criteria for searching for a Service Code."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaEnterpriseCommonPhoneListNumber(SearchCriteria):
    """Criteria for searching for a phone number in an enterprise common phone list."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaHomeMscAddress(SearchCriteria):
    """Criteria for searching for a system Home Network Msc Address."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceManagementEventRequest(SearchCriteria):
    """Criteria for searching for a particular OCI request name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaUserHotlineContact(SearchCriteria):
    """Criteria for searching for a user's hotline contact."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaPersonalAssistantExclusionNumber(SearchCriteria):
    """Criteria for searching for Personal Assistant Exclusion Number."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaAlternateUserId(SearchCriteria):
    """Criteria for searching for a user's alternate userId."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaUserName(SearchCriteria):
    """Criteria for searching for a user's full name.
    This search criterion will be compared against multiple combinations of first name and last name:

    First Name + ' ' + Last Name
    Last Name + ' ' + First Name
    Last Name + ', ' + First Name
    Hiragana Last Name + ' ' + Hiragana First Name

    Note that when specific conditions are met, VON users will be included in the search results."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactOrganizationType(SearchCriteria):
    """Criteria for searching for an organization type."""

    organizationType: str


@dataclass
class SearchCriteriaGroupName(SearchCriteria):
    """Criteria for searching for a group name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaTitle(SearchCriteria):
    """Criteria for searching for a user's title."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactCallCenterReportTemplateKey(SearchCriteria):
    """Criteria for searching for a particular call center enhanced reporting report template."""

    reportTemplate: CallCenterReportTemplateKey


@dataclass
class SearchCriteriaCallCenterScheduledReportName(SearchCriteria):
    """Criteria for searching for a call center enhanced reporting scheduled report name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactDnDepartment(SearchCriteria):
    """Criteria for searching for a particular fully specified DN's department."""

    departmentKey: DepartmentKey


@dataclass
class SearchCriteriaExactMobileNetwork(SearchCriteria):
    """Criteria for searching for a particular BroadWorks Mobility Mobile Network."""

    mobileNetworkName: str


@dataclass
class SearchCriteriaGroupCommonPhoneListNumber(SearchCriteria):
    """Criteria for searching for a phone number in a group common phone list."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceManagementEventLoginId(SearchCriteria):
    """Criteria for searching for a particular login id."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceManagementEventAdditionalInfo(SearchCriteria):
    """Criteria for searching for a particular additional info of a DeviceManagement event."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactScheduleLevel(SearchCriteria):
    """Criteria for searching for a particular schedule level."""

    level: str


@dataclass
class SearchCriteriaExactSubscriberType(SearchCriteria):
    """Criteria for searching for a particular Subscriber Type."""

    subscriberType: str


@dataclass
class SearchCriteriaSystemServiceDn(SearchCriteria):
    """Criteria for searching for a system service DN."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactUserGroup(SearchCriteria):
    """Criteria for searching for a particular fully specified user's group."""

    serviceProviderId: str

    groupId: str


@dataclass
class SearchCriteriaEnterpriseCommonMultiPartPhoneListName(SearchCriteria):
    """Criteria for searching for a multi-part name in an enterprise common phone list.\
        Note: For this search criterion, the searchMode is always ‘Contains’ and the multi-part search criteria are always AND’ed."""

    value: List[str] = field(default_factory=list)

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactEndpointType21sp1(SearchCriteria):
    """Criteria for searching for a particular endpoint type."""

    endpointType: str


@dataclass
class SearchCriteriaAnnouncementFileName(SearchCriteria):
    """Criteria for searching for an Announcement File Name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaCallParkName(SearchCriteria):
    """Criteria for searching for a call park by name"""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaGroupExternalId(SearchCriteria):
    """Criteria for searching by a group's externalId."""

    mode: str

    value: str


@dataclass
class SearchCriteriaExactMediaFileType(SearchCriteria):
    """Criteria for searching for a particular media file type."""

    type: str


@dataclass
class SearchCriteriaResellerId(SearchCriteria):
    """Criteria for searching for a reseller ID."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactUserPersonId(SearchCriteria):
    """Criteria for searching for a particular user's personId."""

    userPersonId: str


@dataclass
class SearchCriteriaYahooId(SearchCriteria):
    """Criteria for searching for a user's yahoo id."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaServiceInstanceName(SearchCriteria):
    """Criteria for searching for a service instance name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaIMRN(SearchCriteria):
    """Criteria for searching for an IMRN Number."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactDeviceServiceProvider(SearchCriteria):
    """Criteria for searching for a particular fully specified service provider associated with a device."""

    serviceProviderId: str


@dataclass
class SearchCriteriaZoneIPAddress(SearchCriteria):
    """Criteria for searching for a system zone's IP Address."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactServiceProviderAdminType(SearchCriteria):
    """Criteria for searching for a particular service provider administrator type."""

    type: str


@dataclass
class SearchCriteriaExactDeviceManagementEventLevel(SearchCriteria):
    """Criteria for searching for a particular fully specified DeviceManagement event level."""

    dmEventLevel: str


@dataclass
class SearchCriteriaExactDomainLevel(SearchCriteria):
    """Criteria for searching for a particular domain level."""

    domainLevel: str


@dataclass
class SearchCriteriaLinePortDomain(SearchCriteria):
    """Criteria for searching for device line/port, or SIPURI domain part."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDn(SearchCriteria):
    """Criteria for searching for a DN."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDepartmentName(SearchCriteria):
    """Criteria for searching for a user's department."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDigitPattern(SearchCriteria):
    """Criteria for searching for digit pattern."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactCallCenterScheduledReportServiceProvider(SearchCriteria):
    """Criteria for searching for a particular call center scheduled report's service provider."""

    serviceProviderId: str


@dataclass
class SearchCriteriaUserPlaceType(SearchCriteria):
    """Criteria for searching based on a user type – \"User\" or \"Place\"."""

    value: str


@dataclass
class SearchCriteriaExactScheduleType(SearchCriteria):
    """Criteria for searching for a particular schedule type."""

    type: str


@dataclass
class SearchCriteriaCommunicationBarringAuthorizationCodeDescription(SearchCriteria):
    """Criteria for searching for a Communication Barring Authorization Code description."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaPersonalAssistantExclusionNumberDescription(SearchCriteria):
    """Criteria for searching Personal Assistant Exclusion Number's Description."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaNetworkClassOfServiceName(SearchCriteria):
    """Criteria for searching for a Network Class of Service name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactGroupAdminType(SearchCriteria):
    """Criteria for searching for a particular group administrator type."""

    type: str


@dataclass
class SearchCriteriaForwardedToNumber(SearchCriteria):
    """Criteria for searching for a forwarded to number.
    This search criteria data type is only intended to be used by the commands
    introduced by BW-2301.
    The commands are EnterpriseUserCallForwardingSettingsGetListRequest
    and GroupUserCallForwardingSettingsGetListRequest.
    The following Call Forwarding services are compatible for this search:
    Call Forwarding Always, Call Forwarding Always Secondary, Call Forwarding Busy,
    Call Forwarding No Answer, Call Forwarding Not Reachable, Call Forwarding Selective."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactCallCenterType(SearchCriteria):
    """Criteria for searching for a particular fully specified call center type."""

    callCenterType: str


@dataclass
class SearchCriteriaUserPersonalPhoneListNumber(SearchCriteria):
    """Criteria for searching for a phone number in a user personal phone list."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaGroupId(SearchCriteria):
    """Criteria for searching for a group ID."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactUserRouteListAssignment(SearchCriteria):
    """Criteria for searching for users with Route List feature assignment."""

    assigned: bool


@dataclass
class SearchCriteriaExactDeviceManagementEventType(SearchCriteria):
    """Criteria for searching for a particular fully specified DeviceManagement event type."""

    dmEventType: str


@dataclass
class SearchCriteriaServiceCodeDescription(SearchCriteria):
    """Criteria for searching for a Service Code description."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaAccessDeviceVersion(SearchCriteria):
    """Criteria for searching for an Access Device Version."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaEnterpriseTrunkName(SearchCriteria):
    """Criteria for searching for an Enterprise Trunk name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaResellerName(SearchCriteria):
    """Criteria for searching for a reseller name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaUserFirstName(SearchCriteria):
    """Criteria for searching for a user's first name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactDeviceManagementEventAction(SearchCriteria):
    """Criteria for searching for a particular fully specified DeviceManagement event action."""

    dmEventAction: str


@dataclass
class SearchCriteriaAgentThresholdProfile(SearchCriteria):
    """Criteria for searching a Call Center Agent Threshold Profile."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaNumberPortabilityQueryDigitPattern(SearchCriteria):
    """Criteria for searching for digit pattern."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaReceptionistNote(SearchCriteria):
    """Criteria for searching for Receptionist Notes."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceNetAddress(SearchCriteria):
    """Criteria for searching for device network address."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaAdminFirstName(SearchCriteria):
    """Criteria for searching for an administrator's first name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaMultiPartUserName(SearchCriteria):
    """Criteria for searching for a user's full name.
    This search criterion will be compared against multiple combinations of first name and last name:

    First Name + ‘ ‘ + Last Name
    Last Name + ‘ ‘ + First Name
    Last Name + ‘, ‘ + First Name
    Hiragana Last Name + Hiragana First Name

    Note that when specific conditions are met, VON users will be included in the search results.
    Note: For this search criterion, the searchMode is always ‘Contains’ and the multi-part search criteria are always AND’ed."""

    value: List[str] = field(default_factory=list)

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaUserPersonalMultiPartPhoneListName(SearchCriteria):
    """Criteria for searching for a name in a user personal phone list.
    Note: For this search criterion, the searchMode is always ‘Contains’ and the multi-part search criteria are always AND’ed."""

    value: List[str] = field(default_factory=list)

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaOutgoingDNorSIPURI(SearchCriteria):
    """Criteria for searching for a phone number or SIPURI."""

    mode: str

    value: str

    isCaseInsensitive: bool


@dataclass
class SearchCriteriaGroupCommonPhoneListName(SearchCriteria):
    """Criteria for searching for a name in a group common phone list."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactUserInTrunkGroup(SearchCriteria):
    """Criteria for searching for user in/not in a trunk group."""

    userInTrunkGroup: bool


@dataclass
class SearchCriteriaPhysicalLocation(SearchCriteria):
    """Criteria for searching for a Physical Location."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceSerialNumber(SearchCriteria):
    """Criteria for searching for device serial number."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactDeviceLevel(SearchCriteria):
    """Criteria for searching for a particular device level."""

    deviceLevel: str


@dataclass
class SearchCriteriaScheduleName(SearchCriteria):
    """Criteria for searching for a schedule name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaAdminLastName(SearchCriteria):
    """Criteria for searching for an administrator's last name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactDeviceType(SearchCriteria):
    """Criteria for searching for a particular fully specified device type."""

    deviceType: str


@dataclass
class SearchCriteriaDomainName(SearchCriteria):
    """Criteria for searching for Domain Names."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactCallCenterScheduledReportGroup(SearchCriteria):
    """Criteria for searching for a particular fully specified call center scheduled
    report's group."""

    serviceProviderId: str

    groupId: str


@dataclass
class SearchCriteriaExactLocationEnabled(SearchCriteria):
    """Criteria for searching for a particular Location enabled state."""

    enabled: bool


@dataclass
class SearchCriteriaUserExternalId(SearchCriteria):
    """Criteria for searching for a user's externalId."""

    mode: str

    value: str


@dataclass
class SearchCriteriaExtension(SearchCriteria):
    """Criteria for searching for an extension."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaLocation(SearchCriteria):
    """Criteria for searching for a Location."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceType(SearchCriteria):
    """Criteria for searching for device type."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaCallCenterName(SearchCriteria):
    """Criteria for searching for a call center"""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaMobilePhoneNumber(SearchCriteria):
    """Criteria for searching for a user's mobile phone number."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaUserId(SearchCriteria):
    """Criteria for searching for a user's userId."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaEnterpriseCommonPhoneListName(SearchCriteria):
    """Criteria for searching for a name in an enterprise common phone list."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaCommunicationBarringAuthorizationCode(SearchCriteria):
    """Criteria for searching for a Communication Barring Authorization Code."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactDnActivation(SearchCriteria):
    """Criteria for searching for a particular Dn activation state."""

    activated: bool


@dataclass
class SearchCriteriaServiceStatus(SearchCriteria):
    """Criteria for searching for services that are active or not.
    This search criteria data type is only intended to be used by the commands
    introduced by BW-2301.
    The commands are EnterpriseUserCallWaitingSettingsGetListRequest
    and GroupUserCallWaitingSettingsGetListRequest."""

    isActive: bool


@dataclass
class SearchCriteriaExactDeviceManagementEventStatusInProgressOrPending(SearchCriteria):
    """Criteria for searching for a particular fully specified Device Management event in progress or pending status."""

    dmEventStatusInProgressOrPending: str


@dataclass
class SearchCriteriaExactUserDepartment(SearchCriteria):
    """Criteria for searching for a particular fully specified user's department."""

    departmentKey: DepartmentKey


@dataclass
class SearchCriteriaTrunkGroupName(SearchCriteria):
    """Criteria for searching for a trunk group"""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaCallPickupName(SearchCriteria):
    """Criteria for searching for a call pickup by name"""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactMobileDnAvailability(SearchCriteria):
    """Criteria for searching for a particular mobile dn availability."""

    available: bool


@dataclass
class SearchCriteriaExactSkillLevel(SearchCriteria):
    """Criteria for searching for a skill Level."""

    skillLevel: int


@dataclass
class SearchCriteriaExactDnAvailability(SearchCriteria):
    """Criteria for searching for a particular dn availability."""

    available: bool


@dataclass
class SearchCriteriaServiceProviderId(SearchCriteria):
    """Criteria for searching for a service provider ID."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactSignalingAddressType(SearchCriteria):
    """Criteria for searching for a particular fully specified SignalingAddressType."""

    profile: str


@dataclass
class SearchCriteriaLanguage(SearchCriteria):
    """Criteria for searching for a language."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceMACAddress(SearchCriteria):
    """Criteria for searching for device MAC address."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaLoginId(SearchCriteria):
    """Criteria for searching for a Login Id."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaCallCenterReportTemplateName(SearchCriteria):
    """Criteria for searching for a particular call center enhanced reporting report template."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactCustomContactDirectory(SearchCriteria):
    """Criteria for searching for a particular fully specified custom contact directory."""

    customContactDirectoryName: str


@dataclass
class SearchCriteriaAlternateTrunkIdentityDomain(SearchCriteria):
    """Criteria for searching for alternate trunk identity domain part."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceManagementEventRequestTrackingId(SearchCriteria):
    """Criteria for searching for a particular OCI tracking id."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaUserLastName(SearchCriteria):
    """Criteria for searching for a user's last name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactCallCenterScheduledReportCreatedBySupervisor(SearchCriteria):
    """Criteria for searching for call center scheduled report created by a
    supervisor or administrator."""

    createdBySupervisor: bool


@dataclass
class SearchCriteriaExactDeviceManagementEventStatusCompleted(SearchCriteria):
    """Criteria for searching for a particular fully specified Device Management completed event status."""

    dmEventStatusCompleted: str


@dataclass
class SearchCriteriaExactHuntPolicy(SearchCriteria):
    """Criteria for searching for a particular fully specified hunt policy."""

    huntPolicy: str


@dataclass
class SearchCriteriaAlternateTrunkIdentity(SearchCriteria):
    """Criteria for searching for a particular fully specified alternate trunk identity.
    In IMS mode, it only applies to the user part of alternate trunk identity."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaRoamingMscAddress(SearchCriteria):
    """Criteria for searching for a system Roaming Network Msc Address."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaEmailAddress(SearchCriteria):
    """Criteria for searching for a email address."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaDeviceName(SearchCriteria):
    """Criteria for searching for device name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaAdminId(SearchCriteria):
    """Criteria for searching for an administrator's adminId."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaServiceProviderName(SearchCriteria):
    """Criteria for searching for a service provider name."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaServiceProviderNumberPortabilityQueryDigitPattern(SearchCriteria):
    """Criteria for searching for digit pattern."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactPortNumber(SearchCriteria):
    """Criteria for searching for a port number."""

    port: int


@dataclass
class SearchCriteriaGroupLocationCode(SearchCriteria):
    """Criteria for searching for a group location dialing code."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaUserPersonalPhoneListName(SearchCriteria):
    """Criteria for searching for a name in a user personal phone list."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactUserRouteListAssigned(SearchCriteria):
    """Criteria for searching for users with/without Route List feature assigned."""

    routeListAssigned: bool


@dataclass
class SearchCriteriaExactVirtualOnNetCallTypeName(SearchCriteria):
    """Criteria for searching for a particular fully specified Virtual On-Net Call Type Name."""

    virtualOnNetCallTypeName: str


@dataclass
class SearchCriteriaExactUserType(SearchCriteria):
    """Criteria for searching for a particular User Type."""

    userType: str


@dataclass
class SearchCriteriaMobileSubscriberDirectoryNumber(SearchCriteria):
    """Criteria for searching for a BroadWorks Mobility Mobile Subscriber Directory Number."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaLinePortUserPart(SearchCriteria):
    """Criteria for searching for device line/port, or SIPURI user part."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactUserNetworkClassOfService(SearchCriteria):
    """Criteria for searching for users with a specified network class of service."""

    networkClassOfService: str


@dataclass
class SearchCriteriaRoutePointName(SearchCriteria):
    """Criteria for searching for a route point"""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactAutoAttendantType(SearchCriteria):
    """Criteria for searching for a particular auto-attendant type."""

    type: str


@dataclass
class SearchCriteriaExactServiceType(SearchCriteria):
    """Criteria for searching for a particular fully specified service type."""

    serviceType: str


@dataclass
class SearchCriteriaSIPContact(SearchCriteria):
    """Criteria for searching for a SIP Contact."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaNumberPortabilityStatus(SearchCriteria):
    """Criteria for searching for number portability status."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaImpId(SearchCriteria):
    """Criteria for searching for a user's IMP Id."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactAnnouncementFileType(SearchCriteria):
    """Criteria for searching for a particular announcement file type."""

    type: str


@dataclass
class SearchCriteriaRegistrationURI(SearchCriteria):
    """Criteria for searching for a RegistrationURI."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaAccessDeviceEndpointPrivateIdentity(SearchCriteria):
    """Criteria for searching for a private identity."""

    mode: str

    value: str

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactDeviceTypeConfigurationOptionType(SearchCriteria):
    """Criteria for searching for a particular fully specified DeviceTypeConfigurationOptionType."""

    deviceConfigOptions: str


@dataclass
class SearchCriteriaExactServiceProvider(SearchCriteria):
    """Criteria for searching for a particular fully specified service provider."""

    serviceProviderId: str


@dataclass
class SearchCriteriaGroupCommonMultiPartPhoneListName(SearchCriteria):
    """Criteria for searching for a multi-value name in a group common phone list.
    Note: For this search criterion, the searchMode is always ‘Contains’ and the multi-part search criteria are always AND’ed."""

    value: List[str] = field(default_factory=list)

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaExactPolicySelection(SearchCriteria):
    """Criteria for searching for a particular Voice VPN policy selection."""

    policySelection: str


@dataclass
class SearchCriteriaComposedOrUserName(SearchCriteriaComposedOr):
    """Criteria for searching for a user's full name.
    This search criterion will be compared against multiple combinations of first name and last name:

    First Name + ‘ ‘ + Last Name
    Last Name + ‘ ‘ + First Name
    Hiragana Last Name + ' ' + Hiragana First Name

    Note: For this search criterion, the searchMode is always ‘Contains’ and the search criteria are always OR’ed."""

    value: List[str] = field(default_factory=list)

    isCaseInsensitive: bool = True


@dataclass
class SearchCriteriaComposedOrDnExtension(SearchCriteriaComposedOr):
    """Criteria for searching for a DN OR an extension.
    Note: For this search criterion, the searchMode is always ‘Contains’ and the search criteria are always OR’ed."""

    value: UserDNExtension


@dataclass
class SortByAdminLastName(SortCriteria):
    """The sort criteria specifies the administrator last name
    as the column for the
    sort, whether the
    sort is ascending or
    descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByDepartmentName(SortCriteria):
    """The sort criteria specifies the department name as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByLocation(SortCriteria):
    """The sort criteria specifies the Broadworks Location as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByExtension(SortCriteria):
    """The sort criteria specifies the extension as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByMobilePhoneNumber(SortCriteria):
    """The sort criteria specifies the mobile phone number as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByServiceStatus(SortCriteria):
    """The sort criteria specifies the service status as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive.
    This sort criteria data type is only intended to be used by the commands
    introduced by BW-2301.
    The commands are EnterpriseUserCallWaitingSettingsGetListRequest, GroupUserCallWaitingSettingsGetListRequest,
    EnterpriseUserHotelingGuestSettingsGetListRequest, and GroupUserHotelingGuestSettingsGetListRequest."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByGroupCommonPhoneListName(SortCriteria):
    """The sort criteria specifies the group common phone list name as the column for the sort, whether
    the sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByAgentThresholdProfile(SortCriteria):
    """The sort criteria specifies the call center agent threshold profile as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByAdminFirstName(SortCriteria):
    """The sort criteria specifies the administrator first name
    as the column for the
    sort, whether the
    sort is ascending or
    descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByUserFirstName(SortCriteria):
    """The sort criteria specifies the user first name as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByAdminId(SortCriteria):
    """The sort criteria specifies the administrator id as the
    column for the sort,
    whether the
    sort is ascending or descending,
    and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByMobileDirectoryNumber(SortCriteria):
    """The sort criteria specifies the Mobile dn availability as the column for the
    sort, whether the sort is ascending or descending, and whether the sort
    is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByGroupName(SortCriteria):
    """The sort criteria specifies the group name as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByUserDepartment(SortCriteria):
    """The sort criteria specifies the user department name as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByUserLastName(SortCriteria):
    """The sort criteria specifies the user last name as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByReceptionistNote(SortCriteria):
    """The sort criteria specifies the Receptionist Notes as the column for the sort, whether
    the sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByCallCenterType(SortCriteria):
    """The sort criteria specifies the call center type as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByGroupId(SortCriteria):
    """The sort criteria specifies the group id as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByImpId(SortCriteria):
    """The sort criteria specifies the imp id as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByYahooId(SortCriteria):
    """The sort criteria specifies the yahoo id as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByEnabled(SortCriteria):
    """The sort criteria specifies the Broadworks Enabled Flag as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByHuntPolicy(SortCriteria):
    """The sort criteria specifies the call center hunt policy as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByDeviceName(SortCriteria):
    """The sort criteria specifies the device name as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByCallParkName(SortCriteria):
    """The sort criteria specifies the call park name as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByForwardedToNumber(SortCriteria):
    """The sort criteria specifies the forwarded to phone number as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive.
    This sort criteria data type is only intended to be used by the commands
    introduced by BW-2301.
    The commands are EnterpriseUserCallForwardingSettingsGetListRequest
    and GroupUserCallForwardingSettingsGetListRequest.
    The following Call Forwarding services are compatible for this search:
    Call Forwarding Always, Call Forwarding Always Secondary, Call Forwarding Busy,
    Call Forwarding No Answer, Call Forwarding Not Reachable, Call Forwarding Selective."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByDn(SortCriteria):
    """The sort criteria specifies the DN as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByDnActivated(SortCriteria):
    """The sort criteria specifies the dn activation status as the column for the sort,
    whether the sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByDnAvailable(SortCriteria):
    """The sort criteria specifies the dn availability as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByEmailAddress(SortCriteria):
    """The sort criteria specifies the email as the column for the sort, whether
    the sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByUserPersonalPhoneListName(SortCriteria):
    """The sort criteria specifies the user personal phone list name as the column for the sort, whether
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByGroupLocationCode(SortCriteria):
    """The sort criteria specifies the group location code as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByEnterpriseCommonPhoneListName(SortCriteria):
    """The sort criteria specifies the enterprise common phone list name as the
    column for the sort, whether sort is ascending or descending, and
    whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByServiceProviderId(SortCriteria):
    """The sort criteria specifies the service provider id as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByEnterpriseCommonPhoneListNumber(SortCriteria):
    """The sort criteria specifies the enterprise common phone list number as as the column
    for the sort, whether sort is ascending or descending, and whether the sort is
    case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByCallPickupName(SortCriteria):
    """The sort criteria specifies the call pickup name as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByUserId(SortCriteria):
    """The sort criteria specifies the user id as the column for the sort,
    whether the sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByDeviceMACAddress(SortCriteria):
    """The sort criteria specifies the device MAC address as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByDeviceType(SortCriteria):
    """The sort criteria specifies the device type as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByScheduleName(SortCriteria):
    """The sort criteria specifies the schedule name as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByAnnouncementFileName(SortCriteria):
    """The sort criteria specifies the file name as the column for the sort,
    whether the sort is ascending or descending, and whether the sort is
    case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByServiceProviderName(SortCriteria):
    """The sort criteria specifies the service provider name as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByGroupCommonPhoneListNumber(SortCriteria):
    """The sort criteria specifies the group common phone list number as the column for the sort, whether
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByDeviceNetAddress(SortCriteria):
    """The sort criteria specifies the device net address as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByTrunkGroupName(SortCriteria):
    """The sort criteria specifies the trunk group name as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByUserPersonalPhoneListNumber(SortCriteria):
    """The sort criteria specifies the user personal phone list number as the column for
    the sort, whether the sort is ascending or descending, and whether the
    sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByCallCenterName(SortCriteria):
    """The sort criteria specifies the call center name as the column for the sort, whether the
    sort is ascending or descending, and whether the sort is case sensitive."""

    isAscending: bool = True

    isCaseSensitive: bool = True


@dataclass
class SortByAnnouncementFileSize(SortCriteriaNumeric):
    """The sort criteria specifies the file size as the column for the sort,
    whether the sort is ascending or descending, and whether the sort is
    case sensitive."""

    isAscending: bool = True


@dataclass
class EnterpriseVoiceVPNDigitManipulationRequiredValue(
    EnterpriseVoiceVPNDigitManipulation
):
    """Enterprise Voice VPN Digit Manipulation Entry that has a value."""

    operation: str

    value: str


@dataclass
class EnterpriseVoiceVPNDigitManipulationOptionalValue(
    EnterpriseVoiceVPNDigitManipulation
):
    """Enterprise Voice VPN Digit Manipulation Entry that optionally has a value."""

    operation: str

    value: Optional[str] = None


@dataclass
class EnterpriseVoiceVPNDigitManipulationNoValue(EnterpriseVoiceVPNDigitManipulation):
    """Enterprise Voice VPN Digit Manipulation Entry that has no value."""

    operation: str


@dataclass
class ReplacementCustomContactDirectoryEntryList(OCIType):
    """A list of userIds and/or Virtual On-Net user DNs that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    entry: List[CustomContactDirectoryEntry] = field(default_factory=list)


@dataclass
class CallCenterAgentStatistics14sp9(OCIType):
    """Contains Call Center statistics for a specified agent."""

    agentUserId: str

    agentDisplayNames: UserDisplayNames

    available: bool

    statistics: AgentStatistics


@dataclass
class CommPilotExpressAvailableOutOfOffice(OCIType):
    """CommPilot Express Available Out Of Office Configuration used in the context of a get."""

    incomingCalls: CommPilotExpressRedirection

    incomingCallNotify: CommPilotExpressEmailNotify


@dataclass
class CommPilotExpressAvailableInOffice(OCIType):
    """CommPilot Express Available In Office Settings."""

    busySetting: CommPilotExpressRedirection

    noAnswerSetting: CommPilotExpressRedirection

    additionalPhoneNumberToRing: Optional[str] = None


@dataclass
class CommPilotExpressAvailableOutOfOfficeModify(OCIType):
    """CommPilot Express Available Out Of Office Configuration used in the context of a modify."""

    incomingCalls: Optional[CommPilotExpressRedirectionModify] = None

    incomingCallNotify: Optional[CommPilotExpressEmailNotifyModify] = None


@dataclass
class CommPilotExpressAvailableInOfficeModify(OCIType):
    """CommPilot Express Available In Office Settings."""

    additionalPhoneNumberToRing: Optional[str] = None

    busySetting: Optional[CommPilotExpressRedirectionModify] = None

    noAnswerSetting: Optional[CommPilotExpressRedirectionModify] = None


@dataclass
class CommPilotExpressBusy(OCIType):
    """CommPilot Express Available In Office Configuration used in the context of a get."""

    incomingCalls: CommPilotExpressRedirectionWithException

    voiceMailNotify: CommPilotExpressEmailNotify


@dataclass
class CommPilotExpressUnavailable(OCIType):
    """CommPilot Express Unavailable Configuration used in the context of a get."""

    incomingCalls: CommPilotExpressRedirectionWithException

    voiceMailGreeting: str


@dataclass
class CommPilotExpressUnavailableModify(OCIType):
    """CommPilot Express Unavailable Configuration used in the context of a modify."""

    incomingCalls: Optional[CommPilotExpressRedirectionWithExceptionModify] = None

    voiceMailGreeting: Optional[str] = None


@dataclass
class CommPilotExpressBusyModify(OCIType):
    """CommPilot Express Available In Office Configuration used in the context of a modify."""

    incomingCalls: Optional[CommPilotExpressRedirectionWithExceptionModify] = None

    voiceMailNotify: Optional[CommPilotExpressEmailNotifyModify] = None


@dataclass
class IncomingCallingPlanDepartmentPermissionsModify(OCIType):
    """Allows or disallows various types of incoming calls for a specified department.
    For use when modifing settings."""

    departmentKey: DepartmentKey

    allowFromWithinGroup: Optional[bool] = None

    allowFromOutsideGroup: Optional[str] = None

    allowCollectCalls: Optional[bool] = None

    digitPatternPermission: List[IncomingCallingPlanDigitPatternPermission] = field(
        default_factory=list
    )


@dataclass
class IncomingCallingPlanDepartmentPermissions(OCIType):
    """Allows or disallows various types of incoming calls for a specified department."""

    departmentKey: DepartmentKey

    departmentFullPathName: str

    allowFromWithinGroup: bool

    allowFromOutsideGroup: str

    allowCollectCalls: bool

    digitPatternPermission: List[IncomingCallingPlanDigitPatternPermission] = field(
        default_factory=list
    )


@dataclass
class IncomingCallingPlanPermissions(OCIType):
    """Allows or disallows various types of incoming calls for a user or group -- not any particular department."""

    allowFromWithinGroup: bool

    allowFromOutsideGroup: str

    allowCollectCalls: bool

    digitPatternPermission: List[IncomingCallingPlanDigitPatternPermission] = field(
        default_factory=list
    )


@dataclass
class IncomingCallingPlanPermissionsModify(OCIType):
    """Allows or disallows various types of incoming calls for a user or group -- not any particular department.
    For use when modifing settings."""

    allowFromWithinGroup: Optional[bool] = None

    allowFromOutsideGroup: Optional[str] = None

    allowCollectCalls: Optional[bool] = None

    digitPatternPermission: List[IncomingCallingPlanDigitPatternPermission] = field(
        default_factory=list
    )


@dataclass
class MWIDeliveryToMobileEndpointTemplateBody23(OCIType):
    """MWI Delivery To Mobile Endpoint template body."""

    line: List[MWIDeliveryToMobileEndpointTemplateLine23] = field(default_factory=list)


@dataclass
class OutgoingCallingPlanGroupAuthorizationCodes(OCIType):
    """Outgoing Calling Plan Authorization Code for the group default."""

    codeEntry: List[OutgoingCallingPlanAuthorizationCodeEntry] = field(
        default_factory=list
    )


@dataclass
class OutgoingCallingPlanDepartmentAuthorizationCodes(OCIType):
    """Outgoing Calling Plan Authorization Code for a department."""

    departmentKey: DepartmentKey

    departmentName: str

    codeEntry: List[OutgoingCallingPlanAuthorizationCodeEntry] = field(
        default_factory=list
    )


@dataclass
class OutgoingCallingPlanCallMeNowDepartmentPermissions(OCIType):
    """Outgoing Calling Plan for Call Me Now call permissions for a department."""

    departmentKey: DepartmentKey

    departmentName: str

    permissions: OutgoingCallingPlanCallMeNowPermissions


@dataclass
class OutgoingCallingPlanCallMeNowDepartmentPermissionsModify(OCIType):
    """Modify outgoing Calling Plan for Call Me Now call permissions for a department."""

    departmentKey: DepartmentKey

    permissions: OutgoingCallingPlanCallMeNowPermissionsModify


@dataclass
class OutgoingCallingPlanDigitPatternCallMeNowPermissions(OCIType):
    """Outgoing Calling Plan Call Me Now call permissions for specified digit patterns."""

    digitPatternPermissions: List[
        OutgoingCallingPlanDigitPatternCallMeNowPermission
    ] = field(default_factory=list)


@dataclass
class OutgoingCallingPlanDigitPatternOriginatingPermissions(OCIType):
    """Outgoing Calling Plan originating call permissions for specified digit patterns."""

    digitPatternPermissions: List[
        OutgoingCallingPlanDigitPatternOriginatingPermission
    ] = field(default_factory=list)


@dataclass
class OutgoingCallingPlanDigitPatternRedirectingPermissions(OCIType):
    """Outgoing Calling Plan redirecting call permissions for specified digit patterns."""

    digitPatternPermissions: List[
        OutgoingCallingPlanDigitPatternRedirectingPermission
    ] = field(default_factory=list)


@dataclass
class OutgoingCallingPlanOriginatingDepartmentPermissions(OCIType):
    """Outgoing Calling Plan originating call permissions for a department."""

    departmentKey: DepartmentKey

    departmentName: str

    permissions: OutgoingCallingPlanOriginatingPermissions


@dataclass
class OutgoingCallingPlanOriginatingDepartmentPermissionsModify(OCIType):
    """Outgoing Calling Plan originating call permissions for a department."""

    departmentKey: DepartmentKey

    permissions: Optional[OutgoingCallingPlanOriginatingPermissionsModify] = None


@dataclass
class OutgoingCallingPlanRedirectedDepartmentPermissions(OCIType):
    """Outgoing Calling Plan being forwarded/transferred permissions for a department."""

    departmentKey: DepartmentKey

    departmentName: str

    permissions: OutgoingCallingPlanRedirectedPermissions


@dataclass
class OutgoingCallingPlanRedirectedDepartmentPermissionsModify(OCIType):
    """Outgoing Calling Plan being forwarded/transferred permissions for a department."""

    departmentKey: DepartmentKey

    permissions: OutgoingCallingPlanRedirectedPermissionsModify


@dataclass
class OutgoingCallingPlanRedirectingDepartmentPermissions(OCIType):
    """Outgoing Calling Plan initiating call forwards/transfer permissions for a department."""

    departmentKey: DepartmentKey

    departmentName: str

    permissions: OutgoingCallingPlanRedirectingPermissions


@dataclass
class OutgoingCallingPlanRedirectingDepartmentPermissionsModify(OCIType):
    """Outgoing Calling Plan initiating call forwards/transfer permissions for a department."""

    departmentKey: DepartmentKey

    permissions: OutgoingCallingPlanRedirectingPermissionsModify


@dataclass
class OutgoingCallingPlanDepartmentTransferNumbers(OCIType):
    """Outgoing Calling Plan transfer numbers for a department."""

    departmentKey: DepartmentKey

    departmentName: str

    transferNumbers: OutgoingCallingPlanTransferNumbers


@dataclass
class OutgoingCallingPlanDepartmentTransferNumbersModify(OCIType):
    """Outgoing Calling Plan transfer numbers for a department."""

    departmentKey: DepartmentKey

    transferNumbers: Optional[OutgoingCallingPlanTransferNumbersModify] = None


@dataclass
class OutgoingPinholeDigitPlanDigitPatternCallMeNowPermissions(OCIType):
    """Outgoing Pinhole Digit Plan Call Me Now call permissions for specified digit patterns."""

    digitPatternPermissions: List[
        OutgoingPinholeDigitPlanDigitPatternCallMeNowPermission
    ] = field(default_factory=list)


@dataclass
class OutgoingPinholeDigitPlanDigitPatternOriginatingPermissions(OCIType):
    """Outgoing Pinhole Digit Plan originating call permissions for specified digit patterns."""

    digitPatternPermissions: List[
        OutgoingPinholeDigitPlanDigitPatternOriginatingPermission
    ] = field(default_factory=list)


@dataclass
class OutgoingPinholeDigitPlanDigitPatternRedirectingPermissions(OCIType):
    """Outgoing Pinhole Digit Plan redirecting call permissions for specified digit patterns."""

    digitPatternPermissions: List[
        OutgoingPinholeDigitPlanDigitPatternRedirectingPermission
    ] = field(default_factory=list)


@dataclass
class ReplacementEnterpriseEnterpriseTrunkTrunkGroupKeyList(OCIType):
    """A list of Enterprise Trunk Krunk Group Keys that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    trunkGroup: List[EnterpriseTrunkTrunkGroupKey] = field(default_factory=list)


@dataclass
class EnterpriseEnterpriseTrunkPriorityWeightedTrunkGroup(OCIType):
    """Trunk group details (order and weight) for each trunk group"""

    trunkGroup: EnterpriseTrunkTrunkGroupKey

    priority: int

    weight: int


@dataclass
class EnterpriseTrunkPriorityWeightedTrunkGroup(OCIType):
    """Trunk group details (order and weight) for each trunk group"""

    trunkGroup: EnterpriseTrunkTrunkGroupKey

    priority: int

    weight: int


@dataclass
class ReplacementEnterpriseTrunkTrunkGroupKeyList(OCIType):
    """A list of Enterprise Trunk Krunk Group Keys that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    trunkGroupList: List[EnterpriseTrunkTrunkGroupKey] = field(default_factory=list)


@dataclass
class ReplacementGroupEnterpriseTrunkPriorityWeightedTrunkGroupList(OCIType):
    """A list of enterprise trunk priority weighted trunk groups in a group that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    trunkGroup: List[GroupEnterpriseTrunkPriorityWeightedTrunkGroup] = field(
        default_factory=list
    )


@dataclass
class OCITable(OCIType):
    """The OCITable type is used in responses only, never in requests.
    The table consists of rows and columns of strings. Each column has a column
    heading. Clients should search the column headings to find a particular
    column. Clients should not assume any particular column order as future
    revisions of the protocol may move or add columns."""

    colHeading: List[str] = field(default_factory=list)

    row: List[OCITableRow] = field(default_factory=list)


@dataclass
class OCIMessage(OCIType):
    """A message contains a list of requests or responses. The server processes all the requests
    and returns a message with a corresponding list of responses."""

    sessionId: str
    # The session id identifies a logged-in user. The client is responsible to ensure the uniqueness of the session id.

    userId: str
    # The user id identifies a preauthenticated user performing a session-less OCI request. The source of the request
    # must be in the external authentication access control list.

    phoneNumber: str
    # The phone number identifies a preauthenticated user performing a session-less OCI request. The source of the request
    # must be in the external authentication access control list.
    # The phone number must be in E.164 format.  Any DN associated with the user may be used.
    # BroadSoft recommends only using this element in the rare case when the userId is not known.

    linePort: str
    # The lineport identifies a preauthenticated user performing a session-less OCI request. The source of the request must be in the external authentication access control list.
    # The lineport may be any lineport associated with a user.
    # BroadSoft recommends only using this element in the rare case when the userId is not known.

    externalUserIdentity: ExternalUserIdentity
    # The external user identity identifies a preauthenticated user/admin performing a session-less OCI request. The source of the request must have a valid CI access token.

    trackingId: Optional[str] = None
    # The client can send the trackingId attribute in any request and the server will return the trackingId attribute in the response.

    command: List[OCICommand] = field(default_factory=list)


# List of requests or responses.


@dataclass
class ReplacementEnterpriseDeviceList(OCIType):
    """A list of enterprise accessible devices that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    device: List[EnterpriseAccessDevice] = field(default_factory=list)


@dataclass
class AutoAttendantKeyModifyConfiguration20(OCIType):
    """The modify configuration of a key for Auto Attendant."""

    key: str

    entry: AutoAttendantKeyConfigurationModifyEntry20


@dataclass
class AutoAttendantKeyReadConfiguration20(OCIType):
    """The read configuration of a key for Auto Attendant."""

    key: str

    entry: AutoAttendantKeyConfigurationReadEntry20


@dataclass
class AutoAttendantKeyConfiguration20(OCIType):
    """The configuration of a key for Auto Attendant."""

    key: str

    entry: AutoAttendantKeyConfigurationEntry20


@dataclass
class CallCenterMediaOnHoldSourceRead22(OCIType):
    """Contains the call center media on hold source configuration."""

    audioMessageSourceSelection: str

    audioUrlList: Optional[CallCenterAnnouncementURLList] = None

    audioFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    externalAudioSource: Optional[AccessDeviceEndpointWithPortNumberRead22] = None

    videoMessageSourceSelection: Optional[str] = None

    videoUrlList: Optional[CallCenterAnnouncementURLList] = None

    videoFileList: Optional[CallCenterAnnouncementFileListRead20] = None

    externalVideoSource: Optional[AccessDeviceEndpointWithPortNumberRead22] = None


@dataclass
class CallCenterMediaOnHoldSourceModify20(OCIType):
    """Contains the call center media on hold source configuration."""

    audioMessageSourceSelection: Optional[str] = None

    audioUrlList: Optional[CallCenterAnnouncementURLListModify] = None

    audioFileList: Optional[CallCenterAnnouncementFileListModify20] = None

    externalAudioSource: Optional[AccessDeviceEndpointModify] = None

    videoMessageSourceSelection: Optional[str] = None

    videoUrlList: Optional[CallCenterAnnouncementURLListModify] = None

    videoFileList: Optional[CallCenterAnnouncementFileListModify20] = None

    externalVideoSource: Optional[AccessDeviceEndpointModify] = None


@dataclass
class AutoAttendantReadMenu19(OCIType):
    """The configuration of the automated receptionist
    greeting
    prompt and dialing menu to be used during
    after business
    hours."""

    announcementSelection: str

    enableFirstMenuLevelExtensionDialing: bool

    audioFileDescription: Optional[str] = None

    audioMediaType: Optional[str] = None

    videoFileDescription: Optional[str] = None

    videoMediaType: Optional[str] = None

    keyConfiguration: List[AutoAttendantKeyReadConfiguration19] = field(
        default_factory=list
    )


@dataclass
class ServiceInstanceAddProfileTrunkGroup(ServiceInstanceAddProfile):
    """Service Profile Information for a trunk group.
    The publicUserIdentity element is not part of ServiceInstanceAddProfileTrunkGroup."""

    name: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    password: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    alias: List[str] = field(default_factory=list)

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class ServiceInstanceAddProfileCallCenter(ServiceInstanceAddProfile):
    """Service Profile Information for a call center.
    Password is required."""

    name: str

    callingLineIdLastName: str

    callingLineIdFirstName: str

    password: str

    hiraganaLastName: Optional[str] = None

    hiraganaFirstName: Optional[str] = None

    phoneNumber: Optional[str] = None

    extension: Optional[str] = None

    department: Optional[DepartmentKey] = None

    language: Optional[str] = None

    timeZone: Optional[str] = None

    alias: List[str] = field(default_factory=list)

    publicUserIdentity: Optional[str] = None

    callingLineIdPhoneNumber: Optional[str] = None


@dataclass
class CPEDeviceModifyOptions22V3(OCIType):
    """CPE device's options when used with a modify request.
    The following options are not changeable:
      configType
      systemFileName
      deviceFileFormat"""

    enableMonitoring: Optional[bool] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeModifyOptions22V3
    ] = None


@dataclass
class ReplacementConsolidatedSharedCallAppearanceAccessDeviceMultipleIdentityEndpointList22(
    OCIType
):
    """A list of shared call appearance endpoints that replaces existing endpoints."""

    sharedCallAppearanceAccessDeviceEndpoint: List[
        ConsolidatedSharedCallAppearanceAccessDeviceMultipleIdentityEndpointAdd22
    ] = field(default_factory=list)


@dataclass
class CPEDeviceOptions22V4(OCIType):
    """CPE device's options.

    The field configType is optional to allow the use of field enableMonitoring for all device types being managed or not
    ie. device configuration option equals to DeviceManagement, or Legacy, or Not Supported).

    If the device configuration option is set to \"Not Supported\", the value of configType is forced set to \"None\" regardless
    of its current value.

    It is not allowed to add a device type with device configuration option set to Device Management or Legacy when the configType
    is not set."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptions22V4
    ] = None


@dataclass
class CPEDeviceOptions22V6(OCIType):
    """CPE device's options.

    The field configType is optional to allow the use of field enableMonitoring for all device types being managed or not
    ie. device configuration option equals to DeviceManagement, or Legacy, or Not Supported).

    If the device configuration option is set to \"Not Supported\", the value of configType is forced set to \"None\" regardless
    of its current value.

    It is not allowed to add a device type with device configuration option set to Device Management or Legacy when the configType
    is not set."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptions22V6
    ] = None


@dataclass
class CPEDeviceOptions22V3(OCIType):
    """CPE device's options.

    The field configType is optional to allow the use of field enableMonitoring for all device types being managed or not
    ie. device configuration option equals to DeviceManagement, or Legacy, or Not Supported).

    If the device configuration option is set to \"Not Supported\", the value of configType is forced set to \"None\" regardless
    of its current value.

    It is not allowed to add a device type with device configuration option set to Device Management or Legacy when the configType
    is not set."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptions22V3
    ] = None


@dataclass
class CPEDeviceModifyOptions22V2(OCIType):
    """CPE device's options when used with a modify request.
    The following options are not changeable:
      configType
      systemFileName
      deviceFileFormat"""

    enableMonitoring: Optional[bool] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeModifyOptions22V2
    ] = None


@dataclass
class CPEDeviceOptions22V5(OCIType):
    """CPE device's options.

    The field configType is optional to allow the use of field enableMonitoring for all device types being managed or not
    ie. device configuration option equals to DeviceManagement, or Legacy, or Not Supported).

    If the device configuration option is set to \"Not Supported\", the value of configType is forced set to \"None\" regardless
    of its current value.

    It is not allowed to add a device type with device configuration option set to Device Management or Legacy when the configType
    is not set."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptions22V5
    ] = None


@dataclass
class CPEDeviceOptions22V2(OCIType):
    """CPE device's options.

    The field configType is optional to allow the use of field enableMonitoring for all device types being managed or not
    ie. device configuration option equals to DeviceManagement, or Legacy, or Not Supported).

    If the device configuration option is set to \"Not Supported\", the value of configType is forced set to \"None\" regardless
    of its current value.

    It is not allowed to add a device type with device configuration option set to Device Management or Legacy when the configType
    is not set."""

    enableMonitoring: bool

    configType: Optional[str] = None

    systemFileName: Optional[str] = None

    deviceFileFormat: Optional[str] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeOptions22V2
    ] = None


@dataclass
class ReplacementConsolidatedSharedCallAppearanceAccessDeviceMultipleIdentityEndpointList(
    OCIType
):
    """A list of shared call appearance endpoints that replaces existing endpoints."""

    sharedCallAppearanceAccessDeviceEndpoint: List[
        ConsolidatedSharedCallAppearanceAccessDeviceMultipleIdentityEndpoint
    ] = field(default_factory=list)


@dataclass
class CPEDeviceModifyOptions22(OCIType):
    """CPE device's options when used with a modify request.
    The following options are not changeable:
      configType
      systemFileName
      deviceFileFormat"""

    enableMonitoring: Optional[bool] = None

    deviceManagementDeviceTypeOptions: Optional[
        DeviceManagementDeviceTypeModifyOptions22
    ] = None


@dataclass
class ReplacementCombinedSharedCallAppearanceAccessDeviceMultipleIdentityEndpointList(
    OCIType
):
    """A list of shared call appearance endpoints that replaces existing endpoints."""

    sharedCallAppearanceAccessDeviceEndpoint: List[
        CombinedSharedCallAppearanceAccessDeviceMultipleIdentityEndpoint
    ] = field(default_factory=list)


@dataclass
class CallCenterReportInterval(OCIType):
    """Report interval for call center enhanced reporting scheduled reports."""

    dates: CallCenterReportIntervalDates

    current: CallCenterReportCurrentInterval

    past: CallCenterReportPastInterval


@dataclass
class AutoAttendantKeyConfiguration19(OCIType):
    """The configuration of a key for Auto Attendant."""

    key: str

    entry: AutoAttendantKeyConfigurationEntry19


@dataclass
class AutoAttendantKeyModifyConfiguration(OCIType):
    """The modify configuration of a key for Auto
    Attendant."""

    key: str

    entry: AutoAttendantKeyConfigurationModifyEntry


@dataclass
class PushNotificationRegistrationData23(OCIType):
    """The common push notification registration elements which supports encryption, if required.
    Elements encryptionKeyIdentifier, encryptionAlgorithm and channel are provided only when registration supports encryption.
    Their absence indicates that encryption is not supported."""

    registrationId: str

    applicationId: str

    applicationVersion: str

    deviceOsType: str

    deviceVersion: str

    timestamp: str

    pushNotificationClientVersion: str

    pushNotificationTokenData: List[PushNotificationTokenData23] = field(
        default_factory=list
    )

    encryptionKeyIdentifier: Optional[str] = None

    encryptionAlgorithm: Optional[str] = None

    channel: Optional[str] = None


@dataclass
class CallCenterReportSchedule(OCIType):
    """A schedule for call center enhanced reporting scheduled report. It can either be a fixed time schedule
    or recurring schedule"""

    scheduleTime: CallCenterReportScheduleTime

    recurrence: CallCenterReportScheduleRecurrence


@dataclass
class TrunkAddressingMultipleContactModify(OCIType):
    """Trunk group endpoint that can have multiple contacts.
    alternateTrunkIdentityDomain is only used in XS mode and the AS when deployed in IMS mode.
    Setting alternateTrunkIdentity or alternateTrunkIdentityDomain to nil in XS mode, the other one paremter should be set to nil at the same time.
    The following elements are only used in AS data mode and are ignored in XS data mode:
     physicalLocation"""

    trunkGroupDeviceEndpoint: Optional[
        TrunkGroupDeviceMultipleContactEndpointModify
    ] = None

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None

    alternateTrunkIdentityDomain: Optional[str] = None

    physicalLocation: Optional[str] = None


@dataclass
class TrunkGroupDeviceMultipleContactEndpointModify22(OCIType):
    """Trunk group device endpoint used in the context of modify that can have multiple contacts."""

    name: Optional[str] = None

    linePort: Optional[str] = None

    contactList: Optional[ReplacementContactList22] = None


@dataclass
class AccessDeviceMultipleIdentityAndContactEndpointModify22(OCIType):
    """Access device end point used in the context of modify that can have more than one contact defined.
    The endpoint is identified by its linePort (public Identity) and possibly a private Identity.
    Only Static Registration capable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering.
    The following elements are only used in XS data mode and ignored in AS data mode:
      privateIdentity
    The following elements are only used in AS data mode and ignored in XS data mode:
      useHotline
      hotlineContact"""

    accessDevice: Optional[AccessDevice] = None

    linePort: Optional[str] = None

    privateIdentity: Optional[str] = None

    contactList: Optional[ReplacementContactList22] = None

    portNumber: Optional[int] = None

    useHotline: Optional[bool] = None

    hotlineContact: Optional[str] = None


@dataclass
class AccessDeviceMultipleContactEndpointModify22(OCIType):
    """Access device end point used in the context of modify that can have more than one contact defined.
    Only Static Registration capable devices may have more than one contact defined.
    Port numbers are only used by devices with static line ordering."""

    accessDevice: Optional[AccessDevice] = None

    linePort: Optional[str] = None

    contactList: Optional[ReplacementContactList22] = None

    portNumber: Optional[int] = None


@dataclass
class TrunkAddressingMultipleContactAdd22(OCIType):
    """Trunk group endpoint that can have multiple contacts.
    alternateTrunkIdentityDomain is only used in XS mode and the AS when deployed in IMS mode.
    Both alternateTrunkIdentity and AlternateTrunkIdentityDomain should be set at the same time if one is set in XS mode.
    The following elements are only used in AS data mode and are ignored in XS data mode:
     physicalLocation"""

    trunkGroupDeviceEndpoint: Optional[TrunkGroupDeviceMultipleContactEndpointAdd22] = (
        None
    )

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None

    alternateTrunkIdentityDomain: Optional[str] = None

    physicalLocation: Optional[str] = None


@dataclass
class TrunkAddressingMultipleContactRead22(OCIType):
    """Trunk group endpoint that can have multiple contacts.
    alternateTrunkIdentityDomain is only used in XS mode and the AS when deployed in IMS mode.
    The following elements are only used in AS data mode and are ignored in XS data mode:
      physicalLocation"""

    trunkGroupDeviceEndpoint: Optional[
        TrunkGroupDeviceMultipleContactEndpointRead22
    ] = None

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None

    alternateTrunkIdentityDomain: Optional[str] = None

    physicalLocation: Optional[str] = None


@dataclass
class ReplacementCombinedUserServiceAuthorizationList(OCIType):
    """A list of user services that replaces a previously authorized user services."""

    userServiceAuthorization: List[CombinedUserServiceAuthorization] = field(
        default_factory=list
    )


@dataclass
class ReplacementCombinedServicePackAuthorizationList(OCIType):
    """A list of service packs that replaces previously authorized service packs."""

    servicePackAuthorization: List[CombinedServicePackAuthorization] = field(
        default_factory=list
    )


@dataclass
class ReplacementCombinedUserServiceAssignmentList(OCIType):
    """A list of user services that replaces existing user services assgined to the user.

    If a service is already assigned to the user, the service quantitiy will be updated if included."""

    serviceName: List[CombinedUserServiceAssignment] = field(default_factory=list)


@dataclass
class ReplacementCombinedGroupServiceAuthorizationList(OCIType):
    """A list of group services that replaces a previously authorized group services."""

    groupServiceAuthorization: List[CombinedGroupServiceAuthorization] = field(
        default_factory=list
    )


@dataclass
class ReplacementConsolidatedUserServiceAssignmentList(OCIType):
    """A list of user services that replaces existing user services assigned to the user.
    If a service is not authorized to the group, the service will be authorized. The authorizedQuantity will be used if provided; otherwise, the service quantity will be set to unlimited. The command will fail if the authorized Quantity set at the service provider is insufficient.
    If a service is already authorized to the group, the service quantity will be ignored if included."""

    userServiceServiceName: List[ConsolidatedUserServiceAssignment] = field(
        default_factory=list
    )


@dataclass
class ReplacementCombinedServicePackAssignmentList(OCIType):
    """A list of service packs that replaces existing service packs assgined to the user.

    If a service pack is already assigned to the user, the service quantitiy will be updated if included."""

    servicePack: List[CombinedServicePackAssignment] = field(default_factory=list)


@dataclass
class ReplacementConsolidatedServicePackAssignmentList(OCIType):
    """A list of service packs that replaces existing service packs assigned to the user.
    If a service pack is not authorized to the group, the service will be authorized. The authorizedQuantity will be used if provided; otherwise, the service quantity will be set to unlimited. The command will fail if the authorized Quantity set at the service provider is insufficient
    If a service pack is already authorized to the group, the service quantity will be ignored if included."""

    servicePack: List[ConsolidatedServicePackAssignment] = field(default_factory=list)


@dataclass
class ConsolidatedGroupProperties(OCIType):
    """"""

    defaultDomain: str

    userLimit: int

    groupName: Optional[str] = None

    callingLineIdName: Optional[str] = None

    timeZone: Optional[str] = None

    locationDialingCode: Optional[str] = None

    contact: Optional[Contact] = None

    address: Optional[StreetAddress] = None

    networkClassOfService: List[str] = field(default_factory=list)

    defaultNetworkClassOfService: Optional[DefaultNetworkClassOfService] = None

    groupService: List[ConsolidatedGroupServiceAssignment] = field(default_factory=list)

    servicePolicy: Optional[str] = None


@dataclass
class EnhancedCallLogsNumberFilter(OCIType):
    """Filter criteria based on the called number or number called."""

    includeBasicCallType: List[str] = field(default_factory=list)

    includeCallCategory: List[str] = field(default_factory=list)

    includeConfigurableCallType: List[str] = field(default_factory=list)

    searchCriteriaDialedNumber: List[SearchCriteriaOutgoingDNorSIPURI] = field(
        default_factory=list
    )

    searchCriteriaCalledNumber: List[SearchCriteriaOutgoingDNorSIPURI] = field(
        default_factory=list
    )

    searchCriteriaNetworkTranslatedNumber: List[SearchCriteriaOutgoingDNorSIPURI] = (
        field(default_factory=list)
    )

    searchCriteriaCallingPresentationNumber: List[SearchCriteriaOutgoingDNorSIPURI] = (
        field(default_factory=list)
    )


@dataclass
class EnhancedCallLogsRedirectedNumberFilter23(OCIType):
    """Filter criteria based on the transferred/forwarded number."""

    redirectedCall: EnhancedCallLogsRedirectedCallSelection23

    includeServiceInvocationBasicCallType: List[str] = field(default_factory=list)

    includeServiceInvocationCallCategory: List[str] = field(default_factory=list)

    includeServiceInvocationConfigurableCallType: List[str] = field(
        default_factory=list
    )

    searchCriteriaServiceInvocationDialedNumber: List[
        SearchCriteriaOutgoingDNorSIPURI
    ] = field(default_factory=list)

    searchCriteriaServiceInvocationCalledNumber: List[
        SearchCriteriaOutgoingDNorSIPURI
    ] = field(default_factory=list)

    searchCriteriaServiceInvocationNetworkTranslatedNumber: List[
        SearchCriteriaOutgoingDNorSIPURI
    ] = field(default_factory=list)


@dataclass
class SortOrderServiceProviderAdminGetPagedSortedList(OCIType):
    """Used to sort the ServiceProviderAdminGetPagedSortedListRequest request."""

    sortByAdminId: SortByAdminId

    sortByAdminLastName: SortByAdminLastName

    sortByAdminFirstName: SortByAdminFirstName


@dataclass
class SortOrderGroupAdminGetPagedSortedList(OCIType):
    """Used to sort the GroupAdminGetPagedSortedListRequest request."""

    sortByAdminId: SortByAdminId

    sortByAdminLastName: SortByAdminLastName

    sortByAdminFirstName: SortByAdminFirstName


@dataclass
class SortOrderGroupGetListInServiceProviderPagedSortedList(OCIType):
    """Used to sort the GroupGetListInServiceProviderPagedSortedListRequest request."""

    sortByGroupId: SortByGroupId

    sortByGroupName: SortByGroupName


@dataclass
class SortOrderGroupCallCenterAgentThresholdProfileGetPagedSorted(OCIType):
    """Used to sort the GroupCallCenterAgentThresholdProfileGetPagedSortedRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByEmailAddress: SortByEmailAddress


@dataclass
class SortOrderGroupCallCenterGetAvailableAgentPagedSortedList(OCIType):
    """Used to sort the GroupCallCenterGetAvailableAgentPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByEmailAddress: SortByEmailAddress


@dataclass
class SortOrderGroupCollaborateBridgeGetAvailableUserPagedSortedList(OCIType):
    """Used to sort the GroupCollaborateBridgeGetAvailableUserPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension


@dataclass
class SortOrderGroupCollaborateBridgeGetInstancePagedSortedList(OCIType):
    """Used to sort the GroupCollaborateBridgeGetInstancePagedSortedListRequest."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByDn: SortByDn

    sortByExtension: SortByExtension


@dataclass
class SortOrderGroupAutoAttendantGetInstancePagedSortedList(OCIType):
    """Used to sort the GroupAutoAttendantGetInstancePagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByDn: SortByDn

    sortByExtension: SortByExtension


@dataclass
class SortOrderGroupPhoneDirectoryGetPagedSortedList(OCIType):
    """Used to sort the GroupPhoneDirectoryGetPagedSortedListRequest request."""

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByMobilePhoneNumber: SortByMobilePhoneNumber

    sortByEmailAddress: SortByEmailAddress

    sortByDepartmentName: SortByDepartmentName

    sortByYahooId: SortByYahooId

    sortByUserId: SortByUserId

    sortByImpId: SortByImpId


@dataclass
class SortOrderUserGetListInGroupPagedSortedList(OCIType):
    """Used to sort the UserGetListInGroupPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDepartmentName: SortByDepartmentName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByEmailAddress: SortByEmailAddress


@dataclass
class SortOrderGroupCallParkGetAvailableAlternateRecallUserPagedSortedList(OCIType):
    """Used to sort the GroupCallParkGetAvailableAlternateRecallUserPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName


@dataclass
class SortOrderGroupCallPickupGetInstancePagedSorted(OCIType):
    """Used to sort the GroupCallPickupGetInstancePagedSortedRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByEmailAddress: SortByEmailAddress


@dataclass
class SortOrderEnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAssignmentPagedSortedList(
    OCIType
):
    """Used to sort the SortOrderEnterpriseBroadWorksMobilityMobileSubscriberDirectoryNumberGetAssignmentPagedSortedListRequest."""

    sortByMobileDirectoryNumber: SortByMobileDirectoryNumber

    sortByDn: SortByDn

    sortByDepartmentName: SortByDepartmentName

    sortByUserId: SortByUserId

    sortByUserFirstName: SortByUserFirstName

    sortByUserLastName: SortByUserLastName

    sortByExtension: SortByExtension

    sortByDnAvailable: SortByDnAvailable


@dataclass
class SortOrderEnterpriseCallCenterAgentThresholdProfileGetAvailableAgentPagedSortedList(
    OCIType
):
    """Used to sort the EnterpriseCallCenterAgentThresholdProfileGetAvailableAgentPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByEmailAddress: SortByEmailAddress

    sortByAgentThresholdProfile: SortByAgentThresholdProfile


@dataclass
class SortOrderGroupDnGetAssignmentPagedSortedList(OCIType):
    """Used to sort the GroupDnGetAssignmentPagedSortedListRequest request."""

    sortByDn: SortByDn

    sortByDepartmentName: SortByDepartmentName

    sortByDnActivated: SortByDnActivated

    sortByDnAvailable: SortByDnAvailable

    sortByUserId: SortByUserId

    sortByUserFirstName: SortByUserFirstName

    sortByUserLastName: SortByUserLastName

    sortByExtension: SortByExtension

    sortByEmailAddress: SortByEmailAddress


@dataclass
class SortOrderEnterpriseCallCenterAgentThresholdProfileGetPagedSorted(OCIType):
    """Used to sort the EnterpriseCallCenterAgentThresholdProfileGetPagedSortedRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByEmailAddress: SortByEmailAddress


@dataclass
class SortOrderGroupHuntGroupGetInstancePagedSortedList(OCIType):
    """Used to sort the GroupHuntGroupGetInstancePagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByDn: SortByDn

    sortByExtension: SortByExtension


@dataclass
class SortOrderGroupCallCenterAgentThresholdProfileGetAvailableAgentPagedSortedList(
    OCIType
):
    """Used to sort the GroupCallCenterAgentThresholdProfileGetAvailableAgentPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByEmailAddress: SortByEmailAddress

    sortByAgentThresholdProfile: SortByAgentThresholdProfile


@dataclass
class SortOrderGroupCallPickupGetAvailableUserPagedSortedList(OCIType):
    """Used to sort the GroupCallPickupGetAvailableUserPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByEmailAddress: SortByEmailAddress


@dataclass
class SortOrderGroupHuntGroupGetAvailableUserPagedSortedList(OCIType):
    """Used to sort the GroupHuntGroupGetAvailableUserPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension


@dataclass
class SortOrderGroupCallParkGetAvailableUserPagedSortedList(OCIType):
    """Used to sort the GroupCallParkGetAvailableUserPagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByEmailAddress: SortByEmailAddress


@dataclass
class SortOrderEnterprisePhoneDirectoryGetPagedSortedList(OCIType):
    """Used to sort the EnterprisePhoneDirectoryGetPagedSortedListRequest request."""

    sortByUserLastName: SortByUserLastName

    sortByUserFirstName: SortByUserFirstName

    sortByGroupLocationCode: SortByGroupLocationCode

    sortByMobilePhoneNumber: SortByMobilePhoneNumber

    sortByEmailAddress: SortByEmailAddress

    sortByDepartmentName: SortByDepartmentName

    sortByGroupName: SortByGroupName

    sortByYahooId: SortByYahooId

    sortByUserId: SortByUserId

    sortByImpId: SortByImpId


@dataclass
class SortOrderServiceProviderGetPagedSortedList(OCIType):
    """Used to sort the ServiceProviderGetPagedSortedListRequest request."""

    sortByServiceProviderId: SortByServiceProviderId

    sortByServiceProviderName: SortByServiceProviderName


@dataclass
class SortOrderGroupAccessDeviceGetPagedSortedList(OCIType):
    """Used to sort the GroupAccessDeviceGetPagedSortedListRequest request."""

    sortByDeviceName: SortByDeviceName

    sortByDeviceType: SortByDeviceType

    sortByDeviceNetAddress: SortByDeviceNetAddress

    sortByDeviceMACAddress: SortByDeviceMACAddress


@dataclass
class SortOrderGroupCallCenterGetInstancePagedSortedList(OCIType):
    """Used to sort the GroupCallCenterGetInstancePagedSortedListRequest request."""

    sortByUserId: SortByUserId

    sortByCallCenterName: SortByCallCenterName

    sortByDn: SortByDn

    sortByExtension: SortByExtension

    sortByDepartmentName: SortByDepartmentName

    sortByHuntPolicy: SortByHuntPolicy

    sortByCallCenterType: SortByCallCenterType


@dataclass
class OutgoingCallingPlanDigitPatternCallMeNowDepartmentPermissionsModify(OCIType):
    """Modify outgoing Calling Plan Call Me Now call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    digitPatternPermissions: OutgoingCallingPlanDigitPatternCallMeNowPermissions


@dataclass
class OutgoingCallingPlanDigitPatternCallMeNowDepartmentPermissions(OCIType):
    """Outgoing Calling Plan Call Me Now call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    departmentName: str

    digitPatternPermissions: OutgoingCallingPlanDigitPatternCallMeNowPermissions


@dataclass
class OutgoingCallingPlanDigitPatternOriginatingDepartmentPermissions(OCIType):
    """Outgoing Calling Plan originating call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    departmentName: str

    digitPatternPermissions: OutgoingCallingPlanDigitPatternOriginatingPermissions


@dataclass
class OutgoingCallingPlanDigitPatternOriginatingDepartmentPermissionsModify(OCIType):
    """Modify outgoing Calling Plan originating call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    digitPatternPermissions: OutgoingCallingPlanDigitPatternOriginatingPermissions


@dataclass
class OutgoingCallingPlanDigitPatternRedirectingDepartmentPermissionsModify(OCIType):
    """Modify outgoing Calling Plan redirecting call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    digitPatternPermissions: OutgoingCallingPlanDigitPatternRedirectingPermissions


@dataclass
class OutgoingCallingPlanDigitPatternRedirectingDepartmentPermissions(OCIType):
    """Outgoing Calling Plan redirecting call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    departmentName: str

    digitPatternPermissions: OutgoingCallingPlanDigitPatternRedirectingPermissions


@dataclass
class OutgoingPinholeDigitPlanDigitPatternCallMeNowDepartmentPermissionsModify(OCIType):
    """Modify Outgoing Pinhole Digit Plan Call Me Now call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    digitPatternPermissions: OutgoingPinholeDigitPlanDigitPatternCallMeNowPermissions


@dataclass
class OutgoingPinholeDigitPlanDigitPatternCallMeNowDepartmentPermissions(OCIType):
    """Outgoing Pinhole Digit Plan Call Me Now call permissions for a department."""

    departmentKey: DepartmentKey

    departmentName: str

    permissions: OutgoingPinholeDigitPlanDigitPatternCallMeNowPermissions


@dataclass
class OutgoingPinholeDigitPlanDigitPatternOriginatingDepartmentPermissionsModify(
    OCIType
):
    """Modify Outgoing Pinhole Digit Plan originating call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    digitPatternPermissions: OutgoingPinholeDigitPlanDigitPatternOriginatingPermissions


@dataclass
class OutgoingPinholeDigitPlanDigitPatternOriginatingDepartmentPermissions(OCIType):
    """Outgoing Pinhole Digit Plan department originating call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    departmentName: str

    digitPatternPermissions: OutgoingPinholeDigitPlanDigitPatternOriginatingPermissions


@dataclass
class OutgoingPinholeDigitPlanDigitPatternRedirectingDepartmentPermissions(OCIType):
    """Outgoing Pinhole Digit Plan initiating call forwards/transfer permissions for a department."""

    departmentKey: DepartmentKey

    departmentName: str

    permissions: OutgoingPinholeDigitPlanDigitPatternRedirectingPermissions


@dataclass
class OutgoingPinholeDigitPlanDigitPatternRedirectingDepartmentPermissionsModify(
    OCIType
):
    """Modify Outgoing Pinhole Digit Plan redirecting call permissions for specified digit patterns."""

    departmentKey: DepartmentKey

    digitPatternPermissions: OutgoingPinholeDigitPlanDigitPatternRedirectingPermissions


@dataclass
class ReplacementEnterpriseEnterpriseTrunkPriorityWeightedTrunkGroupList(OCIType):
    """A list of enterprise trunk priority weighted trunk groups that replaces a previously configured list.
    By convention, an element of this type may be set nill to clear the list."""

    trunkGroup: List[EnterpriseEnterpriseTrunkPriorityWeightedTrunkGroup] = field(
        default_factory=list
    )


@dataclass
class ProfileAndServiceBusyLampFieldInfo(OCIType):
    """This is the configuration parameters for Busy Lamp Field service
    The monitoredUserTable has column headings:
    \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\", \"Hiragana First Name\",
    \"Phone Number\", \"Extension\", \"Department\", \"Email Address\", \"IMP Id\"."""

    enableCallParkNotification: bool

    monitoredUserTable: OCITable

    listURI: Optional[str] = None


@dataclass
class CallCenterScheduledReportAgentSelectionRead(OCIType):
    """Either all agents or list of agents.
    The agent table has the following column headings:
    \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\" and \"Hiragana First Name\"."""

    allAgent: bool

    agentTable: OCITable


@dataclass
class ProfileAndServiceSimultaneousRingPersonalInfo(OCIType):
    """This is the configuration parameters for Simultaneous Ring Personal  service

    Contains a criteria table with column heading: \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Holiday Schedule\", \"Calls From\" and \"Blacklisted\".

    The \"Calls From\" column is a string containing call numbers"""

    isActive: bool

    doNotRingIfOnCall: bool

    criteriaTable: OCITable

    simultaneousRingNumber: List[SimultaneousRingNumber] = field(default_factory=list)


@dataclass
class ProfileAndServiceCommunicationBarringUserControlInfo(OCIType):
    """This is the configuration parameters for Communication Barring User Control service

    profileTable has column headings: \"Name\", \"Code\", \"Activated\" and \"Primary\"."""

    lockoutStatus: bool

    profileTable: OCITable


@dataclass
class ProfileAndServiceSharedCallAppearanceInfo(OCIType):
    """This is the configuration parameters for shared call appearance service
    The endpointTable contains columns:
      \"Device Level\", \"Device Name\", \"Device Type\", \"Line/Port\", \"SIP Contact\", \"Port Number\". \"Private Identity\" .

    The \"Device Level\" column contains one of the AccessDeviceLevel enumerated constants.
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

    useUserPrimaryWithAlternateCallsSetting: bool

    allowSimultaneousPrimaryAndAlternate: bool

    restrictCallRetrieveOfPrimary: bool

    restrictCallBridgingOfPrimary: bool


@dataclass
class ProfileAndServiceSelectiveCallRejectionInfo(OCIType):
    """This is the configuration parameters for Selective Call Rejection service

    The criteria table's column headings are:
    \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Blacklisted\", \"Holiday Schedule\"

    The \"Calls From\" column is a string containing call numbers"""

    criteriaTable: OCITable


@dataclass
class CallCenterScheduledReportAgentSelectionAdminRead(OCIType):
    """Either all agents or 2 list of agents: one for current and one for past (deleted) agents.
    This is used when an admin reads a Scheduled Report.
    Each agent table has the following column headings:
    \"User Id\", \"Last Name\", \"First Name\", \"Hiragana Last Name\" and \"Hiragana First Name\"."""

    allAgent: bool

    currentAgentTable: OCITable

    pastAgentTable: OCITable


@dataclass
class ProfileAndServiceCustomRingbackInfo(OCIType):
    """This is the configuration parameters for Custom Ringback service

    The criteria table's column headings are: \"Is Active\", \"Criteria Name\",
    \"Time Schedule\", \"Calls From\", \"Blacklisted\", \"Holiday Schedule\".

    The \"Calls From\" column is a string containing call numbers"""

    criteriaTable: OCITable


@dataclass
class ProfileAndServiceCallForwardingSelectiveInfo(OCIType):
    """This is the configuration parameters for Call Forwarding Selective service

    The criteria table's column headings are:
            \"Is Active\", \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Forward To\", \"Blacklisted\", \"Holiday Schedule\"

            The \"Calls From\" column is a string containing call numbers"""

    isActive: bool

    playRingReminder: bool

    criteriaTable: OCITable

    defaultForwardToPhoneNumber: Optional[str] = None


@dataclass
class ProfileAndServicePreAlertingAnnouncementInfo(OCIType):
    """This is the configuration parameters for Pre Alerting Announcement service

    The criteria table's column headings are: \"Is Active\", \"Criteria Name\",
    \"Blacklisted\", and \"Calls From\".

    The \"Calls From\" column is a string containing call numbers"""

    isActive: bool

    audioSelection: str

    videoSelection: str

    criteriaTable: OCITable

    audioFileDescription: Optional[str] = None

    audioMediaType: Optional[str] = None

    audioFileUrl: Optional[str] = None

    videoFileDescription: Optional[str] = None

    videoMediaType: Optional[str] = None

    videoFileUrl: Optional[str] = None


@dataclass
class ProfileAndServiceCallNotifyInfo(OCIType):
    """This is the configuration parameters for Call Notify service

    The criteria table's column headings are: \"Is Active\",
    \"Criteria Name\", \"Time Schedule\", \"Calls From\", \"Blacklisted\" ,\"Holiday Schedule\"

    The \"Calls From\" column is a string containing call numbers"""

    criteriaTable: OCITable

    callNotifyEmailAddress: Optional[str] = None


@dataclass
class AutoAttendantModifyMenu20(OCIType):
    """The configuration of the automated receptionist greeting
    prompt and dialing menu to be used during business hours.
    It is used when modifying an Auto Attendant group."""

    announcementSelection: Optional[str] = None

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    enableFirstMenuLevelExtensionDialing: Optional[bool] = None

    keyConfiguration: List[AutoAttendantKeyModifyConfiguration20] = field(
        default_factory=list
    )


@dataclass
class AutoAttendantReadMenu20(OCIType):
    """The configuration of the automated receptionist greeting
    prompt and dialing menu to be used during after business hours."""

    announcementSelection: str

    enableFirstMenuLevelExtensionDialing: bool

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    keyConfiguration: List[AutoAttendantKeyReadConfiguration20] = field(
        default_factory=list
    )


@dataclass
class AutoAttendantAddMenu20(OCIType):
    """The configuration of the automated receptionist greeting
    prompt and dialing menu to be used during after business hours."""

    announcementSelection: str

    enableFirstMenuLevelExtensionDialing: bool

    audioFile: Optional[AnnouncementFileLevelKey] = None

    videoFile: Optional[AnnouncementFileLevelKey] = None

    keyConfiguration: List[AutoAttendantKeyConfiguration20] = field(
        default_factory=list
    )


@dataclass
class AutoAttendantAddMenu19(OCIType):
    """The configuration of the automated receptionist
    greeting
    prompt and dialing menu to be used during
    after business
    hours."""

    announcementSelection: str

    enableFirstMenuLevelExtensionDialing: bool

    audioFile: Optional[LabeledMediaFileResource] = None

    videoFile: Optional[LabeledMediaFileResource] = None

    keyConfiguration: List[AutoAttendantKeyConfiguration19] = field(
        default_factory=list
    )


@dataclass
class AutoAttendantModifyMenu16(OCIType):
    """The configuration of the automated receptionist
    greeting
    prompt and dialing menu to be used during
    business
    hours.
    It is used when modifying an Auto Attendant group."""

    announcementSelection: Optional[str] = None

    audioFile: Optional[LabeledMediaFileResource] = None

    videoFile: Optional[LabeledMediaFileResource] = None

    enableFirstMenuLevelExtensionDialing: Optional[bool] = None

    keyConfiguration: List[AutoAttendantKeyModifyConfiguration] = field(
        default_factory=list
    )


@dataclass
class TrunkAddressingMultipleContactModify22(OCIType):
    """Trunk group endpoint that can have multiple contacts.
    alternateTrunkIdentityDomain is only used in XS mode and the AS when deployed in IMS mode. .
    Setting alternateTrunkIdentity or alternateTrunkIdentityDomain to nil in XS mode, the other one paremter should be set to nil at the same time.
    The following elements are only used in AS data mode and are ignored in XS data mode:
     physicalLocation"""

    trunkGroupDeviceEndpoint: Optional[
        TrunkGroupDeviceMultipleContactEndpointModify22
    ] = None

    enterpriseTrunkName: Optional[str] = None

    alternateTrunkIdentity: Optional[str] = None

    alternateTrunkIdentityDomain: Optional[str] = None

    physicalLocation: Optional[str] = None
