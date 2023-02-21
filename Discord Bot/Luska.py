import discord
import random
import requests
import json
import time



client = discord.Client()



music_list = ['https://open.spotify.com/track/3PJMsxg6rz9FOo6xNiASXz?si=51ab154212324e52', 'https://open.spotify.com/track/4Iv4KgHBWsFhLNXXMvyUmb?si=9f5d377965bd4661', 'https://open.spotify.com/track/1YQWosTIljIvxAgHWTp7KP?si=ad6fd13a058f41a8', 'https://open.spotify.com/track/7DUGRxCf9NFJffb5Eei8Ar?si=2832f8edceb8434b', 'https://open.spotify.com/track/4rmCI9VWrwrJTJ8XQ80BMN?si=7ee28eac1a174bb7', 
'https://open.spotify.com/track/5izUwBbaQqfpTm9eYKTYFf?si=6d78183d6abe417f', 'https://open.spotify.com/track/3VtdvomG4MZVbmZ1V5Ys2k?si=8f43b319bc9e4d58', 'https://open.spotify.com/track/3DNRdudZ2SstnDCVKFdXxG?si=0b3a78b438634c2a', 'https://open.spotify.com/track/6WY4wvlmgccWapnIg14Vy0?si=c4842bef01924a09', 'https://open.spotify.com/track/6ZFbXIJkuI1dVNWvzJzown?si=282d57d6564e4b45', 'https://open.spotify.com/track/1V3EBMIULmc7H3Uu68wWpE?si=2d2c1500311d41e1', 
'https://open.spotify.com/track/34b3a3Pz9Jlz0092LMyNAB?si=5e8090e74887451f', 'https://open.spotify.com/track/7hzgk557YLr0722EFkmp9Z?si=38593c09c15c4537', 'https://open.spotify.com/track/57IHG8x8BiqKHanYQk92ji?si=59b0163b89ce4eaf', 'https://open.spotify.com/track/2M9ro2krNb7nr7HSprkEgo?si=94be9094f64d4e12', 'https://open.spotify.com/track/6Rqn2GFlmvmV4w9Ala0I1e?si=95c0bcee8ff94ea0', 'https://open.spotify.com/track/02a8cGumnKuEPgoCzmalJp?si=b0fb3f743a204ad2', 
'https://open.spotify.com/track/5GjCLHeNC77C0IbTkOU3tI?si=683867f301d5433d', 'https://open.spotify.com/track/1uOKN6ZbtEaLI5aLsBNRLe?si=503e98f532ad412d', 'https://open.spotify.com/track/1k1Bqnv2R0uJXQN4u6LKYt?si=759f05c8b2cd427c', 'https://open.spotify.com/track/13toFl1UwJPsRxDiD9jgtn?si=a28be1f616a34eef', 'https://open.spotify.com/track/3uCkIqD0VzQUijbs8WIizs?si=4ed9ca80e2d24f7c', 'https://open.spotify.com/track/6U03Orwr5Dxt8jahLnQpYV?si=ff4663670461407e', 
'https://open.spotify.com/track/52Bg6oaos7twR7IUtEpqcE?si=05689cc9e3a646be', 'https://open.spotify.com/track/6Jv7kjGkhY2fT4yuBF3aTz?si=0758fc7f0059432b', 'https://open.spotify.com/track/7LZgdL0MxiElfaKZbuuE4l?si=d1d0c38a967149c5', 'https://open.spotify.com/track/3BQHpFgAp4l80e1XslIjNI?si=9886590341204e59', 'https://open.spotify.com/track/612VcBshQcy4mpB2utGc3H?si=740cf68a56494cdf', 'https://open.spotify.com/track/3BEZCNZSmVv30vsMNSOCri?si=d5b590180a7d4fee',
'https://open.spotify.com/track/2KAQMHnDLzc3jr9tlLSJIC?si=7c84a7826b524229', 'https://open.spotify.com/track/5MxNLUsfh7uzROypsoO5qe?si=7449a6b1dcd74fd8', 'https://open.spotify.com/track/5O4erNlJ74PIF6kGol1ZrC?si=effe3e378f3a485a', 'https://open.spotify.com/track/7BfW1eoDh27W69nxsmRicb?si=db165afc02cc42cc', 'https://open.spotify.com/track/2RcanAJpudPNDkyIe9DzKS?si=6042c32b22bd4160', 'https://open.spotify.com/track/4euxFlxLWVGmZZLyYARTyE?si=3c720b10088b49a2',
'https://open.spotify.com/track/0y8h1AJzI4y7UxzX5xdVpo?si=966dc56204ea4f9a', 'https://open.spotify.com/track/0KOE1hat4SIer491XKk4Pa?si=d5fdc9363f884870', 'https://open.spotify.com/track/57IHG8x8BiqKHanYQk92ji?si=2d6fdc83f2f14918', 'https://open.spotify.com/track/0ofHAoxe9vBkTCp2UQIavz?si=3d18c6cf44934a56', 'https://open.spotify.com/track/7oOOI85fVQvVnK5ynNMdW7?si=216bb6b4a53c487b', 'https://open.spotify.com/track/13UqaNF8STsJSGKxd12rmy?si=1396fe4314fd4244',
'https://open.spotify.com/track/4t87dWb7q5e7TtWMFeV0Z8?si=7ee6e0850eeb4478', 'https://open.spotify.com/track/4MqFHxNM8uM7UEW4t56nzU?si=e9927ab16f2e40c0', 'https://open.spotify.com/track/2aoo2jlRnM3A0NyLQqMN2f?si=451e0518a9f14256', 'https://open.spotify.com/track/4xHWH1jwV5j4mBYRhxPbwZ?si=61129df4915241b9', 'https://open.spotify.com/track/32dnKMni3I3gwUbWp4mi45?si=c8915eefe0114c76', 'https://open.spotify.com/track/7aE5WXu5sFeNRh3Z05wwu4?si=c455416af52c4767',
'https://open.spotify.com/track/10FLYqpqDN4uo6eWtD6WEB?si=7fa97ba44039492e', 'https://open.spotify.com/track/7wCmS9TTVUcIhRalDYFgPy?si=ea88130bf6a346ca', 'https://open.spotify.com/track/2Aqc48sn8He26hmTvQ2BMj?si=4b1fa51656244a47', 'https://open.spotify.com/track/3cEVhx8rkM0FlETJFFpxoF?si=114cce842a1e44bb', 'https://open.spotify.com/track/0MsrWnxQZxPAcov7c74sSo?si=e524cfe5fa514bde', 'https://open.spotify.com/track/5quv9YDjbVlXddPEk08N0H?si=318882888ec54467',
'https://open.spotify.com/track/5k7RUvywwUAl7Dq6qEXR8c?si=d322fcc4fb134800', 'https://open.spotify.com/track/31AOj9sFz2gM0O3hMARRBx?si=383c35f573bb40de', 'https://open.spotify.com/track/40riOy7x9W7GXjyGp4pjAv?si=8210729ee40f4eba', 'https://open.spotify.com/track/2NVmpcUm2FUUQ04FlWIj2q?si=0935d495ee2f4d80', 'https://open.spotify.com/track/6WBOioUUtvTyvUK5ydumGZ?si=817372413a7c4be7', 'https://open.spotify.com/track/6wM3sxSUsKDhBqeui5FDAh?si=c1de1aa85b9d425e',
'https://open.spotify.com/track/4Uiw0Sl9yskBaC6P4DcdVD?si=7cc5718ad8e44e0c', 'https://open.spotify.com/track/5gz38AxRkD6Ywxd4fr2pLj?si=cc16295ed5054953', 'https://open.spotify.com/track/3SVAN3BRByDmHOhKyIDxfC?si=97d0b6c7b1094fee', 'https://open.spotify.com/track/2j2n2VGCMIyFaQ6ToEC0Cy?si=5b5fbad9042f469e', 'https://open.spotify.com/track/5olWalQH1oVza5D6xJg4oX?si=0f9d5e797b9e4e02', 'https://open.spotify.com/track/5k7VKj1Xwy5DjO4B0PdAOb?si=cfb498206a324eba',
'https://open.spotify.com/track/4Iyo50UoYhuuYORMLrGDci?si=a4431edc7abc4274', 'https://open.spotify.com/track/4eruRiSfDY1jdT03hjyi0i?si=6d5d19eb23604fb5', 'https://open.spotify.com/track/2sW8fmnISifQTRgnRrQTYW?si=c9a376fdfbd24771', 'https://open.spotify.com/track/7uv632EkfwYhXoqf8rhYrg?si=62c7f37326454c9b', 'https://open.spotify.com/track/0GN3fXUdsTHeUg50xfDS0V?si=f214282a0f764e89', 'https://open.spotify.com/track/0F0imGVd7KnvQPkBmVtPo9?si=73ff0966e5314801',
'https://open.spotify.com/track/1ZgMsA55GIY7ICkQh5MILA?si=9218c801213c4102', 'https://open.spotify.com/track/5ADsYkqsZvaPeoPqEHYr2X?si=d6f13324217a4bf9']

