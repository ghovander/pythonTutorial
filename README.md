# Python Tutorial
## Why Learn Python
* Solve complex problems in less time with fewer lines of code
* Used for Data Analysis, AI/Machine Learning, Automation Scripts, Web Apps, Mobile Apps, Desktop Apps, Software Testing, Hacking
* High Level language
* Huge community
* Cross-platform
* Large ecosystem  

## Versions of Python
* Python 2 - Legacy (Support up to 2020)
* Python 3 - Future

## IDE
* Includes Features such as Autocompletion, Debugging, Unit Testing, Linting (Static analysis code for potential errors), Code Formatting, Code Snippets
* Popular: PyCharm

## Code Editor
* Popular: VSCode, Atom, Sublime

## Python Enhancement Proposals (PEP)

## Python Implementations (Compilers) -> Python ByteCode
* CPython - C
* Jython - Java
* IronPython - C#
* PyPy - Subset of Python

Python ByteCode is processed by Python Virtual Machine and instructions are sent to the Kernel

## Variable Names
* Should always be descriptive and meaningful
* always use lowercase with underscore

## Escape Sequences
* Escape Character = \
* Escape Sequences = \\", \\', \\\\, \n

## Primitive Types
* Strings
* Numbers
  * Int
  * Float
  * Complex Numbers
* Booleans

## Types of Functions
* Perform a task
* Return a value

## Stack
* LIFO - Last In First Out

## Queue
* FIFO - First In First Out

## Tuples
* Readonly List
* Used to contain a sequence of objects 
  
## Set
* A collection without duplicates
* Unordered - Cannot access value by index

## Note
* An object that represents the absense of a value

## Class
* A blueprint for creating new objects

## Object
* An instance of a class
* Objects are dynamic like Javascript, meaning you can add attributes after the object has been created

## Object Data
* Attributes (like Fields in other languages)
* Can be be private if prefixed with two underscores. However, they can be accessed by looking up the key in the __dict__ magic method.

## Magic Methods
* Built-in methods that are called by the Python interpreter
* Documentation: https://rszalski.github.io/magicmethods/

## Base Class
* object is the base class for all classes in Python

## Method Overriding
* Replacing or extending the method in the base class

# Empty Method
* Must have at least one statement in a method so "pass" allows nothing to be defined

## Inheritance
* Multi-Level Inheritance is bad because it increase software complexity and will introduce bugs
* At most, there should only be 2 levels of inheritance
* Multiple Inheritance should be used with objects that are not related/inheriting from one another

## Modules
* Should contain highly related objects
* Module loaded from the CLI is always reloaded. However, the dependent modules will only be reloaded if the module file is newer than the compiled version of the module.

## Package
* A container for 1 or more modules
* Python recognizes directory as package if __init__.py file found