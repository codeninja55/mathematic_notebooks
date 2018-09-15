
# Getting Started with Equations
Equations are calculations in which one or more variables represent unknown values. In this notebook, you'll learn some fundamental techniques for solving simple equations.

## One Step Equations
Consider the following equation:

\begin{equation}x + 16 = -25\end{equation}

The challenge here is to find the value for **x**, and to do this we need to *isolate the variable*. In this case, we need to get **x** onto one side of the "=" sign, and all of the other values onto the other side. To accomplish this we'll follow these rules:
1. Use opposite operations to cancel out the values we don't want on one side. In this case, the left side of the equation includes an addition of 16, so we'll cancel that out by subtracting 16 and the left side of the equation becomes **x + 16 - 16**.
2. Whatever you do to one side, you must also do to the other side. In this case, we subtracted 16 from the left side, so we must also subtract 16 from the right side of the equation, which becomes **-25 - 16**.
Our equation now looks like this:

\begin{equation}x + 16 - 16 = -25 - 16\end{equation}

Now we can calculate the values on both side. On the left side, 16 - 16 is 0, so we're left with:

\begin{equation}x = -25 - 16\end{equation}

Which yields the result **-41**. Our equation is now solved, as you can see here:

\begin{equation}x = -41\end{equation}

It's always good practice to verify your result by plugging the variable value you've calculated into the original equation and ensuring that it holds true. We can easily do that by using some simple Python code.

To verify the equation using Python code, place the cursor in the following cell and then click the &#9658;<b>|</b> button in the toolbar.


```python
x = -41
x + 16 == -25
```




    True



## Two-Step Equations
The previous example was fairly simple - you could probably work it out in your head. So what about something a little more complex?

\begin{equation}3x - 2 = 10 \end{equation}

As before, we need to isolate the variable **x**, but this time we'll do it in two steps. The first thing we'll do is to cancel out the *constants*. A constant is any number that stands on its own, so in this case the 2 that we're subtracting on the left side is a constant. We'll use an opposite operation to cancel it out on the left side, so since the current operation is to subtract 2, we'll add 2; and of course whatever we do on the left side we also need to do on the right side, so after the first step, our equation looks like this:

\begin{equation}3x - 2 + 2 = 10 + 2 \end{equation}

Now the -2 and +2 on the left cancel one another out, and on the right side, 10 + 2 is 12; so the equation is now:

\begin{equation}3x = 12 \end{equation}

OK, time for step two - we need to deal with the *coefficients* - a coefficient is a number that is applied to a variable. In this case, our expression on the left is 3x, which means x multiplied by 3; so we can apply the opposite operation to cancel it out as long as we do the same to the other side, like this:

\begin{equation}\frac{3x}{3} = \frac{12}{3} \end{equation}

3x &divide; 3 is x, so we've now isolated the variable

\begin{equation}x = \frac{12}{3} \end{equation}

And we can calculate the result as <sup>12</sup>/<sub>3</sub> which is **4**:

\begin{equation}x = 4 \end{equation}

Let's verify that result using Python:


```python
x = 4
3*x - 2 == 10
```




    True



