# Circle Loop✨

For this exercise I mainly modified last semester's 3D graphics assignment and added modifiers to modify the number of graphics and their orientation in the x, y, and z-axis in real time. It is worth mentioning that because I put in the z-axis, I can convert flat 2D graphics to 3D when using the mouse.

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%202%20Exercise%20-%20Your%20first%20OF%20project/Images/Final%20work/mix.png)  

You can try it through download the **CircleLoop.xcodeproj.zip** file

You can watch the demo video through this link：https://youtu.be/lrOSLaOZkK4

## OpenFrameworks

OpenFrameworks is a library of classes written in the computer programming language C ++ that help facilitate fast and efficient coding of applications primarily for artistic expression or experimentation. Also OpenFrameworks is designed as a cross-platform library, so programs using the code can be compiled on almost any operating system and can run on certain mobile devices. This could lead to many possibilities, especially in the process of instilling digital art into galleries, where viewers could download the displayed interactive artwork to their mobile devices for later viewing. Another benefit of cross-platform is the ability to integrate unique input devices (such as touch screens) on handheld devices or 3D motion tracking cameras on game consoles.

# Knowledge Expansion💫
This week started with C++ and I explored mainly about pointers.🎱

## What exactly is a pointer? Is it an address? Or is it a type?

Question:

Regarding pointers, there are two schools of thought.
1. Address school: output with `%p` , get the address, so the pointer is the **address**. `int * p` , `p` is a pointer type variable that holds the address, **so the pointer is the address**. This is the same reason as int-type variables store int-type data.
2. non-address school: think pointer is a **type**, both our understanding in programming and the international standard is to prove that pointer is type, especially the international standard has said very clearly that pointer is type.

*So I have a question, both of them are right in what they say, so what exactly is a pointer?*

### Here's an answer that I think is easy to understand📝

* **Declaring a variable**: When a variable is declared in C, the compiler sets aside a unique address cell in memory to store the variable, as shown in the figure below. The variable var is initialized to 100 and the compiler leaves the memory cell at address 1004 for the variable and associates the address 1004 with the name of the variable.

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%202%20Exercise%20-%20Your%20first%20OF%20project/Images/Example%20diagrams/1.png)  

* **Create a pointer**: The address of the variable var is 1004, which is a number. This number of the address can be saved with another variable for it. Suppose this variable is p. At this time, the variable p is not initialized and the system allocates space for it, but the value is not yet determined, as shown in the following figure.

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%202%20Exercise%20-%20Your%20first%20OF%20project/Images/Example%20diagrams/2.png) 

* **Initializing a pointer**: Storing the address of a variable var into a variable p. After initialization `(p=&var)`, p points to var and is called a pointer to var. A pointer is a variable that stores the address of another variable.

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%202%20Exercise%20-%20Your%20first%20OF%20project/Images/Example%20diagrams/3.png) 

* **Declare pointer**: typename `*p` where typename refers to the variable type of var, can be short, char, float, because each type occupies different memory bytes, short occupies 2 bytes, char occupies 1 byte, float occupies 4 bytes, the value of the pointer is equal to the address of the first byte of the variable it points to . `*` is an indirect operator, indicating that `p` is a pointer variable, as distinguished from a non-pointer variable.

* `*p` and var refer to the contents of var; `p` and `&var` refer to the address of var

![image](https://github.com/YuchenTan777/CCI-S2-Coding-Two/blob/main/Week%202%20Exercise%20-%20Your%20first%20OF%20project/Images/Example%20diagrams/4.png) 

### Since the value of pointer `*p` is equal to var,`p` is equal to `&var`, why invent this one more pointer symbol to increase the amount of memory.

**There are two main functions of a pointer: avoiding copies and sharing data.**

**The important function of a pointer is to pass parameters between functions.**

Reference :https://www.zhihu.com/question/31022750

