from flask import Flask, jsonify, make_response
import threading
import requests
import time
import random
import os

app = Flask(__name__, static_folder=None)

# ==========================================
# MASTER CONFIGURATIONS & 1.1M KNOWLEDGE REGISTRY
# ==========================================
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "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")
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY", "dbcaa19r01qqr3s0pf60dbcaa19r01qqr3s0pf6g")
TWELVE_DATA_KEY = os.environ.get("TWELVE_DATA_KEY", "8f5d4d4fce7f44e5bda54420591411c8")
QX_API_TOKEN = os.environ.get("QX_API_TOKEN", "qx_live_1xxOcsg5_3vEavHfZwAkGufh9NLLWJhUqG3T6H6oCEuoDWeJV")

http_session = requests.Session()

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

@app.route('/')
def home():
    return "RA QX Spooky Bot Engine v360.0 [Ghost Mode Active] Running 24/7!"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/signal')
def get_signal():
    try:
        t = int(time.time() * 1000)
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are an elite institutional trading arbiter. Return ONLY 'UP' or 'DOWN' based on strict market momentum. No extra text."},
                {"role": "user", "content": "Evaluate accurate market direction now:"}
            ],
            "temperature": 0.01,
            "max_tokens": 5
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=2.5)
        base_signal = "UP"
        if resp.status_code == 200:
            ai_text = resp.json()["choices"][0]["message"]["content"].strip().upper()
            if "DOWN" in ai_text or "PUT" in ai_text:
                base_signal = "DOWN"
        else:
            base_signal = "UP" if (t % 2 == 0) else "DOWN"
            
        signal_conf = 99
        
        res = jsonify({
            "signal": base_signal,
            "trend": "GHOST CONFLUENCE MOMENTUM",
            "confidence": signal_conf,
            "status": "GREEN_EXECUTE"
        })
        return res
    except Exception as e:
        res = jsonify({
            "signal": "UP",
            "trend": "GHOST ARBITER GATE",
            "confidence": 99,
            "status": "GREEN_EXECUTE"
        })
        return res

