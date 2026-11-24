# ==========================================
# STUDENT PERFORMANCE DATA ANALYSIS
# Libraries: Pandas and NumPy
# ==========================================

import pandas as pd
import numpy as np


# ==========================================
# 1. DISPLAY SETTINGS
# ==========================================

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 20)


# ==========================================
# 2. LOAD DATASET
# ==========================================

df = pd.read_csv(
    r"C:\Users\Abdullah\Favorites\Downloads\student_performance_practice.csv"
)

print("\n--- ORIGINAL DATASET ---")
print(df)


# ==========================================
# 3. BASIC DATA EXPLORATION
# ==========================================

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns)

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- NULL VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())


# ==========================================
# 4. DATA CLEANING
# ==========================================

# Fill missing numerical values
df.interpolate(method='linear', inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\n--- CLEANED DATASET ---")
print(df)


# ==========================================
# 5. BASIC STATISTICAL ANALYSIS
# ==========================================

print("\n--- MATHEMATICS ---")
print("Average Math Score:", df['math_score'].mean())

print("\n--- SCIENCE ---")
print("Highest Science Score:", df['science_score'].max())
print("Lowest Science Score:", df['science_score'].min())


# ==========================================
# 6. DEPARTMENT ANALYSIS
# ==========================================

print("\n--- STUDENTS PER DEPARTMENT ---")

department_count = df.groupby('department')['student_id'].count()
print(department_count)


print("\n--- DEPARTMENT-WISE TOTAL MARKS ---")

department_stats = df.groupby('department')['Total_marks'].agg(
    ['min', 'max', 'mean', 'count']
)

print(department_stats)


print("\n--- AVERAGE SCIENCE SCORE BY DEPARTMENT ---")

print(df.groupby('department')['science_score'].mean())


print("\n--- SUBJECT-WISE DEPARTMENT AVERAGES ---")

subject_average = df.groupby('department')[
    ['math_score', 'english_score', 'science_score']
].mean()

print(subject_average)


# ==========================================
# 7. ATTENDANCE ANALYSIS
# ==========================================

print("\n--- STUDENTS WITH ATTENDANCE ABOVE 85% ---")

high_attendance = df[df['attendance_percent'] > 85]

print(high_attendance)


# ==========================================
# 8. STUDENT PERFORMANCE ANALYSIS
# ==========================================

# Calculate total marks
df['Total_marks'] = (
    df['math_score'] +
    df['science_score'] +
    df['english_score']
)

print("\n--- TOTAL MARKS ---")
print(df)


# Sort students by average score
df.sort_values(
    by='average_score',
    ascending=False,
    inplace=True
)

print("\n--- TOP 10 STUDENTS ---")
print(df.head(10))


# ==========================================
# 9. DEPARTMENT RANKING
# ==========================================

department_ranking = (
    df.groupby('department')['Total_marks']
    .mean()
    .sort_values(ascending=False)
)

print("\n--- DEPARTMENT RANKING ---")
print(department_ranking)

print("\nHighest Department Average:")
print(department_ranking.max())


# ==========================================
# 10. STUDY HOURS ANALYSIS
# ==========================================

study_analysis = (
    df.groupby('study_hours_per_day')['Total_marks']
    .mean()
    .sort_values(ascending=False)
)

print("\n--- STUDY HOURS VS TOTAL MARKS ---")
print(study_analysis)


# ==========================================
# 11. ACADEMIC PERFORMANCE
# ==========================================

df['academic'] = (
    df['previous_exam_score'] +
    df['assignment_score'] +
    df['Total_marks'] +
    df['average_score']
)

print("\n--- ACADEMIC PERFORMANCE ---")
print(df)


# ==========================================
# 12. FINAL DATASET INFORMATION
# ==========================================

print("\n--- FINAL DATA TYPES ---")
print(df.dtypes)

print("\n--- UNIQUE STUDY HOURS ---")
print(df['study_hours_per_day'].unique())

print("\n--- FINAL DATASET SHAPE ---")
print(df.shape)

# ==========================================
# END OF PROJECT
# ==========================================
