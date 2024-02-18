export default function authHeader() {
    const user: string = JSON.parse(localStorage.getItem('user'))

    if (user && user.accessToken) { // syntax may change for express+node backend or flask backend
        return { Authorization: 'Bearer' + user.accessToken };
    } else {
        return {};
    }
}
