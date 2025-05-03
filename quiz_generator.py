def generate_quiz(difficulty: str, num_questions: int = 5) -> list:
    """
    Returns a list of dicts:
    [
        {
            "question": "What color is the sun? ☀️",
            "options": ["Blue", "Yellow", "Green", "Red"],
            "answer_idx": 1
        },
        ...
    ]
    """
    if difficulty == "Easy":
        return [
            {
                "question": "What is special about this book? 📚👀",
                "options": [
                    "It has no pictures! 😔",
                    "Anyone can read it for free! 🎉",
                    "You need to buy it to own it! 💸",
                    "It's only for kids in the United States! 🇺🇸"
                ],
                "answer_idx": 1
            },
            {
                "question": "📖 What do you need to do before reading an eBook? 🤔",
                "options": [
                    "Just start reading it anywhere!",
                    "Use headphones and a flashlight!",
                    "Ask your friend if they want to read it with you!",
                    "Make some popcorn and grab a snack!"
                ],
                "answer_idx": 1
            },
            {
                "question": "What are the names of the four little Rabbits mentioned in the story? 🐰🏠",
                "options": [
                    "Benny, Billy, Bob, and Barbara",
                    "Flopsy, Mopsy, Cotton-tail, and Peter",
                    "Rosie, Ruby, Rusty, and Rex",
                    "Sammy, Sally, Sasha, and Squeaky"
                ],
                "answer_idx": 1
            },
            {
                "question": "What did old Mrs. Rabbit take with her when she went to the baker's? 🎁",
                "options": [
                    "Her favorite hat and a book 📖",
                    "A basket and an umbrella ☔️",
                    "A bag of carrots and some seeds 🥕",
                    "Her slippers and a blanket 😴"
                ],
                "answer_idx": 1
            }
        ]
    elif difficulty == "Medium":
        return [
            {
                "question": "What is special about this book? 📖👀",
                "options": [
                    "It's only for kids in the United States. 🇺🇸",
                    "You can copy it and share it with friends! 📨👫",
                    "It's a story about a rabbit who gets into trouble. 🐰😳",
                    "It's written by a famous author, J.K. Rowling. ✨📚"
                ],
                "answer_idx": 1
            },
            {
                "question": "📖 What do you need to do before using this eBook? 🤔",
                "options": [
                    "Just open it and start reading! 📚",
                    "Ask your teacher for permission first 👩‍🏫",
                    "Make sure you have a big smile on your face 😊",
                    "Use the special code provided by the publisher to unlock it 🔑"
                ],
                "answer_idx": 3
            }
        ]
    else:  # Hard
        return [
            {
                "question": "🐰 Who is the main character in this story? 🤔",
                "options": [
                    "Mr. McGregor",
                    "Benjamin Bunny",
                    "Peter Rabbit",
                    "Old Man Jenkins"
                ],
                "answer_idx": 2
            },
            {
                "question": "What do you need to do before using this eBook? 📖👀",
                "options": [
                    "Tap your feet three times 🔴",
                    "Hold it upside down 💥",
                    "Scroll through it carefully  👀",
                    "Read it from back to front 📚"
                ],
                "answer_idx": 2
            },
            {
                "question": "What are the names of the four little Rabbits in the story? 🐰🌿",
                "options": [
                    "Benny, Sammy, and two others",
                    "Flopsy, Mopsy, Cotton-tail, and Peter",
                    "Rosie, Lily, and two brothers",
                    "Timmy, Tommy, and two sisters"
                ],
                "answer_idx": 1
            }
        ] 