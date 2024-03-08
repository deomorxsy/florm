<template>
    <div class="two-column-layout">
    <div class="left-column">
      <!-- Content for the left column goes here -->

      <img src="../assets/upe.png" class="img-login">
    </div>
    <div id="outerDiv" class="right-column">
      <!-- Content for the right column goes here -->
    <form id="innerForm" @submit.prevent="handleSubmit">
        <label>Username: </label>
        <input type="username" required v-model="formData.user">

        <label>Email: </label>
        <input type="email" required v-model="email">

        <label>Password: </label>
        <input type="password" required v-model="password">
        <input type="checkbox" v-model="showPassword" @change="toggleVisibility">
        <label>Show Password</label>

        <hr width="10%" >

        <label>Role:</label>
        <select required v-model="role">
            <option>Professor</option>
            <option>Alumni</option>
            <option>Escolaridade</option>
        </select>

        <div class="terms">
            <input type="checkbox" required>
            <label>Accept <a href="127.0.0.1:5173/policy">terms and conditions</a></label>
        </div>

        <div class="submit">
            <button>
                Create Account
            </button>
        </div>


    </form>
    </div>
          </div>

    <p>Email: {{ email }}</p>
    <p>Password: {{ password }}</p>
    <p>Role: {{ role }}</p>
</template>

<script setup lang="ts">
//import { Form, Field, ErrorMessage } from "vee-validate";
//import * as yup from "yup";

import { ref } from 'vue';
import axios from 'axios';
import querystring from 'querystring';

const email = ref('');
const password = ref('');
const showPassword = false;
const role = ref('');

const toggleVisibility = () => {
    this.showPassword = !this.showPassword;
};

const formData = ref({
    user: '',
    email: '',
    password: '',
    role: '',
});


// state management: reactive ref/reactive,
// pinia, vuex. Also redux vs useState in react


const post = ref({
    title: '',
    body: '',
})

const handleInput = (event: Event) => {
    // validate input
    const target = event.target as HTMLInputElement;
    formData.value = { ...formData.value, [target.name]: target.value }; //post.value
}

const handleSubmit = async () => {
    // handle post request from submit
    console.log("form submitted!");
    try {
        const response = await axios.post('https://jsonplaceholder.typicode.com/posts', formData.value);
        console.log(response);
    } catch(err) {
    console.log(err);
    };
};

</script>

<style>

#app {
    font-family: avenir, helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialised;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: auto;
    margin-bottom: auto;
}

body {
    margin: 0;
    background: #eee;
    overflow: hidden;
}

form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
}

label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.7em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
}

input, select {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
}

input[type="checkbox"] {
    display: inline-block;
    width: 16px;
    margin: 0 10px 0 0;
    position: relative;
    top: 2px;
}

hr {
    margin-bottom: 20px;
    margin-top: 20px;
}

button {
    /*background: #0b6dff;*/
    /*background: #f2f2f2;*/
    background: #2f2e41;
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: white;
    border-radius: 20px;
}

submit {
    text-align: center;
}

.two-column-layout {
  display: flex;
  /*height: 100vh; /* 100% of the viewport height */
}

.left-column {
  /* Add additional styling for the left column */
  flex: 1; /* Takes up 1/2 of the available space */
  background-color: #465C83;
  /*height: 130vh*/
}

.right-column {
  /* Add additional styling for the right column */
  flex: 1; /* Takes up 1/2 of the available space */
  /*background-color: #f2f2f2*/
  background-color: #DDE0E8;
}

.img-login {
    text-align: left;
    margin-top: 15em;
}

#outerDiv {
    width: 100vw;
    height: 130vh;
}
#innerForm {
    width: 500px;
    margin: auto;
    margin-top: 15px;
    height: 550px;
    /*overflow-y: scroll;*/
}

</style>