film_list = ['https://boxd.it/v2uy', 'https://boxd.it/mxuc', 'https://boxd.it/hTha', 'https://boxd.it/jkPq', 'https://boxd.it/azpY', 'https://boxd.it/hHUa', 'https://boxd.it/hDNu', 'https://boxd.it/hNVe', 'https://boxd.it/fcFu', 'https://boxd.it/d6bE', 'https://boxd.it/aNGk', 'https://boxd.it/cUqs', 'https://boxd.it/dSQU', 'https://boxd.it/8H5e', 'https://boxd.it/4VZ8', 'https://boxd.it/5RFA', 'https://boxd.it/4pD0', 'https://boxd.it/7Uau', 'https://boxd.it/7bQA',
'https://boxd.it/4JQI', 'https://boxd.it/4E5i', 'https://boxd.it/2p2E', 'https://boxd.it/4sr2', 'https://boxd.it/2cCk', 'https://boxd.it/2Y3s', 'https://boxd.it/2Emk', 'https://boxd.it/dVI', 'https://boxd.it/1skk', 'https://boxd.it/1U82', 'https://boxd.it/21ew', 'https://boxd.it/1Y2i', 'https://boxd.it/1Mse', 'https://boxd.it/2a3M', 'https://boxd.it/2a2a', 'https://boxd.it/1blA' , 'https://boxd.it/1UlA', 'https://boxd.it/2b1i', 'https://boxd.it/1SZe', 'https://boxd.it/27q4',
'https://boxd.it/29Ts', 'https://boxd.it/1U9E']

