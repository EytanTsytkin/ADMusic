import pandas as pd

def find_sure_matches(session,device_data,ip_data,ck_data):
    # Looks for similar seesions using Hard indicators
    device_match = device_data.loc[session.device_fingerprint]
    cookie_match = ck_data.loc[session.cookie]
    ip_match = ip_data.loc[session.ip]
    sure_matches = pd.concat([ip_match,cookie_match,device_match])
    sure_matches = sure_matches.drop_duplicates()
    sure_matches['relevance'] = 1
    return sure_matches

def find_ip_c_class_mathces(session, ip_c_data):
    # Finds sessions with similar ip c class
    ip_weak_match = None
    ip_weak_match = ip_c_data.loc[session.ip_c_class]
    ip_weak_match['relevance'] = 0.8
    return ip_weak_match

def find_matching_domains(session,domain_data):
    # Finds sessions with similar Rare Email Domain
    domain_match = None
    if session.domain_rarity < 0.01:
        domain_match = domain_data.loc[session.email_domain]
        domain_match['relevance'] = 2
    return domain_match

def find_partial_matches(session, ip_c_data, domain_data):
    # Looks for rare email matches + ip c class matches.
    # Combines results and increases the relevance of duplicates.
    ip_weak_match = find_ip_c_class_mathces(session, ip_c_data)
    rare_domain_match = find_matching_domains(session, domain_data)
    if ip_weak_match is not None and rare_domain_match is not None:
        combined = pd.concat([ip_weak_match, rare_domain_match], ignore_index=True)
        duplicates = combined.duplicated(subset=['timestamp', 'user_id'], keep=False)
        # Sessions with same rare domain and c class
        combined.loc[duplicates, 'relevance'] = 3
        combined = combined.drop_duplicates(subset=['timestamp', 'user_id'], keep='first')
        return combined 
    else: 
        try:
            # Either one is not None
            return pd.concat([ip_weak_match,rare_domain_match])
        except ValueError:
            # Both are None
            return None

def fetch_related_sessions(session, device_data,ip_data,ck_data, ip_c_data, domain_data):

    sure_matches = find_sure_matches(session, device_data,ip_data,ck_data)
    # Exclude sure matches from the rest of the data
    # weak_matches = find_partial_matches(session,ip_c_data, domain_data)
    # related_sessions = pd.concat([sure_matches, weak_matches])
    # related_sessions = related_sessions.drop_duplicates(subset=[col for col in related_sessions.columns if col != 'relevance'])
    related_sessions = sure_matches.sort_values(by='timestamp')
    related_sessions = sure_matches[sure_matches.timestamp < session.timestamp]
    return related_sessions

def index_data(data):
    # Indexes the dataframe by rekevant matching columns
    device_data = data.set_index(data.device_fingerprint)
    ip_data = data.set_index(data.ip)
    ck_data = data.set_index(data.cookie)
    ip_c_data = data.set_index(data.ip_c_class)
    domain_data = data.set_index(data.email_domain)
    return device_data,ip_data,ck_data, ip_c_data, domain_data