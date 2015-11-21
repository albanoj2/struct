import abc


class Parser (object):

    def __init__(self, project_root_dir):
        # Create a stub to store the parsed project
        self._project = None
        self._project_root_dir = project_root_dir

    @abc.abstractmethod
    def parse(self):
        pass

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, project):
        self._project = project

    @property
    def project_root_dir(self):
        return self._project

    @project_root_dir.setter
    def project_root_dir(self, dir):
        self._project = dir