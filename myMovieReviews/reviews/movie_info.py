import requests
from bs4 import BeautifulSoup as bs

def main_img(code):
    url = f"https://movie.naver.com{code}"

    resp = requests.get(url)

    soup = bs(resp.text, "html.parser")

    img_src = soup.select(".mv_info_area .poster img")

  
    return img_src[0].get("src")
    


def searchInfo(keyword):
    url = f"https://movie.naver.com/movie/search/result.naver?section=movie&query={keyword}"

    resp = requests.get(url)

    soup = bs(resp.text, "html.parser")

    infos = soup.select("#old_content .search_list_1 li")

    info_data = []

    if infos:
        for info in infos:
            img = info.select_one("img").get("src")
            datas = info.select(".etc")
            title = info.select_one("dt").text
            main = info.select_one("dt a").get("href")
            poster = main_img(main)
            tmp = []
            for idx in range(len(datas)):
                data = datas[idx].text.split("|")
                if idx == 0 :
                    if len(data) == 4:
                        if data[2] != data[2].replace("분 ", ""):
                            data[2] = data[2].replace("분 ", "")
                            data[2] = int(data[2])
                            data[3] = int(data[3])
                    else:
                        if len(data) == 3:
                            if data[2][len(data[2])-2] != "분 ":
                                data.insert(2, "")
                        elif len(data) == 2:
                            data.insert(0, "")
                            data.insert(2, "")
                else:
                    if len(data) == 0:
                        data.insert(0, "")
                        data.insert(1, "")
                    elif len(data) == 1:
                        data.insert(1, "")
                    data[0] = data[0][5:]
                    data[1] = data[1][5:]
                tmp += data
            tmp.insert(0, title)
            tmp.append(img)
            tmp.append(poster)
            
            info_data.append(tmp)
        
    return info_data
    