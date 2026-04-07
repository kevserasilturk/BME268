from llama_cpp import Llama

model = Llama(
    model_path="C:/Users/Kevser/Downloads/BME268/models/model.gguf"
)


# 1. Topic al
topic = input("Enter a topic: ")

# 2. Quiz üret
response = model.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": (
                "Generate a multiple choice question with 4 options (A, B, C, D). "
                "State the correct answer at the end as 'Answer: X'."
            )
        },
        {
            "role": "user",
            "content": topic
        }
    ],
    max_tokens=256,
    temperature=0.7
)

quiz_text = response["choices"][0]["message"]["content"]
print("\n" + quiz_text)

# 3. Kullanıcı cevabı
user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

# 4. Doğru cevabı bul
correct = None

for line in quiz_text.split("\n"):
    if "Answer:" in line:
        correct = line.split("Answer:")[-1].strip()[0].upper()
        break

# 5. Kontrol
if correct and user_answer == correct:
    print("Correct!")
else:
    print(f"Wrong! The correct answer was {correct}.")