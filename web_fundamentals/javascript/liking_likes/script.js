var counts = [0, 0, 0];
var counters = [
    document.querySelector("#counter1"),
    document.querySelector("#counter2"),
    document.querySelector("#counter3")
]


function liked(index) {
    counts[index]++;
    counters[index].innerHTML = counts[index] + " like(s)";
}