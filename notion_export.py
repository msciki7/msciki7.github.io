import os
import re
from notion_client import Client
from datetime import datetime

# Load env vars
notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

# ===================================================
# Utility
# ===================================================

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text.strip("-")


def convert_block(block):
    """Convert Notion block → Markdown"""
    t = block["type"]
    md = ""

    if t == "paragraph":
        text = "".join(r["plain_text"] for r in block[t]["rich_text"])
        md += text + "\n\n"

    elif t == "heading_1":
        text = "".join(r["plain_text"] for r in block[t]["rich_text"])
        md += f"# {text}\n\n"

    elif t == "heading_2":
        text = "".join(r["plain_text"] for r in block[t]["rich_text"])
        md += f"## {text}\n\n"

    elif t == "heading_3":
        text = "".join(r["plain_text"] for r in block[t]["rich_text"])
        md += f"### {text}\n\n"

    elif t == "bulleted_list_item":
        text = "".join(r["plain_text"] for r in block[t]["rich_text"])
        md += f"- {text}\n"

    elif t == "numbered_list_item":
        text = "".join(r["plain_text"] for r in block[t]["rich_text"])
        md += f"1. {text}\n"

    return md


# ===================================================
# Read every page (any status)
# ===================================================

def get_all_pages():
    response = notion.databases.query(database_id=DATABASE_ID)
    return response["results"]


# ===================================================
# Delete GitHub file
# ===================================================

def delete_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"🔥 Deleted: {path}")
        return True
    return False


# ===================================================
# Export single Notion page
# ===================================================

def export_page(page):
    props = page["properties"]

    # Title
    title = props["Name"]["title"][0]["text"]["content"]
    slug = slugify(title)

    # Status
    status_prop = props.get("Status")
    if status_prop and status_prop.get("select"):
    status = status_prop["select"]["name"]
    else:
    status = "Draft"   # 기본값


    # Category (Class)
    category_raw = page["properties"]["Class"]["select"]["name"]
    chapter_raw = page["properties"]["Chapter"]["select"]["name"]

    category_slug = slugify(category_raw)
    chapter_slug = slugify(chapter_raw)

    folder_path = f"_posts/category-{category_slug}/{chapter_slug}"
    os.makedirs(folder_path, exist_ok=True)

    filename = f"{folder_path}/{date_str}-{slug}.md"

    # Chapter (optional)
    chapter_raw = props.get("Chapter", {}).get("rich_text", [])
    chapter_name = chapter_raw[0]["plain_text"] if chapter_raw else "general"
    chapter_slug = slugify(chapter_name)

    # Date
    date_prop = props.get("Date")
    date_str = date_prop["date"]["start"] if (date_prop and date_prop["date"]) \
        else datetime.now().strftime("%Y-%m-%d")

    # File path
    folder_path = f"_posts/category-{category_slug}/{chapter_slug}"
    filename = f"{folder_path}/{date_str}-{slug}.md"

    # =============== Status: Deleted ===============
    if status == "Deleted":
        delete_file_if_exists(filename)
        return

    # =============== Status: Not Published ===============
    if status != "Published":
        return

    # =============== Overwrite 방지 ===============
    if os.path.exists(filename):
        print(f"⛔ Skip (already exists): {filename}")
        return

    # Create folder
    os.makedirs(folder_path, exist_ok=True)

    # Tags
    tags = props.get("Tags", {}).get("multi_select", [])
    tag_list = [t["name"] for t in tags]

    # Load blocks
    blocks = notion.blocks.children.list(page["id"])
    md_body = "".join(convert_block(b) for b in blocks["results"])

    # Front matter
    fm = "---\n"
    fm += f"title: \"{title}\"\n"
    fm += f"date: {date_str}\n"
    fm += f"category: {category_raw}\n"
    fm += f"chapter: {chapter_name}\n"
    if tag_list:
        fm += "tags:\n"
        for t in tag_list:
            fm += f"  - {t}\n"
    fm += "---\n\n"

    # Write markdown
    with open(filename, "w", encoding="utf-8") as f:
        f.write(fm + md_body)

    print(f"✅ Exported: {filename}")


# ===================================================
# Main
# ===================================================

def main():
    pages = get_all_pages()
    for p in pages:
        export_page(p)


if __name__ == "__main__":
    main()
