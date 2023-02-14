# Hot-or-Cold-Game
My first attempt to learn Object Oriented Programming (OOP) through project.

How it works:
Simply run the entire script by pressing F5 (for Anaconda Spyder) or other keys to run the script in other IDEs.
The only input you will need to make in the console is any number between 1 to 100.
You can try any other inputs, there are special comments for them.

Inner workings:
When user gives an input number, the script will check whether the randomly generated number matches with the input.
The game ends when both numbers matches.
However, if input number does not match with generated number, it will determine the distance of input number from the generated number.
A hot or cold response will be dependent on the distance.
The user will then be prompted to input another number.
If the number does not match after first attempt, any subsequent attempts will check if the distance from the newer input is larger or smaller than the previous input.
Previous input value will also be included for easy reference.
