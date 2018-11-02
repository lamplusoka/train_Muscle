import sys
import datetime
import json #前回ファイルの読み込み

# ---------------------------------------------------------------------------
#  Functions
# ---------------------------------------------------------------------------
def get_name_muscle_next(name_muscle_last): #次回部位の特定
    if name_muscle_last == '前側': 
        return '下半身'
    elif name_muscle_last == '下半身':
        return '後側'
    elif name_muscle_last == '後側':
        return '前側'
    else:
        print('不正な部位です')
        exit()

def get_time_next(time_given_string):
    time_given_datetime = datetime.datetime.strptime(time_given_string, '%Y/%m/%d') #日付文字列をdatetimeへ変換
    time_add_day_one    = time_given_datetime + datetime.timedelta(days=1) #一日足す
    time_next_day       = time_add_day_one.strftime('%Y/%m/%d') #日付を文字列へ変換
    return time_next_day

def make_file_json_first(data_first_muscle, data_first_time):
    make_file_json = open('output.json', 'w')
    make_file_json.write('{"部位":"' + data_first_muscle + '", "日付": "' + data_first_time + '"}')
    make_file_json.close

def print_msg_last(date_last, name_muscle):
    print('前回は' + date_last + 'に' + name_muscle + 'を鍛えました。' )

def print_msg_next(date_next, name_muscle): 
    print('次回は'+ date_next + 'に' + name_muscle + 'をやりましょう。')


def read_file_json(path_file_json):
    file_object = open(path_file_json, 'r')
    return json.load(file_object)

def write_file_json(path_file_json, data_to_save):
    file_object  = open(path_file_json, 'w')
    return json.dump(data_to_save, file_object, ensure_ascii=False)
