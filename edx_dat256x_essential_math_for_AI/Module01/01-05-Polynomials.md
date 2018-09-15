
# Polynomials
Some of the equations we've looked at so far include expressions that are actually *polynomials*; but what *is* a polynomial, and why should you care?

A polynomial is an algebraic expression containing one or more *terms* that each meet some specific criteria. Specifically:
- Each term can contain:
 - Numeric values that are coefficients or constants (for example 2, -5, <sup>1</sup>/<sub>7</sub>)
 - Variables (for example, x, y)
 - Non-negative integer exponents (for example <sup>2</sup>, <sup>64</sup>)
- The terms can be combined using arithmetic operations - but **not** division by a variable.

For example, the following expression is a polynomial:

\begin{equation}12x^{3} + 2x - 16 \end{equation}

When identifying the terms in a polynomial, it's important to correctly interpret the arithmetic addition and subtraction operators as the sign for the term that follows. For example, the polynomial above contains the following three terms:
- 12x<sup>3</sup>
- 2x
- -16

The terms themselves include:
- Two coefficients(12 and 2) and a constant (-16)
- A variable (x)
- An exponent (<sup>3</sup>)

A polynomial that contains three terms is also known as a *trinomial*. Similarly, a polynomial with two terms is known as a *binomial* and a polynomial with only one term is known as a *monomial*.

So why do we care? Well, polynomials have some useful properties that make them easy to work with. for example, if you multiply, add, or subtract a polynomial, the result is always another polynomial.

## Standard Form for Polynomials
Techbnically, you can write the terms of a polynomial in any order; but the *standard form* for a polynomial is to start with the highest *degree* first and constants last. The degree of a term is the highest order (exponent) in the term, and the highest order in a polynomial determines the degree of the polynomial itself.

For example, consider the following expression:
\begin{equation}3x + 4xy^{2} - 3 + x^{3} \end{equation}

To express this as a polynomial in the standard form, we need to re-order the terms like this:

\begin{equation}x^{3} + 4xy^{2} + 3x - 3 \end{equation}

## Simplifying Polynomials
We saw previously how you can simplify an equation by combining *like terms*. You can simplify polynomials in the same way.

For example, look at the following polynomial:

\begin{equation}x^{3} + 2x^{3} - 3x - x + 8 - 3 \end{equation}

In this case, we can combine x<sup>3</sup> and 2x<sup>3</sup> by adding them to make 3x<sup>3</sup>. Then we can add -3x and -x (which is really just a shorthand way to say -1x) to get -4x, and then add 8 and -3 to get 5. Our simplified polynomial then looks like this:

\begin{equation}3x^{3} - 4x + 5 \end{equation}

We can use Python to compare the original and simplified polynomials to check them - using an arbitrary random value for ***x***:


```python
from random import randint
x = randint(1,100)

(x**3 + 2*x**3 - 3*x - x + 8 - 3) == (3*x**3 - 4*x + 5)
```




    True



## Adding Polynomials
When you add two polynomials, the result is a polynomial. Here's an example:

\begin{equation}(3x^{3} - 4x + 5)   +   (2x^{3} + 3x^{2} - 2x + 2) \end{equation}

because this is an addition operation, you can simply add all of the like terms from both polynomials. To make this clear, let's first put the like terms together:

\begin{equation}3x^{3} + 2x^{3} + 3x^{2} - 4x -2x + 5 + 2 \end{equation}

This simplifies to:

\begin{equation}5x^{3} + 3x^{2} - 6x + 7 \end{equation}

We can verify this with Python:


```python
from random import randint
x = randint(1,100)


(3*x**3 - 4*x + 5) + (2*x**3 + 3*x**2 - 2*x + 2) == 5*x**3 + 3*x**2 - 6*x + 7
```




    True



## Subtracting Polynomials
Subtracting polynomials is similar to adding them but you need to take into account that one of the polynomials is a negative.

Consider this expression:

\begin{equation}(2x^{2} - 4x + 5)   -   (x^{2} - 2x + 2) \end{equation}

The key to performing this calculation is to realize that the subtraction of the second polynomial is really an expression that adds -1(x<sup>2</sup> - 2x + 2); so you can use the distributive property to multiply each of the terms in the polynomial by -1 (which in effect simply reverses the sign for each term). So our expression becomes:

\begin{equation}(2x^{2} - 4x + 5)   +   (-x^{2} + 2x - 2) \end{equation}

Which we can solve as an addition problem. First place the like terms together:

\begin{equation}2x^{2} + -x^{2} + -4x + 2x + 5 + -2 \end{equation}

Which simplifies to:

\begin{equation}x^{2} - 2x + 3 \end{equation}

Let's check that with Python:


```python
from random import randint
x = randint(1,100)

(2*x**2 - 4*x + 5) - (x**2 - 2*x + 2) == x**2 - 2*x + 3
```




    True



