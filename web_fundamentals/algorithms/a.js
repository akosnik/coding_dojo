

// Create a function called isPal that takes in an array
function isPal(arr) {
    // in a for loop: create a var left start at 0, itterate through half of the array, increment each loop by 1
    for (var left = 0; left < arr.length / 2; left++) {
        // we declare a variable right and set it equal to the array length minus 1,
        // minus the value of left
        var right = arr.length - 1 - left;
        // a conditional if statement compares if the array at the left index is 
        // not equal to the array coming from the right index
        if (arr[left] != arr[right]) {
            // if the conditional is true, we will return the string "not a pal-indrome"
            return "Not a pal-indrome!";
            // close the if conditional
        }
        // the for loop ends
    }
    // if the condition is not met, the return statement will run and finish the function
    return "Pal-indrome!";
    // closes the function declaration
}


var result1 = isPal([1, 1, 2, 2, 1]);
console.log(result1);

var result2 = isPal([3, 2, 1, 1, 2, 3]);
console.log(result2);