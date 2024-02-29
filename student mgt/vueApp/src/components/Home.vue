<template>
    <div>
        <h2>Student Records</h2>
        <h3 @click="allData">Show all records</h3>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Student ID</th>
                    <th>Email</th>
                    <th>Contact Number</th>
                    <th>Course Name</th>
                    <th>Grades</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="student in students" :key="student.studentId">
                    <td>{{ student.name}}</td>
                    <td>{{ student.studentId }}</td>
                    <td>{{ student.email }}</td>
                    <td>{{ student.contactNumber }}</td>
                    <td>{{ student.courseName }}</td>
                    <td>{{ student.grades }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            students: []
        };
    },
    methods: {
        async allData() {
            try {
                const response = await fetch('http://localhost:5000/allData', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                    // body: JSON.stringify({
                    //     username: this.username,
                    //     studentId: this.studentId
                    // })
                });
                let data = await response.json();
                if (response.ok) {
                    // alert(data.msg); // Assuming the server returns a message upon successful login
                    // this.$router.push('/home')
                    console.log(data['students'].length);
                    for(let i=0;i< data['students'].length;i++){
                        let row = data['students'][i];
                        let obj = {
                            name: row[1],
                            studentId: row[0],
                            email: row[7],
                            contactNumber: row[6],
                            courseName: row[2],
                            grades: row[3]
                        }
                        this.students.push(obj)
                    }
                    // this.students = data;
                    // window.location.href='/home'
                    // Redirect the user to another page or perform other actions
                } else {
                    alert(data.error); // Display error message if login fails
                }
            } catch (error) {
                console.error('Data loading failed:', error);
                alert('An error occurred while fetching data.');
            }
        }
    }
};
</script>

<style scoped>
table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
}
</style>
