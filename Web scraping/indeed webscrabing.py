import requests
from bs4 import BeautifulSoup
import pandas
def extract(page):
    headers = {'User_Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"}

    url = f"https://au.indeed.com/jobs?q=data+analyst&l=2028&start={page}"

    r = requests.get(url, headers)
    soup = BeautifulSoup(r. content, "html.parser")
    return soup
def transform(soup):
    divs = soup.find_all("div", class_ = "jobsearch-SerpJobCard")
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find("span", class_ ="company").text.strip()
        try:
            salary = item.find("span", class_ ="salaryText").text.strip()
        except:
            salary = " "
        summary = item.find("div", {"class": "summary"}).text.strip().replace("\n", " ")

        job = {
            "title": title,
            'company': company,
            "salary": salary,
            "summary":summary
        }
        joblist.append(job)
    return

joblist = []
for i in range(0,40, 10):
    print(f"Getting page, {i}")

    c= extract(0)
    transform(c)
df = pandas.DataFrame(joblist)
print(df.head())
df.to_csv("jobs.cvs")


#summary=item.find_all("div", {"id": "summary"})
