jury = int(input())
presentation = input()
number_of_presentations = 0
total_average = 0

while presentation != "Finish":
    total_score = 0
    number_of_presentations += 1
    for number in range(1, jury + 1):
        score = float(input())
        total_score += score
    average_score = total_score / number
    total_average += average_score
    print(f"{presentation} - {average_score:.2f}.")
    presentation = input()

final_score = total_average / number_of_presentations
print(f"Student's final assessment is {final_score:.2f}.")
