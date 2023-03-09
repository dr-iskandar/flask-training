from flask import Flask, request
import openai

app = Flask(__name__)

jsreq = ''

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/testing')
def hello_aq():
    return 'Hello, A!'

# @app.route(prefixUrl + '/get-roles', methods = ['POST'])
# @doValidateCredential(request)
# def searchRoleByAppCodeAndName():
# jsreq = request.json
# log = getLogger(__name__)
# log.info(" api searchRoleByAppCodeAndName " + str(jsreq))
# result = rpc.mstRole.searchRoleByAppCodeAndName(json.dumps(jsreq))
# return Response(result, mimetype = 'application/json')

@app.route('/tta', methods = ['POST'])
def texttoanswer():
    openai.api_key= "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"
    jsreq = request.json
    answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": jsreq['text']}
        ]
    )
    realanswer = answer['choices'][0]['message']['content']
    av = addedValue(realanswer)
    return av

def addedValue(val):
    message = val + 'ok'
    return message

@app.route('/wtt', methods = ['POST'])
def wavtotext():
    audio = request.files
    openai.api_key= "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"
    audio_file= open(audio['sound'], "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    answer = tta(transcript["text"])
    # tts(answer["choices"][0]["message"]["content"])
    return answer

def tta(val):
    openai.api_key= "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"
    answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": val}
        ]
    )
    realanswer = answer['choices'][0]['message']['content']
    return realanswer