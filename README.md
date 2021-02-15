# Scraping-Downloading-Bulk-Images
My Client give me a Project in which I have to Scrape and Download the Images of Famous People from this Website: https://www.famousbirthdays.com/  After Scarping I have to Convert every single Image into a 1 sec Video. Actually I have to write a Program that will do this task.   For Scraping and Downloading all the Images I Use Scrapy, OS Module, Requests, Pandas and for converting them into a 1 sec video (as soon as they download), I use Wand, FFmpy, Collections.  It was a long Journey and it was also not an easy task but You know I have Experience of 6+ Years in Python Scraping and all of the other Stuff it was not that hard for me but it was still a long Journey.  I Love to Work with my Client on this Project and Hopefully it was Successfully Done :)

# Instructions
Hi There,

I Hope You are Doing well, Please Read these Instructions to use the script well.

Thank You

Best Regards,

Kaleem Arshad 

IDE or Code Editor:
I recommend you Pycharm IDE or you can also use Visual Studio Code. Dont Forgot to install Python and set it up for use.


Modules to Install:
> Scrapy (write this in terminal): (pip install scrapy)
> Requests (write this in terminal): (pip install requests)
> Scrapy-User-Agents (write this in terminal): (pip install scrapy-user-agents)
> Wand (write this in terminal): (pip install wand)
> FFMPY (write this in terminal): (pip install ffmpy)
> Bs4 (write this in the terminal): (pip install bs4)
> Pandas (write this in the terminal): (pip install pandas)

First, You will Scrape the URLs from sitemap of the webpages and from those you will scrape urls of People Profiles then using those URLs, Scrape the Required Data.

Follow the Following steps:
1) Go to Images_Scraper\Images_Scraper\spiders and Open the (sitemap_scraper.py) file.
2) Just Run it(click on the green play button), it will extract data form the website sitemaps.
3) After, its done you will see a URLs.csv file(ignore it for now) and comment all the lines of this file and close it.
4) Now, Go to Images_Scraper\Images_Scraper\spiders and Open the (Url_scraper.py) file.
>>> Uncomment all the line of the file <<<
5) On line number 9 write the path to the URLs.csv file.
6) To Run it, Open the Terminal in the Images_Scraper folder write (scrapy crawl url -o URLs2.csv) and press ENTER.
7) It will take some time to scrape all the URLs from the "webpages urls in URLs.csv file" and delete the duplicates also and write them into URLs2.csv, this is the final CSV file.
8) Open URLs2.csv file and just remove the first line, save it and close it(it will cause problem).

>>> URLs Scraping is Done, comment all the lines of this file too(it is necessary to prevent confusion for the program) :)


5) After you have Scraped URLs its time to scrape data from those URls, Navigate to (Images_Scraper\Images_Scraper\spiders and Open the (Images_famous_birthdays.py) file).
>>> Uncomment all the line of the file <<<
6) On line number 17 in Images_famous_birthdays.py file, write the path to the URLs2.csv file.
7) On line number 49 in Images_famous_birthdays.py file, write the path where you want to store the scraped and downloaded    data.
8) On line number 68 in Images_famous_birthdays.py file, write the path to white.png file, it will be in the Images_Scraper    folder.
9) On line number 77 in Images_famous_birthdays.py file, write the path to green.mp4 file.
10) All Set, it's time to run the file. Open the terminal in the Images_Scraper folder and write (scrapy crawl images) and press ENTER.

>>> Note: (FOR BOTH(Url_Scraper.py and Images_famous_birthdays.py) SCRIPT) Before Running the script, check that the terminal window is opened in the Images_Scraper folder or directory, it should be opened in that directory otherwise the script will not run.
