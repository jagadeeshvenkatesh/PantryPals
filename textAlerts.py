from bandwidth import messaging, voice, account
messaging_api = messaging.Client('u-cbnapluxzd4wndtezeitasq', 't-dkfhqbmlimll7sfwxtl2ijy', 'vagoxd24knrdrxvuify6ks2eq2fv4wpba6c2dcy')
voice_api = voice.Client('u-cbnapluxzd4wndtezeitasq', 't-dkfhqbmlimll7sfwxtl2ijy', 'vagoxd24knrdrxvuify6ks2eq2fv4wpba6c2dcy')
account_api = account.Client('u-cbnapluxzd4wndtezeitasq', 't-dkfhqbmlimll7sfwxtl2ijy', 'vagoxd24knrdrxvuify6ks2eq2fv4wpba6c2dcy')

fromNumber = '+19102414176'
message = 'Shreya purchased bread, milk and eggs for you'

shreyaNumber = '+18432604372'
helenaNumber = '+18438221283'
natalieNumber = '+18154512285'

def sendText(f,t,m):
	message_id = messaging_api.send_message(from_ = f,
                              				to = t,
                              				text = m)
	print(message_id)



