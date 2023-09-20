function askQuestion() {
    const question = document.getElementById("userQuestion").value;
    // Make an API call to your Python program here
}
function getPosts() {
    FB.api('/me/posts', function (response) {
        // Do something with the posts
    });
}
function checkLoginState() {
    FB.getLoginStatus(function (response) {
        // handle the response
    });
}

