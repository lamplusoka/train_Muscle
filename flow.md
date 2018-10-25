
## シーケンシャル図

```mermaid
sequenceDiagram
Browser ->> API: Request to API header
API ->> Browser: 200 OK
Browser ->> API: Request to API data
Note right of API:Load data from DB
API ->> Browser: Send text data
```

## フロー図

```mermaid
graph TD

```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMwODg4MDkzOSwtMTk5OTIzNTEwXX0=
-->