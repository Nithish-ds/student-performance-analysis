import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df.index = df.index + 1
    return df

def show_data(df):
    print("\nFIRST 5 RECORDS :")
    print(df.head())

def check_missing_values(df):
    print("\nMISSING VALUES :")

    missing = df.isnull().sum()

    for column, value in missing.items():
        print(f"{column}: {value}")

def check_duplicates(df):
    print("\nDUPLICATE RECORDS :")
    print(df.duplicated().sum())

def average_cgpa(df):
    avg = df["CGPA"].mean()

    print("\nAVERAGE CGPA OF THE DEPARTMENT :")
    print(round(avg, 2))

def highest_cgpa_student(df):
    max_cgpa = df["CGPA"].max()

    print("\nHIGHEST CGPA STUDENT DETAILS :")
    print(df[df["CGPA"] == max_cgpa].to_string(index=False))

def lowest_cgpa_student(df):
    min_cgpa = df["CGPA"].min()

    print("\nLOWEST CGPA STUDENT DETAILS :")
    print(df[df["CGPA"] == min_cgpa].to_string(index=False))

def semester_wise_student_count(df):

    semester_count = (df["Semester"].value_counts().sort_index().reset_index())
    semester_count.columns = ["Semester", "Students"]

    print("\nSEMESTER WISE STUDENT COUNT :")
    print(semester_count.to_string(index=False))

def semester_wise_average_cgpa(df):

    semester_avg = (df.groupby("Semester")["CGPA"].mean().round(2).reset_index())
    semester_avg.columns = ["Semester", "Average CGPA"]

    print("\nSEMESTER WISE AVERAGE CGPA :")
    print(semester_avg.to_string(index=False))

def attendance_wise_cgpa(df):

    df["Attendance Group"] = pd.cut(df["Attendance"],bins=[60,70,80,90,100],
                                    labels=["60-70","70-80","80-90","90-100"])
    
    attendance_cgpa = (df.groupby("Attendance Group")["CGPA"].mean().round(2).reset_index())
    attendance_cgpa.columns = ["Attendance","CGPA"]

    print("\nATTENDANCE WISE AVERAGE CGPA :")
    print(attendance_cgpa.to_string(index=False))


def cgpa_statistics(df):

    stats = df["CGPA"].describe().round(2)
    
    print("\nCGPA STATISTICS :")
    print("-" * 25)

    for index, value in stats.items():
        print(f"{index.capitalize():<10} : {value}")

def main():

    df = load_data("100_students.csv")

    show_data(df)

    check_missing_values(df)

    check_duplicates(df)

    average_cgpa(df)

    highest_cgpa_student(df)

    lowest_cgpa_student(df)

    semester_wise_student_count(df)

    semester_wise_average_cgpa(df)

    attendance_wise_cgpa(df)

    cgpa_statistics(df)

main()
