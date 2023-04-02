def correct_points(text):
    correct_1 = 'пунктывыдачи'
    correct_2 = 'пунктывыдачиввурнарах'
    correct_3 = 'пунктывыдачивчебоксарах'
    correct_4 = 'пункты'
    correct_5 = 'пунктывурнары'
    correct_6 = 'пунктычебоксары'
    text = text.lower().replace(' ', '')
    if text == correct_1 or text == correct_4:
        return ('Пункты выдачи', True)
    elif text == correct_2 or text == correct_5:
        return ('Пункты выдачи в Вурнарах', True)
    elif text == correct_3 or text == correct_6:
        return ('Пункты выдачи в Чебоксарах', True)
    elif correct_help(correct_3, text) or correct_help(correct_6, text):
        return ('Пункты выдачи в Чебоксарах', False)
    elif correct_help(correct_2, text) or correct_help(correct_5, text):
        return ('Пункты выдачи в Вурнарах', False)
    elif correct_help(correct_1, text) or correct_help(correct_4, text):
        return ('Пункты выдачи', False)


def correct_help(correct_text, source_text):
    criterion_1 = False
    criterion_2 = False
    correct_text1 = list(correct_text)
    source_text1 = list(source_text)
    count1 = 0
    for i in correct_text1:
        if i in source_text1:
            count1 += 1
            del source_text1[source_text1.index(i)]
    if count1 / len(correct_text1) * 100 > 65:
        criterion_1 = True
    count2 = 0
    if len(correct_text) < len(source_text):
        for i in range(len(correct_text) - 1):
            for j in range(len(correct_text)):
                if correct_text[i:j] in source_text:
                    count2 = max(count2, len(correct_text[i:j]))
    else:
        for i in range(len(source_text) - 1):
            for j in range(i, len(source_text)):
                if source_text[i:j] in correct_text:
                    count2 = max(count2, len(source_text[i:j]))
    if count2 / len(correct_text) * 100 > 50:
        criterion_2 = True
    if criterion_1 and criterion_2:
        return True
    return False
