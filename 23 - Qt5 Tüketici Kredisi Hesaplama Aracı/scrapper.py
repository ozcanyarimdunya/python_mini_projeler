import os
import requests

base_url = "https://www.hesapkurdu.com"

product_types = {
    "ihtiyac": 2,
    "konut": 1,
    "tasit": 3,
    "kobi": 16
}


def get_icon_path(name):
    icon_dir = 'icons'
    if not os.path.isdir(icon_dir):
        os.mkdir(icon_dir)

    return os.path.join(icon_dir, name + '.png')


def get_logo(bank_id):
    url = base_url + "/assets/img/bank/m-{}.png".format(bank_id)
    icon_path = get_icon_path(bank_id)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(icon_path, 'wb') as fp:
            for chunk in response:
                fp.write(chunk)
        return icon_path


def get_data(amount, maturity, product_type):
    url = base_url + "/Calculator/GetProductList"
    payload = {
        "loanAmount": amount,
        "maturity": maturity,
        "productLineTypes": product_types[product_type],
    }
    response = requests.post(url, payload)

    if response.status_code != 200:
        return list()

    data = response.json()

    data = list(map(lambda item: {**item, "logo": get_logo(str(item.get('BankId')))}, data))
    return data

