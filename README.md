# 🎓 Smart LMS – CREWAI-Powered Learning Management System

Smart LMS is a role-based Learning Management System built with **Django**, enhanced with an **AI-powered integration** to assist students and teachers in real time. The platform supports structured course creation, lesson management, manual completion tracking, and intelligent academic assistance through AI integration. It is designed to be scalable, secure, and production-ready.

---

## 📌 Overview

Smart LMS provides:

- A structured digital learning environment for students  
- A powerful content management system for teachers  
- AI-based academic support integrated into the dashboard  
- A scalable backend architecture ready for deployment  

The system follows clean architecture principles, role-based access control, and secure environment configuration.

---

## 🚀 Core Features

### 👥 Role-Based Authentication

- Custom user model with role differentiation:
  - 👨‍🎓 Student
  - 👩‍🏫 Teacher
- Role-based dashboard redirection after login  
- Role-specific profile handling  
- Access restriction for unauthorized users  
- Protected routes using Django authentication decorators  

---

### 📚 Course Management (Teacher Panel)

Teachers can:

- Create new courses  
- Set course difficulty level:
  - Beginner  
  - Intermediate  
  - Advanced  
- Add modules inside courses  
- Add lessons inside modules  
- Control lesson completion manually (no auto-completion)  
- Receive visual feedback after successful course creation  

---

### 🎓 Student Learning Interface

Students can:

- View enrolled courses  
- Navigate using sidebar structure:
  - Modules  
  - Lessons  
- Access detailed lesson pages  
- Manually mark lessons as complete  
- Follow structured learning progression  

---

### 🤖 AI Chatbot Integration

The dashboard includes an intelligent assistant:

- Floating chat icon  
- Interactive chat window  
- User messages aligned to the right  
- AI responses aligned to the left  
- Press **Enter** to send messages  
- Contextual learning assistance  

AI integration is powered via secure API configuration using environment variables.

---

### 🎨 UI & UX

- Unified dashboard layout for all roles  
- Responsive design  
- Sidebar navigation  
- Profile redirection based on user role  
- Clean and modern chat interface  
- Flexbox-based alignment for user/AI message separation  

---

## 🏗️ System Architecture

Client (Browser)
│
▼
Django Templates (Frontend)
│
▼
Django Views (Business Logic)
│
▼
Django Models (ORM)
│
▼
Database (SQLite / PostgreSQL)
│
▼
External AI API (Gemini)


---

## 🛠️ Tech Stack

- **Backend:** Django  
- **Frontend:** HTML, CSS, Bootstrap, JavaScript  
- **AI Integration:** Gemini API  
- **Database:** SQLite (Development), PostgreSQL (Production)  
- **Deployment:** not yet
- **Version Control:** Git & GitHub  

---



## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/smart-lms.git
cd smart-lms

### Create Virtual Environment
python -m venv venv

### Install Dependencies
pip install -r requirements.txt


### Create .env file and put all key there
SECRET_KEY=your_secret_key
DEBUG=True
GOOGLE_API_KEY=your_gemini_api_key
