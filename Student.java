public class Student {
     // Private Attributes
     private String name;
     private String studentId;
     private double grade;
     // Constructor
     public Student(String name, String studentId, double grade) {
         this.name = name;
         this.studentId = studentId;
         this.grade = grade;
     }
     // Getters
     public String getName() {
         return name;
     }
     public String getStudentId() {
         return studentId;
     }
     public double getGrade() {
         return grade;
     }
     // Setter ONLY for grade
     public void setGrade(double newGrade) {
         this.grade = newGrade;
     }
     // displayInfo() Method
     public void displayInfo() {
         System.out.println("Name: " + name + " | ID: " + studentId + " | Grade: " + grade);
     }
     // Main Method
     public static void main(String[] args) {
         // Create two Student objects
         Student student1 = new Student("Braezzil Rein Renion", "2026-001", 92.0);
         Student student2 = new Student("Rein Madrid", "2026-002", 88.5);
         // Change one student’s grade using setter
         student1.setGrade(95.0);
         // Call displayInfo() for both
         student1.displayInfo();
         student2.displayInfo();
     }
 }
