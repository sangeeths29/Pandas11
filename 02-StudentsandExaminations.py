# Problem 2 - Students and Examinations (https://leetcode.com/problems/students-and-examinations/ )
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_rows = students.merge(subjects, how='cross')
    groupedDf = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name = 'attended_exams')
    interDf = pd.merge(all_rows, groupedDf, on = ['student_id', 'subject_name'], how = 'left')
    interDf['attended_exams'] = interDf['attended_exams'].fillna(0)
    return interDf.sort_values(by = ['student_id', 'subject_name'])