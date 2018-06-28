# Before you can use the jobs API, you need to set up an access token.
# Log in to the IBM Q experience. Under "Account", generate a personal 
# access token. Replace 'PUT_YOUR_API_TOKEN_HERE' below with the quoted
# token string. Uncomment the APItoken variable, and you will be ready to go.

APItoken = '36ad8b31280d5d431c22e75d77858b3500186b7a4836b0b25199fe40edf502addfa35cb19ab8d1bd91e67418c2039efb5f7310bae262bee1a114c6523e7aee4a'

config = {
    'url': 'https://quantumexperience.ng.bluemix.net/api',

    # If you have access to IBM Q features, you also need to fill the "hub",
    # "group", and "project" details. Replace "None" on the lines below
    # with your details from Quantum Experience, quoting the strings, for
    # example: 'hub': 'my_hub'
    # You will also need to update the 'url' above, pointing it to your custom
    # URL for IBM Q.
    'hub': 'HUBBA_HUBBA'
    'group': 'FUD'
    'project': 'BUILD'
}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
