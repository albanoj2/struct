from parser import Parser

import os
import xml.etree.ElementTree


class XmlParser (Parser):

    def __init__(self, project_root_dir):
        Parser.__init__(self, project_root_dir)

        # Store the path of the XML file
        self._xml_file_path = os.path.join(project_root_dir, 'struct.xml')

    def parse(self):
        # Obtain the XML root from the XML file
        xml_root = xml.etree.ElementTree.parse(self._xml_file_path).getroot()

        # Delegate to the main parsing method
        self.__parse_from_xml_root(xml_root)

    def __parse_from_xml_root(self, xml_root):
        print('Made it to parse XML')
