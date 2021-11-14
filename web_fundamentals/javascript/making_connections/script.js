console.log("page loaded...");

var profileName = document.getElementById("profile-name");

function editProfileName() {
    profileName.innerHTML = "Joann Fabrika";
}

var requests = 2;

function removeRequester(index) {
    document.getElementById("requester" + index).remove();

    var requestCount = document.querySelector(".card-header .badge");
    requestCount.innerHTML = --requests;
}