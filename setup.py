# ----------------------------------------------------------------------------
# Copyright (c) 2017-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from setuptools import setup, find_packages

import versioneer

setup(
    name="q2-revert",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Jamie Morton",
    author_email="jamietmorton@gmail.com",
    description="Reverting hashes",
    license='BSD-3-Clause',
    url="https://github.com/qiime2/q2-gneiss",
    scripts=['revert.py'],
    zip_safe=False,
)
