import os
import sys
from robobrowser import RoboBrowser

AMAZON_EMAIL = os.environ['AMAZON_EMAIL']
AMAZON_PASSWORD = os.environ['AMAZON_PASSWORD']

browser = RoboBrowser(
    parser='html.parser',
    user_agent='Mozilla/ 5. 0 (Macintosh; Intel Mac OS X 10. 10; rv: 45. 0) Gecko/ 20100101 Firefox/ 45. 0'
)

def main():
    print('Nabigating...', file=sys.stderr)
    browser.open('https://www.amazon.co.jp/gp/css/order-history')
    assert 'Amazonログイン' in browser.parsed.title.string

    name = 'signIn'
    form = browser.get_form(attrs={'name':'signIn'})
    form['email'] = AMAZON_EMAIL
    form['password'] = AMAZON_PASSWORD

    print('Signing in', file=sys.stderr)
    browser.submit_form(form, headers={
        'Referer': browser.url,
        'Accept-Language':'ja,en-US;q=0.7,en;q=0.3'
    })

    # print(browser.parsed.prettify())

    while True:
        assert '注文履歴' in browser.parsed.title.string
        print_order_history()
        link_to_next = browser.get_link('次へ')

        if not link_to_next:
            break

        print('Follow link to next page...', file=sys.stderr)
        browser.follow_link(link_to_next)


def print_order_history():
    for line_item in browser.select('.order-info'):
        order = {}
        for column in line_item.select('.a-column'):
            label_ele = column.select_one('.label')
            val_ele = column.select_one('.value')

            if label_ele and val_ele:
                label = label_ele.get_text().strip()
                val   = val_ele.get_text().strip()
                order[label] = val
        print(order['注文日'], order['合計'])


if __name__ == '__main__':
    main()
