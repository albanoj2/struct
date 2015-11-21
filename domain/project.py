class Project (object):

    def __init__(self):
        # Create the contained objects in the project
        self._dependencies = None

    @property
    def dependencies(self):
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        self._dependencies = dependencies