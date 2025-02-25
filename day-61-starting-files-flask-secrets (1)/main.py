from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[DataRequired(), Email(message="Invalid email address.")]
    )

    password = PasswordField(
        label='Password',
        validators=[DataRequired(), Length(min=8, max=120, message="Field must be at least 8 characters long")]
    )
    submit = SubmitField(label='Login', validators=[DataRequired()])


app = Flask(__name__)

app.secret_key = "123456"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
