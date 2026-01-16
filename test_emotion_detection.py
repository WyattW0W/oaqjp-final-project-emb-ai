import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant"], "joy")
        self.assertEqual(emotion_detector("I am really mad about this")["dominant"], "anger")
        self.assertEqual(emotion_detector("I feel disgusted about this")["dominant"], "disgust")
        self.assertEqual(emotion_detector("I am so sad about this")["dominant"], "sadness")
        self.assertEqual(emotion_detector("I am really afraid about this")["dominant"], "fear")
        # I shortened the prompts for disgust and fear in order to get the lines less than 100

if __name__ == "__main__":
    unittest.main()