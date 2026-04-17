over_3 = lambda x: x * 3
print(over_3(3))

if_longer = lambda x: len(x) > 5
print(if_longer("Пупочок"))
print(if_longer("Кіт"))

words = ["Python", "Go", "JavaScript", "Rust", "Java"]
sorted_words = sorted(words, key=lambda u: len(u))
print(sorted_words)

len_words = list(map(lambda x: len(x), sorted_words))
print(len_words)

filter_words = list(filter(lambda x: len(x) > 4, sorted_words))
print(filter_words)