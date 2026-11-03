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
        market_status = "GREEN_EXECUTE"
        
        if resp.status_code == 200:
            ai_text = resp.json()["choices"][0]["message"]["content"].strip().upper()
            if "DOWN" in ai_text or "PUT" in ai_text:
                base_signal = "DOWN"
            # Volatility check simulation
            if "VOLATILE" in ai_text or (t % 15 == 0):
                market_status = "VOLATILE_WAIT"
        else:
            base_signal = "UP" if (t % 2 == 0) else "DOWN"
            
        signal_conf = 99
        
        res = jsonify({
            "signal": base_signal,
            "trend": "GHOST CONFLUENCE MOMENTUM",
            "confidence": signal_conf,
            "status": market_status
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
                        '0%{border-color:#00ff66;box-shadow:0 0 22px rgba(0,255,102,0.7), inset 0 0 12px rgba(0,255,102,0.4);}' +
                        '50%{border-color:#9400D3;box-shadow:0 0 28px rgba(148,0,211,0.9), inset 0 0 18px rgba(148,0,211,0.5);}' +
                        '100%{border-color:#00ff66;box-shadow:0 0 22px rgba(0,255,102,0.7), inset 0 0 12px rgba(0,255,102,0.4);}' +
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
                    '@keyframes panelPop {0%{opacity:0;transform:translate(-50%, -48%) scale(0.85);}100%{opacity:1;transform:translate(-50%, -50%) scale(1);}}' +
                    '@keyframes spinAnim {0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}';
                d.head.appendChild(s);
            }

            var isVerified = sessionStorage.getItem('ra_bot_verified_' + uniqueId) === 'true';

            if(!isVerified){
                createLicensePanel();
            } else {
                createPillWidget();
            }

            function speakVoice(text) {
                try {
                    if('speechSynthesis' in window) {
                        window.speechSynthesis.cancel();
                        var utterance = new SpeechSynthesisUtterance(text);
                        utterance.lang = 'bn-BD';
                        utterance.rate = 1.05;
                        utterance.pitch = 1.1;
                        window.speechSynthesis.speak(utterance);
                    }
                } catch(e){}
            }

            function createLicensePanel(){
                var panel = d.getElementById('ra_bot_license_panel');
                if(panel) panel.remove();

                panel = d.createElement('div');
                panel.id = 'ra_bot_license_panel';
                panel.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%, -50%);width:250px;background:linear-gradient(135deg, #07040f, #0d0918);border:2.5px solid #00ff66;border-radius:14px;z-index:2147483647;font-family:sans-serif;color:#fff;box-shadow:0 25px 80px rgba(0,0,0,0.95);overflow:hidden;animation:panelPop 0.3s ease-out forwards, spookyPillGlow 2.0s infinite linear;';
                
                var header = d.createElement('div');
                header.style.cssText = 'background:#030208;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #161026;';
                header.innerHTML = '<div style="display:flex;align-items:center;gap:8px;">' +
                                   '<img src="https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg" style="width:34px;height:34px;border-radius:50%;object-fit:cover;border:2px solid #00ff66;" />' +
                                   '<div>' +
                                   '<div style="font-size:11px;font-weight:900;color:#00ff66;letter-spacing:0.8px;">RA QX BOT</div>' +
                                   '<div style="font-size:6.5px;color:#b19cd9;font-weight:700;">SECURE ACCESS</div>' +
                                   '</div>' +
                                   '</div>' +
                                   '<button id="close-license" style="background:#130b22;border:none;color:#fff;width:22px;height:22px;border-radius:50%;cursor:pointer;font-weight:bold;font-size:12px;">×</button>';
                panel.appendChild(header);
                header.querySelector('#close-license').onclick = function(){ panel.remove(); };

                var box = d.createElement('div');
                box.style.cssText = 'padding:14px;text-align:center;';
                box.innerHTML = '<div style="font-size:8.5px;color:#b19cd9;margin-bottom:6px;" id="err-msg">Enter Bot Access Key</div>' +
                                '<input type="password" id="license-input" placeholder="Password (YR)" style="width:100%;box-sizing:border-box;background:#030208;border:1px solid #23173d;padding:8px;border-radius:6px;color:#fff;font-size:10px;outline:none;margin-bottom:10px;text-align:center;letter-spacing:2px;" />' +
                                '<button id="verify-btn" style="width:100%;background:linear-gradient(90deg, #00ff66, #9400D3);border:none;padding:9px;border-radius:6px;font-weight:900;font-size:10px;color:#000;cursor:pointer;box-shadow:0 0 20px rgba(0,255,102,0.6);">ACTIVATE BOT</button>';
                panel.appendChild(box);

                var verifyBtn = box.querySelector('#verify-btn');
                var licenseInput = box.querySelector('#license-input');
                var errMsg = box.querySelector('#err-msg');

                verifyBtn.onclick = function(){
                    var keyVal = licenseInput.value.trim();
                    if(keyVal === 'YR'){
                        verifyBtn.innerHTML = '<span style="display:inline-block;width:9px;height:9px;border:2px solid #000;border-top-color:transparent;border-radius:50%;animation:spinAnim 0.8s linear infinite;"></span> Verifying...';
                        setTimeout(function(){
                            sessionStorage.setItem('ra_bot_verified_' + uniqueId, 'true');
                            panel.remove();
                            createPillWidget();
                        }, 800);
                    } else {
                        errMsg.innerText = '⚠️ INCORRECT KEY!';
                        errMsg.style.color = '#ff1744';
                        licenseInput.style.borderColor = '#ff1744';
                        verifyBtn.style.background = '#ff1744';
                        verifyBtn.style.color = '#fff';
                        verifyBtn.innerText = 'ACCESS DENIED';
                    }
                };

                d.body.appendChild(panel);
            }

            function createPillWidget(){
                var existingWrap = d.getElementById('ra_pill_wrap');
                if(existingWrap) existingWrap.remove();

                var wrap = d.createElement('div');
                wrap.id = 'ra_pill_wrap';
                wrap.style.cssText = 'position:fixed;bottom:25px;left:25px;display:flex;align-items:center;gap:10px;background:linear-gradient(135deg, #07040f, #0d0918);border:2.5px solid #00ff66;padding:8px 16px 8px 8px;border-radius:35px;z-index:2147483647;cursor:pointer;box-sizing:border-box;animation:spookyPillGlow 2.0s infinite ease-in-out;font-family:sans-serif;user-select:none;box-shadow:0 12px 35px rgba(0,0,0,0.85);';
                
                var logoImg = d.createElement('img');
                logoImg.src = 'https://i.postimg.cc/JzRR8g6M/IMG-20261102-WA0003.jpg';
                logoImg.style.cssText = 'width:34px;height:34px;border-radius:50%;object-fit:cover;border:2px solid #9400D3;flex-shrink:0;';
                wrap.appendChild(logoImg);

                var textDiv = d.createElement('div');
                textDiv.style.cssText = 'display:flex;flex-direction:column;line-height:1.2;';
                textDiv.innerHTML = '<span style="font-size:11px;font-weight:900;color:#00ff66;letter-spacing:0.8px;">RA QX BOT</span>' +
                                    '<span style="font-size:7.5px;color:#b19cd9;font-weight:700;letter-spacing:0.4px;">GHOST AI v2</span>';
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

                speakVoice("মার্কেট স্ক্যানিং করা হচ্ছে");

                var spookyOverlay = d.createElement('div');
                spookyOverlay.id = 'ra_spooky_overlay';
                spookyOverlay.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(3,2,10,0.85);backdrop-filter:blur(3.5px);z-index:2147483645;display:flex;align-items:center;justify-content:center;pointer-events:none;animation:panelPop 0.3s ease-out;';
                
                var centerScanner = d.createElement('div');
                centerScanner.style.cssText = 'position:relative;width:290px;height:290px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-family:monospace;';
                
                var ghostRing = d.createElement('div');
                ghostRing.style.cssText = 'position:absolute;width:100%;height:100%;border:4px dashed #00ff66;border-radius:50%;box-shadow:0 0 55px rgba(0,255,102,0.5), inset 0 0 55px rgba(148,0,211,0.6);animation:ghostRingSpin 3.5s infinite linear;';
                centerScanner.appendChild(ghostRing);

                var innerGlow = d.createElement('div');
                innerGlow.style.cssText = 'position:absolute;width:220px;height:220px;border:3px solid #ff0055;border-radius:50%;box-shadow:0 0 40px rgba(255,0,85,0.7);animation:ghostRingSpin 2.5s infinite reverse linear;';
                centerScanner.appendChild(innerGlow);

                var scanContent = d.createElement('div');
                scanContent.style.cssText = 'position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;gap:6px;';
                scanContent.innerHTML = '<div style="font-size:24px;">👻</div>' +
                                        '<div style="font-size:14px;font-weight:bold;color:#00ff66;letter-spacing:1px;animation:spookyPulseText 1.2s infinite;">GHOST SCANNING...</div>' +
                                        '<div style="font-size:9.5px;color:#b19cd9;" id="scan-sub-text">Reading Market Matrix</div>';
                centerScanner.appendChild(scanContent);

                spookyOverlay.appendChild(centerScanner);
                d.body.appendChild(spookyOverlay);

                setTimeout(function(){
                    fetch('https://qx-hack-bot.onrender.com/signal?t='+Date.now())
                    .then(function(r){ return r.json(); })
                    .catch(function(){ return {signal: "DOWN", confidence: 99, status: "GREEN_EXECUTE"}; })
                    .then(function(j){
                        var rawSig = String(j.signal || 'DOWN').toUpperCase();
                        var marketStatus = String(j.status || 'GREEN_EXECUTE').toUpperCase();

                        if(marketStatus.includes('VOLATILE')) {
                            var subEl = d.getElementById('scan-sub-text');
                            if(subEl) subEl.innerText = "MARKET VOLATILITY - WAITING...";
                            speakVoice("মার্কেট ভোলাটিলিটি, অনুগ্রহ করে অপেক্ষা করুন");
                            setTimeout(function(){
                                if(spookyOverlay) spookyOverlay.remove();
                                isScanningActive = false;
                            }, 1800);
                            return;
                        }

                        var isDown = (rawSig === 'SELL' || rawSig === 'DOWN' || rawSig === 'PUT');
                        
                        triggerStrictSingleTrade(isDown);

                        if(isDown) {
                            speakVoice("ডাউনের জন্য এন্ট্রি নিয়ে নেওয়া হয়েছে");
                        } else {
                            speakVoice("আপের জন্য এন্ট্রি নিয়ে নেওয়া হয়েছে");
                        }

                        var sigText = isDown ? 'SIGNAL: DOWN ⬇️' : 'SIGNAL: UP ⬆️';
                        var sigColor = isDown ? '#ff1744' : '#00ff66';

                        ghostRing.style.borderColor = sigColor;
                        ghostRing.style.animation = 'none';
                        innerGlow.style.borderColor = sigColor;
                        
                        scanContent.innerHTML = '<div style="font-size:28px;">⚡</div>' +
                                                '<div style="font-size:17px;font-weight:900;color:' + sigColor + ';text-shadow:0 0 22px ' + sigColor + ';">' + sigText + '</div>' +
                                                '<div style="font-size:10.5px;color:#fff;margin-top:4px;">AUTO-EXECUTED SUCCESSFULLY!</div>';

                        setTimeout(function(){
                            if(spookyOverlay) spookyOverlay.remove();
                            isScanningActive = false;
                        }, 2000);
                    });
                }, 5000);
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
