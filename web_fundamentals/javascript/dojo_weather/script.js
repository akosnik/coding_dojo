function cityAlert() {
    alert("Loading weather report...")
}

var forecast = {
    "today": [24, 18],
    "tomorrow": [27, 19],
    "friday": [21, 16],
    "saturday": [26, 21]
}

function convert() {
    var days = Object.keys(forecast);           //MEMORIZE THIS days = ["today", "tomorrow", ]
    for (var i = 0; i < days.length; i++) {
        var hi = forecast[days[i]][0];          //UTILIZE NESTED INDECIES
        var low = forecast[days[i]][1];

        if (isFahr()) {
            hi = convertFahr(hi);
            low = convertFahr(low);
        }

        var hiElement = document.querySelector("#" + days[i] + " .hi");
        var lowElement = document.querySelector("#" + days[i] + " .low");

        hiElement.innerHTML = (hi + "&deg");
        lowElement.innerHTML = (low + "&deg");
    }
}

function isFahr() {
    //default celcius
    return document.getElementById("units").value == "f"
}

function convertFahr(celcius) {
    return Math.round(celcius * 9 / 5 + 32);
}

function removeCookie() {
    document.getElementById("cookie-alert").remove();
}


