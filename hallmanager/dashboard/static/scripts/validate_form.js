function validatePassword() {
    console.log("Hello");
    const pass = document.getElementById("password").value;
    const confPass = document.getElementById("confpass").value;
    const error = document.getElementById("form-error");
    if (pass < 8) {
        error.innerText = "Password must have a minimum length of 8 character";
        return;
    }
    if (pass > 16) {
        error.innerText = "Password can have a maximum length of 16 character";
        return;
    }
    if (pass !== confPass) {
        error.innerText = "Password and Confirm Password don't match";
        return;
    }
}