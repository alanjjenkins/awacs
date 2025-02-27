# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Chatbot"
prefix = "chatbot"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateChimeWebhookConfiguration = Action("CreateChimeWebhookConfiguration")
CreateSlackChannelConfiguration = Action("CreateSlackChannelConfiguration")
DeleteChimeWebhookConfiguration = Action("DeleteChimeWebhookConfiguration")
DeleteSlackChannelConfiguration = Action("DeleteSlackChannelConfiguration")
DescribeChimeWebhookConfigurations = Action("DescribeChimeWebhookConfigurations")
DescribeSlackChannelConfigurations = Action("DescribeSlackChannelConfigurations")
DescribeSlackChannels = Action("DescribeSlackChannels")
DescribeSlackWorkspaces = Action("DescribeSlackWorkspaces")
GetSlackOauthParameters = Action("GetSlackOauthParameters")
RedeemSlackOauthCode = Action("RedeemSlackOauthCode")
UpdateChimeWebhookConfiguration = Action("UpdateChimeWebhookConfiguration")
UpdateSlackChannelConfiguration = Action("UpdateSlackChannelConfiguration")
