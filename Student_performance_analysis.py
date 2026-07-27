import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 1. LOAD STUDENT DATASET
file_path = r"C:\Users\D PREETHI\Downloads\archive\Students Performance Dataset.csv"
df = pd.read_csv(file_path)
print("Dataset Loaded Successfully!")
print("Number of Students:", len(df))
print("Columns:", list(df.columns))
# 2. FIND NUMERICAL COLUMNS
numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
print("\nNumerical Columns:")
print(numeric_columns)
# 3. CALCULATE METRICS
total_students = len(df)
if len(numeric_columns) > 0:
    average_values = df[numeric_columns].mean()
    first_numeric_column = numeric_columns[0]
else:
    average_values = pd.Series()
    first_numeric_column = None
# 4. CREATE DASHBOARD
fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 10)
)
fig.suptitle(
    "Student Performance Analysis Dashboard",
    fontsize=22,
    fontweight="bold"
)
# CHART 1: TOTAL STUDENTS
axes[0, 0].bar(
    ["Total Students"],
    [total_students],
    color="royalblue"
)
axes[0, 0].set_title(
    "Total Number of Students",
    fontsize=14,
    fontweight="bold"
)
axes[0, 0].set_ylabel("Student Count")
# CHART 2: AVERAGE STUDENT METRICS
if len(numeric_columns) > 0:
    average_values.plot(
        kind="bar",
        ax=axes[0, 1],
        color="orange"
    )
    axes[0, 1].set_title(
        "Average of Student Metrics",
        fontsize=14,
        fontweight="bold"
    )
    axes[0, 1].set_ylabel("Average")
# CHART 3: PIE CHART - AGE GROUP DISTRIBUTION
if first_numeric_column is not None:
    pie_data = pd.cut(
        df[first_numeric_column],
        bins=5
    ).value_counts().sort_index()
    axes[1, 0].pie(
        pie_data.values,
        labels=pie_data.index.astype(str),
        autopct="%1.1f%%",
        startangle=90,
        colors=[
            "skyblue",
            "lightgreen",
            "orange",
            "pink",
            "violet"
        ]
    )
    axes[1, 0].set_title(
        "Age Group Distribution",
        fontsize=14,
        fontweight="bold"
    )
# CHART 4: AGE DISTRIBUTION
age_column = None
for column in df.columns:
    if column.lower() == "age":
        age_column = column
        break
if age_column is not None:
    df[age_column].value_counts().sort_index().plot(
        kind="bar",
        ax=axes[1, 1],
        color="mediumseagreen"
    )
    axes[1, 1].set_title(
        "Distribution of Age",
        fontsize=14,
        fontweight="bold"
    )
    axes[1, 1].set_xlabel("Age")
    axes[1, 1].set_ylabel("Number of Students")
else:
    axes[1, 1].text(
        0.5,
        0.5,
        "Age column not found",
        ha="center",
        va="center",
        fontsize=14
    )
    axes[1, 1].set_title(
        "Distribution of Age"
    )
# FINAL DASHBOARD SETTINGS
plt.tight_layout()
plt.savefig(
    "student_performance_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)
print("\n--- DASHBOARD CREATED SUCCESSFULLY ---")
plt.show()