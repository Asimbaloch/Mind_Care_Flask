from flask import Blueprint, render_template, request, jsonify
from app.utils import get_ai_response

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@main.route('/mental_peace_videos')
def mental_peace_videos():
    return render_template('mental_peace_videos.html')

@main.route('/peace_music')
def peace_music():
    return render_template('peace_music.html')

@main.route('/information_posts')
def information_posts():
    return render_template('information_posts.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    image_url = request.json.get('image_url')
    
    try:
        response = get_ai_response(user_message, image_url)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500