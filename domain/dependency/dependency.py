import abc
import os


class Dependency (object):

    @abc.abstractmethod
    def pull_into_project(self):
        pass


class CompositeDependency (Dependency):

    def __init__(self):
        # Create a list to store the dependencies
        self._dependencies = []

    def add_dependency(self, dependency):
        # Add the dependency to the list of dependencies
        self._dependencies.append(dependency)

    def remove_dependency(self, dependency):
        # Remove the dependency from the list of dependencies
        self._dependencies.remove(dependency)

    @property
    def dependencies(self):
        return self._dependencies

    def pull_into_project(self):

        for dependency in self._dependencies:
            # Pull in each dependency from the list of dependencies
            dependency.pull_into_project()


class DependencyRoot (CompositeDependency):

    def __init__(self, project_root_dir):
        CompositeDependency.__init__(self)

        # Store the dependency configuration information
        self._project_root_dir = project_root_dir

    def pull_into_project(self):

        # Compute the name of the dependency directory
        dependency_dir = os.path.join(self._project_root_dir, 'dependencies')

        if not os.path.isdir(dependency_dir):
            # The dependency directory does not yet exist, so it must be created
            os.makedirs(dependency_dir)

        # Perform the default logic
        super(CompositeDependency, self).pull_into_project()