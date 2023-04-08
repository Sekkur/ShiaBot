import json
from dataclasses import dataclass

from utils.config.Config import Config
from .approval.ApprovalConfig import ApprovalConfig


@dataclass
class AdminConfig(Config):
    name = "admin"

    def __init__(self, admin: str, approvalConfig: ApprovalConfig):
        self.approvalConfig = approvalConfig
        super().__init__(AdminConfig.name)

    @classmethod
    def from_json(cls, json_string: str):
        data = json.loads(json_string)
        return cls(**data)
