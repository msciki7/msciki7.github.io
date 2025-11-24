import os
import re
from notion_client import Client
from datetime import datetime

# Load env vars
notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]ㅇ

# --------------------------
# Utility functions
# --------------------------

def slugify(text):
    """Generate a clean filename slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text.strip("-")


def extract_chapter_folder(title):
    """
    예: "chapter 5-4. Multilevel Caches"
    → chapter5
    """
    match = re.search(r"chapter\s*(\d+)", title, re.IGNORECASE)
    if match:
        return f"chapter{match.group(1)}"
    return "chapter-etc"


def convert_block(block):
    """Convert Notion block to Markdown."""
    block_type = block["type"]
    md = ""

    if block_type == "paragraph":
        texts = block["paragraph"]["rich_text"]
        md += "".join(t["plain_text"] for t in texts) + "\n\n"

    elif block_type == "heading_1":
        text = "".join(t["plain_text"] for t in block["heading_1"]["rich_text"])
        md += f"# {text}\n\n"

    elif block_type == "heading_2":
        text = "".join(t["plain_text"] for t in block["heading_2"]["rich_text"])
        md += f"## {text}\n\n"

    elif block_type == "heading_3":
        text = "".join(t["plain_text"] for t in block["heading_3"]["rich_text"])
        md += f"### {text}\n\n"

    elif block_type == "bulleted_list_item":
        text = "".join(t["plain_text"] for t in block["bulleted_list_item"]["rich_text"])
        md += f"- {text}\n"

    elif block_type == "numbered_list_item":
        text = "".join(t["plain_text"] for t in block["numbered_list_item"]["rich_text"])
        md += f"1. {text}\n"

    return md


# --------------------------
# Query Notion
# --------------------------

def get_pages():
    """모든 Published / Deleted 페이지 가져오기."""
    response = notion.databases.query(
        database_id=DATABASE_ID,
        filter={
            "or": [
                {"property": "Status", "select": {"equals": "Published"}},
                {"property": "Status", "select": {"equals": "Deleted"}},
            ]
        }
    )
    return response["results"]


# --------------------------
# Export Notion page
# --------------------------

def export_page(page):
    props = page["properties"]

    # ------------ 상태 확인 ------------------
    status_prop = props.get("Status")
    if status_prop and status_prop.get("select"):
        status = status_prop["select"]["name"]
    else:
        status = "Draft"

    if status == "Draft":
        print("🔸 Draft → SKIP")
        return None

    # ------------ 제목 -----------------------
    title = props["Name"]["title"][0]["text"]["content"]

    # ------------ 날짜 -----------------------
    date_prop = props.get("Date")
    if date_prop and date_prop["date"]:
        date_str = date_prop["date"]["start"]
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")

    # ------------ category -------------------
    category_raw = props.get("Class", {}).get("select", {}).get("name", "uncategorized")
    category_slug = slugify(category_raw)

    # ------------ chapter folder -------------
    chapter_folder = extract_chapter_folder(title)

    # ------------ tags -----------------------
    tags = props.get("Tags", {}).get("multi_select", [])
    tag_list = [t["name"] for t in tags]

    # ------------ front matter ---------------
    fm = "---\n"
    fm += f"title: \"{title}\"\n"
    fm += f"date: {date_str}\n"

    # ★★ Minimal Mistakes는 categories: 배열 형태여야 함
    fm += "categories:\n"
    fm += f"  - {category_raw}\n"

    if tag_list:
        fm += "tags:\n"
        for t in tag_list:
            fm += f"  - {t}\n"
    fm += "---\n\n"

    # ------------ 본문 -----------------------
    blocks = notion.blocks.children.list(page["id"])
    md_body = "".join(convert_block(b) for b in blocks["results"])

    # ------------ 파일 경로 -------------------
    slug = slugify(title)
    folder = f"_posts/category-{category_slug}/{chapter_folder}"
    os.makedirs(folder, exist_ok=True)

    filename = f"{folder}/{date_str}-{slug}.md"

    # ------------ Status가 Deleted인 경우 삭제 ------------
    if status == "Deleted":
        if os.path.exists(filename):
            os.remove(filename)
            print(f"🗑️ Deleted: {filename}")
        else:
            print("🗑️ Deleted but file not found:", filename)
        return

    # ------------ 기존 파일 있으면 덮어쓰기 금지 ------------
    if os.path.exists(filename):
        print(f"⏭ Already exists, skip: {filename}")
        return

    # ------------ 파일 생성 -------------------
    with open(filename, "w", encoding="utf-8") as f:
        f.write(fm + md_body)

    print(f"✅ Generated: {filename}")


# --------------------------
# Main
# --------------------------

def main():
    pages = get_pages()
    for p in pages:
        export_page(p)


if __name__ == "__main__":
    main()
