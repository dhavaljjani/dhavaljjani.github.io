#This script to run once every X using windows task scheduler?
"""
Outputted directories:
south_bay_journal
    ->archive
        ->BLOG_TITLE
            ->img (FOR FUTURE)
                ->img0.png, img1.png, img2.png, etc, etc
            ->cover_img.png
            ->TITLE.html
        ->[...other blog folders]
    ->[home page, css, python, readme]
"""
import os, feedparser, requests, re, html
from bs4 import BeautifulSoup
from PIL import Image

def extract_cover_image(link_list, title):
    #get link itself
    #print(f"link is {link_list} of type {type(link_list)}")
    link = link_list[1].href

    #empty cover_img.png at path
    path = f"C:/Users/dhava/Documents/dhavaljjani.github.io/south_bay_journal/archive/{clean_title_name_for_dir(title)}/cover_img.png"
    img = Image.new('RGB', (540, 540), color=(255, 255, 255))
    img.save(path, 'PNG')

    #download cover image and save to cover_img.png
    if os.path.exists(path):
        #download link as png
        response = requests.get(link)
        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)


def create_date_string(blog_publish_date):
    month = blog_publish_date[8:11]
    day = blog_publish_date[5:7]
    year = blog_publish_date[12:16]
    match (month):
        case "Jan":
            month = "January"
        case "Feb":
            month = "February"
        case "Mar":
            month = "March"
        case "Apr":
            month = "April"
        case "May":
            month = "May"
        case "Jun":
            month = "June"
        case "Jul":
            month = "July"
        case "Aug":
            month = "August"
        case "Sep":
            month = "September"
        case "Oct":
            month = "October"
        case "Nov":
            month = "November"
        case "Dec":
            month = "December"
    formatted_date = f"{month} {day}, {year}"
    return formatted_date

def extract_images(html_body, title):
    parser = BeautifulSoup(html_body, 'html.parser')

    #First, create img folder:
    path = f"./archive/{title}/"
    image_folder_path = os.path.join(path, "img")
    if not os.path.exists(image_folder_path):
        os.mkdir(image_folder_path)

    #create png files there
    image_number = 0
    for i in parser.find_all("img"):
        image_path = os.path.join(image_folder_path, f"img_{image_number}.png")
        with open(image_folder_path, "a"):
            pass
        image_number += 1
    
    image_number = 0 #reset img number
    for html_img in parser.find_all("img"):
        print(html_img.get("src"))
        try:
            response = requests.get(html_img.get("src"))
            image_path = os.path.join(image_folder_path, f"img_{image_number}.png")
            with open(image_path, 'wb') as f:
                f.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        image_number += 1

def clean_title_name_for_dir(title):
    invalid_chars = r'[\\/:*?"<>|\0]'
    return re.sub(invalid_chars, "_", title)

def create_html_from_blog(title, desc, date, body):
    html_file = """
    <!doctype html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            <link rel="stylesheet" href="../blog.css">
            <title>TITLE</title>
            <meta charset="UTF-8">
            <meta name="TITLE" content="DESCRIPTION">
        </head>
        <body>
            <h1> TITLE </h1>
            <h3> DESCRIPTION </h3>
            <h5> Originally posted on substack on DATE </h5>
            <div class="blog_post">
                BLOG_BODY
                <a href="/south_bay_journal/home.html"> HOME </a>
            </div>
        </body>
    </html>
    """
    html_file = html_file.replace("TITLE", title)
    html_file = html_file.replace("DESCRIPTION", desc)

    soup = BeautifulSoup(body, 'html.parser')
    for certain_elements in soup(["button"]):
        certain_elements.decompose()
    for div in soup.find_all("div", class_="image-link-expand"):
        div.decompose()
    for div in soup.find_all("div", class_="footnote"):
        div.decompose()
    for a in soup.find_all("a", class_="footnote-anchor"):
        a.decompose()
    for p in soup.find_all("p", class_="button-wrapper"):
        p.decompose()
    #soup.prettify().replace('’', "'")
    html_file = html_file.replace("BLOG_BODY", soup.prettify(formatter="html"))
    #html_file = html_file.replace("LINK", link)
    html_file = html_file.replace("DATE", create_date_string(date))

    title = clean_title_name_for_dir(title)
    path = f"./archive/{title}/"
    os.mkdir(path)
    
    file_name = (title + ".html")
    with open(os.path.join(path, file_name), "w") as f:
        f.write(html_file)


substack_rss_url = "https://southbayjournal.substack.com/feed"
feed = feedparser.parse(substack_rss_url) #need to sanitize
#print(feed.encoding)

count = 0
for i in feed.entries:
    current_item = feed.entries[count]
    blog_title = current_item.title
    blog_description = current_item.description
    blog_publish_date = current_item.published
    blog_link = current_item.links
    html_body = current_item.content

    #print(f"html_body is type {type(html_body)}\n")
    for feedparser_dict in html_body:
       #print(f"feedparser_dict is type {type(feedparser_dict)}\n")
       for key in feedparser_dict:
           #print(f"key is type {type(key)}\n")
           #print(f"feedparser_dict[key] is type {type(feedparser_dict[key])}\n")
           value = feedparser_dict[key]
           #print(f"{key}\n")
           if key == "value":
               #print(f"{value}\n")
               html_body = value
    if (blog_title not in os.listdir("archive/")):
        create_html_from_blog(blog_title, blog_description, blog_publish_date, html_body)
        extract_cover_image(blog_link, blog_title)
        #extract_images(html_body, blog_title) STILL A WORK IN PROGRESS FOR THE FUTURE
    count += 1