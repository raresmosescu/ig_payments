function register(email, password) {
  firebase.auth().createUserWithEmailAndPassword(email, password)
  .then((userCredential) => {
    // Signed in 
    var user = userCredential.user;
    // ...
  })
  .catch((error) => {
    var errorCode = error.code;
    var errorMessage = error.message;
    // ..
  });
}

function login(email, password) {
  firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // Signed in
      var user = userCredential.user;
      return user;
    })
    .catch((error) => {
      var errorCode = error.code;
      var errorMessage = error.message;
      console.log(errorCode + "\n" + errorMessage);
      return false;
    });
}


function logout() {
  firebase.auth().signOut().then(() => {
    // Sign-out successful.
  }).catch((error) => {
    // An error happened.
  });
}


function isAuthenticated() {
  const user = firebase.auth().currentUser;
  if (user) {
    return true;
  } else {
    return false;
  }
}

function grantAccess(user) {
  if (user) {
    // If there's any login-status elements on page, update them with the login status. If not, skip to the next block of code.
    login_status = document.getElementById("login-status");
    if (login_status) {
        login_status.innerHTML = "You're logged in as: " + user.email;
    }

    // show all .authenticated elements and remove all .not-authenticated elements
    document.querySelectorAll('.authenticated').forEach(elem => {
        elem.style.display = "block"
    });
    document.querySelectorAll('.not-authenticated').forEach(elem => {
        elem.style.display = "none"
    }); 
    } else {
    document.getElementById("message").innerHTML = "No user signed in.";
    document.querySelectorAll('.authenticated').forEach(elem => {
        elem.style.display = "none"
    });
    document.querySelectorAll('.not-authenticated').forEach(elem => {
        elem.style.display = "block"
    });
    }

}