from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules= cythonize("jit_test_cython.pyx")
)