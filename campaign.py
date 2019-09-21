data = {
    'list': {
        'variable': 'clientid',
        'resource': 'clients',
        'context': 'campaigns',
        'fields': {
            "FromName": "My Name",
            "FromEmail": "myemail@example.com",
            "ReplyTo": "myemail@example.com",
            "WebVersionURL": "http://createsend.com/t/r-765E86829575EE2C/",
            "WebVersionTextURL": "http://createsend.com/t/r-765E86829575EE2C/t",
            "CampaignID": "fc0ce7105baeaf97f47c99be31d02a91",
            "Subject": "Campaign One",
            "Name": "Campaign One",
            "SentDate": "0000-00-00 00:00:00",
            "TotalRecipients": 999
        }
    },
    'summary': {
        'variable': 'campaignid',
        'resource': 'campaigns',
        'context': 'summary',
        'fields': {
            "Recipients": 1000,
            "TotalOpened": 345,
            "Clicks": 132,
            "Unsubscribed": 43,
            "Bounced": 15,
            "UniqueOpened": 298,
            "SpamComplaints": 23,
            "WebVersionURL": "http://createsend.com/t/y-A1A1A1A1A1A1A1A1A1A1A1A1/",
            "WebVersionTextURL": "http://createsend.com/t/y-A1A1A1A1A1A1A1A1A1A1A1A1/t",
            "WorldviewURL": "http://myclient.createsend.com/reports/wv/y/8WY898U9U98U9U9",
            "Forwards": 18,
            "Likes": 25,
            "Mentions": 11
        }
    },
    'opens': {
        'variable': 'campaignid',
        'resource': 'campaigns',
        'context': 'opens',
        'fields': {
            "EmailAddress": "example+1@example.com",
            "ListID": "a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1",
            "Date": "2009-05-18 16:45:00",
            "IPAddress": "192.168.0.1",
            "Latitude": -33.8683,
            "Longitude": 151.2086,
            "City": "Sydney",
            "Region": "New South Wales",
            "CountryCode": "AU",
            "CountryName": "Australia"
        }
    },
    'clicks': {
        'variable': 'campaignid',
        'resource': 'campaigns',
        'context': 'clicks',
        'fields': {
            "EmailAddress": "example+1@example.com",
            "URL": "http://www.myexammple.com/index.html",
            "ListID": "a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1",
            "Date": "2009-05-18 16:45:00",
            "IPAddress": "192.168.0.1",
            "Latitude": -33.8683,
            "Longitude": 151.2086,
            "City": "Sydney",
            "Region": "New South Wales",
            "CountryCode": "AU",
            "CountryName": "Australia"
        }
    },
    'unsubs': {
        'variable': 'campaignid',
        'resource': 'campaigns',
        'context': 'unsubscribes',
        'fields': {
            "EmailAddress": "example+1@example.com",
            "ListID": "a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1",
            "Date": "2009-05-18 16:45:00",
            "IPAddress": "192.168.0.1"
        }
    },
}
