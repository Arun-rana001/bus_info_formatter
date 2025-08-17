# 🚌 Bus Info Formatter

This is a simple Python project that converts raw bus information into a structured **JSON format**.

## 📌 Features
- Accepts multiple bus entries in a single string (separated by `;`).
- Each bus entry should contain:
  - Bus Number
  - Source
  - Destination
  - Time
  - Fare
- Converts the input into a **JSON object** (if one bus) or a **JSON array** (if multiple buses).
- Pretty-printed JSON output.

## 🚀 Example Usage

### Input:
```python
from businfo import bus_info_formatter

input_data = "202, Rohtak, Delhi, 8:45 AM, 50; 305, Chandigarh, Jaipur, 9:30 PM, 120"
print(bus_info_formatter(input_data))

## ⚙️ Installation & Run
## Clone this repository:
git clone https://github.com/Arun-rana001/bus_info_formatter.git

## Navigate to the project folder:
cd busformatter

## Run the program:
python businfo.py