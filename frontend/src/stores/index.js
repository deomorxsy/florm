// initializes pinia, does not import stores
//

//import { createStore } from "vuex";
import { defineStore } from 'pinia'
import { auth } from "./auth.module";

export const useStoreAuth = defineStore('storeAuth', {
    modules: {
        auth,
    },
});

//export default store
