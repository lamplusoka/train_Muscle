#!/usr/bin/python3

import sys
import datetime
import json #前回ファイルの読み込み
import lib.functions
import os #jsonファイルの有無を確認

args = sys.argv #引数受け取り
name_file_json = 'output.json'
time_next = lib.functions.get_time_next(args[2])

# ---------------------------------------------------------------------------
#  main
# ---------------------------------------------------------------------------

# ToDo
# ファイルが存在するか確認。なければ作成
#path = '/mnt/c/users/lamplus/documents/github/trainning/python3/test_import/output.json'
path = './output.json'

if os.path.exists(path) == False:
    lib.functions.make_file_json_first(args[1], args[2])
    print('初めてのご利用ありがとうございます！筋トレライフ、張り切っていきましょう！')
    #初回の次回実施部位を特定
    data_first_next_muscle = lib.functions.get_name_muscle_next(args[1])
    #次回実施日をメッセージ出力
    lib.functions.print_msg_next(time_next, data_first_next_muscle)
    exit()
else:
    pass


# ファイルが空の場合は、ダミーのデータを保存 or 読み込みせず data_json にダミーを与える

# 保存データの読み込み
data_json = lib.functions.read_file_json(name_file_json)

#前回実施日をメッセージ出力
lib.functions.print_msg_last(data_json['日付'], data_json['部位'])

#次回実施部位と時間の取得
data_json['部位'] = lib.functions.get_name_muscle_next(args[1])
#time_next = lib.functions.get_time_next(args[2])

#次回実施日をメッセージ出力
lib.functions.print_msg_next(time_next, data_json['部位'])

#今回の部位と日付をjsonファイルへ保存
data_to_save = {'部位':args[1], '日付':args[2]} 
result = lib.functions.write_file_json(name_file_json, data_to_save)