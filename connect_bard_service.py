from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID": "",
    "__Secure-1PSIDTS": "",
    "__Secure-1PSIDCC": "",
}

bard = BardCookies(cookie_dict=cookie_dict)


def chatBard(mesaj):
    cevap = bard.get_answer(mesaj)["content"]
    return cevap
