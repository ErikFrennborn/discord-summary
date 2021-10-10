import json
import math
import itertools
import emoji
def get_author(message):
    return(message["author"]["name"])

def get_date(message):
    return message["timestamp"].split("T")[0]

def get_time(message):
    return ':'.join(message["timestamp"].split("T")[1].split(":")[:2])

def add_if_exist(store, inc, key):
    if key not in store:
        store[key] = inc
    else:
        store[key] += inc

def is_emoji(word):
    return word in emoji.UNICODE_EMOJI

def is_link(word):
    return "http" in word

def get_words(message):
    return message["content"].strip().split()

def load_authors(data):
    authors = {}
    count = 0
    for message in data["messages"]:
        if not message["author"]["name"] in authors:
            authors[message["author"]["name"]] = count
            count +=1
    return authors

def convert_string_to_int(time):
    time_split = time.split(":")
    m = int(time_split[1])
    h = int(time_split[0])
    return h*60 + m

def convert_int_to_string(time):
    m = time%60
    h = math.floor(time/60)
    return "{}:{}".format(str(h),str(m))


def get_average(data):
    return round(sum(data)/len(data))

def word_analys_user(data, authors):
    words = {}
    for message in data:
        content_words = get_words(message)
        author = get_author(message)
        for word in content_words:
            if word not in words:
                if is_emoji(word):
                    continue
                if is_link(word):
                    continue
                words[word] = [0 for _ in range(len(authors))]

            words[word][authors[author]] +=1

    def sort_func(x):
        if x[0] == 0:
            return -x[1]
        elif x[1] == 0:
            return x[0]
        else:
            return (x[0] - x[1])/sum(x)

    result = list(map(lambda x: (x, sort_func(words[x])),words))
    result.sort(key = lambda x:x[1])
    return (words,result)

def common_words(data):
    words = {}
    for message in data:
        content_words = get_words(message)
        for word in content_words:
            add_if_exist(words,1,word)
    result = list(map(lambda x: (x, words[x]),words))
    result.sort(key=lambda x:x[1],reverse=True)
    return (words,result)

def common_emojis(data):
    result = {}
    for message in data:
        content_words = get_words(message)
        for word in content_words:
            if is_emoji(word):
                add_if_exist(result,1,word)
    result = list(map(lambda x: (x, result[x]),result))
    result.sort(key=lambda x:x[1],reverse=True)
    return result



def average_message(data):
    average = get_average(list(map(lambda x: convert_string_to_int(get_time(x)),data)))
    return(convert_int_to_string(average))

def average_first_message(data):
    dates = {}
    for message in data:
        date = get_date(message)
        if date not in dates:
             dates[date] = convert_string_to_int(get_time(message))
    times = list(map(lambda x: dates[x],dates))
    average = get_average(times)
    return(convert_int_to_string(average))

def average_last_message(data):
    dates = {}
    data_rev = data
    data_rev.reverse()
    for message in data_rev:
        date = get_date(message)
        if date not in dates:
             dates[date] = convert_string_to_int(get_time(message))
    times = list(map(lambda x: dates[x],dates))
    average = get_average(times)
    return(convert_int_to_string(average))



def most_active_date(data):
    dates = {}
    for message in data:
        date = get_date(message)
        add_if_exist(dates,1,date)

    days = list(dates)
    days.sort(key=lambda x:dates[x],reverse=True)
    return (days[0], dates[days[0]])

def first_mover(data):
    dates = {}
    for message in data:
        date = get_date(message)
        if date not in  dates:
            dates[date] = get_author(message)
    result = {}
    for date in dates:
        author = dates[date]
        add_if_exist(result,1,author)
    return result

def number_of_message(data):
    result= {}
    for message in data:
        author = get_author(message)
        add_if_exist(result,1,author)
    return result

def number_of_words(data):
    result= {}
    for message in data:
        author = get_author(message)
        number_of_words = len(list(filter(lambda x: not(is_link(x) or is_emoji(x)),message["content"].strip().split())))
        add_if_exist(result,number_of_words,author)
    return result

def number_of_links(data):
    result= {}
    for message in data:
        author = get_author(message)
        content_word = message["content"].strip().split()
        for word in content_word:
            if is_link(word):
                add_if_exist(result,1,author)
    return result

def number_of_attachements(data):
    result = {}
    for message in data:
        size = len(message["attachments"])
        author = get_author(message)
        add_if_exist(result,size,author)

    return result

def number_of_edits(data):
    result = {}
    for message in data:
        if message["timestampEdited"] != None:
            author = get_author(message)
            add_if_exist(result,1,author)
    return result


def number_of_unique_words(words,authors):
    result = {}
    authors = list(authors)
    for author in authors:
        result[author] = 0
    for word in words:
        for i in range(len(authors)):
            if words[word][i] > 0:
                result[authors[i]] += 1

    return result

