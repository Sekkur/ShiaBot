from .Feature import Feature
from utils.config.ConfigRegistry import ConfigRegistry
from utils.Singleton import Singleton
import FeatureRegistry

class FeatureManager(Singleton):
    def __init__(self):
        self.features = dict[str, Feature]()
        FeatureRegistry.loadAll()

    def add(self, feature: Feature):
        self.features.update({feature.name: feature})

    def getAll(self) -> dict[str, Feature]:
        return self.features
