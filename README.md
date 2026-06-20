# Secure Password Manager

A secure password management application built using Python.  
It allows users to register, log in, generate strong passwords, store credentials securely, and retrieve saved passwords when needed.

## Overview

Secure Password Manager is a command-line based Python project designed to help users manage their login credentials safely. The application uses password hashing for user authentication and encryption for storing saved passwords.

This project is useful for understanding basic concepts of cybersecurity, authentication, encryption, password hashing, and database handling in Python.

## Features

- User registration
- User login authentication
- Password hashing using bcrypt
- Password encryption using Fernet encryption
- Store website, username/email, and password
- View saved passwords
- Generate strong random passwords
- SQLite database for local storage
- Simple command-line interface

## Tech Stack

- Python
- SQLite
- bcrypt
- cryptography / Fernet
- Random and String modules

## Project Structure

```bash
Secure-Password-Manager-
│
├── main.py
├── database.py
├── encryption.py
├── password_generator.py
├── passwords.db
├── requirements.txt
├── .gitignore
└── README.md
