from difflib import get_close_matches


def get_best_match(user_question: str, questions: dict):
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match = get_best_match(user_input.lower(), knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
            if user_input == 'bye':
                break
        else:
            print('Bot I do not understand...')


if __name__ == '__main__':
    brain: dict = {'hello': 'Hey there!', 'how are you': 'I am good, thanks!',
                   'bye': 'See you!',
                   'what time is it': 'Don\'t know, don\'t care...'}

    chat_bot(brain)