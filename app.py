from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import ratemyprofessor
from GradeDistribution import GradeDistribution

# Initialize Flask app
app = Flask(__name__)

# Load data and set up GradeDistribution class
grades_data_file = "databases/grades.csv"
school = ratemyprofessor.get_school_by_name("Virginia Tech")

# Initialize GradeDistribution
grade_dist = GradeDistribution(grades_data_file)

# Define routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        class_str = request.form['class_str']
        return redirect(url_for('results', class_str=class_str))
    return render_template('index.html')

@app.route('/results/<class_str>')
def results(class_str):
    ranked_df = grade_dist.rank_profs(class_str)
    return render_template('results.html', ranked_df=ranked_df)

if __name__ == '__main__':
    app.run(debug=True)
