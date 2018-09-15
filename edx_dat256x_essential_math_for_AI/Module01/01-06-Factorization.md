
# Factorization
Factorization is the process of restating an expression as the *product* of two expressions (in other words, expressions multiplied together).

For example, you can make the value **16** by performing the following multiplications of integer numbers:
- 1 x 16
- 2 x 8
- 4 x 4

Another way of saying this is that 1, 2, 4, 8, and 16 are all factors of 16.

## Factors of Polynomial Expressions
We can apply the same logic to polynomial expressions. For example, consider the following monomial expression:

\begin{equation}-6x^{2}y^{3} \end{equation}

You can get this value by performing the following multiplication:

\begin{equation}(2xy^{2})(-3xy) \end{equation}

Run the following Python code to test this with arbitrary ***x*** and ***y*** values:


```python
from random import randint
x = randint(1,100)
y = randint(1,100)

(2*x*y**2)*(-3*x*y) == -6*x**2*y**3
```




    True



So, we can say that **2xy<sup>2</sup>** and **-3xy** are both factors of **-6x<sup>2</sup>y<sup>3</sup>**.

This also applies to polynomials with more than one term. For example, consider the following expression:

\begin{equation}(x + 2)(2x^{2} - 3y + 2) = 2x^{3} + 4x^{2} - 3xy + 2x - 6y + 4 \end{equation}

Based on this, **x+2** and **2x<sup>2</sup> - 3y + 2** are both factors of **2x<sup>3</sup> + 4x<sup>2</sup> - 3xy + 2x - 6y + 4**.

