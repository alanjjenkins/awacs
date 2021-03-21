# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Elemental Support Cases"
prefix = "elemental-support-cases"


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource="", region="", account=""):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region, account=account)


CreateCase = Action("CreateCase")
GetCase = Action("GetCase")
GetCases = Action("GetCases")
UpdateCase = Action("UpdateCase")
