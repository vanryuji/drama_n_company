from flask import Flask, request, jsonify

import app.v1 as m_v1


web_app = Flask(__name__)


@web_app.route('/v1/users/create', methods=['POST'])
def v1_users_create():
    email = request.form['email']
    passwd = request.form['passwd']
    driver = request.form['driver']  # 't' or 'f'
    if m_v1.create_user(email, passwd, driver):
        result = {
            'users': {
                'email': email,
                'driver': driver
            }
        }
    else:
        result = {
            'error': {
                'code': 422,
                'message': 'Duplicate email',
                'more_info': {'email': email}
            }
        }
    return jsonify(result)


@web_app.route('/v1/users/login', methods=['POST'])
def v1_users_login():
    email = request.form['email']
    passwd = request.form['passwd']
    if m_v1.login(email, passwd):
        result = {
            'users': {
                'email': email,
            }
        }
        # TODO : create login session by flask-login if it needs
    else:
        result = {
            'error': {
                'code': 422,
                'message': 'Wrong email or password',
                'more_info': {'email': email}
            }
        }
    return jsonify(result)


@web_app.route('/v1/dispatches/request', methods=['POST'])
def v1_dispatches_request():
    email = request.form['email']
    address = unicode(request.form['address'])
    if not m_v1.validate_customer(email):
        return jsonify({
            'error': {
                'code': 422,
                'message': 'Invalid customer',
                'more_info': {}
            }
        })

    m_v1.request_dispatch(email, address)
    return jsonify({
        'dispatch': {
            'email': email,
            'address': address,
        }
    })


@web_app.route('/v1/dispatches', methods=['GET'])
def v1_dispatches():
    result = {
        'dispatches': {
            'wait': m_v1.get_dispatches(m_v1.DISPATCH_TYPE_WAIT),
            'complete': m_v1.get_dispatches(m_v1.DISPATCH_TYPE_COMPLETE),
        }
    }
    return jsonify(result)


@web_app.route('/v1/dispatches/response', methods=['PUT'])
def v1_dispatches_response():
    email = request.form['email']
    dispatch_id = request.form['dispatch_id']

    if not m_v1.validate_driver(email):
        return jsonify({
            'error': {
                'code': 422,
                'message': 'Invalid driver',
                'more_info': {}
            }
        })

    if m_v1.response_dispatch(dispatch_id, email):
        result = {
            'dispatch': {
                'email': email,
                'dispatch_id': dispatch_id,
            }
        }
    else:
        result = {
            'error': {
                'code': 422,
                'message': 'This dispatch was already allocated',
                'more_info': {}
            }
        }
    return jsonify(result)


if __name__ == '__main__':
    web_app.run(debug=True)
