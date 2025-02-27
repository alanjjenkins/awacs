# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CloudHSM"
prefix = "cloudhsm"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddTagsToResource = Action("AddTagsToResource")
CopyBackupToRegion = Action("CopyBackupToRegion")
CreateCluster = Action("CreateCluster")
CreateHapg = Action("CreateHapg")
CreateHsm = Action("CreateHsm")
CreateLunaClient = Action("CreateLunaClient")
DeleteBackup = Action("DeleteBackup")
DeleteCluster = Action("DeleteCluster")
DeleteHapg = Action("DeleteHapg")
DeleteHsm = Action("DeleteHsm")
DeleteLunaClient = Action("DeleteLunaClient")
DescribeBackups = Action("DescribeBackups")
DescribeClusters = Action("DescribeClusters")
DescribeHapg = Action("DescribeHapg")
DescribeHsm = Action("DescribeHsm")
DescribeLunaClient = Action("DescribeLunaClient")
GetConfig = Action("GetConfig")
InitializeCluster = Action("InitializeCluster")
ListAvailableZones = Action("ListAvailableZones")
ListHapgs = Action("ListHapgs")
ListHsms = Action("ListHsms")
ListLunaClients = Action("ListLunaClients")
ListTags = Action("ListTags")
ListTagsForResource = Action("ListTagsForResource")
ModifyHapg = Action("ModifyHapg")
ModifyHsm = Action("ModifyHsm")
ModifyLunaClient = Action("ModifyLunaClient")
RemoveTagsFromResource = Action("RemoveTagsFromResource")
RestoreBackup = Action("RestoreBackup")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
