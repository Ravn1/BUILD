#print("Please configure appropriately and then remove this line !"); exit();

# ===== Your specific configuration goes below / please adapt ========

# the HCP account id - trial accounts typically look like p[0-9]*trial
hcp_account_id='s0011642097trial'

# you only need to adapt this part of the URL if you are NOT ON TRIAL but e.g. on PROD
hcp_landscape_host='.hanatrial.ondemand.com'
# hcp_landscape_host='.hana.ondemand.com' # this is used on PROD

# these credentials are used from applications with the "push messages to devices" API
hcp_user_credentials='s0011642097:Odense_1'

# optional network proxy, set if to be used, otherwise set to ''
proxy_url=''
# proxy_url='http://proxy_host:proxy_port'

# the following values need to be taken from the IoT Cockpit
device_id='7b136684-5945-4867-a80a-2db5551c226b'
oauth_credentials_for_device='322a6b5399dcf94bf22eebc074179ca9'

message_type_id_From_device='3b1f0ae2656e22b30b9f'
message_type_id_To_device='43e30128c8747330845a'

# ===== nothing to be changed / configured below this line ===========
