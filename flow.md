
## シーケンシャル図

```mermaid
sequenceDiagram
User->> APP: $ train 前側
APP ->> DB: check User data
Note right of DB: F
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

```mermaid
graph TD
Start[起動] -- load data -->DB((データーベース))
A[ユーザーA] -- 割り込み --> DB
DB --> IF1{日付がN以上?}
IF1-- Yes --> OK[正解]
IF1-- No --> NG[不正解]
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzMxMzA5NjcyLC0zMDg4ODA5MzksLTE5OT
kyMzUxMF19
-->