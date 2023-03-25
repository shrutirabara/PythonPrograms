import pythonModules.moduleExercise as moduleExercise
'''
This program take two simple functions and places them in a python module named moduleExercise.py.
A message is printed when the module is imported and another when the module is run directly. 
Main.py imports these functions, asks the user which function they would like to run and executes the corresponding function.
The program utilizes Python modules, importing, module scripting and "compiled" Python files!
'''

print("Welcome to the my program!")
print("Which operation would you like to perform?")
print("1. Simple Hello World")
print("2. An amazing Rock, Paper, Scissors Game")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("Starting Hello World Function:")
    result = moduleExercise.helloWorld()

if choice == "2":
    print("Starting RPS Game Function:")
    result = moduleExercise.rpsGame()
