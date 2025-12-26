🚀 Python API Automation Framework

A Hybrid Custom API Automation Framework built using Python for scalable, maintainable, and enterprise-ready API testing.
This framework follows industry best practices, clean folder structure, and supports parallel execution, schema validation, and rich reporting.

🖼️ Framework Structure
![Screenshot 2024-08-05 at 08 18 38](https://github.com/user-attachments/assets/3c7d5fe5-207a-42e7-84fe-f4d53354d987)

👨‍💻 Author

Priyanshu Tiwari
QA Automation Engineer | API Automation | Python Enthusiast

📌 Passionate about building robust test frameworks and sharing testing knowledge with the community.

🌐 Connect With Me

▶️ YouTube: https://www.youtube.com/@PriyanshuTiwari
📸 Instagram: https://www.instagram.com/priyanshu_tiwari
💼 LinkedIn: https://www.linkedin.com/in/priyanshutiwari
🐦 Twitter / X: https://twitter.com/priyanshu_t
📧 Email: tiwaripriyanshu640@gmail.com

📌 Project Highlights

✅ Hybrid API Automation Framework
✅ Clean & Scalable Folder Structure
✅ Supports CRUD APIs
✅ Parallel Execution
✅ Schema Validation
✅ Environment-based Configuration
✅ Multiple Test Data Sources
✅ Rich Reporting (Allure + HTML)

🧰 Tech Stack
Language: Python 3.12
HTTP Client: Requests
Test Framework: PyTest
Parallel Execution: PyTest-xDist
Reporting:
    - Allure Report
    - PyTest HTML
Test Data:
    CSV
    Excel
    JSON
    Faker (Dynamic Data)
Schema Validation: jsonschema

✨ Framework Features

🔹 Modular and reusable API utilities

🔹 Supports CRUD operations

🔹 Centralized configuration management

🔹 Data-driven testing

🔹 JSON schema validation

🔹 Parallel test execution

🔹 CI/CD friendly

🔹 Easy to extend and maintain

📦 Installation
1️⃣ Clone the Repository
```
git clone https://github.com/your-username/python-api-automation-framework.git
cd python-api-automation-framework
```
2️⃣ Create Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3️⃣ Install Required Packages
```
pip install requests pytest pytest-html faker allure-pytest jsonschema
```

4️⃣ Install Parallel Execution Plugin
```
pip install pytest-xdist
```

▶️ How to Run Tests
🔹 Run a Single Test
```
pytest tests/tests/crud/test_create_booking.py -s
```
🔹 Run Tests with Allure Report
```
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s
```
🔹 Generate Allure Report
```
allure serve allure_result
```

⚡ Run Tests in Parallel
```
pytest -n auto
```
or
```
pytest -n 4
```

📂 Recommended Folder Structure
├── tests
│   ├── crud
│   ├── schema
│   └── integration
├── utils
│   ├── api_client.py
│   ├── config_reader.py
│   └── logger.py
├── testdata
│   ├── csv
│   ├── json
│   └── excel
├── reports
├── allure_result
├── requirements.txt
└── README.md

🛣️ Roadmap (Future Enhancements)

- OAuth / Token-based Authentication
- Docker Support
- CI/CD Integration (GitHub Actions / Jenkins)
- Environment Switching (QA / UAT / PROD)
- API Contract Testing
- Logging with Loguru
- Retry Mechanism for Flaky APIs

🤝 Contribution Guidelines

- Contributions are welcome! 🚀
- Fork the repository
- Create a feature branch
- Commit your changes
- Push the branch
- Create a Pull Request
