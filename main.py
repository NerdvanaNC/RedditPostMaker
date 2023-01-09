### Create a finished post ###
import os

from reddit import topComments, topPost
from screenshot import screenshot
from resize import resize

PHOTO_PATH, SCREENSHOT_PATH = 'photos', 'screenshots' # no trailing slashes

post = topPost()
comments = topComments(post)

print('Using Post: {} - {}'.format(post.title, post.id))

print(resize(screenshot(post.url, post.id, 'post')))
for comment in comments:
  print(resize(screenshot(comment.permalink, comment.id, 'comment')))

# update completed posts log
with open('done_posts.txt', 'a') as file:
  file.write('{}\n'.format(post.id))

# move all files to folder
post_folder = '{}/post_{}'.format(SCREENSHOT_PATH, post.id)
os.mkdir(post_folder)
for filename in os.listdir(SCREENSHOT_PATH):
  if '.png' in filename:
    os.rename('{}/{}'.format(SCREENSHOT_PATH, filename), '{}/{}'.format(post_folder, filename))