from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID": "",
    "__Secure-1PSIDTS": "",
    "__Secure-1PSIDCC": "",
}

sairus = BardCookies(cookie_dict=cookie_dict)


def chatSairus(mesaj):
    cevap = sairus.get_answer(mesaj)["content"]
    return cevap
