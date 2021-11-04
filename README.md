# The Flasky Blog

### Video Demo: https://www.youtube.com/watch?v=SSSPjkj-7pk

### Description:
A simple blog built along with the [Flask](https://flask.palletsprojects.com/) framework.

UI partly done with the css framework [Bulma](https://bulma.io/).

The app has been restructured with [Blueprints](https://flask.palletsprojects.com/en/2.0.x/blueprints/) for better readability.

### Design choices:
- User session management handled with [Flask-Login](https://flask-login.readthedocs.io/en/latest/).
- Encryption of passwords with the [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) extension.
- Forms were created with the [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) library.
- SQLite Database built with the [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) extension.
- Email sending through [Flask-Mail](https://pythonhosted.org/flask-mail/) - 15min token generated each time requested.


### Installation:
Install with pip:
```
$ pip install -r requirements.txt
```

To run the app correctly you will need to set up a couple environment variables:
- `SECRET_KEY`
- `SQLALCHEMY_DATABASE_URI` #*i.e. "sqlite:///flasky_blog.db"*
- `EMAIL_USER`
- `EMAIL_PWD`

Run:
`flask run`

### Application Structure

```
.
├── app
│   ├── articles
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── utils.py
│   ├── categories
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── config.py
│   ├── errors
│   │   ├── handlers.py
│   │   └── __init__.py
│   ├── flasky_blog.db
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── static
│   │   ├── article_img
│   │   ├── favicon.ico
│   │   ├── profile_img
│   │   │   ├── default.jpg
│   │   ├── script.js
│   │   └── styles.css
│   ├── templates
│   │   ├── account.html
│   │   ├── create_category.html
│   │   ├── create_post.html
│   │   ├── errors
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   ├── list_category.html
│   │   ├── list_post.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   └── user.html
│   └── users
│       ├── forms.py
│       ├── __init__.py
│       ├── routes.py
│       └── utils.py
├── flasky_blog.db
├── README.md
├── requirements.txt
└── run.py
```

#### Improvements that could be done:
- Implement a search bar
- Let the user filter posts by categories
- Integrate [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/) to let the main admin of the blog to easily control the db
