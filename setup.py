from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name="Rouletter: Roulette Selector",
    author="Tom Hebbron",
    author_email="tom@hebbron.com",
    url="https://github.com/tomhebbron/rouletter",
    ext_modules=cythonize([Extension("cyRouletter",
                                     sources=["cyRouletter.pyx"],
                                     language="c++",
                                     extra_compile_args=['-O3'],
                                     )]),
    include_dirs=[]
)
