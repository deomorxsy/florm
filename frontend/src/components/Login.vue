<script setup lang="ts">

import { ref } from 'vue';
import * as yup from "yup"; // typed validation
import { toTypedSchema } from "@vee-validate/yup";
import { useForm } from "vee-validate";

const schema  = toTypedSchema(
    yup.object({
        email: yup.string().required().email(),
        password: yup.string().min(6).required(),
    })
);

const { errors, defineField, handleSubmit } = useForm({
    validationSchema: schema
});

const email = defineField("email");
const password = defineField("password");

const handleLoginSubmit = handleSubmit(async ( email: string, password: string ) => {
})


</script>


<template>
  <div class="two-column-layout">
    <div class="left-column">
      <!-- Content for the left column goes here -->
      <img src="../assets/login.svg" class="img-login">
    </div>
    <div class="right-column">
      <!-- Content for the right column goes here -->

        <form id="login-form">
        <label for="username">LOGIN</label>
        <input type="text" id="username" name="username" required>

        <div class="input-box">
            <input type="password" placeholder="password" required>
            <svg id="eyeicon"
              xmlns="http://www.w3.org/2000/svg"
              height="24"
              viewBox="0 0 24 24"
              width="24"
            >
              <path d="M12 21c-7.605 0-10.804-8.296-10.937-8.648L.932 12l.131-.352C1.196 11.295 4.394 3 12 3s10.804 8.296 10.937 8.648l.131.352-.131.352C22.804 12.705 19.606 21 12 21zm-8.915-9c.658 1.467 3.5 7 8.915 7s8.257-5.533 8.915-7c-.658-1.467-3.5-7-8.915-7s-8.257 5.533-8.915 7zM12 16c-2.206 0-4-1.794-4-4s1.794-4 4-4 4 1.794 4 4-1.794 4-4 4zm0-6c-1.103 0-2 .897-2 2s.897 2 2 2 2-.897 2-2-.897-2-2-2z" />
            </svg>
        </div>

        <button type="submit">ENTRAR</button>
        <p class="forgot-class">
        <a href="https://saadis.net/forgot.php?username=1">Forgot Username?</a>
        |
        <a href="https://saadis.net/forgot.php?password=1">Forgot Password?</a>
        </p>


    </form>
    </div>
  </div>
</template>


<style>
body {
    margin:0;
    /*border: 7px solid #2f2e41;
    box-sizing: border-box;*/
}

.input-box {
    background: #fff;
    /*width: 90%;
    max-width: 500px;
    border-radius: 5px;
    padding: 10px 20px;
    margin: 300px auto;
    display: flex;
    align-items: center;*/
}

.input-box input {
    width: 100%;
    padding: 10px 0;
    border: 0;
    outline: 0;
    /*font-size: 24px;*/
    color: #555;
}

.input-box svg {
    background: #fff;
    width: 35px;
    cursor: pointer;
}

*,
*::after,
*::before {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
}
.two-column-layout {
  display: flex;
  height: 100vh; /* 100% of the viewport height */
}

.left-column {
  flex: 1; /* Takes up 1/2 of the available space */

  background-color: #ffffff;
  /* Add additional styling for the left column */
}

.right-column {
  flex: 1; /* Takes up 1/2 of the available space */

  background-color: #f2f2f2
  /*background-color: #2f2e41;*/
  /* Add additional styling for the right column */
}



#login-form {
width: 100%;
max-width: 300px;
background-color: #fff;
padding: 20px;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
margin: auto;
margin-top: 100px;
}


p {
    text-align: center;
}

label {
display: block;
margin-bottom: 5px;
font-weight: bold;
}

input[type="text"],
input[type="password"] {
width: 100%;
padding: 8px;
border: 1px solid #ccc;
border-radius: 4px;
margin-bottom: 10px;
}

button[type="submit"] {
width: 100%;
padding: 8px;
background-color: #6c63ff;
color: #fff;
border: none;
border-radius: 4px;
cursor: pointer;
}

button[type="submit"]:hover {
background-color: #ff6884
/*light-green: #45a049;*/
}

@media only screen and (min-width: 600px) {
#login-form {
    max-width: 400px;
}
}
</style>
