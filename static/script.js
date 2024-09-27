let coinBalance = 0;
let tapIncrement = 1; // Starting increment for level 1

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "tinubucoin-af37b.firebaseapp.com",
    databaseURL: "https://tinubucoin-af37b.firebaseio.com",
    projectId: "tinubucoin-af37b",
    storageBucket: "tinubucoin-af37b.appspot.com",
    messagingSenderId: "352329915377",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);
const database = firebase.database();

function saveUserData(userId, username, profilePic) {
    database.ref('users/' + userId).set({
        username: username,
        profilePic: profilePic
    });
}

function getUserData(userId) {
    database.ref('users/' + userId).once('value').then((snapshot) => {
        const data = snapshot.val();
        if (data) {
            const username = data.username;
            const profilePic = data.profilePic;
            // Display the username and profile picture in your app
        }
    });
}


document.addEventListener('DOMContentLoaded', async () => {
    const userId = /* Retrieve the user ID from the session or URL */;
    
    const response = await fetch(`/user/${userId}`);
    const userData = await response.json();

    document.getElementById('profile-pic').src = `https://api.telegram.org/file/bot<7773928774:AAEA60tg3ZmtwVLXF2iLJBKT80bR00pvEtM>/${userData.profile_photo}`;
    document.getElementById('username').innerText = userData.username;
});


document.getElementById("tapCircle").addEventListener("click", function() {
    coinBalance += tapIncrement;
    document.getElementById("coinBalance").innerText = `Coins: ${coinBalance}`;

    // Animate tap effect
    const circle = this;
    circle.classList.add("tap-animation");
    setTimeout(() => {
        circle.classList.remove("tap-animation");
    }, 200); // Duration of the animation

    // Level up logic
    if (coinBalance % 10 === 0) { // Change level every 10 coins for example
        tapIncrement += 1;
    }
});


