from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Submission
from career_predictor import predict_career

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create DB tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

# Home page + handle form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        interests = request.form['interests']
        suggestions = predict_career(interests)
        new_submission = Submission(interests=interests, suggestions=', '.join(suggestions))
        db.session.add(new_submission)
        db.session.commit()
        return render_template('result.html', interests=interests, suggestions=suggestions)
    return render_template('index.html')

# Admin page to view entries
@app.route('/admin')
def admin():
    submissions = Submission.query.all()
    return render_template('admin.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
