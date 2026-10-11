import webview

def create_window():
    html_content = """
    <!DOCTYPE html>
    <html lang="az">
    <head>
        <meta charset="UTF-8">
        <title>PrivChro Core</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: sans-serif; }
            body { background: #07090f; color: #00ffcc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
            
            #navbar { height: 50px; background: #0f1423; border-bottom: 1px solid #1e294b; display: flex; align-items: center; padding: 0 10px; gap: 8px; }
            .nav-btn { background: #131c31; border: 1px solid #22345c; color: #00ffcc; width: 36px; height: 36px; border-radius: 6px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 16px; }
            
            #url-bar { flex: 1; background: #05070d; border: 1px solid #22345c; height: 36px; border-radius: 6px; display: flex; align-items: center; padding: 0 12px; }
            #url-input { background: transparent; border: none; outline: none; color: #00ffcc; width: 100%; font-size: 14px; }

            #viewport { flex: 1; background: #0b0f19; display: flex; align-items: center; justify-content: center; text-align: center; }
        </style>
    </head>
    <body>
        <div id="navbar">
            <button class="nav-btn" onclick="location.reload()">🔄</button>
            <div id="url-bar">
                <input type="text" id="url-input" value="https://duckduckgo.com">
            </div>
            <button class="nav-btn" onclick="alert('Ayarlar paneli')">⚙️</button>
        </div>
        <div id="viewport">
            <h3>PrivChro Boş Bünövrə Aktivdir</h3>
        </div>
    </body>
    </html>
    """
    webview.create_window("PrivChro", html=html_content, width=900, height=700, background_color='#07090f')
    webview.start()

if __name__ == '__main__':
    create_window()
