# PortfolioFastAPI: Full-Stack with Admin Panel

A modern, full-stack portfolio web application built using **FastAPI** for the backend, **Jinja2** and **TailwindCSS** for templating and styling, and an **SQLite** database managed by **TortoiseORM**. The app also includes an admin panel for easy management and a mail-sending feature for contact forms.

---

## Features

- **FastAPI Backend**: High-performance backend framework.
- **Jinja2 Templates**: Dynamic frontend rendering.
- **Bootstrap & TailwindCSS**: Modern and responsive design for both the portfolio and admin panel.
- **SQLite Database**: Lightweight database powered by **TortoiseORM** for seamless data handling.
- **Admin Panel**: Manage your portfolio content easily with a dedicated admin interface styled with TailwindCSS.
- **Mail Sender**: Integrated email functionality for contact forms.

---

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: Jinja2, Bootstrap, TailwindCSS
- **Database**: SQLite (with TortoiseORM)
- **Email**: MailSender
- **Styling (Admin Panel)**: TailwindCSS

---

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/theshakawat/PortfolioFastAPI-Full-Stack-with-Admin-Panel.git
   cd PortfolioFastAPI-Full-Stack-with-Admin-Panel
   ```

2. **Install Dependencies**
   Make sure you have Python 3.x installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the FastAPI server by running:
   ```bash
   python3 main.py
   ```
   or
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000
   ```

4. **Access the App**
   - Portfolio Website: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Admin Panel: [http://127.0.0.1:8000/admin/login](http://127.0.0.1:8000/admin/login)

---

## Usage

- **Portfolio Section**: Showcase your projects, skills and experiences.
- **Admin Panel**: Add, edit or delete portfolio items, manage user details and more.
- **Contact Form**: Users can send messages via the integrated mail-sending feature.

---

## Contributing

Feel free to contribute to this project! Open an issue or submit a pull request if you have any improvements or bug fixes.