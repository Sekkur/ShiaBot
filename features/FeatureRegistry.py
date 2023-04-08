from FeatureManager import FeatureManager
from features.admin.approval.ApprovalConfig import ApprovalConfig
from features.admin.approval.ApprovalFeature import ApprovalFeature
from utils.config.ConfigRegistry import ConfigRegistry
from .admin.AdminConfig import AdminConfig
from utils.InstanceStorage import InstanceStorage

def loadAll():
	storage = InstanceStorage()
	feature_manager = storage.get(FeatureManager.__class__.__name__)
	config_registry = storage.get(FeatureManager.__class__.__name__)
	if isinstance(FeatureManager, feature_manager) and isinstance(ConfigRegistry, config_registry):
		config = config_registry.configs.get(AdminConfig.name)
		if isinstance(config, AdminConfig):
			loadApproval(feature_manager, config_registry)
		else:
			print("ERROR: AdminConfig not loaded properly.")
	else:
		print("ERROR: FeatureManager/Config registry not loaded properly.")


def loadApproval(featureManager: FeatureManager, configRegistry: ConfigRegistry):
	config = configRegistry.configs.get(ApprovalConfig.name)
	if isinstance(config, ApprovalConfig):
		featureManager.add(ApprovalFeature(config))