series_list = ['https://www.imdb.com/title/tt0290988/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt0386676/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt3398228/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt0903747/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt3032476/?ref_=ext_shr_lnk', 
'https://www.imdb.com/title/tt3592032/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt0417299/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt2560140/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt0367279/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt0098904/?ref_=ext_shr_lnk', 
'https://www.imdb.com/title/tt2098220/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt4158110/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt5753856/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt4288182/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt0098936/?ref_=ext_shr_lnk', 
'https://www.imdb.com/title/tt0306414/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt0141842/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt2356777/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt7366338/?ref_=ext_shr_lnk', 'https://www.imdb.com/title/tt0944947/?ref_=ext_shr_lnk', 
'https://www.imdb.com/title/tt11126994/?ref_=ext_shr_lnk']

video_list = ['https://youtu.be/H4dGpz6cnHo', 'https://youtu.be/1iUf1FP-pS8', 'https://youtu.be/uGgI6qsg_kc', 'https://youtu.be/t0cmqwyl5iA', 'https://youtu.be/ao6hk8qQ__c', 'https://youtu.be/sGteJAB-OGA', 'https://youtu.be/FHBFwqo7MmM', 'https://youtu.be/n2yJw8mc2EA', 'https://youtu.be/cSDCzm_srfc',
'https://youtu.be/iVSJsjDOMfg', 'https://youtu.be/1Rx_p3NW7gQ', 'https://youtu.be/E8H-67ILaqc', 'https://youtu.be/x--yddOolRQ', 'https://youtu.be/g3AHqcinzZ4', 'https://youtu.be/GrHfWKeTDEI', 'https://youtu.be/Z4UD8J9p8F0', 'https://youtu.be/5R1ITMpChio', 'https://youtu.be/d9NF2edxy-M', 'https://youtu.be/tDxKhiJfgYk',
'https://youtu.be/fXgY54oVWHI', 'https://youtu.be/keWY_mCeqR8', 'https://youtu.be/HB3K5HY5RnE', 'https://youtu.be/oFLpMikkv60', 'https://youtu.be/PXVOFueg7qI', 'https://youtu.be/BbTf-nIxU5A', 'https://youtu.be/bq9X-XOu56E', 'https://youtu.be/sG1IH1vCvko', 'https://youtu.be/LcbTSLZl9hs',
'https://youtu.be/rbE53XUtVw0', 'https://youtu.be/Hf0b_-hVBS4', 'https://youtu.be/vgYZMIU0IlM', 'https://youtu.be/OdZGvMEeNLw', 'https://youtu.be/wEGR_PHKK9g', 'https://youtu.be/9CDT0cwGKxY', 'https://youtu.be/ezPfuzgh6m0', 'https://youtu.be/YwR1LWDUCwM', 'https://youtu.be/qFfnlYbFEiE', 'https://youtu.be/vlt_PnEbabU',
'https://youtu.be/p4cJv6s_Yjw', 'https://youtu.be/yIdKbSeAueY', 'https://youtu.be/fYAQHKk6L0U', 'https://youtu.be/Sfw3vKFZ43U', 'https://youtu.be/x5Swa9CYgRk', 'https://youtu.be/rFtYzVJcWyA', 'https://youtu.be/DWuAn6C8Mfc', 'https://youtu.be/1TiIgm0xY0A', 'https://youtu.be/s_TanvVfYKo', 'https://youtu.be/_CEK34jmpdk',
'https://youtu.be/aMXzLhbWtmk', 'https://youtu.be/0GKHaQ2MpuI', 'https://youtu.be/3U4yDkvRjvs', 'https://youtu.be/tixOyiR8B-8', 'https://youtu.be/Clg7rQB6H2U', 'https://youtu.be/w77zPAtVTuI', 'https://youtu.be/jDqn1ySDF1o', 'https://youtu.be/bRM2Gn9nU7Q', 'https://youtu.be/e5rKKL37kHQ', 'https://youtu.be/e5rKKL37kHQ',
'https://youtu.be/IKFr6m950cQ', 'https://youtu.be/OeTVyL8swZg', 'https://youtu.be/3VSlj34f2aQ', 'https://youtu.be/YsfS7mQBHzk', 'https://youtu.be/cUFVR5sgbt0']

