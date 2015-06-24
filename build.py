# -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

# use_plugin("python.core")
# use_plugin("python.unittest")
# use_plugin("python.install_dependencies")
# use_plugin("python.flake8")
# use_plugin("python.coverage")
use_plugin("python.distutils")
# use_plugin("copy_resources")


name = "pybuilder-smart-copy-resources"
summary = 'PyBuilder plugin for copying additional resources'
authors = [Author('Martin Gruber', 'martin.gruber@email.cz')]
version = "0.1.1"
default_task = "publish"
license = 'MIT'
url = 'https://github.com/margru/pybuilder-smart-copy-resources'

classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 2 - Pre-Alpha',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
]

description = """
Please, see https://github.com/margru/pybuilder-smart-copy-resources for more information.
"""

@init
def set_properties(project):
    project.set_property("name", name)
    project.set_property("version", version)
    project.set_property("distutils_classifiers", classifiers)
