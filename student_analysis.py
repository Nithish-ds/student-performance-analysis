import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Name": [
        "Arjun", "Priya", "Karthik", "Sneha", "Rahul",
        "Divya", "Vikram", "Ananya", "Rohit", "Meera",
        "Sanjay", "Pooja", "Amit", "Neha", "Varun",
        "Kavya", "Surya", "Nisha", "Deepak", "Ishita"
    ],
    
    "Department": [
        "CSE", "IT", "CSE", "AI", "IT",
        "AI", "CSE", "IT", "AI", "CSE",
        "IT", "AI", "CSE", "IT", "AI",
        "CSE", "IT", "AI", "CSE", "IT"
    ],
    
    "Semester": [
        1, 1, 2, 2, 1,
        3, 2, 1, 3, 2,
        1, 3, 2, 1, 3,
        2, 1, 3, 2, 1
    ],
    
    "Marks": [
        85, 40, 72, 30, 90,
        55, 67, 48, 77, 82,
        60, 35, 88, 91, 53,
        46, 69, 74, 28, 80
    ],
    
    "Attendance": [
        90, 60, 75, 50, 95,
        80, 85, 65, 78, 92,
        70, 55, 88, 96, 73,
        60, 82, 77, 45, 89
    ]
}

df = pd.DataFrame(data)
df.index = range(1, len(df)+1)

# Result & Grade
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 80 else
              "B" if x >= 60 else
              "C" if x >= 40 else
              "Fail"
)

print("\n📊 Full Dataset:")
print(df)

# Averages
print("\n📈 Averages:")
print("Average Marks:", round(df["Marks"].mean(), 2))
print("Average Attendance:", round(df["Attendance"].mean(), 2))

# Top 3
top3 = df.sort_values(by="Marks", ascending=False).head(3)
top3["Rank"] = range(1, len(top3)+1)
top3 = top3.reset_index(drop=True)
top3.index = range(1, len(top3)+1)

print("\n🏆 Top Three Students:")
print(top3[["Rank", "Name", "Marks", "Grade", "Department"]])
print(f"\nTopper is {top3.iloc[0]['Name']} with {top3.iloc[0]['Marks']} marks")

# Department average
dep = df.groupby("Department")["Marks"].mean().round(2)
print("\n📊 Department-wise Average:")
print(dep.to_string())

# Failed
print("\n❌ Failed Students:")
print(df[df["Marks"] < 40])

# Low attendance
print("\n⚠️ Low Attendance Students:")
print(df[df["Attendance"] < 70])

# Risk
print("\n🚨 Risk Students:")
print(df[(df["Marks"] < 40) & (df["Attendance"] < 70)])


# 1. Calculate Department Averages
dep_avg = df.groupby("Department")["Marks"].mean().sort_values()

# 2. Create the Plot
plt.figure(figsize=(8, 5))
dep_avg.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])

# 3. Add Labels and Style
plt.title('Average Marks by Department', fontsize=14)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Average Marks', fontsize=12)
plt.xticks(rotation=0) # Keeps department names horizontal
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. Show the result
plt.show()
