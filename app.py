from flask import Flask, request, redirect, jsonify, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_home_page():
    return render_template('home.html', survey=satisfaction_survey)

@app.route('/start', methods=["POST"])
def start_survey():
    return redirect('/questions/0')

@app.route('/questions/<int:num>')
def show_questions(num):
    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thanks')
    if len(responses) != num:
        flash("Hey! Don't touch that!")
        return redirect(f"/questions/{len(responses)}")
    return render_template('questions.html', survey=satisfaction_survey, num=num)

@app.route('/answer', methods=["POST"])
def handle_answer():
    choice = request.form['answer']
    responses.append(choice)

    print(request.form) #i.e. ImmutableMultiDict([('answer', 'Yes')])
    print(request.args) #i.e. ImmutableMultiDict([])
    print(responses) #i.e. ['Yes']

    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thanks')
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/thanks')
def thank_you():
    return render_template('thanks.html', survey=satisfaction_survey)


# ***EXAMPLES TO USE:
# username = request.args["username"]
# wants = request.args.get("wants_compliments")
# comment = request.form["comment"]
# username = request.form["username"]

# @app.route('/posts/<int:id>')
# def find_post(id):
#     post = POSTS.get(id,  "Post not found")
#     return f"<p>{post}</p>"