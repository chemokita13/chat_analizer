import unicodedata
import json

def analyze_chat(chat_string):
    purelines = chat_string.split("\n")

    dates = []
    msgs = []
    lines = []

    for line in purelines:
        if "end-to-end" not in line and len(line) > 0:
            if (len(line)>=3) and (line[1] == "/" or line[2] == "/") and line[0] in "0123456789":
                lines.append(line)
            else:
                lines[-1] = lines[-1] + line
    for line in lines:
        if len(line.split(" - ")) > 1:
            k = line.split(" - ")
            dates.append(k[0])
            msgs.append("".join(k[1:]))

    days = []
    hours = []
    for date in dates:
        days.append(date.split(", ")[0])
        hours.append(date.split(", ")[1])

    moreUsedDay = max(set(days), key = days.count)
    moreUsedHour = max(set(hours), key = hours.count)

    # days len without duplicates
    days = list(set(days))

    words = []
    for msg in msgs:
        words.extend("".join(msg.split(": ")[1:]).split(" "))

    words = [unicodedata.normalize('NFKD', word.lower()).encode('ASCII', 'ignore').decode('utf-8') for word in words]

    wordsToCount = []
    for word in words:
        if len(word)>=5 and "<" not in word and ">" not in word:
            wordsToCount.append(word)

    fiveMoreUsedWords = []
    for i in range(5):
        fiveMoreUsedWords.append(max(set(wordsToCount), key = wordsToCount.count))
        wordsToCount = list(filter(lambda a: a != fiveMoreUsedWords[-1], wordsToCount))

    user1 = msgs[0].split(": ")[0]
    user1words = []
    user1moreUsedWord = ""
    user2 = ""
    user2words = []
    user2moreUsedWord = ""

    for msg in msgs:
        if user2 == "" and user1 not in msg:
            user2 = msg.split(": ")[0]

    for msg in msgs:
        if "<" in msg or ">" in msg:
            continue
        if user1 in msg:
            user1words.extend("".join(msg.split(": ")[1:]).split(" "))
        if user2 in msg:
            user2words.extend("".join(msg.split(": ")[1:]).split(" "))

    user1words = [unicodedata.normalize('NFKD', word.lower()).encode('ASCII', 'ignore').decode('utf-8') for word in user1words]
    user2words = [unicodedata.normalize('NFKD', word.lower()).encode('ASCII', 'ignore').decode('utf-8') for word in user2words]

    user1wordsToCount = []
    for word in user1words:
        if len(word)>=5 and "<" not in word and ">" not in word:
            user1wordsToCount.append(word)
    user2wordsToCount = []
    for word in user2words:
        if len(word)>=5 and "<" not in word and ">" not in word:
            user2wordsToCount.append(word)

    user1moreUsedWords = []
    user2moreUsedWords = []
    for i in range(5):
        user1moreUsedWords.append(max(set(user1wordsToCount), key = user1wordsToCount.count))
        user1wordsToCount = list(filter(lambda a: a != user1moreUsedWords[-1], user1wordsToCount))
        user2moreUsedWords.append(max(set(user2wordsToCount), key = user2wordsToCount.count))
        user2wordsToCount = list(filter(lambda a: a != user2moreUsedWords[-1], user2wordsToCount))

    returner = {
        "msgsNumber": len(msgs),
        "daysNumber": len(days),
        "moreUsedDay": moreUsedDay,
        "moreUsedHour": moreUsedHour,
        "wordsNumber": len(words),
        "fiveMoreUsedWords": fiveMoreUsedWords,
        "user1": user1,
        "user2": user2,
        "user1moreUsedWords": user1moreUsedWords,
        "user2moreUsedWords": user2moreUsedWords,
        "user2words": len(user2words),
        "user1words": len(user1words)
    }

    return returner

def get_chat():
    # read the chat file
    with open("chat3.txt", "r", encoding="utf-8") as file:
        chat = file.read()
        return chat

# chat_string = get_chat()
# result = analyze_chat(chat_string)
# print(json.dumps(result, indent=4))
