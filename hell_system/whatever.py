'`Write a program that simulates a university course management system. The program should have classes for courses, students, and professors. Courses should have attributes such as name, instructor, and content. Students should have attributes such as name and contact information. Professors should have attributes such as name and contact information. The program should allow professors to create and manage courses, and students to enroll in courses, complete assignments, and view their progress. Use interfaces to implement classes for different types of courses (e.g., undergraduate, graduate) and abstract classes for course assignments.`'


courseDB = {}
from abc import ABC, abstractmethod

class Persona(ABC):
    __counter = 0 #class attr for global usage
    def __init__(self, name, contact):
        Persona.__counter += 1
        self.__id = Persona.__counter
        self.name = name
        self.contact = contact

    @property
    def id(self):
        return self.__id 

    def info(self):
        return {"id": self.id, "name": self.name, "contact": self.contact}

    @abstractmethod
    def get_role(self):
        ... #design in child classes


# test2 = Persona() #ERROR  
class Student(Persona):
    def __init__(self, name, contact):
        super(Student, self).__init__(name, contact)
        self.courses = {} #{"coursename": course object}
    
    def get_role(self):
        return "Student"

    #todo
    def enroll(self, course):
        if course not in courseDB:
            raise ValueError(f"Course '{course}' does not exist.")
        obj = courseDB[course]
        if obj.check_id(self):
            self.courses[course] = obj
            return True
        return False

    def submit(self, assignment, submission):
        """Submit assignment for a course"""
        from datetime import datetime
        for course_name, course_obj in self.courses.items():
            if assignment in course_obj.assignments:
                course_obj.assignment_submissions[assignment][self.id] = {
                    "submission": submission,
                    "timestamp": datetime.now(),
                    "status": "submitted"
                }
                return True
        raise ValueError(f"Assignment '{assignment}' not found in enrolled courses.")

    def progress(self, course_arg = None):
        """Calculate and return progress for courses"""
        if course_arg:
            if course_arg not in self.courses:
                return f"Course '{course_arg}' not enrolled."
            course_obj = self.courses[course_arg]
            total_assignments = len(course_obj.assignments)
            submitted = sum(1 for assign in course_obj.assignments if self.id in course_obj.assignment_submissions.get(assign, {}))
            progress_pct = (submitted / total_assignments * 100) if total_assignments > 0 else 0
            return f"{course_arg} is completed by {progress_pct:.1f}%"
        
        result = []
        for course_name, course_obj in self.courses.items():
            total_assignments = len(course_obj.assignments)
            submitted = sum(1 for assign in course_obj.assignments if self.id in course_obj.assignment_submissions.get(assign, {}))
            progress_pct = (submitted / total_assignments * 100) if total_assignments > 0 else 0
            result.append(f"'{course_name}' is completed by {progress_pct:.1f}%")
        return "\n".join(result)


# test3 = Student("Qwen", "qwen@mail.com")
# test3.get_role()


class Professor(Persona):
    def __init__(self, name, contact):
        super(Professor, self).__init__(name, contact)
        self.has_courses = []
    
    #done
    def get_role(self):
        return "Professor"

    #done
    def info(self):
        return {"name": self.name, "contact": self.contact, "has_courses": self.has_courses}

    #done
    def create_course(self, course_type, course_name, topics: list, assignments: list, course_file_path):
        do = f"{course_type}(course_name, topics, self, assignments, course_file_path)"
        # print(do)
        temp = eval(do)
        if temp:
            # print(temp)
            # print("hi")
            self.has_courses.append(temp)
            courseDB[course_name] = temp
            return temp
        print(temp)
        raise(ValueError("hi"))

    def manage_course(self, course, **actions): #generated method beacause i dont have haves
        """Manage course modifications: rename, delete, modify_topics, modify_whitelist"""
        course_obj = None
        for c in self.has_courses:
            if c.name == course:
                course_obj = c
                break
        
        if not course_obj:
            raise ValueError(f"Course '{course}' not found in professor's courses.")
        
        if "rename" in actions:
            old_name = course_obj.name
            course_obj.name = actions["rename"]
            courseDB[actions["rename"]] = courseDB.pop(old_name)
            return f"Course renamed from '{old_name}' to '{actions['rename']}'"
        
        if "delete" in actions and actions["delete"]:
            self.has_courses.remove(course_obj)
            del courseDB[course]
            return f"Course '{course}' deleted."
        
        if "modify_topics" in actions:
            course_obj.topics = actions["modify_topics"]
            return f"Topics updated for '{course}'."
        
        if "modify_whitelist" in actions:
            # Whitelist functionality - restrict enrollment
            course_obj.whitelist = actions["modify_whitelist"]
            return f"Whitelist updated for '{course}'."
        

    def add_assignment(self, course, assignment):
        """Add new assignment to existing course"""
        course_obj = None
        for c in self.has_courses:
            if c.name == course:
                course_obj = c
                break
        
        if not course_obj:
            raise ValueError(f"Course '{course}' not found in professor's courses.")
        
        if assignment not in course_obj.assignments:
            course_obj.assignments.append(assignment)
            course_obj.assignment_submissions[assignment] = {}
            return f"Assignment '{assignment}' added to '{course}'."
        return f"Assignment '{assignment}' already exists in '{course}'."
    

