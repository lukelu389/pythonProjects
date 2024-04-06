from flask import Flask, render_template


class Mentee:
    def __init__(self, student_number, start_date, end_date, duration, program, gender, status, high_school, languages,
                 mentor_languages, same_gender_match, extra_activities, goal_extra_activities, other_hobbies):
        self.student_number = student_number
        self.start_date = start_date
        self.end_date = end_date
        self.duration = duration
        self.program = program
        self.gender = gender
        self.status = status
        self.high_school = high_school
        self.languages = languages
        self.mentor_languages = mentor_languages
        self.same_gender_match = same_gender_match
        self.extra_activities = extra_activities
        self.goal_extra_activities = goal_extra_activities
        self.other_hobbies = other_hobbies

    def rank_mentors(self, mentors):
        ranked_mentors = []
        for mentor in mentors:
            rank = 0
            # Rank based on program
            if self.program == mentor.program:
                rank += 5
            # Rank based on gender
            if self.gender == mentor.gender:
                rank += 4
            # Rank based on language
            common_languages = set(self.languages).intersection(set(mentor.languages))
            rank += len(common_languages)
            # Rank based on hobbies or extracurricular activities
            common_activities = set(self.extra_activities).intersection(set(mentor.extra_activities))
            rank += len(common_activities)
            # Rank based on high school
            if self.high_school == mentor.high_school:
                rank += 3
            ranked_mentors.append((mentor.teacherid, rank))
        # Sort mentors based on rank
        ranked_mentors.sort(key=lambda x: x[1], reverse=True)
        return [teacher_id for teacher_id, _ in ranked_mentors]


class Mentor:
    def __init__(self, teacherid, start_date, end_date, duration, program, gender, high_school, languages,
                 mentor_languages, same_gender_match, extra_activities, goal_extra_activities, other_hobbies,
                 training_session_time, student_amount):
        self.teacherid = teacherid
        self.start_date = start_date
        self.end_date = end_date
        self.duration = duration
        self.program = program
        self.gender = gender
        self.high_school = high_school
        self.languages = languages
        self.mentor_languages = mentor_languages
        self.same_gender_match = same_gender_match
        self.extra_activities = extra_activities
        self.goal_extra_activities = goal_extra_activities
        self.other_hobbies = other_hobbies
        self.training_session_time = training_session_time
        self.student_amount = student_amount


app = Flask(__name__)


@app.route("/")
def index():
    # Mock data for demonstration (replace with your actual data)
    mentees = [Mentee("1", "2022-01-01", "2022-06-01", "6 months", "Program A", "Male", "Status A", "High School A",
                      ["English"], ["English"], True, ["Activity A"], ["Goal Activity A"], ["Hobby A"])]
    mentors = [Mentor("M1", "2022-01-01", "2022-06-01", "6 months", "Program A", "Male", "High School A", ["English"],
                      ["English"], True, ["Activity A"], ["Goal Activity A"], ["Hobby A"], "Session Time", 10)]
    return render_template("index.html", mentees=mentees, mentors=mentors)


if __name__ == "__main__":
    app.run(debug=True)
