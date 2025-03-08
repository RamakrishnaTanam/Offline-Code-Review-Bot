**AI-Powered Code Review Bot (Offline)**




An offline AI-powered code review bot that analyzes Python code snippets, provides feedback, and highlights syntax—all without requiring cloud-based AI models. This project is built using Flask, Pygments for syntax highlighting, and Ollama with CodeLlama for AI-driven analysis.


**Features**


✅ Offline AI Code Review (Uses local CodeLlama via Ollama)

✅ Syntax Highlighting for Python Code

✅ Web-Based Interface (Flask & HTML)

✅ No Cloud Hosting Required (Fully local)

✅ Easy to Run on Any System



**Installation & Setup**


**1️⃣ Clone the Repository**


git clone https://github.com/your-username/ai-code-review-bot.git
cd ai-code-review-bot


2️⃣ Create a Virtual Environment (Optional but Recommended)



python -m venv venv


source venv/bin/activate  # For Linux/Mac


venv\Scripts\activate     # For Windows


3️⃣ Install Dependencies


pip install -r requirements.txt


4️⃣ Install Ollama & CodeLlama Model


🔹 Download and install Ollama


🔹 Pull the CodeLlama model:



ollama pull codellama


5️⃣ Run the Application


python app.py

Then, open your browser and visit:

👉 http://127.0.0.1:5000/




** How It Works**

![Screenshot (38)](https://github.com/user-attachments/assets/b434c204-ee9c-42d3-91fe-63add4ef8a3c)








![Screenshot (37)](https://github.com/user-attachments/assets/5ed9de92-0761-4024-8498-89a21287b3c8)











1️⃣ Enter your Python code snippet in the UI.



2️⃣ Click the Analyze Code button.



3️⃣ The AI bot (CodeLlama) reviews the code and provides suggestions.



4️⃣ The code is also syntax highlighted for better readability.
















