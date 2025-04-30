# 🏞️ NPS API Exporter

A command-line Python tool that extracts U.S. National Park data from the [National Park Service API](https://www.nps.gov/subjects/developer/api-documentation.htm), flattens the nested fields, and exports a clean `.csv` file that opens perfectly in Google Sheets or Excel.

---
---

## 🎯 About This Project

This project was developed as a sample portfolio piece to demonstrate real-world skills in API integration, data cleaning, command-line tooling, and data export. It simulates a client-facing task that involves fetching public data, flattening nested structures, and delivering a ready-to-use dataset.

**Skills demonstrated:**
- Python scripting and automation
- REST API consumption with `requests`
- Command-line interface design with `argparse`
- Environment variable handling with `python-dotenv`
- Data transformation and cleanup
- CSV export (Excel/Google Sheets-ready)
- Project structuring for reusability
- GitHub project packaging


## 🚀 Features

- Fetches real-time park data from the `/parks` endpoint
- Filters by U.S. state code (e.g., `--state OR`)
- Flattens nested fields like `activities` and `operatingHours`
- Outputs clean, structured `parks.csv`
- Secure API key handling via `.env`
- Easy to configure, clone, or extend

---

## 📦 Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root with your API key:

```ini
NPS_API_KEY=your_actual_key_here
```

To get a key, sign up at:  
https://www.nps.gov/subjects/developer/get-started.htm

---

## 💻 Usage

### Fetch all parks:

```bash
python main.py
```

### Fetch only Oregon parks:

```bash
python main.py --state OR
```

The script will generate `parks.csv` in the current directory.

---

## 🧪 Sample Output

| ID     | Name                         | Description              | Activities            | Operating Hours |
|--------|------------------------------|--------------------------|------------------------|-----------------|
| A1B2C3 | Crater Lake National Park    | Deep volcanic lake...    | Hiking, Camping        | Open all year \| Monday: 24 hours; ... |

---

## 🗺️ Fields Included

- `id` — Unique park identifier  
- `fullName` — Full park name  
- `description` — Summary of the park  
- `activities` — Comma-separated list of supported activities  
- `operatingHours` — Description and per-day hours, flattened

---

## 📁 Project Structure

```
nps-api-exporter/
├── main.py
├── .env
├── .gitignore
├── parks.csv
├── requirements.txt
└── README.md
```

---

## ✨ Future Enhancements

Planned or possible additions for version 2:

- `--output excel` option with `.xlsx` export via `pandas` or `openpyxl`
- Pagination support for fetching all parks
- Merge data from `/alerts`, `/activities/parks`, etc.
- Multi-tab Excel export (e.g., `Parks`, `Alerts`)
- Add CLI options:
  - `--filename`
  - `--include-alerts`
  - `--format csv|excel`
- GUI version using Tkinter or Streamlit
- Web app wrapper using Flask or FastAPI

---

## 📣 Attribution

Built using data provided by the [National Park Service API](https://www.nps.gov/subjects/developer/api-documentation.htm).

---

## 🧑‍💻 Author

Geoff Jensen  
_Freelance Python developer building tools to make public data more accessible and usable._


