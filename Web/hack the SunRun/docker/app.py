import flask
import math
import os


latitude = []
longitude = []
def calculate_run_distance(lat1, lon1, lat2, lon2):
    R = 6371000 
    to_radians = lambda deg: math.radians(deg) 
    d_lat = to_radians(lat2 - lat1)  
    d_lon = to_radians(lon2 - lon1) 
    x = d_lon * math.cos(to_radians((lat1 + lat2) / 2))
    y = d_lat
    distance = math.sqrt(x**2 + y**2) * R
    return distance
flag=os.environ.get('FLAG')
distance = 0
time = 0

app = flask.Flask(__name__)

@app.route("/start")
def start():
    return flask.render_template("start_run.html")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/pages/run")
def runindex():
    return flask.render_template("run.html")

@app.route('/api/clock')
def clock():
    global time
    time+=1
    return flask.jsonify({"success":"time add successfully"})

@app.route('/api/getposition', methods=['POST'])
def get_position():
    global distance
    data = flask.request.json
    la = data.get('latitude')
    lo = data.get('longitude')
    print(f"Received position: Latitude={la}, Longitude={lo}")
    latitude.append(la)
    longitude.append(lo)
    if len(latitude) == 1:
        return "0"
    else:
        tmp = calculate_run_distance(latitude.pop(0),longitude.pop(0),latitude[0],longitude[0])
        distance += tmp
        return str(distance)
@app.route('/api/getdistance')
def getdistance():
    global distance
    return str(round(distance,2))


@app.route('/test')
def test():
    return flask.render_template("test.html")

@app.route('/end')
def end():
    global time
    global distance
    global flag

    if time == 0 :
        return "请完成长跑后再点击结束！"
    if not flag : 
        flag = "flag未正确设置，请联系运维"
    speed = distance / time
    info = f"本次跑步已结束，你的路程是：{round(distance,2)}m，用时{time}s，速度为{round(speed,2)}m/s。"
    fail_message0 = "一次长跑需要路程2km，不合格，不给flag"
    fail_message1 = "路程够了，但是太man了（<6m/s），不给flag"
    fail_message2 = "开桂了吧，速度比2km世界纪录（4分43秒）还快，不给flag"
    button = '''<button onclick="window.location.href='/pages/run'">再跑一次</button>'''
    if distance < 2000:
        message = f"<p>{info}</p><p>{fail_message0}</p>{button}"
    elif speed < 6:
        message = f"<p>{info}</p><p>{fail_message1}</p>{button}"
    elif speed > 7.06:
        message = f"<p>{info}</p><p>{fail_message2}</p>{button}"
    else:
        success = f"恭喜你完成了一次长跑，{flag}"
        message = f"<p>{info}</p><p>{success}</p>"
    time = 0
    distance = 0
    return message

if __name__ == "__main__":
    app.run("0.0.0.0",ssl_context=('cert.pem', 'key.pem'),port=5000)