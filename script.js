function validateForm() {
    let inputs = document.querySelectorAll('input');
    for (let input of inputs) {
        if (isNaN(input.value) || input.value === '') {
            alert('Please enter valid numeric values');
            return false;
        }
    }
    return true;
}
