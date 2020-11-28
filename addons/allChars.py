from mitmproxy.http import HTTPFlow
from addons import ArkInterceptor
import json

class allChars(ArkInterceptor):
    '''
        Require: CharsEssential,BattleEssential
    '''
    def __init__(self):
        self.info("Loading success")

    def response(self, flow: HTTPFlow):
        if flow.request.host in self.ServersList and flow.request.path.startswith("/account/syncData"):
            self.info("Receive response")
            data = json.loads(flow.response.get_text())
            char = []
            self.info("Get character list")
            for c in self.tBuilder.cBuilder.characters.keys():
                if "char" in c:
                    char.append(c)
            self.info("add characters.....")
            for c in char:
                self.tBuilder.addCharacter(c)
            data["user"]["troop"] = self.tBuilder.dump()
            flow.response.set_text(json.dumps(data))
            self.info("Complete")