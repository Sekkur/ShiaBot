from .Feature import Feature


class FeatureManager:
    def __init__(self):
        self.features = dict[str, Feature]()

    def add(self, feature: Feature):
        self.features.update({feature.name: feature})

    def getAll(self) -> dict[str, Feature]:
        return self.features