image_list = ['https://pin.it/1ql0XTB', 'https://pin.it/35bMMUI', 'https://pin.it/13MBsxz', 'https://pin.it/3wIVyd3', 'https://pin.it/7CCtUzj', 'https://pin.it/2BHhNyy', 'https://pin.it/2dvGcnq', 'https://pin.it/1ThWGUr', 'https://pin.it/34mYLu3', 'https://pin.it/3AOCX98', 'https://pin.it/7cMwMvz',
'https://pin.it/6mMlWgf', 'https://pin.it/40ReWRc', 'https://pin.it/5LU79gD', 'https://pin.it/4G4W3l8', 'https://pin.it/4xq3arG', 'https://pin.it/5N2SirX', 'https://pin.it/4HdHHVm', 'https://pin.it/3XBxr00', 'https://pin.it/3DweYLA', 'https://pin.it/6hC7ZkQ', 'https://pin.it/1gQZeti',
'https://pin.it/Ol8cwx7', 'https://pin.it/3asYpOM', 'https://pin.it/1s3nIBE', 'https://pin.it/7FwWUMe', 'https://pin.it/7vbIwoe', 'https://pin.it/4p5gQ46', 'https://pin.it/5CV6nZ5', 'https://pin.it/2eeoKgx', 'https://pin.it/55dx9Lg', 'https://pin.it/7pFbKZQ', 'https://pin.it/51en89s',
'https://pin.it/EtLJSsb', 'https://pin.it/2v9xuq8', 'https://pin.it/2TLm0VA', 'https://pin.it/5RJLPkd', 'https://pin.it/5Hskx52', 'https://pin.it/3dM4f2A', 'https://pin.it/5WFquUw', 'https://pin.it/6JWYD4i', 'https://pin.it/3XlNTLh', 'https://pin.it/1gvXPzj', 'https://pin.it/5TQ1Aq7',
'https://pin.it/5KEk7dy', 'https://pin.it/2E3nZ34', 'https://pin.it/6kyjekA', 'https://pin.it/IuzKLhJ', 'https://pin.it/21SPLix', 'https://pin.it/3b0g0Jg', 'https://pin.it/1DcYrvS', 'https://pin.it/7yobbwJ', 'https://pin.it/3NdHFdM', 'https://pin.it/3MCjvH1', 'https://pin.it/1xG2CAf',
'https://pin.it/4wNMoEj', 'https://pin.it/1HidRmV', 'https://pin.it/3zCEEDg', 'https://pin.it/R43eJkp', 'https://pin.it/7IFqbnU', 'https://pin.it/2GwiLq8', 'https://pin.it/6RDDFYJ', 'https://pin.it/1OTNNSK', 'https://pin.it/2T5byi1', 'https://pin.it/6uULYcT', 'https://pin.it/3I2Jdqq',
'https://pin.it/7psIIRP', 'https://pin.it/3f9TYfN', 'https://pin.it/5K8pNv3', 'https://pin.it/1eTS5lz', 'https://pin.it/2Uk3IpO', 'https://pin.it/7HCwMJq', 'https://pin.it/4iDXcVd', 'https://pin.it/6Fw8y30', 'https://pin.it/3TMEXIk', 'https://pin.it/1LaddF5', 'https://pin.it/1QRZHAX',
'https://pin.it/1CU9hcN', 'https://pin.it/6qiJtyD', 'https://pin.it/5fkYp2n', 'https://pin.it/7dvmcFP', 'https://pin.it/2lk9FgA']



hru_ans = ['I\'m gooooood', 'I am amazing!!', 'I\'m decent', 'I AM GREAT, HBU?', 'I\'m well, thanks for asking', 'I\'m ok...', 'Ik ben goed', 'Met mij gaat het goed en met jou?']

dm_list = ['We have already started the process of sending your order.\nThe order DS320Y9 - **Tompouce (250g) x20** from **Driel** was received and processed by us.\nWe plan to deliver **Tompouce (250g) x20** within 3 working days.', 'Congratulations!\nYou\'ve won a $1,000 gift card from **Big Bazar**.\nGo to http://bit.ly/definitelynotvirus tp to claim your gift card.', 
':smirk:', 'Hi it\'s me Franky de Jong, I need $965,50 to pay for a taxi to go to practice.']

bot_intro = '**• • • • • • • • • •  L U S K A  • • • • • • • • • •**\n\n\nHello! My name is **Luska** and I\'m  a bot.\n\nI was created for the sole purpose of entertaining two amazing friends, a dolphin and a turtle.\n\n\nI\'m still in development butttt (dolphin\'s voice), these are some available __***commands***__ I have:\n\n> `-dm ` you may receive a direct message from me\n> `-inspire ` I\'ll share an inspirational quote\n\n> `-random music  ` I\'ll\n> `-random film   ` give\n> `-random series ` a\n> `-random video  ` random\n> `-random image  ` recommendation\n\n> `-hangman ` Do you want to play Hangman?\n> `-decide ` I can help undecided people to actually decide something\n> `-study ` In case you need to remind somone it\'s study time\n> `-shower` One of you is smelly and needs to go take a shower\n> `-soccer` Dolphin is about to destroy everyone in the field\n> `-hug ` Give someone a hug :)\n> `-rules ` Dolphin and Turtle **Rules**\n> `-reminder ` I help you remind something\n\n\n||Luska Bot :tm: is a registered trademark.\nUnauthorized use may result in a fine or/and legal action.\nLuska Bot :copyright:\nAll users must be over 13 years of age.\nPlease contact __*turtlesanddolphinsweee@gmail.com*__ for possible questions||\n\nAlrightyyy (turtle\'s voice), use me with due moderation and I hope you enjoy me.\n\n\n**• • • • • • • • • •  L U S K A  • • • • • • • • • •**'

