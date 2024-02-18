<script setup lang="ts">

import { ref } from 'vue'

const username = ref('')
const password = ref('')

const handleLogin = () => {
    console.log("Logging in with:", username.value, password.value);
}
</script>


<template>
<b-row class="vh-100 vw-100 row-login">
  <b-col sm="5" class="d-flex justify-content-center align-items-center left-login">
          <h1 class="title-login">Login</h1>
          <form @submit.prevent="handleLogin">
              <label for="username">Username:</label>
              <input v-model="username" type="text" id="username" required />

              <label for="password">Password: </label>
              <input v-model="password" type="password" id="password" required>

              <button type="submit">Submit</button>

          </form>
  </b-col>
  <b-col sm="7">
      <img src="../assets/login.svg" class="img-login" />
  </b-col>
  </b-row>
</template>

<style>
.row-login {
    margin-left: 0;
}
.left-login {
    background-color: red;
}

.img-login {
  width: 600px;
  height: 600px;
  position: absolute;
  left: 0px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

p {
   line-height: 1rem;
}

.card {
   padding: 20px;
}

.form-group {
   input {
      margin-bottom: 20px;
   }
}



h1 {
      margin-bottom: 1.5rem;
}

.error {
   animation-name: errorShake;
   animation-duration: 0.3s;
}


label {
    display: block;
    margin-bottom: 5px;
}

@keyframes errorShake {
   0% {
      transform: translateX(-25px);
   }
   25% {
      transform: translateX(25px);
   }
   50% {
      transform: translateX(-25px);
   }
   75% {
      transform: translateX(25px);
   }
   100% {
      transform: translateX(0);
   }
}


* {
        box-sizing: border-box;
}


#login-form {
    width: 100%;
    max-width: 300px;
    background-color: #fff;
    padding: 20px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #45a049;
}

@media only screen and (min-width: 600px) {
    #login-form {
      max-width: 400px;
  }
}

</style>
