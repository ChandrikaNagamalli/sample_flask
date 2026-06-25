from flask import Flask, request, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return"Welcome to Flask Routing!"
@app.route('/about')
def about():
    return"This is the About page"
@app.route('/user/<name>')
def user(name):
    return f"Hello ,{name}!"
@app.route('/product/<int:id>')
def product(id):
    return f"product ID:{id}"
@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    category = request.args.get('category')
    return f"keywprd: {keyword},category:{category}"
@app.route('/urls')
def bulid_urls():
    home_url = url_for('home')
    about_url = url_for('about')
    user_url = url_for('user',name='john')
    product_url = url_for('product',id=101)
    return f"""
Home URL: {home_url}<br>
About URL: {about_url}<br>
User URL: {user_url}<br>
Product URL: {product_url}
"""
if __name__ == '__main__':
    app.run(debug=True)
    print("chandrika")


