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
            "is_quote_status": false,
            "favorited": false,
            "user": {
                "utc_offset": null,
                "friends_count": 45,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/704083351334952960/pPhcLlhw_normal.jpg",
                "listed_count": 4,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 1067,
                "description": "Color anaylst for ODU football, play by play for ODU baseball, and anything else the Monarchs may need along the way.",
                "created_at": "Mon Sep 28 20:25:59 +0000 2015",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "AndyMashawODU",
                "id_str": "3807207255",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 3807207255,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/704083351334952960/pPhcLlhw_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/3807207255/1444656350",
                "statuses_count": 1032,
                "follow_request_sent": null,
                "followers_count": 299,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Andy Mashaw",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102826304262144",
            "reply_count": 0,
            "retweeted_status": {
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Fri Jan 24 16:38:36 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 8,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1220747742496141313",
                "in_reply_to_user_id": null,
                "favorite_count": 29,
                "id": 1220747742496141313,
                "text": "#odu football will kick off Rahne era under Friday Night lights. https://t.co/siLukg9TC1",
                "place": null,
                "lang": "en",
                "quote_count": 1,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.pilotonline.com/sports/vp-sp-odu-football-schedule-opener-20200124-ukc6uvklbjdepj3ci2i2iwwnmm-story.html",
                            "display_url": "pilotonline.com/sports/vp-sp-o…",
                            "indices": [
                                65,
                                88
                            ],
                            "url": "https://t.co/siLukg9TC1"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                0,
                                4
                            ],
                            "text": "odu"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 752,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1207871397055221761/l_RJ3PC__normal.jpg",
                    "listed_count": 93,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 986,
                    "description": "Virginian-Pilot sports writer contributing to your information overload since last century, now at the speed of twitter",
                    "created_at": "Mon Jun 29 18:33:24 +0000 2009",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "edmillervp",
                    "id_str": "52142720",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 52142720,
                    "geo_enabled": false,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1207871397055221761/l_RJ3PC__normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "statuses_count": 13002,
                    "follow_request_sent": null,
                    "followers_count": 2379,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Ed Miller",
                    "location": "Norfolk, Va",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102826304262144,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:35 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @edmillervp: #odu football will kick off Rahne era under Friday Night lights. https://t.co/siLukg9TC1",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968575441",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.pilotonline.com/sports/vp-sp-odu-football-schedule-opener-20200124-ukc6uvklbjdepj3ci2i2iwwnmm-story.html",
                        "display_url": "pilotonline.com/sports/vp-sp-o…",
                        "indices": [
                            81,
                            104
                        ],
                        "url": "https://t.co/siLukg9TC1"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            16,
                            20
                        ],
                        "text": "odu"
                    }
                ],
                "user_mentions": [
                    {
                        "name": "Ed Miller",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 52142720,
                        "screen_name": "edmillervp",
                        "id_str": "52142720"
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
                "friends_count": 887,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/747883038806269953/s3vIVaR2_normal.jpg",
                "listed_count": 39,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 503,
                "description": "Leicester City correspondent for @LiveLCFC",
                "created_at": "Thu Dec 02 14:48:08 +0000 2010",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "JrdnBlackwell",
                "id_str": "222125278",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 222125278,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/747883038806269953/s3vIVaR2_normal.jpg",
                "time_zone": null,
                "url": "https://www.leicestermercury.co.uk/authors/jordan-blackwell/",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/222125278/1574678694",
                "statuses_count": 5597,
                "follow_request_sent": null,
                "followers_count": 1715,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Jordan Blackwell",
                "location": "Leicester, UK",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102635345903622",
            "reply_count": 0,
            "id": 1221102635345903622,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:08:49 +0000 2020",
            "quote_count": 0,
            "extended_tweet": {
                "display_text_range": [
                    0,
                    240
                ],
                "entities": {
                    "urls": [
                        {
                            "expanded_url": "https://www.leicestermercury.co.uk/sport/football/football-news/invaluable-leicester-city-player-ratings-3777672",
                            "display_url": "leicestermercury.co.uk/sport/football…",
                            "indices": [
                                217,
                                240
                            ],
                            "url": "https://t.co/ZRkAH2FwJs"
                        }
                    ],
                    "hashtags": [
                        {
                            "indices": [
                                32,
                                37
                            ],
                            "text": "LCFC"
                        }
                    ],
                    "user_mentions": [],
                    "symbols": []
                },
                "full_text": "Fuchs scores highly as the only #LCFC player who was as good in the second half as they were in the first, while I thought Praet was great too (and cor blimey, that pass).\n\nGray and Perez not up to scratch.\n\nRatings: https://t.co/ZRkAH2FwJs"
            },
            "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
            "text": "Fuchs scores highly as the only #LCFC player who was as good in the second half as they were in the first, while I… https://t.co/8Sj9H9z2N9",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968529913",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://twitter.com/i/web/status/1221102635345903622",
                        "display_url": "twitter.com/i/web/status/1…",
                        "indices": [
                            116,
                            139
                        ],
                        "url": "https://t.co/8Sj9H9z2N9"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            32,
                            37
                        ],
                        "text": "LCFC"
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
                "friends_count": 13,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1205967438141120517/kcnDXmBu_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 104,
                "description": "Mon i hoop's 🇳🇬🍀💚🇳🇬\nMon i Moray\ngirls blue FC ⚽",
                "created_at": "Thu Nov 14 18:56:05 +0000 2019",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "GrahamMilne19",
                "id_str": "1195052666365382657",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1195052666365382657,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1205967438141120517/kcnDXmBu_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "statuses_count": 40,
                "follow_request_sent": null,
                "followers_count": 3,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "Graham Milne",
                "location": "New Elgin",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102389387767810",
            "reply_count": 0,
            "retweeted_status": {
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/X85QzWsOMF",
                            "indices": [
                                82,
                                105
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
                                    "h": 1200,
                                    "resize": "fit",
                                    "w": 1600
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221101978564075521",
                            "expanded_url": "https://twitter.com/MorayClub/status/1221101986126422016/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI5x6LWoAENHTO.jpg",
                            "id": 1221101978564075521,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI5x6LWoAENHTO.jpg",
                            "url": "https://t.co/X85QzWsOMF"
                        }
                    ]
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:06:15 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
                "retweet_count": 1,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221101986126422016",
                "in_reply_to_user_id": null,
                "favorite_count": 1,
                "id": 1221101986126422016,
                "text": "Moray Girls U13’s Football Festival\n#moraygirls#2020team#girlswholovefootball ⚽️💙 https://t.co/X85QzWsOMF",
                "place": null,
                "lang": "en",
                "quote_count": 0,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 0,
                "entities": {
                    "urls": [],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/X85QzWsOMF",
                            "indices": [
                                82,
                                105
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
                                    "h": 1200,
                                    "resize": "fit",
                                    "w": 1600
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "id_str": "1221101978564075521",
                            "expanded_url": "https://twitter.com/MorayClub/status/1221101986126422016/photo/1",
                            "media_url_https": "https://pbs.twimg.com/media/EPI5x6LWoAENHTO.jpg",
                            "id": 1221101978564075521,
                            "type": "photo",
                            "media_url": "http://pbs.twimg.com/media/EPI5x6LWoAENHTO.jpg",
                            "url": "https://t.co/X85QzWsOMF"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "display_text_range": [
                    0,
                    81
                ],
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 191,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1194390380025909250/mFjlQwz6_normal.jpg",
                    "listed_count": 0,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 10,
                    "description": "Moray Girls FC established in 2009. With U13’s and U16’s teams playing in the north regional http://leagues.Training based in Elgin,Moray.All players welcome",
                    "created_at": "Tue Nov 12 23:03:05 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "MorayClub",
                    "id_str": "1194390134252359681",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1194390134252359681,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1194390380025909250/mFjlQwz6_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1194390134252359681/1573600458",
                    "statuses_count": 13,
                    "follow_request_sent": null,
                    "followers_count": 68,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Moray Girls Football Club",
                    "location": "Elgin, Scotland",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102389387767810,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:51 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
            "text": "RT @MorayClub: Moray Girls U13’s Football Festival\n#moraygirls#2020team#girlswholovefootball ⚽️💙 https://t.co/X85QzWsOMF",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968471272",
            "possibly_sensitive": false,
            "entities": {
                "urls": [],
                "media": [
                    {
                        "display_url": "pic.twitter.com/X85QzWsOMF",
                        "source_user_id": 1194390134252359681,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI5x6LWoAENHTO.jpg",
                        "source_status_id": 1221101986126422016,
                        "url": "https://t.co/X85QzWsOMF",
                        "indices": [
                            97,
                            120
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
                                "h": 1200,
                                "resize": "fit",
                                "w": 1600
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221101978564075521",
                        "expanded_url": "https://twitter.com/MorayClub/status/1221101986126422016/photo/1",
                        "source_status_id_str": "1221101986126422016",
                        "media_url_https": "https://pbs.twimg.com/media/EPI5x6LWoAENHTO.jpg",
                        "id": 1221101978564075521,
                        "source_user_id_str": "1194390134252359681"
                    }
                ],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Moray Girls Football Club",
                        "indices": [
                            3,
                            13
                        ],
                        "id": 1194390134252359681,
                        "screen_name": "MorayClub",
                        "id_str": "1194390134252359681"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/X85QzWsOMF",
                        "source_user_id": 1194390134252359681,
                        "type": "photo",
                        "media_url": "http://pbs.twimg.com/media/EPI5x6LWoAENHTO.jpg",
                        "source_status_id": 1221101986126422016,
                        "url": "https://t.co/X85QzWsOMF",
                        "indices": [
                            97,
                            120
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
                                "h": 1200,
                                "resize": "fit",
                                "w": 1600
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "id_str": "1221101978564075521",
                        "expanded_url": "https://twitter.com/MorayClub/status/1221101986126422016/photo/1",
                        "source_status_id_str": "1221101986126422016",
                        "media_url_https": "https://pbs.twimg.com/media/EPI5x6LWoAENHTO.jpg",
                        "id": 1221101978564075521,
                        "source_user_id_str": "1194390134252359681"
                    }
                ]
            },
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
                "favorite_count": 13500,
                "id": 1220738552834809861,
                "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                "place": null,
                "lang": "en",
                "quote_count": 1429,
                "favorited": false,
                "possibly_sensitive": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 547,
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
                "friends_count": 200,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1100028014556037125/OzoH5oJ6_normal.jpg",
                "listed_count": 4,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 4727,
                "description": "Benfica / Porto city",
                "created_at": "Mon Dec 09 22:52:49 +0000 2013",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Miguelpedro009",
                "id_str": "2238264619",
                "profile_link_color": "0084B4",
                "translator_type": "none",
                "id": 2238264619,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "FFFFFF",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1100028014556037125/OzoH5oJ6_normal.jpg",
                "time_zone": null,
                "url": "http://www.instagram.com/miguelpedro007/",
                "contributors_enabled": false,
                "profile_background_tile": true,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2238264619/1446754629",
                "statuses_count": 18033,
                "follow_request_sent": null,
                "followers_count": 254,
                "profile_use_background_image": true,
                "default_profile": false,
                "following": null,
                "name": "Vilaça",
                "location": null,
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102383792578562",
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
                    "favorite_count": 13500,
                    "id": 1220738552834809861,
                    "text": "What. A. Summer. \n\nWhen football very, very nearly came home. 😓🏴󠁧󠁢󠁥󠁮󠁧󠁿 https://t.co/EbXuum8Xu7",
                    "place": null,
                    "lang": "en",
                    "quote_count": 1429,
                    "favorited": false,
                    "possibly_sensitive": false,
                    "coordinates": null,
                    "truncated": false,
                    "reply_count": 547,
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
                "retweet_count": 3218,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1220754234326638593",
                "in_reply_to_user_id": null,
                "favorite_count": 21746,
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
            "id": 1221102383792578562,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:07:49 +0000 2020",
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
            "timestamp_ms": "1579968469938",
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
                "friends_count": 9561,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/839982412461424640/E2TfJroH_normal.jpg",
                "listed_count": 4,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 131891,
                "description": "I wish common sense was more common. 🇺🇸#MAGA #TRUMP2020 NO LISTS! List=Instant Block ! #BackTheBlue #USA #Veterans #AnimalRescue #DogsRule",
                "created_at": "Thu Feb 09 23:53:43 +0000 2017",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Trippledogdare3",
                "id_str": "829840734173982720",
                "profile_link_color": "1B95E0",
                "translator_type": "none",
                "id": 829840734173982720,
                "geo_enabled": false,
                "profile_background_color": "000000",
                "lang": null,
                "profile_sidebar_border_color": "000000",
                "profile_text_color": "000000",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/839982412461424640/E2TfJroH_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/829840734173982720/1572659585",
                "statuses_count": 94083,
                "follow_request_sent": null,
                "followers_count": 9403,
                "profile_use_background_image": false,
                "default_profile": false,
                "following": null,
                "name": "littlebigpaws #Nationalist",
                "location": "State of Euphoria since Nov 8 2016",
                "profile_sidebar_fill_color": "000000",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102828913156096",
            "reply_count": 0,
            "retweeted_status": {
                "extended_tweet": {
                    "display_text_range": [
                        0,
                        191
                    ],
                    "entities": {
                        "urls": [],
                        "hashtags": [],
                        "user_mentions": [],
                        "symbols": []
                    },
                    "full_text": "LOL - I hope they continue to just use the democrats own words against them 😂\n\nIt's so easy...\n\nThis is what happens when a 6th grade football team, the B team, plays the Kansas City Chiefs 🤣"
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 16:01:46 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "retweet_count": 26,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": false,
                "id_str": "1221100858613665792",
                "in_reply_to_user_id": null,
                "favorite_count": 52,
                "id": 1221100858613665792,
                "text": "LOL - I hope they continue to just use the democrats own words against them 😂\n\nIt's so easy...\n\nThis is what happen… https://t.co/T8du9NdFSU",
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
                            "expanded_url": "https://twitter.com/i/web/status/1221100858613665792",
                            "display_url": "twitter.com/i/web/status/1…",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/T8du9NdFSU"
                        }
                    ],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 16876,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1191367126470287361/F86Xor9U_normal.jpg",
                    "listed_count": 27,
                    "profile_background_image_url": null,
                    "default_profile_image": false,
                    "favourites_count": 33346,
                    "description": "🇺🇸 PROUD American 🇺🇸 Brain Aneurysm Survivor 🧠🙏 Common Sense Enthusiast 🧐 Political Loud Mouth 😜 110% TRUMP 🇺🇸 SUPER ELITE #Cult45",
                    "created_at": "Mon Nov 04 14:39:33 +0000 2019",
                    "is_translator": false,
                    "profile_background_image_url_https": null,
                    "protected": false,
                    "screen_name": "MrJones_tm",
                    "id_str": "1191364337631465474",
                    "profile_link_color": "1DA1F2",
                    "translator_type": "none",
                    "id": 1191364337631465474,
                    "geo_enabled": false,
                    "profile_background_color": "F5F8FA",
                    "lang": null,
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1191367126470287361/F86Xor9U_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1191364337631465474/1572879033",
                    "statuses_count": 11344,
                    "follow_request_sent": null,
                    "followers_count": 28685,
                    "profile_use_background_image": true,
                    "default_profile": true,
                    "following": null,
                    "name": "Mr. Jones™️🇺🇸",
                    "location": null,
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "id": 1221102828913156096,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:36 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @MrJones_tm: LOL - I hope they continue to just use the democrats own words against them 😂\n\nIt's so easy...\n\nThis is what happens when a…",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968576063",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Mr. Jones™️🇺🇸",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 1191364337631465474,
                        "screen_name": "MrJones_tm",
                        "id_str": "1191364337631465474"
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
                "friends_count": 4851,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1055862232997867520/rnD_hXhn_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": null,
                "default_profile_image": false,
                "favourites_count": 15165,
                "description": "A new #PremierLeague #EPL community with less noise & junk on @plowio. Follow for an invite to join our open beta!",
                "created_at": "Sun Oct 21 17:51:40 +0000 2018",
                "is_translator": false,
                "profile_background_image_url_https": null,
                "protected": false,
                "screen_name": "EnglishPre_Plow",
                "id_str": "1054067708994744320",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 1054067708994744320,
                "geo_enabled": false,
                "profile_background_color": "F5F8FA",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1055862232997867520/rnD_hXhn_normal.jpg",
                "time_zone": null,
                "url": "https://www.plow.io/anchor/English_Premier_League",
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1054067708994744320/1540572171",
                "statuses_count": 22193,
                "follow_request_sent": null,
                "followers_count": 2031,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "English Premier League Plow",
                "location": "Internet",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102825645559813",
            "reply_count": 0,
            "id": 1221102825645559813,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:35 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"https://www.plow.io/anchor/English_Premier_League\" rel=\"nofollow\">EnglishPre_Plow</a>",
            "text": "Leicester City vs. West Ham United - Football Match Report - January 22, 2020...\nhttps://t.co/lfcnacZaGj\n+1 FootyBot #EPL #premierleague",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "en",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968575284",
            "possibly_sensitive": false,
            "entities": {
                "urls": [
                    {
                        "expanded_url": "https://www.plow.io/post/leicester-city-vs-west-ham-united---football-match-report---january-22-2020---espn?utm_source=Twitter&utm_campaign=English_Premier_League",
                        "display_url": "plow.io/post/leicester…",
                        "indices": [
                            81,
                            104
                        ],
                        "url": "https://t.co/lfcnacZaGj"
                    }
                ],
                "hashtags": [
                    {
                        "indices": [
                            117,
                            121
                        ],
                        "text": "EPL"
                    },
                    {
                        "indices": [
                            122,
                            136
                        ],
                        "text": "premierleague"
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
                    "followers_count": 10301,
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
                "friends_count": 567,
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/1213195362976063494/aE-OEfM2_normal.jpg",
                "listed_count": 0,
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "default_profile_image": false,
                "favourites_count": 31927,
                "description": "Man City",
                "created_at": "Sun Nov 11 22:13:56 +0000 2012",
                "is_translator": false,
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                "protected": false,
                "screen_name": "Olliewebster123",
                "id_str": "942345764",
                "profile_link_color": "1DA1F2",
                "translator_type": "none",
                "id": 942345764,
                "geo_enabled": false,
                "profile_background_color": "C0DEED",
                "lang": null,
                "profile_sidebar_border_color": "C0DEED",
                "profile_text_color": "333333",
                "verified": false,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1213195362976063494/aE-OEfM2_normal.jpg",
                "time_zone": null,
                "url": null,
                "contributors_enabled": false,
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/942345764/1571607005",
                "statuses_count": 1722,
                "follow_request_sent": null,
                "followers_count": 233,
                "profile_use_background_image": true,
                "default_profile": true,
                "following": null,
                "name": "OliverWebster",
                "location": "Manchester, England",
                "profile_sidebar_fill_color": "DDEEF6",
                "notifications": null
            },
            "filter_level": "low",
            "id_str": "1221102686541615105",
            "reply_count": 0,
            "quoted_status_id": 1220620194286129152,
            "retweeted_status": {
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
                        "followers_count": 10301,
                        "profile_use_background_image": false,
                        "default_profile": false,
                        "following": null,
                        "name": "Second Tier Podcast",
                        "location": null,
                        "profile_sidebar_fill_color": "000000",
                        "notifications": null
                    }
                },
                "in_reply_to_status_id_str": null,
                "in_reply_to_status_id": null,
                "created_at": "Sat Jan 25 08:51:15 +0000 2020",
                "in_reply_to_user_id_str": null,
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "quoted_status_id": 1220620194286129152,
                "retweet_count": 68,
                "retweeted": false,
                "geo": null,
                "filter_level": "low",
                "in_reply_to_screen_name": null,
                "is_quote_status": true,
                "id_str": "1220992515324743682",
                "in_reply_to_user_id": null,
                "favorite_count": 703,
                "id": 1220992515324743682,
                "text": "Sam Quek",
                "place": null,
                "quoted_status_permalink": {
                    "url": "https://t.co/rd0TvHc6wN",
                    "expanded": "https://twitter.com/TheSecondTier/status/1220620194286129152",
                    "display": "twitter.com/TheSecondTier/…"
                },
                "lang": "in",
                "quote_count": 7,
                "favorited": false,
                "coordinates": null,
                "truncated": false,
                "reply_count": 12,
                "entities": {
                    "urls": [],
                    "hashtags": [],
                    "user_mentions": [],
                    "symbols": []
                },
                "quoted_status_id_str": "1220620194286129152",
                "contributors": null,
                "user": {
                    "utc_offset": null,
                    "friends_count": 1337,
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1208727041987747841/ZDP0JUb-_normal.jpg",
                    "listed_count": 23,
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "default_profile_image": false,
                    "favourites_count": 8553,
                    "description": "Evertonian, Celtic, New England Patriots, horse racing, Celtics",
                    "created_at": "Tue Dec 07 15:19:42 +0000 2010",
                    "is_translator": false,
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "protected": false,
                    "screen_name": "Macca26efc",
                    "id_str": "223871403",
                    "profile_link_color": "0084B4",
                    "translator_type": "none",
                    "id": 223871403,
                    "geo_enabled": false,
                    "profile_background_color": "C0DEED",
                    "lang": null,
                    "profile_sidebar_border_color": "FFFFFF",
                    "profile_text_color": "333333",
                    "verified": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/1208727041987747841/ZDP0JUb-_normal.jpg",
                    "time_zone": null,
                    "url": null,
                    "contributors_enabled": false,
                    "profile_background_tile": true,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/223871403/1568158494",
                    "statuses_count": 35052,
                    "follow_request_sent": null,
                    "followers_count": 1495,
                    "profile_use_background_image": true,
                    "default_profile": false,
                    "following": null,
                    "name": "Macca",
                    "location": "Liverpool, England",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "notifications": null
                }
            },
            "quoted_status_id_str": "1220620194286129152",
            "id": 1221102686541615105,
            "in_reply_to_user_id": null,
            "coordinates": null,
            "retweeted": false,
            "created_at": "Sat Jan 25 16:09:02 +0000 2020",
            "quote_count": 0,
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @Macca26efc: Sam Quek",
            "in_reply_to_user_id_str": null,
            "in_reply_to_status_id": null,
            "lang": "in",
            "geo": null,
            "retweet_count": 0,
            "in_reply_to_screen_name": null,
            "place": null,
            "timestamp_ms": "1579968542119",
            "entities": {
                "urls": [],
                "hashtags": [],
                "user_mentions": [
                    {
                        "name": "Macca",
                        "indices": [
                            3,
                            14
                        ],
                        "id": 223871403,
                        "screen_name": "Macca26efc",
                        "id_str": "223871403"
                    }
                ],
                "symbols": []
            },
            "truncated": false,
            "in_reply_to_status_id_str": null,
            "quoted_status_permalink": {
                "url": "https://t.co/rd0TvHc6wN",
                "expanded": "https://twitter.com/TheSecondTier/status/1220620194286129152",
                "display": "twitter.com/TheSecondTier/…"
            },
            "favorite_count": 0,
            "contributors": null
        }
    ]
}
         
```




