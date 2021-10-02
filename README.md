<h1 id="project-title" align="center">
  Analysis of Data <img alt="logo" width="40" height="40" src="https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png" /><br>
  <img alt="language" src="https://img.shields.io/badge/language-python-brightgreen?style=flat-square" />
  <img alt="language" src="https://img.shields.io/github/issues/mezgoodle/Templates?style=flat-square" />
  <img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/mezgoodle/Templates?style=flat-square" />
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mezgoodle/Templates?style=flat-square" />
  <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/mezgoodle/Templates?style=flat-square" />
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/mezgoodle/Templates?style=flat-square">
</h1>

<p align="center">
 🌟Hello everyone! This is the repository of my labs on Python "Analysis of Data".🌟
</p>

## Motivation :exclamation:

The main reason of this repository is to hold all My labs of "Analysis Of Data"

## Build status :hammer:

> None

## Badges :mega:

Other badges

[![Theme](https://img.shields.io/badge/Theme-Data_Analysis-green?style=flat-square)](https://www.google.com.ua/)
[![Platform](https://img.shields.io/badge/Platform-Python-green?style=flat-square)](https://www.google.com.ua/)
 
## Screenshots :camera:

> None

## Tech/framework used :wrench:

**Built with**

- [Python](https://www.python.org/)
- [NumPy](https://numpy.org/)

## Features :muscle:

With thess labs You can learn a lot of stuff to start Your journey into Data Analysis 

## Code Example :pushpin:

```python
import numpy as np
import pandas as pd

from string import Template

np.set_printoptions(suppress=True)

template = Template('#' * 10 + ' $string ' + '#' * 10)

# Generating section starts #

print(template.substitute(string='Generate array from 3 to 25 with step 2'))
array = np.arange(3, 25, 2)
print(array)

print(template.substitute(string='Generate array of 13 elements, filled with ones'))
array = np.ones(13, dtype='float')
print(array)

print(template.substitute(string='Generate matrix 3x7x3, filled with zeros'))
array = np.zeros((3, 7, 3), dtype='uint')
print(array)
```

## Installation :computer:

```
git clone https://github.com/mezgoodle/ad_labs.git
```

## Fast usage :dash:

If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.

## API Reference :fireworks:

Run main.py

## Tests :microscope:

> None

## Contribute :running:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also look at the [CONTRIBUTING.md](https://github.com/mezgoodle/ad_labs/blob/master/CONTRIBUTING.md).

## Credits :cat::handshake:

> None

## License :bookmark:

MIT © [mezgoodle](https://github.com/mezgoodle)
