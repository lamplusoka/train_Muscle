
## シーケンシャル図

```mermaid
sequenceDiagram
User->> APP: $ train 前側
APP ->> DB: check User data
Note right of DB: FlowA
Note right of DB:User情報から<br>データ検索=なし
Note right of DB:DBの新規作成<br>前側を保存
DB ->> APP: No data
Note right of APP:初回なので Msg=<br>「頑張りましょう」
APP ->> User: return Msg
Note right of APP: Exit(0) 正常終了
APP -->>User: Status=Exit
User ->> APP: $ train 下半身
APP ->> DB: check User data
Note right of DB:User情報から<br>データ検索=あり
DB ->> APP: 外側
Note right of APP:２回目なので Msg=<br>「明日は後側」
APP -->> User: return Msg
Note right of APP: Exit(0) 正常終了
APP -->>User: Status=Exit
```

## フロー図

引数を返す（表示するだけのもの）
// 引数を確認
// 引数を表示
// 終了

def sample( user_data ) のフロー図

```mermaid
graph TD
Start[input user data] -- user_data --> LoadData{Get old data<br>and mix}
DB((DB)) -- Request old_data --> LoadData
LoadData -- user_data and old_data --> IF1{Is old > current?}
IF1-- Yes --> OK[正解]
IF1-- No --> NG[不正解]
OK --> End[戻り値]
NG --> End
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3Mjc0MjY0MDMsMTUzNzYzMDYzNiwtNz
I2NDU5NjA1LC0zMDg4ODA5MzksLTE5OTkyMzUxMF19
-->