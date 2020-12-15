import os
import sys

from setuptools import setup, find_packages  # magic import to allow us to use entry_point

import re

__version__ = re.findall(
    r"""__version__ = ["']+([0-9\.]*)["']+""",
    open("pyoptsparse/__init__.py").read(),
)[0]

if len(sys.argv) == 1:
    print(
        (
            "\nTo install, run: python setup.py install --user\n\n"
            + "To build, run: python setup.py build_ext --inplace\n\n"
            + "For help on C-compiler options run: python setup.py build --help-compiler\n\n"
            + "For help on Fortran-compiler options run: python setup.py build --help-fcompiler\n\n"
            + "To specify a Fortran compiler to use run: python setup.py install --user --fcompiler=<fcompiler name>\n\n"
            + "For further help run: python setup.py build --help"
        )
    )
    sys.exit(-1)


setup(
    name="pyoptsparse-dhill2522",
    author="MDOLAB",
    author_email="dhill2522@gmail.com",
    url="https://github.com/dhill2522/pyoptsparse",
    version=__version__,
    description="Python package for formulating and solving nonlinear constrained optimization problems",
    long_description="pyOptSparse is a Python package for formulating and solving nonlinear constrained optimization problems",
    keywords="optimization",
    install_requires=["sqlitedict>=1.6", "numpy>=1.16", "scipy>1.2"],
    packages=find_packages(),
    platforms=["Linux"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Education",
    ],
    entry_points={"gui_scripts": ["optview = pyoptsparse.postprocessing.OptView:main"]},
)
