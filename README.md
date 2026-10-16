# Study Planner: Harvard CS50W Capstone Project

A comprehensive, user-isolated academic productivity suite built with **Django**, **Python**, **JavaScript**, and **SQLite/PostgreSQL**, developed as the final Capstone Project for **CS50’s Web Programming with Python and JavaScript (Harvard University / edX)**.

---

## 1. Project Overview

**Study Planner** is a specialized web productivity application engineered for students and academic researchers to manage deadlines, organize course topics, and systematically track study habits. Unlike standard to-do lists, Study Planner directly integrates active study session tracking using the **Pomodoro Technique**, allowing learners to monitor exactly how much time is invested in each subject and avoid academic burnout.

---

## 2. Distinctiveness and Complexity (CS50W Criteria)

### Distinctiveness
- **Departure from Social Networks:** Study Planner contains no public feeds, follower systems, or social interactions. It is a strictly private, personalized utility focused on time allocation and self-management.
- **Departure from E-Commerce:** There are no product listings, bids, or carts. Complexity stems from tracking temporal data (elapsed minutes, study sessions, and intervals) rather than financial transactions.
- **Integrated Pomodoro State Machine:** Features an interactive JavaScript timer communicating asynchronously with Django endpoints to record completed work intervals without reloading the page.
- **Three-Tier Data Hierarchy:** Organizes study workflows hierarchically: `Subjects` → `Tasks` → `Study Sessions`.

### Complexity
- **Modular Multi-App Architecture:** Clean separation into four distinct Django applications: `users`, `subjects`, `tasks`, and `planner`.
- **Dynamic Frontend Integration:** Custom JavaScript event handling for asynchronous task completion toggles, Pomodoro timer state persistence, and real-time interval notifications.
- **Strict Data Isolation:** Custom query filtering ensures that every subject, task, and study record is accessible only by the authenticated owner.
- **Zero-Dependency Responsive Grid:** Lightweight vanilla CSS grid system delivering fast load times and clean responsiveness on mobile devices and laptops.

---

## 3. Main Features

- ⏱ **Interactive Pomodoro Timer:**
  Configurable work and break intervals linked directly to specific academic subjects with browser notifications upon completion.
- 📚 **Subject Management & Color Tagging:**
  Customizable subjects with individual color tags, target study hours, and syllabus tracking.
- ✅ **Task Management & Priority Matrix:**
  Due dates, urgency tags, priority levels, and dynamic completion checkboxes.
- 📈 **Academic Progress Analytics:**
  Summary dashboards showing total hours studied per subject, completed tasks, and streak history.
- 🔒 **User Privacy & Authentication:**
  Registration, session-based authentication, and user-isolated database views.

---

## 4. Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend Framework** | Django, Python |
| **Frontend Scripting** | Vanilla JavaScript (ES6), AJAX (Fetch API) |
| **Styling & Layout** | Modern Vanilla CSS, CSS Grid, Flexbox |
| **Database** | SQLite (Development), PostgreSQL (Production compatible) |
| **Course Curriculum** | Harvard University / edX CS50W |

---

## 5. Architecture Overview

```text
┌────────────────────────────────────────────────────────┐
│               Browser / Client Interface               │
│   Pomodoro JS Engine  │  AJAX Handlers  │  CSS Grid   │
└───────────────────────────┬────────────────────────────┘
                            │ Asynchronous HTTP Requests
┌───────────────────────────▼────────────────────────────┐
│                    Django Web Core                     │
│   ├── users       (Registration & Session Auth)        │
│   ├── subjects    (Course Management & Color Tags)     │
│   ├── tasks       (To-Do Items & Deadlines)            │
│   └── planner     (Pomodoro Sessions & Analytics)      │
└───────────────────────────┬────────────────────────────┘
                            │ ORM Queries
┌───────────────────────────▼────────────────────────────┐
│                  Relational Database                   │
│        (User, Subject, Task, StudySession Models)       │
└────────────────────────────────────────────────────────┘
```

---

## 6. Directory Structure

```text
study_planner/
├── manage.py                     # Django management CLI
├── requirements.txt              # Project dependencies
├── db.sqlite3                    # Local SQLite database
├── study_planner/                # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Django configuration
│   ├── urls.py                   # Master URL routing
│   └── wsgi.py
├── users/                        # User authentication app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/users/          # login.html, register.html
├── subjects/                     # Subject management app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/subjects/       # subjects_list.html, subject_detail.html
├── tasks/                        # Task tracking app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/tasks/          # task_list.html, task_form.html
└── planner/                      # Pomodoro timer and dashboard app
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── static/planner/           # pomodoro.js, styles.css
    └── templates/planner/        # index.html, pomodoro.html, stats.html
```

---

## 7. Prerequisites

- **Python:** 3.10, 3.11, or 3.12
- **pip:** Latest version

---

## 8. Installation Instructions

### Clone Repository
```powershell
# Windows PowerShell
git clone https://github.com/omaremadahmed/study-planner-cs50w.git
Set-Location study-planner-cs50w
```

```bash
# Linux / macOS
git clone https://github.com/omaremadahmed/study-planner-cs50w.git
cd study-planner-cs50w
```

### Virtual Environment Setup
```powershell
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 9. Environment Variables Configuration

Create a `.env` file or export environment variables for production:

```ini
DJANGO_SECRET_KEY=your-secure-production-secret-key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
```

*(For local offline development, safe fallback values are configured in `settings.py`)*.

---

## 10. Database Setup & Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 11. Running the Project

```powershell
python manage.py runserver
# Navigate to http://127.0.0.1:8000 in your browser
```

---

## 12. Testing Instructions

```powershell
python manage.py test
```

---

## 13. Security Considerations

- **User Isolation:** All database queries filter records by `user=request.user`, preventing Insecure Direct Object References (IDOR).
- **CSRF Token Verification:** All AJAX POST and PUT requests include the `X-CSRFToken` header.
- **SQL Parameterization:** Django ORM is strictly used for all queries, blocking SQL injection vectors.

---

## 14. Known Limitations

- Audio notifications for timer completion require browser user interaction permissions before firing audio alerts.
- Offline task caching relies on browser local storage synchronization upon reconnecting.

---

## 15. Future Improvements

- Calendar export integration supporting iCalendar (.ics) format for Google Calendar and Outlook.
- Automated study analytics reports with weekly trend summaries sent via email.

---

## 16. Academic Attribution & License

Developed as the Capstone Project for CS50’s Web Programming with Python and JavaScript (Harvard University). All code is original and adheres to Harvard University academic integrity guidelines.
Licensed under the MIT License.
