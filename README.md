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
````

## 🚀 Getting Started

### Prerequisites

  * Python 3.9 or higher
  * An OpenAI API Key (or access to a compatible LLM provider)

### Installation

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/Yurills/streamlit_ai_ma_analytics.git](https://github.com/Yurills/streamlit_ai_ma_analytics.git)
    cd streamlit_ai_ma_analytics
    ```

2.  **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**
    Create a `.env` file in the root directory (if not already present) and add your API keys:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## 🏃‍♂️ Usage

Run the Streamlit application from the root directory:

```bash
streamlit run Hello.py
```

Once the server starts, navigate to `http://localhost:8501` in your web browser. You can use the sidebar to navigate between the main dashboard and specific analysis pages located in the `pages/` folder.

## 🛠️ Configuration

The application logic is split into analysis and visualization:

  * **`ai_analysis/`**: Modify this folder to change prompt templates, model parameters, or LangChain agents.
  * **`ai_visualization/`**: Edit this folder to change how data is plotted (e.g., switching from Matplotlib to Plotly).

**Author**: [Yurills](https://www.google.com/search?q=https://github.com/Yurills)

