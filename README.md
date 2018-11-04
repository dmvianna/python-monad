# Python-Monad

This is a fork of [reem/python-monad](https://github.com/reem/python-monad). I'd much rather just pip install it, but as the original source wasn't in PyPI, I had to package it myself.

This project provides Python classes that emulate the [Haskell](https://www.haskell.org/) types [`Maybe`](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Maybe.html) and [`Either`](http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Either.html), as well as associated functions to manipulate them and perform input/output [`IO`](http://hackage.haskell.org/package/base-4.12.0.0/docs/System-IO.html). 

Why would you care? Maybe and Either allows you to respectively discard or pass forward errors during execution. Instead of throwing or catching exceptions, one could direct correct behaviour through a *happy* path and exceptions through a *sad* path. Exceptions then become just another ordinary value, which is a much more convenient way to deal with them.
