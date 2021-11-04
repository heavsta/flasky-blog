import os
import secrets

from flask import current_app

def save_img_raw(form_img):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_img.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/article_img', picture_fn)
    # Save
    form_img.save(picture_path)

    return picture_fn