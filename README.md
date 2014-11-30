TSS Python API
==============

### Why it is written in Python?
Python is a very useful scripting language. It's fast, lightweight and easy to understand. I decided to write this library in Python for many purposes. You can modify it almost immediately, without problems. Also you can hook it into your C/C++/Obj-C projects without any issues, plus it has been super quick to write and debug. 
So the real question would be: why it is **NOT** written in Python? 

Introduction
------------

A super-quick Python implementation for iNeal's TSS API. Written entirely in Python, it can also be hooked into your own C/C++/Objective-C libraries.

Features:

- **low-level functions**: Used to request and return JSON data from TSS.
- ~~**wrapper functions**: Used to convert JSON into more complex data structures. (dictionaries, arrays, etc.)~~ *(To be implemented ASAP)*
- ~~**high-level functions**: Used to directly interface with the user.~~ *(To be implemented ASAP)*

Usage
-----

To use into your own Python files, simply import the module first:

  `from TSSAPI import *`

Then you can simply call the functions. Error handling is already done for you by low-level functions.

Hooking into higher-level languages
-----------------------------------

There are some ways to execute Python code from a C environment. The best one IMO is using the `Python.h` header file. This one lets you interface directly with the Python interpreter, and execute Python code. You can even use multithreading! Here's an example:

```
void exec_pycode(const char* code) {
  Py_Initialize(); // init the interpreter
  PyRun_SimpleString(code); // execute the code
  Py_Finalize(); // finalize the interpreter
}
```

We can get a function from a module in a very simple way:

```
... init code ...

pName = PyString_FromString(const char *s);
pModule = PyImport_Import(pName);
pDict = PyModule_GetDict(pModule);
pFunc = PyDict_GetItemString(pDict, const char *s2);

if (PyCallable_Check(pFunc)) { // is the function callable?
  PyObject_CallObject(pFunc, NULL);
} else {
  PyErr_Print();
}

// clean up
Py_DECREF(pModule);
Py_DECREF(pName);

... finalizing code ...
```

As you can see, the code is extremely readable and easy to comprehend. If you want more details, you can look at this very well-made guide: http://www.codeproject.com/Articles/11805/Embedding-Python-in-C-C-Part-I.

Suggestions
-----------

This section will suggest some addiction you could make by yourself to make the library better. Some of these are planned to be implemented in the next versions.

1. _Save requests to disk_ - These requests are very heavy. The JSON that you get in response is much data, and this could slow down you program, especially if the user has a slow connection or iNeal server is overloaded. I *highly* suggest you to implement a disk-saving feature, to avoid redundant requests. _**This feature will be added in the next versions.**_
