Rouletter
=========

Rouletter implements roulette wheel, or [fitness proportionate selection](http://en.wikipedia.org/wiki/Fitness_proportionate_selection). 

It is built for performance - the critical parts are in C++, accessed from Python via Cython.

Take an array of data, e.g., [1,2,1,1]. Now imagine a roulette wheel with slots proportionate to these values (four slots, one twice the width of the others). When we repeatedly spin the wheel and release a ball, oover time it should land twice
as often in the second slot. Rouletter simulates this kind of selection.

Use
---

To use, initialise the Rouletter object with an array of integers that define the 
slot widths, then call `spin` with a random number between 0.0 and 1.0.

```python
  import random, Rouletter
  widths = [1,2,1,1]
  rw = Rouletter.Rouletter(widths)
  print rw.spin(random.random())
  #test distribution looks OK
  hits = [0]*len(widths)
  for i in xrange(1000): hits[rw.spin(random.random())] +=1
  print hits
```


Compiling
---------

To build the code from source, ensure you have Cython and suitable compilers installed and call the setup.py script. For my local windows environment, I use:

```bash
  python setup.py build_ext --inplace --compiler=mingw32
```

