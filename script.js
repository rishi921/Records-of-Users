// script.js
document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get form values
    var firstName = document.getElementById("firstName").value;
    var lastName = document.getElementById("lastName").value;
    var mobileNumber = document.getElementById("mobileNumber").value;
    // var state = document.getElementById("state").value;
    // var City = document.getElementById("City").value;
    var pinCode = document.getElementById("pinCode").value;
  
    // Create user object
    var user = {
      firstName: firstName,
      lastName: lastName,
      mobileNumber: mobileNumber,
    //   State: State,
    //   City: City,
      pinCode: pinCode
    };
  
    // Retrieve existing user records from local storage or initialize an empty array
    var users = JSON.parse(localStorage.getItem("users")) || [];
  
    // Add the new user to the array
    users.push(user);
  
    // Store the updated user records in local storage
    localStorage.setItem("users", JSON.stringify(users));
  
    // Redirect to the index.html page
    window.location.href = "index.html";
  });
  