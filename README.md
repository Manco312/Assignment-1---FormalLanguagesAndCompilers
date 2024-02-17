# Assignment-1---FormalLanguagesAndCompilers

**Group members:** Juan José Gómez Vélez and Santiago Manco Maya

## The DFA (Deterministic finite automaton) given by Professor Sergio Ramirez Rico:

![image](https://github.com/Manco312/Assignment-1---FormalLanguagesAndCompilers/assets/129436458/15363993-4314-46bf-91e5-12b457c9c195)

The assignment was to implement this automaton using any programming language and a library that allows to directly code a DFA.

## Versions and Programming Language

**Version of the OS used:** Windows 11.
**Programming Language:** Python 3.10.12
**Tools:** IDE Pycharm 2023.2.1 and automata-lib library that **requires Python 3.8 or newer versions**.

## Convention for the empty string

The convention used for representing the empty string was: 'e'

## Instructions for running the implementation

**1.** Download the zip file from EAFIT Interactiva.
**2.** Unzip the file and use the cd command in the console to access the folder where the file binary3.py is located.
**3.** Use the next command to install the library automata-lib:
```
py -m pip install automata-lib
```
**4.** Run the binary3.py file by using the next command:
```
py binary3.py
```
**5.** Now you can enter a string and check if the automaton accepts it or not
```
1111
The DFA accepts the string ’1111’
```

```
101
The DFA rejects the string ’101’
```

```
e
The DFA accepts the string ’e’
```



