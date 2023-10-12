import pandas as pd
file_path = r'C:\Users\mohid\Downloads\Assignment_Timecard.xlsx'
df = pd.read_excel(file_path)

df = df.sort_values(by=["Employee Name", "Time"])

# Task 1: Identifying employees who have worked for 7 consecutive days
consecutive_days = df.groupby("Employee Name")["Time"].diff().dt.total_seconds() / 3600
consecutive_days = consecutive_days.groupby(df["Employee Name"]).cumsum()
consecutive_days = df[consecutive_days >= 24 * 7]  # Assuming a day is considered as 24 hours

# Task 2: Finding employees who have less than 10 hours of time between shifts but greater than 1 hour
time_between_shifts = df.groupby("Employee Name")["Time"].diff().dt.total_seconds() / 3600
result = df[(time_between_shifts > 1) & (time_between_shifts < 10)]

# Task 3: Detecting employees who have worked for more than 14 hours in a single shift
# Convert "Timecard Hours (as Time)" to a numeric data type
df["Timecard Hours (as Time)"] = pd.to_numeric(df["Timecard Hours (as Time)"], errors="coerce")

long_shifts = df[df["Timecard Hours (as Time)"] > 14]

# Display the results side by side and in a cleaner format
with open("output.text","w") as f:
 def display_results(task_name, results):
    if not results.empty:
        print(f"{task_name}:")
        for name, group in results.groupby("Employee Name"):
            print(f"Employee Name: {name}")
            print(group.drop(columns=["Employee Name"], axis=1))
            print("-" * 40)  # Separator

display_results("Employees who have worked for 7 consecutive days", consecutive_days)
display_results("Employees with shifts between 1 and 10 hours", result)
display_results("Employees with shifts longer than 14 hours", long_shifts)

f.close()