
# 🎓 Student Grade Calculator

## 📘 Overview
The **Student Grade Calculator** is a Python-based data analysis project that reads student marks from a CSV file and automatically computes:
- Total marks  
- Percentage  
- Grade (A+, A, B, C, or D)

It also identifies:
- The **highest scorer (topper)**
- The **lowest percentage**
- The **average performance**
- The **number of students who failed (<60%)**

Finally, it generates visualizations for better performance insights and exports a new report file.

---

## ⚙️ Features
✅ Reads data from a CSV file (`students_marks.csv`)  
✅ Calculates total marks and percentage  
✅ Automatically assigns grades  
✅ Exports processed data to a new CSV (`students_report.csv`)  
✅ Generates four graphs:
1. **Bar Chart** – Student performance comparison  
2. **Horizontal Bar Chart** – Grade-wise color-coded comparison  
3. **Histogram** – Distribution of student percentages  
4. **Pie Chart** – Grade distribution  

---

## 🧩 Technologies Used
- **Python 3.x**
- **Pandas** – Data handling and analysis  
- **Matplotlib** – Visualization and chart plotting  

---

## 📂 File Descriptions
| File Name | Description |
|------------|-------------|
| `students_marks.csv` | Input dataset containing student names and marks in different subjects |
| `grade_calculator.py` | Main Python script that performs grade calculation and visualization |
| `students_report.csv` | Output file generated after running the script, containing total marks, percentage, and grade for each student |

---

## ▶️ How to Run

### **Step 1: Install Required Libraries**
```bash
pip install pandas matplotlib
```

### **Step 2: Place Files**
Make sure the following files are in the same folder:
```
students_marks.csv
grade_calculator.py
```

### **Step 3: Run the Script**
```bash
python grade_calculator.py
```

### **Step 4: Output**
- Console will show summary statistics (topper, average, fails)
- Graphs will display automatically
- A new CSV file `students_report.csv` will be created

---

## 📊 Example Output (Console)
```
Highest Percentage: 94.33 (Riya)
Lowest Percentage: 52.00
Average Percentage: 76.45
Number of Students Failed(<60%): 2
```

---

## 📦 Tools for Download
If you want to download the required tools manually:
- [Download Python](https://www.python.org/downloads/)
- [Install Pandas](https://pypi.org/project/pandas/)
- [Install Matplotlib](https://pypi.org/project/matplotlib/)

---

## 💡 Future Enhancements
- Add support for more subjects automatically
- Create an interactive GUI version using **Tkinter** or **Streamlit**
- Generate PDF reports for each student

---

📁 **Author:** Souvik Ghosh 
📅 **Project Type:** Data Analysis / Visualization Project
