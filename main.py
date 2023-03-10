### Create a finished post ###
import os

from reddit import topComments, topPosts
from screenshot import screenshot
from resize import resize

PHOTO_PATH, SCREENSHOT_PATH = 'photos', 'screenshots' # no trailing slashes

# post = topPost()
listOfPosts = topPosts()
print("Here are the top 5 posts:")
for i in range(len(listOfPosts)):
  print('[{}] - {}'.format(i, listOfPosts[i].title))
postInput = input('Which post do you want to use? Enter the number in the [brackets]: ')
print('\nGot it!\n')

post = listOfPosts[int(postInput)]
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