// Function to handle Facebook login
function loginWithFacebook() {
    FB.login(function (response) {
        if (response.authResponse) {
            // User is logged in and has authenticated your app
            console.log('User is logged in, token:', response.authResponse.accessToken);
            // Call a function to do something after login (e.g., fetch user data)
            afterLogin();
        } else {
            // User canceled the login or did not fully authorize your app
            console.log('User canceled login or did not fully authorize your app.');
        }
    }, { scope: 'public_profile,email' }); // Define the requested permissions here
}

// Function to perform actions after a successful login
function afterLogin() {
    // Example: Get user's basic information
    FB.api('/me', 'GET', { fields: 'id,first_name,last_name,email' }, function (response) {
        console.log('User information:', response);
        // You can perform actions with the user's information here
    });
}
