from app import cli, create_app, db
from app.models import Message, Notification, Post, Task, User
from config import Config


app = create_app(Config)
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Message': Message,
        'Notification': Notification,
        'Post': Post,
        'Task': Task,
        'User': User,
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
