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

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   python -m venv venv
   # En Windows (PowerShell):
   .\venv\Scripts\Activate
   # En macOS / Linux:
   source venv/bin/activate

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
     pip install -r requirements.txt
  
## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   streamlit run app.py
