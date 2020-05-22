#!/usr/bin/env python3
"""This module collects information about the project and makes
available to the configuration file.
"""
from os import sep as os_sep

PROJECT_INFO_FILE_NAME = 'PROJECT-INFO.txt'
VERSION_SEP = '.'
FIELD_SEP = ': '

class ProjectAttr:
    """Defines attribute names which are recognized in the 'PROJECT_INFO.txt' file"""
    version = 'version'
    copyright = 'copyright'
    product = 'product'
    author = 'author'
    license = 'license'

class ProjectInfo:
    """Defines the names of attributes in a special file that contains release related information. 
    """
    def __init__(self, file_name=PROJECT_INFO_FILE_NAME):
        data = self._read(file_name)
        self.release = data[ProjectAttr.version]
        self.product = data[ProjectAttr.product]
        self.author = data[ProjectAttr.author]
        self.copyright = data[ProjectAttr.copyright]
        self.license = data[ProjectAttr.license]
        self.version = self.release.rpartition(VERSION_SEP)[0]

    @staticmethod
    def _read(file_name):
        """Collects all attributes from the supplied file

        'file_name' must reside in the same directory with this module.
        """
        records = {}
        file_name = file_name.rpartition(os_sep)[-1]
        with open(file_name) as project_data:
            for _line in project_data:
                attr_name, _, attr_value = _line.partition(FIELD_SEP)
                records[attr_name.lower().strip()] = attr_value.strip()
        return records

if __name__ == '__main__':
    pi = ProjectInfo()
    print("Version:\t'{}'\nRelease:\t'{}'\nCopyright:\t'{}'".format(
        pi.version,
        pi.release,
        pi.copyright))
