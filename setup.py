# setup.py
from setuptools import setup
from setuptools import find_packages

# The version is updated automatically with bumpversion
# Do not update manually
__version = '0.3.0'

# windows installer:
# python setup.py bdist_wininst

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords

# ipython profile magic commands implementation
package_list = ['*ui']

# TODO: fill the long description
long_description = """ Python application to monitor and tune IcePAP 
based systems. """

# Add your dependencies in the following line.
# install_requires = ['python-configparser', 'python-pyicepap']
# do not use "python-" prefixes here, otherwise python doesn't look
# for the right library name at run-time. Instead, use the FPM option
# --python-fix-dependencies
# in the gitlab_ci.yml staging script at 
# https://gitlab.maxiv.lu.se/kits-maxiv/icepap-staging/
install_requires = ['configparser', 'pyicepap']

classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: End Users/Desktop',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Communications',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: User Interfaces',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: GNU Library or Lesser General Public ' + \
    'License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
]

# TODO: Include dependencies

setup(
    name="icepaposc",
    description="Python IcePAP Extension",
    version=__version,
    author="Jarkko Inki and Roberto Homs-Puron",
    author_email="ctbeamlines@cells.es",
    url="https://github.com/ALBA-Synchrotron/IcepapOCS",
    packages=find_packages(),
    install_requires=install_requires,
    package_data={'': package_list},
    include_package_data=True,
    keywords='APP',
    license="GPL",
    long_description=long_description,
    classifiers=classifiers,
    entry_points={
        'console_scripts': [
            'icepaposc = icepaposc.__main__:main',
        ]
    }
)
