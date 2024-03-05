const axios = require('axios');

export const isoReq = {
    get: axios.get(),
    post: axios.post(),
    put: axios.put(),
    delete: axios.delete(),
}
