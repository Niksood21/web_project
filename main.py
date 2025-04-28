from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def book_list():
    return render_template('books.html', books=books)


if __name__ == '__main__':
    app.run()
