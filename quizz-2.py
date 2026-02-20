def ask_question(question_text, correct_answer, lives):
    while lives > 0:
        answer = input(question_text + " ")

        if answer.lower() == correct_answer.lower():
            print("Bonne réponse !\n")
            return lives

        lives -= 1
        print(f"Dommage ! Il te reste {lives} chances")

        if lives == 0:
            print("Oh non ! Tu as perdu le jeu...")
            return 0


def run_quiz():
    lives = 3
    print("Voici notre quiz, tu as trois chances !\n")

    questions = [
        ("Combien de fois la France a gagné la coupe du monde ?", "2"),
        ("Quand a été fondé Apple ?", "1976"),
        ("Qui a fondé SpaceX ?", "elon musk"),
    ]

    for question, answer in questions:
        lives = ask_question(question, answer, lives)
        if lives == 0:
            return

    print("Bravo ! Tu as gagné le quiz !")


if __name__ == "__main__":
    run_quiz()
