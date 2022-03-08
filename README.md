# Radix
In mathematics, radix or (base) is a number of unique digits, used to represent numbers.

For example, the most common base used today is base 10 (decimal), it uses digits from 0 to 9.
However, in base 2 (binary) there are only 0 and 1 digits, and it is used as a primary language for computers.

Base Conversion is a process of converting a number from one base to another.
This process is widely used in digital systems, defining colors (in hexadecimal base), displaying error messages, URL shortening, and many more applications. 

**Radix** is a python package for base conversion *(general_purpose_usage)* with high precision. 
* Supports bases from 2 to 62. 
*  Accepts fractions for conversion.

*Note*: only positive numbers are supporeted.

## Installation
```bash
pip install git+https://github.com/BanaAbdallah/Radix.git
```

## Usage
Basic implementation, `b1` stands for the base of the entry, and `b2` the base want to convert into.
```python
from Radix.radix import BaseConvert

conv = BaseConvert(b1=10, b2=16, entry='350')
conv.run()
# returns 15E
```

For fractions, you can specify the rounding using `round` parameter (the default is 10).
```python
conv = BaseConvert(b1=3, b2=50, entry='102.21', round=5)
conv.run()
# returns B.ciMB5
```

