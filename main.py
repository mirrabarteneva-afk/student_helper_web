from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import sqlite3

from validators import validate_registration_data


app = FastAPI(debug=True)

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

def get_db_connection():
    conn = sqlite3.connect('data/data.sqlite')
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                phone_number TEXT NOT NULL,
                password TEXT NOT NULL
                )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.get('/', response_class=HTMLResponse)
async def register_root(request: Request):
    return templates.TemplateResponse(request, 'register.html', {'request': request})

@app.get('/', response_description=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request, 'index.html', {'request': request})

@app.post('/register', response_class=HTMLResponse)
async def register(
    request: Request,
    username: str = Form(...),
    phone_number: str = Form(...),
    password: str = Form(...),
    password_repeat: str = Form(...)
):
    errors = validate_registration_data(
        phone_number, password, password_repeat
    )
    if errors:
        return templates.TemplateResponse(
            request,
            'register.html',
            {'request': request, 'errors': errors}
        )
    try:
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO users (name, phone_number, password) VALUES (?, ?, ?)',
            (username, phone_number.replace(' ', ''), password)
        )
        conn.commit()
        conn.close()
        success_message = 'Регистрация успешна'
        return templates.TemplateResponse(
            request,
            'index.html',
            {'request': request, 'success': success_message, 'username': username}
        )
    except sqlite3.IntegrityError:
        errors.append('Пользователь с таким номером уже существует')
        return templates.TemplateResponse(
            request,
            'register.html',
            {'request': request, 'errors': errors}
        )
    
@app.post('/login', response_class=HTMLResponse)
async def root_login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM users WHERE name = ? AND password = ?',
        (username, password)
    ).fetchone()
    conn.close()

    if user:
        success_message = 'Добро пожаловать'
        return templates.TemplateResponse(
            request,
            'index.html',
            {'request': request, 'success': success_message, 'username': username}
        )
    else:
        error_message = 'Логин или пароль неверны'
        return templates.TemplateResponse(
            request,
            'register.html',
            {'request': request, 'error_message': error_message}
        )
