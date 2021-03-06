import sys
import datetime
import json #前回ファイルの読み込み
import linecache
import ast
import re


name_muscle_part = ['前側', '下半身', '後側']
len_name_muscle_part = len(name_muscle_part)

# ---------------------------------------------------------------------------
#  Functions
# ---------------------------------------------------------------------------
def create_json_if_not_exist(args):
    make_file_json(args[0], args[1])
    print('初めてのご利用ありがとうございます！筋トレライフ、張り切っていきましょう！')

def exit_if_invalid_args(name_muscle_part_this_time_num):
    match = re.search('^[1-3]$', str(name_muscle_part_this_time_num)) #１～３の数字が入力されたか確認。リストを増やしたら正規表現も増やすこと
    if not match:
        print('1～' + str(len_name_muscle_part) + 'の数字をいれてください。')
        name_muscle_part_this_time_num = ''
        #input_muscle_part()
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
    name_muscle_part_this_time_num = input()
    exit_if_invalid_args(name_muscle_part_this_time_num)
    return name_muscle_part[int(name_muscle_part_this_time_num) - 1]

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
    #file_object = open(path_file_json, 'r')
    #return json.load(file_object)
    #path_file = 'test.txt'
    get_total_rows_num = sum(1 for i in open(path_file_json)) #テキストデータの行数を取得
    read_log_last = linecache.getline(path_file_json, get_total_rows_num - 1)
    change_log_last_to_dict = ast.literal_eval(read_log_last)
    return change_log_last_to_dict

def generate_data_json(data_first_muscle, data_first_time):
    return {"部位": data_first_muscle, "日付": data_first_time}

def write_file(path_file, data_to_save):
    #file_object = open(path_file, 'w')
    #json.dump(data_to_save, file_object, ensure_ascii=False) #元はfile_object.write(data_to_save)
    #file_object.close

    with open(path_file,'ab+') as f:
            f.seek(0, 2)
            if f.tell() == 0:
                    f.write('[\n'.encode())
                    f.write(json.dumps(data_to_save,  ensure_ascii=False).encode())
                    f.write('\n]'.encode())
            else:
                    f.seek(-2, 2)
                    f.truncate()
                    f.write(',\n'.encode())
                    f.write(json.dumps(data_to_save,  ensure_ascii=False).encode())
                    f.write('\n]'.encode())
                    f.close
        
