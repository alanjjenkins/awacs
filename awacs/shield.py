# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Shield"
prefix = "shield"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateDRTLogBucket = Action("AssociateDRTLogBucket")
AssociateDRTRole = Action("AssociateDRTRole")
CreateProtection = Action("CreateProtection")
CreateSubscription = Action("CreateSubscription")
DeleteProtection = Action("DeleteProtection")
DeleteSubscription = Action("DeleteSubscription")
DescribeAttack = Action("DescribeAttack")
DescribeDRTAccess = Action("DescribeDRTAccess")
DescribeEmergencyContactSettings = Action("DescribeEmergencyContactSettings")
DescribeProtection = Action("DescribeProtection")
DescribeSubscription = Action("DescribeSubscription")
DisassociateDRTLogBucket = Action("DisassociateDRTLogBucket")
DisassociateDRTRole = Action("DisassociateDRTRole")
GetSubscriptionState = Action("GetSubscriptionState")
ListAttacks = Action("ListAttacks")
ListProtections = Action("ListProtections")
UpdateEmergencyContactSettings = Action("UpdateEmergencyContactSettings")
UpdateSubscription = Action("UpdateSubscription")