all_rules = '> 1. Be honest with each other\n> 2. Always listen to rule number 1\n> 3. It\'s not allowed to be sad while being friends with Luca/Jiska\n> 4. School is important and we need to push each other\n\n*school\'s important, but it isn\'t the most important thing* :)'

weeee_msg = ['**Weeeeeeeeee**', '*Weeeeeee*', '|| Weeeeeeeeeeeeeeeeeeeeeeeeeeeeeee ||', 'Weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 
'**WeeeeEEEeeEEeeEEEEEEEeeeeEEEeee**', '**Weee day** *also refered to as * **The Day of the Weeee** *is celebrated on 20th August*']

hug_gifs = ['https://tenor.com/view/covid-meme-cute-gif-23513805', 'https://tenor.com/view/virtual-hug-gif-19143145', 'https://tenor.com/view/reencuentros-reencuentro-de-amigos-gif-25017874', 'https://tenor.com/view/gif-gif-19491993', 'https://tenor.com/view/matt-hug-hugs-hug-funny-hug-love-hug-gif-26411239', 'https://tenor.com/view/apapacho-hug-love-boy-girl-gif-5731084',
'https://tenor.com/view/leatylrs-friends-gif-24216492', 'https://tenor.com/view/i-love-you-very-much-happy-congratulations-congrats-hug-hard-gif-17232039', 'https://tenor.com/view/travis-band-music-hugs-hugging-gif-22440438', 'https://tenor.com/view/dog-hug-bff-best-friend-friend-gif-17527097', 'https://tenor.com/view/cat-kitten-kitty-kiss-cute-gif-5695555']

study_gifs = ['https://tenor.com/view/the-big-bang-theory-jim-parsons-sheldon-cooper-study-studying-gif-4469265', 'https://tenor.com/view/reactions-funny-dance-studying-the-zone-gif-3554133', 'https://tenor.com/view/reading-big-eyed-wide-eyes-baby-cute-gif-15767856', 'https://tenor.com/view/boss-baby-tired-sleepy-exhausted-working-gif-11373892', 'https://tenor.com/view/k-on-yui-studying-homework-anime-gif-16480285',
'https://tenor.com/view/read-book-study-funny-standing-on-one-foot-gif-12033367', 'https://tenor.com/view/sleepy-reading-sleeping-studying-struggle-gif-8677342', 'https://tenor.com/view/studying-windy-anime-gif-15313949', 'https://tenor.com/view/dog-sleepy-studying-glasses-gif-15618692', 'https://tenor.com/view/studying-assignment-crying-little-girl-school-problems-gif-17358705', 'https://tenor.com/view/school-boy-friend-math-numbers-gif-24316387',
'https://tenor.com/view/black-kid-focus-thinking-at-work-hmm-gif-16917389', 'https://tenor.com/view/business-cat-working-cat-boss-angry-gif-13655998']

study_msg = ['**IT\'S TIME TO STUDYYYYY** :nerd:', '**Stop what you\'re doing and... it\'s study time** :sunglasses:', '**GOOOOO STUDYYYYYYYYYY**', '**I think it\'s time to study** :face_exhaling:', '**S T U D Y   T I M E**', 'study time ig ¯\_(ツ)_/¯']

soccer_msg = ['**soccer practice babyyyyyy**', '**sorry cant\'t do anything rn, bcs it\'s** __**SOCCER**__ **TIME** :sunglasses:', '**Jiska has to go destroy the other team real quick**']

soccer_gifs = ['https://tenor.com/view/nufc-newcastle-united-allan-saintmaximin-gif-25468886', 'https://tenor.com/view/skills-football-turning-ouch-slipped-gif-16611333', 'https://tenor.com/view/tenor-gif-19905228', 'https://tenor.com/view/soccer-pain-hair-girl-gif-13284257', 'https://tenor.com/view/michy-batshuayi-michy-batshuayi-dumb-stupid-gif-21629492', 'https://tenor.com/view/football-soccer-fail-foul-flop-gif-21047233', 
'https://tenor.com/view/fifa-dance-fifa-celebration-annoying-celebration-funny-dance-gif-26762423', 'https://tenor.com/view/messi-balon-de-oro-soccer-player-slide-gif-15709466', 'https://tenor.com/view/soccer-slide-geico-gif-12314027']

shower_msg = ['**it\'s shower time babyyyyyy**', '**SHOWERRRRR**', '**don\'t talk to me right now, I\'m busy**', '**Wanna shower?** :smirk:']

