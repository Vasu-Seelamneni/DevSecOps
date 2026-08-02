"""
Extract text content from tldraw (.tldr) JSON files for study sheet generation.
"""
import json
import os
import sys


def extract_text_from_rich_text(rich_text):
    """Recursively extract plain text from tldraw richText structure."""
    texts = []
    if not isinstance(rich_text, dict):
        return texts

    content = rich_text.get("content", [])
    if not isinstance(content, list):
        return texts

    for node in content:
        node_type = node.get("type", "")

        if node_type == "paragraph":
            node_content = node.get("content", [])
            line = ""
            for item in node_content:
                if isinstance(item, dict):
                    if item.get("type") == "text":
                        line += item.get("text", "")
                    elif item.get("type") == "link":
                        line += f"[{item.get('text', '')}]"
                    elif "content" in item:
                        # nested
                        for sub in extract_text_from_rich_text({"content": [item]}):
                            line += sub
            texts.append(line)

        elif node_type in ("orderedList", "bulletList"):
            for i, item in enumerate(node.get("content", []), 1):
                if isinstance(item, dict) and item.get("type") == "listItem":
                    item_content = item.get("content", [])
                    prefix = f"{i}. " if node_type == "orderedList" else "• "
                    # item_content is a list of paragraphs
                    first = True
                    for para in item_content:
                        if not isinstance(para, dict):
                            continue
                        para_text = ""
                        for sub in para.get("content", []):
                            if isinstance(sub, dict):
                                if sub.get("type") == "text":
                                    para_text += sub.get("text", "")
                                elif sub.get("type") == "link":
                                    para_text += f"[{sub.get('text', '')}]"
                        if first:
                            texts.append(prefix + para_text)
                            first = False
                        else:
                            texts.append(para_text)

        elif node_type in ("codeBlock",):
            for line_node in node.get("content", []):
                if isinstance(line_node, dict):
                    for item in line_node.get("content", []):
                        if isinstance(item, dict) and item.get("type") == "text":
                            texts.append("    " + item.get("text", ""))

        elif "content" in node and isinstance(node["content"], list):
            for sub in extract_text_from_rich_text({"content": node["content"]}):
                texts.append(sub)

    return texts


def extract_from_tldr(path):
    """Extract all text from a tldraw file, grouped by shape."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_texts = []
    for record in data.get("records", []):
        if record.get("typeName") != "shape":
            continue
        props = record.get("props", {})
        rich_text = props.get("richText")
        if not isinstance(rich_text, dict):
            continue
        texts = extract_text_from_rich_text(rich_text)
        shape_type = record.get("type", "unknown")
        # For text shapes, append with a marker showing it's free text
        for t in texts:
            if t.strip():
                all_texts.append(t)

    return all_texts


def main():
    # Ensure UTF-8 output on all platforms
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    files = sys.argv[1:]
    if not files:
        print("Usage: python extract_tldr_text.py <file1.tldr> [file2.tldr ...]")
        return

    for path in files:
        print(f"\n{'=' * 80}")
        print(f"FILE: {path}")
        print(f"{'=' * 80}")
        try:
            texts = extract_from_tldr(path)
            for i, t in enumerate(texts, 1):
                print(f"{i:4d} | {t}")
        except Exception as e:
            print(f"ERROR reading {path}: {e}")


if __name__ == "__main__":
    main()