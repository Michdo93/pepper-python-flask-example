[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A simple example how to use the Python SDK with the pepper robot within a Flask web application. This application will shutdown the pepper after pressing a button. The Python SDK is used for this purpose. A system service is created via this. This service calls the shutdown.

1. Clone the repo and install the requirements with Python 2.7:
  ```
  git clone https://github.com/Michdo93/pepper-python-flask-example.git
  cd pepper-python-flask-example
  pip install -r requirements.txt
  ```
  
2. Download the Pepper Python SDK
   ```
   wget https://community-static.aldebaran.com/resources/2.5.10/Python%20SDK/pynaoqi-python2.7-2.5.7.1-linux64.tar.gz
   ```
   
   Maybe you have to download the Python SDK for Windows or MAC.
 
3. Install the Pepper Python SDK
   Please read [this](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/sdks/python-sdk/python-sdk-installation-guide) for more advices.

4. Run the development server:
  ```
  python app.py
  ```

5. Navigate to [http://localhost:5000](http://localhost:5000)