## Multiplying Polynomials
To multiply two polynomials, you need to perform the following two steps:
1. Multiply each term in the first polynomial by each term in the second polynomial.
2. Add the results of the multiplication operations, combining like terms where possible.

For example, consider this expression:

\begin{equation}(x^{4} + 2)(2x^{2} + 3x - 3) \end{equation}

Let's do the first step and multiply each term in the first polynomial by each term in the second polynomial. The first term in the first polynomial is x<sup>4</sup>, and the first term in the second polynomial is 2x<sup>2</sup>, so multiplying these gives us 2x<sup>6</sup>. Then we can multiply the first term in the first polynomial (x<sup>4</sup>) by the second term in the second polynomial (3x), which gives us 3x<sup>5</sup>, and so on until we've multipled all of the terms in the first polynomial by all of the terms in the second polynomial, which results in this:

\begin{equation}2x^{6} + 3x^{5} - 3x^{4} + 4x^{2} + 6x - 6 \end{equation}

We can verify a match between this result and the original expression this with the following Python code:


```python
from random import randint
x = randint(1,100)

(x**4 + 2)*(2*x**2 + 3*x - 3) == 2*x**6 + 3*x**5 - 3*x**4 + 4*x**2 + 6*x - 6
```




    True



## Dividing Polynomials
When you need to divide one polynomial by another, there are two approaches you can take depending on the number of terms in the divisor (the expression you're dividing by).

### Dividing Polynomials Using Simplification
In the simplest case, division of a polynomial by a monomial, the operation is really just simplification of a fraction.

For example, consider the following expression:

\begin{equation}(4x + 6x^{2}) \div 2x \end{equation}

This can also be written as:

\begin{equation}\frac{4x + 6x^{2}}{2x} \end{equation}

One approach to simplifying this fraction is to split it it into a separate fraction for each term in the dividend (the expression we're dividing), like this:

\begin{equation}\frac{4x}{2x} + \frac{6x^{2}}{2x}\end{equation}

Then we can simplify each fraction and add the results. For the first fraction, 2x goes into 4x twice, so the fraction simplifies to 2; and for the second, 6x<sup>2</sup> is 2x mutliplied by 3x. So our answer is 2 + 3x:

\begin{equation}2 + 3x\end{equation}

Let's use Python to compare the original fraction with the simplified result for an arbitrary value of ***x***:


```python
from random import randint
x = randint(1,100)

(4*x + 6*x**2) / (2*x) == 2 + 3*x
```




    True



### Dividing Polynomials Using Long Division
Things get a little more complicated for divisors with more than one term.

Suppose we have the following expression:
\begin{equation}(x^{2} + 2x - 3) \div (x - 2) \end{equation}

Another way of writing this is to use the long-division format, like this:
\begin{equation} x - 2 |\overline{x^{2} + 2x - 3} \end{equation}

We begin long-division by dividing the highest order divisor into the highest order dividend - so in this case we divide x into x<sup>2</sup>. X goes into x<sup>2</sup> x times, so we put an x on top and then multiply it through the divisor:
\begin{equation} \;\;\;\;x \end{equation}
\begin{equation}x - 2 |\overline{x^{2} + 2x - 3} \end{equation}
\begin{equation} \;x^{2} -2x \end{equation}

Now we'll subtract the remaining dividend, and then carry down the -3 that we haven't used to see what's left:
\begin{equation} \;\;\;\;x \end{equation}
\begin{equation}x - 2 |\overline{x^{2} + 2x - 3} \end{equation}
\begin{equation}- (x^{2} -2x) \end{equation}
\begin{equation}\;\;\;\;\;\overline{\;\;\;\;\;\;\;\;\;\;4x -3} \end{equation}

OK, now we'll divide our highest order divisor into the highest order of the remaining dividend. In this case, x goes into 4x four times, so we'll add a 4 to the top line, multiply it through the divisor, and subtract the remaining dividend:
\begin{equation} \;\;\;\;\;\;\;\;x + 4 \end{equation}
\begin{equation}x - 2 |\overline{x^{2} + 2x - 3} \end{equation}
\begin{equation}- (x^{2} -2x) \end{equation}
\begin{equation}\;\;\;\;\;\overline{\;\;\;\;\;\;\;\;\;\;4x -3} \end{equation}
\begin{equation}- (\;\;\;\;\;\;\;\;\;\;\;\;4x -8) \end{equation}
\begin{equation}\;\;\;\;\;\overline{\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;5} \end{equation}

We're now left with just 5, which we can't divide further by x - 2; so that's our remainder, which we'll add as a fraction.

The solution to our division problem is:

\begin{equation}x + 4 + \frac{5}{x-2} \end{equation}

Once again, we can use Python to check our answer:


```python
from random import randint
x = randint(3,100)

(x**2 + 2*x -3)/(x-2) == x + 4 + (5/(x-2))
                                
```




    True


