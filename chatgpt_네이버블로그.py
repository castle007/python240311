import requests
from bs4 import BeautifulSoup

def naver_blog_search(search_keyword):
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    blog_list = soup.select('.sh_blog_top')

    for blog in blog_list:
        blog_name = blog.select_one('.sh_blog_title').text
        blog_title = blog.select_one('.sh_blog_title').attrs['title']
        blog_date = blog.select_one('.txt_inline').text
        print("블로그명:", blog_name)
        print("글 제목:", blog_title)
        print("날짜:", blog_date)
        print()

search_keyword = input("검색어를 입력하세요: ")
naver_blog_search(search_keyword)
