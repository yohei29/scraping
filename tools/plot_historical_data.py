from datetime import datetime

import pandas as pd
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['font.sans-serif'] = 'Hiragino Kaku Gothic Pro, MigMix 1P'
import matplotlib.pyplot as plt

EX_CSV = '../../../datas/nichigin.csv'
JGBC_CSV = '../../../datas/jgbcm_all.csv'
JOBS_XLS = '../../../datas/job_offer.xls'


def main():
    df_exchange = pd.read_csv(
        EX_CSV,encoding='shift-jis', header=1,names=['date', 'USD', 'rate'],
        skipinitialspace=True, index_col=0, parse_dates=True
    )

    df_jgbcm = pd.read_csv(
        JGBC_CSV, encoding='shift-jis', header=1, index_col=0,
        parse_dates=True, date_parser=parse_jp_date, na_values=['-']
    )

    df_jobs = pd.read_excel(
        JOBS_XLS, skiprows=3, skip_footer=2, parse_cols='W,Y:AJ', index_col=0
    )
    s_jobs = df_jobs.stack()
    s_jobs.index =  [parse_year_and_month(y,m) for y,m in s_jobs.index]

    min_date = datetime(1973, 1, 1)
    max_date = datetime.now()

    plt.subplot(3,1,1)
    plt.plot(df_exchange.index, df_exchange.USD, label='Dollar yen')
    plt.xlim(min_date, max_date)
    plt.ylim(50, 250)
    plt.legend(loc='best')
    plt.subplot(3,1,2)
    plt.plot(df_jgbcm.index, df_jgbcm['1年'], label='1 year government bond interest rate')
    plt.plot(df_jgbcm.index, df_jgbcm['5年'], label='5 year government bond interest rate')
    plt.plot(df_jgbcm.index, df_jgbcm['10年'], label='10 year government bond interest rate')

    plt.xlim(min_date, max_date)
    plt.legend(loc='best')
    plt.subplot(3,1,3)
    plt.plot(s_jobs.index, s_jobs, label='Effective job openings ratio (season)')

    plt.xlim(min_date, max_date)
    plt.ylim(0.0, 2.0)
    plt.axhline(y=1, color='gray')
    plt.legend(loc='best')

    plt.savefig('historical_data.png', dpi=300)

def parse_jp_date(s):
  # Hxx.x.xx 形式の日付フォーマット変換
  b_years = {'S':1925, 'H':1988}
  era = s[0]
  year, month, day = s[1:].split('.')
  year = b_years[era] + int(year)
  return datetime(year, int(month), int(day))

def parse_year_and_month(y, m):
    year  = int(y[:-1])
    month = int(m[:-1])
    year += (1900 if year >= 63 else 2000)
    return datetime(year, month, 1)

if __name__ == '__main__':
    main()