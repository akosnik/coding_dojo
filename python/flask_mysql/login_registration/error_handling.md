your_function() is not defined.
* could be a typo, check where you defined it, check where you called it
* could be a scope issue
    * class methods need to be accessed like User.your_function()
    * you may need to check your import route, did you import the file, or the actual class

your_function expected more or less arguments
* you forgot to pass it the argument when you called it
    * check the function definition for all necessary parameters
* you accidently passed it an extra argument
    * check where you called the function

your server won't start
* likely is a typo/indent
    * follow the call stack of information, look for files that you wrote and check the line

