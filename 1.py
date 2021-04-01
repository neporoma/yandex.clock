import geoip2.database

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/geoip')
def geoip():
    remote_ip = ""
#    user_agent = ""
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        remote_ip = request.environ['REMOTE_ADDR'].split (',')[0]
    else:
        remote_ip = request.environ['HTTP_X_FORWARDED_FOR'].split (',')[0]

    remote_ip = '188.32.54.215'

    with geoip2.database.Reader('D:\GeoLite2-City.mmdb') as reader:
        response = reader.city('188.32.54.215')

    return 'Ваш IP адрес: ' + remote_ip + ', вы находитесь в стране ' + response.country.names['ru'] + ', в городе ' + response.city.names['ru']

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)


#print(response.country.iso_code)

#print(response.country.name)

print(response.country.names['ru'])

#print(response.subdivisions.most_specific.name)

#print(response.subdivisions.most_specific.iso_code)

#print(response.city.name)

print(response.city.names['ru'])

#print(response.postal.code)

#print(response.location.latitude)

#print(response.location.longitude)

print(response.traits.network)
