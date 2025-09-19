sa#personal info 
full_name = "Vanessa Gray"
student_email = "vcgray@aggies.ncat.edu"
hometown = "Bowie, MD"
grad_semester = "Spring 2029"
major = "Computer Science"

#academic data
current_courses = ["COMP 163", "MATH 132", "ENG 101", "HIS 106"]
completed_courses = ["Calculus I", " AP World History", "Psychology", "Sociology"]
credit_hours = [3, 3, 3, 3]
GPA_history = [4.0]

#contact info 
emergency_contact = ("Mom", "Cynthia Gray", "336-444-2299")
home_address = ("305 Jersey Ct", "Bowie, MD", "20721")
insta_info = ("Instagram", "@_nxssabear", 312)
twitter_info = ("Twitter", "@nxssabear", 127 )
birthday = ("Birthday", "1", "11", "2007")

#interest tracking
current_skills = {"Python basics", "HTML", "Problem solving", "Java", "JavaScript", "CSS"}
skills_learn = {"Data structures", "Git", "Web design", "Public speaking"}
career_interest = {"Software development", "Web development", "Cybersecurity", "Game development"}
hobbies = {"Gaming", "Shopping", "Anime", "Volleyball", "Music"}
entertainment_backlog = {"One Piece", "Sailor Moon", "Suits", "Code Geass", "The Summer I Turned Pretty"}

#organizational mapping
course_credits = {
    "COMP 163:": 3,
    "MATH 150:": 3,
    "ENG 101:": 3,
    "HIS 105:": 3
}

course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 150": "Dr. Lee",
    "ENG 101": "Dr. Martinez",
    "HIS 105": "Dr. Brown"
}

course_rooms = {
    "COMP 163": "M-Eric 300",
    "MATH 150": "Marteena 201",
    "ENG 101": "Crosby 121",
    "HIS 105": "Crosby 210"
}

monthly_budget = {
    "Food": 200,
    "Entertainment": 200,
    "Books": 0,
    "Transportation": 150
}

study_hours = {
    "Programming": 10,
    "Math": 8,
    "English": 4,
    "History": 3
}

contact_num = {
    "Mom": "301-742-4901",
    "Roommate": "301-836-2462",
    "Academic Advisor": "336-285-4213"
}

#required calc 
total_current_credit =sum(credit_hours)
cumulative_gpa = ((sum(GPA_history))/4)
rounded_gpa = round(cumulative_gpa,2)
complete_courses = len(completed_courses)
total_weekly_study = study_hours["Programming"] + study_hours["Math"] + study_hours["English"] + study_hours["History"]
academic_load = total_current_credit + total_weekly_study
toal_monthly_budget = monthly_budget['Food'] + monthly_budget['Entertainment'] + monthly_budget['Books'] + monthly_budget['Transportation'] 
daily_food_budget = (monthly_budget['Food']/30) #maybe right? round two decimals !
annual_budget = (toal_monthly_budget * 12)
study_cost_hour = (monthly_budget['Books']/total_weekly_study) #round two decimals.

#analytics calc
social_media_follows = insta_info[2] + twitter_info[2]
skills_count = len(current_skills) / len(skills_learn)
contact_size = len(contact_num)
entertainment_count = len(entertainment_backlog)
# academic_assessment = 

print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO                ")
print("================================================================")

print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {grad_semester}")
print(f"Major: {major}\n")

current_semester = len(current_courses)
#academic_invest = (sum(study_hours)/5)

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credit} credits across {current_semester} courses")
print(f"Cumulative GPA: {rounded_gpa}")
print(f"Weekly Study Time: {total_weekly_study} hours")
print(f"Academic Investment: ${study_cost_hour} per study hour") 

print()
print(f"Current Courses:")
print(f"{current_courses[0]} - {credit_hours[0]} credits - {(course_professors["COMP 163"])} - {(course_rooms["COMP 163"])}")
print(f"{current_courses[1]} - {credit_hours[1]} credits - {(course_professors["MATH 150"])} - {(course_rooms["MATH 150"])}")
print(f"{current_courses[2]} - {credit_hours[2]} credits - {(course_professors["ENG 101"])} - {(course_rooms["ENG 101"])}")
print(f"{current_courses[3]} - {credit_hours[3]} credits - {(course_professors["HIS 105"])} - {(course_rooms["HIS 105"])}")

print()

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_learn}")
print(f"Career Interests: {career_interest}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_learn)}\n")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${toal_monthly_budget}")
print(f"Food: ${(monthly_budget["Food"])} (${monthly_budget["Food"]/30}/day)")
print(f"Entertainment: $200")
print(f"Books: $125")
print(f"Transportation: $100")
print(f"Annual Projection: $10500")

print()

print(f"=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {social_media_follows} followers across 2 platforms")
print(f"Key Contacts: {len(contact_num)} people in directory\n")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses)}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("================================================================")



