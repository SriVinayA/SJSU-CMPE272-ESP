from flask import Flask, render_template, request, jsonify
import tweepy
import config

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(config)  # Load configuration from config.py

    client = tweepy.Client(
        consumer_key=app.config['CONSUMER_KEY'],
        consumer_secret=app.config['CONSUMER_SECRET'],
        access_token=app.config['ACCESS_TOKEN'],
        access_token_secret=app.config['ACCESS_TOKEN_SECRET'],
    )

    @app.route('/')
    def index():
        return render_template('tweet.html')

    @app.route('/tweet', methods=['POST'])
    def tweet():
        tweet_text = request.form['tweet_text']
        response = client.create_tweet(text=tweet_text)
        tweet_id = response.data['id']
        return jsonify({'message': 'Tweet posted!', 'tweet_id': tweet_id})

    @app.route('/delete-tweet/<tweet_id>', methods=['DELETE'])
    def delete_tweet(tweet_id):
        client.delete_tweet(tweet_id)
        return jsonify({'message': f'Tweet with ID {tweet_id} deleted!'})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
