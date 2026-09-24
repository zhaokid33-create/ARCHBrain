#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
建筑案例库自动编译脚本
每周五执行，将 raw/ 中的案例交叉编译到 wiki/
"""

import os
import json
from pathlib import Path
from datetime import datetime

RAW_DIR = Path("E:/codex/brain/raw")
WIKI_DIR = Path("E:/codex/brain/wiki")

def ensure_wiki_structure():
    """确保 wiki 目录结构存在"""
    subdirs = ["building_types", "regions", "design_methods", "styles", "index"]
    for subdir in subdirs:
        (WIKI_DIR / subdir).mkdir(parents=True, exist_ok=True)

def parse_raw_files():
    """扫描 raw/ 并解析建筑案例"""
    cases = []
    if not RAW_DIR.exists():
        print(f"[警告] raw 目录不存在: {RAW_DIR}")
        return cases

    for file_path in RAW_DIR.rglob("*"):
        if file_path.is_file() and file_path.suffix in [".md", ".txt", ".json"]:
            try:
                content = file_path.read_text(encoding="utf-8")
                case = extract_case_info(content, file_path.name)
                if case:
                    cases.append(case)
            except Exception as e:
                print(f"[错误] 解析文件失败 {file_path}: {e}")
    return cases

def extract_case_info(content, filename):
    """从文件内容中提取建筑案例信息"""
    case = {
        "name": "",
        "location": "",
        "year": "",
        "designer": "",
        "style": "",
        "method": "",
        "source": filename
    }

    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("项目名称") or line.startswith("name"):
            case["name"] = line.split(":", 1)[-1].strip() or line.split("：", 1)[-1].strip()
        elif line.startswith("位置") or line.startswith("location"):
            case["location"] = line.split(":", 1)[-1].strip() or line.split("：", 1)[-1].strip()
        elif line.startswith("年份") or line.startswith("year"):
            case["year"] = line.split(":", 1)[-1].strip() or line.split("：", 1)[-1].strip()
        elif line.startswith("设计师") or line.startswith("designer"):
            case["designer"] = line.split(":", 1)[-1].strip() or line.split("：", 1)[-1].strip()
        elif line.startswith("风格") or line.startswith("style"):
            case["style"] = line.split(":", 1)[-1].strip() or line.split("：", 1)[-1].strip()
        elif line.startswith("手法") or line.startswith("method"):
            case["method"] = line.split(":", 1)[-1].strip() or line.split("：", 1)[-1].strip()

    if case["name"] or case["location"]:
        return case
    return None

def compile_to_wiki(cases):
    """将案例编译到 wiki 的各个维度"""
    by_type = {}
    by_region = {}
    by_method = {}
    by_style = {}

    for case in cases:
        btype = case.get("method", "其他").split("/")[0] or "其他"
        if btype not in by_type:
            by_type[btype] = []
        by_type[btype].append(case)

        region = case.get("location", "未分类").split("/")[0] or "未分类"
        if region not in by_region:
            by_region[region] = []
        by_region[region].append(case)

        method = case.get("method", "未分类")
        if method not in by_method:
            by_method[method] = []
        by_method[method].append(case)

        style = case.get("style", "未分类")
        if style not in by_style:
            by_style[style] = []
        by_style[style].append(case)

    write_category_pages("building_types", by_type, cases)
    write_category_pages("regions", by_region, cases)
    write_category_pages("design_methods", by_method, cases)
    write_category_pages("styles", by_style, cases)

    return {
        "total_cases": len(cases),
        "types": len(by_type),
        "regions": len(by_region),
        "methods": len(by_method),
        "styles": len(by_style)
    }

def write_category_pages(category, grouped_data, all_cases):
    """写入分类页面"""
    for category_name, cases_list in grouped_data.items():
        filename = category_name.replace(" ", "_").replace("/", "_") + ".md"
        filepath = WIKI_DIR / category / filename
        content = generate_category_page(category_name, cases_list, all_cases)
        filepath.write_text(content, encoding="utf-8")

def generate_category_page(category_name, cases_list, all_cases):
    """生成分类页面内容"""
    lines = [
        f"# {category_name}",
        "",
        f"更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"案例数量：{len(cases_list)}",
        "",
        "## 案例列表",
        ""
    ]

    for case in cases_list:
        lines.append(f"### {case['name']}")
        lines.append(f"- 位置：{case['location']}")
        lines.append(f"- 年份：{case['year']}")
        lines.append(f"- 设计师：{case['designer']}")
        lines.append(f"- 风格：{case['style']}")
        lines.append(f"- 手法：{case['method']}")
        lines.append("")

    return "\n".join(lines)

def generate_index():
    """生成 wiki 总入口"""
    cases = parse_raw_files()
    stats = compile_to_wiki(cases)

    lines = [
        "# 建筑案例库",
        "",
        f"最后编译：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 统计",
        f"- 总案例数：{stats['total_cases']}",
        f"- 建筑类型：{stats['types']}",
        f"- 地域：{stats['regions']}",
        f"- 设计手法：{stats['methods']}",
        f"- 风格：{stats['styles']}",
        "",
        "## 浏览方式",
        "- [按建筑类型](building_types/)",
        "- [按地域](regions/)",
        "- [按设计手法](design_methods/)",
        "- [按风格](styles/)",
        ""
    ]

    index_path = WIKI_DIR / "index" / "README.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")

    return stats

def main():
    print("[开始] 建筑案例库编译")
    print(f"Raw 目录：{RAW_DIR}")
    print(f"Wiki 目录：{WIKI_DIR}")
    print("")

    ensure_wiki_structure()
    stats = generate_index()

    print("[完成] 编译统计：")
    print(f"  总案例数：{stats['total_cases']}")
    print(f"  建筑类型：{stats['types']}")
    print(f"  地域：{stats['regions']}")
    print(f"  设计手法：{stats['methods']}")
    print(f"  风格：{stats['styles']}")
    print("")
    print(f"Wiki 已更新到：{WIKI_DIR}")

if __name__ == "__main__":
    main()
