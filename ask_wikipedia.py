import wikipedia
from space import space
import textwrap
from voice import say

def checkEcodeRun(ecode, subject):
    if ecode:
        say("I could not find any information on this topic.")
    else:
        print("Source: Wikipedia")
        say("Information on " + subject + " brought to you by wikipedia.")


def do_wiki(input1s, sword):
    term = get_term(input1s, sword)
    term = get_ask_term()
    ecode = ask_wiki(term)
    checkEcodeRun(ecode, term)
    print("==============================")
    print(term)
    print("==============================")
    print("Overview")
    space(1)
    summary = get_tSummary()
    print(summary)
    brief = get_sSumarry()
    say(brief)
    space(2)
    print(term)
    print_content(term)


def get_term(input1s, sword):
    s_info = input1s.split(sword + " ")
    global ask_term
    ask_term = s_info[-1]
    ask_wiki(ask_term)


def ask_wiki(thing, lang="en"):
    global whole
    global main
    try:
        wikipedia.set_lang(lang)
    except:
        print("No such language found")
        wikipedia.set_lang("en")

    try:
        whole = wikipedia.summary(thing)
        main = whole.split(". ")
    except:
        global error
        error = True


def get_tSummary():
    tsummary = '\n'.join(textwrap.wrap(whole, width=120, replace_whitespace=False))
    return  tsummary


def get_sSumarry():
    sSumarry = main[0]
    return  sSumarry


def print_content(thing):
    subject = wikipedia.page(thing)
    print(subject.content)


def take_error_code():
    return error


def get_ask_term():
    return ask_term


