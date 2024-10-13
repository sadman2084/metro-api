# 🚇 Metro-API

Welcome to **Metro-API**, a lightweight, user-friendly backend for handling user balances. Easily recharge, discharge, and manage user data with a powerful FastAPI framework.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CA2430?style=for-the-badge&logo=python)

## 🚀 Features

- 📋 **User management**: Create, read, update, and delete users.
- 💰 **Balance management**: Recharge or discharge user balances with ease.
- 🔄 **SQLAlchemy Integration**: Seamlessly handle database operations.
- 🏗️ **FastAPI-based**: Blazing fast, easy-to-use REST API.

## ⚡ Quick Setup

### 1. Clone the Repo

```bash
git clone https://github.com/SharafatKarim/metro-api.git
```

### 2. Navigate to the directory

```bash
cd metro-api
```

### 3. Deploy on system (Linux)

```bash
bash setup.sh
```

#### 3.1 Manual Setup

If automatic setup (`setup.sh`), you can manually set up the project.

##### 3.1.1 Create a virtual environment

```bash
python -m venv .venv
```

##### 3.1.2 Activate the virtual environment

```bash
source .venv/bin/activate
```

##### 3.1.3 Install the required dependencies

```bash
pip install -r requirements.txt
```

##### 3.1.4 And run the server

```bash
uvicorn main:app --reload
```

### 4. Start the API

Once the setup is complete, the server will start automatically. Visit:

- <http://127.0.0.1:8000/> (It will redirect to `/docs`)

## 📂 Endpoints Overview

- `GET /users/{id}` - Retrieve user balance
- `POST /users` - Create a new user
- `PUT /users/+/id` - Recharge balance
- `PUT /users/-/id` - Discharge balance
- `DELETE /users/{id}` - Delete a user

## 👥 Contributors

[![SharafatKarim's Profilator](https://profilator.deno.dev/SharafatKarim?v=1.0.0.alpha.4)](https://github.com/SharafatKarim)
[![sadman2084's Profilator](https://profilator.deno.dev/sadman2084?v=1.0.0.alpha.4)](https://github.com/sadman2084)

## 📜 License

This project is licensed under the [MIT License](LICENSE).

> Enjoy using Metro-API! ✨
> This `README.md` file is concise and highlights the essential aspects of the project, providing a smooth start for users. Let me know if you'd like to tweak anything!
