# 1. Візьми рядок "  hello, python world!  "
text = "  hello, python world!  "
# 2. Прибери пробіли з країв
text = text.strip()
print(text)
# 3. Зроби кожне слово з великої літери
print(text.title())
# 4. Заміни "python" на "amazing python"
print(text.replace("python", "amazing python"))
# 5. Виведи довжину результату
print(len(text))
# 6. Виведи перший і останній символ
print(f"{text[0]} і {text[-1]}")
# 7. Виведи рядок у зворотньому порядку
print(f"{text[::-1]}")
# 8. Розбий рядок на список слів
print(text.split())