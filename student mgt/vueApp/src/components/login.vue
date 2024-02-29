<template>
    <div class="login">
        <h2>Login</h2>
        <form @submit.prevent="login" >
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" required>
            </div>
            <div class="form-group">
                <label for="studentId">Student ID</label>
                <input type="text" id="studentId" v-model="studentId" required>
            </div>
            <button type="submit">Login</button>
            <p><a href="signup">Signup</a></p>
        </form>
    </div>
</template>

<script>
// import router from './routes'

export default {
    data() {
        return {
            username: '',
            studentId: ''
        };
    },
    methods: {
        async login() {
            try {
                const response = await fetch('http://localhost:5000/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: this.username,
                        studentId: this.studentId
                    })
                });
                const data = await response.json();
                if (response.ok) {
                    // alert(data.msg); // Assuming the server returns a message upon successful login
                    this.$router.push('/home')
                    // window.location.href='/home'
                    // Redirect the user to another page or perform other actions
                } else {
                    alert(data.error); // Display error message if login fails
                }
            } catch (error) {
                console.error('Login failed:', error);
                alert('An error occurred while logging in.');
            }
        }
    }
};
</script>

<style scoped>
.login {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 80%;
    padding: 10px;
    font-size: 16px;
}

button {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>
