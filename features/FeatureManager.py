from .Feature import Feature
from features.approval.ApprovalFeature import ApprovalFeature
from utils.config.ConfigRegistry import ConfigRegistry
from utils.Singleton import Singleton
import FeatureRegistry

class FeatureManager(Singleton):
    def __init__(self):
        self.features = dict[str, Feature]()
        configreg = ConfigRegistry()
        FeatureRegistry.loadApproval(self, configreg)

    def add(self, feature: Feature):
        self.features.update({feature.name: feature})

    def getAll(self) -> dict[str, Feature]:
        return self.features
