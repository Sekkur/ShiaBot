from features.Feature import Feature
from features.members.approval.ApprovalCog import ApprovalCog
from utils import common
from features.members.approval.types.ApprovalChannelTypes import ApprovalChannelType

class ApprovalFeature(Feature):
    def __init__(self):
        cogs = [ApprovalCog()]
        super().__init__("Approval", "Handle member join approvals automatically", cogs)

    def open_ticket(self):
        channel = common.config.get("members").get("approval").get("verifyButtonChannel")
        if channel == ApprovalChannelType.dm:
            pass
        else:
            pass
