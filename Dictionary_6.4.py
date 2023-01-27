Glossary = {
    "Debugging": "The process of identifying and removing errors from computer hardware or software",
    "Refactoring": "Restructure (the source code of an application or piece of software) so as to improve operation without altering functionality.",
    "Object Oriented Programming": "A programming paradigm based on the concept of 'objects', which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).",
    "Polymorphism": "A feature of a programming language that allows routines to use variables of different types at different times.",
    "Recursion": "The process of defining a problem (or the solution to a problem) in terms of (a simpler version of) itself.",
    }

Glossary["Compiling"] = "The transformation from Source Code (human readable) into machine code (computer executable)."
Glossary["Interpreter"] = "A computer program that directly executes instructions written in a programming or scripting language, without requiring them previously to have been compiled into a machine language program." 

for key, value in Glossary.items():
    print(key+":")
    print(f"\t{value}\n")

    
