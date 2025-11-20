import os
import re
from notion_client import Client
from markdownify import markdownify
from datetime import datetime

# Load env vars
notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

# --------------------------
# Utility functions
# --------------------------

def slugify(title):
    """Generate a clean filename slug."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    return slug.strip("-")


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
# Read pages from Notion DB
# --------------------------

def get_pages():
    """Query Notion database for Published items."""
    response = notion.databases.query(
        database_id=DATABASE_ID,
        filter={
            "property": "Status",
            "select": {"equals": "Published"}
        }
    )
    return response["results"]


# --------------------------
# Export a single Notion page
# --------------------------

def export_page(page):
    page_id = page["id"]
    title = page["properties"]["Name"]["title"][0]["text"]["content"]

    # 날짜
    date_prop = page["properties"].get("Date")
    if date_prop and date_prop["date"]:
        date_str = date_prop["date"]["start"]
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")

    # 태그
    tags = page["properties"].get("Tags", {}).get("multi_select", [])
    tag_list = [t["name"] for t in tags]

    # front matter
    fm = "---\n"
    fm += f"title: \"{title}\"\n"
    fm += f"date: {date_str}\n"
    if tag_list:
        fm += "tags:\n"
        for t in tag_list:
            fm += f"  - {t}\n"
    fm += "---\n\n"

    # 본문 블록
    blocks = notion.blocks.children.list(page_id)
    md_body = ""

    for block in blocks["results"]:
        md_body += convert_block(block)

    # 파일명
    slug = slugify(title)
    filename = f"_posts/{date_str}-{slug}.md"

    os.makedirs("_posts", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(fm + md_body)

    print(f"Generated: {filename}")


# --------------------------
# Main
# --------------------------

def main():
    pages = get_pages()
    if not pages:
        print("No Published pages found.")
        return

    for p in pages:
        export_page(p)


if __name__ == "__main__":
    main()
