Rouletter
=========

Rouletter implements roulette wheel, or [fitness proportionate selection](http://en.wikipedia.org/wiki/Fitness_proportionate_selection). 

This implementation is built for performance - the critical parts are in C++, accessed from Python via Cython.

A roulette wheel provides a way of making a random selection from 37 (or 38) slots, all equally likely. If you roll the ball many times, these samples build up a picture of the distribution of slot sizes (in the casino, a uniform distribution). A roulette wheel selector is a generalisation of this process - you can set up a wheel with as many slots as you like, and they don't have to all be of equal size.

As a simple example, let's imagine a wheel with four slots, and with the second slot twice the width of the others, i.e., [1,2,1,1]. The wheel has slots corresponding to these sizes, and when we repeatedly spin the wheel and release a ball, over time it should land twice as often in the second slot. Rouletter simulates this kind of selection.


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
  python setup.py build_ext --inplace
```

