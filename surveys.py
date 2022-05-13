class Question:
    """One question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Creates 1 question (assume Yes/No for choices)."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text

    def __repr__(self):
        return f"""Instance of Question Class:
            question={self.question} 
            choices={self.choices}
            allow_text={self.allow_text}"""

class Survey:
    """Questionnaire of multiple Question instances."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions
    
    def __repr__(self):
        return f"""Instance of Survey Class:
            title={self.title} 
            instructions={self.instructions}
            questions={self.questions}"""

satisfaction_survey = Survey(
    "Customer Satisfaction Survey", #satisfaction_survey.title
    "Please fill out a survey about your experience with us.", # satisfaction_survey.instructions
    [ # satisfaction_survey.questions[0], satisfaction_survey.questions[1], etc.
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

# personality_quiz = Survey(
#     "Rithm Personality Test",
#     "Learn more about yourself with our personality quiz!",
#     [
#         Question("Do you ever dream about code?"),
#         Question("Do you ever have nightmares about code?"),
#         Question("Do you prefer porcupines or hedgehogs?",
#                  ["Porcupines", "Hedgehogs"]),
#         Question("Which is the worst function name, and why?",
#                  ["do_stuff()", "run_me()", "wtf()"],
#                  allow_text=True),
#     ]
# )

# surveys = {
#     "satisfaction": satisfaction_survey,
#     "personality": personality_quiz,
# }