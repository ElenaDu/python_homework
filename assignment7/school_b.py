import sqlite3 

# Connect to the database
with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Bob', 22, 'History')") 
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Charlie', 19, 'Biology')") 
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')") 
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')") 

    #conn.commit() 
   
    #print("Sample data inserted successfully.")
    cursor.execute("SELECT * FROM Students WHERE name = 'Alice'")
    result = cursor.fetchall()
    for row in result:
        print(row)
    
    
    def enroll_student(cursor, student, course):
        cursor.execute("SELECT * FROM Students WHERE name = ?", (student,))
        results = cursor.fetchall()
        if len(results) > 0:
            student_id = results[0][0]
        else:
            print(f"There was no student named {student}.")
            return
        cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
        results = cursor.fetchall()
        if len(results) > 0:
            course_id = results[0][0]
        else:
            print(f"There was no course named {course}.")
            return
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

    enroll_student(cursor, "Alice", "Math 101")
    enroll_student(cursor, "Alice", "Chemistry 101")
    enroll_student(cursor, "Bob", "Math 101")
    enroll_student(cursor, "Bob", "English 101")
    enroll_student(cursor, "Charlie", "English 101")
    conn.commit()