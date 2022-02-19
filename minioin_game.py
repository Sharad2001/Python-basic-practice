def minion_game(string):
    vowels = "AEIOU"
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print("Draw")
    if Stuart_score > Kevin_score:
        print(f"Stuart {Stuart_score}")
    if Stuart_score < Kevin_score:
        print(f"Kevin {Kevin_score}")

if __name__ == '__main__':
    s = input("Enter the word: ")
    a = s.upper()
    minion_game(a)