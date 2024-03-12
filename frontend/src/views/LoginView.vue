<script setup>
import axios from 'axios';
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

import { useStoreAuth } from '@/stores';

const schema = Yup.object().shape({
    username: Yup.string().required('Username is required'),
    password: Yup.string().required('Password is required')
});

async function onSubmit(values) {
    const loginAuthStore = useStoreAuth();
    const { username, password } = values;
    await loginAuthStore.login(username, password);
}
</script>

<template>
    <div class="two-column-layout">
    <div class="left-column">
    <div class="card m-3">
        <h4 class="card-header">Login</h4>
        <div class="card-body">
            <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                <div class="form-group">
                    <label>Username</label>
                    <Field name="username" type="text" class="form-control" :class="{ 'is-invalid': errors.username }" />
                    <div class="invalid-feedback">{{ errors.username }}</div>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <Field name="password" type="password" class="form-control" :class="{ 'is-invalid': errors.password }" />
                    <div class="invalid-feedback">{{ errors.password }}</div>
                </div>
                <div class="form-group">
                    <button class="btn btn-primary" :disabled="isSubmitting">
                        <span v-show="isSubmitting" class="spinner-border spinner-border-sm mr-1"></span>
                        Login
                    </button>
                    <router-link to="register" class="btn btn-link">Register</router-link>
                </div>
            </Form>
        </div>
    </div>
    </div>
    </div>
</template>

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
