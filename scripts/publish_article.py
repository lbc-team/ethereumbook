import requests
import os
import json
import time
from datetime import datetime, timedelta

from config import LBC_BASE_API_URL, LBC_API_KEY
from urllib.parse import urlencode

import llm_analyze

def try_create_user(handle, url):
    lbc_handle = handle
    if len(handle) < 6: # 如果 handle 小于 6 位，则添加几个 _
        lbc_handle = handle + "_" * (6 - len(handle))

    payload = {
        "handle": lbc_handle,
    }

    response = requests.post(
        url=LBC_BASE_API_URL + '/api/create/user',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-api-key': LBC_API_KEY
        },
        data = urlencode(payload)
    )

    
    if response.status_code == 200:
        result = response.json()
        resultCode = result.get("code")
        print(result)
        print(resultCode)
        if resultCode == 0:
            user_id = result.get("user").get("id")
            print(f" LBC  创建用户 Handle: {handle} 成功")

            crawler_db_helper.add_handle_lbc_uid(handle, user_id, lbc_handle, url)
            return user_id
        elif resultCode == -10001:
            user_id = result.get("user").get("id")
            
            print(f"用户 Handle:  {handle} 存在  {user_id}")
            crawler_db_helper.add_handle_lbc_uid(handle, user_id, lbc_handle, url)
            return user_id
        else:
            print(f"LBC创建用户 Handle:  {handle} 失败, 错误信息: {result.get('message')}")
            return None
    else:
        print(f"LBC  创建用户 Handle:  {handle} 失败, 错误信息 {response.status_code}")
        return None



def publish_article(filename):
    content = open(filename, "r").read()
        
    analyze_result = llm_analyze.analyze_article(content)
    print("analyze_result:", analyze_result)
    summary = analyze_result.get("summary")
    keywords = analyze_result.get("keywords")
    print("summary:", summary)
    print("keywords:", keywords)

    handle = "ethbook"
    link = "https://masteringethereum.xyz/" + filename.replace(".md", ".html")
    category_id = get_category_id("以太坊")

    tags = "以太坊"
    
    article_featured = 1
    article_level = 2

    createday = "2025-11-30"
    print("预备发布时间:", createday)

    article_type = 2 # 翻译文章类型， 3： 转发

    # 如果文章是 OpenZeppelin 的审计文章，设置为普通
    if "https://blog.openzeppelin.com/" in link and link.endswith("audit"):
        article_featured = 0
        

    title = first_line_of_file(filename).replace("# ", "")

    payload = {
        'title': title,
        'content': content,
        'summary':  trim_summary(article.get("summary")),
        'link': link,
        'author_id': authorId, # 指定用户 id 
        'category_id': category_id,
        'proofread': False,
        'is_public': True,
        'tags': tags,
        'featured': article_featured,
        'level': article_level,
        'type': article_type
    }

    if createday:
        payload['createday'] = createday

    # print(urlencode(payload))

    lbc_article_id = post_article(
        payload                       
    )

    if lbc_article_id:
        print(f"{article.get('id')} 发布成功，LBC 文章ID: {lbc_article_id}")

    else:
        print(f"发布文章： {article.get('id')} 发布失败")
    return lbc_article_id
        
def post_article(payload, max_retries=2, retry_delay=5):
    """
    发布文章，遇到504错误时自动重试
    
    Args:
        payload: 文章数据
        max_retries: 最大重试次数，默认3次
        retry_delay: 重试前等待时间（秒），默认5秒
    
    Returns:
        lbc_article_id: 成功时返回文章ID，失败时返回None
    """
    for attempt in range(max_retries):
        response = requests.post(
            url=LBC_BASE_API_URL + '/api/post/article',
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-api-key': LBC_API_KEY
            },
            data = urlencode(payload)
        )

        if response.status_code == 200:
            result = response.json()
            print(result)

            if result.get("code") == 0:
                print(f" {payload.get('link')} 发布成功")
                lbc_article_id = result.get("article_id")
                return lbc_article_id
            else:
                print(f" {payload.get('link')} 发布失败, {result.get('code')},   错误信息: {result.get('message')}")
                return None
        
        elif response.status_code == 504:
            # 504 Gateway Timeout 错误，进行重试
            if attempt < max_retries - 1:
                print(f" {payload.get('link')} 遇到504错误，{retry_delay}秒后重试 (第 {attempt + 1}/{max_retries} 次尝试)")
                time.sleep(retry_delay)
                continue
            else:
                print(f" {payload.get('link')} 发布失败，504错误，已重试 {max_retries} 次，放弃")
                return None
        else:
            print(f" {payload.get('link')} 发布失败{response.status_code} {response.text}")
            return None
    
    return None


def update_lbc_article(article_id, new_markdown):
    payload = {
        "article_id": article_id,
        "content": new_markdown
    }

    # print(payload)
    url = LBC_BASE_API_URL + '/api/article/update'

    response = requests.post(
        url,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-api-key': LBC_API_KEY
        },
        data=urlencode(payload)
    )

    
    if response.status_code == 200:
        result = response.json()
        print(result)
        if result.get("code") == 0:
            print(f"更新文章 {article_id} 中的链接成功")
        else:
            print(f"更新文章 {article_id} 中的链接失败")
    else:
        print(f"更新文章 {article_id} 中的链接失败")

if __name__ == "__main__":
    publish_article("src/chapter_1.md")