## Combining Like Terms
Like terms are elements of an expression that relate to the same variable or constant (with the same *order* or *exponential*, which we'll discuss later). For example, consider the following equation:

\begin{equation}\textbf{5x} + 1 \textbf{- 2x} = 22 \end{equation}

In this equation, the left side includes the terms **5x** and **- 2x**, both of which represent the variable **x** multiplied by a coefficent. Note that we include the sign (+ or -) in front of the value.

We can rewrite the equation to combine these like terms:

\begin{equation}\textbf{5x - 2x} + 1 = 22 \end{equation}

We can then simply perform the necessary operations on the like terms to consolidate them into a single term:

\begin{equation}\textbf{3x} + 1 = 22 \end{equation}

Now, we can solve this like any other two-step equation. First we'll remove the constants from the left side - in this case, there's a constant expression that adds 1, so we'll use the opposite operation to remove it and do the same on the other side:

\begin{equation}3x + 1 - 1 = 22 - 1 \end{equation}

That gives us:

\begin{equation}3x = 21 \end{equation}

Then we'll deal with the coefficients - in this case x is multiplied by 3, so we'll divide by 3 on boths sides to remove that:

\begin{equation}\frac{3x}{3} = \frac{21}{3} \end{equation}

This give us our answer:

\begin{equation}x = 7 \end{equation}


```python
x = 7
5*x + 1 - 2*x == 22
```




    True



## Working with Fractions
Some of the steps in solving the equations above have involved working wth fractions - which in themselves are actually just division operations. Let's take a look at an example of an equation in which our variable is defined as a fraction:

\begin{equation}\frac{x}{3} + 1 = 16 \end{equation}

We follow the same approach as before, first removing the constants from the left side - so we'll subtract 1 from both sides.

\begin{equation}\frac{x}{3} = 15 \end{equation}

Now we need to deal with the fraction on the left so that we're left with just **x**. The fraction is <sup>x</sup>/<sub>3</sub> which is another way of saying *x divided by 3*, so we can apply the opposite operation to both sides. In this case, we need to multiply both sides by the denominator under our variable, which is 3. To make it easier to work with a term that contains fractions, we can express whole numbers as fractions with a denominator of 1; so on the left, we can express 3 as <sup>3</sup>/<sub>1</sub> and multiply it with <sup>x</sup>/<sub>3</sub>. Note that the notation for mutiplication is a **&bull;** symbol rather than the standard *x* multiplication operator (which would cause confusion with the variable **x**) or the asterisk symbol used by most programming languages.

\begin{equation}\frac{3}{1} \cdot \frac{x}{3} = 15 \cdot 3 \end{equation}

This gives us the following result:

\begin{equation}x = 45 \end{equation}

Let's verify that with some Python code:


```python
x = 45
x/3 + 1 == 16
```




    True



Let's look at another example, in which the variable is a whole number, but its coefficient is a fraction:

\begin{equation}\frac{2}{5}x + 1 = 11 \end{equation}

As usual, we'll start by removing the constants from the variable expression; so in this case we need to subtract 1 from both sides:

\begin{equation}\frac{2}{5}x = 10 \end{equation}

Now we need to cancel out the fraction. The expression equates to two-fifths times x, so the opposite operation is to divide by <sup>2</sup>/<sub>5</sub>; but a simpler way to do this with a fraction is to multiply it by its *reciprocal*, which is just the inverse of the fraction, in this case <sup>5</sup>/<sub>2</sub>. Of course, we need to do this to both sides:

\begin{equation}\frac{5}{2} \cdot \frac{2}{5}x = \frac{10}{1} \cdot \frac{5}{2} \end{equation}

That gives us the following result:

\begin{equation}x = \frac{50}{2} \end{equation}

Which we can simplify to:

\begin{equation}x = 25 \end{equation}

We can confirm that with Python:


```python
x = 25
2/5 * x + 1 ==11
```




    True



## Equations with Variables on Both Sides
So far, all of our equations have had a variable term on only one side. However, variable terms can exist on both sides. 

Consider this equation:

\begin{equation}3x + 2 = 5x - 1 \end{equation}

This time, we have terms that include **x** on both sides. Let's take exactly the same approach to solving this kind of equation as we did for the previous examples. First, let's deal with the constants by adding 1 to both sides. That gets rid of the -1 on the right:

\begin{equation}3x + 3 = 5x \end{equation}

Now we can eliminate the variable expression from one side by subtracting 3x from both sides. That gets rid of the 3x on the left:

\begin{equation}3 = 2x \end{equation}

Next, we can deal with the coefficient by dividing both sides by 2:

\begin{equation}\frac{3}{2} = x \end{equation}

Now we've isolated x. It looks a little strange because we usually have the variable on the left side, so if it makes you more comfortable you can simply reverse the equation:

\begin{equation}x = \frac{3}{2} \end{equation}

Finally, this answer is correct as it is; but <sup>3</sup>/<sub>2</sub> is an improper fraction. We can simplify it to:

\begin{equation}x = 1\frac{1}{2} \end{equation}

So x is 1<sup>1</sup>/<sub>2</sub> (which is of course 1.5 in decimal notation).
Let's check it in Python:


```python
x = 1.5
3*x + 2 == 5*x -1
```




    True



## Using the Distributive Property
The distributive property is a mathematical law that enables us to distribute the same operation to terms within parenthesis. For example, consider the following equation:

\begin{equation}\textbf{4(x + 2)} + \textbf{3(x - 2)} = 16 \end{equation}

The equation includes two operations in parenthesis: **4(*x* + 2)** and **3(*x* - 2)**. Each of these operations consists of a constant by which the contents of the parenthesis must be multipled: for example, 4 times (*x* + 2). The distributive property means that we can achieve the same result by multiplying each term in the parenthesis and adding the results, so for the first parenthetical operation, we can multiply 4 by *x* and add it to 4 times +2; and for the second parenthetical operation, we can calculate 3 times *x* + 3 times -2). Note that the constants in the parenthesis include the sign (+ or -) that preceed them:

\begin{equation}4x + 8 + 3x - 6 = 16 \end{equation}

Now we can group our like terms:

\begin{equation}7x + 2 = 16 \end{equation}

Then we move the constant to the other side:

\begin{equation}7x = 14 \end{equation}

And now we can deal with the coefficient:

\begin{equation}\frac{7x}{7} = \frac{14}{7} \end{equation}

Which gives us our anwer:

\begin{equation}x = 2 \end{equation}

Here's the original equation with the calculated value for *x* in Python:


```python
x = 2
4*(x + 2) + 3*(x - 2) == 16
```




    True


