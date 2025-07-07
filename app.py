from flask import Flask, render_template, request, redirect, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'

courses = [
    {"id": 1, "title": "Python for Beginners", "description": "Learn Python programming from scratch.", "level": "Beginner"},
    {"id": 2, "title": "Web Development with JavaScript", "description": "Build interactive websites using JS, HTML, and CSS.", "level": "Intermediate"},
    {"id": 3, "title": "Advanced Java & Spring Boot", "description": "Master backend development with Java and Spring.", "level": "Advanced"},
    {"id": 4, "title": "React.js Complete Guide", "description": "Build modern SPAs using React.js and hooks.", "level": "Intermediate"},
    {"id": 5, "title": "Data Structures & Algorithms", "description": "Improve your coding skills and problem-solving.", "level": "Intermediate"},
    {"id": 6, "title": "Full Stack with MERN", "description": "Learn MongoDB, Express, React, and Node in one course.", "level": "Advanced"},
    {"id": 7, "title": "DevOps Fundamentals", "description": "Introduction to CI/CD, Docker, and cloud deployments.", "level": "Beginner"},
    {"id": 8, "title": "Machine Learning with Python", "description": "Build and train models using Scikit-learn and Pandas.", "level": "Advanced"}
]

@app.route('/')
def index():
    return render_template('index.html', courses=courses)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"Message from {name} ({email}): {message}")
    flash("Thank you for contacting us!")
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
