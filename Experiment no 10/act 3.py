import streamlit as st

def main():
    st.set_page_config(page_title="Student Result Calculator", page_icon="🎓")
    
    st.title("🎓 Student Result Calculator")
    st.write("Enter the marks obtained in each subject to generate the final result.")

    # Input Section: Student Details
    col1, col2 = st.columns(2)
    with col1:
        student_name = st.text_input("Student Name", placeholder="e.g. Abhishek Jagdale")
    with col2:
        roll_no = st.text_input("Roll Number", placeholder="e.g. 1108")

    st.divider()

    # Input Section: Subject Marks
    st.subheader("Enter Subject Marks (Out of 100)")
    
    subjects = ["Mathematics", "Physics", "Chemistry", "Programming in Python", "English"]
    marks = []

    cols = st.columns(len(subjects))
    for i, subject in enumerate(subjects):
        with cols[i]:
            score = st.number_input(f"{subject}", min_value=0, max_value=100, value=0, step=1)
            marks.append(score)

    if st.button("Generate Result"):
        if student_name and roll_no:
            total_marks = sum(marks)
            percentage = total_marks / len(subjects)
            
            # Determine Pass/Fail (Assuming 35 is the passing mark for each subject)
            passed = all(m >= 35 for m in marks)
            
            # Determine Grade
            if not passed:
                grade = "F (Fail)"
                color = "red"
            elif percentage >= 90:
                grade = "A+"
                color = "green"
            elif percentage >= 75:
                grade = "A"
                color = "green"
            elif percentage >= 60:
                grade = "B"
                color = "blue"
            elif percentage >= 50:
                grade = "C"
                color = "orange"
            else:
                grade = "D"
                color = "orange"

            # Display Result Card
            st.success(f"### Result for {student_name} (Roll No: {roll_no})")
            
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("Total Marks", f"{total_marks} / {len(subjects)*100}")
            res_col2.metric("Percentage", f"{percentage:.2f}%")
            res_col3.metric("Final Grade", grade)

            if passed:
                st.balloons()
                st.info("Congratulations! You have passed the examination.")
            else:
                st.error("Result: Fail. Better luck next time!")
        else:
            st.warning("Please enter both Student Name and Roll Number.")

if _name_ == "_main_":
    main()