class Course(ABC):
    def __init__(self, name, topics: list, professor, assignments: list, course_file_path):
        self.name = name
        self.topics = topics
        self.professor = professor
        self.assignments = assignments
        self.path = course_file_path
        self.enrolled_students = []  # Track enrolled students
        self.assignment_submissions = {assign: {} for assign in assignments}  # {assignment: {student_id: submission}}
        self.whitelist = []  # List of allowed student IDs
        
    def info(self):
        return {"name": self.name, "topics": self.topics, "professor": self.professor, "assignments": self.assignments, "path": self.path}    
    

    def __del__(self):
        print(f"deleting {self}")
        del self

    def check_id(self, student):
        """Check if student is in whitelist if set, and add to enrolled_students if not already enrolled"""
        if self.whitelist and student.id not in self.whitelist:
            return False
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            return True
        return False

    @abstractmethod
    def calculate_grade(self, student):
        """Calculate grade for a student based on submissions"""
        pass


class Undergraduate_course(Course):
    def calculate_grade(self, student):
        """Calculate grade for undergraduate student (avg of submissions)"""
        total_score = 0
        submitted_count = 0
        for assignment, submissions in self.assignment_submissions.items():
            if student.id in submissions:
                submitted_count += 1
                total_score += 1  # Each submission worth 1 point
        return (total_score / len(self.assignments) * 100) if self.assignments else 0

class Graduate_course(Course):
    def calculate_grade(self, student):
        """Calculate grade for graduate student (stricter grading)"""
        total_score = 0
        submitted_count = 0
        for assignment, submissions in self.assignment_submissions.items():
            if student.id in submissions:
                submitted_count += 1
                total_score += 1.5  # Stricter grading - worth more per submission
        return min((total_score / len(self.assignments) * 100), 100) if self.assignments else 0
    
    
prof1 = Professor("Armen", "armen@mail.com")
# prof1.get_role()
# prof1.info()
prof1.create_course("Undergraduate_course", "global warming", ["1. the sun", "the earth", "the ocean"], ["wash dishes with less water", "go for a walk", "touch grass"], "./courses/global-warming")
# # (prof1.info()["has_courses"][0]).info()
# print(prof1.has_courses)
# stud1 = Student("Aren", "aren@example.com")
# stud1.enroll("global warming")
# print(courseDB)
# # x = Undergraduate_course("abc", ["abc"], prof1, ["wash hands"], "./courses/something")
# # print(x)


# Testing scenario
prof1 = Professor("Armen", "armen@mail.com")
course = prof1.create_course("Undergraduate_course", "global warming", ["1. the sun", "the earth", "the ocean"], ["wash dishes with less water", "go for a walk", "touch grass"], "./courses/global-warming")

stud1 = Student("Aren", "aren@example.com")
stud2 = Student("Bob", "bob@example.com")

# Enroll students
stud1.enroll("global warming")
stud2.enroll("global warming")

# Submit assignments
stud1.submit("wash dishes with less water", "I washed dishes with less water.")
stud1.submit("go for a walk", "I went for a walk.")

# Check progress
print(stud1.progress())
print(stud1.progress("global warming"))

# Professor manages course
prof1.manage_course("global warming", modify_whitelist=[stud1.id])

# Try enroll after whitelist
stud3 = Student("Charlie", "charlie@example.com")
stud3.enroll("global warming")  # Should fail

# Add assignment
prof1.add_assignment("global warming", "new assignment")

# Calculate grade
print(f"Grade for {stud1.name}: {course.calculate_grade(stud1)}%")
# test1 = Student("ind", "121212")
# test1.info()
# test1.get_role()
