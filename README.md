👁️ Morse Code Authentication — Blink-Based Communication System

Morse Code Authentication is an innovative computer vision project built using OpenCV that allows users to input alphabets or words using eye blinks.

By translating short blinks as dots (.) and long blinks as dashes (–), the system decodes your eye patterns into Morse code, then converts them into readable text or authentication keys.

This project demonstrates a futuristic way to interact with computers — hands-free, voice-free, and purely through eye movement.

✨ Features

👁️ Real-Time Eye Detection using OpenCV and Haar cascades

⚡ Blink Duration Detection – distinguishes between short and long blinks

🔠 Morse Code Translation – decodes blink patterns into alphabets or words

🔐 Authentication Use Case – use your unique blink pattern as a secure passcode

🔉 Live Feedback – displays detected blinks, Morse symbols, and decoded text on screen

💡 Hands-Free Operation – ideal for accessibility and assistive communication systems

🧩 Tech Stack

Python 3.8.10

OpenCV – for real-time face and eye detection

Haar Cascade Classifier – for detecting eye regions

Time module – for measuring blink duration

Morse Code Logic – custom algorithm for decoding signals

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/yourusername/MorseCodeAuthentication.git
cd MorseCodeAuthentication

2. Create a Virtual Environment (optional)
python -m venv env
env\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
python morse_auth.py

🧠 How It Works

Camera Capture
The webcam continuously captures frames in real-time.

Eye Detection
OpenCV detects the user’s eyes using Haar cascades or Dlib’s facial landmarks.

Blink Measurement
The system measures how long the eyes remain closed:

Short blink (dot) → .

Long blink (dash) → –

Morse Decoding
Once a pause is detected, the sequence of dots and dashes is matched with Morse code tables to determine the corresponding letter.

Output
The decoded text is displayed live on the screen and can be used for authentication or text entry.

🧩 Example
Blink Pattern	Morse Code	Output
Short → Long	.-	A
Short → Short → Short	...	S
Long → Short → Long	-.-	K

Example Use Case:
User blinks “.-- . .-.. -.-. --- -- .” → Translates to “WELCOME”

⚙️ Configuration Options

You can modify these parameters inside the script:

Short Blink Duration: default ≤ 0.25 seconds

Long Blink Duration: default > 0.25 seconds

Pause Threshold: defines when a new letter starts

Camera Index: change if you have multiple webcams

🎯 Potential Applications

🧑‍🦽 Assistive Communication for people with mobility or speech impairments

🔐 Secure Authentication based on blink patterns

💻 Hands-Free Input System for wearable or embedded devices

🧠 Human-Computer Interaction (HCI) research and innovation

🧠 Future Enhancements

Integration with facial landmark tracking for more accuracy

Adding GUI interface for visual Morse decoding feedback

Machine learning model to auto-tune blink thresholds

Support for custom authentication passphrases
