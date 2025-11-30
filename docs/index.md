# 結算檢查表自動化部署手冊
本頁提供一鍵部署、Secrets 清單、欄位 mapping 及驗收流程，適合 PM、工程師、AI 協作維運。

## 一鍵部署步驟
1. 新增 Secrets：`NOTION_TOKEN`、`NOTION_DATABASE_ID`（必要），`GITHUB_REPO`（選用）。
2. 複製以下檔案至專案：
   - `.github/workflows/auto_sync_notionsheet.yaml`
   - `.github/workflows/generate_report.yml`
   - `scripts/notion_export_csv.py`
   - `scripts/branch_to_task.py`
3. 於 Actions 首次手動 Run workflow 完成首輪驗收。

## 欄位 mapping 一覽
| Notion 欄位名 | 類型 | 說明 | 建議命名 |
|---|---|---|---|
| Branch | title | 分支名稱 | Branch |
| CommitMsg | rich_text | Commit 訊息 | CommitMsg |
| Author | rich_text | 推送人員名稱 | Author |
| Status | select | 任務狀態 | Status |
| 日期 | date | 任務建立/截止日 | Date/Start/End |
| 金額 | number | 結算金額 | Amount/金額 |

## 驗收清單
- 產生 `exported_settlement_tracker.csv`
- 新分支 feat/test 觸發後 Notion 建立任務
- 每日報表在預定時間更新

## 進階支援
- 欄位自動 mapping／多語型別兼容
- 任務標籤自動化、PR 標籤對應優先級
- 整合 Bot 通知、第三方自動報表
- Google Sheets 互通升級
