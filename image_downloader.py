import urllib.request
import argparse
import textwrap
import os
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Download set of images from list of URLs', prog='Image_downloader',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('Written to help get large image sets for machine learning or '
                                                        'simple Windows theme ideas'))
parser.add_argument('infile', type=str, help='Text file with image URLs')
parser.add_argument('outfile', type=str, help='Output for saved images')
parser.add_argument('num_of_images', nargs='?', type=int, default=None, help='Limit the number of images to '
                                                                             'download from file, if left blank, '
                                                                             'all images will be downloaded')
parser.add_argument('not_pref', nargs='?', type=int, default=5, help='How often to print image download rate')

args = parser.parse_args()


def dnld_images(image_url, image_loc):
    """
    Download image to local folder from url
    :param image_url: URL of image
    :param image_loc: Save location for image
    :return: result of save attempt
    """
    try:
        urllib.request.urlretrieve(image_url, '{}.jpg'.format(image_loc))
    except Exception as error:
        return 'There was an error with image download, {}'.format(error)


with open(args.infile, 'r') as url_set:
    urls = url_set.readlines()

image_no = len(urls)
if args.num_of_images:
    image_no = args.num_of_images
print('Downloading {} images'.format(str(image_no)))

if not os.path.exists(args.outfile):
    os.makedirs(args.outfile)

for idx, url in tqdm(enumerate(urls)):
    dnld_images(url, os.path.join(args.outfile, str(idx)))
    if idx % args.not_pref == 0:
        print('Downloaded {} images so far'.format(str(idx)))
    if idx == args.num_of_images - 1:
        break

print('{} Images Downloaded'.format(image_no))