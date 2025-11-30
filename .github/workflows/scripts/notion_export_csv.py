import os, math
import pandas as pd
from notion_client import Client

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
notion = Client(auth=NOTION_TOKEN)

def fetch_all(database_id: str):
    results, cursor = [], None
    while True:
        resp = notion.databases.query(database_id=database_id, start_cursor=cursor, page_size=100)
        results.extend(resp["results"])
        cursor = resp.get("next_cursor")
        if not resp.get("has_more"):
            break
    return results

def cell(prop):
    t = prop["type"]
    v = prop.get(t)
    # 欄位型別自動對應：依下表可增減自定義
    if t == "title":
        return "".join([x["plain_text"] for x in prop["title"]])
    if t == "rich_text":
        return "".join([x["plain_text"] for x in prop["rich_text"]])
    if t == "number":
        return v
    if t == "select":
        return v["name"] if v else ""
    if t == "multi_select":
        return ",".join([x["name"] for x in v])
    if t == "date":
        return v["start"] if v else ""
    if t == "status":
        return v["name"] if v else ""
    if t == "people":
        return ",".join([p.get("name","") for p in v]) if v else ""
    return str(v) if v is not None else ""

def parse(item):
    props = item["properties"]
    # 只要欄位名稱對應 Notion，就自動抓取。可自定增減。
    return {k: cell(props[k]) for k in props.keys()}

items = fetch_all(DATABASE_ID)
rows = [parse(it) for it in items]
pd.DataFrame(rows).to_csv("exported_settlement_tracker.csv", index=False, encoding='utf-8-sig')
print(f"Exported {len(rows)} rows → exported_settlement_tracker.csv")
