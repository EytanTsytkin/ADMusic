class Commands:
    withdraw = 'withdraw_balance'

    sensetive = ['disable_mfa',
                'change_withdrawal_method',
                'withdraw_balance',
                'change_password',
                'change_shipping_address'
                ]
    
    physical_theft = ['change_shipping_address',
                      'submit_purchase',]

    funds_extraction = ['change_password',
                        withdraw,
                        'disable_mfa',
                        'change_withdrawal_method',]
    
    ato = ['change_password',
               'disable_mfa',
               ]
    
    info_steal = ['view_full_info',
                  'download_info',
                  'personal_details']
    
    phishing = ['send_message',
                'add_comment']
    
    stream_faking = ['play',
                     'skip',]

    strange = ['A520311',
                'A121720',
                'AL411722',
                'AL525793',
                'AL634586',
                'AL143326',
                'AL356613',
                'A409478',
                'AL531011',
                'A762816',
                'AL283235',
                'A783696',
                'A035765',
                'AL274308',
                'AL748975',
                'AL825739',
                ]

    sensetivity_map = { **{cmd : 1 for cmd in funds_extraction},
                        **{cmd : 1 for cmd in physical_theft},
                        **{cmd : 0.8 for cmd in strange},
                        **{cmd : 0.8 for cmd in info_steal}
                        }
                       
    

COMMANDS = Commands()