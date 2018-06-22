# Before you can use the jobs API, you need to set up an access token.
# Log in to the IBM Q experience. Under "Account", generate a personal 
# access token. Replace 'PUT_YOUR_API_TOKEN_HERE' below with the quoted
# token string. Uncomment the APItoken variable, and you will be ready to go.

APItoken = '96c86855a5c381875a4ea3a956a7deafbbbbb82e5912ec73655c7c444d2597a7364eda2fa558e4e37f672640029443216899825f945d5a0684e31b796837ce61'

config = {
    'url': 'https://quantumexperience.ng.bluemix.net/api',

    # If you have access to IBM Q features, you also need to fill the "hub",
    # "group", and "project" details. Replace "None" on the lines below
    # with your details from Quantum Experience, quoting the strings, for
    # example: 'hub': 'my_hub'
    # You will also need to update the 'url' above, pointing it to your custom
    # URL for IBM Q.
    'hub': 'MY_HUB',
    'group': 'MY_GROUP',
    'project': 'MY_PROJECT'
}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
