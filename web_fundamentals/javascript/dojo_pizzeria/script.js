
function pizzaOven(crust, sauce, cheese, toppings) {
    var pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheese = cheese;
    pizza.toppings = toppings;
    return pizza;
}

var myPizza = pizzaOven("deepdish", "marinara", "mozzarella", ["spinach", "mushroom"]);
console.log(myPizza);
