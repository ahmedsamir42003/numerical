# Lagrange Interpolation and Linearization Examples

This repository contains two Python functions that demonstrate the concepts of Lagrange interpolation and linearization. These functions can be used to predict values based on a set of data points and fit a linear equation to a given data set, respectively.

## Lagrange Interpolation

The `lagrange` function performs Lagrange interpolation given a list of x-values, a specific x-value to predict, and a corresponding list of y-values. It returns a list of Lagrange coefficients.

### Usage

To use the `lagrange` function, provide a list of x-values, a list of y-values, and the x-value you want to predict. Here's an example:

```python
x_list = [1.0, 2.0, 3.0, 4.0]
y_list = [2.0, 3.0, 5.0, 10.0]
x = 2.5

lx = lagrange(x_list, x)
# lx contains the Lagrange coefficients for x = 2.5
```
## Linearization
The linearization function takes a list of x-values and a corresponding list of y-values as input. It performs linearization by fitting a linear equation to the data set. The function returns a 2D list containing the necessary values for solving the linear equation.

### Usage
To use the linearization function, provide a list of x-values and a list of y-values. Here's an example:

```python

x_list = [1.0, 2.0, 3.0, 4.0]
y_list = [2.0, 3.0, 5.0, 10.0]

lis = linearization(x_list, y_list)
# lis contains the values required for solving the linear equation
