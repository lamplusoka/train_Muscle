import sys
import datetime
import json #前回ファイルの読み込み

name_muscle_part = ['前側', '下半身', '後側']
len_name_muscle_part = len(name_muscle_part)

# ---------------------------------------------------------------------------
#  Functions
# ---------------------------------------------------------------------------
def create_json_if_not_exist(args):
    make_file_json(args[0], args[1])
    print('初めてのご利用ありがとうございます！筋トレライフ、張り切っていきましょう！')

def exit_if_invalid_args(name_muscle_part_this_time_num):
    if name_muscle_part_this_time_num >= len_name_muscle_part:
        print('1～' + str(len_name_muscle_part) + 'の数字をいれてください。')
        exit()

def get_name_muscle_next(name_muscle_last): #次回部位の特定
    num = name_muscle_part.index(name_muscle_last)
    if num % len(name_muscle_part) == len_name_muscle_part - 1:
        return name_muscle_part[0]
    else:
        return name_muscle_part[num + 1]

def get_time_next(time_given_string):
    time_given_datetime = datetime.datetime.strptime(time_given_string, '%Y/%m/%d') #日付文字列をdatetimeへ変換
    time_add_day_one    = time_given_datetime + datetime.timedelta(days=1) #一日足す
    time_next_day       = f'{time_add_day_one:%Y/%m/%d}' #time_add_day_one.strftime('%Y/%m/%d') #日付を文字列へ変換
    return time_next_day

def get_path_file_json():
    return './output.json'

def get_weekday(time_given_string):
    weekday = ['月', '火', '水', '木', '金', '土','日']
    time_given_datetime = datetime.datetime.strptime(time_given_string, '%Y/%m/%d') #日付文字列をdatetimeへ変換
    time_weekday_number = time_given_datetime.weekday() #曜日の値を取得
    time_weekday        = weekday[time_weekday_number] #曜日の値→文字列で曜日へ
    return time_weekday

def input_muscle_part(): #標準入力から部位のキーを取得
    print('どの部位を鍛えましたか？番号を入力してください。')
    num = 1
    for part in name_muscle_part:
        print(str(num) + ':' + part)
        num += 1
    name_muscle_part_this_time_num = int(input()) -1
    exit_if_invalid_args(name_muscle_part_this_time_num)
    return name_muscle_part[name_muscle_part_this_time_num]

def make_file_json(data_first_muscle, data_first_time):
    data_json      = generate_data_json(data_first_muscle, data_first_time)
    path_file_json = get_path_file_json()
    write_file(path_file_json, data_json)

def print_help():
    print("ヘルプです。")

def print_msg_last(date_last, name_muscle):
    date_weekday_last = get_weekday(date_last)
    print('前回は' + date_last + '(' + date_weekday_last + ')に' + name_muscle + 'を鍛えました。' )

def print_msg_next(date_next, name_muscle):
    date_weekday_next = get_weekday(date_next) 
    print('次回は'+ date_next + "(" + date_weekday_next + ')に' + name_muscle + 'をやりましょう。')


def read_file_json(path_file_json):
    file_object = open(path_file_json, 'r')
    return json.load(file_object)

def generate_data_json(data_first_muscle, data_first_time):
    return {"部位": data_first_muscle, "日付": data_first_time}

def write_file(path_file, data_to_save):
    file_object = open(path_file, 'w')
    json.dump(data_to_save, file_object, ensure_ascii=False) #元はfile_object.write(data_to_save)
    file_object.close
