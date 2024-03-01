<template>
    <div>
        <h2>Welcome Admin⚜</h2>
        <h3 @click="allData" style="cursor: pointer;"><button class="delete" style="display: flex; align-items: end;" @click="logout">Logout</button></h3>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Student ID</th>
                    <th>Email</th>
                    <th>Contact Number</th>
                    <th>Course Name</th>
                    <th>Grades</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(student, index) in students" :key="index">
                    <td>
                        <input type="text" v-model="student.name" :disabled="!student.editing">
                    </td>
                    <td>
                        <input type="text" v-model="student.studentId" :disabled="!student.editing">
                    </td>
                    <td>
                        <input type="text" v-model="student.email" :disabled="!student.editing">
                    </td>
                    <td>
                        <input type="text" v-model="student.contactNumber" :disabled="!student.editing">
                    </td>
                    <td>
                        <input type="text" v-model="student.courseName" :disabled="!student.editing">
                    </td>
                    <td>
                        <input type="text" v-model="student.grades" :disabled="!student.editing">
                    </td>
                    <td>
                        <button @click="toggleEdit(index),student.editing?NULL:updateData(index)" class="edit">{{ student.editing ? 'Save' : 'Edit' }}</button>
                        <button @click="deleteData(index), deleteRow(index)" class="delete">Delete</button>
                    </td>
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
    mounted(){
        if(!localStorage.getItem('token')){
            this.$router.push('/');
        }
        this.allData();
    },
    methods: {
        logout(){
            localStorage.removeItem('token');
            this.$router.push("/")
        },
        toggleEdit(index) {
            this.students[index].editing = !this.students[index].editing;
        },
        deleteRow(index) {
            this.students.splice(index, 1);
            // console.log(this.students[index]);
        },
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
                    for (let i = 0; i < data['students'].length; i++) {
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
        },
        async updateData(index){
            try{
                console.log(this.students[index]);
                const response = await fetch('http://localhost:5000/updateData', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: this.students[index].name,
                        studentId: this.students[index].studentId,
                        // address: this.students[index].address,
                        // dob: this.students[index].dob,
                        email: this.students[index].email,
                        contactNumber: this.students[index].contactNumber,
                        grades: this.students[index].grades,
                        coursename: this.students[index].courseName
                    })
                });
                let data = await response.json();
                if (response.ok) {
                    alert("Updated succesfully")
                } else {
                    alert(data.error); // Display error message if login fails
                }
            }
            catch(error){
                console.log(error);
            }
        },
        async deleteData(index) {
            try {
                console.log(index);
                console.log(this.students[index]);
                const response = await fetch('http://localhost:5000/deleteData', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        studentId: this.students[index].studentId
                    })
                });
                let data = await response.json();
                if (response.ok) {
                    alert("Deleted succesfully")
                    
                } else {
                    alert(data.error); // Display error message if login fails
                }
            }
            catch (error) {
                console.log(error);
            }
        }
    }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  font-family: Arial, sans-serif;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

/* Button styles */
.button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

input[type="text"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box;
  transition: border-color 0.3s ease;
}

input[type="text"]:focus {
  outline: none;
  border-color: #007bff;
}

.edit
    {
    cursor: pointer;
    background-color: #007bff;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
}

.delete {
    cursor: pointer;
    background-color: #ff0000;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
}

</style>