(and if you don't believe me, you can try this with random values for x and y with the following Python code):


```python
from random import randint
x = randint(1,100)
y = randint(1,100)

(x + 2)*(2*x**2 - 3*y + 2) == 2*x**3 + 4*x**2 - 3*x*y + 2*x - 6*y + 4
```




    True



## Greatest Common Factor
Of course, these may not be the only factors of **-6x<sup>2</sup>y<sup>3</sup>**, just as 8 and 2 are not the only factors of 16.

Additionally, 2 and 8 aren't just factors of 16; they're factors of other numbers too - for example, they're both factors of 24 (because 2 x 12 = 24 and 8 x 3 = 24). Which leads us to the question, what is the highest number that is a factor of both 16 and 24? Well, let's look at all the numbers that multiply evenly into 12 and all the numbers that multiply evenly into 24:

|   16   |   24   |
|--------|--------|
| 1 x 16 | 1 x 24 |
| 2 x **8**  | 2 x 12 |
|        | 3 x **8**  |
| 4 x 4  | 4 x 6  |

The highest value that is a multiple of both 16 and 24 is **8**, so 8 is the *Greatest Common Factor* (or GCF) of 16 and 24.

OK, let's apply that logic to the following expressions:

\begin{equation}15x^{2}y\;\;\;\;\;\;\;\;9xy^{3}\end{equation}

So what's the greatest common factor of these two expressions?

It helps to break the expressions into their consitituent components. Let's deal with the coefficients first; we have 15 and 9. The highest value that divides evenly into both of these is **3** (3 x 5 = 15 and 3 x 3 = 9).

Now let's look at the ***x*** terms; we have x<sup>2</sup> and x. The highest value that divides evenly into both is these is **x** (*x* goes into *x* once and into *x*<sup>2</sup> *x* times).

Finally, for our ***y*** terms, we have y and y<sup>3</sup>. The highest value that divides evenly into both is these is **y** (*y* goes into *y* once and into *y*<sup>3</sup> *y&bull;y* times).

Putting all of that together, the GCF of both of our expression is:

\begin{equation}3xy\end{equation}

An easy shortcut to identifying the GCF of an expression that includes variables with exponentials is that it will always consist of:
- The *largest* numeric factor of the numeric coefficients in the polynomial expressions (in this case 3)
- The *smallest* exponential of each variable (in this case, x and y, which technically are x<sup>1</sup> and y<sup>1</sup>.

You can check your answer by dividing the original expressions by the GCF to find the coefficent expressions for the GCF (in other words, how many times the GCF divides into the original expression). The result, when multiplied by the GCF will always produce the original expression. So in this case, we need to perform the following divisions:

\begin{equation}\frac{15x^{2}y}{3xy}\;\;\;\;\;\;\;\;\frac{9xy^{3}}{3xy}\end{equation}

These fractions simplify to **5x** and **3y<sup>2</sup>**, giving us the following calculations to prove our factorization:

\begin{equation}3xy(5x) = 15x^{2}y\end{equation}
\begin{equation}3xy(3y^{2}) = 9xy^{3}\end{equation}

Let's try both of those in Python:


```python
from random import randint
x = randint(1,100)
y = randint(1,100)

print((3*x*y)*(5*x) == 15*x**2*y)
print((3*x*y)*(3*y**2) == 9*x*y**3)
```

    True
    True
    

## Distributing Factors
Let's look at another example. Here is a binomial expression:

\begin{equation}6x + 15y \end{equation}

To factor this, we need to find an expression that divides equally into both of these expressions. In this case, we can use **3** to factor the coefficents, because 3 &bull; 2x = 6x and 3&bull; 5y = 15y, so we can write our original expression as:

\begin{equation}6x + 15y = 3(2x) + 3(5y) \end{equation}

Now, remember the distributive property? It enables us to multiply each term of an expression by the same factor to calculate the product of the expression multiplied by the factor. We can *factor-out* the common factor in this expression to distribute it like this:

\begin{equation}6x + 15y = 3(2x) + 3(5y) = \mathbf{3(2x + 5y)} \end{equation}

Let's prove to ourselves that these all evaluate to the same thing:


```python
from random import randint
x = randint(1,100)
y = randint(1,100)

(6*x + 15*y) == (3*(2*x) + 3*(5*y)) == (3*(2*x + 5*y))
```




    True



For something a little more complex, let's return to our previous example. Suppose we want to add our original 15x<sup>2</sup>y and 9xy<sup>3</sup> expressions:

\begin{equation}15x^{2}y + 9xy^{3}\end{equation}

We've already calculated the common factor, so we know that:

\begin{equation}3xy(5x) = 15x^{2}y\end{equation}
\begin{equation}3xy(3y^{2}) = 9xy^{3}\end{equation}

Now we can factor-out the common factor to produce a single expression:

\begin{equation}15x^{2}y + 9xy^{3} = \mathbf{3xy(5x + 3y^{2})}\end{equation}

And here's the Python test code:


```python
from random import randint
x = randint(1,100)
y = randint(1,100)

(15*x**2*y + 9*x*y**3) == (3*x*y*(5*x + 3*y**2))
```




    True



So you might be wondering what's so great about being able to distribute the common factor like this. The answer is that it can often be useful to apply a common factor to multiple terms in order to solve seemingly complex problems.

For example, consider this:

\begin{equation}x^{2} + y^{2} + z^{2} = 127\end{equation}

Now solve this equation:

\begin{equation}a = 5x^{2} + 5y^{2} + 5z^{2}\end{equation}

At first glance, this seems tricky because there are three unknown variables, and even though we know that their squares add up to 127, we don't know their individual values. However, we can distribute the common factor and apply what we *do* know. Let's restate the problem like this:

\begin{equation}a = 5(x^{2} + y^{2} + z^{2})\end{equation}

Now it becomes easier to solve, because we know that the expression in parenthesis is equal to 127, so actually our equation is:

\begin{equation}a = 5(127)\end{equation}

So ***a*** is 5 times 127, which is 635

## Formulae for Factoring Squares
There are some useful ways that you can employ factoring to deal with expressions that contain squared values (that is, values with an exponential of 2).

### Differences of Squares
Consider the following expression:

\begin{equation}x^{2} - 9\end{equation}

The constant *9* is 3<sup>2</sup>, so we could rewrite this as:

\begin{equation}x^{2} - 3^{2}\end{equation}

Whenever you need to subtract one squared term from another, you can use an approach called the *difference of squares*, whereby we can factor *a<sup>2</sup> - b<sup>2</sup>* as *(a - b)(a + b)*; so we can rewrite the expression as:

\begin{equation}(x - 3)(x + 3)\end{equation}

Run the code below to check this:


```python
from random import randint
x = randint(1,100)

(x**2 - 9) == (x - 3)*(x + 3)
```




    True



### Perfect Squares
A *perfect square* is a number multiplied by itself, for example 3 multipled by 3 is 9, so 9 is a perfect square.

When working with equations, the ability to factor between polynomial expressions and binomial perfect square expressions can be a useful tool. For example, consider this expression:

\begin{equation}x^{2} + 10x + 25\end{equation}

We can use 5 as a common factor to rewrite this as:

\begin{equation}(x + 5)(x + 5)\end{equation}

So what happened here?

Well, first we found a common factor for our coefficients: 5 goes into 10 twice and into 25 five times (in other words, squared). Then we just expressed this factoring as a multiplication of two identical binomials *(x + 5)(x + 5)*.

Remember the rule for multiplication of polynomials is to multiple each term in the first polynomial by each term in the second polynomial and then add the results; so you can do this to verify the factorization:

- x &bull; x = x<sup>2</sup>
- x &bull; 5 = 5x
- 5 &bull; x = 5x
- 5 &bull; 5 = 25

When you combine the two 5x terms we get back to our original expression of x<sup>2</sup> + 10x + 25.

Now we have an expression multipled by itself; in other words, a perfect square. We can therefore rewrite this as:

\begin{equation}(x + 5)^{2}\end{equation}

Factorization of perfect squares is a useful technique, as you'll see when we start to tackle quadratic equations in the next section. In fact, it's so useful that it's worth memorizing its formula:

\begin{equation}(a + b)^{2} = a^{2} + b^{2}+ 2ab \end{equation}

In our example, the *a* terms is ***x*** and the *b* terms is ***5***, and in standard form, our equation  *x<sup>2</sup> + 10x + 25* is actually *a<sup>2</sup> +  2ab + b<sup>2</sup>*. The operations are all additions, so the order isn't actually important!

Run the following code with random values for *a* and *b* to verify that the formula works:


```python
from random import randint
a = randint(1,100)
b = randint(1,100)

a**2 + b**2 + (2*a*b) == (a + b)**2
```




    True


