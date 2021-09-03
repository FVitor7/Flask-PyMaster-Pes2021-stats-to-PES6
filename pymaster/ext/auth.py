from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from pymaster.ext.database import db
from pymaster.models import User


def verify_login(user):
    """Valida o usuario e senha para efetuar o login"""
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        return False
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False

def verify_login_user(user):
    """Valida o usuario e senha para efetuar o login"""
    username_user = user.get('username_user')
    password_user = user.get('password_user')
    if not username_user or not password_user:
        return False
    existing_user = User.query.filter_by(username=username_user).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password_user):
        return True
    return False

def create_user(username, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f'{username} ja esta cadastrado')
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
