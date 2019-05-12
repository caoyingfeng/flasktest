import memcache


mc = memcache.Client(['127.0.0.1:11211'],debug=True)

# mc.set('username','cmx', time=120)

# mc.set_multi({'title':'123','content':'abc'},time=120)

username = mc.get('username')
print(username)