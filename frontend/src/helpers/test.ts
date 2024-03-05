const axios = require('axios');

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
    const email = emailInput.value;
    const password
})

axios.get('/singin', {
    params: {
        ID: 12345
    }
})
    .then(function (response) => console.log(response))
    .catch(function (error) => console.log(error))
    .finally(function () {
        // always executed
    });
