#http://stackoverflow.com/questions/14780007/python-list-to-cython

cimport cython

from libc.stdlib cimport malloc, free

#http://docs.cython.org/src/userguide/fusedtypes.html
ctypedef fused numeric_types:
	#cython.unsigned int
	cython.int
	cython.float
	cython.double

cdef extern from "Rouletter.hpp" namespace "Rouletter":

	cdef cppclass CppRouletterD "Rouletter::Rouletter<double>":
		CppRouletterD(double *data, size_t len)
		size_t spin(double luck)
		size_t spin_bisect(double luck)



cdef class RouletteSelector:
	cdef CppRouletterD* thisptr
	def __cinit__(self, data):
		# allocate c array for input data, and copy over.
		cdef double *cdata
		cdata = <double *>malloc(len(data)*cython.sizeof(double))
		if cdata is NULL: raise MemoryError()
		for i in xrange(len(data)): 
			cdata[i] = float(data[i])

		# create new c++ Rouletter objects with cdata
		self.thisptr = new CppRouletterD(cdata, len(data))

	def spin(self, double luck):
		return self.thisptr.spin(luck)

	def spin_bisect(self, double luck):
		return self.thisptr.spin_bisect(luck)


