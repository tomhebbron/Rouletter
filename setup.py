from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name="Rouletter",
    author="Tom Hebbron",
    author_email="tom@hebbron.com",
    url="https://github.com/tomhebbron/Rouletter",
    ext_modules=cythonize([Extension("Rouletter",
                                     sources=["Rouletter.pyx"],
                                     language="c++",
                                     #extra_compile_args=['-O3'],
                                     )]),
    include_dirs=[]
)
