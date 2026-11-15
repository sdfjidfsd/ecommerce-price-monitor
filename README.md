# 📊 Automated E-Commerce Price Monitor

A modular web scraping pipeline and interactive web dashboard built with **Python** and **Streamlit** to extract, sanitize, and export product catalog data in real time.

## ✨ Key Features
- **Modular Architecture:** Separation of concerns across scraping logic (`scraper.py`), export formatting (`exporter.py`), and UI layer (`app.py`).
- **Data Sanitization:** Automated cleaning of currency symbols, whitespace, and character encoding artifacts before numeric conversion.
- **Interactive Web Dashboard:** User-friendly Streamlit interface with live `Pandas` DataFrame previews and timestamped `.csv` / `.xlsx` exports.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Scraping & Parsing:** `Requests`, `BeautifulSoup4`
- **Data Processing & Export:** `Pandas`, `OpenPyXL`
- **Frontend UI:** `Streamlit`

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sdfjidfsd/ecommerce-price-monitor.git](https://github.com/sdfjidfsd/ecommerce-price-monitor.git)
   cd ecommerce-price-monitor

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # En Windows (PowerShell):
   .\venv\Scripts\Activate
   # En macOS / Linux:
   source venv/bin/activate

1. **Install dependencies:**
   ```bash
     pip install -r requirements.txt

1. **Execute web interface:**
   ```bash
   streamlit run app.py

## 

<img width="1920" height="915" alt="image" src="https://github.com/user-attachments/assets/7595238d-9bf2-447a-82d6-dffa12305c72" />
