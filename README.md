# BeginToReason2
[![Build Status](https://travis-ci.com/ClemsonRSRG/beginToReason2.svg?branch=master)](https://travis-ci.com/ClemsonRSRG/beginToReason2)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/ClemsonRSRG/beginToReason2/master/LICENSE.txt)

`BeginToReason2` is a tool that utilizes the RESOLVE programming language to pinpoint difficulties CS students have with learning how to rigorously trace the code they encounter. This version features a new back-end build using Python and Django and a front-end that incorporates Bootstrap and communicates with the RESOLVE verification engine.

A long term goal of `BeginToReason2` is to be a Reactive, RESTful API.

## What is RESOLVE?

RESOLVE (REusable SOftware Language with VErification) is a programming and specification language designed for verifying correctness of object oriented programs.

The RESOLVE language is designed from the ground up to facilitate *mathematical reasoning*. As such, the language provides syntactic slots for assertions such as pre-post conditions that are capable of abstractly describing a program's intended behavior. In writing these assertions, users are free to draw from from a variety of pre-existing and user-defined mathematical theories containing fundamental axioms, definitions, and results necessary/useful in establishing program correctness.

All phases of the verification process spanning verification condition (VC) generation to proving are performed in-house, while RESOLVE programs are translated to Java and run on the JVM.

## Authors and major contributors

The creation and continual evolution of the RESOLVE language is owed to an ongoing joint effort between Clemson University, The Ohio State University, and countless educators and researchers from a variety of [other](https://www.cs.clemson.edu/resolve/about.html) institutions.

Developers of this particular test/working-iteration of the `BeginToReason2` include:

* [RESOLVE Software Research Group (RSRG)](https://www.cs.clemson.edu/resolve/) - School of Computing, Clemson University
* [Florida Atlantic University](http://www.fau.edu/research/)
* [Rose-Hulman Institute of Technology](https://www.rose-hulman.edu/)

## Copyright and license

Copyright © 2020, [RESOLVE Software Research Group (RSRG)](https://www.cs.clemson.edu/resolve/). All rights reserved. The use and distribution terms for this software are covered by the BSD 3-clause license which can be found in the file `LICENSE.txt` at the root of this repository. By using this software in any fashion, you are agreeing to be bound by the terms of this license. You must not remove this notice, or any other, from this software.
