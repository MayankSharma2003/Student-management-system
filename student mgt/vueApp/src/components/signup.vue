<template>
    <div class="signup">
        <h2>Sign Up</h2>
        <form @submit.prevent="signup">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" v-model="email" required>
            </div>
            <div class="form-group">
                <label for="studentId">Student ID</label>
                <input type="text" id="studentId" v-model="studentId" required>
            </div>
            <div class="form-group">
            <label for="coursename">Course Name</label>
            <input type="text" id="coursename" v-model="coursename" required>
        </div>

        <div class="form-group">
            <label for="contactnumber">Contact Number</label>
            <input type="text" id="contactnumber" v-model="contactNumber" required>
        </div>

        <div class="form-group">
            <label for="grades">Grades</label>
            <input type="text" id="grades" v-model="grades" required>
        </div>

        <div class="form-group">
            <label for="dob">Date of Birth (DOB)</label>
            <input type="date" id="dob" v-model="dob" required>
        </div>

        <div class="form-group">
            <label for="address">Address</label>
            <textarea id="address" v-model="address" required></textarea>
        </div>

                <button type="submit">Sign Up</button>
                <p><a href="/">Login</a></p>
            </form>
        </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            email: '',
            studentId:'',
            coursename:'',
            dob:'',
            address:'',
            contactNumber:'',
            grades:''
        };
    },
    methods: {
        async signup() {
            try {
                const response = await fetch('http://localhost:5000/signup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: this.username,
                        studentId: this.studentId,
                        address:this.address,
                        dob: this.dob,
                        email:this.email,
                        contactNumber:this.contactNumber,
                        grades : this.grades,
                        coursename : this.coursename
                    })
                });
                const data = await response.json();
                if (response.ok) {
                    alert(data.msg);  
                    this.$router.push('/')
                    // window.location.href='/home'
                } else {
                    alert(data.error); // Display error message if login fails
                }
            } catch (error) {
                console.error('Signup failed:', error);
                alert('An error occurred while signing in.');
            }
        }
    }
};
</script>

<style scoped>
.signup {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 5px solid #4c4343;
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
