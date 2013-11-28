#http://stackoverflow.com/questions/14780007/python-list-to-cython

cimport cython

import numpy
cimport numpy

from libc.stdlib cimport malloc, free

cdef extern from "Rouletter.hpp":

	void rouletter_init(const int* data, const int len, double* bounds)

	int rouletter_spin(const double* bounds, const int len, const double luck)

	int rouletter_spin_bisect(const double* bounds, const int len, const double luck)

	cdef cppclass clsRouletter:
		clsRouletter(const int *data, const int len)
		int spin(const double luck)
		int spin_bisect(const double luck)



cdef class Rouletter:
	cdef clsRouletter* thisptr
	def __cinit__(self, data):
		# allocate c array for input data, and copy over.
		cdef int *cdata
		cdata = <int *>malloc(len(data)*cython.sizeof(int))
		if cdata is NULL: raise MemoryError()
		for i in xrange(len(data)): 
			cdata[i] = data[i]

		# create new c++ Rouletter objects with cdata
		self.thisptr = new clsRouletter(cdata, len(data))


	def spin(self, double luck):
		return self.thisptr.spin(luck)

	def spin_bisect(self, double luck):
		return self.thisptr.spin_bisect(luck)



def r_init(data):

	#allocate array to make C copy of input data
	cdef int *in_data
	in_data = <int *>malloc(len(data)*cython.sizeof(int))
	if in_data is NULL: raise MemoryError()
	#and copy it over
	for i in xrange(len(data)): 
		in_data[i] = data[i]

	#allocate C array for output to write to
	cdef double *out_bounds
	out_bounds = <double *>malloc(len(data)*cython.sizeof(double))
	if out_bounds is NULL: raise MemoryError()

	#and call the C function
	rouletter_init(in_data, len(data), out_bounds)

	#now copy back
	output = [out_bounds[i] for i in xrange(len(data))]

	# release allocated memory
	free(in_data)
	free(out_bounds)

	return output


def r_spin(bounds,luck, bisect=True):
	#allocate C array to copy bounds into the C function
	cdef double *cbounds
	cbounds = <double *>malloc(len(bounds)*cython.sizeof(double))
	if cbounds is NULL: raise MemoryError()
	#make C-available copy of bounds array
	for i in xrange(len(bounds)): 
		cbounds[i] = bounds[i]
	if (bisect): output = rouletter_spin_bisect(cbounds, len(bounds), luck)
	else:  output =  rouletter_spin(cbounds, len(bounds), luck)
	free(cbounds)
	return output
