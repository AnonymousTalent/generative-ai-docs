# Google Gemini API Website & Documentation

These are the source files for the guide and tutorials on
the [Generative AI developer site](https://ai.google.dev/), home to
the Gemini API and Gemma.

| Path | Description |
| ---- | ----------- |
| [`site/`](site/) | Notebooks and other content used directly on ai.google.dev. |
| [`demos/`](demos/) | Demos apps. Larger than examples, typically consists of working apps. |
| [`examples/`](examples/) | Examples. Smaller, single-purpose code for demonstrating specific concepts. |



To contribute to the site documentation, please read
[CONTRIBUTING.md](CONTRIBUTING.md).

To contribute as a demo app maintainer, please read
[DEMO_MAINTAINERS.md](DEMO_MAINTAINERS.md).

To file an issue, please use the
[GitHub issue tracker](https://github.com/google/generative-ai-docs/issues/new).

## License

[Apache License 2.0](LICENSE)

# Lightning Empire · GitHub × Notion 結算檢查表自動化

將 Notion「結算檢查表 Settlement Tracker」自動導出為 CSV 並回寫至 GitHub，搭配分支/PR 事件自動建立 Notion 任務卡，形成每日稽核循環。

## 目錄
- 功能概述
- 檔案結構
- 安裝與設定
- 快速驗收
- 工作流程說明（L1/L2/L3）
- 常見問題
- 延伸升級

## 功能概述
- **L1 每小時**：Notion → CSV → GitHub
- **L2 事件派單**：branch/PR → Notion 任務卡
- **L3 每日**：自動產生結算報表（CSV）

## 檔案結構
.github/
  workflows/
    auto_sync_notionsheet.yaml
    generate_report.yml
scripts/
  notion_export_csv.py
  branch_to_task.py

## 安裝與設定
1. 在 GitHub → Settings → Secrets and variables → Actions 新增：
   - `NOTION_TOKEN`：Notion Internal Integration Token（已分享至目標 DB）
   - `NOTION_DATABASE_ID`：目標資料庫 ID
   - `GITHUB_REPO`：WindGodLightning/financial-automation（選用）
   - `GITHUB_TOKEN`：Actions 內建，無需新增
2. 將 workflows 與 scripts 置於對應路徑。
3. 啟用 Actions，首次可於 Actions 頁面手動 Run workflow。

## 快速驗收
- 觸發 L1 或 L3 後，檢查根目錄是否產生 `exported_settlement_tracker.csv`
- 測試 L2：
