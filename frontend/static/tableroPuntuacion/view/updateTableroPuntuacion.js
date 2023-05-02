let wsSocket = new WebSocket("ws://127.0.0.1:8000/score")

function setupCommunication() {
    wsSocket.onopen = (event) => {
        console.log(`[INFO] --- CONNECTION ESTABLISHED ---`)
        console.log("[INFO] - Sending to server");
        wsSocket.send(JSON.stringify({device: "score-promoter"}));
    }
    wsSocket.onmessage = (event) => {
        let response = JSON.parse(event.data)
        let competitor = new Competitor();
        Object.assign(competitor, response)
        updateTableroPuntuacion(competitor)
        sendResponse()
    }

    wsSocket.onclose = (event) => {
        if (event.wasClean) {
            console.log('[INFO] - Connection closed cleanly')
        } else {
            console.log('[INFO] - Connection died')
        }
    }

    wsSocket.onerror = (event) => {
        console.error('[ERROR] - Error in websocket')
    }
}

function sendResponse() {
    wsSocket.send(JSON.stringify({'device': 'score-prompter', 'ack': 'success-prompt'}))
}

function updateTableroPuntuacion(competitor) {
    console.log(`[INFO] - ${competitor}`);
}


setupCommunication()