import json
import pandas as pd 

# Data Preproccess

def extract_user_features(user_feaures):
    user_feaures = json.loads(user_feaures)

    device_age = user_feaures['device_fingerprint']['age']
    cookie_age = user_feaures['cookie']['age']
    country_age = user_feaures['country']['age']
    asn_age = user_feaures['org']['age']
    ua_age = user_feaures['user_agent']['age']
    browser_age = user_feaures['browser_family']['age']
    os_age = user_feaures['os_family']['age']
    ip_age = user_feaures['ip']['age']

    return [device_age,
            cookie_age,
            country_age,
            asn_age,
            ua_age,
            browser_age,
            os_age,
            ip_age]

if __name__ == "__main__":
    path = 'data/AD_Music_Data_Sept_2024.csv'
    data = pd.read_csv(path)

    data['timestamp']  = pd.to_datetime(data['timestamp'], unit='s')
    data['account_creation_date']  = pd.to_datetime(data['account_creation_date'], unit='s')
    data['account_age_in_hours'] = (data['timestamp'] - data['account_creation_date']).dt.total_seconds() / 3600
    data['target_artist'] = data.path.apply(lambda x: x.split('/')[2] if x.startswith('/artist/') else None)
    data['target_user'] = data.path.apply(lambda x: x.split('/')[2] if x.startswith('/send_to/') else None)
    data['command'] = data['path'].apply(lambda x: x.split('/')[-1])
    data['email_domain'] = data['user_email'].apply(lambda x: x.split("@")[1])

    domain_counts = data.email_domain.value_counts(normalize=True)
    data['domain_rarity'] = data['email_domain'].map(domain_counts)

    data['ip_c_class'] = data.ip.apply(lambda  x: '.'.join(x.split('.')[:-1]))


    
    data['age'] = data.user_features.apply(lambda x: extract_user_features(x))
    age = pd.DataFrame(data['age'].tolist(), columns=['device_age', 
                                                    'cookie_age', 
                                                    'country_age',
                                                    'asn_age',
                                                    'ua_age',
                                                    'browser_age',
                                                    'os_age',
                                                    'ip_age'])
    data = pd.concat([data.drop(columns=['age']), age], axis=1)
    data.to_csv('data/ad_music_proccessed.csv')
