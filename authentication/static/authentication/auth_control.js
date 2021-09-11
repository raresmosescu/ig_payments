function check_password() {
    p1 = document.getElementById('password').value;
    p2 = document.getElementById('password2').value;
    if (p1.length >= 8 && p2.length >= 8) {
        if (p1 == p2) {
            document.getElementById('password-match-fail').style.display = "none";
            document.getElementById('password-match-success').style.display = "block";
            document.getElementById('submit-button').disabled = false;
        }
        else {
            document.getElementById('password-match-fail').innerHTML = "Passwords don't match"
            document.getElementById('submit-button').disabled = true;
            document.getElementById('password-match-fail').style.display = "block";
            document.getElementById('password-match-success').style.display = "none";
        }
    }
    else {
        document.getElementById('password-match-fail').style.display = "block";
        document.getElementById('password-match-success').style.display = "none";
        document.getElementById('password-match-fail').innerHTML = "Password must contain at least 8 characters"
    }
}