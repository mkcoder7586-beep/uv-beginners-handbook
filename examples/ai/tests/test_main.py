def test_imports():
    from ai_chatbot.main import app
    assert app is not None

def test_flask_setup():
    from ai_chatbot.main import app
    client = app.test_client()
    assert client is not None
