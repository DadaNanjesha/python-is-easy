## 🎯 **Python Is Easy** 🐍  
> **An Interactive Python Learning App using Streamlit**  

![Python Is Easy](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-red?style=flat-square&logo=streamlit)
![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange)

---

### 🖥️ **Overview**
🚀 **Python Is Easy** is an interactive web-based learning platform built with **Streamlit**. It provides step-by-step lessons on Python fundamentals, with hands-on coding exercises to help beginners or kids practice in real-time.

🔹 Features:
- 📌 **Well-structured Lessons** – Learn **Variables, Loops, Functions**, and more.
- 🎨 **Modern UI Design** – Stylish and easy-to-navigate interface.
- 🏆 **Interactive Coding Editor** – Run Python code inside the app.
- 📊 **Instant Feedback** – See the output of your code instantly.
- 💡 **Beginner-Friendly** – Perfect for new programmers.

🔗 **🚀 Live Preview.**
🔗 Try the **Python Is Easy App** on Streamlit **👉 [Click Here](https://python-is-easy.streamlit.app/)**
---

## 🛠️ **Installation & Setup**
Follow these steps to set up and run the app locally:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/python-is-easy.git
cd python-is-easy
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```bash
streamlit run app.py
```
🔹 The app will launch in your browser automatically!

---

## 📦 **Publishing to GitHub Packages**
### **1️⃣ Build the Package**
```bash
python setup.py sdist bdist_wheel
```

### **2️⃣ Authenticate with GitHub Packages**
Ensure your `~/.pypirc` file contains:
```ini
[distutils]
index-servers =
    github

[github]
repository: https://upload.pypi.pkg.github.com/yourusername
username: __token__
password: <YOUR_GITHUB_TOKEN>
```

### **3️⃣ Upload Your Package**
```bash
twine upload --repository github dist/*
```

---

## 🎯 **Usage**
Once the app is running, you can:
- Select **Variables, Loops, or Functions** from the sidebar.
- Write Python code inside the interactive editor.
- Click **Run Code** to see the output instantly.

---

## 🤝 **Contributing**
Want to improve **Python Is Easy**? We’d love your contributions!  

1. **Fork the repository** 🍴
2. **Clone your fork** 🔧  
   ```bash
   git clone https://github.com/yourusername/python-is-easy.git
   ```
3. **Create a new branch** 🚀  
   ```bash
   git checkout -b feature-branch
   ```
4. **Make your changes and commit** 💡  
   ```bash
   git commit -m "Added new feature"
   ```
5. **Push to GitHub** 📤  
   ```bash
   git push origin feature-branch
   ```
6. **Create a Pull Request** ✅

We’ll review and merge your changes! 🚀

---

## ⚖️ **License**
This project is licensed under the **MIT License**. See the **[LICENSE](LICENSE)** file for more details.

---

## 💬 **Feedback & Support**
📧 **Have questions? Need help?**  
open an issue in this repository.

🎉 **Happy Coding! 🚀**  



