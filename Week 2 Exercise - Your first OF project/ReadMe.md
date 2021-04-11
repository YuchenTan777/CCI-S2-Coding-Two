This week started with C++ and I explored mainly about pointers.🎱

## What exactly is a pointer? Is it an address? Or is it a type?

Question:

Regarding pointers, there are two schools of thought.
1. Address school: output with `%p` , get the address, so the pointer is the **address**. `int * p` , `p` is a pointer type variable that holds the address, **so the pointer is the address**. This is the same reason as int-type variables store int-type data.
2. non-address school: think pointer is a **type**, both our understanding in programming and the international standard is to prove that pointer is type, especially the international standard has said very clearly that pointer is type.

*So I have a question, both of them are right in what they say, so what exactly is a pointer?*

### Here's an answer that I think is easy to understand📝

1.Declaring a variable: When a variable is declared in C, the compiler sets aside a unique address cell in memory to store the variable, as shown in the figure below. The variable var is initialized to 100 and the compiler leaves the memory cell at address 1004 for the variable and associates the address 1004 with the name of the variable.

