from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required
from werkzeug.security import generate_password_hash
from flask_security import current_user
from flask_admin.menu import MenuLink

from pymaster.ext.database import db
from pymaster.models import User, Nations, Players

# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


admin = Admin()


class UserAdmin(sqla.ModelView):
    column_list = ['username']
    can_edit = False

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)


def init_app(app):
    admin.name = app.config.TITLE
    #admin.base_template='layout.html',
    admin.template_mode = "bootstrap4"
    admin.init_app(app)
    admin.add_view(sqla.ModelView(Nations, db.session))
    admin.add_view(sqla.ModelView(Players, db.session))
    #admin.add_view(UserAdmin(User, db.session))
   