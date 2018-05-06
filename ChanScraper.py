import bs4
import requests
import urllib.request
import os


def download_image(uri, out_file):
    urllib.request.urlretrieve('http://' + uri, out_file)
    return


def get_soup(uri):
    r = requests.get(uri + '.html');
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    return soup


def get_image_name(uri):
    image_name = uri.split('/')[2]
    return image_name


def scrape_chan(uri, folder):
    soup = get_soup(uri)
    images = soup.findAll(attrs={'class':'fileThumb'})

    for i in range(len(images)):
        images[i] = images[i].get('href')[2:]
        image_name = get_image_name(images[i])
        print(str(i+1) + '/' + str(len(images)) ,'downloading:', images[i], 'to', image_name)
        download_image(images[i], folder + '/' + image_name)

    return


def main():
    uri = input("URL: ")
    folder = input("folder: ")
    os.makedirs(folder)
    scrape_chan(uri, folder)


main()
