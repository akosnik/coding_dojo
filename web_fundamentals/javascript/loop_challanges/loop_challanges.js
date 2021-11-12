
console.log("Print odd numbers 1-20:");
printOdds();
console.log("\n ---------------------- \n")

console.log("Print decreasing multiples of 3:");
decreasingMultiples();
console.log("\n ---------------------- \n")

console.log("Print the sequence:");
printSequence();
console.log("\n ---------------------- \n")

console.log("Sigma - Sum values 1-100:");
sigma();
console.log("\n ---------------------- \n")

console.log("Factorial - multiply values 1-12");
factorial();
console.log("\n ---------------------- \n")

function printOdds() {
    for (var i = 1; i <= 20; i++) {
        if (i % 2 != 0) {
            console.log(i);
        }
    }
}

function decreasingMultiples() {
    for (var i = 100; i >= 0; i--) {
        if (i % 3 == 0) {
            console.log(i);
        }
    }
}

function printSequence() {
    for (var i = 4; i > -4; i -= 1.5) {
        console.log(i);
    }
}

function sigma() {
    var sum = 0;
    for (var i = 0; i <= 100; i++) {
        sum += i;
    }
    console.log(sum);
}

function factorial() {
    var product = 1;
    for (var i = 1; i <= 12; i++) {
        product *= i;
    }
    console.log(product);
}