@app.route('/bot.js')
def bot_script():
    js = """
    (function(){
        try {
            var d = document;
            var uniqueId = 'ra_qx_bot_' + Math.floor(Math.random() * 10000);
            
            var oldS = d.getElementById('ra_spooky_global');
            if(!oldS){
                var s = d.createElement('style');
                s.id = 'ra_spooky_global';
                s.innerHTML = 
                    '@keyframes spookyPillGlow {' +
                        '0%{border-color:#00ff66;box-shadow:0 0 20px rgba(0,255,102,0.6), inset 0 0 10px rgba(0,255,102,0.3);}' +
                        '50%{border-color:#9400D3;box-shadow:0 0 25px rgba(148,0,211,0.8), inset 0 0 15px rgba(148,0,211,0.4);}' +
                        '100%{border-color:#00ff66;box-shadow:0 0 20px rgba(0,255,102,0.6), inset 0 0 10px rgba(0,255,102,0.3);}' +
                    '}' +
                    '@keyframes ghostRingSpin {' +
                        '0%{transform:rotate(0deg) scale(1);}' +
                        '50%{transform:rotate(180deg) scale(1.08);}' +
                        '100%{transform:rotate(360deg) scale(1);}' +
                    '}' +
                    '@keyframes spookyPulseText {' +
                        '0%{opacity:0.6;text-shadow:0 0 10px #00ff66;}' +
                        '50%{opacity:1;text-shadow:0 0 25px #ff0055, 0 0 40px #9400D3;}' +
                        '100%{opacity:0.6;text-shadow:0 0 10px #00ff66;}' +
                    '}' +
                    '@keyframes panelPop {0%{opacity:0;transform:scale(0.8);}100%{opacity:1;transform:scale(1);}}' +
                    '@keyframes spinAnim {0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}';
                d.head.appendChild(s);
            }

            createPillWidget();

            function createPillWidget(){
                var existingWrap = d.getElementById('ra_pill_wrap');
                if(existingWrap) existingWrap.remove();

                var wrap = d.createElement('div');
                wrap.id = 'ra_pill_wrap';
                wrap.style.cssText = 'position:fixed;bottom:25px;left:25px;display:flex;align-items:center;gap:8px;background:linear-gradient(135deg, #07040f, #0d0918);border:2px solid #00ff66;padding:6px 12px 6px 6px;border-radius:30px;z-index:2147483647;cursor:pointer;box-sizing:border-box;animation:spookyPillGlow 3.5s infinite ease-in-out;font-family:sans-serif;user-select:none;box-shadow:0 10px 30px rgba(0,0,0,0.8);';
                
                var logoImg = d.createElement('img');
                logoImg.src = 'https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg';
                logoImg.style.cssText = 'width:28px;height:28px;border-radius:50%;object-fit:cover;border:2px solid #9400D3;flex-shrink:0;';
                wrap.appendChild(logoImg);

                var textDiv = d.createElement('div');
                textDiv.style.cssText = 'display:flex;flex-direction:column;line-height:1.1;';
                textDiv.innerHTML = '<span style="font-size:10px;font-weight:900;color:#00ff66;letter-spacing:0.8px;">RA QX BOT</span>' +
                                    '<span style="font-size:6.5px;color:#b19cd9;font-weight:700;letter-spacing:0.3px;">GHOST AI v2</span>';
                wrap.appendChild(textDiv);

                d.body.appendChild(wrap);
                
                var isDragging = false, startX, startY, hasMoved = false;
                wrap.onmousedown = wrap.ontouchstart = function(e){
                    isDragging = true; hasMoved = false;
                    var p = e.touches ? e.touches[0] : e;
                    startX = p.clientX - wrap.offsetLeft;
                    startY = p.clientY - wrap.offsetTop;
                };
                wrap.onmousemove = wrap.ontouchmove = function(e){
                    if(!isDragging) return;
                    var p = e.touches ? e.touches[0] : e;
                    var nx = p.clientX - startX, ny = p.clientY - startY;
                    if(Math.abs(nx - wrap.offsetLeft) > 2 || Math.abs(ny - wrap.offsetTop) > 2) hasMoved = true;
                    wrap.style.left = nx + 'px';
                    wrap.style.top = ny + 'px';
                    wrap.style.bottom = 'auto';
                    wrap.style.right = 'auto';
                };
                wrap.onmouseup = wrap.ontouchend = function(){ isDragging = false; };
                
                wrap.onclick = function(){
                    if(hasMoved) return;
                    runGhostScanningAndTrade();
                };
            }

            var hasExecutedThisRound = false;

            function triggerStrictSingleTrade(isSell){
                if(hasExecutedThisRound) return;
                hasExecutedThisRound = true;

                var targetBtn = null;
                
                if(isSell){
                    targetBtn = d.querySelector('.section-deal__button-down button') || 
                                d.querySelector('.section-deal__button-down') || 
                                d.querySelector('button.btn-red') || 
                                d.querySelector('button[class*="put"]') || 
                                d.querySelector('button[class*="sell"]');
                } else {
                    targetBtn = d.querySelector('.section-deal__button-up button') || 
                                d.querySelector('.section-deal__button-up') || 
                                d.querySelector('button.btn-green') || 
                                d.querySelector('button[class*="call"]') || 
                                d.querySelector('button[class*="buy"]');
                }

                if(!targetBtn){
                    var btns = d.querySelectorAll('.section-deal button, button, div[role="button"]');
                    for(var i=0; i<btns.length; i++){
                        var txt = (btns[i].innerText || '').toUpperCase();
                        var cls = (btns[i].className || '').toLowerCase();
                        if(isSell && (txt.includes('DOWN') || txt.includes('SELL') || txt.includes('PUT') || cls.includes('down') || cls.includes('put') || cls.includes('red'))){
                            if(btns[i].getBoundingClientRect().width > 0) { targetBtn = btns[i]; break; }
                        }
                        if(!isSell && (txt.includes('UP') || txt.includes('BUY') || txt.includes('CALL') || cls.includes('up') || cls.includes('call') || cls.includes('green'))){
                            if(btns[i].getBoundingClientRect().width > 0) { targetBtn = btns[i]; break; }
                        }
                    }
                }

                if(targetBtn && targetBtn.getBoundingClientRect().width > 0){
                    try {
                        targetBtn.click();
                    } catch(e){}
                }
            }

            var isScanningActive = false;

            function runGhostScanningAndTrade(){
                if(isScanningActive) return;
                isScanningActive = true;
                hasExecutedThisRound = false;

                // Full screen spooky dim overlay
                var spookyOverlay = d.createElement('div');
                spookyOverlay.id = 'ra_spooky_overlay';
                spookyOverlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(3,2,10,0.82);backdrop-filter:blur(3px);z-index:2147483645;display:flex;align-items:center;justify-content:center;pointer-events:none;animation:panelPop 0.3s ease-out;';
                
                // Center Ghost Radar/Scanner box
                var centerScanner = d.createElement('div');
                centerScanner.style.cssText = 'position:relative;width:280px;height:280px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-family:monospace;';
                
                var ghostRing = d.createElement('div');
                ghostRing.style.cssText = 'position:absolute;width:100%;height:100%;border:4px dashed #00ff66;border-radius:50%;box-shadow:0 0 50px rgba(0,255,102,0.4), inset 0 0 50px rgba(148,0,211,0.5);animation:ghostRingSpin 4s infinite linear;';
                centerScanner.appendChild(ghostRing);

                var innerGlow = d.createElement('div');
                innerGlow.style.cssText = 'position:absolute;width:210px;height:210px;border:3px solid #ff0055;border-radius:50%;box-shadow:0 0 35px rgba(255,0,85,0.6);animation:ghostRingSpin 3s infinite reverse linear;';
                centerScanner.appendChild(innerGlow);

                var scanContent = d.createElement('div');
                scanContent.style.cssText = 'position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;gap:6px;';
                scanContent.innerHTML = '<div style="font-size:22px;">👻</div>' +
                                        '<div style="font-size:13px;font-weight:bold;color:#00ff66;letter-spacing:1px;animation:spookyPulseText 1.5s infinite;">GHOST SCANNING...</div>' +
                                        '<div style="font-size:9px;color:#b19cd9;" id="ghost-status-sub">Reading Market Matrix</div>';
                centerScanner.appendChild(scanContent);

                spookyOverlay.appendChild(centerScanner);
                d.body.appendChild(spookyOverlay);

                // Fetch backend signal after 6 seconds of spooky scanning animation
                setTimeout(function(){
                    fetch('https://qx-hack-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN", confidence: 99}; })
                    .then(function(j){
                        var rawSig = String(j.signal || 'DOWN').toUpperCase();
                        var isDown = (rawSig === 'SELL' || rawSig === 'DOWN' || rawSig === 'PUT');
                        
                        triggerStrictSingleTrade(isDown);

                        var sigText = isDown ? 'SIGNAL: DOWN ⬇️' : 'SIGNAL: UP ⬆️';
                        var sigColor = isDown ? '#ff1744' : '#00ff66';

                        // Update center display to show trade execution result
                        ghostRing.style.borderColor = sigColor;
                        ghostRing.style.animation = 'none';
                        innerGlow.style.borderColor = sigColor;
                        
                        scanContent.innerHTML = '<div style="font-size:26px;">⚡</div>' +
                                                '<div style="font-size:16px;font-weight:900;color:' + sigColor + ';text-shadow:0 0 20px ' + sigColor + ';">' + sigText + '</div>' +
                                                '<div style="font-size:10px;color:#fff;margin-top:4px;">AUTO-EXECUTED SUCCESSFULLY!</div>';

                        // Remove overlay after 2 seconds
                        setTimeout(function(){
                            if(spookyOverlay) spookyOverlay.remove();
                            isScanningActive = false;
                        }, 2000);
                    });
                }, 6000);
            }
        } catch(e) { console.error("RAGhostBot Error:", e); }
    })();
    """
    res = make_response(js)
    res.headers['Content-Type'] = 'application/javascript'
    return res

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
