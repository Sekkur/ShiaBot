from FeatureManager import FeatureManager
from utils.config.ConfigRegistry import ConfigRegistry
from approval.ApprovalConfig import ApprovalConfig
from approval.ApprovalFeature import ApprovalFeature


def loadApproval(featureManager: FeatureManager, configRegistry: ConfigRegistry):
    config = configRegistry.configs.get(ApprovalConfig.name)
    if isinstance(config, ApprovalConfig):
        featureManager.add(ApprovalFeature(config))
