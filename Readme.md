# 🧠 MENTO BOT  
> An AI-Powered Coding Assistant built with **Streamlit**, **LangChain**, and **Ollama**

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-2E7D32?logo=python&logoColor=white)](https://python.langchain.com/)
[![Ollama](https://img.shields.io/badge/Model-Ollama-0A66C2?logo=ollama&logoColor=white)](https://ollama.ai/)
[![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

---

## 💡 Overview

**MENTO BOT** is an intelligent coding assistant designed to help developers write, debug, and optimize Python code effortlessly.  
Built with **Streamlit** for an elegant UI and powered by **LangChain + Ollama** for local LLM interactions.

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
- 🧮 Safe code execution  
- 🎨 Custom dark UI theme  
- ⚙️ Local Ollama model integration

---

## 🖥️ Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| AI Framework | LangChain |
| LLM Backend | Ollama |
| Language | Python 3.10+ |

---

## 🧩 Installation

Clone this repository:
```bash
git clone https://github.com/<your-username>/mento-bot.git
cd mento-bot
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit app:

```bash
streamlit run app.py
```

> 🧠 Make sure **Ollama** is running locally at `http://localhost:11434`.

---

## 🧾 Requirements

Create a `requirements.txt` file with:

```txt
streamlit
langchain
langchain-ollama
langchain-core
ollama
```

---

## ⚙️ How It Works

1. User enters a question or Python problem
2. The app builds a prompt chain using LangChain templates
3. Ollama model (`deepseek-r1:1.5b` by default) generates a structured reply
4. (Optional) The app safely executes Python code and displays results

---

## 🧱 Folder Structure

```
mento-bot/
 ├── app.py               # Main Streamlit application
 ├── requirements.txt     # Python dependencies
 ├── README.md            # Project documentation
 └── .gitignore           # Ignored files and folders
```

---

## 🌐 Deployment (Streamlit Cloud)

You can easily host this app for free:

1. Push your project to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Select `app.py` as the entry file
5. Click **Deploy**

---

## 🛠️ Troubleshooting

| Issue                   | Solution                                        |
| ----------------------- | ----------------------------------------------- |
| `ModuleNotFoundError`   | Run `pip install -r requirements.txt`           |
| Ollama connection error | Ensure Ollama server is running on port `11434` |
| Blank Streamlit page    | Clear cache: `streamlit cache clear`            |
| Git push rejected       | Run `git push -f origin main` if needed         |

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

---

## ❤️ Acknowledgements

Special thanks to:

* [Streamlit](https://streamlit.io/)
* [LangChain](https://python.langchain.com/)
* [Ollama](https://ollama.ai/)
* Open-source contributors inspiring this project


