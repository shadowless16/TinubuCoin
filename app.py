from flask import Flask, render_template
# import database


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user = database.get_user(user_id)
    if user:
        return jsonify({
            'username': user.username,
            'profile_photo': user.profile_photo_id
        })
    return jsonify({'error': 'User not found'}), 404