shower_gifs = ['https://tenor.com/view/singing-shower-bath-singing-in-the-shower-pocket-full-of-sunshine-gif-15384814', 'https://tenor.com/view/shower-cat-shower-cat-dm4uz3-water-gif-18374543', 'https://tenor.com/view/haha-funny-come-here-curtain-lol-gif-15046829', 'https://tenor.com/view/bath-time-dog-cute-puppy-pet-gif-16809303', 'https://tenor.com/view/dog-bath-chillin-give-the-dog-a-bath-gif-15106686', 'https://tenor.com/view/shower-showering-shaving-shaving-cream-full-body-shaving-gif-3541845']

hangman_game_words = ['plane', 'frikandelbroodje', 'dolphin', 'turtle', 'portugal', 'netherlands', 'popcorn', 'socks', 'smelly', 'jiska', 'luca', 'void', 'bed', 'utrecht', 'sintra', 'driel', 'tompouce', 'pringles', 'arnhem', 'linux', 'messi', 'samsung', 'weee']
hangman_game_hints = {'plane': ['it has wings', 'Luca doesn\'t really like to \'use\' them', 'it\'s big, heavy and fast'], 'frikandelbroodje': ['it\'s yummy', 'it\'s a funny word', 'it\'s tasty :smirk:'], 'dolphin': ['it\'s an animal', 'Luca really really likes them','an aquatic mammal'],
'turtle': ['it\'s an animal', 'Jiska really really likes \'it\'', 'reptiles that like to swim'], 'portugal': ['it\'s a country', 'good weather + beach + nature + sea + Luca'], 'netherlands': ['it\s a country', 'UTRECHTTTTTT', 'GO VITESSE GO!'], 'popcorn': ['we prefer them sweet :wink:', 'a variety of corn kernel which expands and puffs up when heated', 'it\s associated with going to the movies'], 
'socks': ['Jiska reallyyyy likes to \'use\' them', 'Jiska has them but they\'re smelly :wink:', 'Jiska has 100 of them in the same color'], 'smelly': ['Jiska socks :smirk:', 'Jiska heeft stinkende voeten'], 'jiska': ['Luca\s fav person', 'it\'s a person', 'Luca absolutly adore this person with all of his heart'],
'luca': ['it\'s a person', 'jiska likes to make fun of this person'], 'void': ['Jiska playing MC be like', 'someplace dark and distant'], 'bed': ['jiska loves laying on it', 'it\'s super comfy', 'sleepy jiska'], 'utrecht': ['Luca sister', 'Rabobank', '30 minutes :smirk:'], 
'sintra': ['hometown of someone', 'it\'s a place'], 'driel': ['hometown of someone', 'it\'s a place'], 'tompouce': ['it\'s a pastry', 'it\'s yummy', 'jiska eats a lot of them while Luca don\'t :('], 'pringles': ['PAPRIKAAAAA', 'they\'re stored in a can', 'they\'re a yummy salty snack'], 
'arnhem': ['VITESSE!!!!', 'HAN'], 'linux': ['an open-source operating system', 'Luca uses it a lot', 'windows sucks'], 'messi': ['*the* GOAT', 'Argentina', 'number: 10'], 'samsung': ['South Korean multinational electronics corporation headquartered in Yeongtong-gu, Suwon, South Korea.', 'Galaxy', 'J5 2016/2017 and now A12 A13 xD'], 
'weee': ['20th august :smirk:', 'Dolphin and Turtle\'s catchword']}



def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote


def get_word():
    return random.choice(hangman_game_words)

def get_hidden_word(ww):
    aux_word = ''
    for i in range(len(ww)):
        aux_word += '?'
    return aux_word

def get_image(tt):
    if tt == 6:
        return '**- - - -**\n  O\n /|\\\n  /\\\n**- - - -**'
    elif tt == 5:
        return '**- - - -**\n  O\n /|\\\n  /\n**- - - -**'
    elif tt == 4:
        return '**- - - -**\n  O\n /|\\\n\n**- - - -**'
    elif tt == 3:
        return '**- - - -**\n  O\n /|\n\n**- - - -**'
    elif tt == 2:
        return '**- - - -**\n  O\n /\n\n**- - - -**'
    elif tt == 1:
        return '**- - - -**\n  O\n\n\n**- - - -**'
    else:
        return '**YOU LOST!**'

def get_updated_hidden_word(hiddenword, ll):
    updt = ''
    for i in range(len(hiddenword)):
        if ll == word[i]:
            updt += ll
        else:
            updt += hiddenword[i]
    return updt



def how_many_es(number):
    sss = 'lik'
    for i in range(number):
        sss += 'e'
    sss += 's'
    return sss



def get_gametable(gt):
    table = ''
    cn = 0
    for i in range(len(gt)):
        table += gt[i]
        cn += 1
        if cn == 3:
            cn = 0
            table += '\n'
    return table

