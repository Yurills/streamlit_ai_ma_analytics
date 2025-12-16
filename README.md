# Streamlit AI M&A Analytics 📊🚀

A prototype application for **Mergers and Acquisitions (M&A) analysis** powered by **Generative AI** and **Python**. This tool leverages **LangChain** for document intelligence and **Streamlit** for an interactive dashboard, enabling analysts to perform rapid due diligence, financial summarization, and synergy assessment.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![LangChain](https://img.shields.io/badge/LangChain-AI-green)
![OpenAI](https://img.shields.io/badge/OpenAI-API-orange)

## 🌟 Features

* **📈 Automated Financial Analysis**: Upload financial statements (PDF/CSV) and get instant AI-generated summaries and key metric extractions.
* **🤖 Intelligent Q&A**: Chat with your documents using LangChain to ask specific questions about risks, liabilities, or revenue streams.
* **📊 Dynamic Visualization**: Interactive charts and graphs powered by the `ai_visualization` module to track trends and valuations.
* **📑 Due Diligence Reports**: Generate automated draft reports for investment committees.
* **🔍 Synergy Identification**: AI-driven analysis to identify potential operational and financial synergies between target and acquirer.

## 📂 Project Structure

```bash
streamlit_ai_ma_analytics/
├── Hello.py                 # 🏠 Main entry point for the Streamlit application
├── requirements.txt         # 📦 List of Python dependencies
├── ai_analysis/             # 🧠 Core AI logic and LangChain pipelines
│   ├── chains.py            #    (Expected) Custom LangChain chains
│   └── utils.py             #    (Expected) Text processing utilities
├── ai_visualization/        # 🎨 Visualization modules
│   └── charts.py            #    (Expected) Charting logic
├── data/                    # 💾 Directory for storing uploaded or sample data
└── pages/                   # 📄 Multipage Streamlit interface files
