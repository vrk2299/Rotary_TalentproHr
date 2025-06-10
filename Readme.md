# TalentHuntPro HR Portal 🧑‍💼💻

A simple job application portal built with Flask for demonstration and training purposes. It supports:

- Candidate job listing & application
- HR login with dashboard to view applicants
- Resume uploads (basic handling)
- SQLite backend (can be swapped with AWS RDS)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/TalentHuntPro.git
cd TalentHuntPro
2. Set up virtual environment

python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
3. Install dependencies
#yum install -y gcc gcc-c++ python3-devel (better to run this before all )
pip install -r requirements.txt
4. Initialize the database

python init_db.py
5. Run the app

python app.py
App will be live at: http://127.0.0.1:5000

🗃️ Folder Structure

TalentHuntPro/
├── app.py
├── init_db.py
├── models.py
├── requirements.txt
├── talenthunt.db
├── templates/
│   ├── apply.html
│   ├── apply_success.html
│   ├── home.html
│   ├── hr_dashboard.html
│   ├── login.html
│   └── ...
└── static/


Rotary Club Training Program, June 2025
