# 학점계산 함수
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 학생 수와 과목 수 설정
num_students = 5
num_subjects = 3
subjects = ["영어", "C-언어", "파이썬"]

students = []
student_scores = []

# 입력 함수
def input_scores():
    student_id = input("학번: ")
    student_name = input("이름: ")
    scores = []
    print("점수를 입력하세요:")
    for subject in subjects:
        score = int(input(subject + ": "))
        scores.append(score)
    students.append([student_id, student_name, *scores])

# 총점, 평균, 학점 계산함수
def calculate():
    for scores in student_scores:
        total_score = sum(scores)
        average_score = total_score / num_subjects
        grade = calculate_grade(average_score)
        yield total_score, average_score, grade

# 등수 계산함수
def calculate_rank():
    sorted_students = sorted(enumerate(student_scores), key=lambda x: sum(x[1]), reverse=True)
    ranks = [0] * len(students)
    prev_score = sum(sorted_students[0][1]) + 1
    rank = 1
    for idx, scores in sorted_students:
        total_score = sum(scores)
        if total_score < prev_score:
            rank += 1
            prev_score = total_score
        ranks[idx] = rank
    return ranks

# 출력함수
def print_results():
    print("\t\t\t\t\t성적관리 프로그램\t\t\t\t")
    print("==================================================================")
    print("학번\t\t이름\t\t", end="")
    for subject in subjects:
        print(subject + "\t\t", end="")
    print("총점\t\t평균\t\t학점\t\t등수")
    ranks = calculate_rank()
    for idx, student in enumerate(students):
        print(student[0], student[1], end="\t")  # 학번과 이름 출력
        for score in student[2:]:  # 과목 성적 출력
            print(score, end="\t\t")
        total_score, average_score, grade = student_scores[idx]
        print(total_score, end="\t\t")
        print("{:.1f}".format(average_score), end="\t\t")
        print(grade, ranks[idx], end="\t\t\t")
        print()  # 다음 줄로 넘어감

# 삽입 함수
def insert_student():
    if len(students) < num_students:
        input_scores()
        student_scores.extend(calculate())

# 삭제 함수
def delete_student():
    student_id = input("삭제할 학생의 학번을 입력하세요: ")
    for i, student in enumerate(students):
        if student[0] == student_id:
            del students[i]
            del student_scores[i]
            break


# 탐색 함수(학번, 이름)
def search_student():
    search_key = input("찾을 학생의 학번 또는 이름을 입력하세요: ")
    for student in students:
        if search_key in student:
            print("학번:", student[0])
            print("이름:", student[1])
            for idx, score in enumerate(student[2:]):
                print(subjects[idx] + ":", score)
            break
    else:
        print("해당하는 학생이 없습니다.")

# 정렬(총점) 함수
def sort_students_by_total_score():
    global students, student_scores
    sorted_indices = sorted(range(len(student_scores)), key=lambda x: sum(student_scores[x]), reverse=True)
    students = [students[i] for i in sorted_indices]
    student_scores = [student_scores[i] for i in sorted_indices]

# 80점이상 학생 수 카운트 함수
def count_students_above_80():
    count = sum(1 for scores in student_scores if all(score >= 80 for score in scores))
    print("80점 이상을 받은 학생 수:", count)

# 메인 함수
def main():
    while True:
        print("\n1. 학생 추가\n2. 학생 삭제\n3. 학생 조회\n4. 성적 정렬\n5. 80점 이상 학생 수\n6. 성적 출력\n7. 종료")
        choice = input("원하는 작업을 선택하세요: ")
        if choice == '1':
            insert_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            sort_students_by_total_score()
        elif choice == '5':
            count_students_above_80()
        elif choice == '6':
            print_results()
        elif choice == '7':
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
