import unittest
from app import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            'TESTING': True,
        })
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertIn(b"Type your tweet here", response.data)

    def test_tweet_post(self):
        # Here we should mock the tweepy.Client to not actually send the tweet.
        # This is a placeholder test.
        response = self.client.post('/tweet', data={'tweet_text': 'Test tweet'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tweet posted!", response.data)

    # More tests can be added for other functionalities.

if __name__ == "__main__":
    unittest.main()
