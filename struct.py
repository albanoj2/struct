import os

from struct.configparser.xmlparser import XmlParser


THIS_DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':

    # The directory of the example project
    root_dir = os.path.join(THIS_DIR, 'example')

    # Create the parser to parse the struct configuration file
    parser = XmlParser(root_dir)
    parser.parse()

    # Obtain the project domain object from the parser
    project = parser.project

    for dep in project.dependencies.dependencies:
        print dep.url
