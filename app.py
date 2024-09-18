from flask import Flask

from Repository.seed import seed
from Utils.flow_game import flow_trivia_game
from controllers.answer_question import answer_blueprint
from controllers.question_controller import question_blueprint
from controllers.trivia_controller import trivia_blueprint
from controllers.user_answer_controller import user_answer_bluprint
from controllers.user_controller import user_blueprint

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(user_blueprint, url_prefix="/api/user")
    app.register_blueprint(answer_blueprint, url_prefix="/api/answer")
    app.register_blueprint(question_blueprint, url_prefix="/api/question")
    app.register_blueprint(trivia_blueprint, url_prefix="/api/trivia")
    app.register_blueprint(user_answer_bluprint, url_prefix="/api/user_answer")

    app.run(debug=True)
    seed()
    flow_trivia_game()