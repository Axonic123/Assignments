import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('marks.csv')

# Ensure the CSV file has the correct headers and data
print("Column names:", df.columns.tolist())

# 1. Average marks of students in Maths
average_maths = df['Marks_Maths'].mean()
print(f"Ans1: Average Marks in Maths is: {average_maths:.2f}")

# 2. Average marks of the class 5 in English
average_english_class5 = df[df['Class'] == 5]['Marks_English'].mean()
print(f"Ans2: Average marks of the class 5 in English: {average_english_class5:.2f}")

# 3. Count of students who failed (marks < 40)
failed_students_count = df[(df['Marks_Maths'] < 40) | (df['Marks_English'] < 40)].shape[0]
print(f"Ans3: Count of students which failed: {failed_students_count}")

# 4. List the top 5 scorers, sorted in descending order with total marks
df['Total_Marks'] = df['Marks_Maths'] + df['Marks_English']
top_5_scorers = df.sort_values(by='Total_Marks', ascending=False).head(5)
print("\nAns4: List of top 5 scorers")
print("\nName | Total Marks")
for idx, row in top_5_scorers.iterrows():
    print(f"{idx+1} {row['Name']} | {row['Total_Marks']}")
