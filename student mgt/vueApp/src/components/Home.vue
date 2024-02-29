<template>
    <div>
        <h2>Student Records</h2>
        <ul>
            <li v-for="student in students" :key="student.studentId">
                <div>Name: {{ student.name }}</div>
                <div>Student ID: {{ student.studentId }}</div>
                <div>Email: {{ student.email }}</div>
                <div>Contact Number: {{ student.contactNumber }}</div>
                <div>Course Name: {{ student.courseName }}</div>
                <hr>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            students: [
                {
                    name: 'John Doe',
                    studentId: '123456',
                    email: 'john@example.com',
                    contactNumber: '123-456-7890',
                    courseName: 'Computer Science'
                },
                {
                    name: 'Alice Smith',
                    studentId: '654321',
                    email: 'alice@example.com',
                    contactNumber: '987-654-3210',
                    courseName: 'Mathematics'
                },
                // Add more dummy student data as needed
            ]
        };
    }
};
</script>

<style scoped>
/* Add styling as needed */
</style>
