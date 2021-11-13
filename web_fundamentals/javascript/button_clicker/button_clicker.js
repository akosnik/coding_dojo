function removeButton(element) {
    element.remove();
}

function loginEvent(element) {
    if (element.value == 'Login') {
        return element.value = 'Logout';
    }
    element.value = 'Login';
}

function liked() {
    alert('Ninja was liked');
}