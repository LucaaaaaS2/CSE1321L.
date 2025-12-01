def get_scores():
    try:
        n = int(input("Enter number of students: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return get_scores()

    scores = []
    for i in range(n):
        while True:
            try:
                score = int(input(f"Enter score for student {i + 1}: "))
                scores.append(score)
                break
            except ValueError:
                print("Error: Please enter a valid integer score.")
    return scores


def analyze_scores(scores):
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    passed = sum(1 for s in scores if s >= 60)
    failed = sum(1 for s in scores if s < 60)
    return highest, lowest, average, passed, failed


def display_results(high, low, avg, passed, failed):
    print("--- Score Report ---")
    print(f"Highest score: {high}")
    print(f"Lowest score: {low}")
    print(f"Average score: {avg}")
    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")


def main():
    scores = get_scores()
    high, low, avg, passed, failed = analyze_scores(scores)
    display_results(high, low, avg, passed, failed)


if __name__ == "__main__":
    main()