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
                    localStorage.setItem("token",data.token); 
                    console.log(data);

                    if(data.role=="student" && localStorage.getItem("token"))
                        this.$router.push('/home')
                    else    
                        this.$router.push('/admin')
                } else {
                    alert(data.error); 
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
    border: 5px solid #4c4343;
    border-radius: 5px;
    background-color: rgb(229, 224, 219);
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
