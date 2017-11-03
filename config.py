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
device_id='2f0400f7-8822-4af1-aa1c-47008963e203'
oauth_credentials_for_device='63e2f3b57ee0cb7cf5f82547688131fe'

message_type_id_From_device='059fc0870b48407c90ad'
message_type_id_To_device='f7594b5ca7b341318f54'

# ===== nothing to be changed / configured below this line ===========
