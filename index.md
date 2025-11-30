# 結算檢查表自動化部署手冊
本頁提供一鍵部署步驟、Secrets 清單與驗收流程，適合 PM 與 AI 共同維運。

## 一鍵部署步驟
1. 新增 Secrets：`NOTION_TOKEN`、`NOTION_DATABASE_ID`（必要），`GITHUB_REPO`（選用）。
2. 複製以下檔案至專案：
   - `.github/workflows/auto_sync_notionsheet.yaml`
   - `.github/workflows/generate_report.yml`
   - `scripts/notion_export_csv.py`
   - `scripts/branch_to_task.py`
3. 於 Actions 手動 Run workflow 完成首輪驗收。

## 驗收清單
- 產生 `exported_settlement_tracker.csv`
- 新分支 feat/test 觸發後 Notion 建立任務
- 每日報表在預定時間更新

## 進階支援
- 欄位自動 mapping／多語型別兼容
- 任務標籤自動化、PR 標籤對應優先級
- 整合 Bot 通知、第三方自動報表
- Google Sheets 互通升級
