from redis import Redis

cache = Redis(host='127.0.0.1', port=6379)

# cache.set('username','cy')

ps = cache.pubsub()
ps.subscribe('email')
while True:
    for item in ps.listen():
        if item['type']=='message':
            print(item['data'])