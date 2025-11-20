import os
from notion_client import Client
from markdownify import markdownify
from datetime import datetime

notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

def get_pages():
    response = notion.databases.query(
        **{
            "database_id": DATABASE_ID,
            "filter": {
                "property": "Status",
                "select": {"equals": "Published"}
            }
        }
    )
    return response["results"]

def convert_block_to_markdown(block):
    """Convert supported Notion block types to markdown."""
    block_type = block["type"]
    content = ""

    if block_type == "paragraph":
        for rich in block["paragraph"]["rich_text"]:
            content += rich["plain_text"]
        return content + "\n\n"

    if block_type == "heading_1":
        text = "".join(r["plain_text"] for r in block["heading_1"]["rich_text"])
        return f"# {text}\n\n"

    if block_type == "heading_2":
        text = "".join(r["plain_text"] for r in block["heading_2"]["rich_text"])
        return f"## {text}\n\n"

    if block_type == "heading_3":
        text = "".join(r["plain_text"] for r in block["heading_3"]["rich_text"])
        return f"### {text}\n\n"

    if block_type == "bulleted_list_item":
        text = "".join(r["plain_text"] for r in block["bulleted_list_item"]["rich_text"])
        return f"- {text}\n"

    if block_type == "numbered_list_item":
        text = "".join(r["plain_text"] for r in block["numbered_list_item"]["rich_text"])
        return f"1. {text}\n"

    return ""

def export_page(page):
    page_id = page["id"]
    title = page["properties"]["Title"]["title"][0]["text"]["content"]

    # 날짜 front matter
    date_prop = page["properties"].get("Date")
    date_str = None
    if date_prop and date_prop.get("date"):
        date_str = date_prop["date"]["start"]
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")

    # 태그
    tags = page["properties"].get("Tags", {}).get("multi_select", [])
    tag_list = [t["name"] for t in tags]

    # front matter 생성
    front_matter = "---\n"
    front_matter += f"title: \"{title}\"\n"
    front_matter += f"date: {date_str}\n"
    if tag_list:
        front_matter += "tags:\n"
        for t in tag_list:
            front_matter += f"  - {t}\n"
    front_matter += "---\n\n"

    # 본문 블록 가져오기
    blocks = notion.blocks.children.list(page_id)
    body_md = ""

    for block in blocks["results"]:
        body_md += convert_block_to_markdown(block)

    # 파일명
    safe_title = title.replace(" ", "-").replace("/", "-")
    filename = f"_posts/{date_str}-{safe_title}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + body_md)

    print(f"Generated: {filename}")

def main():
    pages = get_pages()
    for page in pages:
        export_page(page)

if __name__ == "__main__":
    main()
