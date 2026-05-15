# Study Planner - Capstone Project for CS50’s Web Programming with Python and JavaScript

## Overview
Study Planner is a comprehensive web-based productivity application designed specifically for students and lifelong learners to organize their academic life, manage deadlines, and track study habits. Unlike simple "to-do" lists, Study Planner integrates task management with active study session tracking using the Pomodoro technique, allowing users to not just list what they need to do, but actually monitor the time invested in each subject.

The application is built using a Django backend with multiple interconnected apps and a dynamic JavaScript frontend that provides a seamless, responsive experience. It addresses the common problem of "academic burnout" by helping users visualize their progress and maintain a healthy balance between study sessions and breaks.

---

## Distinctiveness and Complexity

### Distinctiveness
The Study Planner project was designed from the ground up to be fundamentally distinct from the previous projects in the CS50W curriculum.

1.  **Departure from Social Networks (Project 4):** While Project 4 (Network) focused on user-to-user interaction, following, and public posting, Study Planner is a private, personalized productivity suite. There is no social feed; instead, the focus is on data visualization and personal time management. The logic centers around the relationship between the user and their own academic goals.
2.  **Departure from E-commerce (Project 2):** Study Planner contains no concept of listings, bidding, transactions, or shopping carts. It is a utility tool rather than a marketplace. The complexity is derived from tracking temporal data (time spent studying) rather than commercial data.
3.  **Unique Features:** The integration of a **Pomodoro Timer** directly linked to the user's subjects is a unique element not found in any course project. This required implementing a JavaScript-based state machine for the timer that communicates with the Django backend to persist completed sessions.
4.  **Data Relationships:** The project manages a three-tier hierarchy of data: Subjects -> Tasks -> Study Sessions. This structure is more complex than the flat structures found in the early projects.

### Complexity
The complexity of Study Planner is evident in both its architectural design and its functional implementation:

*   **Multi-App Architecture:** The project is organized into four distinct Django apps (`users`, `subjects`, `tasks`, and `planner`), each handling a specific domain of the application. This modularity ensures clean separation of concerns but requires sophisticated cross-app referencing and URL routing.
*   **JavaScript Integration:** The frontend utilizes JavaScript for more than just simple UI tweaks. The Pomodoro timer is a fully functional JavaScript application that handles intervals, notifications, and AJAX requests to save data without refreshing the page. Furthermore, task completion toggles and filtering are handled dynamically to provide a modern "Single Page Application" feel within the Django framework.
*   **Database Schema:** The models utilize advanced Django features such as `TextChoices` for priorities and session types, `ForeignKey` with complex `related_name` attributes for efficient querying, and custom `save()` methods to handle timestamps.
*   **Mobile Responsiveness:** The application uses a custom-built responsive CSS grid system (without heavy reliance on frameworks like Bootstrap) to ensure that students can track their tasks on a laptop or check their schedule on a mobile device while in class.
*   **Personalization and Security:** Every piece of data is strictly tied to a user. The application implements rigorous checks to ensure that users can only view, edit, or delete their own subjects, tasks, and sessions, preventing unauthorized data access.

---

## File Contents

### Main Project Folder (`study_planner/`)
*   `manage.py`: The standard Django management script used for running the server, migrations, and shell.
*   `requirements.txt`: Contains all necessary Python dependencies, including Django, Markdown (for note rendering), and django-filter.
*   `db.sqlite3`: The SQLite database containing the project's data.

### Project Configuration (`study_planner/study_planner/`)
*   `settings.py`: Contains the project configuration, including database settings, installed apps, middleware, and the definition of static/template directories.
*   `urls.py`: The root URL configuration that routes requests to the individual apps.
*   `wsgi.py` & `asgi.py`: Standard entry points for web servers.

### Users App (`study_planner/users/`)
Handles authentication and user profiles.
*   `models.py`: Uses the default Django User model but is structured to support future extensions.
*   `views.py`: Contains logic for user registration, login, and logout.
*   `templates/users/`:
    *   `login.html`: A clean, focused login interface.
    *   `register.html`: The signup form for new users.

### Subjects App (`study_planner/subjects/`)
The foundational app for organizing academic content.
*   `models.py`: Defines the `Subject` model, which includes fields for name, description, and a color hex code for UI personalization.
*   `views.py`: Handles CRUD operations for subjects.
*   `templates/subjects/`:
    *   `subjects_list.html`: Displays all subjects with their associated colors and targets.
    *   `subject_detail.html`: A detailed view of a single subject, showing its specific tasks and study history.

### Tasks App (`study_planner/tasks/`)
Manages the user's to-do items.
*   `models.py`: Defines the `Task` model with fields for priority, deadline, estimated time, and completion status.
*   `views.py`: Contains the logic for adding, editing, and deleting tasks, as well as the AJAX view for toggling completion.
*   `templates/tasks/`:
    *   `index.html`: The main dashboard showing upcoming tasks, filtered by priority or deadline.
    *   `add_task.html`: The form for creating new tasks.
    *   `edit_task.html`: The form for modifying existing tasks.

### Planner App (`study_planner/planner/`)
The "engine" of the application, focused on the study timer.
*   `models.py`: Defines the `StudySession` model, which logs the duration and type of study sessions.
*   `views.py`: Handles the rendering of the timer and the API endpoint for saving session data.
*   `static/js/`:
    *   `planner.js`: The core JavaScript file that runs the Pomodoro timer, manages the countdown, and sends Fetch API requests to the backend.
*   `templates/planner/`:
    *   `planner.html`: The main interface for the study timer.
    *   `pomodoro.html`: A specialized sub-view for the Pomodoro interface.

### Global Assets
*   `templates/base.html`: The master template containing the common HTML structure, navigation bar, and responsive meta tags.
*   `templates/navbar.html`: The navigation component that changes based on whether the user is authenticated.
*   `static/css/styles.css`: A comprehensive CSS file containing all the styling for the application, including the grid system, custom buttons, and mobile-responsive media queries.

---

## How to Run the Application

1.  **Install Dependencies:**
    Ensure you have Python installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Apply Migrations:**
    Set up the database schema:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3.  **Start the Server:**
    Run the Django development server:
    ```bash
    python manage.py run_server
    ```

4.  **Access the App:**
    Open your browser and go to `http://127.0.0.1:8000/`. You can register a new account to start planning your studies.

---

## Additional Information

### Design Choices
*   **Color Coding:** We implemented a hex-color system for subjects to allow users to visually distinguish between different classes (e.g., Math is Blue, History is Red) across the entire application.
*   **AJAX for Productivity:** We chose to use the Fetch API for task completion and timer logging. We believe that a productivity tool should never force a full page reload for minor updates, as it breaks the user's flow.
*   **Responsive Meta-tags:** The app uses standard viewport tags and CSS Flexbox/Grid to ensure it is usable on tablets and phones, satisfying the mobile-responsive requirement.

### Complexity Justification
While some might see a task manager as simple, the integration of **Subject-Specific Time Tracking** adds a layer of complexity that mirrors real-world professional tools. The ability to see exactly how many hours were spent on "Calculus" vs "Economics" provides deep insights that require careful database indexing and aggregation logic in the views.

---

*This project was completed as part of the CS50W Capstone requirement.*