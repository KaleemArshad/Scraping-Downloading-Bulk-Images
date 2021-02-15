import scrapy
from ..items import ImagesScraperItem
import csv
import requests
import os
from wand.image import Image
import pandas
import ffmpy
from collections import OrderedDict


class ImagesFamousBirthdaysSpider(scrapy.Spider):
    Urls = []
    name = 'images'
    start_urls = []

    # replace '\' with '/' in path
    with open("F:/CODE/Ezra's Script/Images_Scraper/URLs2.csv", 'r')as f:
        data = csv.reader(f)
        for row in data:
            for link in row:
                start_urls.append(link)

    print(len(start_urls))

    def parse(self, response):
        items = ImagesScraperItem()

        src = response.css("img::attr(src)").extract()
        name = response.css("h1::text").get().strip()
        description = response.css("div.bio p").css('::text').extract()
        age = response.css(".icn-age~ a").css("::text").get()

        url_list = []
        with open("F:/CODE/Ezra's Script/Images_Scraper/URLs2.csv", 'r')as f:
            data = csv.reader(f)
            for row in data:
                for link in row:
                    url_list.append(link)

        del url_list[0:2]
        final = url_list
        cur = os.getcwd()
        dire = "F:/CODE/Ezra's Script/Images_Scraper"
        dire2 = "F:/CODE/Ezra's Script/Images_Scraper/URLs2.csv"
        os.remove(dire2)

        os.chdir(dire)
        df = pandas.DataFrame(final)
        df.to_csv('URLs2.csv', index=False)
        os.chdir(cur)

        for s in src:
            if "large-default" not in s:
                if age[:2] == '1 ' or age[:2] == '2 ' or age[:2] == '3 ' or age[:2] == '4 ' or age[:2] == '5 ' or age[:2] == '6 ' or age[:2] == '7 ' or age[:2] == '8 ' or age[:2] == '9 ' or age[:2] == '10' or age[:2] == '11' or age[:2] == '12' or age[:2] == '13' or age[:2] == '14':

                    total_img = len(src)

                    des_list = []
                    final_des = []

                    for line in description:
                        des_list.append(line.strip())

                    try:
                        separator = ' '
                        join_line = separator.join(des_list)
                        final_des.append(join_line)
                    except:
                        pass

                    curr_dir = os.getcwd()
                    try:
                        # replace '\' with '/' in path
                        os.chdir("F:/Images/Age 1-14")
                        os.mkdir(os.path.join(os.getcwd(), f'{name}'))

                    except:
                        pass

                    os.chdir(os.path.join(os.getcwd(), f'{name}'))
                    img_no = 1

                    for source in src:
                        with open(f"{name} {img_no}-{total_img}.png", 'wb') as f:
                            img_no += 1
                            img = requests.get(source)
                            f.write(img.content)

                    directory = os.getcwd()
                    for image in os.listdir(directory):
                        if image.endswith('.png'):
                            print('img founded')
                            with Image(filename="F:/white.png") as mark:
                                mark.sample(1920, 1080)
                                print('white done')
                                with Image(filename=image) as i:
                                    i.sample(775, 775)
                                    with mark.clone() as cl:
                                        cl.watermark(i, 0.0, 545, 160)
                                        cl.save(filename=image)
                            png = image
                            vid = "F:/My Data/green.mp4"
                            out = image.replace('.png', '.mp4')
                            ff = ffmpy.FFmpeg(
                                inputs=OrderedDict([(png, None), (vid, None)]),
                                outputs={out: "-filter_complex [1:v]colorkey=0x00ff00:0.5:0[ckout];[0:v][ckout]overlay[out] -map [out] -map 1:1"})
                            ff.run()

                    des_set = set(final_des)
                    Description = open('description.txt', 'a')
                    for line in des_set:
                        Description.write(f"{line}'\n'")
                    Description.close()

                    os.chdir(curr_dir)

                elif age[:2] == '15' or age[:2] == '16' or age[:2] == '17' or age[:2] == '18':
                    total_img = len(src)

                    des_list = []
                    final_des = []

                    for line in description:
                        des_list.append(line.strip())

                    try:
                        separator = ' '
                        join_line = separator.join(des_list)
                        final_des.append(join_line)
                    except:
                        pass

                    curr_dir = os.getcwd()
                    try:
                        # replace '\' with '/' in path
                        os.chdir("F:/Images/Age 15-18")
                        os.mkdir(os.path.join(os.getcwd(), f'{name}'))

                    except:
                        pass

                    os.chdir(os.path.join(os.getcwd(), f'{name}'))
                    img_no = 1

                    for source in src:
                        with open(f"{name} {img_no}-{total_img}.png", 'wb') as f:
                            img_no += 1
                            img = requests.get(source)
                            f.write(img.content)

                    directory = os.getcwd()
                    for image in os.listdir(directory):
                        if image.endswith('.png'):
                            print('img founded')
                            with Image(filename="F:/white.png") as mark:
                                mark.sample(1920, 1080)
                                print('white done')
                                with Image(filename=image) as i:
                                    i.sample(775, 775)
                                    with mark.clone() as cl:
                                        cl.watermark(i, 0.0, 545, 160)
                                        cl.save(filename=image)
                            png = image
                            vid = "F:/My Data/green.mp4"
                            out = image.replace('.png', '.mp4')
                            ff = ffmpy.FFmpeg(
                                inputs=OrderedDict([(png, None), (vid, None)]),
                                outputs={out: "-filter_complex [1:v]colorkey=0x00ff00:0.5:0[ckout];[0:v][ckout]overlay[out] -map [out] -map 1:1"})
                            ff.run()

                    des_set = set(final_des)
                    Description = open('description.txt', 'a')
                    for line in des_set:
                        Description.write(f"{line}'\n'")
                    Description.close()

                    os.chdir(curr_dir)

                else:

                    total_img = len(src)

                    des_list = []
                    final_des = []

                    for line in description:
                        des_list.append(line.strip())

                    try:
                        separator = ' '
                        join_line = separator.join(des_list)
                        final_des.append(join_line)
                    except:
                        pass

                    curr_dir = os.getcwd()
                    try:
                        # replace '\' with '/' in path
                        os.chdir("F:/Images/Age 18+")
                        os.mkdir(os.path.join(os.getcwd(), f'{name}'))

                    except:
                        pass

                    os.chdir(os.path.join(os.getcwd(), f'{name}'))
                    img_no = 1

                    for source in src:
                        with open(f"{name} {img_no}-{total_img}.png", 'wb') as f:
                            img_no += 1
                            img = requests.get(source)
                            f.write(img.content)

                    directory = os.getcwd()
                    for image in os.listdir(directory):
                        if image.endswith('.png'):
                            print('img founded')
                            with Image(filename="F:/white.png") as mark:
                                mark.sample(1920, 1080)
                                print('white done')
                                with Image(filename=image) as i:
                                    i.sample(775, 775)
                                    with mark.clone() as cl:
                                        cl.watermark(i, 0.0, 545, 160)
                                        cl.save(filename=image)
                            png = image
                            vid = "F:/My Data/green.mp4"
                            out = image.replace('.png', '.mp4')
                            ff = ffmpy.FFmpeg(
                                inputs=OrderedDict([(png, None), (vid, None)]),
                                outputs={out: "-filter_complex [1:v]colorkey=0x00ff00:0.5:0[ckout];[0:v][ckout]overlay[out] -map [out] -map 1:1"})
                            ff.run()

                    des_set = set(final_des)
                    Description = open('description.txt', 'a')
                    for line in des_set:
                        Description.write(f"{line}'\n'")
                    Description.close()

                    os.chdir(curr_dir)
            else:
                pass

        items['src'] = src
        items['name'] = name
        items['description'] = description

        yield items
