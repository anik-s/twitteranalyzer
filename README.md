# Twitter Real Time Feed Consumer and Analyzer


#### Requirements
* npm
* serverless framework
* Python 3.7 or later

#### Commands
```
npm install
pip install -r requirements.txt
sls deploy
```

#### Postman Collection
* Postman collection is inside postman_collection directory

#### Private Endpoints
##### Start Consuming Twitter Feed
```
GET /tweets/start/?keywords=football
```
##### Sample Response
```
{
    "status": true
}
```
##### Stop Consuming Twitter Feed
```
GET /tweets/stop
```
##### Authorization
```
Authorization is required for private endpoints. A header with below inforamtion should be added to authenticate a request
Authorization: Bearer <access_token>
* access_token is 123 
```


#### Public Endpoints
##### GET Collected Tweets
```
GET /tweets
```

##### Sample Response
```
{
    "tweets": [
        {
            "quoted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 13:20:00 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 106,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221060148354936833",
                "in_reply_to_user_id": null,
                "favorite_count": 887,
                "id": 1221060148354936833,
                "text": "Pablo Mari is excited to be joining Arsenal.\nhttps://t.co/aAU2mJWJTM",
                "place": null,
                "lang": "en",
                "quote_count": 80,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 160,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.football.london/arsenal-fc/transfer-news/pablo-mari-arsenal-medical-latest-17630616",
                            "display_url": "football.london/arsenal-fc/tra…",
                            "indices": [
                                45,
                                68
                            ],
                            "url": "https://t.co/aAU2mJWJTM"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 146,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1204801263575191552/MdKRNC8B_normal.jpg",
                    "listed_count": 318,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 50,
                    "description": "All the latest Arsenal news, analysis and opinion from @Football_LDN. Like us on Facebook for more: https://www.facebook.com/AFCFootball.London",
                    "created_at": "Fri Nov 04 13:36:56 +0000 2016",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "ArsenalFC_fl",
                    "id_str": "794533892778815488",
                    "profile_link_color": "992200",
                    "translator_type": "none",
                    "id": 794533892778815488,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1204801263575191552/MdKRNC8B_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.football.london/arsenal-fc/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/794533892778815488/1577969204",
                    "statuses_count": 42118,
                    "follow_request_sent": null,
                    "followers_count": 56892,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "Arsenal FC News",
                    "location": "London, England",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1918,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220982427134439424/nLuZv5Pl_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 159446,
                "description": "I'm a man who drives an uno //\n20y\n@Flamengo @FCBayern @ManUtd \n🇧🇷🇩🇪🇬🇧",
                "created_at": "Sun Feb 12 03:46:55 +0000 2017",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "vini_frotaa",
                "id_str": "830624195851718656",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 830624195851718656,
                "geo_enabled": true,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1220982427134439424/nLuZv5Pl_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/830624195851718656/1568443501",
                "statuses_count": 85693,
                "follow_request_sent": null,
                "followers_count": 732,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "zags sudamerica king",
                "location": "Acre, Brasil",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102624117870592",
            "reply_count": 0,
            "quoted_status_id": 1221060148354936833,
            "retweeted_status": {
                "quoted_status": {
                    "in_reply_to_status_id_str": null,
                    "in_reply_to_status_id": null,
                    "created_at": "Sat Jan 25 13:20:00 +0000 2020",
                    "in_reply_to_user_id_str": null,
                    "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                    "retweet_count": 106,
                    "retweeted": false,
                    "geo": null,
                    "filter_level": "low",
                    "in_reply_to_screen_name": null,
                    "is_quote_status": false,
                    "id_str": "1221060148354936833",
                    "in_reply_to_user_id": null,
                    "favorite_count": 887,
                    "id": 1221060148354936833,
                    "text": "Pablo Mari is excited to be joining Arsenal.\nhttps://t.co/aAU2mJWJTM",
                    "place": null,
                    "lang": "en",
                    "quote_count": 80,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": false,
                    "reply_count": 160,
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "https://www.football.london/arsenal-fc/transfer-news/pablo-mari-arsenal-medical-latest-17630616",
                                "display_url": "football.london/arsenal-fc/tra…",
                                "indices": [
                                    45,
                                    68
                                ],
                                "url": "https://t.co/aAU2mJWJTM"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "contributors": null,
                    "user": {
                        "utc_offset": null,
                        "friends_count": 146,
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1204801263575191552/MdKRNC8B_normal.jpg",
                        "listed_count": 318,
                        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                        "default_profile_image": false,
                        "favourites_count": 50,
                        "description": "All the latest Arsenal news, analysis and opinion from @Football_LDN. Like us on Facebook for more: https://www.facebook.com/AFCFootball.London",
                        "created_at": "Fri Nov 04 13:36:56 +0000 2016",
                        "is_translator": false,
                        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                        "protected": false,
                        "screen_name": "ArsenalFC_fl",
                        "id_str": "794533892778815488",
                        "profile_link_color": "992200",
                        "translator_type": "none",
                        "id": 794533892778815488,
                        "geo_enabled": true,
                        "profile_background_color": "000000",
                        "lang": null,
                        "profile_sidebar_border_color": "000000",
                        "profile_text_color": "000000",
                        "verified": true,
                        "profile_image_url": "http://pbs.twimg.com/profile_images/1204801263575191552/MdKRNC8B_normal.jpg",
                        "time_zone": null,
                        "url": "http://www.football.london/arsenal-fc/",
                        "contributors_enabled": false,
                        "profile_background_tile": false,
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/794533892778815488/1577969204",
                        "statuses_count": 42118,
                        "follow_request_sent": null,
                        "followers_count": 56892,
                        "profile_use_background_image": false,
                        "default_profile": false,
                        "following": null,
                        "name": "Arsenal FC News",
                        "location": "London, England",
                        "profile_sidebar_fill_color": "000000",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 13:32:57 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "quoted_status_id": 1221060148354936833,
                "retweet_count": 386,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1221063407740301312",
                "in_reply_to_user_id": null,
                "favorite_count": 1935,
                "id": 1221063407740301312,
                "text": "Cuida bem dele, ele gosta de toalhas macias pra secar o bumbum :(",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/jT3wvivjdQ",
                    "expanded": "https://twitter.com/ArsenalFC_fl/status/1221060148354936833",
                    "display": "twitter.com/ArsenalFC_fl/s…"
                },
                "lang": "pt",
                "quote_count": 12,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 21,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1221060148354936833",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 565,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1204121056677638146/d7TYZn9Z_normal.jpg",
                    "listed_count": 471,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 17057,
                    "description": "Tweetando nos espaços que eu não sou cancelado",
                    "created_at": "Tue Dec 13 21:48:43 +0000 2016",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "PoetasFla",
                    "id_str": "808790781561540608",
                    "profile_link_color": "E81C4F",
                    "translator_type": "none",
                    "id": 808790781561540608,
                    "geo_enabled": false,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1204121056677638146/d7TYZn9Z_normal.jpg",
                    "time_zone": null,
                    "url": "http://instagram.com/poetasfla",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/808790781561540608/1579771262",
                    "statuses_count": 108620,
                    "follow_request_sent": null,
                    "followers_count": 94032,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "BI DA AMÉRICA E HEPTA CAMPEÃO",
                    "location": null,
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1221060148354936833",
            "id": 1221102624117870592,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:47 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @PoetasFla: Cuida bem dele, ele gosta de toalhas macias pra secar o bumbum :(",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "pt",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968527236",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "BI DA AMÉRICA E HEPTA CAMPEÃO",
                        "indices": [
                            3,
                            13
                        ],
                        "id": 808790781561540608,
                        "screen_name": "PoetasFla",
                        "id_str": "808790781561540608"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/jT3wvivjdQ",
                "expanded": "https://twitter.com/ArsenalFC_fl/status/1221060148354936833",
                "display": "twitter.com/ArsenalFC_fl/s…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 551,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000613747519/a9d6ebe1e102a8fea8bda2c5820ea8eb_normal.jpeg",
                "listed_count": 1,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 677,
                "description": "An enlightened man is motivated by the desire to achieve, not by the desire to be noticed.",
                "created_at": "Fri Oct 18 13:21:48 +0000 2013",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Jef_Fincher",
                "id_str": "1968899335",
                "profile_link_color": "89C9FA",
                "translator_type": "none",
                "id": 1968899335,
                "geo_enabled": false,
                "profile_background_color": "89C9FA",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/378800000613747519/a9d6ebe1e102a8fea8bda2c5820ea8eb_normal.jpeg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1968899335/1436731064",
                "statuses_count": 1285,
                "follow_request_sent": null,
                "followers_count": 184,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Jef Fincher",
                "location": null,
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102066854252546",
            "reply_count": 0,
            "display_text_range": [
                27,
                108
            ],
            "id": 1221102066854252546,
            "in_reply_to_user_id": 1043185714437992449,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:34 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "@catturd2 @realDonaldTrump Yes it would be like NFL playing a PeeWee league football team in the Super Bowl.",
            "in_reply_to_user_id_str": "1043185714437992449",
            "in_reply_to_status_id": 1221101591568187393,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "catturd2",
            "place": null,
            "timestamp_ms": "1579968394374",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Catturd",
                        "indices": [
                            0,
                            9
                        ],
                        "id": 1043185714437992449,
                        "screen_name": "catturd2",
                        "id_str": "1043185714437992449"
                    },
                    {
                        "name": "Donald J. Trump",
                        "indices": [
                            10,
                            26
                        ],
                        "id": 25073877,
                        "screen_name": "realDonaldTrump",
                        "id_str": "25073877"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": "1221101591568187393",
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 5798,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1215418607556972545/ISMfaZKG_normal.jpg",
                "listed_count": 181,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 74280,
                "description": "UK’s First Openly HIV+ Parliamentary Candidate RA HOLords equalities Chair @LibIntBg Chair LGBTQ+Forum @NLClondon #Juve #NCFC #Powerlifting #European",
                "created_at": "Tue Feb 24 17:17:11 +0000 2009",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Juvelad",
                "id_str": "21772748",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 21772748,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1215418607556972545/ISMfaZKG_normal.jpg",
                "time_zone": null,
                "url": "http://adriantrett.org.uk/en/",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/21772748/1576413382",
                "statuses_count": 81812,
                "follow_request_sent": null,
                "followers_count": 5252,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "A.Hyyrylainen-Trett 🔶 #FBPE",
                "location": "England, United Kingdom",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102684599726081",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        129
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/tFlY9melFz",
                                "indices": [
                                    130,
                                    153
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 549,
                                        "resize": "fit",
                                        "w": 595
                                    },
                                    "medium": {
                                        "h": 549,
                                        "resize": "fit",
                                        "w": 595
                                    },
                                    "large": {
                                        "h": 549,
                                        "resize": "fit",
                                        "w": 595
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221075261074092032",
                                "expanded_url": "https://twitter.com/thenpb/status/1221075267948621826/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIhevxWsAAvzd8.png",
                                "id": 1221075261074092032,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIhevxWsAAvzd8.png",
                                "url": "https://t.co/tFlY9melFz"
                            },
                            {
                                "display_url": "pic.twitter.com/tFlY9melFz",
                                "indices": [
                                    130,
                                    153
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 457,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 806,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 1375,
                                        "resize": "fit",
                                        "w": 2048
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221075261447397377",
                                "expanded_url": "https://twitter.com/thenpb/status/1221075267948621826/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIhexKW4AEKvbp.jpg",
                                "id": 1221075261447397377,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIhexKW4AEKvbp.jpg",
                                "url": "https://t.co/tFlY9melFz"
                            }
                        ]
                    },
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "https://buff.ly/2GjcFK9",
                                "display_url": "buff.ly/2GjcFK9",
                                "indices": [
                                    89,
                                    112
                                ],
                                "url": "https://t.co/mv9gDASwbl"
                            }
                        ],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/tFlY9melFz",
                                "indices": [
                                    130,
                                    153
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 549,
                                        "resize": "fit",
                                        "w": 595
                                    },
                                    "medium": {
                                        "h": 549,
                                        "resize": "fit",
                                        "w": 595
                                    },
                                    "large": {
                                        "h": 549,
                                        "resize": "fit",
                                        "w": 595
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221075261074092032",
                                "expanded_url": "https://twitter.com/thenpb/status/1221075267948621826/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIhevxWsAAvzd8.png",
                                "id": 1221075261074092032,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIhevxWsAAvzd8.png",
                                "url": "https://t.co/tFlY9melFz"
                            },
                            {
                                "display_url": "pic.twitter.com/tFlY9melFz",
                                "indices": [
                                    130,
                                    153
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 457,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 806,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 1375,
                                        "resize": "fit",
                                        "w": 2048
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221075261447397377",
                                "expanded_url": "https://twitter.com/thenpb/status/1221075267948621826/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIhexKW4AEKvbp.jpg",
                                "id": 1221075261447397377,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIhexKW4AEKvbp.jpg",
                                "url": "https://t.co/tFlY9melFz"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [
                            {
                                "name": "Patrick Strudwick",
                                "indices": [
                                    116,
                                    129
                                ],
                                "id": 20703607,
                                "screen_name": "PatrickStrud",
                                "id_str": "20703607"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "A Football Referee Has Quit Over The FA's Handling Of A Case Of Alleged Homophobic Abuse https://t.co/mv9gDASwbl by @PatrickStrud https://t.co/tFlY9melFz"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 14:20:05 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://buffer.com\" rel=\"nofollow\">Buffer</a>",
                "retweet_count": 2,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221075267948621826",
                "in_reply_to_user_id": null,
                "favorite_count": 3,
                "id": 1221075267948621826,
                "text": "A Football Referee Has Quit Over The FA's Handling Of A Case Of Alleged Homophobic Abuse https://t.co/mv9gDASwbl by… https://t.co/UokZfwztEo",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://buff.ly/2GjcFK9",
                            "display_url": "buff.ly/2GjcFK9",
                            "indices": [
                                89,
                                112
                            ],
                            "url": "https://t.co/mv9gDASwbl"
                        },
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221075267948621826",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/UokZfwztEo"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1895,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1176388361386385409/Pewl7l1W_normal.jpg",
                    "listed_count": 36,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
                    "default_profile_image": false,
                    "favourites_count": 1291,
                    "description": "Part-time socialite, full-time #OOH guy @MediaComUK, politically homeless. @LFC @scarlets_rugby & all things 🏴󠁧󠁢󠁷󠁬󠁳󠁿 Also selfies on insta: 📸@thenpb",
                    "created_at": "Fri Oct 15 13:08:33 +0000 2010",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
                    "protected": false,
                    "screen_name": "thenpb",
                    "id_str": "203063767",
                    "profile_link_color": "FF0A0A",
                    "translator_type": "none",
                    "id": 203063767,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1176388361386385409/Pewl7l1W_normal.jpg",
                    "time_zone": null,
                    "url": "http://about.me/natepbarker",
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/203063767/1494098184",
                    "statuses_count": 46757,
                    "follow_request_sent": null,
                    "followers_count": 898,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Nate",
                    "location": "Hammersmith, London",
                    "profile_sidebar_fill_color": "EFEFEF",
                    "notifications": null
                }
            },
            "id": 1221102684599726081,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:01 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @thenpb: A Football Referee Has Quit Over The FA's Handling Of A Case Of Alleged Homophobic Abuse https://t.co/mv9gDASwbl by @PatrickStr…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968541656",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://buff.ly/2GjcFK9",
                        "display_url": "buff.ly/2GjcFK9",
                        "indices": [
                            101,
                            124
                        ],
                        "url": "https://t.co/mv9gDASwbl"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Nate",
                        "indices": [
                            3,
                            10
                        ],
                        "id": 203063767,
                        "screen_name": "thenpb",
                        "id_str": "203063767"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/EbXuum8Xu7",
                            "source_user_id": 117442705,
                            "type": "video",
                            "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "source_status_id": 1017455687981502464,
                            "url": "https://t.co/EbXuum8Xu7",
                            "indices": [
                                71,
                                94
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1017454803503509504",
                            "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                            "source_status_id_str": "1017455687981502464",
                            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "id": 1017454803503509504,
                            "source_user_id_str": "117442705",
                            "additional_media_info": {
                                "description": null,
                                "title": null,
                                "embeddable": true,
                                "monetizable": false
                            },
                            "video_info": {
                                "aspect_ratio": [
                                    16,
                                    9
                                ],
                                "duration_millis": 163160,
                                "variants": [
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 2176000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/1280x720/nxlpH9SZDiXJ5ff7.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 288000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/320x180/DqOXLHd9PbhAJdY6.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 832000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/640x360/cIXlGiMN24w9P4FJ.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/pl/6yRvxYcbNePDJbp6.m3u8?tag=3"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 16:02:05 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 2311,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220738552834809861",
                "in_reply_to_user_id": null,
                "favorite_count": 13496,
                "id": 1220738552834809861,
                "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                "place": null,
                "lang": "en",
                "quote_count": 1429,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 546,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/EbXuum8Xu7",
                            "source_user_id": 117442705,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "source_status_id": 1017455687981502464,
                            "url": "https://t.co/EbXuum8Xu7",
                            "indices": [
                                71,
                                94
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1017454803503509504",
                            "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                            "source_status_id_str": "1017455687981502464",
                            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "id": 1017454803503509504,
                            "source_user_id_str": "117442705",
                            "additional_media_info": {
                                "description": null,
                                "title": null,
                                "embeddable": true,
                                "monetizable": false
                            }
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 58,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                    "listed_count": 29,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 546,
                    "description": "The Home of Football Limbs | Enquires 📧 footylimbs@gmail.com | 18+",
                    "created_at": "Fri Mar 08 15:58:59 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "FootyLimbs",
                    "id_str": "1104048876867276800",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1104048876867276800,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                    "time_zone": null,
                    "url": "http://bit.ly/500-RiskFree",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1104048876867276800/1576774795",
                    "statuses_count": 1398,
                    "follow_request_sent": null,
                    "followers_count": 63679,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Footy Limbs",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 308,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1216427943896977413/Gc8EeKX1_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 71,
                "description": null,
                "created_at": "Thu Jul 21 12:55:58 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "AndySmith50",
                "id_str": "339652121",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 339652121,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1216427943896977413/Gc8EeKX1_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/339652121/1578853996",
                "statuses_count": 504,
                "follow_request_sent": null,
                "followers_count": 128,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Dimis II",
                "location": "London",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102256176685059",
            "reply_count": 0,
            "quoted_status_id": 1220738552834809861,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        154
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is the most overrated World Cup run ever."
                },
                "quoted_status": {
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EbXuum8Xu7",
                                "source_user_id": 117442705,
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "source_status_id": 1017455687981502464,
                                "url": "https://t.co/EbXuum8Xu7",
                                "indices": [
                                    71,
                                    94
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1017454803503509504",
                                "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                                "source_status_id_str": "1017455687981502464",
                                "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "id": 1017454803503509504,
                                "source_user_id_str": "117442705",
                                "additional_media_info": {
                                    "description": null,
                                    "title": null,
                                    "embeddable": true,
                                    "monetizable": false
                                },
                                "video_info": {
                                    "aspect_ratio": [
                                        16,
                                        9
                                    ],
                                    "duration_millis": 163160,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/1280x720/nxlpH9SZDiXJ5ff7.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 288000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/320x180/DqOXLHd9PbhAJdY6.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/640x360/cIXlGiMN24w9P4FJ.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/pl/6yRvxYcbNePDJbp6.m3u8?tag=3"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "in_reply_to_status_id_str": null,
                    "in_reply_to_status_id": null,
                    "created_at": "Fri Jan 24 16:02:05 +0000 2020",
                    "in_reply_to_user_id_str": null,
                    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                    "retweet_count": 2311,
                    "retweeted": false,
                    "geo": null,
                    "filter_level": "low",
                    "in_reply_to_screen_name": null,
                    "is_quote_status": false,
                    "id_str": "1220738552834809861",
                    "in_reply_to_user_id": null,
                    "favorite_count": 13496,
                    "id": 1220738552834809861,
                    "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                    "place": null,
                    "lang": "en",
                    "quote_count": 1429,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": false,
                    "reply_count": 546,
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EbXuum8Xu7",
                                "source_user_id": 117442705,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "source_status_id": 1017455687981502464,
                                "url": "https://t.co/EbXuum8Xu7",
                                "indices": [
                                    71,
                                    94
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1017454803503509504",
                                "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                                "source_status_id_str": "1017455687981502464",
                                "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "id": 1017454803503509504,
                                "source_user_id_str": "117442705",
                                "additional_media_info": {
                                    "description": null,
                                    "title": null,
                                    "embeddable": true,
                                    "monetizable": false
                                }
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "contributors": null,
                    "user": {
                        "utc_offset": null,
                        "friends_count": 58,
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                        "listed_count": 29,
                        "profile_background_image_url": null,
                        "default_profile_image": false,
                        "favourites_count": 546,
                        "description": "The Home of Football Limbs | Enquires 📧 footylimbs@gmail.com | 18+",
                        "created_at": "Fri Mar 08 15:58:59 +0000 2019",
                        "is_translator": false,
                        "profile_background_image_url_https": null,
                        "protected": false,
                        "screen_name": "FootyLimbs",
                        "id_str": "1104048876867276800",
                        "profile_link_color": "1DA1F2",
                        "translator_type": "none",
                        "id": 1104048876867276800,
                        "geo_enabled": false,
                        "profile_background_color": "F5F8FA",
                        "lang": null,
                        "profile_sidebar_border_color": "C0DEED",
                        "profile_text_color": "333333",
                        "verified": false,
                        "profile_image_url": "http://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                        "time_zone": null,
                        "url": "http://bit.ly/500-RiskFree",
                        "contributors_enabled": false,
                        "profile_background_tile": false,
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1104048876867276800/1576774795",
                        "statuses_count": 1398,
                        "follow_request_sent": null,
                        "followers_count": 63679,
                        "profile_use_background_image": true,
                        "default_profile": true,
                        "following": null,
                        "name": "Footy Limbs",
                        "location": null,
                        "profile_sidebar_fill_color": "DDEEF6",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 17:04:24 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "quoted_status_id": 1220738552834809861,
                "retweet_count": 3211,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1220754234326638593",
                "in_reply_to_user_id": null,
                "favorite_count": 21728,
                "id": 1220754234326638593,
                "text": "In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is… https://t.co/D4NNO7o9Ol",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/OioUcvBeoo",
                    "expanded": "https://twitter.com/footylimbs/status/1220738552834809861",
                    "display": "twitter.com/footylimbs/sta…"
                },
                "lang": "en",
                "quote_count": 370,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 346,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220754234326638593",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/D4NNO7o9Ol"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1220738552834809861",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 545,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1200070926248923136/RWROWNzf_normal.jpg",
                    "listed_count": 3,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 8654,
                    "description": "Remember that hibs top you bought me? you printed Porteous on it",
                    "created_at": "Mon Mar 02 21:59:22 +0000 2015",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "AidanDuffy07",
                    "id_str": "3058644439",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 3058644439,
                    "geo_enabled": false,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1200070926248923136/RWROWNzf_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/3058644439/1577756056",
                    "statuses_count": 2177,
                    "follow_request_sent": null,
                    "followers_count": 943,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Duffy",
                    "location": "Southside, Edinburgh ",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1220738552834809861",
            "id": 1221102256176685059,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:19 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @AidanDuffy07: In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is the m…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968439512",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Duffy",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 3058644439,
                        "screen_name": "AidanDuffy07",
                        "id_str": "3058644439"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/OioUcvBeoo",
                "expanded": "https://twitter.com/footylimbs/status/1220738552834809861",
                "display": "twitter.com/footylimbs/sta…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 508,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1212877398187876352/NOQImme7_normal.jpg",
                "listed_count": 10,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 6632,
                "description": "Danseuse | \nRegistered Nurse |\nShortie | \nLeo♌️ | \nAnime❤ |\nWWE❤️ !\nFood❤\nSC:tioluwanimii",
                "created_at": "Fri Sep 13 21:18:19 +0000 2013",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "the_ifekristi",
                "id_str": "1861765934",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1861765934,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1212877398187876352/NOQImme7_normal.jpg",
                "time_zone": null,
                "url": "http://instagram.com/the_ifekristi",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1861765934/1540988144",
                "statuses_count": 7097,
                "follow_request_sent": null,
                "followers_count": 736,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Ifekristi",
                "location": "Narnia",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102059224805377",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        272
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Rules of football as a kid.\n\n1. The fattest one is always the goalkeeper.\n2. The owner of the ball decides who plays.\n3. Penalties are only awarded if injured player swears a lot.\n4. The match ends when everyone is tired.\n5. When the owner of the ball is angry, game over."
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 06:45:08 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 840,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220960776757948416",
                "in_reply_to_user_id": null,
                "favorite_count": 2626,
                "id": 1220960776757948416,
                "text": "Rules of football as a kid.\n\n1. The fattest one is always the goalkeeper.\n2. The owner of the ball decides who play… https://t.co/bfdw73YlDJ",
                "place": null,
                "lang": "en",
                "quote_count": 69,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 168,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220960776757948416",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/bfdw73YlDJ"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 33051,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1213595722488205319/PpgB7XDr_normal.jpg",
                    "listed_count": 72,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 3957,
                    "description": "Hi there, Twitter is currently using me 😓 || Volunteer @thefamefdn || 📧: meetmrahmed@gmail.com",
                    "created_at": "Fri Jul 27 07:23:21 +0000 2018",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "UncleMohamz",
                    "id_str": "1022744230714900480",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1022744230714900480,
                    "geo_enabled": true,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1213595722488205319/PpgB7XDr_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1022744230714900480/1579590115",
                    "statuses_count": 76510,
                    "follow_request_sent": null,
                    "followers_count": 43638,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "MR AHMED🇳🇬",
                    "location": "Nigeria",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102059224805377,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:32 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @UncleMohamz: Rules of football as a kid.\n\n1. The fattest one is always the goalkeeper.\n2. The owner of the ball decides who plays.\n3. P…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968392555",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "MR AHMED🇳🇬",
                        "indices": [
                            3,
                            15
                        ],
                        "id": 1022744230714900480,
                        "screen_name": "UncleMohamz",
                        "id_str": "1022744230714900480"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 434,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220850072835043330/JPBrXpDO_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
                "default_profile_image": false,
                "favourites_count": 7686,
                "description": "SBFC ⚽️",
                "created_at": "Mon Sep 12 11:50:21 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
                "protected": false,
                "screen_name": "SamueelFord",
                "id_str": "372232871",
                "profile_link_color": "19CF86",
                "translator_type": "none",
                "id": 372232871,
                "geo_enabled": true,
                "profile_background_color": "131516",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1220850072835043330/JPBrXpDO_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/372232871/1570737757",
                "statuses_count": 8314,
                "follow_request_sent": null,
                "followers_count": 526,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "Samuel",
                "location": "Stamford",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102070167736320",
            "reply_count": 0,
            "id": 1221102070167736320,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:35 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "What a day for football, bels double and got a brace ⚽️🍺",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968395164",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 197,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1218659109865607168/4zNqy0ya_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 3526,
                "description": "GSU Tiger 🐅",
                "created_at": "Sun Jul 29 18:29:04 +0000 2018",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "Blunt_III",
                "id_str": "1023636541355307009",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1023636541355307009,
                "geo_enabled": true,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1218659109865607168/4zNqy0ya_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1023636541355307009/1571084467",
                "statuses_count": 4310,
                "follow_request_sent": null,
                "followers_count": 227,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Alexander  Blunt III",
                "location": "New Orleans, LA",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101855352205313",
            "reply_count": 0,
            "retweeted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/ByVyuy7dKA",
                            "indices": [
                                44,
                                67
                            ],
                            "sizes": {
                                "small": {
                                    "h": 680,
                                    "resize": "fit",
                                    "w": 383
                                },
                                "medium": {
                                    "h": 1200,
                                    "resize": "fit",
                                    "w": 675
                                },
                                "large": {
                                    "h": 1280,
                                    "resize": "fit",
                                    "w": 720
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1220414359421190151",
                            "expanded_url": "https://twitter.com/JackMacCFB/status/1220414573418885121/video/1",
                            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1220414359421190151/pu/img/Tlu_htzCRRJwYTeu.jpg",
                            "id": 1220414359421190151,
                            "additional_media_info": {
                                "monetizable": false
                            },
                            "type": "video",
                            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1220414359421190151/pu/img/Tlu_htzCRRJwYTeu.jpg",
                            "url": "https://t.co/ByVyuy7dKA",
                            "video_info": {
                                "aspect_ratio": [
                                    9,
                                    16
                                ],
                                "duration_millis": 58550,
                                "variants": [
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/ext_tw_video/1220414359421190151/pu/pl/eoBNAD_onroymCtv.m3u8?tag=10"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 632000,
                                        "url": "https://video.twimg.com/ext_tw_video/1220414359421190151/pu/vid/320x568/ZxlesLDduwtP27K5.mp4?tag=10"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 2176000,
                                        "url": "https://video.twimg.com/ext_tw_video/1220414359421190151/pu/vid/720x1280/34k6Mw3yuHmR7Sla.mp4?tag=10"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 832000,
                                        "url": "https://video.twimg.com/ext_tw_video/1220414359421190151/pu/vid/360x640/RPOSzz0rTyckm7At.mp4?tag=10"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Thu Jan 23 18:34:43 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 11980,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220414573418885121",
                "in_reply_to_user_id": null,
                "favorite_count": 54413,
                "id": 1220414573418885121,
                "text": "Never forget the 2008 Florida Football team https://t.co/ByVyuy7dKA",
                "place": null,
                "lang": "en",
                "quote_count": 1312,
                "favorited": false,
                "possibly_sensitive": true,
                "coordinates": null,
                "truncated": false,
                "reply_count": 226,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/ByVyuy7dKA",
                            "indices": [
                                44,
                                67
                            ],
                            "sizes": {
                                "small": {
                                    "h": 680,
                                    "resize": "fit",
                                    "w": 383
                                },
                                "medium": {
                                    "h": 1200,
                                    "resize": "fit",
                                    "w": 675
                                },
                                "large": {
                                    "h": 1280,
                                    "resize": "fit",
                                    "w": 720
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1220414359421190151",
                            "expanded_url": "https://twitter.com/JackMacCFB/status/1220414573418885121/video/1",
                            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1220414359421190151/pu/img/Tlu_htzCRRJwYTeu.jpg",
                            "id": 1220414359421190151,
                            "additional_media_info": {
                                "monetizable": false
                            },
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1220414359421190151/pu/img/Tlu_htzCRRJwYTeu.jpg",
                            "url": "https://t.co/ByVyuy7dKA"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    43
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 941,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1134239115887726592/A-i2u-8t_normal.jpg",
                    "listed_count": 224,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 30921,
                    "description": "CFB blogger & social media for @BarstoolSports. Podcasting @unnecroughness. The WOAT.",
                    "created_at": "Fri May 21 02:56:17 +0000 2010",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "JackMacCFB",
                    "id_str": "146299618",
                    "profile_link_color": "E81C4F",
                    "translator_type": "none",
                    "id": 146299618,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1134239115887726592/A-i2u-8t_normal.jpg",
                    "time_zone": null,
                    "url": "https://www.instagram.com/jackmaccfb",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/146299618/1569981317",
                    "statuses_count": 22867,
                    "follow_request_sent": null,
                    "followers_count": 18488,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "Jack McGuire",
                    "location": null,
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "id": 1221101855352205313,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:43 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @JackMacCFB: Never forget the 2008 Florida Football team https://t.co/ByVyuy7dKA",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968343948",
            "possibly_sensitive": false,
            "entities": {
                "urls": [],
                "media": [
                    {
                        "display_url": "pic.twitter.com/ByVyuy7dKA",
                        "source_user_id": 146299618,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1220414359421190151/pu/img/Tlu_htzCRRJwYTeu.jpg",
                        "source_status_id": 1220414573418885121,
                        "url": "https://t.co/ByVyuy7dKA",
                        "indices": [
                            60,
                            83
                        ],
                        "sizes": {
                            "small": {
                                "h": 680,
                                "resize": "fit",
                                "w": 383
                            },
                            "medium": {
                                "h": 1200,
                                "resize": "fit",
                                "w": 675
                            },
                            "large": {
                                "h": 1280,
                                "resize": "fit",
                                "w": 720
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1220414359421190151",
                        "expanded_url": "https://twitter.com/JackMacCFB/status/1220414573418885121/video/1",
                        "source_status_id_str": "1220414573418885121",
                        "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1220414359421190151/pu/img/Tlu_htzCRRJwYTeu.jpg",
                        "id": 1220414359421190151,
                        "source_user_id_str": "146299618",
                        "additional_media_info": {
                            "monetizable": false
                        }
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Jack McGuire",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 146299618,
                        "screen_name": "JackMacCFB",
                        "id_str": "146299618"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/ByVyuy7dKA",
                        "source_user_id": 146299618,
                        "type": "video",
                        "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1220414359421190151/pu/img/Tlu_htzCRRJwYTeu.jpg",
                        "source_status_id": 1220414573418885121,
                        "url": "https://t.co/ByVyuy7dKA",
                        "indices": [
                            60,
                            83
                        ],
                        "sizes": {
                            "small": {
                                "h": 680,
                                "resize": "fit",
                                "w": 383
                            },
                            "medium": {
                                "h": 1200,
                                "resize": "fit",
                                "w": 675
                            },
                            "large": {
                                "h": 1280,
                                "resize": "fit",
                                "w": 720
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1220414359421190151",
                        "expanded_url": "https://twitter.com/JackMacCFB/status/1220414573418885121/video/1",
                        "source_status_id_str": "1220414573418885121",
                        "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1220414359421190151/pu/img/Tlu_htzCRRJwYTeu.jpg",
                        "id": 1220414359421190151,
                        "source_user_id_str": "146299618",
                        "additional_media_info": {
                            "monetizable": false
                        },
                        "video_info": {
                            "aspect_ratio": [
                                9,
                                16
                            ],
                            "duration_millis": 58550,
                            "variants": [
                                {
                                    "content_type": "application/x-mpegURL",
                                    "url": "https://video.twimg.com/ext_tw_video/1220414359421190151/pu/pl/eoBNAD_onroymCtv.m3u8?tag=10"
                                },
                                {
                                    "content_type": "video/mp4",
                                    "bitrate": 632000,
                                    "url": "https://video.twimg.com/ext_tw_video/1220414359421190151/pu/vid/320x568/ZxlesLDduwtP27K5.mp4?tag=10"
                                },
                                {
                                    "content_type": "video/mp4",
                                    "bitrate": 2176000,
                                    "url": "https://video.twimg.com/ext_tw_video/1220414359421190151/pu/vid/720x1280/34k6Mw3yuHmR7Sla.mp4?tag=10"
                                },
                                {
                                    "content_type": "video/mp4",
                                    "bitrate": 832000,
                                    "url": "https://video.twimg.com/ext_tw_video/1220414359421190151/pu/vid/360x640/RPOSzz0rTyckm7At.mp4?tag=10"
                                }
                            ]
                        }
                    }
                ]
            },
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/JdapGXItQi",
                            "indices": [
                                104,
                                127
                            ],
                            "sizes": {
                                "small": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "medium": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "large": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221048686295371783",
                            "expanded_url": "https://twitter.com/houdini__1/status/1221049699068719105/video/1",
                            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                            "id": 1221048686295371783,
                            "additional_media_info": {
                                "monetizable": false
                            },
                            "type": "video",
                            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                            "url": "https://t.co/JdapGXItQi",
                            "video_info": {
                                "aspect_ratio": [
                                    4,
                                    5
                                ],
                                "duration_millis": 140000,
                                "variants": [
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 632000,
                                        "url": "https://video.twimg.com/ext_tw_video/1221048686295371783/pu/vid/320x400/ZMtlg3dbjbxJGTiM.mp4?tag=10"
                                    },
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/ext_tw_video/1221048686295371783/pu/pl/SIXngGgaMzSVKGk3.m3u8?tag=10"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 12:38:28 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "retweet_count": 246,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221049699068719105",
                "in_reply_to_user_id": null,
                "favorite_count": 510,
                "id": 1221049699068719105,
                "text": "How can you not love football, Just take a look at these mad street football skills 😂😂😂\n#Marlians #ASUU https://t.co/JdapGXItQi",
                "place": null,
                "lang": "en",
                "quote_count": 28,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 32,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/JdapGXItQi",
                            "indices": [
                                104,
                                127
                            ],
                            "sizes": {
                                "small": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "medium": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "large": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221048686295371783",
                            "expanded_url": "https://twitter.com/houdini__1/status/1221049699068719105/video/1",
                            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                            "id": 1221048686295371783,
                            "additional_media_info": {
                                "monetizable": false
                            },
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                            "url": "https://t.co/JdapGXItQi"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                88,
                                97
                            ],
                            "text": "Marlians"
                        },
                        {
                            "indices": [
                                98,
                                103
                            ],
                            "text": "ASUU"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    103
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 746,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1205551116043407360/GCl2E5xg_normal.jpg",
                    "listed_count": 0,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 2021,
                    "description": "How did i escape from IRAQ? IRAN 😎",
                    "created_at": "Tue Dec 03 19:13:32 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "houdini__1",
                    "id_str": "1201942357068914689",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1201942357068914689,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1205551116043407360/GCl2E5xg_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1201942357068914689/1577036810",
                    "statuses_count": 1250,
                    "follow_request_sent": null,
                    "followers_count": 699,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Jude Houd!N!",
                    "location": "planet of the ambitious ",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 746,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1205551116043407360/GCl2E5xg_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 2021,
                "description": "How did i escape from IRAQ? IRAN 😎",
                "created_at": "Tue Dec 03 19:13:32 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "houdini__1",
                "id_str": "1201942357068914689",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1201942357068914689,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1205551116043407360/GCl2E5xg_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1201942357068914689/1577036810",
                "statuses_count": 1251,
                "follow_request_sent": null,
                "followers_count": 699,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Jude Houd!N!",
                "location": "planet of the ambitious ",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102077272842240",
            "reply_count": 0,
            "quoted_status_id": 1221049699068719105,
            "retweeted_status": {
                "quoted_status": {
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/JdapGXItQi",
                                "indices": [
                                    104,
                                    127
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 400,
                                        "resize": "fit",
                                        "w": 320
                                    },
                                    "medium": {
                                        "h": 400,
                                        "resize": "fit",
                                        "w": 320
                                    },
                                    "large": {
                                        "h": 400,
                                        "resize": "fit",
                                        "w": 320
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221048686295371783",
                                "expanded_url": "https://twitter.com/houdini__1/status/1221049699068719105/video/1",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                                "id": 1221048686295371783,
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                                "url": "https://t.co/JdapGXItQi",
                                "video_info": {
                                    "aspect_ratio": [
                                        4,
                                        5
                                    ],
                                    "duration_millis": 140000,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 632000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221048686295371783/pu/vid/320x400/ZMtlg3dbjbxJGTiM.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1221048686295371783/pu/pl/SIXngGgaMzSVKGk3.m3u8?tag=10"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "in_reply_to_status_id_str": null,
                    "in_reply_to_status_id": null,
                    "created_at": "Sat Jan 25 12:38:28 +0000 2020",
                    "in_reply_to_user_id_str": null,
                    "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                    "retweet_count": 246,
                    "retweeted": false,
                    "geo": null,
                    "filter_level": "low",
                    "in_reply_to_screen_name": null,
                    "is_quote_status": false,
                    "id_str": "1221049699068719105",
                    "in_reply_to_user_id": null,
                    "favorite_count": 510,
                    "id": 1221049699068719105,
                    "text": "How can you not love football, Just take a look at these mad street football skills 😂😂😂\n#Marlians #ASUU https://t.co/JdapGXItQi",
                    "place": null,
                    "lang": "en",
                    "quote_count": 28,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": false,
                    "reply_count": 32,
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/JdapGXItQi",
                                "indices": [
                                    104,
                                    127
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 400,
                                        "resize": "fit",
                                        "w": 320
                                    },
                                    "medium": {
                                        "h": 400,
                                        "resize": "fit",
                                        "w": 320
                                    },
                                    "large": {
                                        "h": 400,
                                        "resize": "fit",
                                        "w": 320
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221048686295371783",
                                "expanded_url": "https://twitter.com/houdini__1/status/1221049699068719105/video/1",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                                "id": 1221048686295371783,
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                                "url": "https://t.co/JdapGXItQi"
                            }
                        ],
                        "hashtags": [
                            {
                                "indices": [
                                    88,
                                    97
                                ],
                                "text": "Marlians"
                            },
                            {
                                "indices": [
                                    98,
                                    103
                                ],
                                "text": "ASUU"
                            }
                        ],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "display_text_range": [
                        0,
                        103
                    ],
                    "contributors": null,
                    "user": {
                        "utc_offset": null,
                        "friends_count": 746,
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1205551116043407360/GCl2E5xg_normal.jpg",
                        "listed_count": 0,
                        "profile_background_image_url": null,
                        "default_profile_image": false,
                        "favourites_count": 2021,
                        "description": "How did i escape from IRAQ? IRAN 😎",
                        "created_at": "Tue Dec 03 19:13:32 +0000 2019",
                        "is_translator": false,
                        "profile_background_image_url_https": null,
                        "protected": false,
                        "screen_name": "houdini__1",
                        "id_str": "1201942357068914689",
                        "profile_link_color": "1DA1F2",
                        "translator_type": "none",
                        "id": 1201942357068914689,
                        "geo_enabled": false,
                        "profile_background_color": "F5F8FA",
                        "lang": null,
                        "profile_sidebar_border_color": "C0DEED",
                        "profile_text_color": "333333",
                        "verified": false,
                        "profile_image_url": "http://pbs.twimg.com/profile_images/1205551116043407360/GCl2E5xg_normal.jpg",
                        "time_zone": null,
                        "url": null,
                        "contributors_enabled": false,
                        "profile_background_tile": false,
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1201942357068914689/1577036810",
                        "statuses_count": 1250,
                        "follow_request_sent": null,
                        "followers_count": 699,
                        "profile_use_background_image": true,
                        "default_profile": true,
                        "following": null,
                        "name": "Jude Houd!N!",
                        "location": "planet of the ambitious ",
                        "profile_sidebar_fill_color": "DDEEF6",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:00:50 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "quoted_status_id": 1221049699068719105,
                "retweet_count": 1,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1221100623615156228",
                "in_reply_to_user_id": null,
                "favorite_count": 0,
                "id": 1221100623615156228,
                "text": "Mad street skills!",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/5fmzcqP0FF",
                    "expanded": "https://twitter.com/houdini__1/status/1221049699068719105",
                    "display": "twitter.com/houdini__1/sta…"
                },
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1221049699068719105",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1836,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1163563107521875970/9RhIRTNL_normal.jpg",
                    "listed_count": 0,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 12718,
                    "description": null,
                    "created_at": "Wed May 16 22:20:19 +0000 2018",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "LGowong",
                    "id_str": "996878035587657729",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 996878035587657729,
                    "geo_enabled": true,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1163563107521875970/9RhIRTNL_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "statuses_count": 10658,
                    "follow_request_sent": null,
                    "followers_count": 1432,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Lengka Gowong",
                    "location": "Jos, Nigeria",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1221049699068719105",
            "id": 1221102077272842240,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:36 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @LGowong: Mad street skills!",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968396858",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Lengka Gowong",
                        "indices": [
                            3,
                            11
                        ],
                        "id": 996878035587657729,
                        "screen_name": "LGowong",
                        "id_str": "996878035587657729"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/5fmzcqP0FF",
                "expanded": "https://twitter.com/houdini__1/status/1221049699068719105",
                "display": "twitter.com/houdini__1/sta…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 293,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/846042767230996481/7GrebQpQ_normal.jpg",
                "listed_count": 21,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 37700,
                "description": "Jurist (Erasmus / Uppsala) | Hard of hearing | Ajax | Bowie | Film | Books | Art",
                "created_at": "Wed May 26 15:09:07 +0000 2010",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Peter_Bogert",
                "id_str": "148380214",
                "profile_link_color": "3B94D9",
                "translator_type": "none",
                "id": 148380214,
                "geo_enabled": true,
                "profile_background_color": "1A1B1F",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/846042767230996481/7GrebQpQ_normal.jpg",
                "time_zone": null,
                "url": "https://brave-new-books6.webnode.nl/",
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/148380214/1568579791",
                "statuses_count": 37100,
                "follow_request_sent": null,
                "followers_count": 774,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Peter B.",
                "location": "Dordrecht, Holland",
                "profile_sidebar_fill_color": "FFFFFF",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102817705897984",
            "reply_count": 0,
            "id": 1221102817705897984,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:33 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "Newcastle United decline to comment on reported Saudi Arabia takeover talks\n\nhttps://t.co/sNFvR6qlf5",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968573391",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.theguardian.com/football/2020/jan/25/newcastle-decline-to-comment-saudi-arabia-takeover-reports?CMP=Share_AndroidApp_Tweet",
                        "display_url": "theguardian.com/football/2020/…",
                        "indices": [
                            77,
                            100
                        ],
                        "url": "https://t.co/sNFvR6qlf5"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 398,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1199317931928231936/qElhcgA4_normal.jpg",
                "listed_count": 7,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 11624,
                "description": "United season ticket holder. Get up dosser.",
                "created_at": "Fri Feb 27 22:50:16 +0000 2015",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "noncelona",
                "id_str": "3064651012",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 3064651012,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1199317931928231936/qElhcgA4_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/3064651012/1535312869",
                "statuses_count": 21670,
                "follow_request_sent": null,
                "followers_count": 419,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "NORWEGIAN SHERWOOD",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102387114455040",
            "reply_count": 0,
            "retweeted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/A1zM5PTAia",
                            "indices": [
                                69,
                                92
                            ],
                            "sizes": {
                                "small": {
                                    "h": 433,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 652,
                                    "resize": "fit",
                                    "w": 1024
                                },
                                "large": {
                                    "h": 652,
                                    "resize": "fit",
                                    "w": 1024
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221100748949413889",
                            "expanded_url": "https://twitter.com/TheSunFootball/status/1221100751541407744/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI4qVgX4AE3XS9.jpg",
                            "id": 1221100748949413889,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI4qVgX4AE3XS9.jpg",
                            "url": "https://t.co/A1zM5PTAia"
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:01:20 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://www.echobox.com\" rel=\"nofollow\">Echobox Social</a>",
                "retweet_count": 5,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221100751541407744",
                "in_reply_to_user_id": null,
                "favorite_count": 21,
                "id": 1221100751541407744,
                "text": "Man Utd fans plan mass Old Trafford walk-out https://t.co/ndYAisrWhz https://t.co/A1zM5PTAia",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 2,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.thesun.co.uk/sport/football/premierleague/10817767/united-fans-walkout-protest-glazers/?utm_medium=Social&utm_campaign=sunfootballtwitter&utm_source=Twitter#Echobox=1579965143",
                            "display_url": "thesun.co.uk/sport/football…",
                            "indices": [
                                45,
                                68
                            ],
                            "url": "https://t.co/ndYAisrWhz"
                        }
                    ],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/A1zM5PTAia",
                            "indices": [
                                69,
                                92
                            ],
                            "sizes": {
                                "small": {
                                    "h": 433,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 652,
                                    "resize": "fit",
                                    "w": 1024
                                },
                                "large": {
                                    "h": 652,
                                    "resize": "fit",
                                    "w": 1024
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221100748949413889",
                            "expanded_url": "https://twitter.com/TheSunFootball/status/1221100751541407744/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI4qVgX4AE3XS9.jpg",
                            "id": 1221100748949413889,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI4qVgX4AE3XS9.jpg",
                            "url": "https://t.co/A1zM5PTAia"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    68
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 598,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1062782754318880770/FUHd5bZv_normal.jpg",
                    "listed_count": 3441,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 821,
                    "description": "Breaking news, goals, live coverage and more. Give us a like on Facebook too: http://fb.com/TheSunFootball",
                    "created_at": "Thu Feb 12 16:21:06 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "TheSunFootball",
                    "id_str": "20689749",
                    "profile_link_color": "00745F",
                    "translator_type": "none",
                    "id": 20689749,
                    "geo_enabled": false,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1062782754318880770/FUHd5bZv_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.thesun.co.uk/football",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/20689749/1532959094",
                    "statuses_count": 222051,
                    "follow_request_sent": null,
                    "followers_count": 441770,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "The Sun Football ⚽",
                    "location": null,
                    "profile_sidebar_fill_color": "DEDEDE",
                    "notifications": null
                }
            },
            "id": 1221102387114455040,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:50 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @TheSunFootball: Man Utd fans plan mass Old Trafford walk-out https://t.co/ndYAisrWhz https://t.co/A1zM5PTAia",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968470730",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.thesun.co.uk/sport/football/premierleague/10817767/united-fans-walkout-protest-glazers/?utm_medium=Social&utm_campaign=sunfootballtwitter&utm_source=Twitter#Echobox=1579965143",
                        "display_url": "thesun.co.uk/sport/football…",
                        "indices": [
                            65,
                            88
                        ],
                        "url": "https://t.co/ndYAisrWhz"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/A1zM5PTAia",
                        "source_user_id": 20689749,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI4qVgX4AE3XS9.jpg",
                        "source_status_id": 1221100751541407744,
                        "url": "https://t.co/A1zM5PTAia",
                        "indices": [
                            89,
                            112
                        ],
                        "sizes": {
                            "small": {
                                "h": 433,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 652,
                                "resize": "fit",
                                "w": 1024
                            },
                            "large": {
                                "h": 652,
                                "resize": "fit",
                                "w": 1024
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221100748949413889",
                        "expanded_url": "https://twitter.com/TheSunFootball/status/1221100751541407744/photo/1",
                        "source_status_id_str": "1221100751541407744",
                        "media_url_https": "https://pbs.twimg.com/media/EPI4qVgX4AE3XS9.jpg",
                        "id": 1221100748949413889,
                        "source_user_id_str": "20689749"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "The Sun Football ⚽",
                        "indices": [
                            3,
                            18
                        ],
                        "id": 20689749,
                        "screen_name": "TheSunFootball",
                        "id_str": "20689749"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/A1zM5PTAia",
                        "source_user_id": 20689749,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI4qVgX4AE3XS9.jpg",
                        "source_status_id": 1221100751541407744,
                        "url": "https://t.co/A1zM5PTAia",
                        "indices": [
                            89,
                            112
                        ],
                        "sizes": {
                            "small": {
                                "h": 433,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 652,
                                "resize": "fit",
                                "w": 1024
                            },
                            "large": {
                                "h": 652,
                                "resize": "fit",
                                "w": 1024
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221100748949413889",
                        "expanded_url": "https://twitter.com/TheSunFootball/status/1221100751541407744/photo/1",
                        "source_status_id_str": "1221100751541407744",
                        "media_url_https": "https://pbs.twimg.com/media/EPI4qVgX4AE3XS9.jpg",
                        "id": 1221100748949413889,
                        "source_user_id_str": "20689749"
                    }
                ]
            },
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 642,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1212102102299938816/VYXkMEc7_normal.jpg",
                "listed_count": 15,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 17381,
                "description": "The man who believes he knows everything learns nothing. App State '18 Alumnus. 1 Samuel 8: 6-18🇺🇸",
                "created_at": "Mon Jul 14 12:24:10 +0000 2014",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "matthewepley",
                "id_str": "2710340763",
                "profile_link_color": "FAB81E",
                "translator_type": "none",
                "id": 2710340763,
                "geo_enabled": true,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1212102102299938816/VYXkMEc7_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2710340763/1577822224",
                "statuses_count": 46325,
                "follow_request_sent": null,
                "followers_count": 309,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "Matthew Epley 🇺🇸",
                "location": "Boone, NC",
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102097392971777",
            "reply_count": 0,
            "retweeted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/hI7wwLFDTQ",
                            "indices": [
                                38,
                                61
                            ],
                            "sizes": {
                                "small": {
                                    "h": 510,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 900,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 1536,
                                    "resize": "fit",
                                    "w": 2048
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221098857733316608",
                            "expanded_url": "https://twitter.com/coach_sclark/status/1221098892437217281/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI28QLUYAACv79.jpg",
                            "id": 1221098857733316608,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI28QLUYAACv79.jpg",
                            "url": "https://t.co/hI7wwLFDTQ"
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:53:57 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 15,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221098892437217281",
                "in_reply_to_user_id": null,
                "favorite_count": 102,
                "id": 1221098892437217281,
                "text": "The Best Setting in College Football! https://t.co/hI7wwLFDTQ",
                "place": null,
                "lang": "en",
                "quote_count": 1,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 2,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/hI7wwLFDTQ",
                            "indices": [
                                38,
                                61
                            ],
                            "sizes": {
                                "small": {
                                    "h": 510,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 900,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 1536,
                                    "resize": "fit",
                                    "w": 2048
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221098857733316608",
                            "expanded_url": "https://twitter.com/coach_sclark/status/1221098892437217281/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI28QLUYAACv79.jpg",
                            "id": 1221098857733316608,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI28QLUYAACv79.jpg",
                            "url": "https://t.co/hI7wwLFDTQ"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    37
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 2274,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/3366802126/ddeb578af67fcd0a2af69a72ee262431_normal.jpeg",
                    "listed_count": 28,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 4358,
                    "description": "Head Football Coach - Appalachian State University",
                    "created_at": "Mon Mar 11 14:36:37 +0000 2013",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "coach_sclark",
                    "id_str": "1259598522",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1259598522,
                    "geo_enabled": false,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/3366802126/ddeb578af67fcd0a2af69a72ee262431_normal.jpeg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1259598522/1576292049",
                    "statuses_count": 1135,
                    "follow_request_sent": null,
                    "followers_count": 13938,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Shawn Clark",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102097392971777,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:41 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @coach_sclark: The Best Setting in College Football! https://t.co/hI7wwLFDTQ",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968401655",
            "possibly_sensitive": false,
            "entities": {
                "urls": [],
                "media": [
                    {
                        "display_url": "pic.twitter.com/hI7wwLFDTQ",
                        "source_user_id": 1259598522,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI28QLUYAACv79.jpg",
                        "source_status_id": 1221098892437217281,
                        "url": "https://t.co/hI7wwLFDTQ",
                        "indices": [
                            56,
                            79
                        ],
                        "sizes": {
                            "small": {
                                "h": 510,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 900,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 1536,
                                "resize": "fit",
                                "w": 2048
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221098857733316608",
                        "expanded_url": "https://twitter.com/coach_sclark/status/1221098892437217281/photo/1",
                        "source_status_id_str": "1221098892437217281",
                        "media_url_https": "https://pbs.twimg.com/media/EPI28QLUYAACv79.jpg",
                        "id": 1221098857733316608,
                        "source_user_id_str": "1259598522"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Shawn Clark",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 1259598522,
                        "screen_name": "coach_sclark",
                        "id_str": "1259598522"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/hI7wwLFDTQ",
                        "source_user_id": 1259598522,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI28QLUYAACv79.jpg",
                        "source_status_id": 1221098892437217281,
                        "url": "https://t.co/hI7wwLFDTQ",
                        "indices": [
                            56,
                            79
                        ],
                        "sizes": {
                            "small": {
                                "h": 510,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 900,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 1536,
                                "resize": "fit",
                                "w": 2048
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221098857733316608",
                        "expanded_url": "https://twitter.com/coach_sclark/status/1221098892437217281/photo/1",
                        "source_status_id_str": "1221098892437217281",
                        "media_url_https": "https://pbs.twimg.com/media/EPI28QLUYAACv79.jpg",
                        "id": 1221098857733316608,
                        "source_user_id_str": "1259598522"
                    }
                ]
            },
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 166,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220982848397676547/U8TYFjyr_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 158,
                "description": "A father of 3. God fearing. A son. A brother. Qualified teacher👨‍🎓 unemployed. A Buccaneer 🖤 ☠️. Always looking to make a friend. @CoachRulani my Idol 👊",
                "created_at": "Sun Oct 06 20:00:42 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "SihlopheNjabulo",
                "id_str": "1180935792161677313",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1180935792161677313,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1220982848397676547/U8TYFjyr_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1180935792161677313/1577688601",
                "statuses_count": 317,
                "follow_request_sent": null,
                "followers_count": 65,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Xhosa Prince 👑",
                "location": "Harding, South Africa",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102594577268737",
            "reply_count": 0,
            "display_text_range": [
                10,
                66
            ],
            "id": 1221102594577268737,
            "in_reply_to_user_id": 839863848127590400,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:40 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "@mobu_ras Total football... not this nonsense from the log leaders",
            "in_reply_to_user_id_str": "839863848127590400",
            "in_reply_to_status_id": 1221101929608228864,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "mobu_ras",
            "place": null,
            "timestamp_ms": "1579968520193",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "OOM🔥",
                        "indices": [
                            0,
                            9
                        ],
                        "id": 839863848127590400,
                        "screen_name": "mobu_ras",
                        "id_str": "839863848127590400"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": "1221101929608228864",
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 149,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1161394386997010432/NHPG8tyK_normal.jpg",
                "listed_count": 35,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 1104,
                "description": "Highworth Town FC, BetVictor Southern League Division One South, Visit our Instagram 📸 :https://www.instagram.com/highworthtownfc/",
                "created_at": "Sat Sep 29 06:02:19 +0000 2012",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "HighworthTownFC",
                "id_str": "852333613",
                "profile_link_color": "0084B4",
                "translator_type": "none",
                "id": 852333613,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1161394386997010432/NHPG8tyK_normal.jpg",
                "time_zone": null,
                "url": "http://www.highworthtownfc.com",
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/852333613/1565732517",
                "statuses_count": 10471,
                "follow_request_sent": null,
                "followers_count": 3666,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Highworth Town FC",
                "location": "Highworth, Wilts, SN6 7DD",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102304406966279",
            "reply_count": 0,
            "display_text_range": [
                0,
                140
            ],
            "id": 1221102304406966279,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:31 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    131
                ],
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/zu2cVI3KE8",
                            "indices": [
                                132,
                                155
                            ],
                            "sizes": {
                                "small": {
                                    "h": 373,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 448,
                                    "resize": "fit",
                                    "w": 816
                                },
                                "large": {
                                    "h": 448,
                                    "resize": "fit",
                                    "w": 816
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221102220080533506",
                            "expanded_url": "https://twitter.com/HighworthTownFC/status/1221102304406966279/photo/1",
                            "media_url_https": "https://pbs.twimg.com/tweet_video_thumb/EPI5_95XUAIASOb.jpg",
                            "id": 1221102220080533506,
                            "type": "animated_gif",
                            "media_url": "http://pbs.twimg.com/tweet_video_thumb/EPI5_95XUAIASOb.jpg",
                            "url": "https://t.co/zu2cVI3KE8",
                            "video_info": {
                                "aspect_ratio": [
                                    51,
                                    28
                                ],
                                "variants": [
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 0,
                                        "url": "https://video.twimg.com/tweet_video/EPI5_95XUAIASOb.mp4"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/zu2cVI3KE8",
                            "indices": [
                                132,
                                155
                            ],
                            "sizes": {
                                "small": {
                                    "h": 373,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 448,
                                    "resize": "fit",
                                    "w": 816
                                },
                                "large": {
                                    "h": 448,
                                    "resize": "fit",
                                    "w": 816
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221102220080533506",
                            "expanded_url": "https://twitter.com/HighworthTownFC/status/1221102304406966279/photo/1",
                            "media_url_https": "https://pbs.twimg.com/tweet_video_thumb/EPI5_95XUAIASOb.jpg",
                            "id": 1221102220080533506,
                            "type": "animated_gif",
                            "media_url": "http://pbs.twimg.com/tweet_video_thumb/EPI5_95XUAIASOb.jpg",
                            "url": "https://t.co/zu2cVI3KE8",
                            "video_info": {
                                "aspect_ratio": [
                                    51,
                                    28
                                ],
                                "variants": [
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 0,
                                        "url": "https://video.twimg.com/tweet_video/EPI5_95XUAIASOb.mp4"
                                    }
                                ]
                            }
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "Good half for the boys!! Playing some good football and should be 1 up!! Get some squash down yous and lets get the 3 points!!! 🔴⚫️ https://t.co/zu2cVI3KE8"
            },
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "Good half for the boys!! Playing some good football and should be 1 up!! Get some squash down yous and lets get the… https://t.co/IwMbtM9ngT",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968451011",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102304406966279",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/IwMbtM9ngT"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1382,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/839164200878473217/lQTtyLgG_normal.jpg",
                "listed_count": 85,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 204,
                "description": "The best of our journalism. Subscribe here: http://store.thetimes.co.uk\nSpeak to our customer service team: http://thetimes.co.uk/livechat",
                "created_at": "Tue Mar 07 17:20:37 +0000 2017",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "thetimesscot",
                "id_str": "839163893519888384",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 839163893519888384,
                "geo_enabled": true,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": true,
                "profile_image_url": "http://pbs.twimg.com/profile_images/839164200878473217/lQTtyLgG_normal.jpg",
                "time_zone": null,
                "url": "https://www.thetimes.co.uk/",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/839163893519888384/1492509947",
                "statuses_count": 24826,
                "follow_request_sent": null,
                "followers_count": 6668,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "The Times Scotland",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102622255521792",
            "reply_count": 0,
            "display_text_range": [
                0,
                140
            ],
            "id": 1221102622255521792,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:46 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    201
                ],
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/4Wk2zxEmBK",
                            "indices": [
                                202,
                                225
                            ],
                            "sizes": {
                                "small": {
                                    "h": 382,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 385,
                                    "resize": "fit",
                                    "w": 685
                                },
                                "large": {
                                    "h": 385,
                                    "resize": "fit",
                                    "w": 685
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221102619789271040",
                            "expanded_url": "https://twitter.com/thetimesscot/status/1221102622255521792/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI6XO7WoAAW79K.jpg",
                            "id": 1221102619789271040,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI6XO7WoAAW79K.jpg",
                            "url": "https://t.co/4Wk2zxEmBK"
                        }
                    ]
                },
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.thetimes.co.uk/edition/scotland/rachel-corsie-there-was-a-numbness-i-couldnt-believe-that-it-was-happening-to-us-9lnrnlvfz?utm_medium=Social&utm_source=Twitter#Echobox=1579967879",
                            "display_url": "thetimes.co.uk/edition/scotla…",
                            "indices": [
                                178,
                                201
                            ],
                            "url": "https://t.co/4XOBuYc1Aw"
                        }
                    ],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/4Wk2zxEmBK",
                            "indices": [
                                202,
                                225
                            ],
                            "sizes": {
                                "small": {
                                    "h": 382,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 385,
                                    "resize": "fit",
                                    "w": 685
                                },
                                "large": {
                                    "h": 385,
                                    "resize": "fit",
                                    "w": 685
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221102619789271040",
                            "expanded_url": "https://twitter.com/thetimesscot/status/1221102622255521792/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI6XO7WoAAW79K.jpg",
                            "id": 1221102619789271040,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI6XO7WoAAW79K.jpg",
                            "url": "https://t.co/4Wk2zxEmBK"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "Rachel Corsie",
                            "indices": [
                                103,
                                118
                            ],
                            "id": 338380163,
                            "screen_name": "RachelCorsie14",
                            "id_str": "338380163"
                        },
                        {
                            "name": "Graham Spiers",
                            "indices": [
                                128,
                                141
                            ],
                            "id": 213683515,
                            "screen_name": "GrahamSpiers",
                            "id_str": "213683515"
                        }
                    ],
                    "symbols": []
                },
                "full_text": "\"We were the better team, we played better football, but we didn’t win the game. It was very painful.\" @RachelCorsie14 talks to @GrahamSpiers about Scotland's World Cup collapse https://t.co/4XOBuYc1Aw https://t.co/4Wk2zxEmBK"
            },
            "source": "<a href=\"https://www.echobox.com\" rel=\"nofollow\">Echobox Social</a>",
            "text": "\"We were the better team, we played better football, but we didn’t win the game. It was very painful.\"… https://t.co/iRgMZO9mIi",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968526792",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102622255521792",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            104,
                            127
                        ],
                        "url": "https://t.co/iRgMZO9mIi"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        240
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [
                            {
                                "indices": [
                                    16,
                                    22
                                ],
                                "text": "Barça"
                            },
                            {
                                "indices": [
                                    226,
                                    240
                                ],
                                "text": "ValenciaBarça"
                            }
                        ],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Now I know most #Barça fans wanted Valverde out and I'm not defending him, but changing to an entirely different style of play in the middle of the season was never going to be easy. Setién's Barça will need time to click...\n\n#ValenciaBarça"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:58:24 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 22,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221100012886732800",
                "in_reply_to_user_id": null,
                "favorite_count": 117,
                "id": 1221100012886732800,
                "text": "Now I know most #Barça fans wanted Valverde out and I'm not defending him, but changing to an entirely different st… https://t.co/cgG0xLxd97",
                "place": null,
                "lang": "en",
                "quote_count": 9,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 18,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221100012886732800",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/cgG0xLxd97"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                16,
                                22
                            ],
                            "text": "Barça"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 969,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1098665669661466624/rnFtE_QZ_normal.jpg",
                    "listed_count": 705,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme15/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 23748,
                    "description": "Football journalist. Spain correspondent for the London Evening Standard.\n\nMadrid-BCN.",
                    "created_at": "Tue Jan 11 16:20:09 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme15/bg.png",
                    "protected": false,
                    "screen_name": "bghayward",
                    "id_str": "236893969",
                    "profile_link_color": "9266CC",
                    "translator_type": "regular",
                    "id": 236893969,
                    "geo_enabled": true,
                    "profile_background_color": "022330",
                    "lang": null,
                    "profile_sidebar_border_color": "A8C7F7",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1098665669661466624/rnFtE_QZ_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/236893969/1562801645",
                    "statuses_count": 41358,
                    "follow_request_sent": null,
                    "followers_count": 54078,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Ben Hayward",
                    "location": "Working from a café near you",
                    "profile_sidebar_fill_color": "C0DFEC",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 2890,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1208602902203424769/2t5DGU0T_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 42203,
                "description": "Bios are kinda overrated. Human! Disgruntled..but i mean well. Retweets are merely bookmarks, not endorsements. Lighten up!",
                "created_at": "Fri Jun 29 00:44:30 +0000 2018",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "Ozerddd",
                "id_str": "1012496996857466888",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1012496996857466888,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1208602902203424769/2t5DGU0T_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1012496996857466888/1576988869",
                "statuses_count": 5940,
                "follow_request_sent": null,
                "followers_count": 1163,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Augustus of Oz",
                "location": "Up and about",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101910163443712",
            "reply_count": 0,
            "quoted_status_id": 1221100012886732800,
            "quoted_status_id_str": "1221100012886732800",
            "id": 1221101910163443712,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:57 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "How dare you bring logic to football twitter Chief? Lol",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968357016",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/CvTp2mhyuz",
                "expanded": "https://twitter.com/bghayward/status/1221100012886732800",
                "display": "twitter.com/bghayward/stat…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 736,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1198518983189835777/K1-X0iMI_normal.jpg",
                "listed_count": 5,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 35422,
                "description": "20 year old twink, love scally, twink porn. I share anything I find hot please follow and I’ll keep putting more up😈 (not me in the profile)",
                "created_at": "Thu Oct 20 22:21:10 +0000 2016",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "billyfry09",
                "id_str": "789230003024195584",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 789230003024195584,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1198518983189835777/K1-X0iMI_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/789230003024195584/1574584193",
                "statuses_count": 28948,
                "follow_request_sent": null,
                "followers_count": 685,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Billy Fry",
                "location": "London, England",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102605084086273",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        130
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/XADK1mMlAB",
                                "indices": [
                                    131,
                                    154
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221055238272143360",
                                "expanded_url": "https://twitter.com/STAXUS_Official/status/1221056385984684034/video/1",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221055238272143360/pu/img/NYZxzkwu3IJB4_Xs.jpg",
                                "id": 1221055238272143360,
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221055238272143360/pu/img/NYZxzkwu3IJB4_Xs.jpg",
                                "url": "https://t.co/XADK1mMlAB",
                                "video_info": {
                                    "aspect_ratio": [
                                        16,
                                        9
                                    ],
                                    "duration_millis": 128462,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221055238272143360/pu/vid/640x360/Dp5yPLTsOQQ5r1dU.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 256000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221055238272143360/pu/vid/480x270/KNRmoqxrwU4qV33m.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221055238272143360/pu/vid/1280x720/Dr96XdCsdBYRRF0k.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1221055238272143360/pu/pl/tNHLQ1xSUGmU2gvU.m3u8?tag=10"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "http://ow.ly/Z71b1",
                                "display_url": "ow.ly/Z71b1",
                                "indices": [
                                    107,
                                    130
                                ],
                                "url": "https://t.co/zJBLyaDSIh"
                            }
                        ],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/XADK1mMlAB",
                                "indices": [
                                    131,
                                    154
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221055238272143360",
                                "expanded_url": "https://twitter.com/STAXUS_Official/status/1221056385984684034/video/1",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221055238272143360/pu/img/NYZxzkwu3IJB4_Xs.jpg",
                                "id": 1221055238272143360,
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221055238272143360/pu/img/NYZxzkwu3IJB4_Xs.jpg",
                                "url": "https://t.co/XADK1mMlAB",
                                "video_info": {
                                    "aspect_ratio": [
                                        16,
                                        9
                                    ],
                                    "duration_millis": 128462,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221055238272143360/pu/vid/640x360/Dp5yPLTsOQQ5r1dU.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 256000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221055238272143360/pu/vid/480x270/KNRmoqxrwU4qV33m.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221055238272143360/pu/vid/1280x720/Dr96XdCsdBYRRF0k.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1221055238272143360/pu/pl/tNHLQ1xSUGmU2gvU.m3u8?tag=10"
                                        }
                                    ]
                                }
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Jerome want's to watch football, and Nick a movie, instead they compromise and have sex!!! Watch it now on https://t.co/zJBLyaDSIh https://t.co/XADK1mMlAB"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 13:05:03 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://www.hootsuite.com\" rel=\"nofollow\">Hootsuite Inc.</a>",
                "retweet_count": 8,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221056385984684034",
                "in_reply_to_user_id": null,
                "favorite_count": 36,
                "id": 1221056385984684034,
                "text": "Jerome want's to watch football, and Nick a movie, instead they compromise and have sex!!! Watch it now on… https://t.co/braXgQLW8I",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": true,
                "coordinates": null,
                "truncated": true,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221056385984684034",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                108,
                                131
                            ],
                            "url": "https://t.co/braXgQLW8I"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 85,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1128667389321711616/LBD5VRPD_normal.png",
                    "listed_count": 194,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 170,
                    "description": "NEW official ACCOUNT (@Staxus got suspended - 100.000 Flw) Genuine twink bareback PORN. We produce HIGH Quality content with the HOTTEST boys ever! #TeamSTAXUS.",
                    "created_at": "Tue Feb 10 23:07:44 +0000 2015",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "STAXUS_Official",
                    "id_str": "3028953399",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 3028953399,
                    "geo_enabled": false,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1128667389321711616/LBD5VRPD_normal.png",
                    "time_zone": null,
                    "url": "https://staxus.com/trial/?nats=MTAwNDk4LjEwMDIyLjUzLjE0NS4wLjAuMC4wLjA",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/3028953399/1559299478",
                    "statuses_count": 867,
                    "follow_request_sent": null,
                    "followers_count": 39385,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "STAXUS.COM",
                    "location": "Europe",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102605084086273,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:42 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @STAXUS_Official: Jerome want's to watch football, and Nick a movie, instead they compromise and have sex!!! Watch it now on https://t.c…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968522698",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "STAXUS.COM",
                        "indices": [
                            3,
                            19
                        ],
                        "id": 3028953399,
                        "screen_name": "STAXUS_Official",
                        "id_str": "3028953399"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 320,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1348470153/10014_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 328,
                "description": "Ashford Town (Middx) fc Club Sec, Surrey County Member, Combined Counties League Vice Chairman",
                "created_at": "Sun May 31 21:00:04 +0000 2009",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "yellowdot1",
                "id_str": "43754884",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 43754884,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1348470153/10014_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/43754884/1506205601",
                "statuses_count": 1760,
                "follow_request_sent": null,
                "followers_count": 183,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Paul Blair",
                "location": "surrey",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102068779319297",
            "reply_count": 0,
            "id": 1221102068779319297,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:34 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://www.footballwebpages.co.uk\" rel=\"nofollow\">Football Web Pages</a>",
            "text": "KICK-OFF (SECOND-HALF): Harlow Town v Ashford Town (Middx) #IsthmianLeague https://t.co/SQKlaBKSQM",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968394833",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.footballwebpages.co.uk/match/2019-2020/isthmian-football-league-south-central-division/harlow-town/ashford-town-middx/144844",
                        "display_url": "footballwebpages.co.uk/match/2019-202…",
                        "indices": [
                            75,
                            98
                        ],
                        "url": "https://t.co/SQKlaBKSQM"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            59,
                            74
                        ],
                        "text": "IsthmianLeague"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 12:47:31 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 232,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221051974071676928",
                "in_reply_to_user_id": null,
                "favorite_count": 734,
                "id": 1221051974071676928,
                "text": "FOOTBALL: Saudi wealth fund reportedly in talks to purchase Newcastle United",
                "place": null,
                "lang": "en",
                "quote_count": 94,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 41,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 0,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1145865652533547008/XBahoZmX_normal.png",
                    "listed_count": 10541,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 1,
                    "description": "Watching the world. Focused on politics, economics, science and sports. Message us for business inquiries.",
                    "created_at": "Sat Jul 27 20:42:27 +0000 2013",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "spectatorindex",
                    "id_str": "1626294277",
                    "profile_link_color": "ABB8C2",
                    "translator_type": "none",
                    "id": 1626294277,
                    "geo_enabled": false,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1145865652533547008/XBahoZmX_normal.png",
                    "time_zone": null,
                    "url": "http://spectatorindex.com",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1626294277/1430626667",
                    "statuses_count": 40211,
                    "follow_request_sent": null,
                    "followers_count": 1408223,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "The Spectator Index",
                    "location": "Global",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 682,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1189452555962736641/NxjWQozg_normal.jpg",
                "listed_count": 12,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 6303,
                "description": "IGALA OVERLORD ....make e for no cause fight...",
                "created_at": "Thu Mar 31 12:10:17 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Ojo_nu_gwa",
                "id_str": "274985220",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 274985220,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1189452555962736641/NxjWQozg_normal.jpg",
                "time_zone": null,
                "url": "http://www.fiverr.com/charlyente",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/274985220/1382456634",
                "statuses_count": 12924,
                "follow_request_sent": null,
                "followers_count": 344,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Charleey",
                "location": "in my feelings ",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101641501487107",
            "reply_count": 0,
            "quoted_status_id": 1221051974071676928,
            "quoted_status_id_str": "1221051974071676928",
            "id": 1221101641501487107,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:04:52 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "Manchester United and Ole is closer to relegation with all this take overs",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968292962",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/1YhhwolMRp",
                "expanded": "https://twitter.com/spectatorindex/status/1221051974071676928",
                "display": "twitter.com/spectatorindex…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 391,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/897479920733093888/IxQlyLhF_normal.jpg",
                "listed_count": 35,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
                "default_profile_image": false,
                "favourites_count": 39414,
                "description": "Brazil & Real Madrid fan. I (re) tweet about everything related to Football, might include some from Barca unfortunately. I also like basketball!",
                "created_at": "Tue Jun 21 20:21:59 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
                "protected": false,
                "screen_name": "billystsurin",
                "id_str": "321586769",
                "profile_link_color": "009999",
                "translator_type": "none",
                "id": 321586769,
                "geo_enabled": true,
                "profile_background_color": "131516",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/897479920733093888/IxQlyLhF_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/321586769/1499229711",
                "statuses_count": 94539,
                "follow_request_sent": null,
                "followers_count": 457,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Bill Bill",
                "location": "PAP",
                "profile_sidebar_fill_color": "EFEFEF",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101909005815808",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:54:57 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 3,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221099142862327808",
                "in_reply_to_user_id": null,
                "favorite_count": 23,
                "id": 1221099142862327808,
                "text": "Maurizio Sarri has indicated he could retire from coaching at the end of his spell at Juventus...\nhttps://t.co/ey4bLdKSYk",
                "place": null,
                "lang": "en",
                "quote_count": 1,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 1,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://en.as.com/en/2020/01/25/football/1579966841_321861.html",
                            "display_url": "en.as.com/en/2020/01/25/…",
                            "indices": [
                                98,
                                121
                            ],
                            "url": "https://t.co/ey4bLdKSYk"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 983,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1186185704331759619/35ncfPJf_normal.jpg",
                    "listed_count": 2263,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 2920,
                    "description": "Sports news in English from http://AS.com Noticias deportivas en inglés de http://AS.com (...and a little fun at times!)",
                    "created_at": "Thu Jun 07 14:21:35 +0000 2012",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "English_AS",
                    "id_str": "601993521",
                    "profile_link_color": "0084B4",
                    "translator_type": "none",
                    "id": 601993521,
                    "geo_enabled": true,
                    "profile_background_color": "202020",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1186185704331759619/35ncfPJf_normal.jpg",
                    "time_zone": null,
                    "url": "https://en.as.com/en/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/601993521/1579885249",
                    "statuses_count": 156836,
                    "follow_request_sent": null,
                    "followers_count": 170890,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "AS English",
                    "location": "Madrid, España",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221101909005815808,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:56 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @English_AS: Maurizio Sarri has indicated he could retire from coaching at the end of his spell at Juventus...\nhttps://t.co/ey4bLdKSYk",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968356740",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://en.as.com/en/2020/01/25/football/1579966841_321861.html",
                        "display_url": "en.as.com/en/2020/01/25/…",
                        "indices": [
                            114,
                            137
                        ],
                        "url": "https://t.co/ey4bLdKSYk"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "AS English",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 601993521,
                        "screen_name": "English_AS",
                        "id_str": "601993521"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 176,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/900002084099153920/_pCOV3vv_normal.jpg",
                "listed_count": 41,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 12,
                "description": "Bringing you the latest news about Hartlepool United from the town's newspaper, the Hartlepool Mail @hpoolmail.\nGive our #Pools writer @DomScurr a follow.",
                "created_at": "Thu Sep 18 11:06:12 +0000 2014",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "HUFCMail",
                "id_str": "2816793312",
                "profile_link_color": "1B95E0",
                "translator_type": "none",
                "id": 2816793312,
                "geo_enabled": false,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/900002084099153920/_pCOV3vv_normal.jpg",
                "time_zone": null,
                "url": "http://www.hartlepoolmail.co.uk/sport/football/hartlepool-united",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2816793312/1570314765",
                "statuses_count": 27717,
                "follow_request_sent": null,
                "followers_count": 1241,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "MailHUFC",
                "location": "Hartlepool, England",
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102306336411649",
            "reply_count": 0,
            "id": 1221102306336411649,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:31 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
            "text": "Toure blazes over!\n\n#HUFC #Pools \n\nhttps://t.co/xuNg6BmXXb",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968451471",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.hartlepoolmail.co.uk/sport/football/hartlepool-united-1-0-stockport-county-live-team-news-line-ups-previews-action-and-reaction-victoria-park-1375010",
                        "display_url": "hartlepoolmail.co.uk/sport/football…",
                        "indices": [
                            35,
                            58
                        ],
                        "url": "https://t.co/xuNg6BmXXb"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            20,
                            25
                        ],
                        "text": "HUFC"
                    },
                    {
                        "indices": [
                            26,
                            32
                        ],
                        "text": "Pools"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 75,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1105873145850941442/WYAbJduk_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 169,
                "description": "#1 sports betting marketplace\n🔍 Full transparency\n📊 Live odds\n⛏️ Users picks\n🏺 Picks history\n📈 User statistics\n↘️ See you there https://t.co/QjNXr91nuO",
                "created_at": "Wed Mar 13 16:47:26 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "SportsTrader888",
                "id_str": "1105873010446221312",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1105873010446221312,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1105873145850941442/WYAbJduk_normal.jpg",
                "time_zone": null,
                "url": "http://sportstrader.pro",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1105873010446221312/1552495799",
                "statuses_count": 8916,
                "follow_request_sent": null,
                "followers_count": 138,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "SportsTrader.Pro",
                "location": "Delaware, USA",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102373671788545",
            "reply_count": 0,
            "id": 1221102373671788545,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:47 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    277
                ],
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://sportstrader.pro:443/pick/10612",
                            "display_url": "sportstrader.pro/pick/10612",
                            "indices": [
                                60,
                                83
                            ],
                            "url": "https://t.co/rugHkdE2B4"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                84,
                                92
                            ],
                            "text": "Betting"
                        },
                        {
                            "indices": [
                                93,
                                99
                            ],
                            "text": "NCAAF"
                        },
                        {
                            "indices": [
                                100,
                                114
                            ],
                            "text": "Sportsbetting"
                        },
                        {
                            "indices": [
                                115,
                                125
                            ],
                            "text": "SuperBowl"
                        },
                        {
                            "indices": [
                                126,
                                138
                            ],
                            "text": "bettingtips"
                        },
                        {
                            "indices": [
                                139,
                                148
                            ],
                            "text": "NFLpicks"
                        },
                        {
                            "indices": [
                                149,
                                165
                            ],
                            "text": "gamblingtwitter"
                        },
                        {
                            "indices": [
                                166,
                                170
                            ],
                            "text": "NHL"
                        },
                        {
                            "indices": [
                                171,
                                180
                            ],
                            "text": "football"
                        },
                        {
                            "indices": [
                                181,
                                185
                            ],
                            "text": "MMA"
                        },
                        {
                            "indices": [
                                186,
                                190
                            ],
                            "text": "UFC"
                        },
                        {
                            "indices": [
                                191,
                                195
                            ],
                            "text": "dfs"
                        },
                        {
                            "indices": [
                                196,
                                203
                            ],
                            "text": "parlay"
                        },
                        {
                            "indices": [
                                204,
                                211
                            ],
                            "text": "Sports"
                        },
                        {
                            "indices": [
                                212,
                                224
                            ],
                            "text": "sportspicks"
                        },
                        {
                            "indices": [
                                225,
                                234
                            ],
                            "text": "gambling"
                        },
                        {
                            "indices": [
                                235,
                                240
                            ],
                            "text": "Odds"
                        },
                        {
                            "indices": [
                                241,
                                245
                            ],
                            "text": "MLB"
                        },
                        {
                            "indices": [
                                246,
                                259
                            ],
                            "text": "marchmadness"
                        },
                        {
                            "indices": [
                                260,
                                265
                            ],
                            "text": "ncaa"
                        },
                        {
                            "indices": [
                                266,
                                270
                            ],
                            "text": "cbb"
                        },
                        {
                            "indices": [
                                271,
                                277
                            ],
                            "text": "ncaab"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "New pick for Mississippi State Bulldogs vs Oklahoma Sooners https://t.co/rugHkdE2B4 #Betting #NCAAF #Sportsbetting #SuperBowl\n#bettingtips #NFLpicks #gamblingtwitter #NHL\n#football #MMA #UFC #dfs #parlay\n#Sports #sportspicks #gambling #Odds\n#MLB #marchmadness #ncaa #cbb #ncaab"
            },
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "New pick for Mississippi State Bulldogs vs Oklahoma Sooners https://t.co/rugHkdE2B4 #Betting #NCAAF #Sportsbetting… https://t.co/cCoi0lK5FY",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968467525",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://sportstrader.pro:443/pick/10612",
                        "display_url": "sportstrader.pro/pick/10612",
                        "indices": [
                            60,
                            83
                        ],
                        "url": "https://t.co/rugHkdE2B4"
                    },
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102373671788545",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            116,
                            139
                        ],
                        "url": "https://t.co/cCoi0lK5FY"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            84,
                            92
                        ],
                        "text": "Betting"
                    },
                    {
                        "indices": [
                            93,
                            99
                        ],
                        "text": "NCAAF"
                    },
                    {
                        "indices": [
                            100,
                            114
                        ],
                        "text": "Sportsbetting"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 0,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1218779592481050624/s4hgk2cO_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 0,
                "description": null,
                "created_at": "Thu Dec 26 13:32:57 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "ochi_tanaka",
                "id_str": "1210191706286542849",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1210191706286542849,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1218779592481050624/s4hgk2cO_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1210191706286542849/1578041126",
                "statuses_count": 270,
                "follow_request_sent": null,
                "followers_count": 6,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "TV_SportsLiveStream Full HD",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101906929389569",
            "reply_count": 0,
            "id": 1221101906929389569,
            "in_reply_to_user_id": 1210191706286542849,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:56 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "Football |Live Stream| 【 Blois VS Saint-Etienne B -  National 2 Grp. C - 12:00 | 25-Jan-20| click here:https://t.co/PRPXu4VZ9B",
            "in_reply_to_user_id_str": "1210191706286542849",
            "in_reply_to_status_id": 1221101904081514496,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "ochi_tanaka",
            "place": null,
            "timestamp_ms": "1579968356245",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "http://livetv.0fficialmedia.com/ALD",
                        "display_url": "livetv.0fficialmedia.com/ALD",
                        "indices": [
                            103,
                            126
                        ],
                        "url": "https://t.co/PRPXu4VZ9B"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": "1221101904081514496",
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1174,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1219401875415556096/nCaEXnLS_normal.jpg",
                "listed_count": 3,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 0,
                "description": "🔥 🔥 Discover 📣 whats #trending right now. #Merch #Free #Celebs #Business #Gadgets #News #Travel ⭐😀⭐",
                "created_at": "Tue Jun 22 00:00:11 +0000 2010",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Whats_on_Trend",
                "id_str": "158170176",
                "profile_link_color": "0084B4",
                "translator_type": "none",
                "id": 158170176,
                "geo_enabled": false,
                "profile_background_color": "FFFFFF",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1219401875415556096/nCaEXnLS_normal.jpg",
                "time_zone": null,
                "url": "http://www.ontrend.com",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/158170176/1579567193",
                "statuses_count": 3476,
                "follow_request_sent": null,
                "followers_count": 205,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "🔥 🔥 #Trending Merch 📣 Products & Deals! ⭐😀⭐",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102083102765056",
            "reply_count": 0,
            "display_text_range": [
                0,
                140
            ],
            "id": 1221102083102765056,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:38 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    202
                ],
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/dIOc331BcM",
                            "indices": [
                                203,
                                226
                            ],
                            "sizes": {
                                "small": {
                                    "h": 329,
                                    "resize": "fit",
                                    "w": 400
                                },
                                "medium": {
                                    "h": 329,
                                    "resize": "fit",
                                    "w": 400
                                },
                                "large": {
                                    "h": 329,
                                    "resize": "fit",
                                    "w": 400
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221102081689260032",
                            "expanded_url": "https://twitter.com/Whats_on_Trend/status/1221102083102765056/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI536WUEAAQbmH.jpg",
                            "id": 1221102081689260032,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI536WUEAAQbmH.jpg",
                            "url": "https://t.co/dIOc331BcM"
                        }
                    ]
                },
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "http://dlvr.it/RNktD7",
                            "display_url": "dlvr.it/RNktD7",
                            "indices": [
                                179,
                                202
                            ],
                            "url": "https://t.co/r7YFnGv8NZ"
                        }
                    ],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/dIOc331BcM",
                            "indices": [
                                203,
                                226
                            ],
                            "sizes": {
                                "small": {
                                    "h": 329,
                                    "resize": "fit",
                                    "w": 400
                                },
                                "medium": {
                                    "h": 329,
                                    "resize": "fit",
                                    "w": 400
                                },
                                "large": {
                                    "h": 329,
                                    "resize": "fit",
                                    "w": 400
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221102081689260032",
                            "expanded_url": "https://twitter.com/Whats_on_Trend/status/1221102083102765056/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI536WUEAAQbmH.jpg",
                            "id": 1221102081689260032,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI536WUEAAQbmH.jpg",
                            "url": "https://t.co/dIOc331BcM"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                166,
                                178
                            ],
                            "text": "GriffinPark"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "Griffin Park Brentford fc Griffin Park Street Sign metal Aluminium Football ground stadium / 'Farewell to Griffin Park' -Brentford FC 2020 Official A3 Wall Calendar. #GriffinPark https://t.co/r7YFnGv8NZ https://t.co/dIOc331BcM"
            },
            "source": "<a href=\"https://dlvrit.com/\" rel=\"nofollow\">dlvr.it</a>",
            "text": "Griffin Park Brentford fc Griffin Park Street Sign metal Aluminium Football ground stadium / 'Farewell to Griffin P… https://t.co/DYNYkc0q5l",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968398248",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102083102765056",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/DYNYkc0q5l"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 717,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/461764399770779648/5NkOhTCj_normal.jpeg",
                "listed_count": 22,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 4692,
                "description": "Based in Witham, Essex. Competing in the Isthmian North, Isthmian Development and the essex senior Reserve league and youth Leagues. ⚽️ #withamtownfc #CDNM",
                "created_at": "Sat Dec 17 23:24:35 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Withamtownfc",
                "id_str": "439572085",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 439572085,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/461764399770779648/5NkOhTCj_normal.jpeg",
                "time_zone": null,
                "url": "http://www.pitchero.com/clubs/withamtown",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/439572085/1578688708",
                "statuses_count": 13140,
                "follow_request_sent": null,
                "followers_count": 4716,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "WithamTownFC",
                "location": "Spa road Witham, Essex. ",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102601204305921",
            "reply_count": 0,
            "display_text_range": [
                0,
                83
            ],
            "id": 1221102601204305921,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:41 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://www.footballwebpages.co.uk\" rel=\"nofollow\">Football Web Pages</a>",
            "text": "SUB: Oliver Bell replaced Liam Whipps (46') #IsthmianLeague https://t.co/u8tGioN0Rs https://t.co/JCZZ7Tf0hc",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968521773",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.footballwebpages.co.uk/match/2019-2020/isthmian-football-league-north-division/aveley/witham-town/144461",
                        "display_url": "footballwebpages.co.uk/match/2019-202…",
                        "indices": [
                            60,
                            83
                        ],
                        "url": "https://t.co/u8tGioN0Rs"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/JCZZ7Tf0hc",
                        "indices": [
                            84,
                            107
                        ],
                        "sizes": {
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 1280
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221102599316918273",
                        "expanded_url": "https://twitter.com/Withamtownfc/status/1221102601204305921/photo/1",
                        "media_url_https": "https://pbs.twimg.com/media/EPI6WCqXUAE3ICC.jpg",
                        "id": 1221102599316918273,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI6WCqXUAE3ICC.jpg",
                        "url": "https://t.co/JCZZ7Tf0hc"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            44,
                            59
                        ],
                        "text": "IsthmianLeague"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/JCZZ7Tf0hc",
                        "indices": [
                            84,
                            107
                        ],
                        "sizes": {
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 1280
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221102599316918273",
                        "expanded_url": "https://twitter.com/Withamtownfc/status/1221102601204305921/photo/1",
                        "media_url_https": "https://pbs.twimg.com/media/EPI6WCqXUAE3ICC.jpg",
                        "id": 1221102599316918273,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI6WCqXUAE3ICC.jpg",
                        "url": "https://t.co/JCZZ7Tf0hc"
                    }
                ]
            },
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 49,
                "profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 1,
                "description": "CEO/Director.\nWesani group of company",
                "created_at": "Fri Dec 27 05:55:26 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "C_wesani",
                "id_str": "1210438778160062464",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1210438778160062464,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 13,
                "follow_request_sent": null,
                "followers_count": 0,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "C Wesani",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102810944753664",
            "reply_count": 0,
            "id": 1221102810944753664,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:31 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    237
                ],
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.instagram.com/p/B7v7IMXprQd/?igshid=u7wuwb1lh06z",
                            "display_url": "instagram.com/p/B7v7IMXprQd/…",
                            "indices": [
                                214,
                                237
                            ],
                            "url": "https://t.co/vQv0sLVgVg"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                183,
                                189
                            ],
                            "text": "dbest"
                        },
                        {
                            "indices": [
                                190,
                                199
                            ],
                            "text": "c_wesani"
                        },
                        {
                            "indices": [
                                200,
                                212
                            ],
                            "text": "wesanigroup"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "THE MAN BEHIND THE HAPPENINGS IN ABAEZI KINGDOM.\n\nWESANI HIMSELF.\n\nWESANI GROUP FOUNDATION.\n\nHOSTED A FOOTBALL COMPETITION FOR THE PEOPLE OF ABAEZI EGBEMA IN OHAJI/EGBEMA IMO STATE.\n\n#dbest #c_wesani #wesanigroup… https://t.co/vQv0sLVgVg"
            },
            "source": "<a href=\"http://instagram.com\" rel=\"nofollow\">Instagram</a>",
            "text": "THE MAN BEHIND THE HAPPENINGS IN ABAEZI KINGDOM.\n\nWESANI HIMSELF.\n\nWESANI GROUP FOUNDATION.\n\nHOSTED A FOOTBALL COMP… https://t.co/VJBpWobUa2",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968571779",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102810944753664",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/VJBpWobUa2"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        147
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/6AihLmvkk0",
                                "indices": [
                                    148,
                                    171
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 453,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 533,
                                        "resize": "fit",
                                        "w": 800
                                    },
                                    "large": {
                                        "h": 533,
                                        "resize": "fit",
                                        "w": 800
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221045064232767488",
                                "expanded_url": "https://twitter.com/CitysEra/status/1221045068158644224/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIGBDxWkAADIdh.jpg",
                                "id": 1221045064232767488,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIGBDxWkAADIdh.jpg",
                                "url": "https://t.co/6AihLmvkk0"
                            },
                            {
                                "display_url": "pic.twitter.com/6AihLmvkk0",
                                "indices": [
                                    148,
                                    171
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 357,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 630,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 630,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221045064304144386",
                                "expanded_url": "https://twitter.com/CitysEra/status/1221045068158644224/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIGBECXsAIumC1.jpg",
                                "id": 1221045064304144386,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIGBECXsAIumC1.jpg",
                                "url": "https://t.co/6AihLmvkk0"
                            }
                        ]
                    },
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/6AihLmvkk0",
                                "indices": [
                                    148,
                                    171
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 453,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 533,
                                        "resize": "fit",
                                        "w": 800
                                    },
                                    "large": {
                                        "h": 533,
                                        "resize": "fit",
                                        "w": 800
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221045064232767488",
                                "expanded_url": "https://twitter.com/CitysEra/status/1221045068158644224/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIGBDxWkAADIdh.jpg",
                                "id": 1221045064232767488,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIGBDxWkAADIdh.jpg",
                                "url": "https://t.co/6AihLmvkk0"
                            },
                            {
                                "display_url": "pic.twitter.com/6AihLmvkk0",
                                "indices": [
                                    148,
                                    171
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 357,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 630,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 630,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221045064304144386",
                                "expanded_url": "https://twitter.com/CitysEra/status/1221045068158644224/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIGBECXsAIumC1.jpg",
                                "id": 1221045064304144386,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIGBECXsAIumC1.jpg",
                                "url": "https://t.co/6AihLmvkk0"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "If you play football irl, compare your play style to a premier league player.\n\n(I play left back for college and holding midfield in Sunday league) https://t.co/6AihLmvkk0"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 12:20:04 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 5,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221045068158644224",
                "in_reply_to_user_id": null,
                "favorite_count": 534,
                "id": 1221045068158644224,
                "text": "If you play football irl, compare your play style to a premier league player.\n\n(I play left back for college and ho… https://t.co/nsPcIN9JCv",
                "place": null,
                "lang": "en",
                "quote_count": 161,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 431,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221045068158644224",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/nsPcIN9JCv"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1080,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1219934116906524673/7r0r5zy7_normal.jpg",
                    "listed_count": 12,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 122324,
                    "description": "Fan Account. MCFC Season Ticket Holder. Backup - @CityzEra",
                    "created_at": "Thu Sep 08 14:47:48 +0000 2016",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "CitysEra",
                    "id_str": "773895619501035520",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 773895619501035520,
                    "geo_enabled": true,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1219934116906524673/7r0r5zy7_normal.jpg",
                    "time_zone": null,
                    "url": "http://mancity.com",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/773895619501035520/1579764536",
                    "statuses_count": 8693,
                    "follow_request_sent": null,
                    "followers_count": 3972,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Ben",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 144,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1219597520994742272/1x1IWvVS_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 681,
                "description": null,
                "created_at": "Sat Oct 20 14:55:18 +0000 2018",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "KieCLFC6",
                "id_str": "1053660937935355904",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1053660937935355904,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1219597520994742272/1x1IWvVS_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1053660937935355904/1576514262",
                "statuses_count": 8474,
                "follow_request_sent": null,
                "followers_count": 108,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Kie",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102824295149569",
            "reply_count": 0,
            "quoted_status_id": 1221045068158644224,
            "quoted_status_id_str": "1221045068158644224",
            "id": 1221102824295149569,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:34 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "Charlie Adam",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "hi",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968574962",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/yqDI91dTkj",
                "expanded": "https://twitter.com/citysera/status/1221045068158644224",
                "display": "twitter.com/citysera/statu…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/EbXuum8Xu7",
                            "source_user_id": 117442705,
                            "type": "video",
                            "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "source_status_id": 1017455687981502464,
                            "url": "https://t.co/EbXuum8Xu7",
                            "indices": [
                                71,
                                94
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1017454803503509504",
                            "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                            "source_status_id_str": "1017455687981502464",
                            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "id": 1017454803503509504,
                            "source_user_id_str": "117442705",
                            "additional_media_info": {
                                "description": null,
                                "title": null,
                                "embeddable": true,
                                "monetizable": false
                            },
                            "video_info": {
                                "aspect_ratio": [
                                    16,
                                    9
                                ],
                                "duration_millis": 163160,
                                "variants": [
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 2176000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/1280x720/nxlpH9SZDiXJ5ff7.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 288000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/320x180/DqOXLHd9PbhAJdY6.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 832000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/640x360/cIXlGiMN24w9P4FJ.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/pl/6yRvxYcbNePDJbp6.m3u8?tag=3"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 16:02:05 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 2312,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220738552834809861",
                "in_reply_to_user_id": null,
                "favorite_count": 13505,
                "id": 1220738552834809861,
                "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                "place": null,
                "lang": "en",
                "quote_count": 1431,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 548,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/EbXuum8Xu7",
                            "source_user_id": 117442705,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "source_status_id": 1017455687981502464,
                            "url": "https://t.co/EbXuum8Xu7",
                            "indices": [
                                71,
                                94
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1017454803503509504",
                            "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                            "source_status_id_str": "1017455687981502464",
                            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "id": 1017454803503509504,
                            "source_user_id_str": "117442705",
                            "additional_media_info": {
                                "description": null,
                                "title": null,
                                "embeddable": true,
                                "monetizable": false
                            }
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 58,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                    "listed_count": 29,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 546,
                    "description": "The Home of Football Limbs | Enquires 📧 footylimbs@gmail.com | 18+",
                    "created_at": "Fri Mar 08 15:58:59 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "FootyLimbs",
                    "id_str": "1104048876867276800",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1104048876867276800,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                    "time_zone": null,
                    "url": "http://bit.ly/500-RiskFree",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1104048876867276800/1576774795",
                    "statuses_count": 1398,
                    "follow_request_sent": null,
                    "followers_count": 63680,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Footy Limbs",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 60,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1214986368990023686/s5DbYe0h_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 497,
                "description": "don’t test me boy",
                "created_at": "Tue Jul 07 03:37:10 +0000 2015",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Seanicci",
                "id_str": "3363515049",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 3363515049,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1214986368990023686/s5DbYe0h_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/3363515049/1579742459",
                "statuses_count": 265,
                "follow_request_sent": null,
                "followers_count": 42,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Sean",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102627376783367",
            "reply_count": 0,
            "quoted_status_id": 1220738552834809861,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        154
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is the most overrated World Cup run ever."
                },
                "quoted_status": {
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EbXuum8Xu7",
                                "source_user_id": 117442705,
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "source_status_id": 1017455687981502464,
                                "url": "https://t.co/EbXuum8Xu7",
                                "indices": [
                                    71,
                                    94
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1017454803503509504",
                                "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                                "source_status_id_str": "1017455687981502464",
                                "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "id": 1017454803503509504,
                                "source_user_id_str": "117442705",
                                "additional_media_info": {
                                    "description": null,
                                    "title": null,
                                    "embeddable": true,
                                    "monetizable": false
                                },
                                "video_info": {
                                    "aspect_ratio": [
                                        16,
                                        9
                                    ],
                                    "duration_millis": 163160,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/1280x720/nxlpH9SZDiXJ5ff7.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 288000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/320x180/DqOXLHd9PbhAJdY6.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/640x360/cIXlGiMN24w9P4FJ.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/pl/6yRvxYcbNePDJbp6.m3u8?tag=3"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "in_reply_to_status_id_str": null,
                    "in_reply_to_status_id": null,
                    "created_at": "Fri Jan 24 16:02:05 +0000 2020",
                    "in_reply_to_user_id_str": null,
                    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                    "retweet_count": 2312,
                    "retweeted": false,
                    "geo": null,
                    "filter_level": "low",
                    "in_reply_to_screen_name": null,
                    "is_quote_status": false,
                    "id_str": "1220738552834809861",
                    "in_reply_to_user_id": null,
                    "favorite_count": 13505,
                    "id": 1220738552834809861,
                    "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                    "place": null,
                    "lang": "en",
                    "quote_count": 1431,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": false,
                    "reply_count": 548,
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EbXuum8Xu7",
                                "source_user_id": 117442705,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "source_status_id": 1017455687981502464,
                                "url": "https://t.co/EbXuum8Xu7",
                                "indices": [
                                    71,
                                    94
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1017454803503509504",
                                "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                                "source_status_id_str": "1017455687981502464",
                                "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "id": 1017454803503509504,
                                "source_user_id_str": "117442705",
                                "additional_media_info": {
                                    "description": null,
                                    "title": null,
                                    "embeddable": true,
                                    "monetizable": false
                                }
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "contributors": null,
                    "user": {
                        "utc_offset": null,
                        "friends_count": 58,
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                        "listed_count": 29,
                        "profile_background_image_url": null,
                        "default_profile_image": false,
                        "favourites_count": 546,
                        "description": "The Home of Football Limbs | Enquires 📧 footylimbs@gmail.com | 18+",
                        "created_at": "Fri Mar 08 15:58:59 +0000 2019",
                        "is_translator": false,
                        "profile_background_image_url_https": null,
                        "protected": false,
                        "screen_name": "FootyLimbs",
                        "id_str": "1104048876867276800",
                        "profile_link_color": "1DA1F2",
                        "translator_type": "none",
                        "id": 1104048876867276800,
                        "geo_enabled": false,
                        "profile_background_color": "F5F8FA",
                        "lang": null,
                        "profile_sidebar_border_color": "C0DEED",
                        "profile_text_color": "333333",
                        "verified": false,
                        "profile_image_url": "http://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                        "time_zone": null,
                        "url": "http://bit.ly/500-RiskFree",
                        "contributors_enabled": false,
                        "profile_background_tile": false,
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1104048876867276800/1576774795",
                        "statuses_count": 1398,
                        "follow_request_sent": null,
                        "followers_count": 63680,
                        "profile_use_background_image": true,
                        "default_profile": true,
                        "following": null,
                        "name": "Footy Limbs",
                        "location": null,
                        "profile_sidebar_fill_color": "DDEEF6",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 17:04:24 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "quoted_status_id": 1220738552834809861,
                "retweet_count": 3224,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1220754234326638593",
                "in_reply_to_user_id": null,
                "favorite_count": 21777,
                "id": 1220754234326638593,
                "text": "In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is… https://t.co/D4NNO7o9Ol",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/OioUcvBeoo",
                    "expanded": "https://twitter.com/footylimbs/status/1220738552834809861",
                    "display": "twitter.com/footylimbs/sta…"
                },
                "lang": "en",
                "quote_count": 374,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 346,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220754234326638593",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/D4NNO7o9Ol"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1220738552834809861",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 545,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1200070926248923136/RWROWNzf_normal.jpg",
                    "listed_count": 3,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 8654,
                    "description": "Remember that hibs top you bought me? you printed Porteous on it",
                    "created_at": "Mon Mar 02 21:59:22 +0000 2015",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "AidanDuffy07",
                    "id_str": "3058644439",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 3058644439,
                    "geo_enabled": false,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1200070926248923136/RWROWNzf_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/3058644439/1577756056",
                    "statuses_count": 2177,
                    "follow_request_sent": null,
                    "followers_count": 943,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Duffy",
                    "location": "Southside, Edinburgh ",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1220738552834809861",
            "id": 1221102627376783367,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:48 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @AidanDuffy07: In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is the m…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968528013",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Duffy",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 3058644439,
                        "screen_name": "AidanDuffy07",
                        "id_str": "3058644439"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/OioUcvBeoo",
                "expanded": "https://twitter.com/footylimbs/status/1220738552834809861",
                "display": "twitter.com/footylimbs/sta…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 629,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000847025293/3f7fb31d11a73442686080fb8f9663fa_normal.png",
                "listed_count": 6,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 1920,
                "description": null,
                "created_at": "Sat Aug 27 20:32:11 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "HTFC_Minty",
                "id_str": "363272266",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 363272266,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/378800000847025293/3f7fb31d11a73442686080fb8f9663fa_normal.png",
                "time_zone": null,
                "url": "http://harlowtownfc.net",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/363272266/1360783731",
                "statuses_count": 11974,
                "follow_request_sent": null,
                "followers_count": 430,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Ray Dyer",
                "location": "Haverigg, England",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102067122626560",
            "reply_count": 0,
            "id": 1221102067122626560,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:34 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://www.footballwebpages.co.uk\" rel=\"nofollow\">Football Web Pages</a>",
            "text": "KICK-OFF (SECOND-HALF): Harlow Town v Ashford Town (Middx) #IsthmianLeague https://t.co/5Itp4OvqlD",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968394438",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.footballwebpages.co.uk/match/2019-2020/isthmian-football-league-south-central-division/harlow-town/ashford-town-middx/144844",
                        "display_url": "footballwebpages.co.uk/match/2019-202…",
                        "indices": [
                            75,
                            98
                        ],
                        "url": "https://t.co/5Itp4OvqlD"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            59,
                            74
                        ],
                        "text": "IsthmianLeague"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 702,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1208457444491481091/FtsFtEuw_normal.jpg",
                "listed_count": 3,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 664,
                "description": "Minnesotan. Proud father. Lover of sports and music. Collector. PC: Kirilloff, Lindor, Arenado, Goldschmidt, Freeman, Kepler. Focus on RCs and autos.",
                "created_at": "Tue Feb 11 18:41:02 +0000 2014",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "teeedeee27",
                "id_str": "2338803864",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 2338803864,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1208457444491481091/FtsFtEuw_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 272,
                "follow_request_sent": null,
                "followers_count": 440,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Tony D.",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102699506282496",
            "reply_count": 0,
            "display_text_range": [
                13,
                105
            ],
            "id": 1221102699506282496,
            "in_reply_to_user_id": 1069010874747244544,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:05 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "@mahomes1501 I didn’t know Peyton had a brother who also played football. Eli must not have been as good.",
            "in_reply_to_user_id_str": "1069010874747244544",
            "in_reply_to_status_id": 1221100001344065536,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "mahomes1501",
            "place": null,
            "timestamp_ms": "1579968545210",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "mahomes15 (one more win)",
                        "indices": [
                            0,
                            12
                        ],
                        "id": 1069010874747244544,
                        "screen_name": "mahomes1501",
                        "id_str": "1069010874747244544"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": "1221100001344065536",
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 77,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/884127021626003460/P5KURlAk_normal.jpg",
                "listed_count": 3,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 4181,
                "description": "Lubo, on t'aime, on t'adore, ne pars pas, tu es magique 💚💚💚 #TeamASSE #Mercato",
                "created_at": "Sun May 01 13:06:17 +0000 2016",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "GaelB42",
                "id_str": "726759646040563712",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 726759646040563712,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/884127021626003460/P5KURlAk_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/726759646040563712/1463816284",
                "statuses_count": 4792,
                "follow_request_sent": null,
                "followers_count": 1888,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Gaël",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102324845670400",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 14:41:26 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 4,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221080642038960139",
                "in_reply_to_user_id": null,
                "favorite_count": 1,
                "id": 1221080642038960139,
                "text": "Article intéressant sur les relations entre dirigeants et ultras à Saint-Étienne, par @YHautbois (abonnés): https://t.co/JDJftV9itf",
                "place": null,
                "lang": "fr",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.lequipe.fr/Football/Article/Entre-l-asse-ses-dirigeants-et-ses-ultras-une-histoire-complexe/1102332",
                            "display_url": "lequipe.fr/Football/Artic…",
                            "indices": [
                                108,
                                131
                            ],
                            "url": "https://t.co/JDJftV9itf"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "Yo Hautbois",
                            "indices": [
                                86,
                                96
                            ],
                            "id": 370722572,
                            "screen_name": "YHautbois",
                            "id_str": "370722572"
                        }
                    ],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 419,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/982173703436812288/XS2eR9v6_normal.jpg",
                    "listed_count": 1271,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 2808,
                    "description": "Revue de foot et d'eau fraîche",
                    "created_at": "Sat Dec 12 21:16:14 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "cahiersdufoot",
                    "id_str": "96419861",
                    "profile_link_color": "FF8C00",
                    "translator_type": "none",
                    "id": 96419861,
                    "geo_enabled": false,
                    "profile_background_color": "CCCCCC",
                    "lang": null,
                    "profile_sidebar_border_color": "4D4D4D",
                    "profile_text_color": "1F1F1F",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/982173703436812288/XS2eR9v6_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.cahiersdufootball.net",
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/96419861/1360013751",
                    "statuses_count": 34461,
                    "follow_request_sent": null,
                    "followers_count": 101253,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Cahiers du football",
                    "location": null,
                    "profile_sidebar_fill_color": "666666",
                    "notifications": null
                }
            },
            "id": 1221102324845670400,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:35 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @cahiersdufoot: Article intéressant sur les relations entre dirigeants et ultras à Saint-Étienne, par @YHautbois (abonnés): https://t.co…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "fr",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968455884",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Cahiers du football",
                        "indices": [
                            3,
                            17
                        ],
                        "id": 96419861,
                        "screen_name": "cahiersdufoot",
                        "id_str": "96419861"
                    },
                    {
                        "name": "Yo Hautbois",
                        "indices": [
                            105,
                            115
                        ],
                        "id": 370722572,
                        "screen_name": "YHautbois",
                        "id_str": "370722572"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 292,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1063249926728151041/3VfuN2KX_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 145,
                "description": null,
                "created_at": "Sat Aug 01 07:36:41 +0000 2009",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "TCow4",
                "id_str": "61988571",
                "profile_link_color": "0066FF",
                "translator_type": "none",
                "id": 61988571,
                "geo_enabled": false,
                "profile_background_color": "642D8B",
                "lang": null,
                "profile_sidebar_border_color": "65B0DA",
                "profile_text_color": "3D1957",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1063249926728151041/3VfuN2KX_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/61988571/1456915442",
                "statuses_count": 134,
                "follow_request_sent": null,
                "followers_count": 164,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Tim Cowdrick",
                "location": "Cleveland, OH",
                "profile_sidebar_fill_color": "7AC4EE",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102258739466241",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 16:35:12 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://www.prestosports.com\" rel=\"nofollow\">PrestoSports Twitter</a>",
                "retweet_count": 14,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220746887398969344",
                "in_reply_to_user_id": null,
                "favorite_count": 44,
                "id": 1220746887398969344,
                "text": "2019 CWRU Football Season Recap https://t.co/lGBcZ5ELHY",
                "place": null,
                "lang": "cy",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "http://athletics.case.edu/x/wkn6l",
                            "display_url": "athletics.case.edu/x/wkn6l",
                            "indices": [
                                32,
                                55
                            ],
                            "url": "https://t.co/lGBcZ5ELHY"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 232,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/963835562292666368/v_ZLyWZ-_normal.jpg",
                    "listed_count": 9,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 238,
                    "description": "UAA Champs: '07 '08 '09 '11 '16 '17 PAC Champs: '17 '19 NCAA Playoffs: '07, '08, '09, '17 '19. 38-0 Reg Season Streak '07-'10",
                    "created_at": "Tue May 19 13:27:12 +0000 2015",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "CWRUFootball",
                    "id_str": "3289959819",
                    "profile_link_color": "3B94D9",
                    "translator_type": "none",
                    "id": 3289959819,
                    "geo_enabled": false,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/963835562292666368/v_ZLyWZ-_normal.jpg",
                    "time_zone": null,
                    "url": "http://athletics.case.edu/sports/fball/index",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/3289959819/1543941172",
                    "statuses_count": 931,
                    "follow_request_sent": null,
                    "followers_count": 1741,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "CWRU Football",
                    "location": "Cleveland, OH",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "id": 1221102258739466241,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:20 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @CWRUFootball: 2019 CWRU Football Season Recap https://t.co/lGBcZ5ELHY",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "cy",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968440123",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "http://athletics.case.edu/x/wkn6l",
                        "display_url": "athletics.case.edu/x/wkn6l",
                        "indices": [
                            50,
                            73
                        ],
                        "url": "https://t.co/lGBcZ5ELHY"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "CWRU Football",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 3289959819,
                        "screen_name": "CWRUFootball",
                        "id_str": "3289959819"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 273,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1208889149018669056/DiLU0vtO_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 5268,
                "description": "Massive Chelsea fan & boxing casual. Tweets mainly about Chelsea or sport in general. Frank Lampard is my manager!",
                "created_at": "Tue Oct 31 23:09:39 +0000 2017",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "LukeCFC__1905",
                "id_str": "925500040289882114",
                "profile_link_color": "1B95E0",
                "translator_type": "none",
                "id": 925500040289882114,
                "geo_enabled": false,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1208889149018669056/DiLU0vtO_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/925500040289882114/1570266986",
                "statuses_count": 2488,
                "follow_request_sent": null,
                "followers_count": 118,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "Luke",
                "location": null,
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102686055124993",
            "reply_count": 0,
            "display_text_range": [
                34,
                140
            ],
            "id": 1221102686055124993,
            "in_reply_to_user_id": 1205102773697732610,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:02 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    34,
                    170
                ],
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "Dave Cameron",
                            "indices": [
                                0,
                                16
                            ],
                            "id": 1205102773697732610,
                            "screen_name": "DaveCam86873947",
                            "id_str": "1205102773697732610"
                        },
                        {
                            "name": "Football Tweet",
                            "indices": [
                                17,
                                33
                            ],
                            "id": 462312323,
                            "screen_name": "Football__Tweet",
                            "id_str": "462312323"
                        }
                    ],
                    "symbols": []
                },
                "full_text": "@DaveCam86873947 @Football__Tweet So scoring 72 goals in both seasons but conceding little means we \"parked the bus\".\n\nYou really are clueless about football, aren't you?"
            },
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "@DaveCam86873947 @Football__Tweet So scoring 72 goals in both seasons but conceding little means we \"parked the bus… https://t.co/ZyCBUXD8mg",
            "in_reply_to_user_id_str": "1205102773697732610",
            "in_reply_to_status_id": 1221101761957695490,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "DaveCam86873947",
            "place": null,
            "timestamp_ms": "1579968542003",
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102686055124993",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/ZyCBUXD8mg"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Dave Cameron",
                        "indices": [
                            0,
                            16
                        ],
                        "id": 1205102773697732610,
                        "screen_name": "DaveCam86873947",
                        "id_str": "1205102773697732610"
                    },
                    {
                        "name": "Football Tweet",
                        "indices": [
                            17,
                            33
                        ],
                        "id": 462312323,
                        "screen_name": "Football__Tweet",
                        "id_str": "462312323"
                    }
                ],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": "1221101761957695490",
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1073,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1185599748377600000/UmzlPj_q_normal.jpg",
                "listed_count": 15,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 76620,
                "description": "25 Years Old #StriveForGreatness #PinstripePride #GiantsPride",
                "created_at": "Fri Dec 30 02:55:42 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "BigPapiRamirezz",
                "id_str": "450294524",
                "profile_link_color": "080101",
                "translator_type": "none",
                "id": 450294524,
                "geo_enabled": true,
                "profile_background_color": "000305",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1185599748377600000/UmzlPj_q_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/450294524/1571664441",
                "statuses_count": 78095,
                "follow_request_sent": null,
                "followers_count": 902,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Joe Ramirez",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102805886390272",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        242
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/Ccb4c6smTM",
                                "indices": [
                                    243,
                                    266
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 443,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1104
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1104
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221099829079826433",
                                "expanded_url": "https://twitter.com/AlexWilsonESM/status/1221102151541436417/video/1",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221099829079826433/pu/img/bqNkrAZAkmpgpX_w.jpg",
                                "id": 1221099829079826433,
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221099829079826433/pu/img/bqNkrAZAkmpgpX_w.jpg",
                                "url": "https://t.co/Ccb4c6smTM",
                                "video_info": {
                                    "aspect_ratio": [
                                        23,
                                        15
                                    ],
                                    "duration_millis": 103249,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 256000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221099829079826433/pu/vid/414x270/X9cSDkkVRTROopdF.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221099829079826433/pu/vid/552x360/YePcE5Pe6tRqv3Ll.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1221099829079826433/pu/pl/jat4vnjNpK04F5IF.m3u8?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221099829079826433/pu/vid/1104x720/kXvlilsSYqP5YRpx.mp4?tag=10"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/Ccb4c6smTM",
                                "indices": [
                                    243,
                                    266
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 443,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1104
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1104
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221099829079826433",
                                "expanded_url": "https://twitter.com/AlexWilsonESM/status/1221102151541436417/video/1",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221099829079826433/pu/img/bqNkrAZAkmpgpX_w.jpg",
                                "id": 1221099829079826433,
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221099829079826433/pu/img/bqNkrAZAkmpgpX_w.jpg",
                                "url": "https://t.co/Ccb4c6smTM",
                                "video_info": {
                                    "aspect_ratio": [
                                        23,
                                        15
                                    ],
                                    "duration_millis": 103249,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 256000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221099829079826433/pu/vid/414x270/X9cSDkkVRTROopdF.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221099829079826433/pu/vid/552x360/YePcE5Pe6tRqv3Ll.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1221099829079826433/pu/pl/jat4vnjNpK04F5IF.m3u8?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/ext_tw_video/1221099829079826433/pu/vid/1104x720/kXvlilsSYqP5YRpx.mp4?tag=10"
                                        }
                                    ]
                                }
                            }
                        ],
                        "hashtags": [
                            {
                                "indices": [
                                    231,
                                    242
                                ],
                                "text": "giantschat"
                            }
                        ],
                        "user_mentions": [
                            {
                                "name": "Ahmad Bradshaw",
                                "indices": [
                                    100,
                                    114
                                ],
                                "id": 331162098,
                                "screen_name": "AhmadBradshaw",
                                "id_str": "331162098"
                            },
                            {
                                "name": "Brandon Jacobs",
                                "indices": [
                                    137,
                                    148
                                ],
                                "id": 577552672,
                                "screen_name": "gatorboyrb",
                                "id_str": "577552672"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "Woke up, was missing a little ground and pound football!\n\nWow, were we lucky to see Ahmad Bradshaw (@AhmadBradshaw) and Brandon Jacobs  (@gatorboyrb) rumblin and tumblin all over the place!\n\nWhat a duo they were for the Giants...\n\n#giantschat https://t.co/Ccb4c6smTM"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:06:54 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 2,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221102151541436417",
                "in_reply_to_user_id": null,
                "favorite_count": 6,
                "id": 1221102151541436417,
                "text": "Woke up, was missing a little ground and pound football!\n\nWow, were we lucky to see Ahmad Bradshaw (@AhmadBradshaw)… https://t.co/0QZzLel02g",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 1,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221102151541436417",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/0QZzLel02g"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "Ahmad Bradshaw",
                            "indices": [
                                100,
                                114
                            ],
                            "id": 331162098,
                            "screen_name": "AhmadBradshaw",
                            "id_str": "331162098"
                        }
                    ],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1669,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/965925487632633857/5aXqZwSu_normal.jpg",
                    "listed_count": 66,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 27857,
                    "description": "Founder of Empire Sports Media • Covering the New York Giants & Yankees from places unknown • Super Bowl XLII is the source of my anxiety",
                    "created_at": "Sun Oct 02 03:15:28 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "AlexWilsonESM",
                    "id_str": "383559123",
                    "profile_link_color": "0084B4",
                    "translator_type": "none",
                    "id": 383559123,
                    "geo_enabled": true,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/965925487632633857/5aXqZwSu_normal.jpg",
                    "time_zone": null,
                    "url": "https://www.empiresportsmedia.com",
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/383559123/1569605822",
                    "statuses_count": 18366,
                    "follow_request_sent": null,
                    "followers_count": 5697,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Alex Wilson",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102805886390272,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:30 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @AlexWilsonESM: Woke up, was missing a little ground and pound football!\n\nWow, were we lucky to see Ahmad Bradshaw (@AhmadBradshaw) and…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968570573",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Alex Wilson",
                        "indices": [
                            3,
                            17
                        ],
                        "id": 383559123,
                        "screen_name": "AlexWilsonESM",
                        "id_str": "383559123"
                    },
                    {
                        "name": "Ahmad Bradshaw",
                        "indices": [
                            119,
                            133
                        ],
                        "id": 331162098,
                        "screen_name": "AhmadBradshaw",
                        "id_str": "331162098"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        188
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EljDwf6reC",
                                "indices": [
                                    189,
                                    212
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 200,
                                        "resize": "fit",
                                        "w": 490
                                    },
                                    "medium": {
                                        "h": 200,
                                        "resize": "fit",
                                        "w": 490
                                    },
                                    "large": {
                                        "h": 200,
                                        "resize": "fit",
                                        "w": 490
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221098509455298563",
                                "expanded_url": "https://twitter.com/footballitalia/status/1221098513309818881/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPI2n-vXkAMlbLI.jpg",
                                "id": 1221098509455298563,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPI2n-vXkAMlbLI.jpg",
                                "url": "https://t.co/EljDwf6reC"
                            }
                        ]
                    },
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "https://www.football-italia.net/149220/conte-inter-didnt-buy-real-madrid",
                                "display_url": "football-italia.net/149220/conte-i…",
                                "indices": [
                                    151,
                                    174
                                ],
                                "url": "https://t.co/HxVSpV81o3"
                            }
                        ],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EljDwf6reC",
                                "indices": [
                                    189,
                                    212
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 200,
                                        "resize": "fit",
                                        "w": 490
                                    },
                                    "medium": {
                                        "h": 200,
                                        "resize": "fit",
                                        "w": 490
                                    },
                                    "large": {
                                        "h": 200,
                                        "resize": "fit",
                                        "w": 490
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221098509455298563",
                                "expanded_url": "https://twitter.com/footballitalia/status/1221098513309818881/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPI2n-vXkAMlbLI.jpg",
                                "id": 1221098509455298563,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPI2n-vXkAMlbLI.jpg",
                                "url": "https://t.co/EljDwf6reC"
                            }
                        ],
                        "hashtags": [
                            {
                                "indices": [
                                    175,
                                    180
                                ],
                                "text": "FCIM"
                            },
                            {
                                "indices": [
                                    181,
                                    188
                                ],
                                "text": "SerieA"
                            }
                        ],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Antonio Conte: “The fact that we considered a draw away to Lecce to be a negative result shows how much Inter have advanced compared to past seasons.\" https://t.co/HxVSpV81o3 #FCIM #SerieA https://t.co/EljDwf6reC"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:52:27 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 4,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221098513309818881",
                "in_reply_to_user_id": null,
                "favorite_count": 16,
                "id": 1221098513309818881,
                "text": "Antonio Conte: “The fact that we considered a draw away to Lecce to be a negative result shows how much Inter have… https://t.co/6I4dzpZCif",
                "place": null,
                "lang": "en",
                "quote_count": 5,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 1,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221098513309818881",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                116,
                                139
                            ],
                            "url": "https://t.co/6I4dzpZCif"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1030,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/2514923001/kvc336eae86bjgy8ys1s_normal.jpeg",
                    "listed_count": 3363,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 236,
                    "description": "The website for English-speaking fans of Italian football",
                    "created_at": "Sat Jan 10 18:34:38 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "footballitalia",
                    "id_str": "18841928",
                    "profile_link_color": "28920C",
                    "translator_type": "none",
                    "id": 18841928,
                    "geo_enabled": false,
                    "profile_background_color": "FFFFFF",
                    "lang": null,
                    "profile_sidebar_border_color": "FA0A16",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/2514923001/kvc336eae86bjgy8ys1s_normal.jpeg",
                    "time_zone": null,
                    "url": "http://www.football-italia.net/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/18841928/1575590344",
                    "statuses_count": 276074,
                    "follow_request_sent": null,
                    "followers_count": 177260,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "footballitalia",
                    "location": null,
                    "profile_sidebar_fill_color": "DDFFCC",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 179,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1214297214585102337/gbmNpYiW_normal.jpg",
                "listed_count": 3,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 9745,
                "description": "Free Da Fam @DroPiloT",
                "created_at": "Sun Dec 11 01:23:52 +0000 2016",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "DroPil0T",
                "id_str": "807757763241721856",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 807757763241721856,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1214297214585102337/gbmNpYiW_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/807757763241721856/1574949682",
                "statuses_count": 23407,
                "follow_request_sent": null,
                "followers_count": 668,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Lucian Dro🇱🇨",
                "location": "#SaintJohn",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101982599077888",
            "reply_count": 0,
            "quoted_status_id": 1221098513309818881,
            "quoted_status_id_str": "1221098513309818881",
            "id": 1221101982599077888,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:14 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "Ole?",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "und",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968374286",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/nv6xLuGTAD",
                "expanded": "https://twitter.com/footballitalia/status/1221098513309818881",
                "display": "twitter.com/footballitalia…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 519,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220709260918525952/11FySzNm_normal.jpg",
                "listed_count": 10,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 135244,
                "description": "United Fan. on loan at CFC",
                "created_at": "Mon Apr 15 08:07:12 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "UTDFuture",
                "id_str": "1117700886829121537",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1117700886829121537,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1220709260918525952/11FySzNm_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1117700886829121537/1575985265",
                "statuses_count": 36761,
                "follow_request_sent": null,
                "followers_count": 4851,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "AD™",
                "location": "marcus and martial FC",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102575799287815",
            "reply_count": 0,
            "id": 1221102575799287815,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:35 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "People are watching Barca lol, watch real football, watch Leipzig",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968515716",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 75,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1105873145850941442/WYAbJduk_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 169,
                "description": "#1 sports betting marketplace\n🔍 Full transparency\n📊 Live odds\n⛏️ Users picks\n🏺 Picks history\n📈 User statistics\n↘️ See you there https://t.co/QjNXr91nuO",
                "created_at": "Wed Mar 13 16:47:26 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "SportsTrader888",
                "id_str": "1105873010446221312",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1105873010446221312,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1105873145850941442/WYAbJduk_normal.jpg",
                "time_zone": null,
                "url": "http://sportstrader.pro",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1105873010446221312/1552495799",
                "statuses_count": 8913,
                "follow_request_sent": null,
                "followers_count": 138,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "SportsTrader.Pro",
                "location": "Delaware, USA",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101901997051906",
            "reply_count": 0,
            "id": 1221101901997051906,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:55 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    276
                ],
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://sportstrader.pro:443/pick/10609",
                            "display_url": "sportstrader.pro/pick/10609",
                            "indices": [
                                59,
                                82
                            ],
                            "url": "https://t.co/gThqSP5kIY"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                83,
                                91
                            ],
                            "text": "Betting"
                        },
                        {
                            "indices": [
                                92,
                                98
                            ],
                            "text": "NCAAF"
                        },
                        {
                            "indices": [
                                99,
                                113
                            ],
                            "text": "Sportsbetting"
                        },
                        {
                            "indices": [
                                114,
                                124
                            ],
                            "text": "SuperBowl"
                        },
                        {
                            "indices": [
                                125,
                                137
                            ],
                            "text": "bettingtips"
                        },
                        {
                            "indices": [
                                138,
                                147
                            ],
                            "text": "NFLpicks"
                        },
                        {
                            "indices": [
                                148,
                                164
                            ],
                            "text": "gamblingtwitter"
                        },
                        {
                            "indices": [
                                165,
                                169
                            ],
                            "text": "NHL"
                        },
                        {
                            "indices": [
                                170,
                                179
                            ],
                            "text": "football"
                        },
                        {
                            "indices": [
                                180,
                                184
                            ],
                            "text": "MMA"
                        },
                        {
                            "indices": [
                                185,
                                189
                            ],
                            "text": "UFC"
                        },
                        {
                            "indices": [
                                190,
                                194
                            ],
                            "text": "dfs"
                        },
                        {
                            "indices": [
                                195,
                                202
                            ],
                            "text": "parlay"
                        },
                        {
                            "indices": [
                                203,
                                210
                            ],
                            "text": "Sports"
                        },
                        {
                            "indices": [
                                211,
                                223
                            ],
                            "text": "sportspicks"
                        },
                        {
                            "indices": [
                                224,
                                233
                            ],
                            "text": "gambling"
                        },
                        {
                            "indices": [
                                234,
                                239
                            ],
                            "text": "Odds"
                        },
                        {
                            "indices": [
                                240,
                                244
                            ],
                            "text": "MLB"
                        },
                        {
                            "indices": [
                                245,
                                258
                            ],
                            "text": "marchmadness"
                        },
                        {
                            "indices": [
                                259,
                                264
                            ],
                            "text": "ncaa"
                        },
                        {
                            "indices": [
                                265,
                                269
                            ],
                            "text": "cbb"
                        },
                        {
                            "indices": [
                                270,
                                276
                            ],
                            "text": "ncaab"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "New pick for Virginia Tech Hokies vs Boston College Eagles https://t.co/gThqSP5kIY #Betting #NCAAF #Sportsbetting #SuperBowl\n#bettingtips #NFLpicks #gamblingtwitter #NHL\n#football #MMA #UFC #dfs #parlay\n#Sports #sportspicks #gambling #Odds\n#MLB #marchmadness #ncaa #cbb #ncaab"
            },
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "New pick for Virginia Tech Hokies vs Boston College Eagles https://t.co/gThqSP5kIY #Betting #NCAAF #Sportsbetting… https://t.co/ge2fjPWK17",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968355069",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://sportstrader.pro:443/pick/10609",
                        "display_url": "sportstrader.pro/pick/10609",
                        "indices": [
                            59,
                            82
                        ],
                        "url": "https://t.co/gThqSP5kIY"
                    },
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221101901997051906",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            115,
                            138
                        ],
                        "url": "https://t.co/ge2fjPWK17"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            83,
                            91
                        ],
                        "text": "Betting"
                    },
                    {
                        "indices": [
                            92,
                            98
                        ],
                        "text": "NCAAF"
                    },
                    {
                        "indices": [
                            99,
                            113
                        ],
                        "text": "Sportsbetting"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 2179,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/884383824968376321/tjWyvxlf_normal.jpg",
                "listed_count": 7,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 63528,
                "description": null,
                "created_at": "Tue Feb 16 19:02:06 +0000 2016",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "ObengDaniel93",
                "id_str": "4920596656",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 4920596656,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/884383824968376321/tjWyvxlf_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/4920596656/1464121008",
                "statuses_count": 55261,
                "follow_request_sent": null,
                "followers_count": 260,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Danny Obeng Boamah",
                "location": "sunyani  Area 4",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102046138466311",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:48:00 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 3,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221097393707347973",
                "in_reply_to_user_id": null,
                "favorite_count": 23,
                "id": 1221097393707347973,
                "text": "Lamptey to start!\nhttps://t.co/X9QB8W5IBl",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.football.london/chelsea-fc/news/chelsea-team-news-lamptey-hull-17627752",
                            "display_url": "football.london/chelsea-fc/new…",
                            "indices": [
                                18,
                                41
                            ],
                            "url": "https://t.co/X9QB8W5IBl"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 780,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1204801445989625856/ooWhT3cz_normal.jpg",
                    "listed_count": 1365,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme15/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 977,
                    "description": "All the latest Chelsea news, rumours and opinion from @Football_LDN. Like us on Facebook for more: https://www.facebook.com/CFCFootball.London/",
                    "created_at": "Thu Feb 04 15:54:16 +0000 2010",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme15/bg.png",
                    "protected": false,
                    "screen_name": "Chelsea_FL",
                    "id_str": "111342458",
                    "profile_link_color": "0084B4",
                    "translator_type": "none",
                    "id": 111342458,
                    "geo_enabled": true,
                    "profile_background_color": "022330",
                    "lang": null,
                    "profile_sidebar_border_color": "A8C7F7",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1204801445989625856/ooWhT3cz_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.football.london/chelsea-fc/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/111342458/1569886360",
                    "statuses_count": 96563,
                    "follow_request_sent": null,
                    "followers_count": 130725,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Chelsea FC News",
                    "location": "London, England",
                    "profile_sidebar_fill_color": "C0DFEC",
                    "notifications": null
                }
            },
            "id": 1221102046138466311,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:29 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @Chelsea_FL: Lamptey to start!\nhttps://t.co/X9QB8W5IBl",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968389435",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.football.london/chelsea-fc/news/chelsea-team-news-lamptey-hull-17627752",
                        "display_url": "football.london/chelsea-fc/new…",
                        "indices": [
                            34,
                            57
                        ],
                        "url": "https://t.co/X9QB8W5IBl"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Chelsea FC News",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 111342458,
                        "screen_name": "Chelsea_FL",
                        "id_str": "111342458"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 91,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1210328122459074561/GZ_KJLbA_normal.jpg",
                "listed_count": 7,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 156986,
                "description": ".✫*ﾟ･ﾟ｡.★.*｡･ﾟ✫*.\n𝕋𝕠 𝕒 𝕡𝕝𝕒𝕔𝕖 𝕟𝕠 𝕠𝕟𝕖 𝕔𝕒𝕟 𝕗𝕚𝕟𝕕 𝕞𝕪 𝕥𝕣𝕖𝕒𝕤𝕦𝕣𝕖 ✫*ﾟ･ﾟ｡.★.*｡･ﾟ✫*.",
                "created_at": "Tue Jan 20 18:20:03 +0000 2015",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "xduygu_arsx",
                "id_str": "2987723974",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 2987723974,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1210328122459074561/GZ_KJLbA_normal.jpg",
                "time_zone": null,
                "url": "http://instagram.com/_xduygu.arsx_",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2987723974/1578050952",
                "statuses_count": 36023,
                "follow_request_sent": null,
                "followers_count": 192,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "᯽𝑆𝑜𝑛𝑔 𝑀𝑖𝑛𝑔𝑖᯽| D-63📍ATEEZ in Berlin",
                "location": "𝑤𝑜𝑛𝑑𝑒𝑟𝑙𝑎𝑛𝑑",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102397126213632",
            "reply_count": 0,
            "retweeted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/Li52G42dyL",
                            "indices": [
                                110,
                                133
                            ],
                            "sizes": {
                                "small": {
                                    "h": 680,
                                    "resize": "fit",
                                    "w": 679
                                },
                                "medium": {
                                    "h": 1026,
                                    "resize": "fit",
                                    "w": 1024
                                },
                                "large": {
                                    "h": 1026,
                                    "resize": "fit",
                                    "w": 1024
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221024514248773638",
                            "expanded_url": "https://twitter.com/atee_zZz/status/1221024642401492993/video/1",
                            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221024514248773638/pu/img/MGmc9rM671n1rZj9.jpg",
                            "id": 1221024514248773638,
                            "additional_media_info": {
                                "monetizable": false
                            },
                            "type": "video",
                            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221024514248773638/pu/img/MGmc9rM671n1rZj9.jpg",
                            "url": "https://t.co/Li52G42dyL",
                            "video_info": {
                                "aspect_ratio": [
                                    512,
                                    513
                                ],
                                "duration_millis": 8308,
                                "variants": [
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/ext_tw_video/1221024514248773638/pu/pl/z679rhlcof3nKpEx.m3u8?tag=10"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 632000,
                                        "url": "https://video.twimg.com/ext_tw_video/1221024514248773638/pu/vid/320x320/6W0-5HnHR7tjKa59.mp4?tag=10"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 2176000,
                                        "url": "https://video.twimg.com/ext_tw_video/1221024514248773638/pu/vid/720x720/YXoP_cTEVvpxuY2i.mp4?tag=10"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 832000,
                                        "url": "https://video.twimg.com/ext_tw_video/1221024514248773638/pu/vid/360x360/b_5tX_BaX6jY8tt7.mp4?tag=10"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 10:58:54 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "retweet_count": 167,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221024642401492993",
                "in_reply_to_user_id": null,
                "favorite_count": 479,
                "id": 1221024642401492993,
                "text": "Hongjoong is not only great leader, producer, rapper, singer and dancer. he's also a superior football player https://t.co/Li52G42dyL",
                "place": null,
                "lang": "en",
                "quote_count": 15,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 6,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/Li52G42dyL",
                            "indices": [
                                110,
                                133
                            ],
                            "sizes": {
                                "small": {
                                    "h": 680,
                                    "resize": "fit",
                                    "w": 679
                                },
                                "medium": {
                                    "h": 1026,
                                    "resize": "fit",
                                    "w": 1024
                                },
                                "large": {
                                    "h": 1026,
                                    "resize": "fit",
                                    "w": 1024
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221024514248773638",
                            "expanded_url": "https://twitter.com/atee_zZz/status/1221024642401492993/video/1",
                            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221024514248773638/pu/img/MGmc9rM671n1rZj9.jpg",
                            "id": 1221024514248773638,
                            "additional_media_info": {
                                "monetizable": false
                            },
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221024514248773638/pu/img/MGmc9rM671n1rZj9.jpg",
                            "url": "https://t.co/Li52G42dyL"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    109
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 121,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220677447408144385/53hLGbdE_normal.jpg",
                    "listed_count": 102,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 12473,
                    "description": "always by your side ∞ @ATEEZofficial 🖤 #홍중 • ☁️🌥⛅️🌤☀️",
                    "created_at": "Fri May 18 22:11:22 +0000 2018",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "atee_zZz",
                    "id_str": "997600558587531264",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 997600558587531264,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1220677447408144385/53hLGbdE_normal.jpg",
                    "time_zone": null,
                    "url": "https://www.youtube.com/channel/UCk34X7QR6MUNiQd3B9fVahg",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/997600558587531264/1579867213",
                    "statuses_count": 20582,
                    "follow_request_sent": null,
                    "followers_count": 6644,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "kenny",
                    "location": "since 18th May • 평홍만 • 아이콘 ",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102397126213632,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:53 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @atee_zZz: Hongjoong is not only great leader, producer, rapper, singer and dancer. he's also a superior football player https://t.co/Li…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968473117",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "kenny",
                        "indices": [
                            3,
                            12
                        ],
                        "id": 997600558587531264,
                        "screen_name": "atee_zZz",
                        "id_str": "997600558587531264"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 2570,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1164200838446878725/1z4syNXH_normal.jpg",
                "listed_count": 14,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 6175,
                "description": "never give up on what you love",
                "created_at": "Sun Jun 12 10:31:29 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "umusajibrin",
                "id_str": "315727967",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 315727967,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1164200838446878725/1z4syNXH_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/315727967/1562237730",
                "statuses_count": 10823,
                "follow_request_sent": null,
                "followers_count": 392,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Osment zaki",
                "location": "Lagos, Nigeria",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102150794780674",
            "reply_count": 0,
            "retweeted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/kO28bbLo7y",
                            "indices": [
                                113,
                                136
                            ],
                            "sizes": {
                                "small": {
                                    "h": 360,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 413,
                                    "resize": "fit",
                                    "w": 780
                                },
                                "large": {
                                    "h": 413,
                                    "resize": "fit",
                                    "w": 780
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221096194405031936",
                            "expanded_url": "https://twitter.com/DailyStar_Sport/status/1221096209420640256/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI0hOgX4AAK04S.jpg",
                            "id": 1221096194405031936,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI0hOgX4AAK04S.jpg",
                            "url": "https://t.co/kO28bbLo7y"
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:43:17 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 2,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221096209420640256",
                "in_reply_to_user_id": null,
                "favorite_count": 7,
                "id": 1221096209420640256,
                "text": "Man Utd reach transfer 'agreement' with Sporting Lisbon over key Bruno Fernandes detail\n\nhttps://t.co/oIS7lJOIlB https://t.co/kO28bbLo7y",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.dailystar.co.uk/sport/football/man-utd-reach-transfer-agreement-21358735",
                            "display_url": "dailystar.co.uk/sport/football…",
                            "indices": [
                                89,
                                112
                            ],
                            "url": "https://t.co/oIS7lJOIlB"
                        }
                    ],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/kO28bbLo7y",
                            "indices": [
                                113,
                                136
                            ],
                            "sizes": {
                                "small": {
                                    "h": 360,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 413,
                                    "resize": "fit",
                                    "w": 780
                                },
                                "large": {
                                    "h": 413,
                                    "resize": "fit",
                                    "w": 780
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221096194405031936",
                            "expanded_url": "https://twitter.com/DailyStar_Sport/status/1221096209420640256/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI0hOgX4AAK04S.jpg",
                            "id": 1221096194405031936,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI0hOgX4AAK04S.jpg",
                            "url": "https://t.co/kO28bbLo7y"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    112
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 628,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1078570606797508608/FeH5pmUh_normal.jpg",
                    "listed_count": 521,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 147,
                    "description": "Your official Daily Star sport Twitter page. All the breaking sport news, live coverage, expert opinion and more.",
                    "created_at": "Wed May 27 15:51:45 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "DailyStar_Sport",
                    "id_str": "42910151",
                    "profile_link_color": "B60000",
                    "translator_type": "none",
                    "id": 42910151,
                    "geo_enabled": true,
                    "profile_background_color": "E0072A",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1078570606797508608/FeH5pmUh_normal.jpg",
                    "time_zone": null,
                    "url": "https://www.dailystar.co.uk/sport/football",
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/42910151/1515076524",
                    "statuses_count": 99974,
                    "follow_request_sent": null,
                    "followers_count": 40115,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Daily Star Sport",
                    "location": "United Kingdom",
                    "profile_sidebar_fill_color": "FF0000",
                    "notifications": null
                }
            },
            "id": 1221102150794780674,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:54 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @DailyStar_Sport: Man Utd reach transfer 'agreement' with Sporting Lisbon over key Bruno Fernandes detail\n\nhttps://t.co/oIS7lJOIlB https…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968414387",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.dailystar.co.uk/sport/football/man-utd-reach-transfer-agreement-21358735",
                        "display_url": "dailystar.co.uk/sport/football…",
                        "indices": [
                            110,
                            133
                        ],
                        "url": "https://t.co/oIS7lJOIlB"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Daily Star Sport",
                        "indices": [
                            3,
                            19
                        ],
                        "id": 42910151,
                        "screen_name": "DailyStar_Sport",
                        "id_str": "42910151"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 221,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/947114930515439616/efHE4_FW_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 13858,
                "description": "Geek and Gooner. Pretty much covers it.",
                "created_at": "Sat Mar 19 13:49:33 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Demz87",
                "id_str": "268796776",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 268796776,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/947114930515439616/efHE4_FW_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/268796776/1449056145",
                "statuses_count": 768,
                "follow_request_sent": null,
                "followers_count": 85,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Demola Adewunmi",
                "location": "London",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102381640888320",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        206
                    ],
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "https://anchor.fm/Banditfootballfans/episodes/Bandit-Football-Fans---Episode-002---Jones--Stones--Luiz-ft--Deji--Kiz--Dee--Ben--Kelechi--Calum-eadp53",
                                "display_url": "anchor.fm/Banditfootball…",
                                "indices": [
                                    155,
                                    178
                                ],
                                "url": "https://t.co/c92MfxSRxd"
                            }
                        ],
                        "hashtags": [
                            {
                                "indices": [
                                    180,
                                    189
                                ],
                                "text": "football"
                            },
                            {
                                "indices": [
                                    190,
                                    197
                                ],
                                "text": "Banter"
                            },
                            {
                                "indices": [
                                    198,
                                    206
                                ],
                                "text": "podcast"
                            }
                        ],
                        "user_mentions": [
                            {
                                "name": "Anchor",
                                "indices": [
                                    146,
                                    153
                                ],
                                "id": 3044472165,
                                "screen_name": "anchor",
                                "id_str": "3044472165"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "Listen to Bandit Football Fans - Episode 002 - Jones, Stones &amp; Luiz ft. Deji, Kiz, Dee, Ben, Kelechi &amp; Calum from Bandit Football Fans on @anchor: https://t.co/c92MfxSRxd\n\n#football #Banter #podcast"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 13:51:13 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "retweet_count": 1,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221068007474106368",
                "in_reply_to_user_id": null,
                "favorite_count": 1,
                "id": 1221068007474106368,
                "text": "Listen to Bandit Football Fans - Episode 002 - Jones, Stones &amp; Luiz ft. Deji, Kiz, Dee, Ben, Kelechi &amp; Calum from B… https://t.co/g1KPmEEBNQ",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221068007474106368",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                125,
                                148
                            ],
                            "url": "https://t.co/g1KPmEEBNQ"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 2,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1217745919988457473/9okgw4rm_normal.jpg",
                    "listed_count": 0,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 0,
                    "description": "Real football opinions, real football banter, real football fans. Strap in, put on a crash helmet and grab your popcorn. We're going in...",
                    "created_at": "Thu Jan 16 09:48:20 +0000 2020",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "FansBandit",
                    "id_str": "1217745323973582848",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1217745323973582848,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1217745919988457473/9okgw4rm_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "statuses_count": 6,
                    "follow_request_sent": null,
                    "followers_count": 3,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "BanditFootballFansPodcast",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102381640888320,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:49 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @FansBandit: Listen to Bandit Football Fans - Episode 002 - Jones, Stones &amp; Luiz ft. Deji, Kiz, Dee, Ben, Kelechi &amp; Calum from Bandit Fo…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968469425",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "BanditFootballFansPodcast",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 1217745323973582848,
                        "screen_name": "FansBandit",
                        "id_str": "1217745323973582848"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 274,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/997933176558268416/kid5fV4h_normal.jpg",
                "listed_count": 4,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 1171,
                "description": null,
                "created_at": "Sun Nov 28 18:35:54 +0000 2010",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "johnkelly1965",
                "id_str": "220748625",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 220748625,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/997933176558268416/kid5fV4h_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 12722,
                "follow_request_sent": null,
                "followers_count": 78,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "John Kelly",
                "location": "stockport ",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102625472598016",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        163
                    ],
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "https://www.pscp.tv/w/1BRKjqgYkOexw",
                                "display_url": "pscp.tv/w/1BRKjqgYkOexw",
                                "indices": [
                                    140,
                                    163
                                ],
                                "url": "https://t.co/tEw2NPRdP5"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [
                            {
                                "name": "Paddy Power",
                                "indices": [
                                    103,
                                    114
                                ],
                                "id": 14387275,
                                "screen_name": "paddypower",
                                "id_str": "14387275"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "\"They are not a well coached team\"\n\nDamien Delaney thinks Manchester United aren't coached well ⬇️\n\n📺⚽️@paddypower | Saturday Football Show\nhttps://t.co/tEw2NPRdP5"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:58:35 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 1,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221100057069608960",
                "in_reply_to_user_id": null,
                "favorite_count": 1,
                "id": 1221100057069608960,
                "text": "\"They are not a well coached team\"\n\nDamien Delaney thinks Manchester United aren't coached well ⬇️\n\n📺⚽️@paddypower… https://t.co/ii3Mwt9EMB",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221100057069608960",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                116,
                                139
                            ],
                            "url": "https://t.co/ii3Mwt9EMB"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "Paddy Power",
                            "indices": [
                                103,
                                114
                            ],
                            "id": 14387275,
                            "screen_name": "paddypower",
                            "id_str": "14387275"
                        }
                    ],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1441,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1118144075495092226/chGMDo8c_normal.png",
                    "listed_count": 469,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 4150,
                    "description": "#OTBAM live @ 7.30am - YouTube & http://offtheball.com 🎧📱\n\nOff The Ball FM - Mon-Fri 7pm, Sat+Sun 1pm | @NewstalkFM & OTB Sports Radio 🎧📱",
                    "created_at": "Sun Oct 30 16:32:42 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "offtheball",
                    "id_str": "401488459",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 401488459,
                    "geo_enabled": true,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1118144075495092226/chGMDo8c_normal.png",
                    "time_zone": null,
                    "url": "http://www.offtheball.com",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/401488459/1572609340",
                    "statuses_count": 105565,
                    "follow_request_sent": null,
                    "followers_count": 113910,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Off The Ball",
                    "location": "🎙 - 📻 - 🎧 - 🎥",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102625472598016,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:47 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @offtheball: \"They are not a well coached team\"\n\nDamien Delaney thinks Manchester United aren't coached well ⬇️\n\n📺⚽️@paddypower | Saturd…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968527559",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Off The Ball",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 401488459,
                        "screen_name": "offtheball",
                        "id_str": "401488459"
                    },
                    {
                        "name": "Paddy Power",
                        "indices": [
                            119,
                            130
                        ],
                        "id": 14387275,
                        "screen_name": "paddypower",
                        "id_str": "14387275"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 11,
                "profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 0,
                "description": "gone golfing , mowing or drywallin ,be blessed",
                "created_at": "Fri Jan 06 05:07:15 +0000 2012",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "degruver",
                "id_str": "456365432",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 456365432,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 13,
                "follow_request_sent": null,
                "followers_count": 5,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Dennis  Hodges",
                "location": "Bishop Ca.",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102809006800897",
            "reply_count": 0,
            "id": 1221102809006800897,
            "in_reply_to_user_id": 714674839,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:31 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "@DeForestBuckner  Love the football hands  , pix looks like two VICTORY SIGNALS ! Go Ninets",
            "in_reply_to_user_id_str": "714674839",
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "DeForestBuckner",
            "place": null,
            "timestamp_ms": "1579968571317",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "DeForest Buckner",
                        "indices": [
                            0,
                            16
                        ],
                        "id": 714674839,
                        "screen_name": "DeForestBuckner",
                        "id_str": "714674839"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 0,
                "profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 0,
                "description": null,
                "created_at": "Sat Jan 25 16:04:18 +0000 2020",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "Patrici54297178",
                "id_str": "1221101467152658434",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1221101467152658434,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 3,
                "follow_request_sent": null,
                "followers_count": 0,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Patricia",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101901946728451",
            "reply_count": 0,
            "quoted_status_id": 1221100121380859904,
            "quoted_status_id_str": "1221100121380859904",
            "id": 1221101901946728451,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:55 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    240
                ],
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "(ncwp) ⬇⬇ Porn daddy needed sex porn omegaverse au tits pussy penis vagina anal doggy style gaming fortnite 18+ sugar mommy minecraft boobs ass boyfriend girlfriend kpoop football Porno p wpolitics photography nsfw choking spanking twerk ⬇⬇"
            },
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "(ncwp) ⬇⬇ Porn daddy needed sex porn omegaverse au tits pussy penis vagina anal doggy style gaming fortnite 18+ sug… https://t.co/WcByQ8xe9J",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968355057",
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221101901946728451",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/WcByQ8xe9J"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 571,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000452487733/fe421884a142f3c453946af974f35d5a_normal.jpeg",
                "listed_count": 2,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme13/bg.gif",
                "default_profile_image": false,
                "favourites_count": 1927,
                "description": "@ManUtd",
                "created_at": "Wed May 29 11:47:47 +0000 2013",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme13/bg.gif",
                "protected": false,
                "screen_name": "nevillecolaco94",
                "id_str": "1467073994",
                "profile_link_color": "1B95E0",
                "translator_type": "none",
                "id": 1467073994,
                "geo_enabled": true,
                "profile_background_color": "F0E2CE",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/378800000452487733/fe421884a142f3c453946af974f35d5a_normal.jpeg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1467073994/1579364573",
                "statuses_count": 3472,
                "follow_request_sent": null,
                "followers_count": 263,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Neville",
                "location": "Lake View County ,Kepler-452b",
                "profile_sidebar_fill_color": "FFFFFF",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101959983161344",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        280
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Pep Guardiola wants League Cup scrapped. \n\nPep Guardiola wants FA Cup replays scrapped. \n\nPep Guardiola wants... \n\nDoes Pep Guardiola realise there's actually hundreds of football clubs not rolling in blood money who live for and are often funded by such occasions.  Smug elitism."
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 18:41:11 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 1634,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220778591895609345",
                "in_reply_to_user_id": null,
                "favorite_count": 12317,
                "id": 1220778591895609345,
                "text": "Pep Guardiola wants League Cup scrapped. \n\nPep Guardiola wants FA Cup replays scrapped. \n\nPep Guardiola wants...… https://t.co/aqp8Zz5RbK",
                "place": null,
                "lang": "en",
                "quote_count": 177,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 371,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220778591895609345",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                114,
                                137
                            ],
                            "url": "https://t.co/aqp8Zz5RbK"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1766,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/949697816087224320/3aRObHuB_normal.jpg",
                    "listed_count": 287,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme8/bg.gif",
                    "default_profile_image": false,
                    "favourites_count": 45165,
                    "description": "So you run and you run to catch up with the sun but it's sinking, racing around to come up behind you again.\n\nSports writer of year once upon a time.",
                    "created_at": "Tue Jan 25 14:46:59 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme8/bg.gif",
                    "protected": false,
                    "screen_name": "EwanMacKenna",
                    "id_str": "242759237",
                    "profile_link_color": "ABB8C2",
                    "translator_type": "none",
                    "id": 242759237,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/949697816087224320/3aRObHuB_normal.jpg",
                    "time_zone": null,
                    "url": "http://ewanmackenna.wordpress.com/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/242759237/1549712606",
                    "statuses_count": 91660,
                    "follow_request_sent": null,
                    "followers_count": 32727,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "Ewan MacKenna",
                    "location": "Portugal. Brazil. Ireland. ",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "id": 1221101959983161344,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:08 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @EwanMacKenna: Pep Guardiola wants League Cup scrapped. \n\nPep Guardiola wants FA Cup replays scrapped. \n\nPep Guardiola wants... \n\nDoes P…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968368894",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Ewan MacKenna",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 242759237,
                        "screen_name": "EwanMacKenna",
                        "id_str": "242759237"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat May 03 16:20:09 +0000 2014",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
                "retweet_count": 537,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "462627683458097153",
                "in_reply_to_user_id": null,
                "favorite_count": 488,
                "id": 462627683458097153,
                "text": "Ole Gunnar Solskjaer after Cardiff's relegation: \"They didn't deserve to lose. It's about showing character &amp; bouncing back next season\"",
                "place": null,
                "lang": "en",
                "quote_count": 237,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 58,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 83,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1204508293596635137/ssjmIYjS_normal.jpg",
                    "listed_count": 26237,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 1759,
                    "description": "The official Twitter account of the Premier League 📱 @OfficialFPL | 🇮🇳 @PLforIndia | 🇺🇸 @PLinUSA Join us on YouTube 👉 http://youtube.com/premierleague",
                    "created_at": "Wed Jul 27 21:09:32 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "premierleague",
                    "id_str": "343627165",
                    "profile_link_color": "93A644",
                    "translator_type": "none",
                    "id": 343627165,
                    "geo_enabled": true,
                    "profile_background_color": "050528",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "FFFFFF",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1204508293596635137/ssjmIYjS_normal.jpg",
                    "time_zone": null,
                    "url": "http://premierleague.com",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/343627165/1579880436",
                    "statuses_count": 113416,
                    "follow_request_sent": null,
                    "followers_count": 21264126,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "Premier League",
                    "location": null,
                    "profile_sidebar_fill_color": "171838",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 2295,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1053542822157189120/ETqiyywl_normal.jpg",
                "listed_count": 26,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 7258,
                "description": "Man united | Red Devils  |Team SIRKAL |We're the brave ones|| Baily FC 🔴",
                "created_at": "Tue Feb 09 09:00:54 +0000 2010",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Oskidhe",
                "id_str": "112665699",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 112665699,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1053542822157189120/ETqiyywl_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/112665699/1494507091",
                "statuses_count": 90839,
                "follow_request_sent": null,
                "followers_count": 3483,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Oskidhe",
                "location": "Nairobi ",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102385050914817",
            "reply_count": 0,
            "quoted_status_id": 462627683458097153,
            "quoted_status_id_str": "462627683458097153",
            "id": 1221102385050914817,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:50 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "😂😂😂 The world's best known football brand hired this guy as manager #mufc",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968470238",
            "entities": {
                "urls": [],
                "hashtags": [
                    {
                        "indices": [
                            68,
                            73
                        ],
                        "text": "mufc"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/xmgRAOUel5",
                "expanded": "https://twitter.com/premierleague/status/462627683458097153",
                "display": "twitter.com/premierleague/…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 75,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1105873145850941442/WYAbJduk_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 169,
                "description": "#1 sports betting marketplace\n🔍 Full transparency\n📊 Live odds\n⛏️ Users picks\n🏺 Picks history\n📈 User statistics\n↘️ See you there https://t.co/QjNXr91nuO",
                "created_at": "Wed Mar 13 16:47:26 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "SportsTrader888",
                "id_str": "1105873010446221312",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1105873010446221312,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1105873145850941442/WYAbJduk_normal.jpg",
                "time_zone": null,
                "url": "http://sportstrader.pro",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1105873010446221312/1552495799",
                "statuses_count": 8915,
                "follow_request_sent": null,
                "followers_count": 138,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "SportsTrader.Pro",
                "location": "Delaware, USA",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102251047112705",
            "reply_count": 0,
            "id": 1221102251047112705,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:18 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    274
                ],
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://sportstrader.pro:443/pick/10611",
                            "display_url": "sportstrader.pro/pick/10611",
                            "indices": [
                                52,
                                75
                            ],
                            "url": "https://t.co/TOPvLDNWcL"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                76,
                                84
                            ],
                            "text": "Betting"
                        },
                        {
                            "indices": [
                                85,
                                91
                            ],
                            "text": "NCAAF"
                        },
                        {
                            "indices": [
                                92,
                                106
                            ],
                            "text": "Sportsbetting"
                        },
                        {
                            "indices": [
                                107,
                                111
                            ],
                            "text": "MLB"
                        },
                        {
                            "indices": [
                                112,
                                122
                            ],
                            "text": "SuperBowl"
                        },
                        {
                            "indices": [
                                123,
                                135
                            ],
                            "text": "bettingtips"
                        },
                        {
                            "indices": [
                                136,
                                145
                            ],
                            "text": "NFLpicks"
                        },
                        {
                            "indices": [
                                146,
                                162
                            ],
                            "text": "gamblingtwitter"
                        },
                        {
                            "indices": [
                                163,
                                167
                            ],
                            "text": "NHL"
                        },
                        {
                            "indices": [
                                168,
                                177
                            ],
                            "text": "football"
                        },
                        {
                            "indices": [
                                178,
                                182
                            ],
                            "text": "MMA"
                        },
                        {
                            "indices": [
                                183,
                                187
                            ],
                            "text": "UFC"
                        },
                        {
                            "indices": [
                                188,
                                192
                            ],
                            "text": "dfs"
                        },
                        {
                            "indices": [
                                193,
                                200
                            ],
                            "text": "parlay"
                        },
                        {
                            "indices": [
                                201,
                                208
                            ],
                            "text": "Sports"
                        },
                        {
                            "indices": [
                                209,
                                221
                            ],
                            "text": "sportspicks"
                        },
                        {
                            "indices": [
                                222,
                                231
                            ],
                            "text": "gambling"
                        },
                        {
                            "indices": [
                                232,
                                237
                            ],
                            "text": "Odds"
                        },
                        {
                            "indices": [
                                238,
                                242
                            ],
                            "text": "MLB"
                        },
                        {
                            "indices": [
                                243,
                                256
                            ],
                            "text": "marchmadness"
                        },
                        {
                            "indices": [
                                257,
                                262
                            ],
                            "text": "ncaa"
                        },
                        {
                            "indices": [
                                263,
                                267
                            ],
                            "text": "cbb"
                        },
                        {
                            "indices": [
                                268,
                                274
                            ],
                            "text": "ncaab"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "New pick for Clemson Tigers vs Louisville Cardinals https://t.co/TOPvLDNWcL #Betting #NCAAF #Sportsbetting #MLB #SuperBowl\n#bettingtips #NFLpicks #gamblingtwitter #NHL\n#football #MMA #UFC #dfs #parlay\n#Sports #sportspicks #gambling #Odds\n#MLB #marchmadness #ncaa #cbb #ncaab"
            },
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "New pick for Clemson Tigers vs Louisville Cardinals https://t.co/TOPvLDNWcL #Betting #NCAAF #Sportsbetting #MLB… https://t.co/KFzrhbsKi6",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968438289",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://sportstrader.pro:443/pick/10611",
                        "display_url": "sportstrader.pro/pick/10611",
                        "indices": [
                            52,
                            75
                        ],
                        "url": "https://t.co/TOPvLDNWcL"
                    },
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102251047112705",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            113,
                            136
                        ],
                        "url": "https://t.co/KFzrhbsKi6"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            76,
                            84
                        ],
                        "text": "Betting"
                    },
                    {
                        "indices": [
                            85,
                            91
                        ],
                        "text": "NCAAF"
                    },
                    {
                        "indices": [
                            92,
                            106
                        ],
                        "text": "Sportsbetting"
                    },
                    {
                        "indices": [
                            107,
                            111
                        ],
                        "text": "MLB"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 75,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1105873145850941442/WYAbJduk_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 169,
                "description": "#1 sports betting marketplace\n🔍 Full transparency\n📊 Live odds\n⛏️ Users picks\n🏺 Picks history\n📈 User statistics\n↘️ See you there https://t.co/QjNXr91nuO",
                "created_at": "Wed Mar 13 16:47:26 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "SportsTrader888",
                "id_str": "1105873010446221312",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1105873010446221312,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1105873145850941442/WYAbJduk_normal.jpg",
                "time_zone": null,
                "url": "http://sportstrader.pro",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1105873010446221312/1552495799",
                "statuses_count": 8917,
                "follow_request_sent": null,
                "followers_count": 138,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "SportsTrader.Pro",
                "location": "Delaware, USA",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102624373723137",
            "reply_count": 0,
            "id": 1221102624373723137,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:47 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    274
                ],
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://sportstrader.pro:443/pick/10613",
                            "display_url": "sportstrader.pro/pick/10613",
                            "indices": [
                                52,
                                75
                            ],
                            "url": "https://t.co/gjdvjqPIfO"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                76,
                                84
                            ],
                            "text": "Betting"
                        },
                        {
                            "indices": [
                                85,
                                91
                            ],
                            "text": "NCAAF"
                        },
                        {
                            "indices": [
                                92,
                                106
                            ],
                            "text": "Sportsbetting"
                        },
                        {
                            "indices": [
                                107,
                                111
                            ],
                            "text": "MLB"
                        },
                        {
                            "indices": [
                                112,
                                122
                            ],
                            "text": "SuperBowl"
                        },
                        {
                            "indices": [
                                123,
                                135
                            ],
                            "text": "bettingtips"
                        },
                        {
                            "indices": [
                                136,
                                145
                            ],
                            "text": "NFLpicks"
                        },
                        {
                            "indices": [
                                146,
                                162
                            ],
                            "text": "gamblingtwitter"
                        },
                        {
                            "indices": [
                                163,
                                167
                            ],
                            "text": "NHL"
                        },
                        {
                            "indices": [
                                168,
                                177
                            ],
                            "text": "football"
                        },
                        {
                            "indices": [
                                178,
                                182
                            ],
                            "text": "MMA"
                        },
                        {
                            "indices": [
                                183,
                                187
                            ],
                            "text": "UFC"
                        },
                        {
                            "indices": [
                                188,
                                192
                            ],
                            "text": "dfs"
                        },
                        {
                            "indices": [
                                193,
                                200
                            ],
                            "text": "parlay"
                        },
                        {
                            "indices": [
                                201,
                                208
                            ],
                            "text": "Sports"
                        },
                        {
                            "indices": [
                                209,
                                221
                            ],
                            "text": "sportspicks"
                        },
                        {
                            "indices": [
                                222,
                                231
                            ],
                            "text": "gambling"
                        },
                        {
                            "indices": [
                                232,
                                237
                            ],
                            "text": "Odds"
                        },
                        {
                            "indices": [
                                238,
                                242
                            ],
                            "text": "MLB"
                        },
                        {
                            "indices": [
                                243,
                                256
                            ],
                            "text": "marchmadness"
                        },
                        {
                            "indices": [
                                257,
                                262
                            ],
                            "text": "ncaa"
                        },
                        {
                            "indices": [
                                263,
                                267
                            ],
                            "text": "cbb"
                        },
                        {
                            "indices": [
                                268,
                                274
                            ],
                            "text": "ncaab"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "New pick for Louisiana Tech Bulldogs vs UAB Blazers https://t.co/gjdvjqPIfO #Betting #NCAAF #Sportsbetting #MLB #SuperBowl\n#bettingtips #NFLpicks #gamblingtwitter #NHL\n#football #MMA #UFC #dfs #parlay\n#Sports #sportspicks #gambling #Odds\n#MLB #marchmadness #ncaa #cbb #ncaab"
            },
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "New pick for Louisiana Tech Bulldogs vs UAB Blazers https://t.co/gjdvjqPIfO #Betting #NCAAF #Sportsbetting #MLB… https://t.co/wL3LryuyK7",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968527297",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://sportstrader.pro:443/pick/10613",
                        "display_url": "sportstrader.pro/pick/10613",
                        "indices": [
                            52,
                            75
                        ],
                        "url": "https://t.co/gjdvjqPIfO"
                    },
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102624373723137",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            113,
                            136
                        ],
                        "url": "https://t.co/wL3LryuyK7"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            76,
                            84
                        ],
                        "text": "Betting"
                    },
                    {
                        "indices": [
                            85,
                            91
                        ],
                        "text": "NCAAF"
                    },
                    {
                        "indices": [
                            92,
                            106
                        ],
                        "text": "Sportsbetting"
                    },
                    {
                        "indices": [
                            107,
                            111
                        ],
                        "text": "MLB"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 2552,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1208049684159385603/PxRiTc2G_normal.jpg",
                "listed_count": 5,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 3128,
                "description": "@individbarbham Head Promoter, run @fresh_thursdays @brunchhiphopbhm,@darktraits @enjoyclothinguk Owner. MY GAAAAAD!!! Chin Rub lover.",
                "created_at": "Wed Jan 14 19:42:08 +0000 2015",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "manlikebaldwin",
                "id_str": "2983168236",
                "profile_link_color": "F5ABB5",
                "translator_type": "none",
                "id": 2983168236,
                "geo_enabled": true,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1208049684159385603/PxRiTc2G_normal.jpg",
                "time_zone": null,
                "url": "https://youtu.be/6WM3hOT_Tv4",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2983168236/1548627463",
                "statuses_count": 4713,
                "follow_request_sent": null,
                "followers_count": 1594,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "Kacey Jones",
                "location": "Birmingham",
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102098282164226",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        244
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/Y31NS3Paqk",
                                "indices": [
                                    245,
                                    268
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 385,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 480,
                                        "resize": "fit",
                                        "w": 848
                                    },
                                    "large": {
                                        "h": 480,
                                        "resize": "fit",
                                        "w": 848
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220707863133331456",
                                "expanded_url": "https://twitter.com/FREDSZ_/status/1220707969207296000/video/1",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1220707863133331456/pu/img/iKGSsTxTUgP0IWvu.jpg",
                                "id": 1220707863133331456,
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1220707863133331456/pu/img/iKGSsTxTUgP0IWvu.jpg",
                                "url": "https://t.co/Y31NS3Paqk",
                                "video_info": {
                                    "aspect_ratio": [
                                        53,
                                        30
                                    ],
                                    "duration_millis": 40160,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 256000,
                                            "url": "https://video.twimg.com/ext_tw_video/1220707863133331456/pu/vid/476x270/N3a2W2lK3KgMUknr.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/ext_tw_video/1220707863133331456/pu/vid/848x480/dPi-NBRK2OLj-nya.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1220707863133331456/pu/pl/K6RRxRAZBAoaZUxs.m3u8?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/ext_tw_video/1220707863133331456/pu/vid/636x360/p54U8WhwaOAPTvfk.mp4?tag=10"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/Y31NS3Paqk",
                                "indices": [
                                    245,
                                    268
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 385,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 480,
                                        "resize": "fit",
                                        "w": 848
                                    },
                                    "large": {
                                        "h": 480,
                                        "resize": "fit",
                                        "w": 848
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220707863133331456",
                                "expanded_url": "https://twitter.com/FREDSZ_/status/1220707969207296000/video/1",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1220707863133331456/pu/img/iKGSsTxTUgP0IWvu.jpg",
                                "id": 1220707863133331456,
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1220707863133331456/pu/img/iKGSsTxTUgP0IWvu.jpg",
                                "url": "https://t.co/Y31NS3Paqk",
                                "video_info": {
                                    "aspect_ratio": [
                                        53,
                                        30
                                    ],
                                    "duration_millis": 40160,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 256000,
                                            "url": "https://video.twimg.com/ext_tw_video/1220707863133331456/pu/vid/476x270/N3a2W2lK3KgMUknr.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/ext_tw_video/1220707863133331456/pu/vid/848x480/dPi-NBRK2OLj-nya.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1220707863133331456/pu/pl/K6RRxRAZBAoaZUxs.m3u8?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/ext_tw_video/1220707863133331456/pu/vid/636x360/p54U8WhwaOAPTvfk.mp4?tag=10"
                                        }
                                    ]
                                }
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [
                            {
                                "name": "DJ Dougie Fresh",
                                "indices": [
                                    61,
                                    75
                                ],
                                "id": 35909195,
                                "screen_name": "DougieFreshDJ",
                                "id_str": "35909195"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "It's been a LONG time coming... and its finally here! Me and @DougieFreshDJ finally got the ball rolling with a football podcast show and it's all about one thing... the love of the game! \n\nLike and RT!!!!! \n\nFull video will soon be uploaded!!! https://t.co/Y31NS3Paqk"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 14:00:34 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "retweet_count": 167,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220707969207296000",
                "in_reply_to_user_id": null,
                "favorite_count": 233,
                "id": 1220707969207296000,
                "text": "It's been a LONG time coming... and its finally here! Me and @DougieFreshDJ finally got the ball rolling with a foo… https://t.co/NBbkkeWYoG",
                "place": null,
                "lang": "en",
                "quote_count": 40,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 20,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220707969207296000",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/NBbkkeWYoG"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "DJ Dougie Fresh",
                            "indices": [
                                61,
                                75
                            ],
                            "id": 35909195,
                            "screen_name": "DougieFreshDJ",
                            "id_str": "35909195"
                        }
                    ],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1124,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220090304377819137/T7VjKCZO_normal.jpg",
                    "listed_count": 19,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 119239,
                    "description": "#FreshNFredz⚽️\n\nAFC🔴⚪",
                    "created_at": "Fri Apr 22 18:58:14 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "FREDSZ_",
                    "id_str": "286308355",
                    "profile_link_color": "94D487",
                    "translator_type": "none",
                    "id": 286308355,
                    "geo_enabled": true,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1220090304377819137/T7VjKCZO_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/286308355/1579533095",
                    "statuses_count": 184019,
                    "follow_request_sent": null,
                    "followers_count": 2259,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "FREDZ⚽️",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102098282164226,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:41 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @FREDSZ_: It's been a LONG time coming... and its finally here! Me and @DougieFreshDJ finally got the ball rolling with a football podca…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968401867",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "FREDZ⚽️",
                        "indices": [
                            3,
                            11
                        ],
                        "id": 286308355,
                        "screen_name": "FREDSZ_",
                        "id_str": "286308355"
                    },
                    {
                        "name": "DJ Dougie Fresh",
                        "indices": [
                            74,
                            88
                        ],
                        "id": 35909195,
                        "screen_name": "DougieFreshDJ",
                        "id_str": "35909195"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 130,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1042029016469782528/Em5GJOOX_normal.jpg",
                "listed_count": 9,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 4,
                "description": "Google Trends Online is your trending news, entertainment, music, fashion and tech Page. Find out what's trending near you right now.",
                "created_at": "Tue Sep 18 12:30:21 +0000 2018",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "GoogleTrendsOn1",
                "id_str": "1042028047447273473",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1042028047447273473,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1042029016469782528/Em5GJOOX_normal.jpg",
                "time_zone": null,
                "url": "https://www.googletrends.online",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1042028047447273473/1537273973",
                "statuses_count": 315424,
                "follow_request_sent": null,
                "followers_count": 176,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Google Trends Online",
                "location": "Australia",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102613556596743",
            "reply_count": 0,
            "display_text_range": [
                0,
                82
            ],
            "id": 1221102613556596743,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:44 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://publicize.wp.com/\" rel=\"nofollow\">WordPress.com</a>",
            "text": "The Biggest Release Clauses In Football Have Been Revealed https://t.co/kFUZUcEiC3 https://t.co/BdFdEe1Jc6",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968524718",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://tinyurl.com/thrz3vh",
                        "display_url": "tinyurl.com/thrz3vh",
                        "indices": [
                            59,
                            82
                        ],
                        "url": "https://t.co/kFUZUcEiC3"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/BdFdEe1Jc6",
                        "indices": [
                            83,
                            106
                        ],
                        "sizes": {
                            "small": {
                                "h": 414,
                                "resize": "fit",
                                "w": 648
                            },
                            "medium": {
                                "h": 414,
                                "resize": "fit",
                                "w": 648
                            },
                            "large": {
                                "h": 414,
                                "resize": "fit",
                                "w": 648
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221102612168265728",
                        "expanded_url": "https://twitter.com/GoogleTrendsOn1/status/1221102613556596743/photo/1",
                        "media_url_https": "https://pbs.twimg.com/media/EPI6WyiXUAAQ1rU.jpg",
                        "id": 1221102612168265728,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI6WyiXUAAQ1rU.jpg",
                        "url": "https://t.co/BdFdEe1Jc6"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/BdFdEe1Jc6",
                        "indices": [
                            83,
                            106
                        ],
                        "sizes": {
                            "small": {
                                "h": 414,
                                "resize": "fit",
                                "w": 648
                            },
                            "medium": {
                                "h": 414,
                                "resize": "fit",
                                "w": 648
                            },
                            "large": {
                                "h": 414,
                                "resize": "fit",
                                "w": 648
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221102612168265728",
                        "expanded_url": "https://twitter.com/GoogleTrendsOn1/status/1221102613556596743/photo/1",
                        "media_url_https": "https://pbs.twimg.com/media/EPI6WyiXUAAQ1rU.jpg",
                        "id": 1221102612168265728,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI6WyiXUAAQ1rU.jpg",
                        "url": "https://t.co/BdFdEe1Jc6"
                    }
                ]
            },
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 68,
                "profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 830,
                "description": "Studied International Relations @ University of Venda, Preacher, Hustler",
                "created_at": "Sat Oct 24 09:14:42 +0000 2015",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "RamakuelaU2",
                "id_str": "4030583320",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 4030583320,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 164,
                "follow_request_sent": null,
                "followers_count": 2,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "@RamakuelaU",
                "location": "Lwamondo, Thohoyandou (Venda)",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102623895556098",
            "reply_count": 0,
            "display_text_range": [
                13,
                107
            ],
            "id": 1221102623895556098,
            "in_reply_to_user_id": 26456506,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:47 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "@superjourno It was a boring game, if this team which plays bad football wins the league it will be a joke!",
            "in_reply_to_user_id_str": "26456506",
            "in_reply_to_status_id": 1221090722549501957,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "superjourno",
            "place": null,
            "timestamp_ms": "1579968527183",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Mazola J. Molefe",
                        "indices": [
                            0,
                            12
                        ],
                        "id": 26456506,
                        "screen_name": "superjourno",
                        "id_str": "26456506"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": "1221090722549501957",
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 406,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/3109137770/890f8c05394261b427be8a68b1ef1de7_normal.jpeg",
                "listed_count": 11,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 3018,
                "description": "Serving God in politics and in leading my family. @FPAofGA",
                "created_at": "Mon Jan 14 19:13:53 +0000 2013",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "ColeMuzio",
                "id_str": "1089900085",
                "profile_link_color": "3B94D9",
                "translator_type": "none",
                "id": 1089900085,
                "geo_enabled": false,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/3109137770/890f8c05394261b427be8a68b1ef1de7_normal.jpeg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1089900085/1398286502",
                "statuses_count": 4347,
                "follow_request_sent": null,
                "followers_count": 507,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "Cole Muzio",
                "location": "Georgia, USA",
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101893159673856",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        158
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "I hate when athletes come to twitter, and say they are going to do this and that on the field. This is the game of football, man put your head down and work!!"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 18:18:16 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 45,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220772822760534017",
                "in_reply_to_user_id": null,
                "favorite_count": 635,
                "id": 1220772822760534017,
                "text": "I hate when athletes come to twitter, and say they are going to do this and that on the field. This is the game of… https://t.co/7zuDyMIwk0",
                "place": null,
                "lang": "en",
                "quote_count": 7,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 12,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220772822760534017",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                116,
                                139
                            ],
                            "url": "https://t.co/7zuDyMIwk0"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 382,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1175769112418516992/i-QF69i-_normal.jpg",
                    "listed_count": 48,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 1536,
                    "description": "| ΩΨΦ | Linebacker at The Auburn University 🐯 #getlive 3.3. IG: k_britt10",
                    "created_at": "Wed Aug 28 00:02:28 +0000 2013",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "K_Britt10",
                    "id_str": "1705862148",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1705862148,
                    "geo_enabled": true,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1175769112418516992/i-QF69i-_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1705862148/1551646735",
                    "statuses_count": 3182,
                    "follow_request_sent": null,
                    "followers_count": 8654,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Kj Britt",
                    "location": "Auburn, Alabama",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221101893159673856,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:52 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "RT @K_Britt10: I hate when athletes come to twitter, and say they are going to do this and that on the field. This is the game of football,…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968352962",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Kj Britt",
                        "indices": [
                            3,
                            13
                        ],
                        "id": 1705862148,
                        "screen_name": "K_Britt10",
                        "id_str": "1705862148"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1144,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1219395970817019905/fuWhq8Vf_normal.jpg",
                "listed_count": 32,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
                "default_profile_image": false,
                "favourites_count": 176118,
                "description": "I'm 29, support (WORLD FAMOUS) Dundee United! HATE Dundee FC!!!!",
                "created_at": "Thu Dec 15 23:24:35 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
                "protected": false,
                "screen_name": "Pedro83_V",
                "id_str": "437886782",
                "profile_link_color": "009999",
                "translator_type": "none",
                "id": 437886782,
                "geo_enabled": false,
                "profile_background_color": "131516",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1219395970817019905/fuWhq8Vf_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/437886782/1572438828",
                "statuses_count": 163582,
                "follow_request_sent": null,
                "followers_count": 479,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Peter Vaughan",
                "location": null,
                "profile_sidebar_fill_color": "EFEFEF",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102097883680770",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        254
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [
                            {
                                "indices": [
                                    239,
                                    251
                                ],
                                "text": "Tangerine50"
                            }
                        ],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Some fantastic football from United as the link up between Shankland and Sow has got off to a great start. Highlight from first 15 mins: \n\n🔸25 seconds!! Sow denied a lightning opener by the offside flag as he taps home a Harkes rebound. \n\n#Tangerine50 🧡🖤"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:16:23 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 3,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221089439805513728",
                "in_reply_to_user_id": null,
                "favorite_count": 25,
                "id": 1221089439805513728,
                "text": "Some fantastic football from United as the link up between Shankland and Sow has got off to a great start. Highligh… https://t.co/qIcNdsbxco",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 2,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221089439805513728",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/qIcNdsbxco"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 378,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1132936017835638784/iA9S5ivB_normal.jpg",
                    "listed_count": 426,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 1310,
                    "description": "Dundee United FC official account bringing you the latest news and info when it's official. Updated by the Media Dept.🧡🖤",
                    "created_at": "Tue Mar 10 10:57:49 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "dundeeunitedfc",
                    "id_str": "23579243",
                    "profile_link_color": "FF6600",
                    "translator_type": "none",
                    "id": 23579243,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "FF8F1F",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1132936017835638784/iA9S5ivB_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/23579243/1569242466",
                    "statuses_count": 31718,
                    "follow_request_sent": null,
                    "followers_count": 56191,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Dundee United FC",
                    "location": "Tannadice Park",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "id": 1221102097883680770,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:41 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @dundeeunitedfc: Some fantastic football from United as the link up between Shankland and Sow has got off to a great start. Highlight fr…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968401772",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Dundee United FC",
                        "indices": [
                            3,
                            18
                        ],
                        "id": 23579243,
                        "screen_name": "dundeeunitedfc",
                        "id_str": "23579243"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 2288,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1127283867214393344/7-qmrwlZ_normal.jpg",
                "listed_count": 9,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 3181,
                "description": "🙋‍♀️Joshua 24:15. Wife, mom, M. Ed. C&I, Teacher, Blogger, Presenter, Operation Teacher Relief Together for TX (YT Channel for T impacted by natural disaster)",
                "created_at": "Tue Dec 13 04:55:52 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "TraciBrowder",
                "id_str": "435528847",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 435528847,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1127283867214393344/7-qmrwlZ_normal.jpg",
                "time_zone": null,
                "url": "https://tracibrowder.com/",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/435528847/1557600393",
                "statuses_count": 3025,
                "follow_request_sent": null,
                "followers_count": 1172,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "𝐓𝐫𝐚𝐜𝐢 𝐁𝐫𝐨𝐰𝐝𝐞𝐫 #𝐢𝐡𝐞𝐚𝐫𝐭𝐤𝐢𝐝𝐬",
                "location": "Mansfield, TX",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101845885652993",
            "reply_count": 0,
            "id": 1221101845885652993,
            "in_reply_to_user_id": 131948686,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:41 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    257
                ],
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.nbcdfw.com/news/local/teen-makes-wishes-come-true-for-family-who-lost-father/2274161/",
                            "display_url": "nbcdfw.com/news/local/tee…",
                            "indices": [
                                207,
                                230
                            ],
                            "url": "https://t.co/rO2KAq2NOk"
                        },
                        {
                            "expanded_url": "https://www.fox4news.com/news/mansfield-boy-collecting-donations-for-hurricane-harvey-victims",
                            "display_url": "fox4news.com/news/mansfield…",
                            "indices": [
                                234,
                                257
                            ],
                            "url": "https://t.co/kIXAOW9JAB"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "JJ Watt",
                            "indices": [
                                0,
                                7
                            ],
                            "id": 131948686,
                            "screen_name": "JJWatt",
                            "id_str": "131948686"
                        }
                    ],
                    "symbols": []
                },
                "full_text": "@JJWatt watch my 14 yo son’s  Harvey efforts and his 2019 special adoption featured on local news. If you listen 👂 to podcasts, take 10 min to listen to Donovan and his head football coach. You’ll be moved. https://t.co/rO2KAq2NOk    https://t.co/kIXAOW9JAB"
            },
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "@JJWatt watch my 14 yo son’s  Harvey efforts and his 2019 special adoption featured on local news. If you listen 👂… https://t.co/HBY8zIGQ0O",
            "in_reply_to_user_id_str": "131948686",
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "JJWatt",
            "place": null,
            "timestamp_ms": "1579968341691",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221101845885652993",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            116,
                            139
                        ],
                        "url": "https://t.co/HBY8zIGQ0O"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "JJ Watt",
                        "indices": [
                            0,
                            7
                        ],
                        "id": 131948686,
                        "screen_name": "JJWatt",
                        "id_str": "131948686"
                    }
                ],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1195,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1148561910134202369/DRu4DQGV_normal.png",
                "listed_count": 23926,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 7,
                "description": "News, comment and features from The Independent. \n\nTry an ad-free experience with access to premium articles with our app: https://t.co/XGI8DtCR6B",
                "created_at": "Sun Oct 26 00:00:29 +0000 2008",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Independent",
                "id_str": "16973333",
                "profile_link_color": "FC051A",
                "translator_type": "none",
                "id": 16973333,
                "geo_enabled": false,
                "profile_background_color": "EBEBEB",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "333333",
                "verified": true,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1148561910134202369/DRu4DQGV_normal.png",
                "time_zone": null,
                "url": "http://independent.co.uk",
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/16973333/1576571997",
                "statuses_count": 942978,
                "follow_request_sent": null,
                "followers_count": 3019045,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "The Independent",
                "location": "London, England",
                "profile_sidebar_fill_color": "FFFFFF",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101966455197696",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:06:01 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 1,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221101928635142145",
                "in_reply_to_user_id": null,
                "favorite_count": 0,
                "id": 1221101928635142145,
                "text": "Athletic star Inaki Williams ‘sad’ after suffering alleged racist abuse vs Espanyol\n\nhttps://t.co/CqCHfJCl4P",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.independent.co.uk/sport/football/european/inaki-williams-athletic-bilbao-racist-abuse-espanyol-fans-la-liga-news-a9301671.html",
                            "display_url": "independent.co.uk/sport/football…",
                            "indices": [
                                85,
                                108
                            ],
                            "url": "https://t.co/CqCHfJCl4P"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 102,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/981894325297647617/DQQ7XZQU_normal.jpg",
                    "listed_count": 1432,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 119,
                    "description": "Football news, comment and features. Facebook: https://www.facebook.com/TheIndependentFootball Instagram: https://www.instagram.com/independentsport/",
                    "created_at": "Wed Mar 14 10:44:23 +0000 2012",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "IndyFootball",
                    "id_str": "524235256",
                    "profile_link_color": "E41E2B",
                    "translator_type": "none",
                    "id": 524235256,
                    "geo_enabled": false,
                    "profile_background_color": "059426",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/981894325297647617/DQQ7XZQU_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.independent.co.uk/sport/football/",
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/524235256/1573819119",
                    "statuses_count": 130167,
                    "follow_request_sent": null,
                    "followers_count": 98504,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Indy Football",
                    "location": "United Kingdom",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221101966455197696,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:10 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
            "text": "RT @IndyFootball: Athletic star Inaki Williams ‘sad’ after suffering alleged racist abuse vs Espanyol\n\nhttps://t.co/CqCHfJCl4P",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968370437",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.independent.co.uk/sport/football/european/inaki-williams-athletic-bilbao-racist-abuse-espanyol-fans-la-liga-news-a9301671.html",
                        "display_url": "independent.co.uk/sport/football…",
                        "indices": [
                            103,
                            126
                        ],
                        "url": "https://t.co/CqCHfJCl4P"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Indy Football",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 524235256,
                        "screen_name": "IndyFootball",
                        "id_str": "524235256"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        274
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/RJIabUkJ4h",
                                "indices": [
                                    275,
                                    298
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 355,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 626,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 626,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221057233980657666",
                                "expanded_url": "https://twitter.com/cercleofficial/status/1221057239651430401/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIRFbnWkAIVwkB.jpg",
                                "id": 1221057233980657666,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIRFbnWkAIVwkB.jpg",
                                "url": "https://t.co/RJIabUkJ4h"
                            }
                        ]
                    },
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/RJIabUkJ4h",
                                "indices": [
                                    275,
                                    298
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 355,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 626,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 626,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1221057233980657666",
                                "expanded_url": "https://twitter.com/cercleofficial/status/1221057239651430401/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPIRFbnWkAIVwkB.jpg",
                                "id": 1221057233980657666,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPIRFbnWkAIVwkB.jpg",
                                "url": "https://t.co/RJIabUkJ4h"
                            }
                        ],
                        "hashtags": [
                            {
                                "indices": [
                                    47,
                                    54
                                ],
                                "text": "CerAnd"
                            }
                        ],
                        "user_mentions": [
                            {
                                "name": "RSC Anderlecht",
                                "indices": [
                                    14,
                                    28
                                ],
                                "id": 71287752,
                                "screen_name": "rscanderlecht",
                                "id_str": "71287752"
                            },
                            {
                                "name": "Miguel Van Damme",
                                "indices": [
                                    96,
                                    108
                                ],
                                "id": 1000207266,
                                "screen_name": "MiguelVd_16",
                                "id_str": "1000207266"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "Chers fans du @rscanderlecht, la 16e minute de #CerAnd sera non seulement un symbole pour notre @MiguelVd_16, mais aussi pour tous ceux qui luttent. Avec une minute d'applaudissements, nous aimerions leur souhaiter à tous beaucoup de courage. Pouvons-nous compter sur vous ? https://t.co/RJIabUkJ4h"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 13:08:26 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 23,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221057239651430401",
                "in_reply_to_user_id": null,
                "favorite_count": 100,
                "id": 1221057239651430401,
                "text": "Chers fans du @rscanderlecht, la 16e minute de #CerAnd sera non seulement un symbole pour notre @MiguelVd_16, mais… https://t.co/iaDzfVtlf3",
                "place": null,
                "lang": "fr",
                "quote_count": 3,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 10,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221057239651430401",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                116,
                                139
                            ],
                            "url": "https://t.co/iaDzfVtlf3"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                47,
                                54
                            ],
                            "text": "CerAnd"
                        }
                    ],
                    "user_mentions": [
                        {
                            "name": "RSC Anderlecht",
                            "indices": [
                                14,
                                28
                            ],
                            "id": 71287752,
                            "screen_name": "rscanderlecht",
                            "id_str": "71287752"
                        },
                        {
                            "name": "Miguel Van Damme",
                            "indices": [
                                96,
                                108
                            ],
                            "id": 1000207266,
                            "screen_name": "MiguelVd_16",
                            "id_str": "1000207266"
                        }
                    ],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 254,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1212773479545786368/nCHAhx9a_normal.jpg",
                    "listed_count": 243,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
                    "default_profile_image": false,
                    "favourites_count": 1240,
                    "description": "Officieel Twitteraccount van Cercle Brugge KSV | https://t.co/CwnRCpVe5c | https://t.co/LgzWy7aViO | https://t.co/R9kxUbDHfR | #levecercle #WEBEATASONE",
                    "created_at": "Sun Jan 23 17:40:22 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme14/bg.gif",
                    "protected": false,
                    "screen_name": "cercleofficial",
                    "id_str": "241994051",
                    "profile_link_color": "4A913C",
                    "translator_type": "none",
                    "id": 241994051,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1212773479545786368/nCHAhx9a_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.cerclebrugge.be",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/241994051/1578839889",
                    "statuses_count": 9115,
                    "follow_request_sent": null,
                    "followers_count": 16082,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "Cercle Brugge",
                    "location": "Brugge, Belgium",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 204,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/880722596056190976/gvKsKRrk_normal.jpg",
                "listed_count": 925,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme10/bg.gif",
                "default_profile_image": false,
                "favourites_count": 785,
                "description": "The official Twitter account of Royal Sporting Club Anderlecht | rsca.be | https://t.co/1AZrOxz06m | https://t.co/bltaii00OS | https://t.co/sSQutQvv83",
                "created_at": "Thu Sep 03 15:59:25 +0000 2009",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme10/bg.gif",
                "protected": false,
                "screen_name": "rscanderlecht",
                "id_str": "71287752",
                "profile_link_color": "61279E",
                "translator_type": "none",
                "id": 71287752,
                "geo_enabled": true,
                "profile_background_color": "9266CC",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "1F0C2E",
                "verified": true,
                "profile_image_url": "http://pbs.twimg.com/profile_images/880722596056190976/gvKsKRrk_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/71287752/1567426601",
                "statuses_count": 33856,
                "follow_request_sent": null,
                "followers_count": 172454,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "RSC Anderlecht",
                "location": "Anderlecht, Belgique",
                "profile_sidebar_fill_color": "9A7CED",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102588214550528",
            "reply_count": 0,
            "quoted_status_id": 1221057239651430401,
            "quoted_status_id_str": "1221057239651430401",
            "id": 1221102588214550528,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:38 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "This goes far beyond colours, clubpassion or football. Yes, we'll support this @cercleofficial 💚💜",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968518676",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Cercle Brugge",
                        "indices": [
                            79,
                            94
                        ],
                        "id": 241994051,
                        "screen_name": "cercleofficial",
                        "id_str": "241994051"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/zy7Oxdj1GQ",
                "expanded": "https://twitter.com/cercleofficial/status/1221057239651430401",
                "display": "twitter.com/cercleofficial…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/qViKhG6ooJ",
                            "indices": [
                                46,
                                69
                            ],
                            "sizes": {
                                "small": {
                                    "h": 365,
                                    "resize": "fit",
                                    "w": 648
                                },
                                "medium": {
                                    "h": 365,
                                    "resize": "fit",
                                    "w": 648
                                },
                                "large": {
                                    "h": 365,
                                    "resize": "fit",
                                    "w": 648
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1220620182999183360",
                            "expanded_url": "https://twitter.com/TheSecondTier/status/1220620194286129152/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPCDlt1WsAAQT4K.jpg",
                            "id": 1220620182999183360,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPCDlt1WsAAQT4K.jpg",
                            "url": "https://t.co/qViKhG6ooJ"
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 08:11:47 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 3,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220620194286129152",
                "in_reply_to_user_id": null,
                "favorite_count": 115,
                "id": 1220620194286129152,
                "text": "What's the worst thing about modern football? https://t.co/qViKhG6ooJ",
                "place": null,
                "lang": "en",
                "quote_count": 232,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 274,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/qViKhG6ooJ",
                            "indices": [
                                46,
                                69
                            ],
                            "sizes": {
                                "small": {
                                    "h": 365,
                                    "resize": "fit",
                                    "w": 648
                                },
                                "medium": {
                                    "h": 365,
                                    "resize": "fit",
                                    "w": 648
                                },
                                "large": {
                                    "h": 365,
                                    "resize": "fit",
                                    "w": 648
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1220620182999183360",
                            "expanded_url": "https://twitter.com/TheSecondTier/status/1220620194286129152/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPCDlt1WsAAQT4K.jpg",
                            "id": 1220620182999183360,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPCDlt1WsAAQT4K.jpg",
                            "url": "https://t.co/qViKhG6ooJ"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    45
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 214,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1148171098208575488/e__yHAUQ_normal.png",
                    "listed_count": 18,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 760,
                    "description": "A podcast dedicated to Championship football. New episode every Sunday. Apple Podcasts, Spotify and Acast. Email: secondtierpod@gmail.com",
                    "created_at": "Sun Jun 02 16:43:28 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "TheSecondTier",
                    "id_str": "1135225428141137920",
                    "profile_link_color": "1B95E0",
                    "translator_type": "none",
                    "id": 1135225428141137920,
                    "geo_enabled": false,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1148171098208575488/e__yHAUQ_normal.png",
                    "time_zone": null,
                    "url": "https://apple.co/2YpdmZI",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1135225428141137920/1562580285",
                    "statuses_count": 2849,
                    "follow_request_sent": null,
                    "followers_count": 10303,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "Second Tier Podcast",
                    "location": null,
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 633,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1219769072453287936/PxOVDcfw_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 5451,
                "description": "🏴󠁧󠁢󠁥󠁮󠁧󠁿🇬🇧🇺🇦 20",
                "created_at": "Wed Jun 26 23:58:18 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "D4NNY1894",
                "id_str": "1144032166860529664",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1144032166860529664,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1219769072453287936/PxOVDcfw_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1144032166860529664/1576284527",
                "statuses_count": 1311,
                "follow_request_sent": null,
                "followers_count": 283,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Danny",
                "location": "Stockport, England",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102820453240832",
            "reply_count": 0,
            "quoted_status_id": 1220620194286129152,
            "quoted_status_id_str": "1220620194286129152",
            "id": 1221102820453240832,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:34 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "All of it",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968574046",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/0yO1iUjQpX",
                "expanded": "https://twitter.com/thesecondtier/status/1220620194286129152",
                "display": "twitter.com/thesecondtier/…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 198,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1164118343034580993/-YvqXQJf_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 1992,
                "description": "CHAMPIONS OF EUROPE #YNWA",
                "created_at": "Fri Aug 18 22:05:10 +0000 2017",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "victorlucas10c",
                "id_str": "898667109311492096",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 898667109311492096,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1164118343034580993/-YvqXQJf_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/898667109311492096/1559942960",
                "statuses_count": 1378,
                "follow_request_sent": null,
                "followers_count": 169,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Lucas Victor",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102065067470849",
            "reply_count": 0,
            "display_text_range": [
                42,
                140
            ],
            "id": 1221102065067470849,
            "in_reply_to_user_id": 1213547518761394176,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:33 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    42,
                    208
                ],
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "Nico",
                            "indices": [
                                0,
                                9
                            ],
                            "id": 1213547518761394176,
                            "screen_name": "fcbnico_",
                            "id_str": "1213547518761394176"
                        },
                        {
                            "name": "Planet origi",
                            "indices": [
                                10,
                                21
                            ],
                            "id": 1159148410043326464,
                            "screen_name": "Gerald_yea",
                            "id_str": "1159148410043326464"
                        },
                        {
                            "name": "musanicacha",
                            "indices": [
                                22,
                                35
                            ],
                            "id": 844827477516021760,
                            "screen_name": "MusabiChacha",
                            "id_str": "844827477516021760"
                        },
                        {
                            "name": "Goal",
                            "indices": [
                                36,
                                41
                            ],
                            "id": 26809005,
                            "screen_name": "goal",
                            "id_str": "26809005"
                        }
                    ],
                    "symbols": []
                },
                "full_text": "@fcbnico_ @Gerald_yea @MusabiChacha @goal Lol.. Alisson missed the first 3months of football with injury and Liverpool couldn’t keep clean sheets. He came back and they’ve kept 9 clean sheet in 11 games since"
            },
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "@fcbnico_ @Gerald_yea @MusabiChacha @goal Lol.. Alisson missed the first 3months of football with injury and Liverp… https://t.co/h2t1vSCwmw",
            "in_reply_to_user_id_str": "1213547518761394176",
            "in_reply_to_status_id": 1221101481111232514,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "fcbnico_",
            "place": null,
            "timestamp_ms": "1579968393948",
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102065067470849",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/h2t1vSCwmw"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Nico",
                        "indices": [
                            0,
                            9
                        ],
                        "id": 1213547518761394176,
                        "screen_name": "fcbnico_",
                        "id_str": "1213547518761394176"
                    },
                    {
                        "name": "Planet origi",
                        "indices": [
                            10,
                            21
                        ],
                        "id": 1159148410043326464,
                        "screen_name": "Gerald_yea",
                        "id_str": "1159148410043326464"
                    },
                    {
                        "name": "musanicacha",
                        "indices": [
                            22,
                            35
                        ],
                        "id": 844827477516021760,
                        "screen_name": "MusabiChacha",
                        "id_str": "844827477516021760"
                    },
                    {
                        "name": "Goal",
                        "indices": [
                            36,
                            41
                        ],
                        "id": 26809005,
                        "screen_name": "goal",
                        "id_str": "26809005"
                    }
                ],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": "1221101481111232514",
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 537,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000844041672/6389bbf49fc91db22dd3811fed2ba09c_normal.jpeg",
                "listed_count": 11,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 4062,
                "description": "https://www.instagram.com/n3lsv/",
                "created_at": "Fri Apr 15 04:07:50 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "n3lsv",
                "id_str": "282400167",
                "profile_link_color": "0084B4",
                "translator_type": "none",
                "id": 282400167,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/378800000844041672/6389bbf49fc91db22dd3811fed2ba09c_normal.jpeg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/282400167/1350317379",
                "statuses_count": 8378,
                "follow_request_sent": null,
                "followers_count": 186,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "ネリー",
                "location": "London",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102567414992896",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        280
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Pep Guardiola wants League Cup scrapped. \n\nPep Guardiola wants FA Cup replays scrapped. \n\nPep Guardiola wants... \n\nDoes Pep Guardiola realise there's actually hundreds of football clubs not rolling in blood money who live for and are often funded by such occasions.  Smug elitism."
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 18:41:11 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 1654,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220778591895609345",
                "in_reply_to_user_id": null,
                "favorite_count": 12455,
                "id": 1220778591895609345,
                "text": "Pep Guardiola wants League Cup scrapped. \n\nPep Guardiola wants FA Cup replays scrapped. \n\nPep Guardiola wants...… https://t.co/aqp8Zz5RbK",
                "place": null,
                "lang": "en",
                "quote_count": 177,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 372,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220778591895609345",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                114,
                                137
                            ],
                            "url": "https://t.co/aqp8Zz5RbK"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1766,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/949697816087224320/3aRObHuB_normal.jpg",
                    "listed_count": 287,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme8/bg.gif",
                    "default_profile_image": false,
                    "favourites_count": 45164,
                    "description": "So you run and you run to catch up with the sun but it's sinking, racing around to come up behind you again.\n\nSports writer of year once upon a time.",
                    "created_at": "Tue Jan 25 14:46:59 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme8/bg.gif",
                    "protected": false,
                    "screen_name": "EwanMacKenna",
                    "id_str": "242759237",
                    "profile_link_color": "ABB8C2",
                    "translator_type": "none",
                    "id": 242759237,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/949697816087224320/3aRObHuB_normal.jpg",
                    "time_zone": null,
                    "url": "http://ewanmackenna.wordpress.com/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/242759237/1549712606",
                    "statuses_count": 91660,
                    "follow_request_sent": null,
                    "followers_count": 32727,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "Ewan MacKenna",
                    "location": "Portugal. Brazil. Ireland. ",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "id": 1221102567414992896,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:33 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @EwanMacKenna: Pep Guardiola wants League Cup scrapped. \n\nPep Guardiola wants FA Cup replays scrapped. \n\nPep Guardiola wants... \n\nDoes P…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968513717",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Ewan MacKenna",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 242759237,
                        "screen_name": "EwanMacKenna",
                        "id_str": "242759237"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1022,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1206356255704408065/msTJe3pK_normal.jpg",
                "listed_count": 2797,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 14536,
                "description": "Football writer and analyst for @YahooSports but expect more than that from me. #ReceptionPerception creator. I did it my way.",
                "created_at": "Mon Feb 13 03:29:10 +0000 2012",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "MattHarmon_BYB",
                "id_str": "490970028",
                "profile_link_color": "1B95E0",
                "translator_type": "none",
                "id": 490970028,
                "geo_enabled": true,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": true,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1206356255704408065/msTJe3pK_normal.jpg",
                "time_zone": null,
                "url": "http://www.instagram.com/mattharmon_byb/",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/490970028/1512142622",
                "statuses_count": 136398,
                "follow_request_sent": null,
                "followers_count": 95761,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "Matt Harmon",
                "location": "Los Angeles, CA",
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102633521303553",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        196
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/wcTsxLFatj",
                                "indices": [
                                    197,
                                    220
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 1152,
                                        "resize": "fit",
                                        "w": 2048
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220753334631419904",
                                "expanded_url": "https://twitter.com/YahooFantasy/status/1221100413669105664/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPD8sKUUUAAngja.jpg",
                                "id": 1220753334631419904,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPD8sKUUUAAngja.jpg",
                                "url": "https://t.co/wcTsxLFatj"
                            }
                        ]
                    },
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "https://apple.co/2vkbYhn",
                                "display_url": "apple.co/2vkbYhn",
                                "indices": [
                                    140,
                                    163
                                ],
                                "url": "https://t.co/cU675ktcKY"
                            },
                            {
                                "expanded_url": "https://spoti.fi/3aEElXz",
                                "display_url": "spoti.fi/3aEElXz",
                                "indices": [
                                    173,
                                    196
                                ],
                                "url": "https://t.co/z826hCAeVC"
                            }
                        ],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/wcTsxLFatj",
                                "indices": [
                                    197,
                                    220
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 1152,
                                        "resize": "fit",
                                        "w": 2048
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220753334631419904",
                                "expanded_url": "https://twitter.com/YahooFantasy/status/1221100413669105664/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPD8sKUUUAAngja.jpg",
                                "id": 1220753334631419904,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPD8sKUUUAAngja.jpg",
                                "url": "https://t.co/wcTsxLFatj"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [
                            {
                                "name": "Liz Loza",
                                "indices": [
                                    86,
                                    97
                                ],
                                "id": 80101877,
                                "screen_name": "LizLoza_FF",
                                "id_str": "80101877"
                            },
                            {
                                "name": "Matt Harmon",
                                "indices": [
                                    102,
                                    117
                                ],
                                "id": 490970028,
                                "screen_name": "MattHarmon_BYB",
                                "id_str": "490970028"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "ICYMI: Playoff talk galore and 2020 ranks in the latest fantasy football podcast with @LizLoza_FF and @MattHarmon_BYB !\n\nLISTEN ON:\n\nAPPLE: https://t.co/cU675ktcKY\nSPOTIFY: https://t.co/z826hCAeVC https://t.co/wcTsxLFatj"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:00:00 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://studio.twitter.com\" rel=\"nofollow\">Twitter Media Studio</a>",
                "retweet_count": 3,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221100413669105664",
                "in_reply_to_user_id": null,
                "favorite_count": 3,
                "id": 1221100413669105664,
                "text": "ICYMI: Playoff talk galore and 2020 ranks in the latest fantasy football podcast with @LizLoza_FF and… https://t.co/fehgsVLl6n",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221100413669105664",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                103,
                                126
                            ],
                            "url": "https://t.co/fehgsVLl6n"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "Liz Loza",
                            "indices": [
                                86,
                                97
                            ],
                            "id": 80101877,
                            "screen_name": "LizLoza_FF",
                            "id_str": "80101877"
                        }
                    ],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 523,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1176101741508481025/WBRj09Th_normal.png",
                    "listed_count": 4358,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 5542,
                    "description": "Rule your league and have fun doing it.\nOfficial Twitter page for Yahoo Fantasy.\nHit up @YahooFantasyCC for account or league issues.",
                    "created_at": "Thu Jul 23 20:27:51 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "YahooFantasy",
                    "id_str": "59578815",
                    "profile_link_color": "6D00F6",
                    "translator_type": "none",
                    "id": 59578815,
                    "geo_enabled": true,
                    "profile_background_color": "003015",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "000000",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1176101741508481025/WBRj09Th_normal.png",
                    "time_zone": null,
                    "url": "http://sports.yahoo.com/fantasy",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/59578815/1569239481",
                    "statuses_count": 57844,
                    "follow_request_sent": null,
                    "followers_count": 357445,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Yahoo Fantasy Sports",
                    "location": null,
                    "profile_sidebar_fill_color": "E6AD1E",
                    "notifications": null
                }
            },
            "id": 1221102633521303553,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:49 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @YahooFantasy: ICYMI: Playoff talk galore and 2020 ranks in the latest fantasy football podcast with @LizLoza_FF and @MattHarmon_BYB !…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968529478",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Yahoo Fantasy Sports",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 59578815,
                        "screen_name": "YahooFantasy",
                        "id_str": "59578815"
                    },
                    {
                        "name": "Liz Loza",
                        "indices": [
                            104,
                            115
                        ],
                        "id": 80101877,
                        "screen_name": "LizLoza_FF",
                        "id_str": "80101877"
                    },
                    {
                        "name": "Matt Harmon",
                        "indices": [
                            120,
                            135
                        ],
                        "id": 490970028,
                        "screen_name": "MattHarmon_BYB",
                        "id_str": "490970028"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        279
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/Z21oHmiskb",
                                "indices": [
                                    280,
                                    303
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 347,
                                        "resize": "fit",
                                        "w": 600
                                    },
                                    "medium": {
                                        "h": 347,
                                        "resize": "fit",
                                        "w": 600
                                    },
                                    "large": {
                                        "h": 347,
                                        "resize": "fit",
                                        "w": 600
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220787930752528385",
                                "expanded_url": "https://twitter.com/iMiaSanMia/status/1220787934506508288/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPEcJ66WsAENmMi.jpg",
                                "id": 1220787930752528385,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPEcJ66WsAENmMi.jpg",
                                "url": "https://t.co/Z21oHmiskb"
                            }
                        ]
                    },
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/Z21oHmiskb",
                                "indices": [
                                    280,
                                    303
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 347,
                                        "resize": "fit",
                                        "w": 600
                                    },
                                    "medium": {
                                        "h": 347,
                                        "resize": "fit",
                                        "w": 600
                                    },
                                    "large": {
                                        "h": 347,
                                        "resize": "fit",
                                        "w": 600
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220787930752528385",
                                "expanded_url": "https://twitter.com/iMiaSanMia/status/1220787934506508288/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPEcJ66WsAENmMi.jpg",
                                "id": 1220787930752528385,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPEcJ66WsAENmMi.jpg",
                                "url": "https://t.co/Z21oHmiskb"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "KHR on Neuer: \"I have seen everyone: Sepp Maier, Oliver Kahn - and now Manu. I have the greatest respect for Sepp and Oli, they were absolutely world-class. But what Manuel did was different: he took the goalkeeper game to a new level. Manu is the best GK the world has ever had\" https://t.co/Z21oHmiskb"
                },
                "in_reply_to_status_id_str": "1220786737296834562",
                "in_reply_to_status_id": 1220786737296834562,
                "created_at": "Fri Jan 24 19:18:19 +0000 2020",
                "in_reply_to_user_id_str": "618387275",
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "retweet_count": 72,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": "iMiaSanMia",
                "is_quote_status": false,
                "id_str": "1220787934506508288",
                "in_reply_to_user_id": 618387275,
                "favorite_count": 326,
                "id": 1220787934506508288,
                "text": "KHR on Neuer: \"I have seen everyone: Sepp Maier, Oliver Kahn - and now Manu. I have the greatest respect for Sepp a… https://t.co/9F0EBdaSmR",
                "place": null,
                "lang": "en",
                "quote_count": 20,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 13,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220787934506508288",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/9F0EBdaSmR"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 524,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1079495209363361792/Zs5jHFj9_normal.jpg",
                    "listed_count": 1120,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 4255,
                    "description": "FC Bayern | Die Mannschaft | Tweets in English.\n\nBack-up account: @eMiaSanMia \nVideo account: @iMiaSanMia_Vid\nGerman account: @iMiaSanMia_GER",
                    "created_at": "Mon Jun 25 19:57:21 +0000 2012",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "iMiaSanMia",
                    "id_str": "618387275",
                    "profile_link_color": "0084B4",
                    "translator_type": "none",
                    "id": 618387275,
                    "geo_enabled": false,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1079495209363361792/Zs5jHFj9_normal.jpg",
                    "time_zone": null,
                    "url": "https://Instagram.com/imiasanmia_/",
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/618387275/1485203370",
                    "statuses_count": 64409,
                    "follow_request_sent": null,
                    "followers_count": 104857,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Bayern & Germany",
                    "location": "Munich, Bavaria",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 472,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1150124631015198721/vAh4TTo__normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 3236,
                "description": null,
                "created_at": "Sat Sep 26 19:00:13 +0000 2009",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "MailmanPan",
                "id_str": "77548037",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 77548037,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1150124631015198721/vAh4TTo__normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/77548037/1563044896",
                "statuses_count": 1009,
                "follow_request_sent": null,
                "followers_count": 73,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "A Knowlton",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102251747500032",
            "reply_count": 0,
            "quoted_status_id": 1220787934506508288,
            "retweeted_status": {
                "quoted_status": {
                    "extended_tweet": {
                        "display_text_range": [
                            0,
                            279
                        ],
                        "extended_entities": {
                            "media": [
                                {
                                    "display_url": "pic.twitter.com/Z21oHmiskb",
                                    "indices": [
                                        280,
                                        303
                                    ],
                                    "sizes": {
                                        "small": {
                                            "h": 347,
                                            "resize": "fit",
                                            "w": 600
                                        },
                                        "medium": {
                                            "h": 347,
                                            "resize": "fit",
                                            "w": 600
                                        },
                                        "large": {
                                            "h": 347,
                                            "resize": "fit",
                                            "w": 600
                                        },
                                        "thumb": {
                                            "h": 150,
                                            "resize": "crop",
                                            "w": 150
                                        }
                                    },
                                    "id_str": "1220787930752528385",
                                    "expanded_url": "https://twitter.com/iMiaSanMia/status/1220787934506508288/photo/1",
                                    "media_url_https": "https://pbs.twimg.com/media/EPEcJ66WsAENmMi.jpg",
                                    "id": 1220787930752528385,
                                    "type": "photo",
                                    "media_url": "http://pbs.twimg.com/media/EPEcJ66WsAENmMi.jpg",
                                    "url": "https://t.co/Z21oHmiskb"
                                }
                            ]
                        },
                        "entities": {
                            "urls": [],
                            "media": [
                                {
                                    "display_url": "pic.twitter.com/Z21oHmiskb",
                                    "indices": [
                                        280,
                                        303
                                    ],
                                    "sizes": {
                                        "small": {
                                            "h": 347,
                                            "resize": "fit",
                                            "w": 600
                                        },
                                        "medium": {
                                            "h": 347,
                                            "resize": "fit",
                                            "w": 600
                                        },
                                        "large": {
                                            "h": 347,
                                            "resize": "fit",
                                            "w": 600
                                        },
                                        "thumb": {
                                            "h": 150,
                                            "resize": "crop",
                                            "w": 150
                                        }
                                    },
                                    "id_str": "1220787930752528385",
                                    "expanded_url": "https://twitter.com/iMiaSanMia/status/1220787934506508288/photo/1",
                                    "media_url_https": "https://pbs.twimg.com/media/EPEcJ66WsAENmMi.jpg",
                                    "id": 1220787930752528385,
                                    "type": "photo",
                                    "media_url": "http://pbs.twimg.com/media/EPEcJ66WsAENmMi.jpg",
                                    "url": "https://t.co/Z21oHmiskb"
                                }
                            ],
                            "hashtags": [],
                            "user_mentions": [],
                            "symbols": []
                        },
                        "full_text": "KHR on Neuer: \"I have seen everyone: Sepp Maier, Oliver Kahn - and now Manu. I have the greatest respect for Sepp and Oli, they were absolutely world-class. But what Manuel did was different: he took the goalkeeper game to a new level. Manu is the best GK the world has ever had\" https://t.co/Z21oHmiskb"
                    },
                    "in_reply_to_status_id_str": "1220786737296834562",
                    "in_reply_to_status_id": 1220786737296834562,
                    "created_at": "Fri Jan 24 19:18:19 +0000 2020",
                    "in_reply_to_user_id_str": "618387275",
                    "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                    "retweet_count": 72,
                    "retweeted": false,
                    "geo": null,
                    "filter_level": "low",
                    "in_reply_to_screen_name": "iMiaSanMia",
                    "is_quote_status": false,
                    "id_str": "1220787934506508288",
                    "in_reply_to_user_id": 618387275,
                    "favorite_count": 326,
                    "id": 1220787934506508288,
                    "text": "KHR on Neuer: \"I have seen everyone: Sepp Maier, Oliver Kahn - and now Manu. I have the greatest respect for Sepp a… https://t.co/9F0EBdaSmR",
                    "place": null,
                    "lang": "en",
                    "quote_count": 20,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": true,
                    "reply_count": 13,
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "https://twitter.com/i/web/status/1220787934506508288",
                                "display_url": "twitter.com/i/web/status/1…",
                                "indices": [
                                    117,
                                    140
                                ],
                                "url": "https://t.co/9F0EBdaSmR"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "display_text_range": [
                        0,
                        140
                    ],
                    "contributors": null,
                    "user": {
                        "utc_offset": null,
                        "friends_count": 524,
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1079495209363361792/Zs5jHFj9_normal.jpg",
                        "listed_count": 1120,
                        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                        "default_profile_image": false,
                        "favourites_count": 4255,
                        "description": "FC Bayern | Die Mannschaft | Tweets in English.\n\nBack-up account: @eMiaSanMia \nVideo account: @iMiaSanMia_Vid\nGerman account: @iMiaSanMia_GER",
                        "created_at": "Mon Jun 25 19:57:21 +0000 2012",
                        "is_translator": false,
                        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                        "protected": false,
                        "screen_name": "iMiaSanMia",
                        "id_str": "618387275",
                        "profile_link_color": "0084B4",
                        "translator_type": "none",
                        "id": 618387275,
                        "geo_enabled": false,
                        "profile_background_color": "C0DEED",
                        "lang": null,
                        "profile_sidebar_border_color": "FFFFFF",
                        "profile_text_color": "333333",
                        "verified": false,
                        "profile_image_url": "http://pbs.twimg.com/profile_images/1079495209363361792/Zs5jHFj9_normal.jpg",
                        "time_zone": null,
                        "url": "https://Instagram.com/imiasanmia_/",
                        "contributors_enabled": false,
                        "profile_background_tile": true,
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/618387275/1485203370",
                        "statuses_count": 64409,
                        "follow_request_sent": null,
                        "followers_count": 104857,
                        "profile_use_background_image": true,
                        "default_profile": false,
                        "following": null,
                        "name": "Bayern & Germany",
                        "location": "Munich, Bavaria",
                        "profile_sidebar_fill_color": "DDEEF6",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:56:56 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "quoted_status_id": 1220787934506508288,
                "retweet_count": 6,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1221099645121847298",
                "in_reply_to_user_id": null,
                "favorite_count": 27,
                "id": 1221099645121847298,
                "text": "Truth. Neuer changed the game. He's a historic football figure and a modern legend of the game.",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/hrITFCIu1U",
                    "expanded": "https://twitter.com/iMiaSanMia/status/1220787934506508288",
                    "display": "twitter.com/iMiaSanMia/sta…"
                },
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 1,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1220787934506508288",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 2148,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1082820054306181120/uWdL4D2z_normal.jpg",
                    "listed_count": 747,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme9/bg.gif",
                    "default_profile_image": false,
                    "favourites_count": 36634,
                    "description": "@DAZN_USA | Media. Digital. Social. Tech. Creative. Strategy. Former: @FCBayernUS @nytimes @optasuit @goal @BleacherReport @Bundesliga4u Views my own",
                    "created_at": "Sat Nov 27 22:58:24 +0000 2010",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme9/bg.gif",
                    "protected": false,
                    "screen_name": "Cnyari",
                    "id_str": "220484183",
                    "profile_link_color": "1178BD",
                    "translator_type": "none",
                    "id": 220484183,
                    "geo_enabled": true,
                    "profile_background_color": "1A1B1F",
                    "lang": null,
                    "profile_sidebar_border_color": "4A4C4F",
                    "profile_text_color": "666666",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1082820054306181120/uWdL4D2z_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.cristiannyari.com/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/220484183/1449675607",
                    "statuses_count": 116347,
                    "follow_request_sent": null,
                    "followers_count": 18101,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Cristian Nyari",
                    "location": "New York City",
                    "profile_sidebar_fill_color": "141311",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1220787934506508288",
            "id": 1221102251747500032,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:18 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @Cnyari: Truth. Neuer changed the game. He's a historic football figure and a modern legend of the game.",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968438456",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Cristian Nyari",
                        "indices": [
                            3,
                            10
                        ],
                        "id": 220484183,
                        "screen_name": "Cnyari",
                        "id_str": "220484183"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/hrITFCIu1U",
                "expanded": "https://twitter.com/iMiaSanMia/status/1220787934506508288",
                "display": "twitter.com/iMiaSanMia/sta…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 696,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/901566207450591234/6WtorrjO_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 4892,
                "description": null,
                "created_at": "Fri Sep 19 09:46:54 +0000 2014",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "jimohisah6",
                "id_str": "2775361612",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 2775361612,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/901566207450591234/6WtorrjO_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 20958,
                "follow_request_sent": null,
                "followers_count": 96,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "jimoh isah diyo",
                "location": "Abuja",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101859634667520",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:01:08 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://ifttt.com\" rel=\"nofollow\">IFTTT</a>",
                "retweet_count": 6,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221085602394902529",
                "in_reply_to_user_id": null,
                "favorite_count": 22,
                "id": 1221085602394902529,
                "text": "Chelsea boss Lampard eyes transfer swoop for Palace keeper Guiata to challenge Kepa for first team place in summer https://t.co/5mJDE0YIha",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.thesun.co.uk/sport/football/10818867/chelsea-lampard-transfer-palace-guiata-kepa/",
                            "display_url": "thesun.co.uk/sport/football…",
                            "indices": [
                                115,
                                138
                            ],
                            "url": "https://t.co/5mJDE0YIha"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 5,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/766320068099772416/hlPZV2jO_normal.jpg",
                    "listed_count": 388,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 13,
                    "description": "Follow all the latest news on Chelsea with The Sun @TheSunFootball @SunSport",
                    "created_at": "Fri Jul 31 13:55:46 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "SunChelsea",
                    "id_str": "61775718",
                    "profile_link_color": "00745F",
                    "translator_type": "none",
                    "id": 61775718,
                    "geo_enabled": false,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "0A000A",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/766320068099772416/hlPZV2jO_normal.jpg",
                    "time_zone": null,
                    "url": "https://www.thesun.co.uk/sport/football/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/61775718/1375294484",
                    "statuses_count": 13345,
                    "follow_request_sent": null,
                    "followers_count": 47763,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "The Sun - Chelsea",
                    "location": null,
                    "profile_sidebar_fill_color": "CFCFCF",
                    "notifications": null
                }
            },
            "id": 1221101859634667520,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:44 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @SunChelsea: Chelsea boss Lampard eyes transfer swoop for Palace keeper Guiata to challenge Kepa for first team place in summer https://…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968344969",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "The Sun - Chelsea",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 61775718,
                        "screen_name": "SunChelsea",
                        "id_str": "61775718"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/EbXuum8Xu7",
                            "source_user_id": 117442705,
                            "type": "video",
                            "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "source_status_id": 1017455687981502464,
                            "url": "https://t.co/EbXuum8Xu7",
                            "indices": [
                                71,
                                94
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1017454803503509504",
                            "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                            "source_status_id_str": "1017455687981502464",
                            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "id": 1017454803503509504,
                            "source_user_id_str": "117442705",
                            "additional_media_info": {
                                "description": null,
                                "title": null,
                                "embeddable": true,
                                "monetizable": false
                            },
                            "video_info": {
                                "aspect_ratio": [
                                    16,
                                    9
                                ],
                                "duration_millis": 163160,
                                "variants": [
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 2176000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/1280x720/nxlpH9SZDiXJ5ff7.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 288000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/320x180/DqOXLHd9PbhAJdY6.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 832000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/640x360/cIXlGiMN24w9P4FJ.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/pl/6yRvxYcbNePDJbp6.m3u8?tag=3"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 16:02:05 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 2309,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220738552834809861",
                "in_reply_to_user_id": null,
                "favorite_count": 13490,
                "id": 1220738552834809861,
                "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                "place": null,
                "lang": "en",
                "quote_count": 1428,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 546,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/EbXuum8Xu7",
                            "source_user_id": 117442705,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "source_status_id": 1017455687981502464,
                            "url": "https://t.co/EbXuum8Xu7",
                            "indices": [
                                71,
                                94
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1017454803503509504",
                            "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                            "source_status_id_str": "1017455687981502464",
                            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "id": 1017454803503509504,
                            "source_user_id_str": "117442705",
                            "additional_media_info": {
                                "description": null,
                                "title": null,
                                "embeddable": true,
                                "monetizable": false
                            }
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 58,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                    "listed_count": 29,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 546,
                    "description": "The Home of Football Limbs | Enquires 📧 footylimbs@gmail.com | 18+",
                    "created_at": "Fri Mar 08 15:58:59 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "FootyLimbs",
                    "id_str": "1104048876867276800",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1104048876867276800,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                    "time_zone": null,
                    "url": "http://bit.ly/500-RiskFree",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1104048876867276800/1576774795",
                    "statuses_count": 1398,
                    "follow_request_sent": null,
                    "followers_count": 63679,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Footy Limbs",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 535,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1164436640028405761/6H7woBBP_normal.jpg",
                "listed_count": 2,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 43148,
                "description": "pussy cat.",
                "created_at": "Tue Jun 05 11:26:39 +0000 2018",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "kofi_xx",
                "id_str": "1003961293915803650",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1003961293915803650,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1164436640028405761/6H7woBBP_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1003961293915803650/1565449759",
                "statuses_count": 12439,
                "follow_request_sent": null,
                "followers_count": 300,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "kamara",
                "location": "Accra",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101909836214273",
            "reply_count": 0,
            "quoted_status_id": 1220738552834809861,
            "retweeted_status": {
                "quoted_status": {
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EbXuum8Xu7",
                                "source_user_id": 117442705,
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "source_status_id": 1017455687981502464,
                                "url": "https://t.co/EbXuum8Xu7",
                                "indices": [
                                    71,
                                    94
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1017454803503509504",
                                "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                                "source_status_id_str": "1017455687981502464",
                                "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "id": 1017454803503509504,
                                "source_user_id_str": "117442705",
                                "additional_media_info": {
                                    "description": null,
                                    "title": null,
                                    "embeddable": true,
                                    "monetizable": false
                                },
                                "video_info": {
                                    "aspect_ratio": [
                                        16,
                                        9
                                    ],
                                    "duration_millis": 163160,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/1280x720/nxlpH9SZDiXJ5ff7.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 288000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/320x180/DqOXLHd9PbhAJdY6.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/640x360/cIXlGiMN24w9P4FJ.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/pl/6yRvxYcbNePDJbp6.m3u8?tag=3"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "in_reply_to_status_id_str": null,
                    "in_reply_to_status_id": null,
                    "created_at": "Fri Jan 24 16:02:05 +0000 2020",
                    "in_reply_to_user_id_str": null,
                    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                    "retweet_count": 2309,
                    "retweeted": false,
                    "geo": null,
                    "filter_level": "low",
                    "in_reply_to_screen_name": null,
                    "is_quote_status": false,
                    "id_str": "1220738552834809861",
                    "in_reply_to_user_id": null,
                    "favorite_count": 13490,
                    "id": 1220738552834809861,
                    "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                    "place": null,
                    "lang": "en",
                    "quote_count": 1428,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": false,
                    "reply_count": 546,
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EbXuum8Xu7",
                                "source_user_id": 117442705,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "source_status_id": 1017455687981502464,
                                "url": "https://t.co/EbXuum8Xu7",
                                "indices": [
                                    71,
                                    94
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1017454803503509504",
                                "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                                "source_status_id_str": "1017455687981502464",
                                "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "id": 1017454803503509504,
                                "source_user_id_str": "117442705",
                                "additional_media_info": {
                                    "description": null,
                                    "title": null,
                                    "embeddable": true,
                                    "monetizable": false
                                }
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "contributors": null,
                    "user": {
                        "utc_offset": null,
                        "friends_count": 58,
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                        "listed_count": 29,
                        "profile_background_image_url": null,
                        "default_profile_image": false,
                        "favourites_count": 546,
                        "description": "The Home of Football Limbs | Enquires 📧 footylimbs@gmail.com | 18+",
                        "created_at": "Fri Mar 08 15:58:59 +0000 2019",
                        "is_translator": false,
                        "profile_background_image_url_https": null,
                        "protected": false,
                        "screen_name": "FootyLimbs",
                        "id_str": "1104048876867276800",
                        "profile_link_color": "1DA1F2",
                        "translator_type": "none",
                        "id": 1104048876867276800,
                        "geo_enabled": false,
                        "profile_background_color": "F5F8FA",
                        "lang": null,
                        "profile_sidebar_border_color": "C0DEED",
                        "profile_text_color": "333333",
                        "verified": false,
                        "profile_image_url": "http://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                        "time_zone": null,
                        "url": "http://bit.ly/500-RiskFree",
                        "contributors_enabled": false,
                        "profile_background_tile": false,
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1104048876867276800/1576774795",
                        "statuses_count": 1398,
                        "follow_request_sent": null,
                        "followers_count": 63679,
                        "profile_use_background_image": true,
                        "default_profile": true,
                        "following": null,
                        "name": "Footy Limbs",
                        "location": null,
                        "profile_sidebar_fill_color": "DDEEF6",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 17:34:28 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "quoted_status_id": 1220738552834809861,
                "retweet_count": 31,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1220761801639546881",
                "in_reply_to_user_id": null,
                "favorite_count": 230,
                "id": 1220761801639546881,
                "text": "I'm on the floor 🤣🤣 this is quite easily the most overrated campaign in football history",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/PBFx2bz72H",
                    "expanded": "https://twitter.com/FootyLimbs/status/1220738552834809861",
                    "display": "twitter.com/FootyLimbs/sta…"
                },
                "lang": "en",
                "quote_count": 1,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 5,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1220738552834809861",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 405,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1219307849949622273/dDeTCWxv_normal.jpg",
                    "listed_count": 39,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 2895,
                    "description": "you may know me as Mourinholic/CFCWriter",
                    "created_at": "Wed Jun 26 17:17:23 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "CarefreeRash",
                    "id_str": "1143931275104968704",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1143931275104968704,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1219307849949622273/dDeTCWxv_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1143931275104968704/1579523104",
                    "statuses_count": 5665,
                    "follow_request_sent": null,
                    "followers_count": 5768,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "CR",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1220738552834809861",
            "id": 1221101909836214273,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:56 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @CarefreeRash: I'm on the floor 🤣🤣 this is quite easily the most overrated campaign in football history",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968356938",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "CR",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 1143931275104968704,
                        "screen_name": "CarefreeRash",
                        "id_str": "1143931275104968704"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/PBFx2bz72H",
                "expanded": "https://twitter.com/FootyLimbs/status/1220738552834809861",
                "display": "twitter.com/FootyLimbs/sta…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        123
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/L1Bn3gPQrp",
                                "indices": [
                                    124,
                                    147
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 526,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 743,
                                        "resize": "fit",
                                        "w": 960
                                    },
                                    "large": {
                                        "h": 743,
                                        "resize": "fit",
                                        "w": 960
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220718092935991303",
                                "expanded_url": "https://twitter.com/DevilsOfUnited/status/1220718126368804864/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPDco0xXkAc2xHz.jpg",
                                "id": 1220718092935991303,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPDco0xXkAc2xHz.jpg",
                                "url": "https://t.co/L1Bn3gPQrp"
                            },
                            {
                                "display_url": "pic.twitter.com/L1Bn3gPQrp",
                                "indices": [
                                    124,
                                    147
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 434,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 612,
                                        "resize": "fit",
                                        "w": 960
                                    },
                                    "large": {
                                        "h": 612,
                                        "resize": "fit",
                                        "w": 960
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220718117694922752",
                                "expanded_url": "https://twitter.com/DevilsOfUnited/status/1220718126368804864/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPDcqRAW4AADPAk.jpg",
                                "id": 1220718117694922752,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPDcqRAW4AADPAk.jpg",
                                "url": "https://t.co/L1Bn3gPQrp"
                            }
                        ]
                    },
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/L1Bn3gPQrp",
                                "indices": [
                                    124,
                                    147
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 526,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 743,
                                        "resize": "fit",
                                        "w": 960
                                    },
                                    "large": {
                                        "h": 743,
                                        "resize": "fit",
                                        "w": 960
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220718092935991303",
                                "expanded_url": "https://twitter.com/DevilsOfUnited/status/1220718126368804864/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPDco0xXkAc2xHz.jpg",
                                "id": 1220718092935991303,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPDco0xXkAc2xHz.jpg",
                                "url": "https://t.co/L1Bn3gPQrp"
                            },
                            {
                                "display_url": "pic.twitter.com/L1Bn3gPQrp",
                                "indices": [
                                    124,
                                    147
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 434,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 612,
                                        "resize": "fit",
                                        "w": 960
                                    },
                                    "large": {
                                        "h": 612,
                                        "resize": "fit",
                                        "w": 960
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220718117694922752",
                                "expanded_url": "https://twitter.com/DevilsOfUnited/status/1220718126368804864/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPDcqRAW4AADPAk.jpg",
                                "id": 1220718117694922752,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPDcqRAW4AADPAk.jpg",
                                "url": "https://t.co/L1Bn3gPQrp"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Phil Jones arriving in a Lamborghini Urus. Jesse Lingard arriving in a Bentley truck.\n\nThe fucking state of football man. 😂 https://t.co/L1Bn3gPQrp"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 14:40:55 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 2811,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220718126368804864",
                "in_reply_to_user_id": null,
                "favorite_count": 15894,
                "id": 1220718126368804864,
                "text": "Phil Jones arriving in a Lamborghini Urus. Jesse Lingard arriving in a Bentley truck.\n\nThe fucking state of footbal… https://t.co/U5SlOxGAeA",
                "place": null,
                "lang": "en",
                "quote_count": 1098,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 803,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220718126368804864",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/U5SlOxGAeA"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 29487,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/437597255559041024/o7iGg_I6_normal.jpeg",
                    "listed_count": 384,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 3720,
                    "description": "Manchester United Football Club is our life. | Not Affiliated with Manchester United. For promotional tweets DM us.",
                    "created_at": "Mon Oct 28 16:51:24 +0000 2013",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "DevilsOfUnited",
                    "id_str": "2161245086",
                    "profile_link_color": "FC0303",
                    "translator_type": "none",
                    "id": 2161245086,
                    "geo_enabled": false,
                    "profile_background_color": "050505",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/437597255559041024/o7iGg_I6_normal.jpeg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/2161245086/1405427908",
                    "statuses_count": 8194,
                    "follow_request_sent": null,
                    "followers_count": 120397,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Devils of United 🔰",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 893,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/972646804931186688/wc_55mSd_normal.jpg",
                "listed_count": 25,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 122734,
                "description": "23|Soy El Fuego.",
                "created_at": "Mon May 14 16:57:07 +0000 2012",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "AMCXI_",
                "id_str": "580042361",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 580042361,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/972646804931186688/wc_55mSd_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/580042361/1517620659",
                "statuses_count": 163882,
                "follow_request_sent": null,
                "followers_count": 566,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Lucky Luciano",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102626328236034",
            "reply_count": 0,
            "quoted_status_id": 1220718126368804864,
            "retweeted_status": {
                "quoted_status": {
                    "extended_tweet": {
                        "display_text_range": [
                            0,
                            123
                        ],
                        "extended_entities": {
                            "media": [
                                {
                                    "display_url": "pic.twitter.com/L1Bn3gPQrp",
                                    "indices": [
                                        124,
                                        147
                                    ],
                                    "sizes": {
                                        "small": {
                                            "h": 526,
                                            "resize": "fit",
                                            "w": 680
                                        },
                                        "medium": {
                                            "h": 743,
                                            "resize": "fit",
                                            "w": 960
                                        },
                                        "large": {
                                            "h": 743,
                                            "resize": "fit",
                                            "w": 960
                                        },
                                        "thumb": {
                                            "h": 150,
                                            "resize": "crop",
                                            "w": 150
                                        }
                                    },
                                    "id_str": "1220718092935991303",
                                    "expanded_url": "https://twitter.com/DevilsOfUnited/status/1220718126368804864/photo/1",
                                    "media_url_https": "https://pbs.twimg.com/media/EPDco0xXkAc2xHz.jpg",
                                    "id": 1220718092935991303,
                                    "type": "photo",
                                    "media_url": "http://pbs.twimg.com/media/EPDco0xXkAc2xHz.jpg",
                                    "url": "https://t.co/L1Bn3gPQrp"
                                },
                                {
                                    "display_url": "pic.twitter.com/L1Bn3gPQrp",
                                    "indices": [
                                        124,
                                        147
                                    ],
                                    "sizes": {
                                        "small": {
                                            "h": 434,
                                            "resize": "fit",
                                            "w": 680
                                        },
                                        "medium": {
                                            "h": 612,
                                            "resize": "fit",
                                            "w": 960
                                        },
                                        "large": {
                                            "h": 612,
                                            "resize": "fit",
                                            "w": 960
                                        },
                                        "thumb": {
                                            "h": 150,
                                            "resize": "crop",
                                            "w": 150
                                        }
                                    },
                                    "id_str": "1220718117694922752",
                                    "expanded_url": "https://twitter.com/DevilsOfUnited/status/1220718126368804864/photo/1",
                                    "media_url_https": "https://pbs.twimg.com/media/EPDcqRAW4AADPAk.jpg",
                                    "id": 1220718117694922752,
                                    "type": "photo",
                                    "media_url": "http://pbs.twimg.com/media/EPDcqRAW4AADPAk.jpg",
                                    "url": "https://t.co/L1Bn3gPQrp"
                                }
                            ]
                        },
                        "entities": {
                            "urls": [],
                            "media": [
                                {
                                    "display_url": "pic.twitter.com/L1Bn3gPQrp",
                                    "indices": [
                                        124,
                                        147
                                    ],
                                    "sizes": {
                                        "small": {
                                            "h": 526,
                                            "resize": "fit",
                                            "w": 680
                                        },
                                        "medium": {
                                            "h": 743,
                                            "resize": "fit",
                                            "w": 960
                                        },
                                        "large": {
                                            "h": 743,
                                            "resize": "fit",
                                            "w": 960
                                        },
                                        "thumb": {
                                            "h": 150,
                                            "resize": "crop",
                                            "w": 150
                                        }
                                    },
                                    "id_str": "1220718092935991303",
                                    "expanded_url": "https://twitter.com/DevilsOfUnited/status/1220718126368804864/photo/1",
                                    "media_url_https": "https://pbs.twimg.com/media/EPDco0xXkAc2xHz.jpg",
                                    "id": 1220718092935991303,
                                    "type": "photo",
                                    "media_url": "http://pbs.twimg.com/media/EPDco0xXkAc2xHz.jpg",
                                    "url": "https://t.co/L1Bn3gPQrp"
                                },
                                {
                                    "display_url": "pic.twitter.com/L1Bn3gPQrp",
                                    "indices": [
                                        124,
                                        147
                                    ],
                                    "sizes": {
                                        "small": {
                                            "h": 434,
                                            "resize": "fit",
                                            "w": 680
                                        },
                                        "medium": {
                                            "h": 612,
                                            "resize": "fit",
                                            "w": 960
                                        },
                                        "large": {
                                            "h": 612,
                                            "resize": "fit",
                                            "w": 960
                                        },
                                        "thumb": {
                                            "h": 150,
                                            "resize": "crop",
                                            "w": 150
                                        }
                                    },
                                    "id_str": "1220718117694922752",
                                    "expanded_url": "https://twitter.com/DevilsOfUnited/status/1220718126368804864/photo/1",
                                    "media_url_https": "https://pbs.twimg.com/media/EPDcqRAW4AADPAk.jpg",
                                    "id": 1220718117694922752,
                                    "type": "photo",
                                    "media_url": "http://pbs.twimg.com/media/EPDcqRAW4AADPAk.jpg",
                                    "url": "https://t.co/L1Bn3gPQrp"
                                }
                            ],
                            "hashtags": [],
                            "user_mentions": [],
                            "symbols": []
                        },
                        "full_text": "Phil Jones arriving in a Lamborghini Urus. Jesse Lingard arriving in a Bentley truck.\n\nThe fucking state of football man. 😂 https://t.co/L1Bn3gPQrp"
                    },
                    "in_reply_to_status_id_str": null,
                    "in_reply_to_status_id": null,
                    "created_at": "Fri Jan 24 14:40:55 +0000 2020",
                    "in_reply_to_user_id_str": null,
                    "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                    "retweet_count": 2811,
                    "retweeted": false,
                    "geo": null,
                    "filter_level": "low",
                    "in_reply_to_screen_name": null,
                    "is_quote_status": false,
                    "id_str": "1220718126368804864",
                    "in_reply_to_user_id": null,
                    "favorite_count": 15894,
                    "id": 1220718126368804864,
                    "text": "Phil Jones arriving in a Lamborghini Urus. Jesse Lingard arriving in a Bentley truck.\n\nThe fucking state of footbal… https://t.co/U5SlOxGAeA",
                    "place": null,
                    "lang": "en",
                    "quote_count": 1098,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": true,
                    "reply_count": 803,
                    "entities": {
                        "urls": [
                            {
                                "expanded_url": "https://twitter.com/i/web/status/1220718126368804864",
                                "display_url": "twitter.com/i/web/status/1…",
                                "indices": [
                                    117,
                                    140
                                ],
                                "url": "https://t.co/U5SlOxGAeA"
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "display_text_range": [
                        0,
                        140
                    ],
                    "contributors": null,
                    "user": {
                        "utc_offset": null,
                        "friends_count": 29487,
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/437597255559041024/o7iGg_I6_normal.jpeg",
                        "listed_count": 384,
                        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                        "default_profile_image": false,
                        "favourites_count": 3720,
                        "description": "Manchester United Football Club is our life. | Not Affiliated with Manchester United. For promotional tweets DM us.",
                        "created_at": "Mon Oct 28 16:51:24 +0000 2013",
                        "is_translator": false,
                        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                        "protected": false,
                        "screen_name": "DevilsOfUnited",
                        "id_str": "2161245086",
                        "profile_link_color": "FC0303",
                        "translator_type": "none",
                        "id": 2161245086,
                        "geo_enabled": false,
                        "profile_background_color": "050505",
                        "lang": null,
                        "profile_sidebar_border_color": "000000",
                        "profile_text_color": "333333",
                        "verified": false,
                        "profile_image_url": "http://pbs.twimg.com/profile_images/437597255559041024/o7iGg_I6_normal.jpeg",
                        "time_zone": null,
                        "url": null,
                        "contributors_enabled": false,
                        "profile_background_tile": false,
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/2161245086/1405427908",
                        "statuses_count": 8194,
                        "follow_request_sent": null,
                        "followers_count": 120397,
                        "profile_use_background_image": true,
                        "default_profile": false,
                        "following": null,
                        "name": "Devils of United 🔰",
                        "location": null,
                        "profile_sidebar_fill_color": "DDEEF6",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 09:15:24 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "quoted_status_id": 1220718126368804864,
                "retweet_count": 33,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1220998595316416514",
                "in_reply_to_user_id": null,
                "favorite_count": 223,
                "id": 1220998595316416514,
                "text": "What do you expect man to do? “Ahhh I had a shit game today, might aswell trade in my Bentley for a Hyundai”",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/WKlsIpBZyY",
                    "expanded": "https://twitter.com/devilsofunited/status/1220718126368804864",
                    "display": "twitter.com/devilsofunited…"
                },
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1220718126368804864",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 377,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1193802809084456960/I6l4PT7a_normal.jpg",
                    "listed_count": 5,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 18064,
                    "description": "Any promo - DM🔌📲",
                    "created_at": "Sat May 18 17:31:26 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "lewasntme",
                    "id_str": "1129801683603738625",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1129801683603738625,
                    "geo_enabled": true,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1193802809084456960/I6l4PT7a_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1129801683603738625/1571246848",
                    "statuses_count": 7767,
                    "follow_request_sent": null,
                    "followers_count": 10060,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "You dont recognise me",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1220718126368804864",
            "id": 1221102626328236034,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:47 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @lewasntme: What do you expect man to do? “Ahhh I had a shit game today, might aswell trade in my Bentley for a Hyundai”",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968527763",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "You dont recognise me",
                        "indices": [
                            3,
                            13
                        ],
                        "id": 1129801683603738625,
                        "screen_name": "lewasntme",
                        "id_str": "1129801683603738625"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/WKlsIpBZyY",
                "expanded": "https://twitter.com/devilsofunited/status/1220718126368804864",
                "display": "twitter.com/devilsofunited…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1790,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/3092378254/559776f1516b2680bf0c5a0ca0a3f455_normal.jpeg",
                "listed_count": 21,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 984,
                "description": "Sales Director for British fashion brand Luke and American giant Alpha Industries. Level 4 referee and generally good guy ;-)",
                "created_at": "Mon Jan 03 22:19:28 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Cba_WBA1",
                "id_str": "233699995",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 233699995,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/3092378254/559776f1516b2680bf0c5a0ca0a3f455_normal.jpeg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 1788,
                "follow_request_sent": null,
                "followers_count": 815,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Carl Barratt",
                "location": "Manchester",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102082024968198",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        258
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [
                            {
                                "indices": [
                                    188,
                                    199
                                ],
                                "text": "Manchester"
                            },
                            {
                                "indices": [
                                    200,
                                    207
                                ],
                                "text": "ladies"
                            },
                            {
                                "indices": [
                                    208,
                                    214
                                ],
                                "text": "women"
                            },
                            {
                                "indices": [
                                    215,
                                    222
                                ],
                                "text": "player"
                            },
                            {
                                "indices": [
                                    223,
                                    235
                                ],
                                "text": "recruitment"
                            },
                            {
                                "indices": [
                                    236,
                                    248
                                ],
                                "text": "Wythenshawe"
                            },
                            {
                                "indices": [
                                    249,
                                    258
                                ],
                                "text": "football"
                            }
                        ],
                        "user_mentions": [
                            {
                                "name": "find me a player ",
                                "indices": [
                                    173,
                                    187
                                ],
                                "id": 1273652930,
                                "screen_name": "findmeaplayer",
                                "id_str": "1273652930"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "Our womens 1st team are looking for new players, long term injuries have forced our hand and anyone fancying a new challenge playing with a great set of ladies get in touch @findmeaplayer #Manchester #ladies #women #player #recruitment #Wythenshawe #football"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 13:12:58 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 5,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221058381433200640",
                "in_reply_to_user_id": null,
                "favorite_count": 3,
                "id": 1221058381433200640,
                "text": "Our womens 1st team are looking for new players, long term injuries have forced our hand and anyone fancying a new… https://t.co/nYbrG05JId",
                "place": null,
                "lang": "en",
                "quote_count": 1,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221058381433200640",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                116,
                                139
                            ],
                            "url": "https://t.co/nYbrG05JId"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 208,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/970754746297536512/ppZoultT_normal.jpg",
                    "listed_count": 4,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 36,
                    "description": "Official Twiiter account of Wythenshawe Amateurs Ladies FC, we play at The Hollyhedge Community Stadium, Altrincham Road, Sharston, M22 4US",
                    "created_at": "Mon Mar 05 20:12:47 +0000 2018",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "WAFC_Womens",
                    "id_str": "970754014609633281",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 970754014609633281,
                    "geo_enabled": true,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/970754746297536512/ppZoultT_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.pitchero.com/clubs/wythenshaweamateursfc",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/970754014609633281/1520281250",
                    "statuses_count": 223,
                    "follow_request_sent": null,
                    "followers_count": 400,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Wythenshawe Amateurs FC",
                    "location": "Manchester, England",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102082024968198,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:37 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @WAFC_Womens: Our womens 1st team are looking for new players, long term injuries have forced our hand and anyone fancying a new challen…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968397991",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Wythenshawe Amateurs FC",
                        "indices": [
                            3,
                            15
                        ],
                        "id": 970754014609633281,
                        "screen_name": "WAFC_Womens",
                        "id_str": "970754014609633281"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 950,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1097035386013011969/6UB8ydcJ_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 12329,
                "description": "God's very own| Engineer| comedian|football lover| Manchester United inside-out|",
                "created_at": "Wed Oct 05 05:31:17 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Osaroo3",
                "id_str": "385263983",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 385263983,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1097035386013011969/6UB8ydcJ_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 4979,
                "follow_request_sent": null,
                "followers_count": 465,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Goldmedalist Osaro",
                "location": "Lagos, Nigeria",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102257921503234",
            "reply_count": 0,
            "retweeted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/JdapGXItQi",
                            "indices": [
                                104,
                                127
                            ],
                            "sizes": {
                                "small": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "medium": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "large": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221048686295371783",
                            "expanded_url": "https://twitter.com/houdini__1/status/1221049699068719105/video/1",
                            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                            "id": 1221048686295371783,
                            "additional_media_info": {
                                "monetizable": false
                            },
                            "type": "video",
                            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                            "url": "https://t.co/JdapGXItQi",
                            "video_info": {
                                "aspect_ratio": [
                                    4,
                                    5
                                ],
                                "duration_millis": 140000,
                                "variants": [
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 632000,
                                        "url": "https://video.twimg.com/ext_tw_video/1221048686295371783/pu/vid/320x400/ZMtlg3dbjbxJGTiM.mp4?tag=10"
                                    },
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/ext_tw_video/1221048686295371783/pu/pl/SIXngGgaMzSVKGk3.m3u8?tag=10"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 12:38:28 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "retweet_count": 248,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221049699068719105",
                "in_reply_to_user_id": null,
                "favorite_count": 513,
                "id": 1221049699068719105,
                "text": "How can you not love football, Just take a look at these mad street football skills 😂😂😂\n#Marlians #ASUU https://t.co/JdapGXItQi",
                "place": null,
                "lang": "en",
                "quote_count": 28,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 32,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/JdapGXItQi",
                            "indices": [
                                104,
                                127
                            ],
                            "sizes": {
                                "small": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "medium": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "large": {
                                    "h": 400,
                                    "resize": "fit",
                                    "w": 320
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221048686295371783",
                            "expanded_url": "https://twitter.com/houdini__1/status/1221049699068719105/video/1",
                            "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                            "id": 1221048686295371783,
                            "additional_media_info": {
                                "monetizable": false
                            },
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1221048686295371783/pu/img/XpnNyjJSXEMmkpRn.jpg",
                            "url": "https://t.co/JdapGXItQi"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                88,
                                97
                            ],
                            "text": "Marlians"
                        },
                        {
                            "indices": [
                                98,
                                103
                            ],
                            "text": "ASUU"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    103
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 746,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1205551116043407360/GCl2E5xg_normal.jpg",
                    "listed_count": 0,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 2021,
                    "description": "How did i escape from IRAQ? IRAN 😎",
                    "created_at": "Tue Dec 03 19:13:32 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "houdini__1",
                    "id_str": "1201942357068914689",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1201942357068914689,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1205551116043407360/GCl2E5xg_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1201942357068914689/1577036810",
                    "statuses_count": 1251,
                    "follow_request_sent": null,
                    "followers_count": 699,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Jude Houd!N!",
                    "location": "planet of the ambitious ",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102257921503234,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:19 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @houdini__1: How can you not love football, Just take a look at these mad street football skills 😂😂😂\n#Marlians #ASUU https://t.co/JdapGX…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968439928",
            "entities": {
                "urls": [],
                "hashtags": [
                    {
                        "indices": [
                            104,
                            113
                        ],
                        "text": "Marlians"
                    },
                    {
                        "indices": [
                            114,
                            119
                        ],
                        "text": "ASUU"
                    }
                ],
                "user_mentions": [
                    {
                        "name": "Jude Houd!N!",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 1201942357068914689,
                        "screen_name": "houdini__1",
                        "id_str": "1201942357068914689"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/EbXuum8Xu7",
                            "source_user_id": 117442705,
                            "type": "video",
                            "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "source_status_id": 1017455687981502464,
                            "url": "https://t.co/EbXuum8Xu7",
                            "indices": [
                                71,
                                94
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1017454803503509504",
                            "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                            "source_status_id_str": "1017455687981502464",
                            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "id": 1017454803503509504,
                            "source_user_id_str": "117442705",
                            "additional_media_info": {
                                "description": null,
                                "title": null,
                                "embeddable": true,
                                "monetizable": false
                            },
                            "video_info": {
                                "aspect_ratio": [
                                    16,
                                    9
                                ],
                                "duration_millis": 163160,
                                "variants": [
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 2176000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/1280x720/nxlpH9SZDiXJ5ff7.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 288000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/320x180/DqOXLHd9PbhAJdY6.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "video/mp4",
                                        "bitrate": 832000,
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/640x360/cIXlGiMN24w9P4FJ.mp4?tag=3"
                                    },
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/amplify_video/1017454803503509504/pl/6yRvxYcbNePDJbp6.m3u8?tag=3"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 16:02:05 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 2309,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220738552834809861",
                "in_reply_to_user_id": null,
                "favorite_count": 13494,
                "id": 1220738552834809861,
                "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                "place": null,
                "lang": "en",
                "quote_count": 1428,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 546,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/EbXuum8Xu7",
                            "source_user_id": 117442705,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "source_status_id": 1017455687981502464,
                            "url": "https://t.co/EbXuum8Xu7",
                            "indices": [
                                71,
                                94
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1017454803503509504",
                            "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                            "source_status_id_str": "1017455687981502464",
                            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                            "id": 1017454803503509504,
                            "source_user_id_str": "117442705",
                            "additional_media_info": {
                                "description": null,
                                "title": null,
                                "embeddable": true,
                                "monetizable": false
                            }
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 58,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                    "listed_count": 29,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 546,
                    "description": "The Home of Football Limbs | Enquires 📧 footylimbs@gmail.com | 18+",
                    "created_at": "Fri Mar 08 15:58:59 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "FootyLimbs",
                    "id_str": "1104048876867276800",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1104048876867276800,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                    "time_zone": null,
                    "url": "http://bit.ly/500-RiskFree",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1104048876867276800/1576774795",
                    "statuses_count": 1398,
                    "follow_request_sent": null,
                    "followers_count": 63679,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Footy Limbs",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 137,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1192239252546949121/qJDk9mGc_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 1260,
                "description": null,
                "created_at": "Thu Jul 04 23:01:04 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "RMcgreechin",
                "id_str": "1146916865823956992",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1146916865823956992,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1192239252546949121/qJDk9mGc_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1146916865823956992/1562281843",
                "statuses_count": 51,
                "follow_request_sent": null,
                "followers_count": 31,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Ryan McGreechin",
                "location": "Glasgow, Scotland",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102083409174528",
            "reply_count": 0,
            "quoted_status_id": 1220738552834809861,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        154
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is the most overrated World Cup run ever."
                },
                "quoted_status": {
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EbXuum8Xu7",
                                "source_user_id": 117442705,
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "source_status_id": 1017455687981502464,
                                "url": "https://t.co/EbXuum8Xu7",
                                "indices": [
                                    71,
                                    94
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1017454803503509504",
                                "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                                "source_status_id_str": "1017455687981502464",
                                "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "id": 1017454803503509504,
                                "source_user_id_str": "117442705",
                                "additional_media_info": {
                                    "description": null,
                                    "title": null,
                                    "embeddable": true,
                                    "monetizable": false
                                },
                                "video_info": {
                                    "aspect_ratio": [
                                        16,
                                        9
                                    ],
                                    "duration_millis": 163160,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/1280x720/nxlpH9SZDiXJ5ff7.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 288000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/320x180/DqOXLHd9PbhAJdY6.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/vid/640x360/cIXlGiMN24w9P4FJ.mp4?tag=3"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/amplify_video/1017454803503509504/pl/6yRvxYcbNePDJbp6.m3u8?tag=3"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "in_reply_to_status_id_str": null,
                    "in_reply_to_status_id": null,
                    "created_at": "Fri Jan 24 16:02:05 +0000 2020",
                    "in_reply_to_user_id_str": null,
                    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                    "retweet_count": 2309,
                    "retweeted": false,
                    "geo": null,
                    "filter_level": "low",
                    "in_reply_to_screen_name": null,
                    "is_quote_status": false,
                    "id_str": "1220738552834809861",
                    "in_reply_to_user_id": null,
                    "favorite_count": 13494,
                    "id": 1220738552834809861,
                    "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                    "place": null,
                    "lang": "en",
                    "quote_count": 1428,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": false,
                    "reply_count": 546,
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/EbXuum8Xu7",
                                "source_user_id": 117442705,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "source_status_id": 1017455687981502464,
                                "url": "https://t.co/EbXuum8Xu7",
                                "indices": [
                                    71,
                                    94
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 383,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 675,
                                        "resize": "fit",
                                        "w": 1200
                                    },
                                    "large": {
                                        "h": 720,
                                        "resize": "fit",
                                        "w": 1280
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1017454803503509504",
                                "expanded_url": "https://twitter.com/GranadaReports/status/1017455687981502464/video/1",
                                "source_status_id_str": "1017455687981502464",
                                "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/1017454803503509504/img/6usiPsYLeOP9OW38.jpg",
                                "id": 1017454803503509504,
                                "source_user_id_str": "117442705",
                                "additional_media_info": {
                                    "description": null,
                                    "title": null,
                                    "embeddable": true,
                                    "monetizable": false
                                }
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "contributors": null,
                    "user": {
                        "utc_offset": null,
                        "friends_count": 58,
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                        "listed_count": 29,
                        "profile_background_image_url": null,
                        "default_profile_image": false,
                        "favourites_count": 546,
                        "description": "The Home of Football Limbs | Enquires 📧 footylimbs@gmail.com | 18+",
                        "created_at": "Fri Mar 08 15:58:59 +0000 2019",
                        "is_translator": false,
                        "profile_background_image_url_https": null,
                        "protected": false,
                        "screen_name": "FootyLimbs",
                        "id_str": "1104048876867276800",
                        "profile_link_color": "1DA1F2",
                        "translator_type": "none",
                        "id": 1104048876867276800,
                        "geo_enabled": false,
                        "profile_background_color": "F5F8FA",
                        "lang": null,
                        "profile_sidebar_border_color": "C0DEED",
                        "profile_text_color": "333333",
                        "verified": false,
                        "profile_image_url": "http://pbs.twimg.com/profile_images/1207314176865177600/gMrYf5Bo_normal.jpg",
                        "time_zone": null,
                        "url": "http://bit.ly/500-RiskFree",
                        "contributors_enabled": false,
                        "profile_background_tile": false,
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1104048876867276800/1576774795",
                        "statuses_count": 1398,
                        "follow_request_sent": null,
                        "followers_count": 63679,
                        "profile_use_background_image": true,
                        "default_profile": true,
                        "following": null,
                        "name": "Footy Limbs",
                        "location": null,
                        "profile_sidebar_fill_color": "DDEEF6",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 17:04:24 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "quoted_status_id": 1220738552834809861,
                "retweet_count": 3203,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1220754234326638593",
                "in_reply_to_user_id": null,
                "favorite_count": 21704,
                "id": 1220754234326638593,
                "text": "In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is… https://t.co/D4NNO7o9Ol",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/OioUcvBeoo",
                    "expanded": "https://twitter.com/footylimbs/status/1220738552834809861",
                    "display": "twitter.com/footylimbs/sta…"
                },
                "lang": "en",
                "quote_count": 370,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 346,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220754234326638593",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/D4NNO7o9Ol"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1220738552834809861",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 545,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1200070926248923136/RWROWNzf_normal.jpg",
                    "listed_count": 3,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 8654,
                    "description": "Remember that hibs top you bought me? you printed Porteous on it",
                    "created_at": "Mon Mar 02 21:59:22 +0000 2015",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "AidanDuffy07",
                    "id_str": "3058644439",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 3058644439,
                    "geo_enabled": false,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1200070926248923136/RWROWNzf_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/3058644439/1577756056",
                    "statuses_count": 2177,
                    "follow_request_sent": null,
                    "followers_count": 943,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Duffy",
                    "location": "Southside, Edinburgh ",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1220738552834809861",
            "id": 1221102083409174528,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:38 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @AidanDuffy07: In 90 minutes they beat Panama, Tunisia and Sweden, drew to Colombia and lost to Croatia and Belgium twice. This is the m…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968398321",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Duffy",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 3058644439,
                        "screen_name": "AidanDuffy07",
                        "id_str": "3058644439"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/OioUcvBeoo",
                "expanded": "https://twitter.com/footylimbs/status/1220738552834809861",
                "display": "twitter.com/footylimbs/sta…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        248
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "Best returning QB in every College Football Conference for 2020:\n\nACC: Trevor Lawrence(Clemson)\n\nBig Ten: Justin Fields(Ohio State)\n\nSEC: Kyle Trask(Florida)\n\nPac-12: Kedon Slovis(USC)\n\nBig 12: Sam Ehlinger(Texas)\n\nIndependent: Ian Book(Notre Dame)"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Thu Jan 23 23:22:28 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 203,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220486991067803650",
                "in_reply_to_user_id": null,
                "favorite_count": 1339,
                "id": 1220486991067803650,
                "text": "Best returning QB in every College Football Conference for 2020:\n\nACC: Trevor Lawrence(Clemson)\n\nBig Ten: Justin Fi… https://t.co/TYq80Seltf",
                "place": null,
                "lang": "en",
                "quote_count": 45,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 32,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220486991067803650",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/TYq80Seltf"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 4966,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1204048780921724929/z4d_YMke_normal.jpg",
                    "listed_count": 7,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 127,
                    "description": "The place for all College Football & Basketball updates.",
                    "created_at": "Fri Nov 15 15:07:44 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "NCAA_Elite",
                    "id_str": "1195357687241822208",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1195357687241822208,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1204048780921724929/z4d_YMke_normal.jpg",
                    "time_zone": null,
                    "url": "https://www.instagram.com/collegesportselite/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1195357687241822208/1575912994",
                    "statuses_count": 400,
                    "follow_request_sent": null,
                    "followers_count": 4525,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "CollegeSports Elite",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 263,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1114874640873213952/NUoNzTF5_normal.jpg",
                "listed_count": 2,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 8794,
                "description": "4/12/15 RIP B Stites",
                "created_at": "Sat Dec 24 04:21:48 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "_DavidBrown15",
                "id_str": "445209662",
                "profile_link_color": "0084B4",
                "translator_type": "none",
                "id": 445209662,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1114874640873213952/NUoNzTF5_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/445209662/1554641804",
                "statuses_count": 27920,
                "follow_request_sent": null,
                "followers_count": 713,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "D Breezy ™ ⛵️",
                "location": "Greenville, SC📍",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102051528265729",
            "reply_count": 0,
            "quoted_status_id": 1220486991067803650,
            "quoted_status_id_str": "1220486991067803650",
            "id": 1221102051528265729,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:30 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "🐊🐊🐊🐊🐊",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "und",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968390720",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/QIS0NX2P6t",
                "expanded": "https://twitter.com/ncaa_elite/status/1220486991067803650",
                "display": "twitter.com/ncaa_elite/sta…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 885,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220131053723144192/kw7NLb-3_normal.jpg",
                "listed_count": 3,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 208,
                "description": "You can’t buy your way to success 👌 | Manchester United Fan | #MUFC",
                "created_at": "Thu May 04 18:18:04 +0000 2017",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "opynice1",
                "id_str": "860196843690627073",
                "profile_link_color": "E81C4F",
                "translator_type": "none",
                "id": 860196843690627073,
                "geo_enabled": true,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1220131053723144192/kw7NLb-3_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/860196843690627073/1579462244",
                "statuses_count": 78026,
                "follow_request_sent": null,
                "followers_count": 905,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "OPY NICEONE",
                "location": null,
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102634037399554",
            "reply_count": 0,
            "id": 1221102634037399554,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:49 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "Is this football Barcelona Fc promise us to starting watching now ? Ogun dem them and I carry Barcelona first to goal... Ogbeni 😒😒😒😒",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968529601",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 502,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/931122071060516865/KeOYgaD2_normal.jpg",
                "listed_count": 5,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 11409,
                "description": "Man Utd #MUFC Miami Dolphins #FINSUP New York Mets #LGM Melbourne Stars #TEAMGREEN Essex Eagles #soarwithus",
                "created_at": "Tue Oct 11 09:42:33 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "davidplittle",
                "id_str": "388768505",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 388768505,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/931122071060516865/KeOYgaD2_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/388768505/1366717055",
                "statuses_count": 14702,
                "follow_request_sent": null,
                "followers_count": 249,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "David Little",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102582694850560",
            "reply_count": 0,
            "retweeted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/Ld3DV0c3FW",
                            "indices": [
                                89,
                                112
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221102276716220418",
                            "expanded_url": "https://twitter.com/GWRovers/status/1221102278578462720/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI6DQ4XUAI9Zt9.jpg",
                            "id": 1221102276716220418,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI6DQ4XUAI9Zt9.jpg",
                            "url": "https://t.co/Ld3DV0c3FW"
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:07:24 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://www.footballwebpages.co.uk\" rel=\"nofollow\">Football Web Pages</a>",
                "retweet_count": 1,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221102278578462720",
                "in_reply_to_user_id": null,
                "favorite_count": 1,
                "id": 1221102278578462720,
                "text": "ATTENDANCE: Great Wakering Rovers v Histon - 131 #IsthmianLeague https://t.co/ieIRdLBIp0 https://t.co/Ld3DV0c3FW",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.footballwebpages.co.uk/match/2019-2020/isthmian-football-league-north-division/great-wakering-rovers/histon/144466",
                            "display_url": "footballwebpages.co.uk/match/2019-202…",
                            "indices": [
                                65,
                                88
                            ],
                            "url": "https://t.co/ieIRdLBIp0"
                        }
                    ],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/Ld3DV0c3FW",
                            "indices": [
                                89,
                                112
                            ],
                            "sizes": {
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221102276716220418",
                            "expanded_url": "https://twitter.com/GWRovers/status/1221102278578462720/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI6DQ4XUAI9Zt9.jpg",
                            "id": 1221102276716220418,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI6DQ4XUAI9Zt9.jpg",
                            "url": "https://t.co/Ld3DV0c3FW"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                49,
                                64
                            ],
                            "text": "IsthmianLeague"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    88
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 437,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1191260439633711105/01N7or0v_normal.jpg",
                    "listed_count": 43,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 1861,
                    "description": "Formed in 1919. Members of The Isthmian Football League & Essex County FA. Manager Stephen Butterworth",
                    "created_at": "Wed Apr 01 23:48:04 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "GWRovers",
                    "id_str": "28229743",
                    "profile_link_color": "19CF86",
                    "translator_type": "none",
                    "id": 28229743,
                    "geo_enabled": true,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1191260439633711105/01N7or0v_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.gwrovers.com",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/28229743/1573398238",
                    "statuses_count": 9556,
                    "follow_request_sent": null,
                    "followers_count": 4434,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Gt Wakering Rovers",
                    "location": "Great Wakering",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102582694850560,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:37 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @GWRovers: ATTENDANCE: Great Wakering Rovers v Histon - 131 #IsthmianLeague https://t.co/ieIRdLBIp0 https://t.co/Ld3DV0c3FW",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968517360",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.footballwebpages.co.uk/match/2019-2020/isthmian-football-league-north-division/great-wakering-rovers/histon/144466",
                        "display_url": "footballwebpages.co.uk/match/2019-202…",
                        "indices": [
                            79,
                            102
                        ],
                        "url": "https://t.co/ieIRdLBIp0"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/Ld3DV0c3FW",
                        "source_user_id": 28229743,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI6DQ4XUAI9Zt9.jpg",
                        "source_status_id": 1221102278578462720,
                        "url": "https://t.co/Ld3DV0c3FW",
                        "indices": [
                            103,
                            126
                        ],
                        "sizes": {
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 1280
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221102276716220418",
                        "expanded_url": "https://twitter.com/GWRovers/status/1221102278578462720/photo/1",
                        "source_status_id_str": "1221102278578462720",
                        "media_url_https": "https://pbs.twimg.com/media/EPI6DQ4XUAI9Zt9.jpg",
                        "id": 1221102276716220418,
                        "source_user_id_str": "28229743"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            63,
                            78
                        ],
                        "text": "IsthmianLeague"
                    }
                ],
                "user_mentions": [
                    {
                        "name": "Gt Wakering Rovers",
                        "indices": [
                            3,
                            12
                        ],
                        "id": 28229743,
                        "screen_name": "GWRovers",
                        "id_str": "28229743"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/Ld3DV0c3FW",
                        "source_user_id": 28229743,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI6DQ4XUAI9Zt9.jpg",
                        "source_status_id": 1221102278578462720,
                        "url": "https://t.co/Ld3DV0c3FW",
                        "indices": [
                            103,
                            126
                        ],
                        "sizes": {
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 1280
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221102276716220418",
                        "expanded_url": "https://twitter.com/GWRovers/status/1221102278578462720/photo/1",
                        "source_status_id_str": "1221102278578462720",
                        "media_url_https": "https://pbs.twimg.com/media/EPI6DQ4XUAI9Zt9.jpg",
                        "id": 1221102276716220418,
                        "source_user_id_str": "28229743"
                    }
                ]
            },
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 2040,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1181981719118827520/By_a2yVs_normal.jpg",
                "listed_count": 3,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 222,
                "description": "Juventus FC BOT founder: @Juventusruling",
                "created_at": "Sat Aug 10 16:05:24 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "JuveTweetBot",
                "id_str": "1160220612033310720",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1160220612033310720,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1181981719118827520/By_a2yVs_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1160220612033310720/1570639189",
                "statuses_count": 12096,
                "follow_request_sent": null,
                "followers_count": 505,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Juventus News | RT bot",
                "location": "Twitter ",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102631373942789",
            "reply_count": 0,
            "id": 1221102631373942789,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:48 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    185
                ],
                "entities": {
                    "urls": [],
                    "hashtags": [
                        {
                            "indices": [
                                178,
                                185
                            ],
                            "text": "SerieA"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "Serie A Week 21 referees\n\nThe referees for Serie A week 21 have been announced, and Gianpaolo Calvarese has been given the derby match between Roma and Lazio.\n[football-italia] \n#SerieA"
            },
            "source": "<a href=\"https://juventuslive.epziy.com\" rel=\"nofollow\">Juventus Live Tv</a>",
            "text": "Serie A Week 21 referees\n\nThe referees for Serie A week 21 have been announced, and Gianpaolo Calvarese has been gi… https://t.co/wgIvmCbHSv",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968528966",
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102631373942789",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/wgIvmCbHSv"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 632,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1188477670071427072/Vi_cY50U_normal.jpg",
                "listed_count": 4,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 14018,
                "description": "23",
                "created_at": "Wed Jul 04 15:57:52 +0000 2012",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "joe_painter0",
                "id_str": "626563919",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 626563919,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1188477670071427072/Vi_cY50U_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 16972,
                "follow_request_sent": null,
                "followers_count": 1288,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "joe painter",
                "location": "Hull",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102590416556036",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        244
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [
                            {
                                "indices": [
                                    237,
                                    244
                                ],
                                "text": "Bisons"
                            }
                        ],
                        "user_mentions": [
                            {
                                "name": "SOUTH PARK RANGERS",
                                "indices": [
                                    4,
                                    13
                                ],
                                "id": 1142068564926636034,
                                "screen_name": "Spr2019_",
                                "id_str": "1142068564926636034"
                            },
                            {
                                "name": "Liam Allenby",
                                "indices": [
                                    182,
                                    195
                                ],
                                "id": 2337739275,
                                "screen_name": "LiamAllenby_",
                                "id_str": "2337739275"
                            },
                            {
                                "name": "jack ♛",
                                "indices": [
                                    200,
                                    212
                                ],
                                "id": 325192294,
                                "screen_name": "JackMortley",
                                "id_str": "325192294"
                            },
                            {
                                "name": "Liam Allenby",
                                "indices": [
                                    221,
                                    234
                                ],
                                "id": 2337739275,
                                "screen_name": "LiamAllenby_",
                                "id_str": "2337739275"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "FT: @Spr2019_ 1 - 4 Souths \n\nGood second half performance ensures we continue our winning form. Good effort from everyone along with some nice football being played. \n\nGoalscorers: \n@LiamAllenby_ x 3\n@JackMortley \n\nMOTM: @LiamAllenby_ \n\n#Bisons"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:01:00 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 2,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221100666619400193",
                "in_reply_to_user_id": null,
                "favorite_count": 2,
                "id": 1221100666619400193,
                "text": "FT: @Spr2019_ 1 - 4 Souths \n\nGood second half performance ensures we continue our winning form. Good effort from ev… https://t.co/Eb8QarShbM",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1221100666619400193",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/Eb8QarShbM"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "SOUTH PARK RANGERS",
                            "indices": [
                                4,
                                13
                            ],
                            "id": 1142068564926636034,
                            "screen_name": "Spr2019_",
                            "id_str": "1142068564926636034"
                        }
                    ],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 171,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1042042646401830913/ijpyzMt2_normal.jpg",
                    "listed_count": 0,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 806,
                    "description": "ERCL Division 2 19/20. Division 5 Champions 18/19🏆 Harold Robinson Cup Winners 18/19 🏆 FA Charter Standard Club. Home ground - South Holderness 3G. #Bisons",
                    "created_at": "Sun May 20 16:03:10 +0000 2018",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "souths_fc",
                    "id_str": "998232673603784704",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 998232673603784704,
                    "geo_enabled": true,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1042042646401830913/ijpyzMt2_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/998232673603784704/1526845856",
                    "statuses_count": 544,
                    "follow_request_sent": null,
                    "followers_count": 196,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Souths FC",
                    "location": "Hull, England",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102590416556036,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:39 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @souths_fc: FT: @Spr2019_ 1 - 4 Souths \n\nGood second half performance ensures we continue our winning form. Good effort from everyone al…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968519201",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Souths FC",
                        "indices": [
                            3,
                            13
                        ],
                        "id": 998232673603784704,
                        "screen_name": "souths_fc",
                        "id_str": "998232673603784704"
                    },
                    {
                        "name": "SOUTH PARK RANGERS",
                        "indices": [
                            19,
                            28
                        ],
                        "id": 1142068564926636034,
                        "screen_name": "Spr2019_",
                        "id_str": "1142068564926636034"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:02:35 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 1,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221101062872096769",
                "in_reply_to_user_id": null,
                "favorite_count": 5,
                "id": 1221101062872096769,
                "text": "NUFC player ratings https://t.co/QTw7GE8X8O #nufc",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 3,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.chroniclelive.co.uk/sport/football/football-news/newcastle-united-player-ratings-magpies-17631384?utm_source=twitter.com&utm_medium=social&utm_campaign=sharebar",
                            "display_url": "chroniclelive.co.uk/sport/football…",
                            "indices": [
                                20,
                                43
                            ],
                            "url": "https://t.co/QTw7GE8X8O"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                44,
                                49
                            ],
                            "text": "nufc"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 2297,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/791257304385609728/7uS0O137_normal.jpg",
                    "listed_count": 707,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 1817,
                    "description": "The Chronicle's Chief NUFC Writer. Follow #nufc home and away. https://t.co/0tsB8gJp0k https://t.co/AuFOad0Y9c",
                    "created_at": "Sun Feb 08 18:46:49 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "lee_ryder",
                    "id_str": "20383794",
                    "profile_link_color": "0084B4",
                    "translator_type": "none",
                    "id": 20383794,
                    "geo_enabled": true,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/791257304385609728/7uS0O137_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.chroniclelive.co.uk/authors/lee-ryder/",
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/20383794/1355161800",
                    "statuses_count": 80569,
                    "follow_request_sent": null,
                    "followers_count": 109313,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Lee Ryder",
                    "location": "North Shields",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 248,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1180925698107744257/_hhysc2U_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 6220,
                "description": "NUFC & Balti pies",
                "created_at": "Thu Nov 27 20:00:34 +0000 2014",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "NathanM71500393",
                "id_str": "2895096190",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 2895096190,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1180925698107744257/_hhysc2U_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2895096190/1480183958",
                "statuses_count": 643,
                "follow_request_sent": null,
                "followers_count": 98,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Nathan Miller",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101645255315462",
            "reply_count": 0,
            "quoted_status_id": 1221101062872096769,
            "quoted_status_id_str": "1221101062872096769",
            "id": 1221101645255315462,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:04:53 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "Paul Dummet 7 #NUFC #ratings",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968293857",
            "entities": {
                "urls": [],
                "hashtags": [
                    {
                        "indices": [
                            14,
                            19
                        ],
                        "text": "NUFC"
                    },
                    {
                        "indices": [
                            20,
                            28
                        ],
                        "text": "ratings"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/CqEz1VEoMU",
                "expanded": "https://twitter.com/lee_ryder/status/1221101062872096769",
                "display": "twitter.com/lee_ryder/stat…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 679,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1068115074563350528/KTiHogLr_normal.jpg",
                "listed_count": 9,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme18/bg.gif",
                "default_profile_image": false,
                "favourites_count": 144072,
                "description": null,
                "created_at": "Thu Jul 02 22:03:27 +0000 2009",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme18/bg.gif",
                "protected": false,
                "screen_name": "1CraigFisher",
                "id_str": "53202775",
                "profile_link_color": "0C29E8",
                "translator_type": "none",
                "id": 53202775,
                "geo_enabled": true,
                "profile_background_color": "3AB8E6",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1068115074563350528/KTiHogLr_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/53202775/1567631576",
                "statuses_count": 18259,
                "follow_request_sent": null,
                "followers_count": 501,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Craig Fisher",
                "location": null,
                "profile_sidebar_fill_color": "F6F6F6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102384883142656",
            "reply_count": 0,
            "id": 1221102384883142656,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:50 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "Fuck all goals today in the football!",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968470198",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "in_reply_to_status_id_str": "1221002166128627714",
                "in_reply_to_status_id": 1221002166128627714,
                "created_at": "Sat Jan 25 15:54:54 +0000 2020",
                "in_reply_to_user_id_str": "441636351",
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 6,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": "MEAIndia",
                "is_quote_status": false,
                "id_str": "1221099133462814725",
                "in_reply_to_user_id": 441636351,
                "favorite_count": 30,
                "id": 1221099133462814725,
                "text": "Read the India - Brazil Joint Statement released during the ongoing State Visit of President @jairbolsonaro at https://t.co/VhraeS2zKQ",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 1,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "http://mymea.in/eqf",
                            "display_url": "mymea.in/eqf",
                            "indices": [
                                111,
                                134
                            ],
                            "url": "https://t.co/VhraeS2zKQ"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [
                        {
                            "name": "Jair M. Bolsonaro",
                            "indices": [
                                93,
                                107
                            ],
                            "id": 128372940,
                            "screen_name": "jairbolsonaro",
                            "id_str": "128372940"
                        }
                    ],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 872,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/893447414169743361/XnWvdUhM_normal.jpg",
                    "listed_count": 1862,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme19/bg.gif",
                    "default_profile_image": false,
                    "favourites_count": 58,
                    "description": "Official Spokesperson, Ministry of External Affairs, India. #Alert : #Passport issues may kindly be addressed to → @CPVIndia @passportsevamea",
                    "created_at": "Tue Dec 20 08:31:03 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme19/bg.gif",
                    "protected": false,
                    "screen_name": "MEAIndia",
                    "id_str": "441636351",
                    "profile_link_color": "0099CC",
                    "translator_type": "none",
                    "id": 441636351,
                    "geo_enabled": true,
                    "profile_background_color": "FFF04D",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/893447414169743361/XnWvdUhM_normal.jpg",
                    "time_zone": null,
                    "url": "http://mea.gov.in",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/441636351/1560783706",
                    "statuses_count": 21075,
                    "follow_request_sent": null,
                    "followers_count": 2025240,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Raveesh Kumar",
                    "location": null,
                    "profile_sidebar_fill_color": "F6FFD1",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 348,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/626801003837329409/dddUnsVF_normal.jpg",
                "listed_count": 4,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme4/bg.gif",
                "default_profile_image": false,
                "favourites_count": 2368,
                "description": "भारतीय होना गर्व की बात है",
                "created_at": "Sat Jul 02 03:51:51 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme4/bg.gif",
                "protected": false,
                "screen_name": "digeswarjha",
                "id_str": "327773126",
                "profile_link_color": "0099B9",
                "translator_type": "none",
                "id": 327773126,
                "geo_enabled": false,
                "profile_background_color": "0099B9",
                "lang": null,
                "profile_sidebar_border_color": "5ED4DC",
                "profile_text_color": "3C3940",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/626801003837329409/dddUnsVF_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/327773126/1573734436",
                "statuses_count": 2642,
                "follow_request_sent": null,
                "followers_count": 58,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Digeswar Jha ★★",
                "location": "Ranchi, Jharkhand",
                "profile_sidebar_fill_color": "95E8EC",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101959727312897",
            "reply_count": 0,
            "quoted_status_id": 1221099133462814725,
            "quoted_status_id_str": "1221099133462814725",
            "id": 1221101959727312897,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:08 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "Football is missing",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968368833",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/a8bVZ6wrVq",
                "expanded": "https://twitter.com/MEAIndia/status/1221099133462814725",
                "display": "twitter.com/MEAIndia/statu…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        148
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/bx6mcbFuYg",
                                "source_user_id": 165086088,
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1197888932890992640/pu/img/_g__HfU7eZp0jJUe.jpg",
                                "source_status_id": 1197889172062822400,
                                "url": "https://t.co/bx6mcbFuYg",
                                "indices": [
                                    125,
                                    148
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 680,
                                        "resize": "fit",
                                        "w": 383
                                    },
                                    "medium": {
                                        "h": 1200,
                                        "resize": "fit",
                                        "w": 675
                                    },
                                    "large": {
                                        "h": 1280,
                                        "resize": "fit",
                                        "w": 720
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1197888932890992640",
                                "expanded_url": "https://twitter.com/Wes_nship/status/1197889172062822400/video/1",
                                "source_status_id_str": "1197889172062822400",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1197888932890992640/pu/img/_g__HfU7eZp0jJUe.jpg",
                                "id": 1197888932890992640,
                                "source_user_id_str": "165086088",
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "video_info": {
                                    "aspect_ratio": [
                                        9,
                                        16
                                    ],
                                    "duration_millis": 59065,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 632000,
                                            "url": "https://video.twimg.com/ext_tw_video/1197888932890992640/pu/vid/320x568/KfN1m4gLrmIsnU1W.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/ext_tw_video/1197888932890992640/pu/vid/720x1280/vR0l3dT80h6lqWfW.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1197888932890992640/pu/pl/eDwCCwEV58pJAJGo.m3u8?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/ext_tw_video/1197888932890992640/pu/vid/360x640/PPoq1G88Niy_tmwU.mp4?tag=10"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/bx6mcbFuYg",
                                "source_user_id": 165086088,
                                "type": "video",
                                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1197888932890992640/pu/img/_g__HfU7eZp0jJUe.jpg",
                                "source_status_id": 1197889172062822400,
                                "url": "https://t.co/bx6mcbFuYg",
                                "indices": [
                                    125,
                                    148
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 680,
                                        "resize": "fit",
                                        "w": 383
                                    },
                                    "medium": {
                                        "h": 1200,
                                        "resize": "fit",
                                        "w": 675
                                    },
                                    "large": {
                                        "h": 1280,
                                        "resize": "fit",
                                        "w": 720
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1197888932890992640",
                                "expanded_url": "https://twitter.com/Wes_nship/status/1197889172062822400/video/1",
                                "source_status_id_str": "1197889172062822400",
                                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1197888932890992640/pu/img/_g__HfU7eZp0jJUe.jpg",
                                "id": 1197888932890992640,
                                "source_user_id_str": "165086088",
                                "additional_media_info": {
                                    "monetizable": false
                                },
                                "video_info": {
                                    "aspect_ratio": [
                                        9,
                                        16
                                    ],
                                    "duration_millis": 59065,
                                    "variants": [
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 632000,
                                            "url": "https://video.twimg.com/ext_tw_video/1197888932890992640/pu/vid/320x568/KfN1m4gLrmIsnU1W.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 2176000,
                                            "url": "https://video.twimg.com/ext_tw_video/1197888932890992640/pu/vid/720x1280/vR0l3dT80h6lqWfW.mp4?tag=10"
                                        },
                                        {
                                            "content_type": "application/x-mpegURL",
                                            "url": "https://video.twimg.com/ext_tw_video/1197888932890992640/pu/pl/eDwCCwEV58pJAJGo.m3u8?tag=10"
                                        },
                                        {
                                            "content_type": "video/mp4",
                                            "bitrate": 832000,
                                            "url": "https://video.twimg.com/ext_tw_video/1197888932890992640/pu/vid/360x640/PPoq1G88Niy_tmwU.mp4?tag=10"
                                        }
                                    ]
                                }
                            }
                        ],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "This dude’s impression of high school football radio announcers in the South just may be the greatest thing I’ve ever seen.  https://t.co/bx6mcbFuYg"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Nov 23 01:13:57 +0000 2019",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 338,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1198046996709425152",
                "in_reply_to_user_id": null,
                "favorite_count": 1538,
                "id": 1198046996709425152,
                "text": "This dude’s impression of high school football radio announcers in the South just may be the greatest thing I’ve ev… https://t.co/wQEdoVVnDe",
                "place": null,
                "lang": "en",
                "quote_count": 77,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 37,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1198046996709425152",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/wQEdoVVnDe"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 638,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/2410406952/r2s9t3pz6g63yyspvhnn_normal.jpeg",
                    "listed_count": 368,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme9/bg.gif",
                    "default_profile_image": false,
                    "favourites_count": 207,
                    "description": "Diligence by the media is paramount, and all aspects of the Kentucky basketball program must be constantly scrutinized. Pulitzers don't grow on trees. (Parody)",
                    "created_at": "Wed Dec 22 20:46:27 +0000 2010",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme9/bg.gif",
                    "protected": false,
                    "screen_name": "NotJerryTipton",
                    "id_str": "229601344",
                    "profile_link_color": "2FC2EF",
                    "translator_type": "none",
                    "id": 229601344,
                    "geo_enabled": true,
                    "profile_background_color": "1A1B1F",
                    "lang": null,
                    "profile_sidebar_border_color": "181A1E",
                    "profile_text_color": "666666",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/2410406952/r2s9t3pz6g63yyspvhnn_normal.jpeg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/229601344/1348023566",
                    "statuses_count": 25411,
                    "follow_request_sent": null,
                    "followers_count": 77551,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Not Jerry Tipton",
                    "location": "The Hall of Fame, baby",
                    "profile_sidebar_fill_color": "252429",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 725,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1203866903711801346/hLxVVcR2_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 2426,
                "description": "Proud dad of Caleb, Abbi and Gracie. Married to VV Volleyball coach Margie",
                "created_at": "Fri Jul 29 01:49:21 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "b_ray_mcgee",
                "id_str": "344428599",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 344428599,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1203866903711801346/hLxVVcR2_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/344428599/1485770018",
                "statuses_count": 1493,
                "follow_request_sent": null,
                "followers_count": 340,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Barry Ray",
                "location": "Arkansas, USA",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102619751481344",
            "reply_count": 0,
            "quoted_status_id": 1198046996709425152,
            "quoted_status_id_str": "1198046996709425152",
            "id": 1221102619751481344,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:46 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "Wow",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "und",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968526195",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/D86xFSViq6",
                "expanded": "https://twitter.com/notjerrytipton/status/1198046996709425152",
                "display": "twitter.com/notjerrytipton…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 159,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1090300635172474881/IxklC3Gm_normal.jpg",
                "listed_count": 1,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme18/bg.gif",
                "default_profile_image": false,
                "favourites_count": 13887,
                "description": "insta: _maarifornia 👻: whoricator",
                "created_at": "Sat Jul 18 02:39:21 +0000 2009",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme18/bg.gif",
                "protected": false,
                "screen_name": "_maarifornia",
                "id_str": "57831687",
                "profile_link_color": "038543",
                "translator_type": "none",
                "id": 57831687,
                "geo_enabled": true,
                "profile_background_color": "ACDED6",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1090300635172474881/IxklC3Gm_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/57831687/1548782755",
                "statuses_count": 10844,
                "follow_request_sent": null,
                "followers_count": 490,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "tacobella",
                "location": "Probably w gootch",
                "profile_sidebar_fill_color": "F6F6F6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101973262544896",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 20:44:53 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 2,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220809722221268997",
                "in_reply_to_user_id": null,
                "favorite_count": 2,
                "id": 1220809722221268997,
                "text": "Maples Collegiate now has a flag football team for girls. https://t.co/SBM9yzP7hg",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.winnipegfreepress.com/our-communities/times/New-flag-football-team-at-Maples-Collegiate-567271251.html",
                            "display_url": "winnipegfreepress.com/our-communitie…",
                            "indices": [
                                58,
                                81
                            ],
                            "url": "https://t.co/SBM9yzP7hg"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 544,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/648938176384405504/wcgAP4PM_normal.jpg",
                    "listed_count": 39,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 69,
                    "description": "Community news for northwest Winnipeg. News tips are welcome! Call 204-697-7206 or email sydney.hildebrandt@canstarnews.com",
                    "created_at": "Thu Feb 03 23:06:31 +0000 2011",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "TimesWPG",
                    "id_str": "247024764",
                    "profile_link_color": "B30000",
                    "translator_type": "none",
                    "id": 247024764,
                    "geo_enabled": false,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/648938176384405504/wcgAP4PM_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.canstarnews.com",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/247024764/1572279851",
                    "statuses_count": 2085,
                    "follow_request_sent": null,
                    "followers_count": 1047,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "The Times",
                    "location": "Northwest Winnipeg",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221101973262544896,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:12 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @TimesWPG: Maples Collegiate now has a flag football team for girls. https://t.co/SBM9yzP7hg",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968372060",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.winnipegfreepress.com/our-communities/times/New-flag-football-team-at-Maples-Collegiate-567271251.html",
                        "display_url": "winnipegfreepress.com/our-communitie…",
                        "indices": [
                            72,
                            95
                        ],
                        "url": "https://t.co/SBM9yzP7hg"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "The Times",
                        "indices": [
                            3,
                            12
                        ],
                        "id": 247024764,
                        "screen_name": "TimesWPG",
                        "id_str": "247024764"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1855,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1182872206088359937/abtfu7P5_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 0,
                "description": "🇮🇹Serie A bot  :) Bot will post all Serie A related datas from 1993 - 2019",
                "created_at": "Fri Oct 11 17:47:50 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "BotSerieA",
                "id_str": "1182714365381894144",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1182714365381894144,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1182872206088359937/abtfu7P5_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1182714365381894144/1570817852",
                "statuses_count": 11053,
                "follow_request_sent": null,
                "followers_count": 87,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Serie A Bot",
                "location": "Serie A Twitter",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102380273557511",
            "reply_count": 0,
            "id": 1221102380273557511,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:49 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    201
                ],
                "entities": {
                    "urls": [],
                    "hashtags": [
                        {
                            "indices": [
                                194,
                                201
                            ],
                            "text": "SerieA"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "Sarri: 'I could retire after Juventus'\n\nMaurizio Sarri would see jeers as “a sign of affection” from his old Napoli fans, but hints Juventus could be his final coaching role.\n[football-italia] \n#SerieA"
            },
            "source": "<a href=\"https://iamnazeem.me\" rel=\"nofollow\">Bot Serie A </a>",
            "text": "Sarri: 'I could retire after Juventus'\n\nMaurizio Sarri would see jeers as “a sign of affection” from his old Napoli… https://t.co/RNKz9IwV0I",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968469099",
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102380273557511",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/RNKz9IwV0I"
                    }
                ],
                "hashtags": [],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": true,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 203,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1064147335549239297/_nreisjJ_normal.jpg",
                "listed_count": 42,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 371,
                "description": "Members of Cambridgeshire FA, Isthmian League and Cambridgeshire League\n\n📷 https://instagram.com/sohamtownfc",
                "created_at": "Thu Jun 23 18:27:27 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "SohamTownRanger",
                "id_str": "322771240",
                "profile_link_color": "4A913C",
                "translator_type": "none",
                "id": 322771240,
                "geo_enabled": false,
                "profile_background_color": "FCFCFC",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1064147335549239297/_nreisjJ_normal.jpg",
                "time_zone": null,
                "url": "http://www.pitchero.com/clubs/sohamtownrangersfc/",
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/322771240/1435502385",
                "statuses_count": 19295,
                "follow_request_sent": null,
                "followers_count": 4925,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Soham Town Rangers FC",
                "location": "Soham, Cambridgeshire - CB7 5E",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101968740974597",
            "reply_count": 0,
            "display_text_range": [
                0,
                98
            ],
            "id": 1221101968740974597,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:10 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://www.footballwebpages.co.uk\" rel=\"nofollow\">Football Web Pages</a>",
            "text": "KICK-OFF (SECOND-HALF): Canvey Island v Soham Town Rangers #IsthmianLeague https://t.co/HEt0YK1gHi https://t.co/sFdoJU59TC",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968370982",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.footballwebpages.co.uk/match/2019-2020/isthmian-football-league-north-division/canvey-island/soham-town-rangers/144463",
                        "display_url": "footballwebpages.co.uk/match/2019-202…",
                        "indices": [
                            75,
                            98
                        ],
                        "url": "https://t.co/HEt0YK1gHi"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/sFdoJU59TC",
                        "indices": [
                            99,
                            122
                        ],
                        "sizes": {
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 1280
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221101966773886984",
                        "expanded_url": "https://twitter.com/SohamTownRanger/status/1221101968740974597/photo/1",
                        "media_url_https": "https://pbs.twimg.com/media/EPI5xOQWoAgc1fN.jpg",
                        "id": 1221101966773886984,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI5xOQWoAgc1fN.jpg",
                        "url": "https://t.co/sFdoJU59TC"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            59,
                            74
                        ],
                        "text": "IsthmianLeague"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/sFdoJU59TC",
                        "indices": [
                            99,
                            122
                        ],
                        "sizes": {
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 1280
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221101966773886984",
                        "expanded_url": "https://twitter.com/SohamTownRanger/status/1221101968740974597/photo/1",
                        "media_url_https": "https://pbs.twimg.com/media/EPI5xOQWoAgc1fN.jpg",
                        "id": 1221101966773886984,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI5xOQWoAgc1fN.jpg",
                        "url": "https://t.co/sFdoJU59TC"
                    }
                ]
            },
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 182,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/558806480099741696/cBD-IJTD_normal.jpeg",
                "listed_count": 6,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 789,
                "description": "#OAFC fan. Stage 4 #Cancer fighter and #SepticShock survivor. Keen photographer, also, keen interest in Local/National Politics.",
                "created_at": "Mon Nov 26 10:19:46 +0000 2012",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "pgreen83",
                "id_str": "971691408",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 971691408,
                "geo_enabled": true,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/558806480099741696/cBD-IJTD_normal.jpeg",
                "time_zone": null,
                "url": "https://paulgreen83.wixsite.com/pg-photography",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/971691408/1420864722",
                "statuses_count": 1901,
                "follow_request_sent": null,
                "followers_count": 165,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Paul Green",
                "location": "Royton, Oldham",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102316763435009",
            "reply_count": 0,
            "id": 1221102316763435009,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:33 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "My god 6 points off the bottom of the league. That’s bottom of the Professional Football League! Just WOW! #oafc",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968453957",
            "entities": {
                "urls": [],
                "hashtags": [
                    {
                        "indices": [
                            107,
                            112
                        ],
                        "text": "oafc"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 659,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1215829206606721024/J5UiQGdc_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 16790,
                "description": "AFC only",
                "created_at": "Sun Sep 08 20:49:55 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "Realistone123",
                "id_str": "1170801427196891137",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1170801427196891137,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1215829206606721024/J5UiQGdc_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1170801427196891137/1577588066",
                "statuses_count": 8496,
                "follow_request_sent": null,
                "followers_count": 170,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Ike Turner Got The Burner",
                "location": "None of yo buisness biatch",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102812215554050",
            "reply_count": 0,
            "display_text_range": [
                9,
                121
            ],
            "id": 1221102812215554050,
            "in_reply_to_user_id": 34613288,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:32 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "@Arsenal Rosicky better than Ramsey and that’s facts. People that disagree are British or lack the knowledge to Football.",
            "in_reply_to_user_id_str": "34613288",
            "in_reply_to_status_id": 1221100917396852744,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": "Arsenal",
            "place": null,
            "timestamp_ms": "1579968572082",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Arsenal",
                        "indices": [
                            0,
                            8
                        ],
                        "id": 34613288,
                        "screen_name": "Arsenal",
                        "id_str": "34613288"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": "1221100917396852744",
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 2290,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1203729208410693632/GUrgkzN9_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 57071,
                "description": "A simple guy with lots of quality to admire ..😉",
                "created_at": "Fri Aug 09 02:52:21 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "BhaiSelan",
                "id_str": "1159658647749718016",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1159658647749718016,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1203729208410693632/GUrgkzN9_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1159658647749718016/1574279856",
                "statuses_count": 40058,
                "follow_request_sent": null,
                "followers_count": 152,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Selan Bhai",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102066975641600",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 15:50:00 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "retweet_count": 2,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221097897212751872",
                "in_reply_to_user_id": null,
                "favorite_count": 41,
                "id": 1221097897212751872,
                "text": "It's not done yet. https://t.co/aFrH6YpHt8",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 1,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.football.london/arsenal-fc/transfer-news/pablo-mari-arsenal-transfer-news-17630154",
                            "display_url": "football.london/arsenal-fc/tra…",
                            "indices": [
                                19,
                                42
                            ],
                            "url": "https://t.co/aFrH6YpHt8"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 146,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1204801263575191552/MdKRNC8B_normal.jpg",
                    "listed_count": 318,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 50,
                    "description": "All the latest Arsenal news, analysis and opinion from @Football_LDN. Like us on Facebook for more: https://www.facebook.com/AFCFootball.London",
                    "created_at": "Fri Nov 04 13:36:56 +0000 2016",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "ArsenalFC_fl",
                    "id_str": "794533892778815488",
                    "profile_link_color": "992200",
                    "translator_type": "none",
                    "id": 794533892778815488,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1204801263575191552/MdKRNC8B_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.football.london/arsenal-fc/",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/794533892778815488/1577969204",
                    "statuses_count": 42118,
                    "follow_request_sent": null,
                    "followers_count": 56894,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "Arsenal FC News",
                    "location": "London, England",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "id": 1221102066975641600,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:34 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @ArsenalFC_fl: It's not done yet. https://t.co/aFrH6YpHt8",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968394403",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.football.london/arsenal-fc/transfer-news/pablo-mari-arsenal-transfer-news-17630154",
                        "display_url": "football.london/arsenal-fc/tra…",
                        "indices": [
                            37,
                            60
                        ],
                        "url": "https://t.co/aFrH6YpHt8"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Arsenal FC News",
                        "indices": [
                            3,
                            16
                        ],
                        "id": 794533892778815488,
                        "screen_name": "ArsenalFC_fl",
                        "id_str": "794533892778815488"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "quoted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 12:43:21 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 1,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221050927181959169",
                "in_reply_to_user_id": null,
                "favorite_count": 0,
                "id": 1221050927181959169,
                "text": "So proud of ⁦@GiovanniLugo7⁩ #hbcupride #hbcu #football #nfl https://t.co/vxCHVjOcfv",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 1,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.savannahnow.com/sports/20200123/savannah-statersquos-lugo-earns-bowl-game-honor",
                            "display_url": "savannahnow.com/sports/2020012…",
                            "indices": [
                                61,
                                84
                            ],
                            "url": "https://t.co/vxCHVjOcfv"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                29,
                                39
                            ],
                            "text": "hbcupride"
                        },
                        {
                            "indices": [
                                40,
                                45
                            ],
                            "text": "hbcu"
                        },
                        {
                            "indices": [
                                46,
                                55
                            ],
                            "text": "football"
                        },
                        {
                            "indices": [
                                56,
                                60
                            ],
                            "text": "nfl"
                        }
                    ],
                    "user_mentions": [
                        {
                            "name": "Giovanni Lugo",
                            "indices": [
                                13,
                                27
                            ],
                            "id": 2884062636,
                            "screen_name": "GiovanniLugo7",
                            "id_str": "2884062636"
                        }
                    ],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 762,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1219251864128147457/nikqs7OQ_normal.jpg",
                    "listed_count": 19,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme9/bg.gif",
                    "default_profile_image": false,
                    "favourites_count": 437,
                    "description": "Creative visualizer, positive thinker, communications professional who always tries to see the good in people, and a runner.",
                    "created_at": "Tue Mar 31 16:32:12 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme9/bg.gif",
                    "protected": false,
                    "screen_name": "TreeMcDougal",
                    "id_str": "27905490",
                    "profile_link_color": "2FC2EF",
                    "translator_type": "none",
                    "id": 27905490,
                    "geo_enabled": true,
                    "profile_background_color": "121314",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "666666",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1219251864128147457/nikqs7OQ_normal.jpg",
                    "time_zone": null,
                    "url": "http://www.linkedin.com/in/annetteogletreemcdougal",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/27905490/1577471183",
                    "statuses_count": 1175,
                    "follow_request_sent": null,
                    "followers_count": 455,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "A. Ogletree-McDougal",
                    "location": "Savannah, GA",
                    "profile_sidebar_fill_color": "252429",
                    "notifications": null
                }
            },
            "is_quote_status": true,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 686,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1215862988617416704/Xq1MBT4k_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 731,
                "description": "DE @SavannahStateUniversity 🐅Trenches 🤕🏈 LLBugDaPluG🕊🙏🏾🔌‼️ #478🏚 to #912🏝 Gods Angel 👼🏾‼️InDaNameOfGee🦍🕊 TBG🦍‼️",
                "created_at": "Wed Apr 26 16:16:51 +0000 2017",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "JeremyDenson5",
                "id_str": "857267236301615105",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 857267236301615105,
                "geo_enabled": true,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1215862988617416704/Xq1MBT4k_normal.jpg",
                "time_zone": null,
                "url": "https://www.hudl.com/profile/8723574/Jeremy-Denson/videos",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/857267236301615105/1576739562",
                "statuses_count": 631,
                "follow_request_sent": null,
                "followers_count": 572,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "The 1AndOnlyJD🤤🦍‼️",
                "location": "Georgia",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102094695923712",
            "reply_count": 0,
            "quoted_status_id": 1221050927181959169,
            "quoted_status_id_str": "1221050927181959169",
            "id": 1221102094695923712,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:41 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "Congratulations bro 😈‼️ One of the most talented teammates we had Qb/Punter/kicker all around athlete @GiovanniLugo7",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968401012",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Giovanni Lugo",
                        "indices": [
                            102,
                            116
                        ],
                        "id": 2884062636,
                        "screen_name": "GiovanniLugo7",
                        "id_str": "2884062636"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/c3cr39gQyQ",
                "expanded": "https://twitter.com/treemcdougal/status/1221050927181959169",
                "display": "twitter.com/treemcdougal/s…"
            },
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 278,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220410749606146050/QmNMF2_Z_normal.jpg",
                "listed_count": 14,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 20229,
                "description": "SC: itsbodee • GU ‘22 • Psalm 51:1-19 🇳🇬",
                "created_at": "Mon Mar 17 23:39:15 +0000 2014",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "itsBode_",
                "id_str": "2395279820",
                "profile_link_color": "E09616",
                "translator_type": "none",
                "id": 2395279820,
                "geo_enabled": true,
                "profile_background_color": "090A0A",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1220410749606146050/QmNMF2_Z_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2395279820/1560457923",
                "statuses_count": 27754,
                "follow_request_sent": null,
                "followers_count": 355,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "IT'S L🕯T 🥇🤫",
                "location": "Laurel, MD",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102165634244610",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 01:17:40 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 18,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220878369518182401",
                "in_reply_to_user_id": null,
                "favorite_count": 86,
                "id": 1220878369518182401,
                "text": "guys watch football, but won’t let me put my foot on they balls 😐",
                "place": null,
                "lang": "en",
                "quote_count": 2,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 13,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 819,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1220395901581242369/oBAzSr2W_normal.jpg",
                    "listed_count": 2,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 5068,
                    "description": "single mom with no kids",
                    "created_at": "Fri Apr 27 13:47:51 +0000 2018",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "natatemyrat",
                    "id_str": "989863700403236865",
                    "profile_link_color": "FAB81E",
                    "translator_type": "none",
                    "id": 989863700403236865,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "000000",
                    "profile_text_color": "000000",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1220395901581242369/oBAzSr2W_normal.jpg",
                    "time_zone": null,
                    "url": "https://instagram.com/sayjinkiesalready?igshid=cbnbs6xdb71g",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/989863700403236865/1579732364",
                    "statuses_count": 2600,
                    "follow_request_sent": null,
                    "followers_count": 882,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "nat♡",
                    "location": "playpen",
                    "profile_sidebar_fill_color": "000000",
                    "notifications": null
                }
            },
            "id": 1221102165634244610,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:06:57 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @natatemyrat: guys watch football, but won’t let me put my foot on they balls 😐",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968417925",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "nat♡",
                        "indices": [
                            3,
                            15
                        ],
                        "id": 989863700403236865,
                        "screen_name": "natatemyrat",
                        "id_str": "989863700403236865"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 702,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1194390230029258757/N_yl9p08_normal.jpg",
                "listed_count": 48,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 4173,
                "description": "Official twitter of Barking Football Club established 1880 who play at Mayesbrook Park. Members of the Bet Victor I Isthmian League South Central. #WEAREBARKING",
                "created_at": "Sat Apr 25 10:21:23 +0000 2009",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "barkingfc",
                "id_str": "35187126",
                "profile_link_color": "000CB4",
                "translator_type": "none",
                "id": 35187126,
                "geo_enabled": true,
                "profile_background_color": "9AE4E8",
                "lang": null,
                "profile_sidebar_border_color": "BDDCAD",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1194390230029258757/N_yl9p08_normal.jpg",
                "time_zone": null,
                "url": "http://www.barking-fc.co.uk",
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/35187126/1579681012",
                "statuses_count": 10121,
                "follow_request_sent": null,
                "followers_count": 5025,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Barking FC",
                "location": "Barking",
                "profile_sidebar_fill_color": "DDFFCC",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102588600504321",
            "reply_count": 0,
            "display_text_range": [
                0,
                83
            ],
            "id": 1221102588600504321,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:38 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://www.footballwebpages.co.uk\" rel=\"nofollow\">Football Web Pages</a>",
            "text": "KICK-OFF (SECOND-HALF): Westfield v Barking #IsthmianLeague https://t.co/aUg8t4hT7y https://t.co/KVpm9IB0as",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968518768",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.footballwebpages.co.uk/match/2019-2020/isthmian-football-league-south-central-division/westfield/barking/144849",
                        "display_url": "footballwebpages.co.uk/match/2019-202…",
                        "indices": [
                            60,
                            83
                        ],
                        "url": "https://t.co/aUg8t4hT7y"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/KVpm9IB0as",
                        "indices": [
                            84,
                            107
                        ],
                        "sizes": {
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 1280
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221102586557816833",
                        "expanded_url": "https://twitter.com/barkingfc/status/1221102588600504321/photo/1",
                        "media_url_https": "https://pbs.twimg.com/media/EPI6VTIW4AElp1Q.jpg",
                        "id": 1221102586557816833,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI6VTIW4AElp1Q.jpg",
                        "url": "https://t.co/KVpm9IB0as"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            44,
                            59
                        ],
                        "text": "IsthmianLeague"
                    }
                ],
                "user_mentions": [],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/KVpm9IB0as",
                        "indices": [
                            84,
                            107
                        ],
                        "sizes": {
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 1280
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221102586557816833",
                        "expanded_url": "https://twitter.com/barkingfc/status/1221102588600504321/photo/1",
                        "media_url_https": "https://pbs.twimg.com/media/EPI6VTIW4AElp1Q.jpg",
                        "id": 1221102586557816833,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI6VTIW4AElp1Q.jpg",
                        "url": "https://t.co/KVpm9IB0as"
                    }
                ]
            },
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        },
        {
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 1215,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1219094906716721153/diZRsmVk_normal.jpg",
                "listed_count": 302,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 36403,
                "description": "Work @TCS. Proud to be in @TataCompanies. Alumnus of http://www.rkmcnarendrapur.org & http://www.iiests.ac.in Lived @ 🇮🇳🇬🇧🇿🇦🇸🇬🇨🇳Views are personal.",
                "created_at": "Sat Mar 19 11:46:44 +0000 2011",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "BanerjiSougata",
                "id_str": "268752244",
                "profile_link_color": "DD2E44",
                "translator_type": "none",
                "id": 268752244,
                "geo_enabled": true,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1219094906716721153/diZRsmVk_normal.jpg",
                "time_zone": null,
                "url": "https://www.facebook.com/Banerji.Sougata?fref=ts",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/268752244/1558398785",
                "statuses_count": 47072,
                "follow_request_sent": null,
                "followers_count": 1051,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "Sougata Banerji",
                "location": "Edison, New Jersey",
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221101894153707521",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        252
                    ],
                    "extended_entities": {
                        "media": [
                            {
                                "display_url": "pic.twitter.com/wLHw9MHzpi",
                                "indices": [
                                    253,
                                    276
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 680,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 1080,
                                        "resize": "fit",
                                        "w": 1080
                                    },
                                    "large": {
                                        "h": 1080,
                                        "resize": "fit",
                                        "w": 1080
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220937986553958400",
                                "expanded_url": "https://twitter.com/SVFsocial/status/1220937996712546304/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPGkoUVUUAAco9L.jpg",
                                "id": 1220937986553958400,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPGkoUVUUAAco9L.jpg",
                                "url": "https://t.co/wLHw9MHzpi"
                            }
                        ]
                    },
                    "entities": {
                        "urls": [],
                        "media": [
                            {
                                "display_url": "pic.twitter.com/wLHw9MHzpi",
                                "indices": [
                                    253,
                                    276
                                ],
                                "sizes": {
                                    "small": {
                                        "h": 680,
                                        "resize": "fit",
                                        "w": 680
                                    },
                                    "medium": {
                                        "h": 1080,
                                        "resize": "fit",
                                        "w": 1080
                                    },
                                    "large": {
                                        "h": 1080,
                                        "resize": "fit",
                                        "w": 1080
                                    },
                                    "thumb": {
                                        "h": 150,
                                        "resize": "crop",
                                        "w": 150
                                    }
                                },
                                "id_str": "1220937986553958400",
                                "expanded_url": "https://twitter.com/SVFsocial/status/1220937996712546304/photo/1",
                                "media_url_https": "https://pbs.twimg.com/media/EPGkoUVUUAAco9L.jpg",
                                "id": 1220937986553958400,
                                "type": "photo",
                                "media_url": "http://pbs.twimg.com/media/EPGkoUVUUAAco9L.jpg",
                                "url": "https://t.co/wLHw9MHzpi"
                            }
                        ],
                        "hashtags": [
                            {
                                "indices": [
                                    62,
                                    72
                                ],
                                "text": "Golondaaj"
                            }
                        ],
                        "user_mentions": [
                            {
                                "name": "dhrubo banerjee",
                                "indices": [
                                    188,
                                    204
                                ],
                                "id": 942268189718740992,
                                "screen_name": "dhrubo_banerjee",
                                "id_str": "942268189718740992"
                            },
                            {
                                "name": "Dev",
                                "indices": [
                                    207,
                                    220
                                ],
                                "id": 138077726,
                                "screen_name": "idevadhikari",
                                "id_str": "138077726"
                            },
                            {
                                "name": "Ishaa",
                                "indices": [
                                    221,
                                    229
                                ],
                                "id": 606956447,
                                "screen_name": "m_ishaa",
                                "id_str": "606956447"
                            },
                            {
                                "name": "indrasish roy",
                                "indices": [
                                    230,
                                    243
                                ],
                                "id": 186759584,
                                "screen_name": "indrasishroy",
                                "id_str": "186759584"
                            },
                            {
                                "name": "John Bhattacharyya",
                                "indices": [
                                    244,
                                    252
                                ],
                                "id": 354691476,
                                "screen_name": "Shaurja",
                                "id_str": "354691476"
                            }
                        ],
                        "symbols": []
                    },
                    "full_text": "ভারতীয় ফুটবলের জনক নগেন্দ্রপ্রসাদ সর্বাধিকারীর জীবন অবলম্বনে #Golondaaj...\n\nHere's the star-studded cast list of the most intriguing football drama the country has ever seen, directed by @dhrubo_banerjee.\n\n@idevadhikari @m_ishaa @indrasishroy @Shaurja https://t.co/wLHw9MHzpi"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 05:14:37 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                "retweet_count": 95,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220937996712546304",
                "in_reply_to_user_id": null,
                "favorite_count": 486,
                "id": 1220937996712546304,
                "text": "ভারতীয় ফুটবলের জনক নগেন্দ্রপ্রসাদ সর্বাধিকারীর জীবন অবলম্বনে #Golondaaj...\n\nHere's the star-studded cast list of t… https://t.co/TuLpHELb1x",
                "place": null,
                "lang": "en",
                "quote_count": 19,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": true,
                "reply_count": 25,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://twitter.com/i/web/status/1220937996712546304",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/TuLpHELb1x"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                62,
                                72
                            ],
                            "text": "Golondaaj"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    140
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 281,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/837857919261638658/U49tD8qd_normal.jpg",
                    "listed_count": 179,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 14372,
                    "description": "Films | Television | Music | New Media | Exhibition. We do it all. We are Bengal’s leading Media & Entertainment house.",
                    "created_at": "Sat Nov 29 02:06:57 +0000 2008",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "SVFsocial",
                    "id_str": "17725688",
                    "profile_link_color": "0084B4",
                    "translator_type": "none",
                    "id": 17725688,
                    "geo_enabled": true,
                    "profile_background_color": "000000",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": true,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/837857919261638658/U49tD8qd_normal.jpg",
                    "time_zone": null,
                    "url": "http://bit.ly/DwitiyoPurush_bms",
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/17725688/1579873988",
                    "statuses_count": 37807,
                    "follow_request_sent": null,
                    "followers_count": 508058,
                    "profile_use_background_image": false,
                    "default_profile": false,
                    "following": null,
                    "name": "SVF",
                    "location": "Kolkata",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221101894153707521,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:05:53 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @SVFsocial: ভারতীয় ফুটবলের জনক নগেন্দ্রপ্রসাদ সর্বাধিকারীর জীবন অবলম্বনে #Golondaaj...\n\nHere's the star-studded cast list of the most i…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968353199",
            "entities": {
                "urls": [],
                "hashtags": [
                    {
                        "indices": [
                            77,
                            87
                        ],
                        "text": "Golondaaj"
                    }
                ],
                "user_mentions": [
                    {
                        "name": "SVF",
                        "indices": [
                            3,
                            13
                        ],
                        "id": 17725688,
                        "screen_name": "SVFsocial",
                        "id_str": "17725688"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "favorite_count": 0,
            "contributors": null
        }
    ]
}
```

##### GET Country Metrics from Cloudwatch
```
GET /metrics?country=Canada&period=3000&start_time=2020-01-24T12:00:00&end_time=2020-01-26T23:00:00
```

##### Sample Response
```
{
    "Label": "NumberOfTweets",
    "Datapoints": [
        {
            "Timestamp": "2020-01-25 13:50:00+00:00",
            "Sum": 19.0,
            "Unit": "None"
        },
        {
            "Timestamp": "2020-01-25 13:00:00+00:00",
            "Sum": 47.0,
            "Unit": "None"
        },
        {
            "Timestamp": "2020-01-25 15:30:00+00:00",
            "Sum": 461.0,
            "Unit": "None"
        },
        {
            "Timestamp": "2020-01-25 14:40:00+00:00",
            "Sum": 136.0,
            "Unit": "None"
        }
    ]
}
```



