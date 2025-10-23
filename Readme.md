# 🧠 MENTO BOT  
> An AI-Powered Python Coding Assistant built with **Streamlit**, **LangChain**, and **Ollama**

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-2E7D32?logo=python&logoColor=white)](https://python.langchain.com/)  
[![Ollama](https://img.shields.io/badge/Model-Ollama-0A66C2?logo=ollama&logoColor=white)](https://ollama.ai/)  
![Local Only](https://img.shields.io/badge/Local%20Run-Required-red)  
[![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)  

---

## 💡 Overview

**MENTO BOT** is an intelligent Python coding assistant.  
It helps developers **debug, review, optimize, and generate Python code** in real-time.  

⚠️ **Important:** This app requires **Ollama** to be installed locally and the model downloaded manually. It **cannot run on cloud platforms** like Streamlit Cloud.

---

## 🚀 Features

✅ **Multiple AI Modes**
- 🧠 *Default* – Smart coding assistant  
- 🐞 *Bug Fixer* – Identify and fix code issues  
- 🧑‍💻 *Code Reviewer* – Suggest improvements and style fixes  
- ⚡ *Optimizer* – Enhance performance and efficiency  

✅ **Extras**
- 💬 Persistent chat history  
- 💾 Download chat logs  
- 🧮 Safe Python code execution  
- 🎨 Custom dark UI theme  
- ⚙️ Local Ollama model integration

---

## 🖥️ Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| AI Framework | LangChain |
| LLM Backend | Ollama (local) |
| Language | Python 3.10+ |

---

## ⚠️ Local Setup Instructions

Follow these steps to run the app locally:

1. Install [Ollama](https://ollama.ai/).  
2. Download the required model:

```bash
ollama pull deepseek-r1:1.5b
````

3. Start the Ollama server:

```bash
ollama serve
```

4. Clone this repository:

```bash
git clone https://github.com/<your-username>/mento-bot.git
cd mento-bot
```

5. Install Python dependencies:

```bash
pip install -r requirements.txt
```

6. Run the app:

```bash
streamlit run app.py
```

> ⚠️ The app will **not work on Streamlit Cloud** because it relies on a local Ollama server.



## 🧩 Folder Structure


mento-bot/
 ├── app.py               # Main Streamlit application
 ├── requirements.txt     # Python dependencies
 ├── README.md            # Project documentation
 ├── .gitignore           # Ignored files and folders


## 🛠️ Troubleshooting

| Issue                   | Solution                                                |
| ----------------------- | ------------------------------------------------------- |
| `ModuleNotFoundError`   | Run `pip install -r requirements.txt`                   |
| Blank Streamlit page    | Clear cache: `streamlit cache clear`                    |
| Git push rejected       | Run `git push -f origin main` if needed                 |


## 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first to discuss.


## ❤️ Acknowledgements

* [Streamlit](https://streamlit.io/)
* [LangChain](https://python.langchain.com/)
* [Ollama](https://ollama.ai/)
* Open-source contributors inspiring this project





