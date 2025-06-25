from cdnsadmin import create_app

app = create_app()

if __name__ == '__main__':
    # Listen on all network interfaces so the WebUI is reachable on the LAN
    app.run(debug=True, host="0.0.0.0")
