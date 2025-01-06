from commands import COMMANDS

one_year = 24 * 365

def get_command_sensitivity(command):
    return COMMANDS.sensetivity_map.get(command) or 0.001
    
def calculate_age_sensitivity(session):
    age_sensitivity = 1
    if session.account_age_in_hours > one_year:
        if session.cookie_age < 1 and session.device_age < 1:
            age_sensitivity = 2
        if session.device_age > one_year or session.cookie_age > one_year:
            age_sensitivity = 0.5
    return age_sensitivity

def calculate_session_sensetivity(session):
    command_sensitivity = get_command_sensitivity(session.command)
    age_sensitivity = calculate_age_sensitivity(session)
    session_sensistivity = command_sensitivity * age_sensitivity 
    return session_sensistivity