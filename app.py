from flask import Flask, request, redirect, jsonify, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def show_home_page():
    """Start our survey"""

    return render_template('home.html', survey=satisfaction_survey)


@app.route('/start', methods=["POST"])
def start_survey():
    """Clear session's responses, and redirect to first question"""

    session['responses'] = []
    return redirect('/questions/0')


@app.route('/questions/<int:num>')
def show_questions(num):
    """Display survey questions"""
    all_user_responses = session['responses']

    if len(all_user_responses) == len(satisfaction_survey.questions):
        """If user answered last question, redirect to thanks page"""
        return redirect('/thanks')

    if len(all_user_responses) != num:
        """If user tries to access question other than succeeding one, flash and redirect"""
        flash("Hey! Don't touch that!")
        return redirect(f"/questions/{len(all_user_responses)}")

    return render_template('questions.html', survey=satisfaction_survey, num=num)


@app.route('/answer', methods=["POST"])
def handle_answer():
    """Retrieve user answer and append to session list"""
    choice = request.form['answer']

    all_user_responses = session['responses']
    all_user_responses.append(choice)
    session['responses'] = all_user_responses # why do we need to rebind this????

    print(request.form) #i.e. ImmutableMultiDict([('answer', 'Yes')])
    print(request.args) #i.e. ImmutableMultiDict([])
    print(all_user_responses) #i.e. ['Yes']

    if len(all_user_responses) == len(satisfaction_survey.questions):
        """If user answers all questions, redirect to thanks page."""
        return redirect('/thanks')
    else:
        return redirect(f"/questions/{len(all_user_responses)}")


@app.route('/thanks')
def thank_you():
    """All questions answer. Redirect to thanks page"""
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