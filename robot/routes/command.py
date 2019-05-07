from flask import request, jsonify

from robot import application as app

from robot import motion_control

actions = {
    'forward': motion_control.forward,
    'stop': motion_control.stop,
    'left': motion_control.left,
    'right': motion_control.right,
    'reverse': motion_control.reverse,
    'forward_steer': motion_control.steer_forward_2,
    'reverse_steer': motion_control.steer_reverse_2
}

@app.route('/command', methods=['POST','PUT'])
def command():
    data = request.get_json()
    # print(data)
    action = data['action']
    gas = data['gas'] if 'gas' in data else 1
    multiplier = data['multiplier'] if 'multiplier' in data else 1
    if action == 'forward_steer' or action == 'reverse_steer':
        degree = data['degree'] if 'degree' in data else 0
        actions[action](degree, gas, multiplier)
    elif action in actions:
        actions[action](multiplier)
    return jsonify({'status':'ok'})