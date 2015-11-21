import os
import xml.etree.ElementTree

from struct.configparser.parser import Parser
from struct.domain.project import Project
from struct.domain.dependency.depedency import Dependency, DependencyRoot
from struct.domain.dependency.git import GitDependency


class XmlParser (Parser):

    def __init__(self, project_root_dir):
        Parser.__init__(self, project_root_dir)

        # Store the path of the XML file
        self._xml_file_path = os.path.join(project_root_dir, 'struct.xml')

        # Create the parser context
        self._context = XmlParserContext()
        self._context.project_root_dir = project_root_dir

    def parse(self):
        # Obtain the XML root from the XML file
        xml_root = xml.etree.ElementTree.parse(self._xml_file_path).getroot()

        # Delegate to the main parsing method
        self.__parse_from_xml_root(xml_root)

    def __parse_from_xml_root(self, xml_root):

        # Create a project object to be configured through parsing
        self.project = Project()

        # Delegate parsing to the project parser
        XmlProjectParser(self._context).parse(xml_root, self.project)


class XmlParserContext (object):

    def __init__(self):
        # Create stubs for the context information
        self._project_root_dir = None

    @property
    def project_root_dir(self):
        return self._project_root_dir

    @project_root_dir.setter
    def project_root_dir(self, root_dir):
        self._project_root_dir = root_dir


class XmlComponentParser (object):

    def __init__(self, context):
        # Store the context
        self._context = context

    @property
    def context(self):
        return self._context


class InvalidXmlConfigurationElement (Exception):
    pass


class XmlProjectParser (XmlComponentParser):

    def __init__(self, context):
        XmlComponentParser.__init__(self, context)

    def parse(self, xml_obj, project):

        for element in xml_obj:
            # Iterate through each of the elements

            if element.tag == 'dependencies':
                # Dependencies element found
                XmlDependenciesParser(self.context).parse(element, project)
            else:
                # Invalid element found
                raise InvalidXmlConfigurationElement()


class XmlDependenciesParser (XmlComponentParser):

    def __init__(self, context):
        XmlComponentParser.__init__(self, context)

    def parse(self, xml_obj, project_obj):

        # Add the root dependencies element to the project
        project_obj.dependencies = DependencyRoot(self.context.project_root_dir)

        for element in xml_obj:
            # Iterate through each of the elements

            if element.tag == 'dependency':
                # Dependency element found
                XmlDependencyParser(self.context).parse(element, project_obj.dependencies)
            else:
                # Invalid element found
                raise InvalidXmlConfigurationElement()


class XmlDependencyParser (XmlComponentParser):

    def __init__(self, context):
        XmlComponentParser.__init__(self, context)

    def parse(self, xml_obj, dependencies_obj):

        if xml_obj.attrib['type'] == 'git':
            # Git dependency found
            dependencies_obj.add_dependency(GitDependency(xml_obj.attrib['url']))
        else:
            # An invalid dependency found
            raise InvalidXmlConfigurationElement()