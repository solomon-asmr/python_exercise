from flask import Flask, render_template, request, Mail, Message
import requests
import os



# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  # Your email address
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')  # Your email password

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message_body = request.form.get('message')

        # Create the email message
        subject = f"New Contact Form Submission from {email}"

        msg = Message(subject,
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])  # Send to yourself

        # Structure the email body
        msg.body = f"""
                You have a new message from your blog's contact form:

                From: {email}
                Name: {name}
                Phone: {phone}

                Message:
                {message_body}
                """

        try:
            Mail.send(msg)
        except Exception as e:
            return f"An error occurred: {str(e)}"
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
