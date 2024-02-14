final_score = 0.0
sum_score = 0.0
for i in range(20):
    subject, score, grade = map(str, input().split())
    if grade != "P":
        sum_score += float(score)
        if grade == "A+":
            final_score += float(score)*4.5
        elif grade == "A0":
            final_score += float(score)*4.0
        elif grade == "B+":
            final_score += float(score)*3.5
        elif grade == "B0":
            final_score += float(score)*3.0
        elif grade == "C+":
            final_score += float(score)*2.5
        elif grade == "C0":
            final_score += float(score)*2.0
        elif grade == "D+":
            final_score += float(score)*1.5
        elif grade == "D0":
            final_score += float(score)*1.0
final_score = final_score / sum_score
print(final_score)