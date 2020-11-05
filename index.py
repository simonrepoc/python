from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


browser = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr")

browser.implicitly_wait(5)


browser.get('https://www.instagram.com/')


sleep(2)


username_input = browser.find_element_by_css_selector("input[name='username']")

password_input = browser.find_element_by_css_selector("input[name='password']")


username_input.send_keys("___cipher_____")

password_input.send_keys("Simon@macha2")


login_button = browser.find_element_by_xpath("//button[@type='submit']")

login_button.click()


sleep(5)

hashtag_list = ['explore']
tag_list = ['followme','follow','followforfollow','followback','followers','follow4follow','followher','follower','followhim','followall','followbackteam','followbackalways','follows','followgram','followalways','tagblender','followmefollowyou','following','followstagram','follownow','ifollowback','followus','followmeback','followforlike','followmeplease','followshoutoutlikecomment','followbackinstantly','f4f','ifollo','followyou']

prev_user_list = [] #- if it's the first time you run it, use this line and comment the two below
#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    #browser.get('https://www.instagram.com/'+ hashtag_list[tag] + '/')
    browser.get('https://www.instagram.com/explore/tags/'+ tag_list[tag] + '/')
    sleep(5)
    first_thumbnail = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[1]')
    
    first_thumbnail.click()
    sleep(randint(1,2))    
    try:        
        for x in range(1,200):
            username = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
            
            if username not in prev_user_list:
                # If we already follow, do not unfollow
                if browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[2]'):

                    # Liking the picture
                    button_like = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]')
                    
                    button_like.click()
                    likes += 1
                    sleep(randint(5,5))

                    # Comments and tracker
                    comm_prob = randint(1,10)
                    print('{}_{}: {}'.format(hashtag, x,comm_prob))
                    if comm_prob > 7:
                        comments += 1
                        browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]').click()
                        comment_box = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')

                        if (comm_prob < 7):
                            comment_box.send_keys('Really cool!')
                            sleep(1)
                        elif (comm_prob > 6) and (comm_prob < 9):
                            comment_box.send_keys('Nice work :)')
                            sleep(1)
                        elif comm_prob == 9:
                            comment_box.send_keys('Nice gallery!!')
                            sleep(1)
                        elif comm_prob == 10:
                            comment_box.send_keys('So cool! :)')
                            sleep(1)
                        # Enter to post comment
                        comment_box.send_keys(Keys.ENTER)
                        sleep(randint(5,5))

                # Next picture
                browser.find_element_by_link_text('Next').click()
                sleep(randint(5,5))
            else:
                browser.find_element_by_link_text('Next').click()
                sleep(randint(5,5))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue
for n in range(0,len(hashtag_list)):
    prev_user_list.append(hashtag_list[n])
    
updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
