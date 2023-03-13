from MicroWebSrv2  import *
from time          import sleep
from datetime      import datetime


# ============================================================================
# ============================================================================
# ============================================================================

# TODO: update post-message to do something with internal Python state.
@WebRoute(POST, '/test-post', name='TestPost2/2')
def RequestTestPost(microWebSrv2, request) :
    print('received post')
    data = request.GetPostedURLEncodedForm()
    try :
        test_input = data['test_input']
    except :
        request.Response.ReturnBadRequest()
        return
    content   = """\
    <!DOCTYPE html>
    <html>
        <head>
            <title>POST 2/2</title>
        </head>
        <body>
            <h2>MicroWebSrv2 - POST 2/2</h2>
            You got data %s :)<br />
        </body>
    </html>
    """ % MicroWebSrv2.HTMLEscape(test_input)
    request.Response.ReturnOk(content)


# ============================================================================
# ============================================================================
# ============================================================================

def OnWebSocketAccepted(microWebSrv2, webSocket) :
    """On a newly established web socket, continually send it the time."""
    # TODO: Put onto another thread so it doesn't block other form input.
    while True:
        webSocket.SendTextMessage(datetime.today().strftime("%Y-%m-%d: %H:%M:%S"))
        sleep(1)


wsMod = MicroWebSrv2.LoadModule('WebSockets')
wsMod.OnWebSocketAccepted = OnWebSocketAccepted

mws2 = MicroWebSrv2()
mws2.BindAddress = ('0.0.0.0', 8090)
mws2.RootPath = '.'
mws2.AddDefaultPage('index.html')
mws2.SetEmbeddedConfig()
mws2.NotFoundURL = '/'
mws2.StartManaged()

try :
    while mws2.IsRunning :
        sleep(1)
except KeyboardInterrupt :
    pass

mws2.Stop()