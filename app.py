from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

# Load blog posts from a JSON file
with open('posts.json') as f:
    posts = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', title="Home", posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return render_template('post.html', title=post['title'], post=post)
    else:
        return "Post not found", 404

if __name__ == "__main__":
    app.run(debug=True)
