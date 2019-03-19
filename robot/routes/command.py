from flask import request, jsonify

from robot import application as app

from robot import motion_control

actions = {
    'forward': motion_control.forward,
    'stop': motion_control.stop,
    'left': motion_control.left,
    'right': motion_control.right
}

@app.route('/command', methods=['POST','PUT'])
def command():
    data = request.get_json()
    # print(data)
    action = data['action']
    if action in actions:
        actions[action]()
    return jsonify({'status':'ok'})