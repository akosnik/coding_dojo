
var possibilities = 5;
function d6(possibilities) {

    for (var i = 0; i < 10000; i++) {
        var roll = Math.ceil(Math.random() * possibilities)
        console.log("The player rolled: " + roll);
    }
    return roll;
}


ee