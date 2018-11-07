#!/usr/bin/python3

import sys
import datetime
import json #前回ファイルの読み込み
import lib.functions as libf
import os #jsonファイルの有無を確認

# ---------------------------------------------------------------------------
#  settings
# ---------------------------------------------------------------------------

args            = sys.argv #引数受け取り
name_file_json  = 'output.json'
path_file_json  = "./" + name_file_json
isCommitInitial = False

# ---------------------------------------------------------------------------
#  main
# ---------------------------------------------------------------------------

libf.exit_if_invalid_args(args)
time_next = libf.get_time_next(args[2])

if os.path.exists(path_file_json) == False:
    libf.create_json_if_not_exist(args)
    isCommitInitial = True


# 保存データ内の日付より前の日付が入力された場合、メッセージを出す
# ファイルが空の場合は、ダミーのデータを保存 or 読み込みせず data_json にダミーを与える

# 保存データの読み込み
data_json = libf.read_file_json(name_file_json)

#前回実施日をメッセージ出力
if not isCommitInitial :
    libf.print_msg_last(data_json['日付'], data_json['部位'])

#次回実施部位と時間の取得
data_json['部位'] = libf.get_name_muscle_next(args[1])
#time_next = libf.get_time_next(args[2])

#次回実施日をメッセージ出力
libf.print_msg_next(time_next, data_json['部位'])

#今回の部位と日付をjsonファイルへ保存
data_to_save = {'部位': args[1], '日付': args[2] }
result = libf.write_file(name_file_json, data_to_save)
