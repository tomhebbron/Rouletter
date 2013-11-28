from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

import numpy

# extensions = [
# 	Extension("Rouletter", ["Rouletter.pyx"], 
# 		extra_compile_args=['-std=c99'])
# 	]


# setup(
# 	name = "Rouletter: Roulette Selector",
# 	ext_modules = cythonize(extensions)
# )

# setup(
# 	#cmdclass 	= {'build_ext': build_ext},
# 	ext_modules =[Extension("Rouletter",
# 					sources=["Rouletter"],
# 					language="c++"),],

# )


setup(
	name 		= "Rouletter: Roulette Selector",
	author 		= "Tom Hebbron",
	author_email= "tom@hebbron.com",
	url			= "https://github.com/tomhebbron/rouletter",
	ext_modules = cythonize([Extension("Rouletter", 
										sources=["Rouletter.pyx"], 
										language="c++",
										extra_compile_args=['-O3'],
										)]),
	include_dirs= [numpy.get_include()]
)

#http://stackoverflow.com/questions/2379898/make-distutils-look-for-numpy-header-files-in-the-correct-place
