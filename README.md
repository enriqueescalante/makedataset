# MakeDataset


## Introduction

This module allows the creation of an invariant representation of the effective models of heterotic string theory $E_8 \times E_8$. The effective models are created by the program
[**The Orbifolder**](https://orbifolder.hepforge.org/), these models are in a format that is not invariant to transformations of the lattice of the norm group of the theory. Our goal is to obtain information to train a neural network of the autoencoder type, which allows us to change the paradigm to solve the string landscape problem.

This module depends on `The orbifolder`, so much so that it is necessary to compile its code, obtain the executable file *orbifolder* and copy it into the src folder of this module. The compilation process is available in the following [article.](https://arxiv.org/pdf/1110.5229.pdf)

The elements necessary to process the information are:
* The file with the effective models produced by `The orbifolder`.
* The geometry of the orbifolder with which the compaction was performed. The nomenclature of the geometries follows the structure published in this [article](https://arxiv.org/pdf/1209.3906.pdf). To obtain the particular name of a geometry you can check the `Geometry` folder contained in the `src` folder.
* The list with the twisted sectors of interest. The maximum number of sectors depends on the geometry, to see it you can open the file of the particular geometry.

## Installation


For installation you must first clone this repository or download the compressed file and unzip it.

Once located in the module folder, we run

```
python setup.py install
```
to install all the necessary dependencies.


