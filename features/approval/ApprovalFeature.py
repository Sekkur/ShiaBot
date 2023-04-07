import discord
from features.Feature import Feature
from features.approval.ApprovalCog import ApprovalCog
from features.approval.ApprovalConfig import ApprovalConfig


class ApprovalFeature(Feature):
    def __init__(self, config: ApprovalConfig):
        self.config = config
        cogs = [ApprovalCog()]
        super().__init__("Approval", "Handle member join approvals automatically", cogs)

    def open_ticket(self):
        pass
