from Singleton import Singleton


class InstanceStorage(Singleton):
    def __init__(self):
        self.objects = dict[str, object]()

    def add(self, obj: object):
        self.objects.update({obj.__class__.__name__: obj})

    def get(self, obj: object):
        return self.objects.get(obj.__class__.__name__)