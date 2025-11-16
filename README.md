# ⚡ EV Intelligence System  
### 🔋 Smart EV Battery & Range Predictor + 🤖 AI Chatbot  

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-yellow)
![Groq](https://img.shields.io/badge/AI-Groq%20Llama%203.3-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 **Project Overview**

The **EV Intelligence System** is an AI-driven application that integrates:  
🔹 A **Machine Learning–based Predictor** to estimate **battery capacity** and **real-world driving range**, and  
🔹 A **Groq-powered AI Chatbot** that interacts with users to answer EV-related questions in natural language.

Built using **Python**, **Streamlit**, **Scikit-Learn**, and **Groq API**, this project merges **Data Science + Generative AI** to create a futuristic EV assistant.

---

## 🎯 **Core Features**

- 🔋 Predict **Battery Capacity (kWh)**  
- 🚗 Predict **Driving Range (km)**  
- 💬 Ask EV-related queries via **AI Chatbot (Llama 3.3)**  
- 🧮 Lightweight Random Forest model trained on simplified EV specs  
- 🧠 Integrated `.env` key management (for Groq API)  
- 🖥️ Clean, modern Streamlit interface with dark mode  

---

## 🧭 **Workflow Diagram**

```text
User Input
   │
   ▼
Machine Learning Model (RandomForest)
   │
   ├── Predicts Battery Capacity
   ├── Predicts Range (km)
   │
   ▼
Groq Chatbot (Llama 3.3)
   │
   ▼
Streamlit Front-End (Unified App)

⚙️ Technologies Used
Category	Tools / Libraries
💻 Programming	Python
🧠 Machine Learning	Scikit-Learn, Pandas, NumPy
🌐 Web Framework	Streamlit
🤖 Chatbot	Groq API (Llama 3.3 70B Versatile)
📊 Visualization	Matplotlib, Seaborn
🧩 Environment	python-dotenv, joblib
🧰 IDE	VS Code / Jupyter Notebook
🧱 Project Structure
EV-Project/
│── app.py                   # Main Streamlit entry point (Chatbot + Predictor)
│── chatbot.py               # Handles Groq API chat logic
│── model/
│     └── simple_ev_model.pkl # ML model file
│── pages/
│     ├── EV_chatbot.py      # Chatbot interface
│     └── ev_predictor.py    # Predictor interface
│── .env                     # (hidden) API key file
│── .gitignore               # Ignores env, cache, models
│── requirements.txt         # Python dependencies
│── README.md                # This file

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/AKSHAYA1323/EV-Range-and-Battery-Health-Prediction.git
cd EV-Range-and-Battery-Health-Prediction

2️⃣ Create and Activate a Virtual Environment
python -m venv .venv
.venv\Scripts\activate        # On Windows
# or
source .venv/bin/activate     # On Mac/Linux

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Add Your Groq API Key

Create a file named .env in your project root:

GROQ_API_KEY=your_actual_groq_api_key_here

▶️ Run the Application
streamlit run app.py


Then open your browser at 👉 http://localhost:8501

🧩 Sidebar Options

🔋 EV Predictor — Enter EV specs to get range & battery predictions

🤖 EV Chatbot — Ask anything about electric vehicles

🧠 Machine Learning Details

Algorithm: RandomForestRegressor

Features Used:

Vehicle Weight (kg)

Motor Power (kW)

Battery Type (LFP/NMC)

Fast Charging Support (Yes/No)

Vehicle Type (SUV/Sedan/Hatchback)

Aerodynamic Efficiency (0 – 1)

Outputs:

Estimated Battery Capacity (kWh)

Predicted Range (km)

💬 AI Chatbot
Attribute	Description
Model	Llama 3.3 (70B Versatile)
Provider	Groq API
Purpose	Answers EV-related queries
Integration	Python SDK + dotenv + Streamlit
Examples	“How long to charge a Tata Nexon EV?” / “Best EV for city driving?”
🖼️ Sample Screenshots
EV Predictor	EV Chatbot

	

(Replace these with your real screenshots)

📈 Future Enhancements

⚡ Add charging cost/time estimation

🔋 Integrate real-time telemetry for live EV stats

📊 Visualize battery degradation over time

☁️ Deploy app on Streamlit Cloud / Render / Hugging Face

🗣️ Add voice-based chatbot interaction