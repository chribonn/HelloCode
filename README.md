# Welcome to HelloCode

Anyone who has ever peaked at a programming language would have come across the famous "Hello, World!" program. It is the universally accepted first code to delicately introduce someone to a language. It helps beginners execute a program that outputs a phrase on their console, providing reassurance that the interpreter or compiler is working and can execute the source code. "Hello, World!" is so universally acceptable that today certain editors will initialize a new program with this code. Programmers then replace the output command with their own code.

HelloCode is intended to be the next step of the "Hello" family of code intended to familiarise a developer with a particular language.  This is no easy task as no single block of code, will ever turn a person into an expert. The aim of the HelloCode project is to raise the bar, making a newbie aware of the development ecosystem of the language they are exploring and introducing them to a function-calling solution that references a package.

HelloCode projects:
* Uses the console thereby ensuring the resulting output is independent of particular hardware and will not change if the hardware changes;
* Introduces variables, arrays and constants. While the core set of constants and variables will be named the same, they will be adjusted to reflect the naming conventions of the language;
* Introduce procedures. While there may be additional procedures in a solution, one procedure called *Show Result* will be responsible for console output.
* Makes new developers aware that the programming language can be extended through the use of external libraries/packages (the term "package" will be used from this point onwards);
* Demonstrates package managers and how to install packages;
* Demonstrates how to incorporate a module in one's code;
* Demonstrates how to create a file that allows the code to be distributed with package information.



# What is HelloCode?

HelloCode is designed to introduce you to the capabilities possible in the programming language of your choice. Every HelloCode program performs an identical task and produces the same output.

Each HelloCode program will call a PBKDF2 key derivation function using the SHA256 hash function to create a hash value. This hash value is then converted to hexadecimal and Base64. The subject matter falls within the realm of cryptography. HelloCode will not teach you cryptography or numbering systems. For more information on these topics, refer to the links below:

* PBKDF2, https://en.wikipedia.org/w/index.php?title=PBKDF2&oldid=1226427534.
* SHA-2, https://en.wikipedia.org/w/index.php?title=SHA-2&oldid=1239730727.
* Hexadecimal, https://en.wikipedia.org/w/index.php?title=Hexadecimal&oldid=1241204322.
* Base64, https://en.wikipedia.org/w/index.php?title=Base64&oldid=1238321958.

Because every HelloCode program uses identical initial values the output of every HelloCode program will be identical. This highlights how algorithms, once defined, are implemented across programming languages.


# HelloCode Programs 

Every HelloCode program will:

* Introduce you to a subset of data types supported by your programming language (the list is not exhaustive).
* Familiarize you with procedures/functions, henceforth referred to as routines. Some solutions may have multiple routines, but every HelloCode program will have one called **Show Result** that outputs the result to the console and returns TRUE if the computed value matches the expected value (otherwise FALSE). For more information on routines, you can refer to [Procedural programming](https://en.wikipedia.org/w/index.php?title=Procedural_programming&oldid=1239348683).
* Introduce you to the naming conventions commonly used in your environment. This applies to constants, variables, routines, and program names.
* Show the placement of routines with respect to the main module that is invoked when the program is executed.
* Make you aware of package managers for your programming language (in certain environments, these are called libraries).
* Demonstrate how to install a package and invoke it in your code.
* Where applicable, explain tools available with the language to create a list of the packages required by your project. When you distribute your program, others can install the dependent packages from this file.


# The structure of a HelloCode program

Every HelloCode program defines the following constants/variables (variables if the language does not support constants):
* *Programming Language (Constant)*
* *Expected Base64 Result (Constant)*
* *Password*
* *Salt*
* *Iteration*
* *Key Length*
* *Key*
* *Base64 Encoded Key*

The program initializes *Programming Language*, *Password*, *Salt* and *Iteration* and *Expected Base64 Result* with fixed values.

It then calls the PBKDF2 function using the SHA256 hash to generate a *Key* based on *Programming Language*, *Password*, *Salt* and *Iteration*.

The **Show Result** module is called. This module will:
* Convert *Key* to *Base64 Encoded Key*
* Output to the console:
    * *Programming Language*
    * *Key* (as a hexadecimal)
    * *Base64 Encoded Key*

If *Base64 Encoded Key* is identical to *Expected Base64 Result* a value of TRUE, otherwise FALSE, is returned to the calling routine.


# Why are the multiple programs for a particular language?

Some programming languages have multiple packages that perform the same task. Different contributors to this project have used different packages and each package is contained in its own project. The name of the folder highlights the packages that that particular solution invokes.  If multiple packages have been installed, the project name will list them in alphabetical order, separated using *\$\_\$*. 