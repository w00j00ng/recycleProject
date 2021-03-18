from pybo.config import homedir
import pandas as pd


fdir = homedir + '/static/schedule.csv'
df_raw = pd.read_csv(fdir, encoding='euc-kr')

regionList = df_raw['region'].unique()


def guideStr(userInput):
    df_temp = df_raw[df_raw['region'] == userInput]

    info_trash = df_temp[df_temp['class'] == 'trash']
    info_recycle = df_temp[df_temp['class'] == 'recycle']

    str_trash = f"일반쓰레기 배출일정은 {info_trash.iloc[0,2]} {info_trash.iloc[0, 3]} 입니다"
    str_recycle = f"재활용 배출일정은 {info_recycle.iloc[0,2]} {info_recycle.iloc[0, 3]} 입니다"

    return str_trash, str_recycle


def guideResult(userInput):
    df_temp = df_raw[df_raw['region'] == userInput]

    info_trash = df_temp[df_temp['class'] == 'trash']
    info_recycle = df_temp[df_temp['class'] == 'recycle']

    # 일반쓰레기 배출일정 : info_trash.iloc[0,2] 요일  info_trash.iloc[0, 3] 시
    # 재활용쓰레기 배출일정 : info_recycle.iloc[0,2] 요일  info_recycle.iloc[0, 3] 시

    return info_trash.iloc[0, 2], info_trash.iloc[0, 3], info_recycle.iloc[0, 2], info_recycle.iloc[0, 3]