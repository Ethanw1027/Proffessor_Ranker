from flask import Flask, render_template, request, redirect, session
import pandas as pd
from GradeDistribution import GradeDistribution

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management
grades_data_file = "databases/grades.csv"

grade_dist = GradeDistribution(grades_data_file)

@app.route('/', methods=['GET', 'POST'])
def prof_search():
    return render_template('prof_search.html', ranked_profs=None)
    if request.method == 'POST':
        course_dept = request.form['course_dept']
        course_num = request.form['course_num']
        course_data = grade_dist.search_class(course_dept, course_num)
        
        if not course_data.empty:
            ranked_profs = grade_dist.rank_profs(course_data)
            return render_template('prof_search.html', ranked_profs=ranked_profs)
    else:
        return render_template('prof_search.html', ranked_profs=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
