
inst = """Instruction: You will be given a math problem. Think step by step to solve the problem, and give the final answer in \\boxed{} tags.

Problem: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Solution: If Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May, we need to calculate how many she sold in May and then add that to the number she sold in April to find the total.

Half of 48 is calculated as follows:
48 / 2 = 24

So, Natalia sold 24 clips in May.

Now, to find the total number of clips sold in April and May, we add the two amounts together:
48 (April) + 24 (May) = 72

Natalia sold a total of 72 clips in April and May combined.
Final Answer: The answer is $\\boxed{72}$."""

# answer: 60
prompt_without_retrieval_1 = inst + """\n\nProblem: What is the greatest common divisor of all integers that can be represented as $k^6-k^2$, where k is a positive integer?"""

prompt_with_retrieval_1 = inst + """\n\nProblem: What is the greatest common divisor of all integers that can be represented as $k^3-k$, where k is a positive integer?

Solution: When $k=2$, the expression is equal to $2^3-2=6$. Next, note that $k^3-k=k(k-1)(k+1)$. This is divisible by 2, because one of $k$ and $k+1$ has to be divisible by $2$. This is also divisible by $3$ because one of $k-1, k, k+1$ is divisible by $3$. Therefore, it must be divisible by $6$. 
Final Answer: The final answer is $\\boxed{6}$.
 
Problem: What is the greatest common divisor of all integers that can be represented as $k^6-k^2$, where k is a positive integer?"""

# answer: 506
prompt_without_retrieval_2 = inst + """\n\nProblem: How many divisors of $6^2023$ have a units digit of $1$?"""

prompt_with_retrieval_2 = inst + """\n\nProblem: How many divisors of $10^{100}$ have a units digit of $5$?
Solution: We have that $10^{100} = 2^{100} \cdot 5^{100}$. If a divisor of $10^{100}$ is even, then it cannot have a units digit of $5$.

Therefore, all divisors with a units digit of $5$ must be of the form $5^{k}$, for $k=1, 2, \cdots, 100$. Therefore, thre are 100 divisors of $10^{100}$ with a units digit of $5$.
Final Answer: The final answer is $\\boxed{100}$.

Problem: How many divisors of $6^{2023}$ have a units digit of $1$?"""

# answer: 5
prompt_without_retrieval_3 = inst + """\n\nProblem: How many ordered pairs $(m, n)$ of positive integers satisfy $m^n = 6^{16}$?"""

prompt_with_retrieval_3 = inst + """\n\nProblem: How many ordered pairs $(x, y)$ of positive integers satisfy $x^y = 4^{10}$?

Solution: We have that $x^y = 4^{10} = 2^{20}$. Note that $x$ must be a power of $2$, because $2^{20}$ has no other prime factors. Therefore, we can have $x=2^a$, so that $x^y = 2^{ay} = 2^{20}$. 

Here, $a$ and $y$ can be anything, as long as $ay = 20$. Therefore, we just need to count the factors of $20$: $1, 2, 4, 5, 10, 20$, so the answer is 6.
Final Answer: The final answer is $\\boxed{6}$.

Problem: How many ordered pairs $(m, n)$ of positive integers satisfy $m^n = 6^{16}$?"""

prompt_without_retrieval_4 = inst + """\n\nProblem: Determine the least positive integer $n$ for which the following statement is true: the product of any $n$ odd consecutive positive integers is divisible by $45$."""

prompt_with_retrieval_4 = inst + """Problem: What is the least $n$ such that the product of any $n$ even consecutive positive integers is divisible by $56$?

Solution: If something is divisible by $56$, then it must be divisible by $8$ and $7$. 

We know that for $n \ge 3$, the product will be divisible by $8$, because each integer is even.

Now, for the product to be divisible by $7$, one integer must be a multiple of $7$. Note that for any $7$ consecutive even integers, one must be divisible by $7$.

Therefore, when $n=7$, the statement is true. For $n=6$, observe that $2 \cdot 4 \cdot 6 \cdot 8 \cdot 10 \cdot 12$ is not divisible by $56$, because none of the integers is divisible by $7$.

Final Answer: The final answer is $\\boxed{7}$.

Problem: Determine the least positive integer $n$ for which the following statement is true: the product of any $n$ odd consecutive positive integers is divisible by $45$."""
# prompt_without_retrieval_4 = inst + """\n\nProblem: What is the least possible positive sum of three integers multiplying to 2025? The integers are not necessarily positive."""

# prompt_without_retrieval_3 = inst + """\n\nProblem: How many ordered pairs $(m, n)$ of positive integers satisfy $m^n = 6^{16}$?"""
