from datetime import datetime as dt

import campaign
import get_data
import pvt_creds
import utils
import writer


campaign_ids = []


def campaign_list():
    _data = []
    res = get_data.get_data(url=utils.url_builder(
        variable=pvt_creds.creds[pvt_creds.CLIENT_NAME]['clientID'],
        resource=campaign.data['list']['resource'],
        context=campaign.data['list']['context'],
    ),
                            user=pvt_creds.creds[pvt_creds.CLIENT_NAME]['user'],
                            pwd=pvt_creds.creds[pvt_creds.CLIENT_NAME]['pwd'])
    for cm in res:
        campaign_ids.append(cm['CampaignID'])
        _temp = []
        for field in campaign.data['list']['fields'].keys():
            _temp.append(cm[field])
        _data.append(_temp)
    header = []
    for x in campaign.data['list']['fields'].keys():
        header.append(x)
    writer.csv_writer(_data, header=tuple(header), file_name='campaign_list')


def campaign_clicks():
    _data = []
    for cid in campaign_ids:
        res = get_data.get_data(url=utils.url_builder(
            variable=cid,
            resource=campaign.data['clicks']['resource'],
            context=campaign.data['clicks']['context'],
        ),
            user=pvt_creds.creds[pvt_creds.CLIENT_NAME]['user'],
            pwd=pvt_creds.creds[pvt_creds.CLIENT_NAME]['pwd'])
        for clk in res['Results']:
            _temp = [cid]
            for field in campaign.data['clicks']['fields'].keys():
                try:
                    _temp.append(clk[field])
                except KeyError:
                    _temp.append('')
            _data.append(_temp)
    header = ['CampaignID']
    for x in campaign.data['clicks']['fields'].keys():
        header.append(x)
    writer.csv_writer(_data, header=tuple(header), file_name='clicks')


# print('Start Campaign Lists:', dt.now())
# campaign_list()
# print('End Campaign Lists:', dt.now())
# print('Start Clicks:', dt.now())
# campaign_clicks()
# print('End Clicks:', dt.now())