def tic_checker(gt):
    return (gt[0] == gt[1] == gt[2] != '+') or (gt[3] == gt[4] == gt[5] != '+') or (gt[6] == gt[7] == gt[8] != '+') or (gt[0] == gt[3] == gt[6] != '+') or (gt[1] == gt[4] == gt[7] != '+') or (gt[2] == gt[5] == gt[8] != '+') or (gt[0] == gt[4] == gt[8] != '+') or (gt[2] == gt[4] == gt[8] != '+')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):

    global tries, word, hidden_word, updated_hidden_word, cc, aux_word, hint_condition, used_letters, gametable, moves

    message_from_user = message.content
    message_from_user_split = message_from_user.split()
    message_split_len = len(message_from_user_split)

    if message.author == client.user:
        return
    
    if message.content.startswith('-tictactoe'):
        await message.channel.send('/ / / / / / **Tic Tac Toe** \\ \\ \\ \\ \\ \\ \n\nDo the following command, **-ttt** to start the game.\nAnd do the command **-<position>** to make your play.\n\n*game table and their positions*\n           +++          1,2,3\n           +++          4,5,6\n           +++          7,8,9\n\nGood luck :)\n\n\\ \\ \\ \\ \\ \\ **Tic Tac Toe** / / / / / /')
        return

    if message.content.startswith('-ttt'):
        gametable = ['+','+','+','+','+','+','+','+','+']
        moves = []
        await message.channel.send('Tic Tac Toe game has started\nJiska shall be the **o**\'s and Luca the **x**\'s\n\n' + get_gametable(gametable))
        return
    
    if message.content.startswith('-'):
        if (len(message.content) == 2) and (ord('1') <= ord(message.content[1]) <= ord('9')):
            coord = int(message.content[1])
            if coord not in moves:
                if message.author.name == 'lucaznch':
                    gametable[coord - 1] = 'x'
                    moves += [coord]
                    if tic_checker(gametable):
                        await message.channel.send('**GAME OVER!**\n' + get_gametable(gametable) + '\nLuca won!')
                    else:
                        await message.channel.send(get_gametable(gametable))
                else:
                    gametable[coord - 1] = 'o'
                    moves += [coord]
                    if tic_checker(gametable):
                        await message.channel.send('**GAME OVER!**\n' + get_gametable(gametable) + '\nJiska won!')
                    else:
                        await message.channel.send(get_gametable(gametable))
            else:
                await message.channel.send('*that position is taken*')

    if message.content.startswith('-hangman'):
        word = get_word()
        hidden_word = get_hidden_word(word)
        tries = 6
        cc = 0
        hint_condition = True
        used_letters = []
        await message.channel.send('We have randomly selected a word for you.\nHow to play? Do the following command, **--<letter>** ,to guess one letter.\nIf you\'re confident that you know the word, do the command, **--<word>**, to guess the word\nOhhhh, and you may use the command, **-hint**, to get 1 single hint of your word\n\n' + get_image(tries) + '\n\nword-> **' + hidden_word + '**')
        return

    if message.content.startswith('--'):
        if len(message.content) == 3:
            letter = message.content[2]

            if letter not in used_letters:
                used_letters += [letter]

                if letter in word:
                    if cc == 0:
                        updated_hidden_word = get_updated_hidden_word(hidden_word, letter)
                        aux_word = updated_hidden_word
                        cc += 1
                        await message.channel.send('**' + letter + '** is in the word!    **' + updated_hidden_word + '**\n' + get_image(tries))
                    else:
                        updated_hidden_word = get_updated_hidden_word(aux_word, letter)
                        aux_word = updated_hidden_word

                        if updated_hidden_word == word:
                            await message.channel.send('You win! **' + word + '** was the right word!     `-hangman` to play again')
                        else:
                            await message.channel.send('**' + letter + '** is in the word!    **' + updated_hidden_word + '**\n' + get_image(tries))
                else:
                    tries -= 1
                    if tries == 0:
                        await message.channel.send('YOU LOST! **' + word + '** was the word!     `-hangman` to play again')
                    else:
                        await message.channel.send('**' + letter + '** is NOT in the word!    ' + '\n' + get_image(tries))
            else:
                await message.channel.send('you already used the letter **' + letter + '**')

        elif len(message.content) > 3:
            possible_word = message.content[2:]
            if possible_word == word:
                await message.channel.send('You win! **' + word + '** was the right word!     `-hangman` to play again')
            else:
                await message.channel.send('YOU LOST! **' + word + '** was the word!     `-hangman` to play again')

        else:
            await message.channel.send('*you have to put a letter after the* **--**')
        return
    
    if message.content.startswith('-hint'):
        if hint_condition:
            if word in hangman_game_hints:
                await message.channel.send('***hint:***')
                await message.channel.send(random.choice(hangman_game_hints[word]))
                hint_condition = False
                return
            else:
                await message.channel.send('since my developer is lazy, there aren\'t any hints to this word yet :/')
                return
        else:
            await message.channel.send('*you already used your hint* :(')
            return

    if message.content.startswith('-luca'):
        id_list_luca = ['<@688793217810170089>', '<@&1011240656343154740>', '<@&1011730608118046770>', '<@&1014127168336429146>', '<@&1016324944042397696>', '<@&1018451703588204604>', '<@&1028411690615836734>', '<@&1031105795674353746>']
        await message.channel.send('**LUCAAAAAAAAAAAAAAAAAAAAA**')
        for i in range(len(id_list_luca)):
            await message.channel.send(id_list_luca[i])
    
    if message.content.startswith('-jiska'):
        id_list_jiska = ['<@368406450004951050>', '<@&1011240953954185277>', '<@&1011903042230169610>', '<@&1011903808844070933>', '<@&1013807864277643264>', '<@&1016278769884991528>', '<@&1018800526432935987>', '<@&1028591915173691493>', '<@&1032256412685967400>']
        await message.channel.send('**JISKAAAAAAAAAAAAAAAAAAAAA**')
        for i in range(len(id_list_jiska)):
            await message.channel.send(id_list_jiska[i])

    if message.content.startswith('-help') or message.content.startswith('-luska'):
        await message.channel.send(bot_intro)
        return

    if message.content.startswith('-inspire'):
        await message.channel.send(get_quote())
        return

    if message.content.startswith('-study'):
        await message.channel.send(random.choice(study_msg))
        await message.channel.send(random.choice(study_gifs))
        return
    
    if message.content.startswith('-reminder'):
        reminder = '**' + message.content[10:] + '**'
        await message.channel.send('`HEYYYY`\n     :triumph:\n:index_pointing_at_the_viewer:\n' + reminder)
        return
    
    if message.content.startswith('-shower'):
        await message.channel.send(random.choice(shower_msg))
        await message.channel.send(random.choice(shower_gifs))
        return
    
    if message.content.startswith('-soccer'):
        await message.channel.send(random.choice(soccer_msg))
        await message.channel.send(random.choice(soccer_gifs))
        return

    if message.content.startswith('-random music'):
        await message.channel.send(random.choice(music_list))
        return
    if message.content.startswith('-random series'):
        await message.channel.send(random.choice(series_list))
        return
    if message.content.startswith('-random film'):
        await message.channel.send(random.choice(film_list))
        return
    if message.content.startswith('-random image'):
        await message.channel.send(random.choice(image_list))
        return
    if message.content.startswith('-random video'):
        await message.channel.send(random.choice(video_list))
        return
    
    if message.content.startswith('-rules'):
        await message.channel.send(all_rules)
        return

    if message.content.startswith('-hug'):
        name = message.content[5:]
        if message.author.name == 'lucaznch':
            await message.channel.send('**Luca** hugs **' + name + '**\n')
            await message.channel.send(random.choice(hug_gifs))
            return
        else:
            await message.channel.send('**Jiska** hugs **' + name + '**\n')
            await message.channel.send(random.choice(hug_gifs))
            return
    
    if message.content.startswith('-like'):
        nmb = int(message.content[6:])
        if nmb <= 1977:
            if message.author.name == 'lucaznch':
                await message.channel.send('**Luca **' + how_many_es(nmb) + '** Jiska**')
                return
            else:
                await message.channel.send('**Jiska **' + how_many_es(nmb) + '** Luca**')
                return
        else:
            await message.channel.send('due to the text character limit, numbers of **e**\'s must be <= 1977\n\n*but basically...*')
            if message.author.name == 'lucaznch':
                await message.channel.send('Luca **likes** Jiska **a LOT!**')
                return
            else:
                await message.channel.send('Jiska **likes** Luca **a LOT!**')
                return



    if message.content.startswith('-dm'):
        try:
            await message.author.send(random.choice(dm_list))
            return
        except discord.errors.Forbidden:
            await message.send('Settings -> Privacy & Safety -> Allow direct messages from server members')
            return
    
    if message.content.startswith('-decide'):
        if (message_split_len == 1):
            await message.channel.send('Want help deciding something?\n**-decide  <something1>  <something2>  <somethingN>  ...**\n\nOhh, since my developer is lazy, please don\'t put spaces in **<something>** content')
            return
        else:
            await message.channel.send(':thinking: I have taken your options into consideration, and I\'ve decided...')
            time.sleep(3)
            await message.channel.send('**' + random.choice(message_from_user_split[1:]) + '**')
            return

    """
    for i in range(message_split_len):
        if ('Hii' in message_from_user_split[i]) or ('hii' in message_from_user_split[i]) or ('HII' in message_from_user_split[i]):
            await message.channel.send('Hallo! :smile:')
        elif ('Wee' in message_from_user_split[i]) or ('weee' in message_from_user_split[i]) or ('WEE' in message_from_user_split[i]):
            await message.channel.send(random.choice(weeee_msg))
        elif ('hru' in message_from_user_split[i]) or ('Hru' in message_from_user_split[i]) or ('HRU' in message_from_user_split[i]):
            await message.channel.send(random.choice(hru_ans))
    """






client.run('MTAxNzQ3OTcxOTcxMDYzODE1MQ.GS21SX.xdCnNYrZt_kbOI1rNv0qF0Nxl2JH2fzNOlxU20')
