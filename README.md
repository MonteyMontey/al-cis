# al-cis
Cell Interaction Service of the "Artificial Life"-Project at @codeuniveristy
___

**Table of content**
- [About](#about)
  - [alife](#alife)
  - [cis](#cis)
- [Getting started](#getting-started)
- [Documentation](#documentation)
- [Collaboration](#collaboration)
  - [styleguide](#styleguide)

## About
CIS is no open source project in the classical sense, but a university project at the CODE University of Applied Sciences Berlin.
The code is open anymays. We are happy to get in contact with in interestes people.

### alife
The Artifical Life Project aims to build a cell simulator, which is able to compute the life of multiple cells, each having it's own unique dna which determines their individual fitness to the environment.

### cis
The Cell Interaction Service (aka. CIS) is the instance of this project which computes the interaction of a cell with the environment and other cells. That contains movement, food, energy consumption, but also splitting and mutation.


## Getting started 

1. Make sure you have [virtualenv](https://virtualenv.pypa.io/en/latest/) in your PATH
2. Install all dependencies via
   ```shell
   al-cis$ make dep
   ```
3. Run [`al-master`](https://github.com/codeuniversity/al-master) in one terminal via
   ```shell
   al-master$ make run
   ```
4. Run [`al-cis`] in another terminal via
   ```shell
   al-cis$ make run
   ```
5. Open the `index.html` of [`al-client`](https://github.com/codeuniversity/al-client) in your favourite browser


## Documentation
coming soon ...

## Collaboration

### styleguide
We use `autopep8` for autoformatting. It is configured in [`setup.cfg`](setup.cfg)
