<template>
    <div>
        <h2>Student Records</h2>
        <h3  style="cursor: pointer; display: flex; width:110%;"><span @click="allData" style="flex:1; float: inline-start;">1. Scrapped records</span><span @click="myData" style="flex:1; float: inline-end ;">2. Show my record</span><button class="delete" style="display: flex; align-items: end;" @click="logout">Logout</button></h3>
        
        
        <table style="display: none;" id="allData">
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
            <tbody >
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
        <table style="display: none;" id="myData">
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
                            <button class="edit" @click="toggleEdit(index), student.editing ? NULL : updateData(index)">{{ student.editing ? 'Save' : 'Edit' }}</button>
                            <button class="delete" @click="deleteData(index), deleteRow(index)">Delete</button>
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
    mounted() {
        if (!localStorage.getItem('token')) {
            this.$router.push('/');
        }
    },
    methods: {
        async logout(){
            localStorage.removeItem('token');
            this.$router.push('/')
        },
        toggleEdit(index) {
            this.students[index].editing = !this.students[index].editing;
        },
        deleteRow(index) {
            alert("Are you sure want to delete your records?");
            this.students.splice(index, 1);
            this.$router.push('/')
            // console.log(this.students[index]);
        },
        async allData() {
            document.getElementById("myData").style.display = "none";
            document.getElementById("allData").style.display = "block";
            this.students=[]
            try {
                const response = await fetch('http://localhost:5000/allData', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
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
        },
        async myData() {
            document.getElementById("myData").style.display = "block";
            document.getElementById("allData").style.display = "none";
            // document.querySelector(tbody).innerHTML = NULL;
            this.students=[]
            try {
                const response = await fetch('http://localhost:5000/myData', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        "Authorization": localStorage.getItem("token")
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
        async updateData(index) {
            try {
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
            catch (error) {
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
.edit{
    cursor: pointer;
    background-color: #0091ff;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
}
.delete{
    cursor: pointer;
    background-color: #ff0000;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
}
</style>