def number_of_letters(words,authors):
    result = {}
    authors = list(authors)
    for author in authors:
        result[author] = 0
    for word in words:
        word_length = len(word)
        for i in range(len(authors)):
            if words[word][i] > 0:
                result[authors[i]] += word_length * words[word][i]

    return result


def total_number_of_message(data):
    return data["messageCount"]

def print_sort_tuple(data):
    data_list=list(map(lambda x:(x,data[x]),data))
    total = sum(list(map(lambda x:x[1],data_list)))
    data_list.sort(key = lambda x: x[1], reverse = True)
    data_list=list(map(lambda x:(x[0],(x[1],round(100*x[1]/total)) if total != 0 else "N/A" ),data_list))
    for row in data_list:
        print("{} {}% ({})".format(row[0],row[1][1],row[1][0]))
    print("")


def get_n_closest(data, n, around):
    data.sort(key=lambda x: abs(x[1]-around))
    result = []
    for row in data:
        result.append(row)
        if len(result) == n:
            return result

def print_table(header,data):
    col_width = []
    data = list(map(list, itertools.zip_longest(*data, fillvalue=None)))
    data.insert(0,header)
    combine = data
    combine = list(map(list, itertools.zip_longest(*combine, fillvalue=None)))
    for xs in combine:
        col_width.append(max(list(map(lambda x:len(x),xs))))

    line_string = "|"
    for cols in col_width:
        line_string += "-"*(cols+2) + "|"

    print(line_string)
    for i in range(len(combine)):
        row_string = "|"
        for j in range(len(combine)):
            space = " "*(col_width[j] - len(combine[j][i]))
            if not is_emoji(combine[j][i]):
                space += " "
            row_string += " " + str(combine[j][i]) + space + "|"
        print(row_string)
        if i == len(combine)-1:
            line_string ="|"
            for cols in col_width:
                line_string += "_"*(cols+2) + "|"
            print(line_string)
        else:
            print(line_string)


def print_data():
    with open('data.json', 'r') as json_file:
        data = json.loads(json_file.read())
    authors = load_authors(data)

    print("Total number of messages: {}".format(str(total_number_of_message(data))))
    messages = data["messages"]
    print("")
    (words, result) = word_analys_user(messages,authors)


    print("Number of messages:")
    print_sort_tuple(number_of_message(messages))

    result_of_words = number_of_words(messages)
    print("Number of words:")
    print_sort_tuple(result_of_words)

    print("Number of links:")
    print_sort_tuple(number_of_links(messages))

    print("Number of edits:")
    print_sort_tuple(number_of_edits(messages))

    print("Number of attachments:")
    print_sort_tuple(number_of_attachements(messages))

    print("Number of unique words:")
    print_sort_tuple(number_of_unique_words(words, authors))

    print("Number of letters:")
    result_of_letters = number_of_letters(words, authors)
    print_sort_tuple(result_of_letters)

    print("Average words length:")
    for key in result_of_letters:
        print("{} {} letter/word".format(key, round(result_of_letters[key]/result_of_words[key],2)\
                if result_of_words[key] != 0 else "N/A"))
    print("")

    print("First mover (first message per day)")
    print_sort_tuple(first_mover(messages))

    print("Most active date {} with {} messages\n".format(*most_active_date(messages)))
    print("Average first message time {}\n".format(average_first_message(messages)))
    print("Average message time {}\n".format(average_message(messages)))

    if len(authors.keys()) == 2:
        print("Words spread, who uses what words most:")
        targets = [result[-1][1], 0.9, 0.5, 0.2, 0.0, -0.2, -0.5,-0.9, result[0][1]]
        word_speard = list(map(lambda x: list(map(lambda y: y[0], get_n_closest(result,10, x))),targets))
        header = []
        for target in targets:
            if target >= 1:
                header.append(list(authors.keys())[0])
            elif target <= -1:
                header.append(list(authors.keys())[1])
            else:
                header.append(str(target))
        print_table(header, word_speard)
        print("")

    print("50 most common words:")
    print("Growing right then down")
    result = common_words(messages)[1][:50]
    row_string = ""
    for i in range(len(result)):
        if (i %10 == 0)and i != 0:
            print(row_string)
            row_string = ""
        row_string += result[i][0] + ", "
    print(row_string+ "\n")

    print("Most common emoji:")
    result = common_emojis(messages)
    total = sum(list(map(lambda x:x[1],result)))
    result = result[0:6]
    result = list(map(lambda x:(x[0],(x[1],round(100*x[1]/total))),result))
    for row in result:
        print ("{} {}% ({})".format(row[0],row[1][1], row[1][0]))
