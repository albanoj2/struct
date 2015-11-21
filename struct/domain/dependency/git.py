from struct.domain.dependency.depedency import Dependency


class GitDependency (Dependency):

    def __init__(self, url):
        # Store the data for the dependency
        self._url = url

    def pull_into_project(self):
        print('Found Git dependency: {}'.format(self._url))

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url
