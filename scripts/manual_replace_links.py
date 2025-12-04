import re
from pathlib import Path

# 手动映射的链接
manual_mappings = {
    "https://oreil.ly/ge7zP": "https://en.wikipedia.org/wiki/Fungibility",
    "https://oreil.ly/TTA96": "https://en.wikipedia.org/wiki/Not_invented_here",
    "https://oreil.ly/wOT_b": "https://en.wikipedia.org/wiki/Cryptography",
    "https://oreil.ly/WrxXr": "https://en.wikipedia.org/wiki/Trapdoor_function",
    "https://oreil.ly/rxAnN": "https://en.wikipedia.org/wiki/Integer_factorization",
    "https://oreil.ly/pj8PD": "https://en.wikipedia.org/wiki/Discrete_logarithm",
    "https://oreil.ly/RP2QF": "https://en.wikipedia.org/wiki/Elliptic-curve_cryptography",
    "https://oreil.ly/kRnY2": "https://en.wikipedia.org/wiki/Digital_signature",
    "https://oreil.ly/_-iC-": "https://web.archive.org/web/20180723043801/https:/github.com/etherpot/contract/blob/master/app/contracts/lotto.sol",
}

def replace_manual_links(content, mappings):
    """
    手动替换内容中的短链接

    参数:
        content: 文本内容
        mappings: 短链接到长链接的映射字典

    返回:
        替换后的内容和替换次数
    """
    replacements = 0
    updated_content = content

    for short_url, long_url in mappings.items():
        if short_url in updated_content:
            count = updated_content.count(short_url)
            updated_content = updated_content.replace(short_url, long_url)
            replacements += count
            print(f"    ✓ 替换 {count} 次: {short_url}")
            print(f"      -> {long_url}")

    return updated_content, replacements

def process_files(src_dir="src", backup=True):
    """处理指定目录下的 markdown 文件"""
    src_path = Path(src_dir)

    if not src_path.exists():
        print(f"错误: {src_dir} 目录不存在")
        return

    total_files = 0
    processed_files = 0
    total_replacements = 0

    print("开始手动替换剩余的短链接...")
    print("=" * 60)

    for file_path in sorted(src_path.glob("*.md")):
        # 读取文件内容
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 检查是否包含需要替换的链接
        needs_replacement = any(short_url in content for short_url in manual_mappings.keys())

        if not needs_replacement:
            continue

        total_files += 1
        print(f"\n📄 处理文件: {file_path.relative_to(src_path.parent)}")

        # 备份原文件（如果需要且不存在备份）
        if backup:
            backup_path = str(file_path) + ".manual.bak"
            if not Path(backup_path).exists():
                with open(backup_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  💾 已备份到: {Path(backup_path).name}")

        # 替换内容
        updated_content, replacements = replace_manual_links(content, manual_mappings)

        if replacements > 0:
            # 写入更新后的内容
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

            print(f"  ✅ 成功替换 {replacements} 个链接")
            processed_files += 1
            total_replacements += replacements
        else:
            print(f"  ⏭️  跳过: 没有需要替换的链接")

    # 打印统计信息
    print(f"\n{'='*60}")
    print(f"处理完成!")
    print(f"处理文件数: {processed_files}")
    print(f"总替换数: {total_replacements}")
    print(f"{'='*60}")

if __name__ == "__main__":
    process_files(src_dir="src", backup=True)
