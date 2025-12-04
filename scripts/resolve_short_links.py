import re
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import urllib3

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class LinkResolver:
    def __init__(self, timeout=30, delay=0.5, verify_ssl=False):
        """
        初始化链接解析器

        参数:
            timeout: HTTP 请求超时时间（秒）
            delay: 两次请求之间的延迟（秒），避免请求过快
            verify_ssl: 是否验证 SSL 证书
        """
        self.timeout = timeout
        self.delay = delay
        self.verify_ssl = verify_ssl
        self.cache = {}  # 缓存已解析的链接

    def resolve_url(self, short_url):
        """
        解析短链接，获取真实的长链接

        参数:
            short_url: 短链接 URL

        返回:
            解析后的长链接，如果失败则返回原链接
        """
        # 检查缓存
        if short_url in self.cache:
            print(f"    [缓存] {short_url} -> {self.cache[short_url]}")
            return self.cache[short_url]

        try:
            print(f"    [解析] {short_url}", end=" ... ")

            # 发送 GET 请求，跟随重定向
            response = requests.get(
                short_url,
                allow_redirects=True,
                timeout=self.timeout,
                verify=self.verify_ssl,
                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
            )

            # 获取最终的 URL
            final_url = response.url

            # 缓存结果
            self.cache[short_url] = final_url

            print(f"-> {final_url}")

            # 延迟，避免请求过快
            time.sleep(self.delay)

            return final_url

        except requests.exceptions.SSLError as e:
            # SSL 错误时，如果还没有尝试过不验证 SSL，则重试
            if self.verify_ssl:
                print(f"SSL错误，不验证SSL重试...", end=" ")
                try:
                    response = requests.get(
                        short_url,
                        allow_redirects=True,
                        timeout=self.timeout,
                        verify=False,
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
                    )
                    final_url = response.url
                    self.cache[short_url] = final_url
                    print(f"-> {final_url}")
                    time.sleep(self.delay)
                    return final_url
                except Exception as e2:
                    print(f"重试失败: {e2}")
                    return short_url
            else:
                print(f"SSL错误: {e}")
                return short_url
        except requests.exceptions.Timeout:
            print(f"超时")
            return short_url
        except requests.exceptions.RequestException as e:
            print(f"失败: {e}")
            return short_url
        except Exception as e:
            print(f"错误: {e}")
            return short_url


def replace_short_links(content, resolver, domain="oreil.ly"):
    """
    替换内容中的短链接

    参数:
        content: 文本内容
        resolver: LinkResolver 实例
        domain: 要替换的短链接域名

    返回:
        替换后的内容和替换次数
    """
    # 匹配 oreil.ly 链接的正则表达式
    # 匹配 markdown 链接格式 [text](url) 和纯文本 URL
    pattern = rf'https?://{re.escape(domain)}/[A-Za-z0-9_-]+'

    replacements = 0

    def replace_func(match):
        nonlocal replacements
        short_url = match.group(0)
        long_url = resolver.resolve_url(short_url)

        if long_url != short_url:
            replacements += 1

        return long_url

    # 执行替换
    updated_content = re.sub(pattern, replace_func, content)

    return updated_content, replacements


def process_markdown_files(src_dir="src", domain="oreil.ly", backup=True):
    """
    处理指定目录下的所有 markdown 文件

    参数:
        src_dir: 源文件目录
        domain: 要替换的短链接域名
        backup: 是否备份原文件
    """
    src_path = Path(src_dir)

    if not src_path.exists():
        print(f"错误: {src_dir} 目录不存在")
        return

    # 初始化解析器
    resolver = LinkResolver()

    # 统计信息
    total_files = 0
    processed_files = 0
    skipped_files = 0
    total_replacements = 0

    print(f"开始处理 {src_dir} 目录下的 markdown 文件...")
    print(f"目标短链接域名: {domain}")
    print("=" * 60)

    # 遍历所有 .md 文件
    for file_path in sorted(src_path.rglob("*.md")):
        total_files += 1

        try:
            print(f"\n📄 处理文件: {file_path.relative_to(src_path.parent)}")

            # 读取文件内容
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 检查文件中是否包含目标短链接
            if domain not in content:
                print(f"  ⏭️  跳过: 文件中没有 {domain} 链接")
                skipped_files += 1
                continue

            # 处理内容
            updated_content, replacements = replace_short_links(content, resolver, domain)

            # 检查是否有变化
            if replacements == 0:
                print(f"  ⏭️  跳过: 没有成功解析的链接")
                skipped_files += 1
                continue

            # 备份原文件（如果需要）
            if backup:
                backup_path = str(file_path) + ".short_links.bak"
                # 如果备份文件已存在，不覆盖
                if not Path(backup_path).exists():
                    with open(backup_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"  💾 已备份到: {Path(backup_path).name}")

            # 写入更新后的内容
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

            print(f"  ✅ 成功替换 {replacements} 个链接")
            processed_files += 1
            total_replacements += replacements

        except Exception as e:
            print(f"  ❌ 处理文件时发生错误: {e}")

    # 打印统计信息
    print(f"\n{'='*60}")
    print(f"处理完成!")
    print(f"总文件数: {total_files}")
    print(f"已处理: {processed_files}")
    print(f"已跳过: {skipped_files}")
    print(f"失败: {total_files - processed_files - skipped_files}")
    print(f"总替换数: {total_replacements}")
    print(f"{'='*60}")

    # 打印缓存的链接映射
    if resolver.cache:
        print(f"\n📋 链接映射表:")
        print(f"{'='*60}")
        for short_url, long_url in sorted(resolver.cache.items()):
            print(f"{short_url}")
            print(f"  -> {long_url}")


if __name__ == "__main__":
    # 运行脚本
    # 可以通过修改参数来自定义行为
    # backup=False 表示不备份原文件
    # domain 可以改为其他短链接域名
    process_markdown_files(src_dir="src", domain="oreil.ly", backup=True)
