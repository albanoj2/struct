import os
from parser.xml import XmlParser


THIS_DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':

    # The directory of the example project
    root_dir = os.path.join(THIS_DIR, 'example')

    # Create the parser to parse the struct configuration file
    parser = XmlParser(root_dir)

    print(root_dir)
