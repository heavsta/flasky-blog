import os
import secrets

from app import mail
from flask import current_app, url_for
from flask_mail import Message
from PIL import Image

# Save image from the form to the db
def save_img(form_img):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_img.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_img', picture_fn)
    # Resize pic
    output_size = (500, 500)
    img = Image.open(form_img)
    img.thumbnail(output_size)
    # Save
    img.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''Please click on the following link to reset your password:
{url_for('users.reset_token', token=token, _external=True)}

If you didn't make this request please ignore this email.
'''
    mail.send(msg)