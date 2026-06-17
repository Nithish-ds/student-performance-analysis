import pandas as pd
import matplotlib.pyplot as plt

def load_data():

    df = pd.read_csv("100_students.csv")

    return df

def semester_student_bar_chart(df):

    semester_count = df["Semester"].value_counts().sort_index()

    plt.figure(figsize=(8,5))

    bars = plt.bar(semester_count.index, semester_count.values, color="cyan", 
                   edgecolor="black", linewidth=2, width=0.5)

    plt.title("Students in Each Semester")
    plt.xlabel("Semester")
    plt.ylabel("Number of Students")

    for bar in bars:
        plt.text(bar.get_x()+bar.get_width()/2, bar.get_height(), str(int(bar.get_height())),
                  ha="center", va="bottom")

    plt.grid(True,alpha=0.3)

    plt.tight_layout()
    plt.show()

def cgpa_distribution_histogram(df):

    plt.figure(figsize=(8,5))

    plt.hist(df["CGPA"], bins=8, color="lime", edgecolor="black", linewidth=2)

    plt.title("CGPA Distribution")
    plt.xlabel("CGPA")
    plt.ylabel("Number of Students")
    plt.grid(True,alpha=0.3)

    plt.tight_layout()
    plt.show()

def attendance_cgpa_scatter(df):

    plt.figure(figsize=(8,5))

    attendance = df["Attendance"]
    cgpa = df["CGPA"]

    plt.scatter(attendance,cgpa,s=50,color="deepskyblue",edgecolor="black",alpha=0.8)
    plt.title("ATTENDANCE VS CGPA")
    plt.xlabel("Attendance")
    plt.ylabel("CGPA")
    plt.grid(True,alpha=1)

    plt.tight_layout()
    plt.show()

def semester_student_pie_chart(df):

    semester_count = df["Semester"].value_counts().sort_index()

    plt.figure(figsize=(8,5))
    plt.pie(semester_count.values,labels=semester_count.index,autopct="%1.1f%%",startangle=90,
            colors=["cyan","lime","orange","violet","gold","deepskyblue"])
    plt.title("Semester Wise Student Distribution")

    plt.tight_layout()
    plt.show()

def main():

    df = load_data()

    semester_student_bar_chart(df)

    cgpa_distribution_histogram(df)

    attendance_cgpa_scatter(df)

    semester_student_pie_chart(df)

main()