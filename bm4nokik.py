#cd storage
#cd downloads
#cd B
#python3 bm3.py



# -*- coding: utf-8 -*-
from linepy import *
from token import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import  pafy, tweepy, wikipedia, time, timeit, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib3.connection, urllib.parse,antolib,subprocess,unicodedata,GACSender
_session = requests.session()
#from gtts import gTTS
from googletrans import Translator
import youtube_dl
import requests
from pafy import new
from urllib.parse import urlencode
#==============================================================================#
botStart = time.time()
#================EvVcY4Nk9hKiJZYdRMW3.TAVOkm2wqPizxdXz1JiGmW.4QUmFeBLiOjPKtdV7+ddmEw6IuVk/aIHke+OWKLmu/Q===============================================================#
with open('token1.txt','r') as fp:
    #akun = json.load(fp)
    token = fp.read()

try:
    #line = LINE(akun['master'])
    line = LINE(token)
except:
    try:
        line = LINE()
    except:
        try:
            line = LINE()
        except:
            pass
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))
print ("BY: 『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

zxcv = lineMID
oepoll = OEPoll(line)
#call = Call(line)

Rfu = [line]
Exc = [line]
lineMID = line.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
#Kicker01=[m1MID]
#Kickerme=[m1MID]
Family=["ua4a73598979ab61dcf42787b0701f43e",lineMID]
admin=['ua4a73598979ab61dcf42787b0701f43e',lineMID]
adminMID="ua4a73598979ab61dcf42787b0701f43e"
RfuFamily = RfuBot + Family
msg_dict = {}
msg_image={}
msg_video={}
msg_sticker={}
unsendchat = {}
temp_flood = {}
wbanlist = []
wblacklist = []
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
tokenz = {}
setback = ()
#==============================================================================#
ผู้สร้างบอท ="ua4a73598979ab61dcf42787b0701f43e"
#==============================================================================
settings = {
    "MANBOTLINE": True,
    "admin1": {
        "u1b5c2be92de2400509578dfcd211b9ad": True,
        "ua4a73598979ab61dcf42787b0701f43e": True,
    },
    "admin2": False,
    "admin3": False,
    "admin4": False,
    "admin5": False,
    "admin6":{},
    "ของขวัญคนแอด": False,
    #"aotoAddGift": {
        #"setgift": True,
    #},
    "autoAdd": True,
    "autoBlock": False,
    "ตรวจสอบแอด": False,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":3},	
    "autoLeave": True,
    "autoRead": False,
    "autoReply": False,
    "botcancel": False,
    "leaveRoom": False,
    "detectMention": False,
    "checkSticker": False,
    "checkContact": False,
    "checkPost": False,
    "kickMention": False,
    "potoMention": False,
    "delayMention": False,
    "unsendMessage": False,
    "noคิก": False,
    "1คิก": False,
    "2คิก": False,
    "ยกเลิกข้อความ": True,
    "Wc": False,
    "Lv": False,
    "Nk": False,
    "Wcsk": False,
    "Lvsk": False,
    "Nksk": False,
    "Api": False,
    "Aip": False,
    "selfbot": True,
    "blacklist":{},
    "wbanlist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "Mentiongift": False,
    "detectMentionPM": False,
    "dwhitelist": False,
    "gift": {},
    "likeOn": True,
    "lang":"JP",
    "1autolike": True, #autolike
    "autoLike": {
        "comment": "AutoLike by Manbotline",
        "status": True,
    },
    "comment": "Autolike by Manbotline",
    "timeline": False,
    "commentOn":True,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture": [],
    "changePictureProfile": False,
    "changeProfileVideo": False,
    "kickContact": False,
    "changeVideo": False,
    "chatMessage": "dih",
    "unsendMessage": False,
    "autoJoinTicket": False,
    "welcome2":" 􀬁􀅳sparkle􏿿• 􂘁􀄗w􏿿􂘁􀄅e􏿿􂘁􀄌l􏿿􂘁􀄃c􏿿􂘁􀄏o􏿿􂘁􀄍m􏿿􂘁􀄅e􏿿 •􀬁􀅳sparkle􏿿", #   􀬁􀅳sparkle􏿿• 􂘁􀄗w􏿿􂘁􀄅e􏿿􂘁􀄌l􏿿􂘁􀄃c􏿿􂘁􀄏o􏿿􂘁􀄍m􏿿􂘁􀄅e􏿿 •􀬁􀅳sparkle􏿿
    "welcome1":"สวัสดีครับ",
    "welcome":"╔══•⊰✯⊱✴❤✴⊰✯⊱•══╗\n\n        􀄃􀇡moon attracted􏿿สวัสดีสมาชิกใหม่􀄃􀇡moon attracted􏿿\n         🙏ยินดีต้อนรับจร้าาา🙏 \n     􀂗มาแร้วอย่าดื้ออย่าซน􀂗\n 􀂊ทำตัวน่ารักๆอย่าตบตีกันล่ะ􀂊\n 􀂖เข้ามาแล้วแนะนำตัวด้วยนะ􀂖\n 􀄃􀆿brown beloved􏿿สมาชิกใหม่เข้ามาแก้ผ้าจร้า􀄃􀆿brown beloved􏿿\n  􀼂􀆩นาฬิกา􏿿กรุณาปิดแจ้งเตือนด้วยค่าบ􀨁􀅐quiet􏿿\n ╚══•⊰✯⊱✴❤✴⊰✯⊱•══╝", #ข้อความต้อนรับ
    "bye":"╔▬▬▬▬▬▬▬▬▬▬▬╗\n🙏แล้วพบกันใหม่ขอให้โชคดี🙏\n╚▬▬▬▬▬▬▬▬▬▬▬╝\n╔▬▬▬▬▬▬▬▬▬▬▬╗\n i'll see you then. good bye.\n╚▬▬▬▬▬▬▬▬▬▬▬╝\n╔▬▬▬▬▬▬▬▬▬▬▬╗\n aku akan. selamat tinggal.\n╚▬▬▬▬▬▬▬▬▬▬▬╝", #ข้อความคนออกกลุ่ม
    "kick":"คุณยังไม่ได้ตั้งข้อความคนลบ",
    "bye1":"      ✨🇬 🇴 🇴 🇩 🇧 🇾 🇪✨\nไปแล้ว  (｀・ω・´)👀ก็ขอให้โชคดีน๊ะจ๊ะ\n      􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿",
    "คนแอบ":"สวัสดีครับคุณ",
    "join13":"ยินดีที่ได้เข้าร่วมกลุ่ม",
    "Respontag":"แทคบ่อยๆจะติดต่อเรื่องอะไรครับ",
    "eror":"คุณใช้คำสั่งผิด กรุณาศึกษาวิธีใช้ หรือสอบถามกับผู้สร้าง โดยพิมคำสั่ง *.ผส*เพื่อแสดง คท ของผู้สร้าง",
    "คอมเม้น":"""     ─┅═✥By. ℳ₳N ※ ฿✪₮✥═┅─
╭═════════════════╮
║          รับทำเชลบอทกันรัน
║͜͡☆➣(Selfbot)
║͜͡☆➣ไม่เข้าแชตรวม
║͜͡☆➣กันรันได้100%
║͜͡☆➣สามารถตั้งคำแทคได้ด้วตัวเอง
║͜͡☆➣สามารถตั้งตอบรับได้ด้วยตัวเอง
║͜͡☆➣สามารถยกเลิกข้อความได้
║͜͡☆➣สามารถดูคนยกเลิกข้อความได้
║͜͡☆➣สามารถดูคนอ่าน
║͜͡☆➣สามารถสั่งแทคทั้งได้
║͜͡☆➣สามารถแทคกลับทางแชทได้
║͜͡☆➣สามารถป้องกันห้องตัวเองได้
║͜͡☆➣เขียนโดย py3
╰═════════════════╯
╭═══════════════╮
║͜͡☆➣         ᵐᵃⁿ ˡᵒᵛᵉ ˢᵉˡᶠᵇᵒᵗ 
╰═══════════════╯
╭═════════════════╮
║͜͡☆➣แถมฟรีบอท AutoBlock  
╰═════════════════╯
║͜͡☆➣🌷คุณสมบัติ BotAutoBlock🌷
║͜͡☆➣ป้องกันการรันห้องได้100%
║͜͡☆➣ทุกครั้งที่มีการ@เพิ่มเพื่อน
║͜͡☆➣Block Auto Block จะทำงาน
║͜͡☆➣แบบอัตโนมัติ เพื่ิอป้องกันการรันห้อง
║͜͡☆➣กันรันได้100%ครับ
╰═════════════════╯
╭═════════════════╮
*****เซล์ฟบอทเฉพาะเช่ารายเดือนเท่านั้น !!!
  -----------------------------------------------------------

📌📌รับลงบอทป้องกันห้องบอทวี10.7📌📌
👉กันคนบิน
👉กันคนอื่นเชิญมั่ว
👉แก้ดำได้
👉ยัดดำให้คนที่ไม่ชอบได้
👉กันคนเปิดลิ้งกลุ่มได้
👉ดูคนอ่านได้
👉ตั้งแอดมินได้2คน

 ราคากันเองนะจ๊ะ🔙

╰═════════════════╯
╭═════════════════╮ 
║͜͡☆➣🚨งานทำโดยฝีมือคนไทย
║͜͡☆➣ติดต่อได้ที่นี้เลยครับ
║͜͡☆➣ http://line.me/ti/p/~manbotline
╰═════════════════╯
  รันในเชิฟความเร็วของเชลอยู่ 0.04    by. ℳ₳N ※ ฿✪₮""",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "notag": False,
    "pcancel": False,
    "pinvite": False,
    "pmMessage": "ว่างเดี๊ยวเห็นข้อความจะมาตอบน๊ะ",
    "qrp": False,
    "readerPesan": " แอบทมายเดะจิ้มตาบอด",
    "replyPesan": "Sorry , i'm busy right now.",
    "responGc": True,
    "responcall": False,
    "responcallgc": False,
    "restartPoint": "c07540238e0ddffa5187313406f7f3c67",
    "server": "VPS",
    "ksticker": False,
    "userMentioned": False,
    "timeRestart": "18000",
    "message1":"By.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ",
    "message":"By.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ",
#    "comment":"""By.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ""",
    "comment1":"""By.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ""",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "addPesan": "By.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ",
    "addSticker": {
        "name": "",
        "status": False,
    },
    "mentionPesan": " ว่าไง? ที่รัก􀄃􀈻",
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "addSticker": {
                "STKID": "409",
                "STKPKGID": "1",
                "STKVER": "100"
            },
            "leaveSticker": {
                "STKID": "51626533",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "kickSticker": {
                "STKID": "123",
                "STKPKGID": "1",
                "STKVER": "100"
            },
            "readerSticker": {
                "STKID": "51626497",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "responSticker": {
                "STKID": "52002738",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "ติกเกอร์ทัก": {
                "STKID": "51626494",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "sleepSticker": "",
            "welcomeSticker": {
                "STKID": "51626494",
                "STKPKGID": "11538",
                "STKVER": "1"
            }
        }
    },
    "mimic": {
       "copy": False,
       "status": False,
       "target": {}
     #  "target": {"u97155061ad8974b480df9a9de723eacb":True,}
    }
}
RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
    "autoBlock": False,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

botman = {
    "Manbot":True,
    }

wait = {
   "bc": {
    },
}


wait2 = {
    "readPoint":{},
    "readMember":{},
    "readTime": {},
    "setTime":{},
    "ROM":{}
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']
setTime = wait2['setTime']
msg_dict = {}
msg_dict1 = {}
manlovebot = [""]
#===
msg_text={}
msg_text1={}
msg_image={}
msg_tes=[]
msg_video={}
msg_sticker={}
#unsendchat = {}
#temp_flood = {}

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
Kuman = "u6fc71977555896280f337a1094664f5f"
#Kuman1 = "ua4a73598979ab61dcf42787b0701f43e"
#line.findAndAddContactsByMid(Kuman)
line.sendMessage(Kuman,"『เข้าสู่ระบบสำเร็จ』")
#line.findAndAddContactsByMid(Kuman1)
#line.sendMessage(Kuman1,"『เข้าสู่ระบบสำเร็จ』")

#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#==============================================================================================================
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))                        

def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+line.getContact(lineMID).pictureStatus, line.getContact(lineMID).displayName)
                    except Exception as error:
                        logError(error)
                        
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    line.sendMessage(to, '', contentMetadata, 7)

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            line.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
        
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

#=====================================================================

def command(text):
    pesan = text.lower()
    return pesan

def waktu(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days,hours = divmod(hours,24)
	#return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)
	return '╠❂➣ %02d วัน\n╠❂➣ %02d ชั่วโมง \n╠❂➣ %02d นาที \n╠❂➣ %02d วินาที\n╰════════╯' % (days, hours, mins, secs)

def manwaktu(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days,hours = divmod(hours,24)
	return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)
	#return '╠❂➣ %02d วัน\n╠❂➣ %02d ชั่วโมง \n╠❂➣ %02d นาที \n╠❂➣ %02d วินาที\n╰═══════════╯' % (days, hours, mins, secs)

def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': lineMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def cloneProfile(mid):
    contact = line.getContact(mid)
    if contact.videoProfile == None:
        line.cloneContactProfile(mid)
    else:
        profile = line.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        line.updateProfile(profile)
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = line.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = line.getProfileDetail(mid)['result']['objectId']
    line.updateProfileCoverById(coverId)

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def sendMentionV10(to, text,name, url, iconlink):
    line.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })


def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[ชื่อกลุ่ม {} ]\n╠".format(str(line.getGroup(to).name))
        arr = []
        no = 0 + 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[จำนวนคนที่แท็ก {} คน] ".format(str(len(mid)))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False


#==============================================================================#
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)
def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน บอททำงานผิดปกติ ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def myhelp():
    myHelp = """╭─「『ℳ₳N』฿✪₮ᴸᴵᶰᵉ  」─
│• 01. help [คำสั่งเซลบอท]
│• 02. help2 [คำสั่งตั้งค่า]
│• 03. help3 [คำสั่งโซเชล]
│• 04. help4 [คำสั่งเปิด/ปิด]
│• 05. help5 [คำสั่งมิเดีย]
│• 06. help6 [คำสั่งMp3]
│• 07. help7 [คำสั่งภาษา]
│• 08. helpsiri [ชุดคำสั่งบอทสิริ]
│• 09. Set     [เช็คการตั้งค่าบอท]
├───────────
│• BY: 『ℳ₳N』฿✪₮ᴸᴵᶰᵉ
│• line.me/ti/p/~manbotline
╰───────────
"""

    return myHelp
        
        
def myhelp2():
    myHelp2 = """╭─「『ℳ₳N』฿✪₮ᴸᴵᶰᵉ  」─
│• 01. Set「เช็คกาตรั้งค่าเซลบอท」
│• 02. Help2「คำสั่งในกลุ่ม
│• 03. Help3「คำสั่งตั้งค่า」
│• 04. Help4「คำสั่งโซเชล」
│• 05. Help5「คำสั่งพูดMp3」
│• 06. Help6「คำสั่งแปลภาษา」
├───────────
│• 07. ไอดีล่อง「ไอดีคนใส่ล่องหน」
│• 08. คทล่อง「คทคนใส่ล่องหน」
│• 09. แทคล่อง「แทคคนใส่ร่องหน」
│• 10. ปฏิทิน「เช็ควันเวลา」
├───────────
│• 11. Mimic「on/off「」
│• 12. MimicList「ชื่อเลียนแบบ」
│• 13. MimicAdd「@」
│• 14. MimicDel「@」
├───────────
│• 15. ส่งเสียงกลุ่ม「ข้อความ」 
│• 16. ส่งเสียงแชท「ข้อความ」
│• 17. ประกาศกลุ่「ข้อความ」
│• 18. ประกาศแชท「ข้อความ」
├───────────
│• 19. เริ่มใหม่「รีบูสระบบใหม่」
│• 20. เวลออน「เช็คเวลาออน」
│• 21. ตัวเรา
│• 22. เช็ค「เช็คการตั้งค่า」
│• 23. ผส「คท.ผู้สร้าง」
│• 24. ข้อมูล「ข้อมูลตัวเอง」
│• 25. ข้อมูล「@」
│• 26. ไอดี「@」
│• 27. ชื่อ「@」
│• 28. ตัส「@」
│• 29. รูปโปร「@」
│• 30. รูปปก「@」
│• 31. คท「@」
│• 32. วีดีโอโปร「@」
├───────────
│• BY: 『ℳ₳N』฿✪₮ᴸᴵᶰᵉ
│• line.me/ti/p/~
╰───────────
 """
    return myHelp2

def listgrup():
    listGrup = """╭════════════════╮
║─┅═✥ᵐᵃⁿ ˡᵒᵛᵉ ˢᵉˡᶠᵇᵒᵗ✥═┅─
╰════════════════╯
╭════════════════╮
║        ❂➣หมวดเช็คข้อมูล
╠════════════════
╠❂➣ แอด     ➣เช็คคนสร้าง
╠❂➣ ชื่อกลุ่ม  ➣เช็คชื่อห้อง
╠❂➣ ไอดีกลุ่ม ➣เช็คไอดีห้อง
╠❂➣ เปิดลิ้ง   ➣เปิดลิ้งห้อง
╠❂➣ ปิดลิ้ง    ➣ปิดลิ้งห้อง
╠❂➣ ลิ้ง      ➣ขอลิ้งห้อง
╠❂➣ ลิ้งกลุ่ม  ➣ขอลิ้งห้อง
╠❂➣ กลุ่ม    ➣เช็คกลุ่มที่เรามี
╠❂➣ เช็คกลุ่ม @ ➣เช็คกลุ่มร่วม@
╠❂➣ สมาชิกกลุ่ม ➣เช็คสมาชิก
╠❂➣ ข้อมูลกลุ่ม ➣เช็คข้อมูลกลุ่ม
╠❂➣ รูปกลุ่ม    ➣ดึงรูปปกกลุ่ม
╠❂➣ แทค      ➣แทคทั้งกลุ้ม
╠══════════════════
║       ❂➣หมดใช้งานประจำ
╠══════════════════
╠❂➣ เช็คไอดี
╠❂➣ ไอดีล่อง
╠❂➣ คทล่อง
╠❂➣ แทคล่อง
╠❂➣ แทค [จำนวน] @
╠❂➣ คลอ [จำนวน]
╠❂➣ โทร [จำนวน]
╠❂➣ แทคล่อง
╠❂➣ จับ
╠❂➣ เลิกจับ
╠❂➣ จับใหม่
╠❂➣ อ่าน
╠❂➣ ห้ามพิม [ข้อความ]
╠❂➣ ดูห้าม
╠❂➣ ลบห้ามพิม [ข้อความ]
╠❂➣ แจก [จำนวน] @
╠════════════════
║   ❂➣โหมดเปิด/ปิด
╠════════════════
╠❂➣ 🔘เปลี่ยนรูปกลุ่ม
╠❂➣ 🔘เปิด/ปิดแสกน
╠❂➣ 🔘เปิด/ปิดรับแขก
╠❂➣ 🔘เปิด/ปิดส่งแขก
╠❂➣ 🔘เปิด/ปิดทักเตะ
╠❂➣ 🔘เปิด/ปิดพูด
╠❂➣ 🔘เปิด/ปิดตรวจสอบ
╠════════════════
║   🌀❂➣เช็คดำ สั่งดำ ล้างดำ
╠════════════════
╠❂➣ 🔺เช็คดำ
╠❂➣ 🔺ลงดำ
╠❂➣ 🔺ล้างดำ
╠❂➣ 🔺ไล่ดำ
╠❂➣ 🔺คทดำ
╠❂➣ 🔺ปวดตับ
╰════════════════╯
╭════════════════╮
║  🌴🌴『『ℳ₳N』฿✪₮ᴸᴵᶰᵉ  』🌴🌴
╰════════════════╯"""
    return listGrup

def socmedia():
    socMedia = """╭════════════════╮
║─┅═✥ᴛᴇᴀᴍᵀᴴᴬᴵᴸᴬᴺᴰʙᴏᴛLɪɴᴇ✥═┅─
║        ✪ 🅼🅴🅳🅸🅰 ✪
╰════════════════╯
╭════════════════╮
║   🌀❂➣หมวดโซเชี่ยวมีเดัยร์👀
╠════════════════
╠❂➣ 🔹ปฏิทิน
╠❂➣ 🔹รูปภาพ [ชื่อรูปภาพ]
╠❂➣ 🔹ค้นหารูปภาพ [ชื่อรูปภาพ]
╠❂➣ 🔹ยูทูป [ข้อความ]
╠❂➣ 🔹เพลง [ชื่อเพลง]
╠❂➣ 🔹ขอเพลง [ชื่อเพลง]
╠❂➣ 🔹Lyric
╠❂➣ 🔹ScreenshootWebsite
╠❂➣ 🔹หนัง [ชื่อหนัง]
╠❂➣ 🔹วีดีโอ [ชื่อวีดีโอ]
╠❂➣ 🔹รูปการ์ตูน [ชื่อรูป]
╠❂➣ 🔹ไอจี [ชื่อยูส]
╠❂➣ 🔹Urban
╠❂➣ 🔹เพลสโต [ชื่อแอพ]
╠❂➣ 🔹เฟสบุค [ข้อความ]
╠❂➣ 🔹Github[ข้อความ]
╠❂➣ 🔹กูเกิ้ล [ข้อความ]
╰════════════════╯
╭════════════════╮
║  🌴🌴『『ℳ₳N』฿✪₮ᴸᴵᶰᵉ  』🌴🌴
╰════════════════╯"""
    return socMedia

def helpset():
    helpSet = """╭════════════════╮
║   ─┅═✥ᵐᵃⁿ ˡᵒᵛᵉ ˢᵉˡᶠᵇᵒᵗ✥═┅─
╰════════════════╯
╭════════════════╮
║       ❂➣โหมดเช็คตัวบอทเรา
╠════════════════╯
╠❂➣ คท
╠❂➣ ไอดี
╠❂➣ ชื่อ
╠❂➣ ตัส
╠❂➣ รูปโปร
╠❂➣ รูปปก
╠❂➣ วัดรอบ
╠❂➣ Sp
╠════════════════
║   ❂➣หมวดเช็คค่าข้อความ/ติ๊กเก้อร์
╠════════════════
╠❂➣ ทักเข้า
╠❂➣ ติ๊กคนเข้า
╠❂➣ ลบติ๊กคนเข้า
╠❂➣ ทักออก
╠❂➣ ติ๊กคนออก
╠❂➣ ลบติ๊กคนออก
╠❂➣ ทักเตะ
╠❂➣ ติ๊กคนเตะ
╠❂➣ ลบติ๊กคนเตะ
╠❂➣ คอมเม้น
╠❂➣ ข้อความแทค
╠❂➣ ติ๊กคนแทค
╠❂➣ ลบติ๊กคนแทค
╠❂➣ ข้อความแอด
╠❂➣ ติ๊กคนแอด
╠❂➣ ลบติ๊กคนแอด
╠════════════════
║    ❂➣ตั้งค่าข้อความ/ตั้งติ๊กเก้อร์
╠════════════════
╠❂➣ ชื่อ:
╠❂➣ ตัส:
╠❂➣ ทักเข้า:
╠❂➣ ตั้งติ๊กคนเข้า
╠❂➣ ทักออก:
╠❂➣ ตั้งติ๊กออก
╠❂➣ ทักเตะ:
╠❂➣ ตั้งติ๊กเตะ
╠❂➣ ตั้งแทค:
╠❂➣ ตั้งติ๊กแทค
╠❂➣ ตั้งแอด:
╠❂➣ ตั้งติ๊กแอด
╠❂➣ ตั้งทักแชท:
╠❂➣ คอมเม้น:
╠════════════════
║   ❂➣เช็คดำ/บล๊อค/เตะ
╠════════════════
╠❂➣ ออน
╠❂➣ ดำ
╠❂➣ ขาว
╠❂➣ แบ น @
╠❂➣ ลบแบ น @
╠❂➣ เพิ่มเพื่อน @
╠❂➣ ลบรัน
╠❂➣ ดึง
╠❂➣ ทัก [จำนวน] (แชท.สต)
╠❂➣ หวด @
╠❂➣ สอย @
╠❂➣ ลาก่อย @
╠❂➣ ปลิว @
╠❂➣ ดับไฟ
╠❂➣ แปลงโฉม
╠❂➣ เพื่อน
╠❂➣ ไอดีเพื่อน
╠❂➣ Gcancel:(จำนวนสมาชิก)
╰════════════════╯"""
    return helpSet

def helpsetting():
    helpSetting = """╭════════════════╮
║─┅═✥ᴛᴇᴀᴍᵀᴴᴬᴵᴸᴬᴺᴰʙᴏᴛLɪɴᴇ✥═┅─
║  ✪✨ 🆂🅴🆃🆃🅸??🅶?? ✨✪  
╠════════════════
║   🌀❂➣โหมดการป้องกันกลุ่ม👀
╰════════════════╯
╭════════════════╮
╠❂➣ 🔀เปิดกัน/ปิดกัน
╠❂➣ 🔀กันยก/ปิดกันยก
╠❂➣ 🔀กันเชิญ/ปิดกันเชิญ
╠❂➣ 🔀กันลิ้ง/ปิดกันลิ้ง
╠❂➣ 🔀กันเข้า/ปิดกันเข้า
╠❂➣ 🔀เปิดหมด/ปิดหมด
╠❂➣ 🔀เปิดกทม/ปิดกทม
╠❂➣ 🔀เปิดเข้า/ปิดเข้า
╠❂➣ 🔀เปิดออก/ปิดออก
╠❂➣ 🔀เปิดติ๊ก/ปิดติ๊ก
╠❂➣ 🔀เปิดบล็อค/ปิดบล็อค
╠❂➣ 🔀เปิดมุด/ปิดมุด
╠❂➣ 🔀เปิดเผือก/ปิดเผือก
╠❂➣ 🔀เปิดอ่าน/ปิดอ่าน
╠❂➣ 🔀เปิดพูด/ปิดพูด
╠❂➣ 🔀เปิดแทค/ปิดแทค
╠❂➣ 🔀เปิดแทค2/ปิดแทค2
╠❂➣ 🔀เปิดแทค3/ปิดแทค3
╠❂➣ 🔀เปิดแทคเจ็บ/ปิดแทคเจ็บ
╠❂➣ 🔀เปิดคท/ปิดคท
╠❂➣ 🔀เปิดตรวจสอบ/ปิดตรวจสอบ
╠❂➣ 🔀เปิดเช็คโพส/ปิดเช็คโพส
╠❂➣ 🔀เปิดแสกน/ปิดแสกน
╠❂➣ 🔀เปิดรับแขก/ปิดรับแขก
╠❂➣ 🔀เปิดส่งแขก/ปิดส่งแขก
╠❂➣ 🔀เปิดทักเตะ/ปิดทักเตะ
╠❂➣ 🔀เปิดข้อความ/ปิดข้อความ
╠❂➣ 🔀เปิดแทคแชท/ปิดแทคแชท
╰════════════════╯
╭════════════════╮
║  🌴🌴『『ℳ₳N』฿✪₮ᴸᴵᶰᵉ  』🌴🌴
╰════════════════╯"""
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   """╭════════════════╮
║─┅═✥ᴛᴇᴀᴍᵀᴴᴬᴵᴸᴬᴺᴰʙᴏᴛLɪɴᴇ✥═┅─
║     ✪ 🅶🆁🅾🆄🅿 ✪
╰════════════════╯
╭════════════════╮
╠❂➣ af : แอฟริกัน
╠❂➣ sq : อัลเบเนีย
╠❂➣ hy : อาเมเนีย
╠❂➣ bn : เบนจาลี
╠❂➣ zh-cn : จีน
╠❂➣ zh-tw : ใต้หวัน
╠❂➣ cs : เช็ก
╠❂➣ nl : ดัช
╠❂➣ en : อังกฤษ
╠❂➣ en-us : สหรัฐ
╠❂➣ el : กรีก
╠❂➣ id : อินโดนีเซีย
╠❂➣ it : อิตาลี
╠❂➣ ja : ญี่ปุ่น
╠❂➣ ko : เกาหลี
╠❂➣ la : ลาติน
╠❂➣ ro : โรมาเนีย
╠❂➣ ru : รัสเซีย
╠❂➣ sr : เซอเบียร์
╠❂➣ th : ไทย
╠❂➣ vi : เวียดนาม
╰════════════════╯
╭════════════════╮
║  🌴🌴『『ℳ₳N』฿✪₮ᴸᴵᶰᵉ  』🌴🌴
╰════════════════╯

「วิธีใช้ : say-th ผมชื่อแมนนะครับ」"""
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange =    """╭════════════════╮
║─┅═✥ᴛᴇᴀᴍᵀᴴᴬᴵᴸᴬᴺᴰʙᴏᴛLɪɴᴇ✥═┅─
║     ✪ 🅶🆁🅾🆄🅿 ✪
╰════════════════╯
╭════════════════╮
╠❂➣ af : แอฟริกัน
╠❂➣ sq : อัลเบเนีย
╠❂➣ ar : อราบิค
╠❂➣ hy : อาเมเนีย
╠❂➣ bn : บังการี่
╠❂➣ bs : บอสเนีย
╠❂➣ bg : บังแกเรีย
╠❂➣ zh-cn : จีน
╠❂➣ zh-tw : ใต้หวัน
╠❂➣ cs : เช็ก
╠❂➣ nl : ดัช
╠❂➣ en : อังกฤษ
╠❂➣ et : เอสโตเนียน
╠❂➣ el : กรีก
╠❂➣ id : อินโดนีเซีย
╠❂➣ ga : ไอริส
╠❂➣ it : อิตาลี
╠❂➣ ja : ญี่ปุ่น
╠❂➣ kn : แคนาดา
╠❂➣ la : ลาติน
╠❂➣ lv : ลัตเวีย
╠❂➣ ms : มาเลเซีย
╠❂➣ mt : มอลเตส
╠❂➣ mn : มองโกเลีย
╠❂➣ my : พม่า
╠❂➣ fa : เปอร์เซีย
╠❂➣ pt : โปรตุเกศ
╠❂➣ ro : โรมาเนีย
╠❂➣ ru : รัสเซีย
╠❂➣ th : ไทย
╠❂➣ zu : ซูลู
╰════════════════╯
╭════════════════╮
║  🌴🌴『『ℳ₳N』฿✪₮ᴸᴵᶰᵉ  』🌴🌴
╰════════════════╯
 
「วิธีใช้ : tr-th hello」"""
    return helpLanguange
  
def helpsiri():
    helpSiri = """   ╭════════════════╮
║─┅═✥ᴛᴇᴀᴍᵀᴴᴬᴵᴸᴬᴺᴰʙᴏᴛLɪɴᴇ✥═┅─
║       ✪ 🅶🆁🅾🆄🅿 ✪
║  ✪✨ชุดคำสั่งบอทสิริวี10✨✪
╰════════════════╯
╭════════════════╮
╠❂➣ แอด 
╠❂➣ แอดรอง
╠❂➣ ตั่งค่า
╠❂➣ ตั้งแอดรอง
╠❂➣ สลับ
╠❂➣ ปลดแอด
╠❂➣ ทวิทเต้อ
╠❂➣ ย้ายตั๋ว
╠❂➣ บอทกลับ
╠❂➣ ชุดล็อคen
╠❂➣ ชุดล็อคjp
╠❂➣ เพิ่มดำ
╠❂➣ แก้ดำ
╠❂➣ ลบค้างเชิญ
╠❂➣ เปลี่ยนอด
╠❂➣ ปิดลิ้ง
╠❂➣ เปิดลิ้ง
╠❂➣ ตั้งอ่าน
╠❂➣ คนแอบ
╠❂➣ ปิดการเชิญ
╠❂➣ เปิดเชิญ
╠❂➣ ปิดพูด
╠❂➣ เปิดพูด
╠❂➣ รันติก
╠❂➣ ล็อคแอด
╠❂➣ ล็อคชื่อ
╠❂➣ ล็อครูป
╠❂➣ ล็อคเชิญ
╰════════════════╯
╭════════════════╮
║  🌴🌴『『ℳ₳N』฿✪₮ᴸᴵᶰᵉ  』🌴🌴
╰════════════════╯
"""
    return helpSiri

def helpki():
    helpKi =    """                ✰ℳ₳N ※ ฿✪₮✰

╔══════════════┓
║         คำสั่งสำหรับแอดมินBot 
╠══════════════┛
╠❂คท➠ ดูคอนแทคตัวเอง
╠❂นับ➠ ตั้งเวลาดูคนอ่าน
╠❂อ่าน➠ ดูคนอ่าน
╠❂แทค➠ แทคสมาชิกทั้งห้อง
╠❂แอดมิน ➠ ดูรายชื่อแอดมิน
╠❂เปิดลิ้ง ➠ เปิดลิ้งกลุ่ม
╠❂ปิดลิ้ง ➠ ปิดลิ้งกลุ่ม
╠❂Me「@」➠ ดูคอนแทคเพื่อน
╠❂Mid「@」➠ ดูไอดีเพื่อน
╠❂รูป「@」➠ ดูรูปเพื่อน
╠❂ปก「@」➠ ดูปกเพื่อน
╠❂เตะ「@」➠ สั่งบอทเตะ
╠❂เขียน「Text」➠ เขียนคำบนรูป
╠❂ยูทูป「Text」➠ ค้นหายูทูป
╠❂ID「Text」➠ ดูคอนแทคด้วยไอดี
╠❂แมนออก ➠ สั่งแมนออกจากกลุ่ม
╠❂เชคดำ ➠ เช็ครายชื่อดำ
╠❂แอด ➠ ดูผู้สร้างกลุ่ม
╠❂กลุ่ม ➠ ดูข้อมูลกลุ่ม
╚══════════════┛
  http://line.me/ti/p/~manrungrot
              「MANBOTLINE」
"""
    return helpKi

#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                #line.findAndAddContactsByMid(op.param1)
                line.sendMessage("u6fc71977555896280f337a1094664f5f", "『ออโต้แอด』")
                line.sendMessage("u6fc71977555896280f337a1094664f5f", None, contentMetadata={'mid':op.param1}, contentType=13)
                line.sendMessage("u6fc71977555896280f337a1094664f5f", "BY.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                print ("[   5   ]『ออโต้แอด』")
                #line.sendMessage(op.param1, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
        if op.type == 5:
            if settings["autoBlock"] == True:
                line.blockContact(op.param1)
                line.sendMessage("u6fc71977555896280f337a1094664f5f", "『ออโต้บล็อค』")
                line.sendMessage("u6fc71977555896280f337a1094664f5f", None, contentMetadata={'mid':op.param1}, contentType=13)
                line.sendMessage("u6fc71977555896280f337a1094664f5f", "BY..『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                print ("[   5   ]『ออโต้บล๊อค』")
        #if op.type == 5:
            #if settings["ของขวัญคนแอด"] == True:
                #line.sendMessage(op.param1, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                #line.sendMessage(op.param1, None, contentMetadata={'mid':"u6fc71977555896280f337a1094664f5f"}, contentType=13)
                #line.sendMessage(op.param1, "🎁จากเพจ 『ℳ₳N』฿✪₮ᴸᴵᶰᵉ ☝ ครับ🎁\n💞ฝาก@เพื่อน กดติดดาว🌟ฝากไลค์ ฝากแชร์ให้ด้วยนะครับ ขอบคุณมากๆครับ😘")
                #print ("[   5   ]『ของขวัญคนแอด』")
            #msgSticker = settings["messageSticker"]["listSticker"]["addSticker"]
            #if msgSticker != None:
                #sid = msgSticker["STKID"]
                #spkg = msgSticker["STKPKGID"]
                #sver = msgSticker["STKVER"]
                #sendSticker(op.param1, sver, spkg, sid)
        if op.type == 5:
            if settings["ตรวจสอบแอด"] == True:

            #try:
                line.sendText(op.param1,"ระบบกำลังตรวจสอบบัญชีของคุณ กรุณารอสักครู่...")
                you = op.param1
                G = line.getGroupIdsJoined()
                cgroup = line.getGroups(G)
                ngroup = ""
                for x in range(len(cgroup)):
                    gMembMids = [contact.mid for contact in cgroup[x].members]
                    if you in gMembMids:
                        ngroup += "\n➢ " + cgroup[x].name + " | สมาชิก: " + str(len(cgroup[x].members)) + "คน"
                if ngroup == "":
                    line.sendMessage(op.param1, "「 ไม่พบกลุ่มที่อยู่ร่วมกัน 」")
                    line.blockContact(op.param1)
                    line.sendMessage(Kuman, "『ออโต้บล็อค』")
                    line.sendMessage(Kuman, None, contentMetadata={'mid':op.param1}, contentType=13)
                    line.sendMessage(Kuman, "BY..『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                    print ("[   5   ]『ออโต้บล๊อค』")
                else:
                    line.sendMessage(op.param1, "              「 กลุ่มที่อยู่ร่วมกัน 」              \n %s\n "%(ngroup))
                    line.sendMessage(Kuman, "『ออโต้แอด』")
                    line.sendMessage(Kuman, None, contentMetadata={'mid':op.param1}, contentType=13)
                    line.sendMessage(Kuman, "BY.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                    line.sendText(op.param1,str(settings["คอมเม้น"]))
                    print ("[   5   ]『ออโต้แอด』")
            #    AutoAdd()
         #   except:
         #       pass
        #    try:
           #     time.sleep(0.5)
                #line.sendMessage(Kuman,"มีคนแอดตัวนี้มา  contact ด้านล่างนี้เลย")
                #line.sendMessage(Kuman, None, contentMetadata={'mid': op.param1}, contentType=13)
                #line.sendText(op.param1,str(settings["คอมเม้น"]))
                #line.sendMessage("u6fc71977555896280f337a1094664f5f", "『ออโต้แอด』")
                #line.sendMessage("u6fc71977555896280f337a1094664f5f", None, contentMetadata={'mid':op.param1}, contentType=13)
                #line.sendMessage("u6fc71977555896280f337a1094664f5f", "BY.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
        #        print ("[   5   ]『ออโต้』[   5   ]")
           # except Exception as error:
       ##         logError(error)
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                            print ("[   13   ]『ยกเชิญห้องรัน』")
                        else:
                            line.acceptGroupInvitation(op.param1)
                            print ("[   13   ]『ยกเชิญห้องรัน』")
                    else:
                        line.acceptGroupInvitation(op.param1)
                        print ("[   13   ]『ยกเชิญห้องรัน』")
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
                        print ("[   13   ]『ยกเชิญห้องรัน』")
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)
                    print ("[   13   ]『ยกเชิญห้องรัน』")

        if op.type == 19:
            contact1 = line.getContact(op.param2)
            group = line.getGroup(op.param1)
            contact2 = line.getContact(op.param3)
            print(("[19] กลุ่มชื่อ: " + str(group.name) + "\n" + op.param1 +"\nคนเตะ: " + contact1.displayName + "\nMid:" + contact1.mid + "\nผู้ถูกเตะ: " + contact2.displayName + "\nMid:" + contact2.mid ))
            if RfuProtect["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
                        line.sendMessage(op.param1, "คนเตะมีดังนี้！")
                        line.sendContact(op.param1,op.param2)
                        time.sleep(0.1)
                        line.sendMessage(op.param1, "ผู้ที่ถูกเตะมีดังนี้！")
                        line.sendContact(op.param1,op.param3)
                    else:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    line.sendMessage(op.param1, "คนเตะ！")
                    line.sendContact(op.param1,op.param2)
                    time.sleep(0.1)
                    line.sendMessage(op.param1, "ผู้ที่ถูกเตะ！")
                    line.sendContact(op.param1,op.param3)
                else:
                    pass
        if op.type == 15:
            #print ("[ 15 ]  NOTIFIED LEAVE GROUP")
            if settings["Lvsk"] == True:
                if "{gname}" in settings['bye']:
                    gName = line.getGroup(op.param1).name
                    msg = settings['bye'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        if op.type == 19:
            if settings["Nksk"] == True:
                if "{gname}" in settings['kick']:
                    gName = line.getGroup(op.param1).name
                    msg = settings['kick'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        if op.type == 17:
            #print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["Wcsk"] == True:
                if "{gname}" in settings['welcome']:
                    gName = line.getGroup(op.param1).name
                    msg = settings['welcome'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = line.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 line.sendText(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 line.sendText(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 line.sendText(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     line.findAndAddContactsByMid(target)
                                     line.inviteIntoGroup(msg.to,[target])
                                     line.sendText(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         line.findAndAddContactsByMid(invite)
                                         line.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         line.sendText(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break
#        if op.type == 25:
#            msg = op.message
#            if msg.contentType == 16:
#                url = msg.contentMetadata["postEndUrl"]
#                line.like(url[25:58], url[66:], likeType=1001)
#                line.comment(url[25:58], url[66:], settings["comment"])
#        if op.type == 26:
#            msg = op.message
#            if msg.contentType == 16:
#                url = msg.contentMetadata["postEndUrl"]
#                line.like(url[25:58], url[66:], likeType=1001)
#                line.comment(url[25:58], url[66:], settings["comment"])
#===============
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["admin2"] == True:
                    if msg.contentMetadata["mid"] in settings["admin6"]:
                        line.sendText(msg.to,"รับทราบ")
                        settings["admin2"] = False
                    else:
                        settings["admin6"][msg.contentMetadata["mid"]] = True
                        settings["admin2"] = False
                        line.sendText(msg.to,"decided not to comment")
               elif settings["admin3"] == True:
                   if msg.contentMetadata["mid"] in settings["admin6"]:
                        del settings["admin6"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"ลบจากรายการที่ถูกแบนแล้ว")
                        settings["admin3"] = False
                   else:
                        settings["admin3"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif settings["admin4"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["admin1"]:
                        line.sendText(msg.to,"Sudah Ada")
                        settings["admin4"] = False
                   else:
                        settings["admin1"][msg.contentMetadata["mid"]] = True
                        settings["admin4"] = False
                        line.sendText(msg.to,"➠ เพิ่มบัญชีนี้ในรายชื่อแอดมินแล้ว")
               elif settings["admin5"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["admin1"]:
                        del settings["admin1"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"➠ ลบบัญชีนี้ในรายชื่อแล้ว")
                        settings["admin5"] = False
                   else:
                        settings["admin5"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
#========================================================================
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendText(msg.to,"รับทราบ")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendText(msg.to,"decided not to comment")

               elif settings["dblack"] == True:
                   if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"ลบจากรายการที่ถูกแบนแล้ว") #, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        settings["dblack"] = False

                   else:
                        settings["dblack"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendText(msg.to,"Sudah Ada")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว") #, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

               elif settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว") #, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        settings["dblacklist"] = False

                   else:
                        settings["dblacklist"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
       # if op.type == 26:
#            if settings ["mutebot2"] == True:
           # msg = op.message
           # try:
               # if msg.toType == 0:
                  #  line.log("[%s]"%(msg._from)+str(msg.text))
               # else:
                  #  group = line.getGroup(msg.to)
                    #contact = line.getContact(msg._from)
                  #  line.log("[%s]"%(msg.to)+"\nGroupname: "+str(group.name)+"\nNamenya: "+str(contact.displayName)+"\nPesannya: "+str(msg.text))
               # if msg.contentType == 0:
            #Save message to dict
                    #msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                #if msg.contentType == 7:
                    #stk_id = msg.contentMetadata['STKID']
                    #stk_ver = msg.contentMetadata['STKVER']
                   # pkg_id = msg.contentMetadata['STKPKGID']
                    #ret_ = "="
                    #ret_ += "\nSTICKER ID : {}".format(stk_id)
                  #  ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                    #ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                    #ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                    #ret_ += "\n"
                    #msg_dict[msg.id] = {"text":str(ret_),"from":msg._from,"createdTime":msg.createdTime}
            #except Exception as e:
                #print(e)                    
        if op.type == 25:
          if settings ["MANBOTLINE"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver

                if msg.contentType == 0:
                    if msg.toType == 0:
                        if msg._from in lineMID:
                            if text.lower() == 'เชคกลุ่ม':
                                G = line.getGroupIdsJoined()
                                cgroup = line.getGroups(G)
                                ngroup = ""
                                for x in range(len(cgroup)):
                                    gMembMids = [contact.mid for contact in cgroup[x].members]
                                    if receiver in gMembMids:
                                        ngroup += "\n➢ " + cgroup[x].name + " | สมาชิก: " + str(len(cgroup[x].members))    
                                if ngroup == "":
                                    line.sendMessage(to, "「 ไม่พบกลุ่มที่อยู่ร่วมกัน 」")
                                else:
                                    line.sendMessage(to, "「 กลุ่มที่อยู่ร่วมกัน 」 %s\n\n BY.MANBOTLINE"%(ngroup))
				

            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if ".พูด " in msg.text.lower():
                    spl = re.split(".พูด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'help':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    myHelp = myhelp()
                    #line.sendFooter(to, str(myHelp),link ,icon,name)
                    line.sendMentionFooter(to, str(myHelp) + "\n「ผู้สร้างบอท」:", ผู้สร้างบอท, "https://line.me/ti/p/~manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(ผู้สร้างบอท).pictureStatus, line.getContact(ผู้สร้างบอท).displayName);line.sendMessage(to, line.getContact(ผู้สร้างบอท).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(ผู้สร้างบอท).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manbotline', 'type': 'mt', 'subText': "MANBOTLINE", 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manbotline', 'i-linkUri': 'https://line.me/ti/p/~manbotline', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~manbotline'}, contentType=19)
                    #msg.contentType = 13
                    #msg.contentMetadata = {'mid': msg._from}
                    #contact = line.getContact(sender)
                    #line.sendMessage(to, '{}'.format(contact.displayName),contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manrungrot', 'type': 'mt', 'subText': "{}".format(contact.statusMessage), 'a-installUrl': 'https://line.me/ti/p/~manrungrot', 'a-installUrl': 'https://line.me/ti/p/~manrungrot', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manrungrot', 'i-linkUri': 'https://line.me/ti/p/~manrungrot', 'id': 'mt000000000a6b79f9', 'text': '{}'.format(contact.displayName), 'linkUri': 'https://line.me/ti/p/~manrungrot'}, contentType=19)
                    print ("[  Help  ]『ขอความช่วยเหลือ』")
                    #line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                if text.lower() == 'help1':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    myHelp1 = myhelp2()
                    line.sendFooter(to, str(myHelp1),link ,icon,name)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    print ("[  Help 1 ]『ขอความช่วยเหลือ』")
                elif text.lower() == 'help2':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    helpSet = helpset()
                    #line.sendFooter(to, str(helpSet),link ,icon,name)
                    line.sendMentionFooter(to, str(helpSet) + "\n「ผู้สร้างบอท」:", ผู้สร้างบอท, "https://line.me/ti/p/~manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(ผู้สร้างบอท).pictureStatus, line.getContact(ผู้สร้างบอท).displayName);line.sendMessage(to, line.getContact(ผู้สร้างบอท).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(ผู้สร้างบอท).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manbotline', 'type': 'mt', 'subText': "MANBOTLINE", 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manbotline', 'i-linkUri': 'https://line.me/ti/p/~manbotline', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~manbotline'}, contentType=19)
                    #line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    print ("[  Help 2 ]『ขอความช่วยเหลือ』")
                elif text.lower() == 'helpsiri':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    helpSiri = helpsiri()
                    line.sendFooter(to, str(helpSiri),link ,icon,name)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    print ("[  Help Siri ]『ขอความช่วยเหลือ』")
                elif text.lower() == 'help3':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    listGrup = listgrup()
                    line.sendFooter(to, str(listGrup),link ,icon,name)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    print ("[  Help 3 ]『ขอความช่วยเหลือ』")
                elif text.lower() == 'help4':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    helpSetting = helpsetting()
                    line.sendFooter(to, str(helpSetting),link ,icon,name)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    print ("[  Help 4 ]『ขอความช่วยเหลือ』")
                elif text.lower() == 'help5':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    socMedia = socmedia()
                    line.sendFooter(to, str(socMedia),link ,icon,name)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    print ("[  Help 5 ]『ขอความช่วยเหลือ』")
                elif text.lower() == 'help6':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    helpTextToSpeech = helptexttospeech()
                    line.sendFooter(to, str(helpTextToSpeech),link ,icon,name)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    print ("[  Help 6 ]『ขอความช่วยเหลือ』")
                elif text.lower() == 'help7':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    helpLanguange = helplanguange()
                    line.sendFooter(to, str(helpLanguange),link ,icon,name)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    print ("[  Help 7 ]『ขอความช่วยเหลือ』")
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'สปีด':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")

                elif "##Sp" in msg.text:
                    line.sendText(msg.to, "🇹🇭ประมวลผลความเร็ว🇹🇭....")
                    start = time.time()
                    time.sleep(0.00000000001)
                    elapsed_time = time.time() - start
                    line.sendText(msg.to, "%sseconds" % (elapsed_time))    
                    print ("Speed")

                elif msg.text in ["Sp","sp"]:
                    start = time.time()
                    line.sendText(receiver, "「 ทดสอบความเร็วของบอท 」")
                    elapsed_time = time.time() - start
                    line.sendText(receiver,"[ %.4f วินาที ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                    print ("[ Sp ] ทดสอบความแร็วบอท")

                elif msg.text in ["เทสสปีด"]:
                    #start = time.time()
                    #elapsed_time = time.time() - start
                    line.sendMessage(to,"「 ทดสอบความเร็วของบอท 」")
                    line.sendMessage(to,"▒...0%")  
                    line.sendMessage(to,"█▒... 10.0%")       
                    line.sendMessage(to,"██▒... 20.0%")
                    line.sendMessage(to,"███▒... 30.0%")
                    line.sendMessage(to,"████▒... 40.0%")
                    line.sendMessage(to,"█████▒... 50.0%")
                    line.sendMessage(to,"██████▒... 60.0%")
                    line.sendMessage(to,"███████▒... 70.0%")
                    line.sendMessage(to,"████████▒... 80.0%")
                    line.sendMessage(to,"█████████▒... 90.0%")
                    #line.sendMessage(to,"███████████..100.0%")                    
                    #line.sendMessage(to,"บอทยังทำงานปรกติน๊ะจ๊ะ\n™─┅❈͜͡✯ʙᴀsʙᴏᴛʟɪɴᴇ✯͜͡❈┅─")
                    start = time.time()
                    line.sendMessage(to,"███████████..100.0%")
                    elapsed_time = time.time() - start
                    line.sendText(receiver,"[ %.4f วินาที ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                    print ("[ เทสสปีด ] ทดสอบความแร็วบอท")

                elif msg.text in ["ผู้สร้าง","ผส","ทีมงาน"]:
                    line.sendMentionFooter(to,"「ผู้สร้างเซลบอท」:", ผู้สร้างบอท, "https://line.me/ti/p/~manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(ผู้สร้างบอท).pictureStatus, line.getContact(ผู้สร้างบอท).displayName);line.sendMessage(to, line.getContact(ผู้สร้างบอท).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(ผู้สร้างบอท).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manbotline', 'type': 'mt', 'subText': "MANBOTLINE", 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manbotline', 'i-linkUri': 'https://line.me/ti/p/~manbotline', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~manbotline'}, contentType=19)

                elif text.lower() == 'รีบอท':
                    line.sendMessage("u1b5c2be92de2400509578dfcd211b9ad", "Restarting....")
                    line.sendMessage(to, "    กำลังรีสตาทบอท ... โปรดรอสักครู่ ..", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    line.sendMessage(to, "Success Restarting....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    restartBot()

                elif ".บัญชี" == msg.text.lower():
                    line.sendMessage(to, """╔══•⊰✯⊱✴❤✴⊰✯⊱•══╗
                    พร้อมเพย์
                 0821464951

           บัญชีธนาคารกรุงเทพ
               749-0-28582-7

                     ชื่อบัญชี
        นายรุ่งโรจน์ เหล็กอยู่มะดัน
 ╚══•⊰✯⊱✴❤✴⊰✯⊱•══╝""")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': msg._from}
                    contact = line.getContact(sender)
                    line.sendMessage(to, '{}'.format(contact.displayName),contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manrungrot', 'type': 'mt', 'subText': "{}".format(contact.statusMessage), 'a-installUrl': 'https://line.me/ti/p/~manrungrot', 'a-installUrl': 'https://line.me/ti/p/~manrungrot', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manrungrot', 'i-linkUri': 'https://line.me/ti/p/~manrungrot', 'id': 'mt000000000a6b79f9', 'text': '{}'.format(contact.displayName), 'linkUri': 'https://line.me/ti/p/~manrungrot'}, contentType=19)
                elif ".บัญชี1" == msg.text.lower():
                    line.sendMessage(to, """╔══•⊰✯⊱✴❤✴⊰✯⊱•══╗
                    พร้อมเพย์
              1300600194367

           บัญชีธนาคารกรุงไทย
               323-0-31746-7

                     ชื่อบัญชี
        นายรุ่งโรจน์ เหล็กอยู่มะดัน
 ╚══•⊰✯⊱✴❤✴⊰✯⊱•══╝""")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': msg._from}
                    contact = line.getContact(sender)
                    line.sendMessage(to, '{}'.format(contact.displayName),contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manrungrot', 'type': 'mt', 'subText': "{}".format(contact.statusMessage), 'a-installUrl': 'https://line.me/ti/p/~manrungrot', 'a-installUrl': 'https://line.me/ti/p/~manrungrot', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manrungrot', 'i-linkUri': 'https://line.me/ti/p/~manrungrot', 'id': 'mt000000000a6b79f9', 'text': '{}'.format(contact.displayName), 'linkUri': 'https://line.me/ti/p/~manrungrot'}, contentType=19)

                if text.lower() == 'ออน':
                    eltime = time.time() - mulai
                    van = "╭════════╮\n║ระยะเวลาการทำงาน\n╠════════\n"+waktu(eltime)
                    #line.sendMessage(receiver,van)
                    line.sendMentionFooter(to,van + "\n\n     「ผู้สร้างบอท」:\n", ผู้สร้างบอท, "https://line.me/ti/p/~manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(ผู้สร้างบอท).pictureStatus, line.getContact(ผู้สร้างบอท).displayName);line.sendMessage(to, line.getContact(ผู้สร้างบอท).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(ผู้สร้างบอท).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manbotline', 'type': 'mt', 'subText': "MANBOTLINE", 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manbotline', 'i-linkUri': 'https://line.me/ti/p/~manbotline', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~manbotline'}, contentType=19)


                if text.lower() == '!ออน':
                    eltime = time.time() - mulai
                    van = "    ระยะเวลาการทำงานของบอท :\n"+manwaktu(eltime)
                    #line.sendMessage(receiver,van)
                    line.sendMentionFooter(to,van + "\n\n「ผู้สร้างบอท」:", ผู้สร้างบอท, "https://line.me/ti/p/~manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(ผู้สร้างบอท).pictureStatus, line.getContact(ผู้สร้างบอท).displayName);line.sendMessage(to, line.getContact(ผู้สร้างบอท).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(ผู้สร้างบอท).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manbotline', 'type': 'mt', 'subText': "MANBOTLINE", 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manbotline', 'i-linkUri': 'https://line.me/ti/p/~manbotline', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~manbotline'}, contentType=19)


                elif "##runtime" == msg.text.lower():
                    line.sendMessage(to, "╭═══════════╮\n║   👀RunTime👀\n╠═══════════\n╠❂➣ 00「ปี」\n╠❂➣ 00「เดือน」\n╠❂➣ 00「วัน」\n╠❂➣ 03「ชั่วโมง」\n╠❂➣ 32「นาที」\n╠❂➣ 05「วิ」\n╰═══════════╯")

                elif text.lower() == '.ออน':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทสาสบาส"                   
                    link = "https://line.me/ti/p/FMRCTkb0nl"
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "ระยะเวลาการทำงานของบอท {}".format(str(runtime),link ,icon,name))
                elif text.lower() == '.ข้อมูล':
                    try:
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "คำสั่งบอทสาสบาส"                   
                        link = "https://line.me/ti/p/FMRCTkb0nl"
                        arr = []
                        owner = adminMID
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ ™❍✯͜͡『✯ʙᴀsʙᴏᴛʟɪɴᴇ✯』✯͜͡❂➣]"
                        ret_ += "\n╠۞➢ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠۞➢ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠۞➢ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠۞➢บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠➢➢➢[สถานะ] ═ {}".format(contact.statusMessage)
                        ret_ += "\n╠۞➢ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[ ™❍✯͜͡『✯ʙᴀsʙᴏᴛʟɪɴᴇ✯』✯͜͡❂➣]"
                        line.sendContact(to, owner)
                        line.sendFooter(to, str(ret_),link ,icon,name)
                        line.sendMentionFooter(to, '「ผู้สร้างบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#===================================                
                elif msg.text in ["จุด","นับ"]:
                    line.sendMessage(msg.to, "➠ จุดตั้งเวลาดูคนอ่าน")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("นับ")
                elif msg.text in ["อ่าน"]:
                    if msg.to in wait2['readPoint']:
                        print ("อ่าน")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        #line.sendText(msg.to, "😁รายชื่อคนที่อ่าน😁%s\n\n😆รายชื่อคนที่อ่าน😆\n%s\nสั่งนับเวลา[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        line.sendText(msg.to, "           [ By. ℳ₳N ※ ฿✪₮]%s\n          🌟รายชื่อคนที่อ่าน🌟\n%s\n🌹🌹สั่งนับเมื่อเวลา[%s]🌹🌹" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        line.sendMessage(msg.to, "ไม่สามารถทำการอ่านได้กรุณาพิม➠ นับ")

                elif 'ไอดี: ' in msg.text:
                  if botman["Manbot"] == True:
                   if msg._from in admin:
                      msgs = msg.text.replace('ไอดี: ','')
                      conn = line.findContactsByUserid(msgs)
                      if True:
                          line.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                          line.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)


#=============  Botkicker  ==============
                elif msg.text in ["โทเคน"]:
                  if botman["Manbot"] == True:
                   if msg._from in admin:
                       line.sendMessage(msg.to,"ผม\n\n"+line.authToken)
                       line.sendMessage(msg.to,"คิก1\n\n"+m1.authToken)
                       #line.sendMessage(msg.to,"คิก2\n\n"+m2.authToken)
                       #line.sendMessage(msg.to,"คิก3\n\n"+m3.authToken)
                       #line.sendMessage(msg.to,"คิก4\n\n"+m4.authToken)
                elif text.lower() == "ลบแชท1":
                  if botman["Manbot"] == True:
                    if msg._from in admin:
                       try:
                           line.removeAllMessages(op.param2)
                           line.sendMessage(to, "➠ ลบแชทสำเร็จแล้ว")
                           #m2.removeAllMessages(op.param2)
                           #m2.sendMessage(to, "➠ 2ลบแชทสำเร็จแล้ว")
                           #kc.removeAllMessages(op.param2)
                           #kc.sendMessage(to, "➠ 3ลบแชทสำเร็จแล้ว")
                           #ke.removeAllMessages(op.param2)
                           #ke.sendMessage(to, "➠ 4ลบแชทสำเร็จแล้ว")
                       except:
                           pass
                elif '1?' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])           
                               print ("สั่งคิก1เตะ")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")

                elif text.lower() == '/set0':
                    if msg._from in admin:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("/set0","")
                            gs = line.getGroup(msg.to)
                            #gs = m1.getGroup(msg.to)
                            #line.sendMessage(msg.to,"「 ขอต้อนรับสู่ห้องว่าง 」")
     #                       line.sendMessage(msg.to,"「 ขอต้อนรับสู่ห้องว่าง 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                line.sendMessage(msg.to,"ปีกหักอ่ะ555")
                            else:
                                for target in targets:
                                    if not target in bot1:
                                        if not target in RfuBot:
                                            if not target in settings["admin1"]:
                                                try:
                                                    random.choice(Exc).kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    pass
                                                    #line.sendMessage(msg.to,"Byeeee..") 

                elif msg.text in ["เพิ่มแอด"]:
                  if msg._from in admin: 
                    settings["admin4"] = True
                    line.sendText(msg.to,"➠ กรุณาส่งคอทแทค")
                elif msg.text in ["ลบแอด"]:
                  if msg._from in admin: 
                    settings["admin5"] = True
                    line.sendText(msg.to,"➠ กรุณาส่งคอทแทค")
                elif msg.text in ["คทแอดมิน",".เชคแอดมิน"]:
                    if msg._from in lineMID:
                        if settings["admin1"] == []:
                            line.sendMessage(to, "Nothing boss")
                        else:
                            for bl in settings["admin1"]:
                                line.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif msg.text in ["แอดมิน","เชคแอดมิน","Listadmin"]:
                  if botman["Manbot"] == True:
                    if msg._from in admin:
                        ma = ""
                        mb = ""
                        mc = ""
                        a = 0
                        b = 0
                        c = 0
                        for m_id in settings["admin1"]:
                            b = b + 1
                            end = '\n'
                            mb += str(b) + ". " +line.getContact(m_id).displayName + "\n"
                        #line.sendMessage(msg.to,"💻 BOT admin\n\nAdmin:\n"+mb+"\nTotal「%s」Admin" %(str(len(admin))))
                        #line.sendMessage(msg.to,"💻 BOT admin\n\nAdmin:\n"+mb+"\nTotal「%s」Admin" %(str(len(settings["admin1"]))))
                        line.sendMessage(msg.to,"    「 รายชื่อแอดมิน 」\n\n"+mb+"\n   จำนวน「%s」แอดมิน" %(str(len(settings["admin1"]))))
#=================
                elif "ขอรูป " in msg.text:
                   # txt = msg.text.replace("Tx: ", "")
                    try:
                        #search = cmd.replace("ขอรูป ","")
                        search = msg.text.replace("ขอรูป ", "")
                        r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(search))
                        data = r.text
                        data = json.loads(data)
                        if data["content"] != []:
                            items = data["content"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                    except Exception as error:
                         logError(error)
                         var= traceback.print_tb(error.__traceback__)
                         line.sendMessage(to,str(var))
                elif msg.text.lower() == 'ลิ้งกลุ่ม':
                  if botman["Manbot"] == True:
                        if msg.toType == 2:
                           x = line.getGroup(msg.to)
                           if x.preventedJoinByTicket == True:
                              x.preventedJoinByTicket = False
                              line.updateGroup(x)
                           gurl = line.reissueGroupTicket(msg.to)
                           line.sendMessage(msg.to, "ชื่อกลุ่ม : "+str(x.name)+ "\nลิ้งกลุ่ม : http://line.me/R/ti/g/"+gurl)

#=============
                elif 'ทัก: ' in msg.text:
                  if botman["Manbot"] == True:
                   if msg._from in admin:
                      korban = msg.text.replace('ทัก: ','')
                      korban2 = korban.split()
                      midd = korban2[0]
                      jumlah = int(korban2[1])
                      if jumlah <= 1000:
                          for var in range(0,jumlah):
                              msgSticker = settings["messageSticker"]["listSticker"]["ติกเกอร์ทัก"]
                              if msgSticker != None:
                                  sid = msgSticker["STKID"]
                                  spkg = msgSticker["STKPKGID"]
                                  sver = msgSticker["STKVER"]
                                  sendSticker(midd, sver, spkg, sid)

#=================#[Unsend Messages]==================#

        #        elif msg.text.lower().startswith("ยก "):
        #            args = msg.text.lower().replace("ยก ","")
          #          mes = 0
             #       try:
          #              mes = int(args[1])
            #        except:
               #         mes = 100
                #        M = line.getRecentMessagesV2(to, 100)
               #         MId = []
             #           for ind,i in enumerate(M):
               #             if ind == 0:
                        #        pass
                #            else:
                   #             if i._from == line.profile.mid:
                       #             MId.append(i.id)
                             #       if len(MId) == mes:
                         #               break
                    #    def unsMes(id):
                      #      line.unsendMessage(id)
                     #   for i in MId:
                      #      thread1 = threading.Thread(target=unsMes, args=(i,))
                    #        thread1.start()
                   #         thread1.join()
                  #      line.sendMessage(to, ' 「 กำลังยกเลิก 」\nยกเลิกทั้งหมด {} ข้อความ'.format(len(MId)))                               

#=================#[Unsend Messages]==================#
                elif "ยกเริก" in msg.text:
                    #args = cmd.replace("ยกเริก ","")
                    args = msg.text.replace("ยกเริก ", "")
                    mes = 0
                    try:
                        mes = int(args[1])
                    except:
                        mes = 1
                    M = line.getRecentMessagesV2(to,101)
                    MId = []
                    for ind,i in enumerate(M):
                        if ind == 0:
                            pass
                        else:
                            if i._from == line.profile.mid:
                                MId.append(i.id)
                                if len(MId) == mes:
                                    break
                    def unsMes(id):
                        line.unsendMessage(id)
                    for i in MId:
                        thread1 = threading.Thread(target=unsMes, args=(i,))
                        thread1.start()
                        thread1.join()
                    #line.sendMessage(to, '「 ได้ยกเลิกข้อความแล้ว 」\nจำนวนที่ยกเลิก {} ข้อความ'.format(len(MId)))
         

#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "╭════[ ᵐᵃⁿ ˡᵒᵛᵉ ˢᵉˡᶠᵇᵒᵗ ]\n╠═══════════════\n║              『เช็คค่า』\n╠═══════════════"
                        if settings["autoAdd"] == True: ret_ += "\n╠۞➣● ออโต้แอด[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ออโต้แอด[ ᴏғғ ]"
                        if settings["autoBlock"] == True: ret_ += "\n╠۞➣● ออโต้บล็อค[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ออโต้บล็อค[ ᴏғғ ]"
                        if settings["ตรวจสอบแอด"] == True: ret_ += "\n╠۞➣● ออโต้ตรวจสอบแอด[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ออโต้ตรวจสอบแอด[ ᴏғғ ]"
                        if settings["ของขวัญคนแอด"] == True: ret_ += "\n╠۞➣● ของขวัญเพิ่มเพื่อน[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ของขวัญเพิ่มเพื่อน[ ᴏғғ ]"
                        if settings["autoJoinTicket"] == True: ret_ += "\n╠۞➣● มุดลิ้ง[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ มุดลิ้ง[ ᴏғғ ]"
                        if settings["autoJoin"] == True: ret_ += "\n╠۞➣● เข้าห้องออโต้ [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ เข้าห้องออโต้[ ᴏғғ ]"
                        ret_ += "\n╠═[☆ โหมดแสกนคำพูด ☆]════"
                        if settings["Api"] == True: ret_ += "\n╠۞➣● บอท api[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ บอท api[ ᴏғғ ]"
                        if settings["Aip"] == True: ret_ += "\n╠۞➣● แสกนคำพูด+คำสั่งบิน[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ แสกนคำพูด+คำสั่งบิน[ ᴏғғ ]"
                        ret_ += "\n╠═[ ☆ เปิด/ปิดข้อความ ☆ ]════"
                        if settings["Wc"] == True: ret_ += "\n╠۞➣● ข้อความต้อนรับสมาชิก [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ข้อความต้อนรับสมาชิก[ ᴏғғ ]"
                        if settings["Lv"] == True: ret_ += "\n╠۞➣● ข้อความอำลาสมาชิก [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ข้อความอำลาสมาชิก[ ᴏғғ ]"
                        if settings["Nk"] == True: ret_ += "\n╠۞➣● ข้อความแจ้งเตือนคนลบ ื[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ข้อความแจ้งเตือนคนลบ[ ᴏғғ ]"
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠۞➣● ปฏิเสธกลุ่มสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + "คน"
                        else: ret_ += "\n╠۞➣○ ปฏิเสธกลุ่มเชิญ[ ᴏғғ ]"						
                        if settings["autoLeave"] == True: ret_ += "\n╠۞➣● ออกแชทรวม [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ออกแชทรวม[ ᴏғғ ]"
                        if settings["autoRead"] == True: ret_ += "\n╠۞➣● อ่านออโต้ [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ อ่านออโต้[ ᴏғғ ]"				
                        if settings["checkContact"] == True: ret_ += "\n╠۞➣● อ่านคท [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ อ่านคท[ ᴏғғ ]"
                        if settings["checkPost"] == True: ret_ += "\n╠۞➣● เช็คโพส [ ᴏɴ ]"
                        else: ret_ += "\n╠❂➣○ เช็คโพส[ ᴏғғ ]"
                        if settings["checkSticker"] == True: ret_ += "\n╠۞➣● Sticker [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ Sticker[ ᴏғғ ]"
                        ret_ += "\n╠══[ ☆ ระบบแทค ☆ ]══════"
                        if settings["detectMention"] == True: ret_ += "\n╠۞➣● ตอบกลับคนแทค [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ตอบกลับคนแทค[ ᴏғғ ]"
                        if settings["potoMention"] == True: ret_ += "\n╠۞➣● แสดงภาพคนแทค [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ แสดงภาพคนแทค[ ᴏғғ ]"
                        if settings["kickMention"] == True: ret_ += "\n╠۞➣● เตะคนแทค [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ เตะคนแทคแ[ ᴏғғ ]"
                        if settings["kickContact"] == True: ret_ += "\n╠۞➣● สั่งเตะด้วย คท [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ สั่งเตะด้วย คท [ ᴏғғ ]"
                        if settings["delayMention"] == True: ret_ += "\n╠۞➣● แทคกลับคนแทค [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ แทคกลับคนแทค[ ᴏғғ ]"
                        if settings["detectMentionPM"] == True: ret_ += "\n╠۞➣● แทคกลับทางแชท [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ แทคกลับทางแชท[ ᴏғғ ]"
                        if settings["Mentiongift"] == True: ret_ += "\n╠۞➣● ของขวัญคนแทค [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ของขวัญคนแทค[ ᴏғғ ]"
                        ret_ += "\n╠══[ ☆ ระบบป้องกัน ☆ ]═════"
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠۞➣● กันเชิญ [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ กันเชิญ[ ᴏғғ ]"
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠۞➣● กันยกเชิญ [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ กันยกเชิญ[ ᴏғғ ]"
                        if RfuProtect["protect"] == True: ret_ += "\n╠۞➣● ป้องกัน [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ป้องกัน[ ᴏғғ ]"
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠۞➣● ป้องกันเปิดลิ้ง [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ป้องกันเปิดลิ้ง[ ᴏғғ ]"
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠۞➣● ป้องกันสมาชิก [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ป้องกันสมาชิก[ ᴏғғ ]"
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠۞➣● ป้องกันเข้ากลุ่ม [ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ป้องกันเข้ากลุ่ม[ ᴏғғ ]"						
                        ret_ += "\n╠════════════════\n╰═══[『ℳ₳N』฿✪₮ᴸᴵᶰᵉ ]════\n\n ™─┅❈͜͡✯『ℳ₳N』฿✪₮ᴸᴵᶰᵉ ✯͜͡❈┅─"
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "เช็คการตั้งค่าบอท"                   
                        link = "https://line.me/ti/p/FMRCTkb0nl"
                        #line.sendFooter(to, str(ret_),link ,icon,name)
                        #line.sendMentionFooter(to, "「ผู้สร้างบอท」:", ผู้สร้างบอท, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                        line.sendMentionFooter(to, str(ret_) + "\nผู้สร้างบอท >", ผู้สร้างบอท, "https://line.me/ti/p/~manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(ผู้สร้างบอท).pictureStatus, line.getContact(ผู้สร้างบอท).displayName);line.sendMessage(to, line.getContact(ผู้สร้างบอท).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(ผู้สร้างบอท).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manbotline', 'type': 'mt', 'subText': "MANBOTLINE", 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manbotline', 'i-linkUri': 'https://line.me/ti/p/~manbotline', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~manbotline'}, contentType=19)
                        #line.sendMentionFooter(to, '「ผู้สร้างบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set2':
                    try:
                        ret_ = "╭═[ ᵐᵃⁿ ˡᵒᵛᵉ ˢᵉˡᶠᵇᵒᵗ ]\n║"
                        if settings["unsendMessage"] == True: ret_ += "\n╠۞➣● จับยก[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ จับยก[ ᴏғғ ]"
                        if settings["ยกเลิกข้อความ"] == True: ret_ += "\n╠۞➣● จับยก1[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ จับยก1[ ᴏғғ ]"
                        if settings["noคิก"] == True: ret_ += "\n╠۞➣● ระบบไม่มีคิก[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ระบบไม่มีคิก[ ᴏғғ ]"
                        if settings["1คิก"] == True: ret_ += "\n╠۞➣● ระบบ1คิก[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ระบบ1คิก[ ᴏғғ ]"
                        if settings["2คิก"] == True: ret_ += "\n╠۞➣● ระบบ2คิก[ ᴏɴ ]"
                        else: ret_ += "\n╠۞➣○ ระบบ2คิก[ ᴏғғ ]"
                        ret_ += "\n║\n╰═[『ℳ₳N』฿✪₮ᴸᴵᶰᵉ ]"
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "เช็คการตั้งค่าบอท"                   
                        link = "https://line.me/ti/p/FMRCTkb0nl"
                        #line.sendFooter(to, str(ret_),link ,icon,name)
                        line.sendMentionFooter(to, str(ret_) + "\nผู้สร้างบอท >", ผู้สร้างบอท, "https://line.me/ti/p/~manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(ผู้สร้างบอท).pictureStatus, line.getContact(ผู้สร้างบอท).displayName);line.sendMessage(to, line.getContact(ผู้สร้างบอท).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(ผู้สร้างบอท).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manbotline', 'type': 'mt', 'subText': "MANBOTLINE", 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manbotline', 'i-linkUri': 'https://line.me/ti/p/~manbotline', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~manbotline'}, contentType=19)
                        #line.sendMentionFooter(to, "ผู้สร้างบอท >", ผู้สร้างบอท, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                        #line.sendMentionFooter(to, '「ผู้สร้างบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#===================================================

#==========
                elif "บอกหมุด " in msg.text:
                    bctxt = msg.text.replace("บอกหมุด ","")
                    a = line.getGroupIdsJoined()
                    for manusia in wait["bc"]:
                        if manusia in a:
                            line.sendText(manusia,(bctxt))
                            time.sleep(0.1)
                    line.sendText(receiver,"「 ส่งกลุ่มที่ปักหมุดแล้ว 」")
                elif msg.text in ["ปักหมุด"]: #
                    wait["bc"][receiver] = True
                    line.sendText(receiver,"「 ปักหมุดกลุ่มนี้เรียบร้อย 」")
                elif msg.text in ["ลบหมุด"]:
                    try:
                        del wait["bc"][receiver]
                        line.sendText(receiver,"「 ลบหมุดออกเรียบร้อย 」")
                    except:
                        line.sendText(receiver,"「 ลบหมุดออกเรียบร้อย 」")
                elif msg.text in ["ลิสหมุด"]:
                    a = line.getGroupIdsJoined()
                    ret_ = "══[รายชื่อกลุ่ม]══"
                    num = 1
                    for manusia in wait["bc"]:
                        if manusia in a:
                            group = line.getGroup(manusia)
                            ret_ += "\n {}. {} | {}".format(str(num), str(group.name), str(len(group.members)))
                            num=(num+1)					
                    line.sendMessage(to, str(ret_))
#==========
                elif msg.text in ["ปิดเซลบอท","ปิดเซล"]:
                    settings["MANBOTLINE"] = False
                    line.sendMessage(to, "➠ ปิดระบบเซลบอทแล้ว")
                elif msg.text in ["ระบบ1คิก","เปิดระบบ1คิก"]:
                    settings["1คิก"] = True
                    settings["2คิก"] = False
                    line.sendMessage(to, "          [ 1คิก ᴏɴ ]\n\nเปิดใช้งานระบบ1คิกแล้ว")
                elif msg.text in ["ระบบ2คิก","เปิดระบบ2คิก"]:
                    settings["2คิก"] = True
                    settings["1คิก"] = False
                    line.sendMessage(to, "          [ 2คิก ᴏɴ ]\n\nเปิดใช้งานระบบ2คิกแล้ว")
                elif msg.text in ["Add2 on","เปิดแจกแอด","เปิด แจกแอด"]:
                    settings["ของขวัญคนแอด"] = True
                    line.sendMessage(to, "➠ เปิดระบบแจกของขวัญคนเพิ่มเพื่อนแล้ว")
                elif msg.text in ["Add2 off","ปิดแจกแอด","ปิด แจกแอด"]:
                    settings["ของขวัญคนแอด"] = False
                    line.sendMessage(to, "➠ ปิดระบบแจกของขวัญคนเพิ่มเพื่อนแล้ว")
                elif msg.text in ["Tag5 on","เปิดแจกแทค","เปิด แจกแทค"]:
                    settings["Mentiongift"] = True
                    line.sendMessage(to, "➠ เปิดระบบแจกของขวัญคนแทคแล้ว")
                elif msg.text in ["Tag5 off","ปิดแจกแทค","ปิด แจกแทค"]:
                    settings["Mentiongift"] = False
                    line.sendMessage(to, "➠ ปิดระบบแจกของขวัญคนแทคแล้ว")
                elif msg.text in ["เปิดขโมย","เปิดยก1"]:
                    #settings["unsendMessage"] = True
                    settings["unsendMessage"] = False
                    settings["ยกเลิกข้อความ"] = True
                    line.sendMessage(to, "➠ เปิดขโมยรูปคนยกเลิกข้อความแร้ว")
                elif msg.text in ["ปิดขโมย","ปิดยก1"]:
                    #settings["unsendMessage"] = True
                    settings["ยกเลิกข้อความ"] = False
                    line.sendMessage(to, "➠ ปิดขโมยรูปคนยกเลิกข้อความแร้ว")
                elif msg.text in ["เปิดจับยก","เปิดยก"]:
                    settings["ยกเลิกข้อความ"] = False
                    settings["unsendMessage"] = True
                    line.sendMessage(to, "➠ เปิดจับคนยกเลิกข้อความแร้ว")
                elif msg.text in ["ปิดจับยก","ปิดยก"]:
                    settings["unsendMessage"] = False
                    line.sendMessage(to, "➠ ปิดจับคนยกเลิกข้อความแร้ว")
                elif msg.text in ["เปิดแอด","Add on","A on"]:
                    settings["autoAdd"] = True
                    settings["autoBlock"] = False
                    settings["ตรวจสอบแอด"] = False
                    #RfuProtect["autoAdd"] == True
                    #RfuProtect["autoBlock"] == False
                    line.sendMessage(to, "                 [ Add ᴏɴ ]\n\nออโต้แอดเปิดใช้งานเรียบร้อยแล้ว🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["เปิดบล๊อค","เปิดบล็อค","B on"]:
                    settings["autoBlock"] = True
                    settings["autoAdd"] = False
                    settings["ของขวัญคนแอด"] = False
                    settings["ตรวจสอบแอด"] = False
                   # RfuProtect["autoBlock"] == True
                    #RfuProtect["autoAdd"] == False
                    line.sendMessage(to, "                 [ Block ᴏɴ ]\n\nออโต้บล๊อคเปิดใช้งานแล้ว🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["เปิดระบบตรวจสอบ","เปิดตรวจสอบแอด","ตรวจสอบ on"]:
                    settings["ตรวจสอบแอด"] = True
                    settings["autoAdd"] = False
                    settings["autoBlock"] = False
                    #RfuProtect["autoAdd"] == True
                    #RfuProtect["autoBlock"] == False
                    line.sendMessage(to, "                 [ ระบบตรวจสอบ ᴏɴ ]\n\nออโต้ตรวจสอบแอดเปิดใช้งานเรียบร้อยแล้ว🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดแอด","Add off","A off"]:
                    settings["autoAdd"] = False
                    #RfuProtect["autoAdd"] == False
                    line.sendMessage(to, "                 [ Add ᴏғғ ]\n\nออโต้แอดปิดใช้งานแล้ว🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดบล๊อค","ปิดบล็อค","B off"]:
                    settings["autoBlock"] = False
                    #RfuProtect["autoBlock"] == False
                    line.sendMessage(to, "                 [ Block ᴏғғ ]\n\nออโต้บล็อคปิดใช้งานแล้ว🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == 'เปิดเข้า':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "[ ᴏɴ ]ออโต้เข้าห้องเปิดใช้งาน🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == 'ปิดเข้า':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "[ ᴏғғ ]ออโต้เข้าห้องปิดใช้งาน🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif "gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"ปิดใช้งานระบบปฏิเสธคำเชิญตามจำนวนสมาชิก", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to, " สมาชิกในกลุ่มที่ไม่ถึง" + strnum + "จะถูกปฏิเสธคำเชิญโดยอัตโนมัติ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,str(settings["eror"]))
                        else:
                                line.sendText(msg.to,"Bizarre ratings")					

                elif msg.text in ["เปิดออก","เปิดออกแชท"]:
                    settings["autoLeave"] = True
                    line.sendMessage(to, "เปิดระบบออกแชทรวมอัตโนมัติ🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดออก","ปิดออกแชท"]:
                    settings["autoLeave"] = False
                    line.sendMessage(to, "ปิดระบบออกจากแชทอัตโนมัติแล้ว🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["เปิดอ่าน","เปิดอ่านออโต้"]:
                    settings["autoRead"] = True
                    line.sendMessage(to, "เปิดใช้งานการอ่านอัตโนมัตแล้ว🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดอ่าน","ปิดอ่านออโต้"]:
                    settings["autoRead"] = False
                    line.sendMessage(to, "ปิดใช้งานการอ่านอัตโนมัติแล้ว🔰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["เปิดติ๊ก","Sk on"]:
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Check sticker enabled.", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดติ๊ก","Sk off"]:
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Check sticker disabled.", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["เปิดมุด","เปิดมุดลิ้ง"]:
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "ออโต้มุดเปิดทำงาน", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดมุด","ปิดมุดลิ้ง"]:
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "ออโต้มุดปิดทำงาน", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["เปิดเตะคท","เปิดเตะคอนแทค"]:
                    settings["kickContact"] = True
                    line.sendMessage(to, "KickContact ✔", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดเตะคท","ปิดเตะคอนแทค"]:
                    settings["kickContact"] = False
                    line.sendMessage(to, "KickContact ✘", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text in ["เปิดไลค์","เปิดไลค"]:
                    if settings["likeOn"] == True:
                        if settings["lang"] == "JP":
                            line.sendText(msg.to,"Done。")
                    else:
                        settings["likeOn"] = True
                        if settings["lang"] == "JP":
                            line.sendText(msg.to,"Already。")
                elif msg.text in ["ปิดไลค์","ปิดไลค"]:
                    if settings["likeOn"] == False:
                        if settings["lang"] == "JP":
                            line.sendText(msg.to,"Done。")
                    else:
                        settings["likeOn"] = False
                        if settings["lang"] == "JP":
                            line.sendText(msg.to,"Already。")


                elif text.lower() == 'like on':settings["autolike"]=True;setback();line.sendMessage(to,"Autolike turned on!")
                elif text.lower() == 'like off':settings["autolike"]=False;setback();line.sendMessage(to,"Autolike turned off!")


#==============================================================================#
                elif msg.text.lower() == "gift1":
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text.lower = None
                    line.sendMessage(msg)



                elif msg.text.lower() == "run":
                  if settings["selfbot"] == True:
                    if msg._from in admin:
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                       line.sendMessage(to, None, contentMetadata={"STKID":"123","STKPKGID":"1","STKVER":"100"}, contentType=7)
                       line.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                       line.sendMessage(to, None, contentMetadata={"STKID":"123","STKPKGID":"1","STKVER":"100"}, contentType=7)
                       line.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                       line.sendMessage(to, None, contentMetadata={"STKID":"123","STKPKGID":"1","STKVER":"100"}, contentType=7)
                       line.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                       line.sendMessage(to, None, contentMetadata={"STKID":"123","STKPKGID":"1","STKVER":"100"}, contentType=7)
                       line.sendMessage(msg.to, "Go")

                elif "คท" == msg.text.lower():
                  if settings["selfbot"] == True:
                    if msg._from in admin:
                       msg.contentType = 13
                       line.sendMessage(msg.to, None, contentMetadata={'mid': lineMID}, contentType=13)
                       A = line.getContact(lineMID).mid
                       line.sendReplyMessage(msg_id,to,None,contentMetadata={'mid':A},contentType=13)



                elif "เด้ง" == msg.text.lower():
                       msg.contentType = 13
                       line.sendContact(to, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")

                elif msg.text in ["เชคโทเคน","ดูโทเคน"]:
                    line.sendMessage(receiver,"      ❇TOKEN ADMIN❇\n───────────────\n"+line.authToken)


                elif msg.text.lower() == "/vps":
                    line.sendMessage(to, "https://console.cloud.google.com")
                    line.sendMessage(to, "https://aws.amazon.com")
#                    line.sendMessage(to, "https://console.cloud.google.com")
#                    line.sendMessage(to, "https://console.cloud.google.com")


#==============================================================================#
                elif msg.text.lower() == "//c":
                    pict = line.downloadFileURL("http://dl.profile.line-cdn.net/")
                    vids = line.downloadFileURL("http://dl.profile.line-cdn.net/")
                    changeVideoAndPictureProfile(pict, vids)
                    line.sendMessage(to, "Succes Change Profile Picture With Video")

                elif "runtime" == msg.text.lower():
                    line.sendMessage(to, "╭═══════════╮\n║   👀RunTime👀\n╠═══════════\n╠❂➣ 00「ปี」\n╠❂➣ 00「เดือน」\n╠❂➣ 00「วัน」\n╠❂➣ 03「ชั่วโมง」\n╠❂➣ 32「นาที」\n╠❂➣ 05「วิ」\n╰═══════════╯")

                #elif "ทีมบอท" == msg.text.lower():
                  #  msg.contentType = 13
                  #  line.sendMessage(to, "CREAROT & ADMIN \nŚẾL₣ВΌŦ (｡◕‿◕｡)")
                   # line.sendContact(to, "u0035a5a6c5ae9d30c9a0992ecbc39395")
                   # line.sendContact(to, "u9e0f538586963f09c59b75648081e9d5")
                  #  line.sendContact(to, "ubf4806077f2b20dd22fb3a7072eb0eb8")
                   # line.sendContact(to, "ufec28f9f699a2cb6444e62e5397fe115")
                   # line.sendContact(to, "ue1a44110ed4e82ba603010445f0ba585")
                    #line.sendContact(to, "u6588c368db2307a41862b7385e00f4d8")                        

                elif msg.text in ["เทส","ทดสอบ"]:
                    line.sendMessage(to,"™─┅❈͜͡✯ʙᴀsʙᴏᴛʟɪɴᴇ✯͜͡❈┅─")
                    line.sendMessage(to,"LOADING:▒...0%")  
                    line.sendMessage(to,"█▒... 10.0%")       
                    line.sendMessage(to,"██▒... 20.0%")
                    line.sendMessage(to,"███▒... 30.0%")
                    line.sendMessage(to,"████▒... 40.0%")
                    line.sendMessage(to,"█████▒... 50.0%")
                    line.sendMessage(to,"██████▒... 60.0%")
                    line.sendMessage(to,"███████▒... 70.0%")
                    line.sendMessage(to,"████████▒... 80.0%")
                    line.sendMessage(to,"█████████▒... 90.0%")
                    line.sendMessage(to,"███████████..100.0%")                    
                    line.sendMessage(to,"บอทยังทำงานปรกติน๊ะจ๊ะ\n™─┅❈͜͡✯ʙᴀsʙᴏᴛʟɪɴᴇ✯͜͡❈┅─")       

                elif msg.text in ["เริ่ม","เริ่มเกม"]:
                    line.sendMessage(to,"ใครอยู่ใต้ 9 บน 0 พิมชื่อตัวเอง\n             (ชื่อ+อยู่)\n  รับติ๊ก 10© 1 ตัว")
                    line.sendMessage(to,"1")
                    line.sendMessage(to,"2")  
                    line.sendMessage(to,"3")       
                    line.sendMessage(to,"4")
                    line.sendMessage(to,"5")
                    line.sendMessage(to,"6")
                    line.sendMessage(to,"7")
                    line.sendMessage(to,"8")
                    line.sendMessage(to,"9")
                    line.sendMessage(to,"0")

                elif text.lower() == '/i':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n" + me.displayName, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)



                elif msg.text.lower() == "ผม":
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[👇ชื่อของพี่👇]")
                    sendMessageWithMention(to, lineMID)
                    #line.sendMessage(msg.to,"[สเตตัส]\n" + me.statusMessage)
                    line.sendContact(to, lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    cover = line.getProfileCoverURL(lineMID)
                   # line.sendImageWithURL(msg.to, cover)
                    #line.sendMessage(msg.to,str(settings["comment"]))
                elif text.lower() == ".ตัวเรา":
                    line.sendMentionFooter(to, '「ผู้สร้างบอท」\n', sender, "https://line.me/ti/p/~samuri5.", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~samuri5.', 'type': 'mt', 'subText': "SAMURAI BOT", 'a-installUrl': 'https://line.me/ti/p/~samuri5.', 'a-installUrl': ' https://line.me/ti/p/~samuri5.', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~samuri5.', 'i-linkUri': 'https://line.me/ti/p/~samuri5.', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~samuri5'}, contentType=19)
                elif text.lower() == ".ศรราม":
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendImageWithFooter(to, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, str(userid), "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                    line.sendMentionFooter(to, '「Me」\n', sender, str(userid), "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                    line.sendMusic(to, line.getContact(sender).displayName, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, str(userid), "SAMURAI BOT", line.getContact(sender).displayName)
                elif text.lower() == '.คท':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                    line.sendMentionFooter(to, '「ผู้ควบคุมบอท」\n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)
                elif text.lower() == 'me':
                    #sendMessageWithMention(to, lineMID)
                    #line.sendContact(to, lineMID)
                    line.sendMentionFooter(to, '      「ผู้ควบคุมบอท」      \n', sender, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'type': 'mt', 'subText': "BASBOTLINE", 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-installUrl': 'https://line.me/ti/p/FMRCTkb0nl', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'i-linkUri': 'https://line.me/ti/p/FMRCTkb0nl', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/FMRCTkb0nl'}, contentType=19)

                elif text.lower() == 'ค':
                    sendMessageWithMention(to, lineMID)
                    A = line.getContact(lineMid).mid
                    line.sendReplyMessage(msg_id,to,None,contentMetadata={'mid':A},contentType=13)
                    A = line.getContact(lineMID).mid
                    me = line.getContact(lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == '.me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, adminMID)
                elif text.lower() == '.ไอดี':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif msg.text in ["ชื่อ","ชื่อผม"]:
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n" + me.displayName, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ตัส","ตัสผม"]:
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ดิส","ดิสผม"]:
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'วีดีโอ':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif msg.text in ["ปก","ปกผม"]:
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif text.lower() == '.คอมเม้น':
                    line.sendMessage(msg.to,str(settings["comment1"]), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"52114123","STKPKGID":"11539","STKVER":"1"}, contentType=7)
                elif msg.text in ["ทักเข้า","เชคเข้า","เช็คเข้า"]:
                    line.sendMessage(msg.to, str(settings["welcome"]), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ทักออก","เชคออก","เช็คออก"]:
                    line.sendMessage(msg.to, str(settings["bye"]), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ทักเตะ","เชคเตะ","เช็คเตะ"]:
                    line.sendMessage(msg.to, str(settings["kick"]), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ข้อความแอด","เชคแอด","เช็คแอด"]:
                    line.sendMessage(msg.to, str(settings["message"]), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ข้อความแทค","เชคแทค","เช็คแทค"]:
                    line.sendMessage(msg.to, str(settings["Respontag"]), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == 'แทคล่อง':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "ม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'ไอดีล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีmidคนใส่ร่องหน🤗")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == 'คทล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("ไอดี "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n" + contact.statusMessage)
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("วีดีโอ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.findAndAddContactsByMid(ls)
                        line.sendMessage(to, "เพิ่มคุณ" + str(contact.displayName) + " เป็นเพื่อนแล้ว")
                elif msg.text.lower().startswith("ลบเพื่อน "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            line.delContact(ls)
                        line.sendMessage(to, "ลบออกจากการเป็นเพื่อนแล้ว") #, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower()  == ".ล้างเพื่อน" or text.lower()  == " unfriendall":
                    try:
                        friend = line.getContacts(line.getAllContactIds())
                        line.sendMessage(to,"คุณได้ล้างเพื่อนทั่งหมด {} คน".format(len(friend)))
                        for unfriend in friend:
                            line.delContact(unfriend.mid)
                        line.sendMessage(to,"คุณได้ล้างเพื่อนทั่งหมด {} คน".format(len(friend)))
                    except Exception as error:
                        line.sendMessage(to, "「 Result Error 」\n" + str(error))

                elif msg.text in ["กลุ่ม"]:
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ผู้สร้างได้ลบบัญชีไปแล้ว"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ลิ้งกลุ่มปิดอยู่"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    timeCreated = []
                    timeCreated1 = []
                    timeCreated.append(time.strftime("%d-%m-%Y", time.localtime(int(group.createdTime) / 1000)))
                    timeCreated1.append(time.strftime("%H:%M:%S", time.localtime(int(group.createdTime) / 1000)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔═════[ ข้อมูลกลุ่ม ]"
                    ret_ += "\n╠ ชื่อกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ID กลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ วันที่สร้างกลุ่ม : {}".format(str(timeCreated))
                    ret_ += "\n╠ เวลาที่สร้างกลุ่ม : {}".format(str(timeCreated1))
                    ret_ += "\n╠ จำนวน สมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวน ค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้ง : {}".format(gTicket)
                    ret_ += "\n╚════[ By. ℳ₳N ※ ฿✪₮]"
                    line.sendMessage(to, str(ret_))
                    #line.sendMessage(msg.to, None, contentMetadata={'mid': group.creator.mid}, contentType=13)
                    line.sendImageWithURL(to, path)
                    
                elif msg.text in ["/แอด"]:
                    group = line.getGroup(to)
                    try:
                        line.sendMentionFooter(to, "นี้ไงแอดมินกลุ่ม", group.creator.mid, "https://line.me/ti/p/~manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName) #;line.sendMessage(to, line.getContact(ผู้สร้างบอท).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(ผู้สร้างบอท).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~manbotline', 'type': 'mt', 'subText': "MANBOTLINE", 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-installUrl': 'https://line.me/ti/p/~manbotline', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~manbotline', 'i-linkUri': 'https://line.me/ti/p/~manbotline', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~manbotline'}, contentType=19)
                        line.sendMessage(msg.to, None, contentMetadata={'mid': group.creator.mid}, contentType=13)
                    except Exception as e:
                        line.sendMessage(to, "แอดมินห้องนี้ลบชีไปแล้ว")

                elif ".โพส " in msg.text:
                    tl_text = msg.text.replace(".โพส ","")
                    line.sendText(msg.to,"line://home/post?userMid="+lineMID+"&postId="+line.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])

                elif msg.text in ["โหลดข้อมูล"]:
                    if msg._from in admin:
                        wek = line.getContact(lineMID)
                        a = wek.pictureStatus
                        r = wek.displayName
                        i = wek.statusMessage
                        s = open('mydn.txt',"w")
                        s.write(r)
                        s.close()
                        t = open('mysm.txt',"w")
                        t.write(i)
                        t.close()
                        u = open('myps.txt',"w")
                        u.write(a)
                        u.close()
                        line.sendText(msg.to, "backup has been active")
                        print (wek)
                        print (a)
                        print (r)
                        print (i)
                
                elif "แปลงร่าง " in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = line.getContact(target)
                            X = contact.displayName
                            profile = line.getProfile()
                            profile.displayName = X
                            line.updateProfile(profile)
                            line.sendMessage(msg.to, "Success...")
                        #---------------------------------------
                            Y = contact.statusMessage
                            lol = line.getProfile()
                            lol.statusMessage = Y
                            line.updateProfile(lol)
                        #---------------------------------------
                            settings["changePictureProfile"] = True
                            me = line.getContact(target)     
                            line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                        except Exception as e:
                            line.sendMessage(msg.to, "Failed!")
                            print (e)

                elif "กลับร่าง" in msg.text:
                    if msg._from in admin:
                            try:
                                h = open('mydn.txt',"r")
                                name = h.read()
                                h.close()
                                x = name
                                profile = line.getProfile()
                                profile.displayName = x
                                line.updateProfile(profile)
                                i = open('mysm.txt',"r")
                                sm = i.read()
                                i.close()
                                y = sm
                                cak = line.getProfile()
                                cak.statusMessage = y
                                line.updateProfile(cak)
                                line.sendText(msg.to, "คืนได้แค่ชื่อกับตัสนะ😂😂")

                            except Exception as e:
                                line.sendText(msg.to,"การคืนร่างล้มเหลว!")
                                print (e)
                elif msg.text in ["Allprotect on",".เปิดกทม"]:
                        settings["kickMention"] = True
                        settings["Aip"] = False
                        RfuProtect["protect"] = True
                        RfuProtect["cancelprotect"] = True
                        RfuProtect["inviteprotect"] = True 
                        RfuProtect["linkprotect"] = True 
                        RfuProtect["Protectguest"] = True
                        RfuProtect["Protectjoin"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด เปิด👌", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
						
                elif msg.text in ["Allprotect off",".ปิดกทม"]:
                        settings["kickMention"] = False
                        settings["Aip"] = False
                        RfuProtect["protect"] = False
                        RfuProtect["cancelprotect"] = False
                        RfuProtect["inviteprotect"] = False 
                        RfuProtect["linkprotect"] = False 
                        RfuProtect["Protectguest"] = False
                        RfuProtect["Protectjoin"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด ปิด👌", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        
                elif msg.text in ["Allmsg on",".เปิดข้อความ"]:
                        settings["Wc"] = True
                        settings["Lv"] = True
                        settings["Nk"] = True
                        settings["autoRead"] = True
                        settings["checkSticker"] = True 
                        settings["checkContact"] = True 
                        settings["checkPost"] = True
                        settings["potoMention"] = True
                        settings["detectMention"] = True
                        settings["delayMention"] = True
                        settings["Api"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด เปิด👌", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
						
                elif msg.text in ["Allmsg off",".ปิดข้อความ"]:
                        settings["Wc"] = False
                        settings["Lv"] = False
                        settings["Nk"] = False
                        settings["autoRead"] = True
                        settings["checkSticker"] = False 
                        settings["checkContact"] = False 
                        settings["checkPost"] = False
                        settings["detectMention"] = False
                        settings["potoMention"] = False
                        settings["delayMention"] = False
                        settings["Api"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด ปิด👌", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif "ระบบ" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "เปิด":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    elif mic == "ปิด":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif '.เพลสโต ' in msg.text.lower():
                        tob = msg.text.lower().replace('.เพลสโต ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : Google Play\nลิ้งโหลด : https://play.google.com/store/search?q=" + tob)
                        line.sendText(msg.to,"👆กรุณากดลิ้งเพื่อทำการโหลดแอพ👆")
                elif '.ขอเพลง ' in msg.text.lower():
                        tob = msg.text.lower().replace('.ขอเพลง ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : ยูทูป\nลิ้งรับชม : https://m.youtube.com/results?search_query=เพลง" + tob)
                        line.sendText(msg.to,"👆กรุณากดลิ้งเพื่อทำการโหลดแอพ👆")
                elif 'github ' in msg.text.lower():
                        tob = msg.text.lower().replace('github ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : GitHub\nลิ้ง : https://github.com/search?q=" + tob)
                        line.sendText(msg.to,"??ค้นหาสำเร็จแล้ว👆")
                elif '.กูเกิ้ล ' in msg.text.lower():
                        tob = msg.text.lower().replace('.กูเกิ้ล ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : กูเกิ้ล\nลิ้ง : https://www.google.co.th/search?q=" + tob)
                        line.sendText(msg.to,"👆ค้นหาสำเร็จแล้ว👆")
                elif '.เฟสบุค ' in msg.text.lower():
                        tob = msg.text.lower().replace('.เฟสบุค ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : เฟสบุค\nลิ้ง : https://m.facebook.com/search/top/?q=" + tob)
                        line.sendText(msg.to,"👆ค้นหาสำเร็จแล้วเชิญกดลิ้งเพื่อเข้าไปดูรายละเอียด👆")
                elif "!คท " in msg.text:
                    mmid = msg.text.replace("!คท ","")
                    line.sendMessage(to, text=None, contentMetadata={'mid': mmid}, contentType=13)

                elif ".ค้นหาไอดี " in msg.text:
                    msgg = msg.text.replace(".ค้นหาไอดี ","")
                    conn = line.findContactsByUserid(msgg)
                    if True:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': conn.mid}
                        line.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                        line.sendMessage(to,msg)
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
#==============================================================================#
                elif text.lower() == '.แอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "☝คนนี้แหล่ะคนสร้างกลุ่มนี้", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ไอดีกลุ่ม \n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ชื่อกลุ่ม -> \n" + gid.name)
                elif text.lower() == '.ลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "ลิ้งของกลุ่ม\nhttps://line.me/R/ti/g/{}".format(str(ticket)), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == '.เปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == '.ปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "คนนี้คือผู้สร้างกลุ่มนี้"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    line.sendImageWithURL(to, path)
                elif text.lower() == '.สมาชิกกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == 'ลิสกลุ่ม':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})                

                elif ".เช็คกลุ่ม " in text.lower():
                    line.sendMessage(to, "กำลังตรวจสอบข้อมูล...")
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        G = line.getGroupIdsJoined()
                        cgroup = line.getGroups(G)
                        ngroup = ""
                        for mention in mentionees:
                         for x in range(len(cgroup)):
                           gMembMids = [contact.mid for contact in cgroup[x].members]
                           if mention['M'] in gMembMids:
                                ngroup += "\n۞➢ " + cgroup[x].name + " | สมาชิก: " +str(len(cgroup[x].members))    
                        if ngroup == "":
                             line.sendMessage(to, "ไม่พบ")
                        else:
                             line.sendMessage(to, "۞➢ตรวจพบอยู่ในกลุ่ม %s\n"%(ngroup))				
                elif ".เชิญคลอ" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif ".คลอ" in msg.text.lower():
                    if msg.toType == 2:
                        sep = msg.text.split(" ")
                        resp = msg.text.replace(sep[0] + " ","")
                        num = int(resp)
                        try:
                            line.sendMessage(msg.to,"กำลังดำเนินการ...", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        except:
                            pass
                        for var in range(num):
                            group = line.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            line.acquireGroupCallRoute(msg.to)
                            line.inviteIntoGroupCall(msg.to, contactIds=members)
                        line.sendMessage(msg.to,"เชิญคอลสำเร็จแล้ว(｀・ω・´)", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'}))
                        except:
                            pass
                elif msg.text.lower() == '.เชิญแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "พิมพ์คำเชิญกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "ผู้สร้างกลุ่มอยู่ในแล้ว", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text.lower().startswith(".ไอดีไลน์ "):
                    id = msg.text.lower().replace(".ไอดีไลน์ ","")
                    conn = line.findContactsByUserid(id)
                    if True:                                      
                        line.sendMessage(to,"http://line.me/ti/p/~" + id)
                        line.sendContact(to,conn.mid)
                elif msg.text.lower().startswith(".ถาม "):
                    kata = msg.text.lower().replace("asking", "")
                    sch = kata.replace(" ","+")
                    with _session as web:
                        urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                        r = _session.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                        data = r.text
                        data = json.loads(data)
                        url = data["shorturl"]
                        ret_ = "「คำตอบ」"
                        ret_ += "\n\nLink : {}".format(str(url))
                        line.sendMessage(to, str(ret_))
                        line.sendMessage(to, "กรุณาทำการกดลิ้งเพื่อดูคำตอบ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text.lower().startswith(".บล็อคไอดี "):
                    user = msg.text.lower().replace(".บล็อคไอดี ","")
                    conn = line.findContactsByUserid(conn)
                    if True:
                        line.blockContact(conn)
                        line.sendMessage(to, "ทำการบล็อคไอดีนั้นแล้ว", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text.lower().startswith(".ไวรัส: "):
                    number = msg.text.lower().replace(".ไวรัส: ","")
                    groups = line.getGroupIdsJoined()
                    try:
                        group = groups[int(number)-1]
                        G = line.getGroup(group)
                        try:
                            line.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                        except:
                            line.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                        line.sendMessage(to, "「 Remote Crash 」\n\nGroup : " + G.name)
                    except Exception as error:
                        line.sendMessage(to, str(error))          
                elif msg.text.lower() == "getjoined":
                    line.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendText(msg.to,text[:-2])
                    cnt = 0				
                elif ".ข้อมูล " in msg.text.lower():
                    spl = re.split(".ข้อมูล ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net{}".format(userData.picturePath))
                            except:
                                pass
                            line.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                            line.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                            line.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)# contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                
                elif ".รัน @" in msg.text:
                    print ("[Command]covergroup")
                    _name = msg.text.replace(".รัน @","")
                    _nametarget = _name.rstrip('  ')
                    gs = line.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        line.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                               thisgroup = line.getGroups([msg.to])
                               Mids = [target for contact in thisgroup[0].members]
                               mi_d = Mids[:33]
                               line.createGroup("RED SAMURI Group",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.createGroup("RED SAMURI Group",mi_d)
                               line.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                               line.sendText(msg.to,"เรียบร้อย")
                            except:
                                pass
                    print ("[Command]covergroup]")
                elif ".รันแชท @" in msg.text:
                    _name = msg.text.replace(".รันแชท @","")
                    _nametarget = _name.rstrip(' ')
                    gs = line.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ") 
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(g.mid,"『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           line.sendText(msg.to, "Done")
                           print (" Spammed !")
                elif ".ดึงห้อง" in msg.text:
                    thisgroup = line.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    line.createGroup("『MANBOTLINE』", mi_d)
                    line.sendText(msg.to,"welcome to room 『MANBOTLINE』")
                elif ".ไม่รับเชิญ " in msg.text.lower():
                    spl = re.split(".ไม่รับเชิญ ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"สำเร็จแล้ว")	
                elif msg.text.lower().startswith("ยกเชิญ"):
                                if msg._from in bot1:                                
                                    if msg.toType == 2:
                                        group = line.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//30
                                        line.sendMessage(msg.to,"[ ยกค้างเชิญ จำนวน {} คน] \nรอสักครู่...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*30 : (i+1)*30]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                line.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            line.sendMessage(receiver,"รอสักครู่🕛เดียวยกต่อ 30 คน\n BY.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                                            time.sleep(random.uniform(15,10))
                                        line.sendMessage(receiver,"[ ยกค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว👏]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        line.sendMessage(receiver, None, contentMetadata={"STKID": "52002735","STKPKGID": "11537","STKVER": "1" }, contentType=7)
                                        gname = line.getGroup(receiver).name
                                        line.sendMessage(Kuman,"[ ยกค้างเชิญ >> "+gname+"  <<] \n จำนวน {} คน เรียบร้อยแล้ว👏\nBY.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        #line.leaveGroup(receiver)
                                								
                                    line.sendMessage(receiver,"[ไม่มีค้างเชิญ แล้วนะ😁]")
                                    line.sendMessage(receiver, None, contentMetadata={"STKID": "52114123","STKPKGID": "11539","STKVER": "1" }, contentType=7)
                                    #line.leaveGroup(receiver)
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        line.sendMessage(msg)
                elif ".หวด" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif ".ปลิว" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == "mid":
                    line.sendText(msg.to,user1)
                
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".มุด " in msg.text.lower():
                    spl = re.split(".มุด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))
                elif msg.text.lower().startswith(".โทร "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        members = [mem.mid for mem in group.members]
                        line.acquireGroupCallRoute(to)
                        line.inviteIntoGroupCall(to, contactIds=members)
                    else:
                        line.sendMessage(to, "۞➢เชิญแล้วคริๆ".format(str(jml)))
                elif msg.text.lower().startswith(".แทค "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = line.getContact(receiver)
                                RhyN_(to, contact.mid)
                
                elif msg.text.lower().startswith(".แจก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, text=None, contentMetadata={'sticker':'1002077'}, contentType=9)
                                line.sendMessage(to, "ส่งของขวัญใน ส.ต แล้ว".format(str(jml)))
                            else:
                                pass

                elif 'Gift: ' in msg.text:
                  if settings["selfbot"] == True:
                   if msg._from in admin:
                      korban = msg.text.replace('Gift: ','')
                      korban2 = korban.split()
                      midd = korban2[0]
                      jumlah = int(korban2[1])
                      if jumlah <= 1000:
                          for var in range(0,jumlah):
                              line.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                elif msg.text.lower().startswith(".ดับไฟ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, ".God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                line.sendMessage(to, "ไปดู ส.ต ด้วย".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith(".ทัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = line.getContact(to)
                        RhyN_(to, name.mid)
                elif msg.text.lower() == ".":
                    if msg.toType == 0:
                        sendMention(to, to, "", "")
                    elif msg.toType == 2:
                        group = line.getGroup(to)
                        contact = [mem.mid for mem in group.members]
                        mentionMembers(to, contact)
                elif msg.text.lower().startswith("ห้ามพิม "):
                    wban = msg.text.lower().split()[1:]
                    wban = " ".join(wban)
                    wbanlist.append(wban)
                    line.sendMessage(to,"%s ۞➢พิมคำนี้อาจมีปลิวนะ."%wban)
                elif msg.text.lower().startswith("ลบห้ามพิม "):
                    wunban = msg.text.lower().split()[1:]
                    wunban = " ".join(wunban)
                    if wunban in wbanlist:
                        wbanlist.remove(wunban)
                        line.sendMessage(to,"%s ۞➢ล้างออกจากคำสั่งห้ามพิมแล้ว."%wunban)
                    else:
                        line.sendMessage(to,"%s is not blacklisted."%wunban)
                elif msg.text.lower() == 'ดูห้าม':
                    tst = "คำห้ามพิม:"
                    if len(wbanlist) > 0:
                        for word in wbanlist:
                            tst += "\n- %s"%word
                        line.sendMessage(msg.to,tst)
                    else:
                        line.sendMessage(msg.to,"۞➢ไม่มีคำสั่งห้ามพิม")
                elif msg.text.lower().startswith(".ส่งข้อความ "):
                    pnum = re.split(".ส่งข้อความ ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                line.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                line.sendText(msg._from,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                line.sendText(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                line.sendText(msg._from,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                line.sendText(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                line.sendText(msg._from,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        line.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            line.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")
                if "gift " in msg.text.lower():
                    red = re.compile(re.escape('gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)
#==============================================================================#
                elif msg.text in ["มอง","จัดให้ครับ"]:
                    print ("[   มอง   ]『แท็คสมาชิกทั้งห้อง』")
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    else:
                        line.sendMessage(to, "「 จำนวนสมาชิก {} คน 」".format(str(len(nama))))          
                elif msg.text in ["1มอง","1จัดให้ครับ"]:
                    print ("[   คิกแทค   ]『แท็คสมาชิกทั้งห้อง』")
                    group = m1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        m1.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    else:
                        m1.sendMessage(to, "「 จำนวนสมาชิก {} คน 」".format(str(len(nama))))
#==============================================================================#
#==============================================================================#
                elif text.lower() == '.เยส':
                    print ("[   เยส   ]『แท็คสมาชิกทั้งห้อง』")
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += "@Alin \n"
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    else:
                        line.sendMessage(to,"[ จำนวนคนที่โดนเยสทั้งหมด {} คน]".format(str(len(nama))))
                elif text.lower() == '.แท็ค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        txt = "╔══[ชื่อกลุ่ม {} ]\n╠ ".format(str(line.getGroup(to).name))
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += "╠ " + "@Alin \n"
                        else:
                            try:
                                tex += "╚══[ชื่อกลุ่ม   {} ]".format(str(line.getGroup(to).name))
                            except:
                                pass
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        
                elif text.lower() == 'นับบ':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'เลิกนับ':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'นับใหม่':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'อ่านน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ *** LurkDetector *** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")

#==============================================================================#

#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)

#==============================================================================#
                elif "/ประกาศครับ " in msg.text:
                    bc = msg.text.replace("/ประกาศครับ ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendText(i, bc)

                elif "/ประกาศกลุ่ม " in msg.text:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความประกาศ"                   
                    link = "http://line.me/ti/p/~botline2034"
                    bc = msg.text.replace(".ประกาศกลุ่ม ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendFooter(i,"🅃🄴🄰🄼🄱🄾🅃🅃🄰🅃🄾🄼🄴\n"+bc+"\n🅃🄾🄼🄴🄱🄾🅃🄻🄸🄽🄴",link ,icon,name)
                    
                         
                elif "/ประกาศ: " in msg.text:
                    #if msg._from in admin:
                    sep = text.split(" ")
                    bc = text.replace(sep[0] + " ","")
                    gid = line.getGroupIdsJoined()
                    for group in gid:
                       ryan = line.getContact(mid)
                       zx = ""
                       zxc = ""
                       zx2 = []
                       xpesan =  "「 Broadcast 」\nBroadcast by "
                       ret_ = "{}".format(str(bc))
                       ry = str(ryan.displayName)
                       pesan = ''
                       pesan2 = pesan+"@x\n"
                       xlen = str(len(zxc)+len(xpesan))
                       xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                       zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                       zx2.append(zx)
                       zxc += pesan2
                       text = xpesan + zxc + ret_ + ""
                       line.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)                                
                    
                elif "/ประกาศแชท " in msg.text:
                    bc = msg.text.replace(".ประกาศแชท ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendText(i,"🅃🄴🄰🄼🄱🄾🅃🅃🄰🅃🄾🄼🄴\n"+bc+"\n🅃🄾🄼🄴🄱🄾🅃🄻🄸🄽🄴")
            
                elif "/ส่งรูปภาพตามกลุ่ม: " in msg.text:
                    bc = msg.text.replace(".ส่งรูปภาพตามกลุ่ม: ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
                    
                elif "/ส่งรูปภามตามแชท: " in msg.text:
                    bc = msg.text.replace(".ส่งรูปภาพตามแชท: ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
                elif "/ส่งเสียงกลุ่ม " in msg.text:
                    bctxt = msg.text.replace(".ส่งเสียงกลุ่ม ", "")
                    bc = ("บาย...เรด..ซามูไร..เซลบอท")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "/ส่งเสียงแชท " in msg.text:
                    bctxt = msg.text.replace(".ส่งเสียงแชท ", "")
                    bc = ("บาย...เรด..ซามูไร..เซลบอท")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')
                    
                elif text.lower() == '.ปฏิทิน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "🌴ปฏิทินโดย『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』🌴\n\n🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\n🍁" + hasil + "\n🍁 ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n🍁 เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\nBY: ™『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』"
                    line.sendMessage(msg.to, readTime)

                elif "screenshotwebsite " in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])

                elif ".รูปภาพ " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif ".รูปการ์ตูน " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
      
                elif ".ยูทูป " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))





#===========BOT UPDATE BY NOXTIAN============#
                elif msg.text.lower().startswith("แทค"):
                  if msg._from in admin:						
                    data = msg.text[len("แทค"):].strip()
                    if data == "":
                        print ("[   แทค   ]『แท็คสมาชิกทั้งห้อง』")
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 20:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "<":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count > mentargs:
                                break
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 20:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == ">":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                        cb = ""
                        cb2 = ""
                        count = 1
                        if mentargs >= 0:
                            strt = len(str(mentargs)) + 2
                        else:
                            strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count < mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 20:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "=":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                        cb = ""
                        cb2 = ""
                        count = 1
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count != mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            strt = len(str(count)) + 2
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 20:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
#===========BOT UPDATE============#                        
                elif "google " in msg.text.lower():
                    spl = re.split("google ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        line.sendText(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    else:
                                        line.sendText(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                    text = "ผลการค้นหาจาก Google:\n\n"
                                    for el in resp.findAll("h3",attrs={"class":"r"}):
                                        try:
                                                tmp = el.a["class"]
                                                continue
                                        except:
                                                pass
                                        try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                        except:
                                                continue
                                        text += el.a.text+"\n"
                                        text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                    text = text[:-2]
                                    if msg.toType != 0:
                                        line.sendText(msg.to,str(text))
                                    else:
                                        line.sendText(msg.from_,str(text))
                                except Exception as e:
                                    print(e)
                        
                elif ".วีดีโอ " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "วีดีโอ ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif ".หนัง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "หนัง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif ".เพลง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "เพลง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif "music: " in msg.text.lower():
                   if msg._from in admin:
                      sep = msg.text.split(" ")
                      search = msg.text.replace(sep[0] + " ","")
                      params = {'songname': search}
                      with requests.session() as web:
                          web.headers["User-Agent"] = random.choice(settings["userAgent"])
                          r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?".format(urllib.parse.urlencode(params)))
                          try:
                              data = json.loads(r.text)
                              for song in data:
                                  ret_ = "╔══[ Music ]"
                                  ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                  ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                  ret_ += "\n╠ Link : {}".format(str(song[3]))
                                  ret_ += "\n╚══[ Waiting Audio ]"
                              line.sendMessage(msg.to, str(ret_))
                              line.sendMessage(msg.to, "Mohon bersabar musicnya lagi di upload")
                              line.sendAudioWithURL(msg.to, song[3])
                          except:
                              line.sendMessage(to, "Musik tidak ditemukan")

#=====================================================================================================#
                elif "mp3 " in msg.text.lower():
                    try:
                        proses = text.split(" ")
                        urutan = text.replace(proses[0] + "mp3 ","")
                        r = requests.get("https://www.youtube.com={}".format(str(urllib.parse.quote(urutan))))
                        data = r.text
                        data = json.loads(data)
                        b = data
                        c = str(b["title"])
                        d = str(b["singer"])
                        e = str(b["url"])
                        g = str(b["image"])
                        hasil = "「 Hasil Musik 」\n"
                        hasil += "▪Penyanyi: "+str(d)
                        hasil += "\n▪Judul : "+str(c)
                        hasil += "\n「 Nah Itu Hasil Musiknya 」"
                        line.sendImageWithURL(to,g)
                        line.sendAudioWithURL(to,e)
                        line.sendMessage(msg.to,hasil)
                    except Exception as error:
                        line.sendMessage(to, "error\n" + str(error))


                elif "วีดีโอ " in msg.text.lower():
                  if msg._from in admin:
                    try:
                        sep = msg.text.split(" ")
                        textToSearch = msg.text.replace(sep[0] + "วีดีโอ ","")
                        query = urllib.parse.quote(textToSearch)
                        search_url="https://www.youtube.com/results?search_query="
                        mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                        sb_url = search_url + query
                        sb_get = requests.get(sb_url, headers = mozhdr)
                        soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                        yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                        x = (yt_links[1])
                        yt_href =  x.get("href")
                        yt_href = yt_href.replace("watch?v=", "")
                        qx = "https://youtu.be" + str(yt_href)
                        vid = pafy.new(qx)
                        stream = vid.streams 
                        best = vid.getbest()
                        best.resolution, best.extension
                        for s in stream:
                            me = best.url
                            hasil = ""
                            title = "Judul [ " + vid.title + " ]"
                            author = '\n\n│ Author : ' + str(vid.author)
                            durasi = '\n│ Duration : ' + str(vid.duration)
                            suka = '\n│ Likes : ' + str(vid.likes)
                            rating = '\n│ Rating : ' + str(vid.rating)
                            deskripsi = '\n│ Deskripsi : ' + str(vid.description)
                        line.sendVideoWithURL(msg.to, me)
                        line.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                    except Exception as e:
                         line.sendText(msg.to,str(e))

                elif "รูป " in msg.text.lower():
                  if msg._from in admin:
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + "รูป ","")
                    url = "http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search))
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get(url)
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            start = timeit.timeit()
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(msg.to, str(path))

                elif "img " in msg.text.lower():
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    url = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(txt))
                    data = url.json()
                    line.sendImageWithURL(to, random.choice(data["result"]))


                elif msg.text in [".เปิดแสกน","เปิดแอบ","เปิดทัก"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"เปิดระบบแสกนคนอ่านอัตโนมัติ")
                elif msg.text in [".ปิดแสกน","ปิดแอบ","ปิดทัก"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "ปิดระบบแสกนคนอ่านแล้ว")

                elif text.lower() == '.ปิดเซล':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)
                elif text.lower() == ".ลบแชท":
                        if msg._from in lineMID:
                            try:
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"ลบทุกการแชทเรียบร้อย")
                            except:
                                pass
                                print ("ลบแชท")
                elif text.lower() == '.เพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="🎎รายชื่อเพื่อนทั้งหมด🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎รายชื่อเพื่อนทั้งหมด🎎\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in [".เช็คบล็อค"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════ไม่มีรายการบัญชีที่ถูกบล็อค═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════รายการบัญชีที่ถูกบล็อค════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in [".ไอดีเพื่อน"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════รายการไอดีเพื่อน═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════รายการ ไอดีเพื่อน═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == ".เว็บโป๊":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")
                elif msg.text == ".ประกาศ":
                	line.sendMessage(msg.to,str(settings["message1"]))
                elif msg.text.lower() == '.ดึงแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in [".ไม่รับเชิญ"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)							
                        except:
                            pass
                elif msg.text in [".เช็คไอดี"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="™『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["เปิดแทคเจ็บ","เปิดเตะคนแทค"]:
                    settings["kickMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบเตะคนแท็ก")
                
                elif msg.text in ["ปิดแทคเจ็บ","ปิดเตะคนแทค"]:
                    settings["kickMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบเตะคนแท็ก")
                    
                elif msg.text in ["เปิดแทค","Tag on"]:
                        settings['detectMention'] = True
                        line.sendMessage(msg.to,"Respon enabled.")
                
                elif msg.text in ["ปิดแทค","Tag off"]:
                        settings['detectMention'] = False
                        line.sendMessage(msg.to,"Respon disabled.")

                elif msg.text in ["เปิดแทค2","Tag2 on"]:
                    settings["potoMention"] = True
                    line.sendMessage(msg.to,"AutoRespon enabled.")
                
                elif msg.text in ["ปิดแทค2","Tag2 off"]:
                    settings["potoMention"] = False
                    line.sendMessage(msg.to,"Autorespon disabled.")
                    
                elif msg.text in ["เปิดแทค3","Tag3 on"]:
                    settings["delayMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบแทคกลับคนแทค(○ﾟεﾟ○)")
                
                elif msg.text in [".ปิดแทค3","Tag3 off"]:
                    settings["delayMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบแทคกลับคนแทค(ˉ(∞)ˉ)")
                #elif msg.text.lower() == ".เปิดแทคแชท":
                elif msg.text in ["Tag4 on","เปิดแทคแชท"]:
                    settings["detectMentionPM"] = True
                    line.sendMessage(msg.to,"เปิดแทคแชทเรียบร้อยครับ")
                #elif msg.text.lower() == ".ปิดแทคแชท":
                elif msg.text in ["Tag4 off","ปิดแทคแชท"]:
                    settings["detectMentionPM"] = False
                    line.sendMessage(msg.to,"ปิดแทคแชทเรียบร้อยครับ")
                elif msg.text.lower().startswith("ตั้งแทคแชท: "):
                    text = msg.text.lower().replace("ตั้งแทคแชท: ","")
                    settings["pmMessage"] = text
                    line.sendMessage(msg.to, "คำแทคแชท สต คือ : {}".format(str(settings["pmMessage"])))
                elif msg.text.lower().startswith("setrespongroup: "):
                    text = msg.text.lower().replace("setrespongroup: ","")
                    settings["respMessage"] = text
                    line.sendMessage(msg.to, "Success Update Response Group to : {}".format(str(settings["respMessage"])))
                    
                elif msg.text in ["เปิดตรวจสอบ","Js on"]:
                    settings["Aip"] = True
                    line.sendMessage(msg.to,"เปิดระบบตรวจสอบคำหยาบกับบอทบิน  ^ω^")
                
                elif msg.text in ["ปิดตรวจสอบ","Js off"]:
                    settings["Aip"] = False
                    line.sendMessage(msg.to,"ปิดระบบตรวจสอบคำหยาบกับบอทบินแล้วʕ•ﻌ•ʔ")
                    
                elif msg.text in [".เปิดพูด","api on","Api on"]:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทตาต้อม"                   
                    link = "http://line.me/ti/p/~tome2527"
                    settings["Api"] = True
                    line.sendFooter(msg.to,"เปิดระบบApiข้อความ",link ,icon,name)
                
                elif msg.text in [".ปิดพูด","api off","Api off"]:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทตาต้อม"                   
                    link = "http://line.me/ti/p/~tome2527"
                    settings["Api"] = False
                    line.sendFooter(msg.to,"ปิดระบบApiข้อความแล้ว",link ,icon,name)
                    
                elif 'ตั้งแอด: ' in msg.text:
                  if msg._from in admin:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทตาต้อม"                   
                    link = "http://line.me/ti/p/~tome2527"
                    spl = msg.text.replace('ตั้งแอด: ','')
                    if spl in [""," ","\n",None]:
                        line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                    else:
                        settings["message"] = spl
                        line.sendFooter(msg.to, "™『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』\n👇ตั้งข้อความตอบโต้เมื่อมีคนแอดแล้ว ดังนี้\n\n👉{}".format(str(spl)),link ,icon,name)
                         
                elif 'ตั้งคอมเม้น: ' in msg.text:
                  if msg._from in admin:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทตาต้อม"                   
                    link = "http://line.me/ti/p/~tome2527"
                    spl = msg.text.replace('ตั้งคอมเม้น: ','')
                    if spl in [""," ","\n",None]:
                        line.sendFooter(msg.to, "ตั้งข้อความเรืยบร้อย"),link ,icon,name
                    else:
                        settings["comment1"] = spl
                        line.sendMessage(msg.to, "™『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』\n👇ตั้งข้อความคอมเม้นของคุณแล้ว ดังนี้\n\n👉{}".format(str(spl))) 
                    
                elif 'ตั้งแทค: ' in msg.text:
                  if msg._from in admin:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทตาต้อม"                   
                    link = "http://line.me/ti/p/~tome2527"
                    spl = msg.text.replace('ตั้งแทค: ','')
                    if spl in [""," ","\n",None]:
                        line.sendFooter(msg.to, "ตั้งข้อความเรืยบร้อย"),link ,icon,name
                    else:
                        settings["Respontag"] = spl
                        line.sendFooter(msg.to, "™『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』\n👇ตั้งข้อความตอบโต้เมื่อมีคนแทคแล้ว\n\n👉{}".format(str(spl)),link ,icon,name)
                         
                elif 'ทักเตะ: ' in msg.text:
                  if msg._from in admin:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทตาต้อม"                   
                    link = "http://line.me/ti/p/~tome2527"
                    spl = msg.text.replace('ทักเตะ: ','')
                    if spl in [""," ","\n",None]:
                        line.sendMessage(msg.to, "ตั้งข้อความคนคนลบสมาชิดเรียบร้อย")
                    else:
                         settings["kick"] = spl
                         line.sendFooter(msg.to, "™『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』\nตั้งค่าข้อความเมื่อมีคนลบสมาชิกแล้ว\nดังนี้\n\n👉{}".format(str(spl)),link ,icon,name)

                elif 'ทักออก: ' in msg.text:
                  if msg._from in admin:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทตาต้อม"                   
                    link = "http://line.me/ti/p/~tome2527"
                    spl = msg.text.replace('ทักออก: ','')
                    if spl in [""," ","\n",None]:
                        line.sendMessage(msg.to, "ตั้งข้อความคนออกเรียบร้อย")
                    else:
                         settings["bye"] = spl
                         line.sendFooter(msg.to, "™『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』\nตั้งค่าข้อความเมื่อมีคนออกจากกลุ่มแล้ว\nดังนี้👇\n\n👉{}".format(str(spl)),link ,icon,name)

                elif 'ทักเข้า: ' in msg.text:
                  if msg._from in admin:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "คำสั่งบอทตาต้อม"                   
                    link = "http://line.me/ti/p/~tome2527"
                    spl = msg.text.replace('ทักเข้า: ','')
                    if spl in [""," ","\n",None]:
                        line.sendMessage(msg.to, "ตั้งข้อความคนเข้าเรียบร้อยแล้ว")
                    else:
                         settings["welcome"] = spl
                         line.sendFooter(msg.to, "™『✯ᴛᴏᴍᴇʙᴏᴛʟɪɴᴇ✯』\nตั้งค่าข้อความเมื่อมีคนเข้ากลุ่มแล้ว\nดังนี้👇\n\n👉{}".format(str(spl)),link ,icon,name)
                elif msg.text in ["เปิกกันติก","เปิดเตะติก"]:
                        settings["sticker"] = True
                        line.sendMessage(to,"เปิดเตะคนรันสติกเกอรแล้ว")
                elif msg.text in ["ปิดกันติก","ปิดเตะติก"]:
                        settings["sticker"] = False
                        line.sendMessage(to,"ปิดเตะคนรันสติกเกอรแล้ว")
                elif msg.text.lower() == "sleepmode":
                    if settings["replyPesan"] is not None:
                        line.sendMessage(to,"Your Sleepmode is : " + str(settings["replyPesan"]))
                        msgSticker = settings["messageSticker"]["listSticker"]["sleepSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                    else:
                        line.sendMessage(to,"My Sleepmode : No messages are set")
                elif msg.text.lower() == "addsleepmodesticker":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "sleepSticker"
                    line.sendMessage(to, "โปรดส่งสติ๊กเกอร์ที่คุณต้องการเพิ่ม")
                elif msg.text.lower() == "delsleepmodesticker":
                    settings["messageSticker"]["listSticker"]["sleepSticker"] = None
                    line.sendMessage(to, "ลบรายการสติ๊กเกอร์เรียบร้อย")
                elif msg.text.lower().startswith("setsleepmode: "):
                    text_ = msg.text.lower().replace("setsleepmode:", "")
                    try:
                        settings["replyPesan"] = text_
                        line.sendMessage(to,"Sleep mode changed to : " + text_)
                    except:
                        line.sendMessage(to,"SleepMode \nFailed to replace message")
                elif msg.text.lower() == "ติ๊กออก":
                        msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติ๊กออก":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "leaveSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติ๊กออก":
                    settings["messageSticker"]["listSticker"]["leaveSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนออกแล้ว")
                elif msg.text.lower() == "ติ๊กเตะ":
                        msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติ๊กเตะ":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "kickSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติ๊กเตะ":
                    settings["messageSticker"]["listSticker"]["kickSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเตะแล้ว")
                elif msg.text.lower() == "ติ๊กเข้า":
                        msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติ๊กเข้า":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "welcomeSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติ๊กเข้า":
                    settings["messageSticker"]["listSticker"]["welcomeSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว")
                elif msg.text.lower()== "ติ๊กแอด":
                        msgSticker = settings["messageSticker"]["listSticker"]["addSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower()== "ตั้งติ๊กแอด":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "addSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กแอด":
                    settings["messageSticker"]["listSticker"]["addSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว")
                elif msg.text.lower() == "ติ๊กแทค":
                        msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติ๊กแทค":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "responSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กแทค":
                    settings["messageSticker"]["listSticker"]["responSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว")
                elif msg.text.lower() == "ตั้งติ๊กแอบ":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "readerSticker"
                    line.sendMessage(to, "ส่งสติ๊กเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กแอบ":
                    settings["messageSticker"]["listSticker"]["readerSticker"] = None
                    line.sendMessage(to, "ลบสติ๊กเกอรคนแอบอ่านแล้ว")
                elif msg.text.lower() == "ติ๊กแอบ":
                        msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower().startswith("textig "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith(".เขียน"):
                        sep = msg.text.split(" ")
                        textnya = msg.text.replace(sep[0] + " ","")
                        path = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                        line.sendImageWithURL(msg.to,path)
                elif "kedip " in msg.text:
                    txt = msg.text.replace("kedip ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["ดึง"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                            
                elif msg.text.lower() == ".ยกเชิญ":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == ".บอทยก":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])

                elif 'ID line: ' in msg.text:
                  if settings["selfbot"] == True:
                   if msg._from in admin:
                      msgs = msg.text.replace('ID line: ','')
                      conn = line.findContactsByUserid(msgs)
                      if True:
                          line.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                          line.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                elif msg.text.lower().startswith("ไอดีไลน์"):
                    line.reissueUserTicket()
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendFooter(to, "「ไอดีไลน์ของเรา」\n"+str(userid), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)

#=============COMMAND KICKER===========================#
                elif msg.text in ["ดำ"]:
                  if msg._from in admin: 
                    settings["wblacklist"] = True
                    line.sendText(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["ขาว"]:
                  if msg._from in admin: 
                    settings["dblacklist"] = True
                    line.sendText(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["ล้างดำ"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลางบัญชีดำทั้งหมดเรียร้อย")
                    print ("Clear Ban")
                elif msg.text.lower() == "คทบล็อค":
                    if msg._from in lineMID:
                        blockedlist = line.getBlockedContactIds()
                        if blockedlist == []:
                            line.sendMessage(to, "คุณยังไม่ได้บล็อคใคร!")
                        else:
                            for kontak in blockedlist:
                                line.sendMessage(to, text=None, contentMetadata={'mid': kontak}, contentType=13)
                elif msg.text.lower() == "คทดำ":
                    if msg._from in lineMID:
                        if settings["blacklist"] == []:
                            line.sendMessage(to, "Nothing boss")
                        else:
                            for bl in settings["blacklist"]:
                                line.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif '.ลาก่อย' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")

                elif '.สอย' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")                               

                elif '.เชิญ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "Type👉 Invite Succes")
                           except:
                               line.sendMessage(msg.to,"Type👉 Limit Invite")
                elif "บล็อค @" in msg.text:
                    if msg.toType == 2:
                        print ("[block] OK")
                        _name = msg.text.replace("บล็อค @","")
                        _nametarget = _name.rstrip('  ')
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            sendMassage(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                   line.blockContact(target)
                                   line.sendMessage(to, "บล็อคคุณ ✈" + str(g.displayName) + " แล้ว")
                                except Exception as e:
                                   print (e)
                elif msg.text.lower() == '.บล็อค':
                    blockedlist = line.getBlockedContactIds()
                    sendMessage(msg.to, "Please wait...")
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="User Blocked List\n"
                    for ids in kontak:
                        msgs+="\n%i. %s" % (num, ids.displayName)
                        num=(num+1)
                        msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                        sendMessage(msg.to, msgs)
                elif ".ปวดตับ" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace(".ปวดตับ","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"Just some casual cleansing ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"Group cleanse")
                                         print ("Cleanse Group")

                elif msg.text in [".ไล่ดำ"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")
                elif "ชื่อ: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Update to " + string)
                        print ("Update Name")

                elif "ตัส: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Succes Update 👉 " + string)
                        print ("Update Bio Succes")

#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == '.เปิดกัน':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.ปิดกัน':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.กันยก':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.ปิดกันยก':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.กันเชิญ':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.ปิดกันเชิญ':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.กันลิ้ง':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.ปิดกันลิ้ง':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.กันกลุ่ม':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.ปิดกันกลุ่ม':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.กันเข้า':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.ปิดกันเข้า':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.เปิดหมด':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text.lower() == '.ปิดหมด':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

#==============FINNISHING PROTECT========================#
                elif msg.text in ["เปิดรับแขก","เปิดต้อนรับ"]:
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดรับแขก","ปิดต้อนรับ"]:
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                                
                elif msg.text in ["เปิดทักเตะ","เปิดดูเตะ"]:
                        if settings["Nk"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม...", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["Nk"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม...", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                                
                elif msg.text in ["ปิดทักเตะ","ปิดดูเตะ"]:
                        if settings["Nk"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว..", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["Nk"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว...", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text in ["เปิดส่งแขก","เปิดอำลา"]:
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดส่งแขก","ปิดอำลา"]:
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม   ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                                
                elif msg.text in ["เปิดคท","Contact on"]:
                        if settings["checkContact"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบอ่านข้อมูลด้วยคอนแทคไว้อยู่แล้ว ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["checkContact"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบอ่านข้อมูลด้วยคอนแทค", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดคท","Contact off"]:
                        if settings["checkContact"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบอ่านข้อมูลด้วยคอนแทคไว้อยู่แล้ว ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["checkContact"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบอ่านข้อมูลด้วยคอนแทค", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["เปิดเช็คโพส","เปิดเชคโพส"]:
                        if settings["checkPost"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบเช็คโพสบนทามไลน์ไว้อยู่แล้ว ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["checkPost"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบเช็คโพสบนทามไลน์ ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["ปิดเช็คโพส","ปิดเชคโพส"]:
                        if settings["checkPost"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบเช็คโพสบนทามไลน์ไว้อยู่แล้ว ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        else:
                            settings["checkPost"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบเช็คโพสบนทามไลน์", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.text in ["แปลงโฉม","เปลี่ยนรูป"]:
                    settings["changePictureProfile"] = True
                    line.sendMessage(to, "ส่งรูปภาพลงมาได้เลยครับผม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif msg.text in ["เปลี่ยนดิส","เปลี่ยนวีดีโอ"]:
                    settings["changeProfileVideo"] = False
                    line.sendMessage(to, "ส่งรูปวีดีโอลงมาได้เลยครับผม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/FMRCTkb0nl'})

                elif text.lower() == ".อัพวีดีโอ" and sender == lineMID:
                    settings['changeProfileVideo']['status'] = False
                    settings['changeProfileVideo']['stage'] = 1
                    line.sendMessage(to, "「 ส่งวีดีโอลงมาเลยลูกพี่ 」\n•", "\nSend video !", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == "เปลี่ยนรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        line.sendMessage(to, "ส่งรูปภาพลงมาไดเเลยครับผม", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif text.lower() == ".ดับไฟ":
                        line.sendMessage(to, ".God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                        line.sendMessage(to, "เข้านอนได้แล้วเด็กๆ")

                elif text.lower() == 'แจก':
                        line.sendGift(msg.to,'1','sticker')

                elif text.lower() == '.ของขวัญ':
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')
                        line.sendGift(msg.to,'1002077','sticker')

                elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้วขอรับ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
			
                elif ".ลงดำ" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace(".ลงดำ","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"แบนสมาชิกทุกคนในห้องนี้แล้ว＼（○＾ω＾○）／", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
										   
                elif 'แบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes added for the blacklist ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

                elif 'ล้างแบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                
                elif msg.text in ["เช็คดำ","เชคดำ"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'}) 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ติดดำ", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

            elif msg.contentType == 13:
                if settings["checkContact"] == True:
                    try:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        if line != None:
                            cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            line.sendImageWithURL(to, str(path))
                        except:
                            pass
                        ret_ = "[ รายการทั้งหมดจากการสำรวจด้วย คท ]"
                        ret_ += "\n ชื่อ : {}".format(str(contact.displayName))
                        ret_ += "\n ไอดี : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n ตัส : {}".format(str(contact.statusMessage))
                        ret_ += "\n รูปโปรไฟล : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n  รูปปก : {}".format(str(cover))
                        ret_ += "\n[ สิ้นสุดการสำรวจ ]"
                        line.sendMessage(to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                    except:
                        line.sendMessage(to, "เกิดข้อผิดพลาดในการสำรวจ")
            elif msg.contentType == 1:
                if settings["changePictureProfile"] == True:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changePictureProfile"] = False
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "ทำการแปลงโฉมเสร็จเรียบร้อย", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        line.updateGroupPicture(to, path)
                        line.sendMessage(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
            elif msg.contentType == 1:
                if settings['changeProfileVideo']['status'] == True and sender == lineMID:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changeProfileVideo"] = False
                    line.updateProfileVideo(to, path)
                    line.sendMessage(to, "ทำการอัพเดตวีดีโอโปรไฟลเสร็จเรียบร้อย", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                elif msg.contentType in [1,2]:
                    if sender in lineMID:
                        line.sendMessage(to, str(msg))
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "Success Added " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
                   
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
#================
        if op.type == 65:
            #print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
            if settings["ยกเลิกข้อความ"] == True:
                #at = op.param1
                #at = 'Midห้อง'
                at = 'cfb1412d1d409cb8322f25d7f97d783fa'
                msg_id = op.param2
                if msg_id in msg_dict:
                    ah = time.time()
                    ginfo = line.getGroup(at)
                    ariftj = line.getContact(msg_dict[msg_id]["from"])
                    if "tes" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        waktumsg = format_timespan(waktumsg)
                        ret_ = "• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                        line.sendMessage(at, str(ret_))
                        line.sendImage(at, msg_dict[msg_id]["tes"])
                        del msg_dict[msg_id]
                        print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                    else:
                        if "tes" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            line.sendImage(at, msg_dict[msg_id]["tes"])
                            del msg_dict[msg_id]
                        else:
                            if "tes" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                line.sendImage(at, msg_dict[msg_id]["tes"])
                                del msg_dict[msg_id]
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    #contact = line.getContact(op.param2)
                    #contact = line.getContact(msg._from)
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = line.getGroup(at)
                                ariftj = line.getContact(msg_dict1[msg_id]["from"])
                               # contact = line.getContact(op.param2)
                                ret_ =  "「 ตรวจพบการยกเลิกสติกเกอร์ 」\n\n"
                                ret_ += "• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                                ret_ += "\n• ชื่อกลุ่ม : {}".format(str(ginfo.name))
                                #ret_ += "\n• เวลาส่ง : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                line.sendMessage(at, str(ret_))
                                line.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                        print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                except Exception as e:
                    #print(e)
                    print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")

#=====
        if op.type == 65:
            #print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
            if settings["unsendMessage"] == True:
                at = op.param1
                msg_id = op.param2
                if msg_id in msg_dict:
                  #  if msg_dict[msg_id]["from"] not in manlovebot:
                    ah = time.time()
                    #ikkeh = line.getContact(msg_dict[msg_id]["from"])
                    ginfo = line.getGroup(at)
                    
                    ariftj = line.getContact(msg_dict[msg_id]["from"])
                    if "text" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        waktumsg = format_timespan(waktumsg)
                        ret_ = "「 ตรวจพบการยกเลิกข้อความ 」\n\n• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                        ret_ += "\n\n• ข้อความที่ถูกยกเลิก : {}".format(str(msg_dict[msg_id]["text"]))
                        #rat_ = "\nSend At :\n{} ago".format(waktumsg)
                        #rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                        #sendMention(at, ikkeh.mid, " ** Resend Message **\n\nMaker :\n", str(rat_))
                        line.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                        print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                    else:
                        if "image" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            ret_ = "「 ตรวจพบการยกเลิกรูปภาพ 」\n\n• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                            ret_ += "\n\n• ☟☟รูปภาพที่ถูกยกเลิก☟☟"
                          #  ret_ =  "「 ตรวจพบการยกเลิกข้อความ 」\n\n"
                           # ret_ += "• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                           # ret_ += "\n• ชื่อกลุ่ม : {}".format(str(ginfo.name))
                            #ret_ += "\n• เวลาส่ง: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                           # ret_ += "\n• ข้อความที่ถูกยกเลิก : {}".format(str(msg_dict[msg_id]["text"]))
                            #line.sendMessage(at,"[ตรวจพบการยกเลิกข้อความ]\n\n[ชื่อ]: %s\n\n[ข้อความที่ถูกยกเลิก]:\n%s"%(line.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            #line.sendMessage(at, str(ret_))
                           # rat_ = "\nSend At :\n{} ago".format(waktumsg)
                           # rat_ += "\nImage :\nBelow"
                            #line.sendMessage(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                            #line.sendMessage(at, "「 ตรวจพบการยกเลิกรูปภาพ 」")
                            line.sendMessage(at, str(ret_))
                            line.sendImage(at, msg_dict[msg_id]["image"])
                    #        line.sendMessage("c2d6930f9e4a7c5ba829961f028f88244", str(ret_))
                     #       line.sendMessage("c2d6930f9e4a7c5ba829961f028f88244", msg_dict[msg_id]["image"])
                           # line.sendMessage(at,"[ตรวจพบการยกเลิกข้อความ]\n\n[ชื่อ]: %s\n\n[ข้อความที่ถูกยกเลิก]:\n%s"%(line.getContact(msg_dict[msg_id]["from"])))
                            #line.sendMessage(at, str(ret_))
                            del msg_dict[msg_id]
                            print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                        else:
                            if "video" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                ret_ = "「 ตรวจพบการยกเลิกวีดีโอ 」\n\n• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                                ret_ += "\n\n• ☟☟วีดีโอที่ถูกยกเลิก☟☟"
                                #rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                #rat_ += "\nVideo :\nBelow"
                                #sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                line.sendMessage(at, str(ret_))
                                line.sendVideo(at, msg_dict[msg_id]["video"])
                                del msg_dict[msg_id]
                                print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                            else:
                                if "audio" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    ret_ = "「 ตรวจพบการยกเลิกข้อความเสียง 」\n\n• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                                    ret_ += "\n\n• ☟☟ข้อความเสียงที่ถูกยกเลิก☟☟"
                                    #rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    #rat_ += "\nAudio :\nBelow"
                                    #sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                    line.sendMessage(at, str(ret_))
                                    line.sendAudio(at, msg_dict[msg_id]["audio"])
                                    del msg_dict[msg_id]
                                    print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                                else:
                                    if "mansticker" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        #rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        #rat_ += "\nSticker :\nBelow"
                                      #  sendMention(at, ikkeh.mid, " ** Resend Message **\n\nMaker :\n", str(rat_))
                                        line.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                        del msg_dict[msg_id]
                                        print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                                    else:
                                        if "mid" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            ret_ = "「 ตรวจพบการยกเลิกคอนแทค 」\n\n• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                                            ret_ += "\n\n• ☟☟คอนแทคที่ถูกยกเลิก☟☟"
                                            #rat_ = "\nSend At :\n~ {} ago".format(waktumsg)
                                            #rat_ += "\nContact :\nBelow"
                                            #sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                            line.sendMessage(at, str(ret_))
                                            line.sendContact(at, msg_dict[msg_id]["mid"])
                                            del msg_dict[msg_id]
                                            print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                                        else:
                                            if "lokasi" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                #rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                               # rat_ += "\nLocate :\nBelow"
                                                #sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                                line.sendLocation(at, msg_dict[msg_id]["lokasi"])
                                                del msg_dict[msg_id]
                                                print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                                            else:
                                                if "file" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    #rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    #rat_ += "\nFile :\nBelow"
                                                   # sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                                    ret_ = "「 ตรวจพบการยกเลิกไฟล์ 」\n\n• ผู้ยกเลิก : {}".format(str(ariftj.displayName))
                                                    ret_ += "\n\n• ☟☟ไฟล์ที่ถูกยกเลิก☟☟"
                                                    line.sendMessage(at, str(ret_))
                                                    line.sendFile(at, msg_dict[msg_id]["file"])
                                                    del msg_dict[msg_id]
                                                    print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")
                                                else:
                                                    print ("[ 65 ] ตรวจพบการยกเลิกข้อความ [ 65 ]")

#============
        if op.type == 19:
         if settings["1คิก"] == True:
            if op.param3 in lineMID:
                if op.param2 in m1MID:
                    pass
                else:
                    try:
                        G = m1.getGroup(op.param1)
                        ginfo = m1.getGroup(op.param1)
                        m1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        m1.updateGroup(G)
                        invsend = 0
                        Ticket = m1.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = m1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        m1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            settings["blacklist"][op.param2] = True
                        except:
                            pass
                return
            if op.param3 in m1MID:
                if op.param2 in lineMID:
                    pass
                else:
                    try:
                        G = line.getGroup(op.param1)
                        ginfo = line.getGroup(op.param1)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        m1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            settings["blacklist"][op.param2] = True
                        except:
                            pass
                return
#================
        if op.type == 19:
         if settings["2คิก"] == True:
            if op.param3 in lineMID:
                if op.param2 in m1MID:
                    pass
                else:
                    try:
                        G = m1.getGroup(op.param1)
                        ginfo = m1.getGroup(op.param1)
                        m1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        m1.updateGroup(G)
                        invsend = 0
                        Ticket = m1.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        m2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = m1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        m1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            settings["blacklist"][op.param2] = True
                        except:
                            pass
                return
            if op.param3 in m1MID:
                if op.param2 in m2MID:
                    pass
                else:
                    try:
                        G = m2.getGroup(op.param1)
                        ginfo = m2.getGroup(op.param1)
                        m2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        m2.updateGroup(G)
                        invsend = 0
                        Ticket = m2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        m1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        m2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = m2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        m2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            settings["blacklist"][op.param2] = True
                        except:
                            pass
                return
            if op.param3 in m2MID:
                if op.param2 in m1MID:
                    pass
                else:
                    try:
                        G = m1.getGroup(op.param1)
                        ginfo = m1.getGroup(op.param1)
                        m1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        m1.updateGroup(G)
                        invsend = 0
                        Ticket = m1.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        m1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        m2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = m1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        m1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            settings["blacklist"][op.param2] = True
                        except:
                            pass
                return
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)              
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)             
#==============================================================================#
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])
        
        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])


        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    #settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    #random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    line.sendMentionFooter(op.param1, "「อย่าเล่นลิ้งกลุ่มจ๊ะ」:", op.param2, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(op.param2).pictureStatus, line.getContact(op.param2).displayName)
                    line.sendContact(op.param1, op.param2)
                    #m1.sendMessage(op.param1, "☝ อย่าเล่นลิ้งกลุ่ม")


        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    #random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])

        if op.type == 5:
            if RfuProtect["autoBlock"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["comment1"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["comment1"]))
        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in settings["blacklist"] == {}:
                line.kickoutFromGroup(op.param1,[op.param2])
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                line.sendText(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "Success Added " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
                            
#======
        if op.type == 25:
          if settings ["MANBOTLINE"] == False:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                elif msg.text in ["เปิดเซลบอท","เปิดเซล"]:
                    settings["MANBOTLINE"] = True
                    line.sendMessage(to, "➠ เปิดระบบเซลบอทแล้ว")
#=======

#==============================================================================================================
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 1:
                    if settings["ยกเลิกข้อความ"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"tes":path,"waktu":unsendmsg1}
                        except Exception as e:
                            #print (e)
                            print ("[ 65 ] เออเร่อ [ 65 ]")
#==============================================================================================================
        if op.type == 26:
 #            if settings ["mutebot2"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
               # if botman["Manbot"] == True:
                 #   line.sendChatChecked(to, msg_id)
                if msg.contentType == 0:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"lokasi":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            #print (e)
                            print ("[ 65 ] เออเร่อ [ 65 ]")
                if msg.contentType == 1:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            #print (e)
                            print ("[ 65 ] เออเร่อ [ 65 ]")
                #if msg.contentType == 2:
                    #if settings["vdoman"] == True:
                       # try:
                           # unsendmsg2 = time.time()
                            #path = line.downloadObjectMsg(msg_id)
                           # msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                       # except Exception as e:
                           # print (e)
                if msg.contentType == 3:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            #print (e)
                            print ("[ 65 ] เออเร่อ [ 65 ]")
             #   if msg.contentType == 7:
                 #   if settings["unsendMessage"] == True:
                    #    try:
                     #       unsendmsg7 = time.time()
                        #    sticker = msg.contentMetadata["STKID"]
                       #     link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                         #   msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                     #   except Exception as e:
                          #  print (e)
               # if msg.contentType == 7:
                  #if wait["sticker"] == True:
                     #msg.contentType = 0
                     #line.sendMessage(msg.to,"「Cek ID Sticker」\n🔰 STKID : " + msg.contentMetadata["STKID"] + "\n?? STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n🔰 STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
                if msg.contentType == 7:
                       stk_id = msg.contentMetadata["STKID"]
                       stk_ver = msg.contentMetadata["STKVER"]
                       pkg_id = msg.contentMetadata["STKPKGID"]
                       ret_ = "\n\n「 Sticker Info 」"
                       ret_ += "\n• Sticker ID : {}".format(stk_id)
                       ret_ += "\n• Sticker Version : {}".format(stk_ver)
                       ret_ += "\n• Sticker Package : {}".format(pkg_id)
                       ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                       query = int(stk_id)
                       if type(query) == int:
                                data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                                path = line.downloadFileURL(data)
                                msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 13:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            #print (e)
                            print ("[ 65 ] เออเร่อ [ 65 ]")
                if msg.contentType == 14:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            #print (e)
                            print ("[ 65 ] เออเร่อ [ 65 ]")
#=========================


#============================
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if settings["autoRead"] == True:
                        line.sendChatChecked(to, msg_id)				
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        #line.sendMessage(msg.to,text)
                        #line.sendMessage(wait["bc"],text)
                        a = line.getGroupIdsJoined()
                        for manusia in wait["bc"]:
                            if manusia in a:
                                #line.sendText(manusia,(text))
                                line.sendText(manusia,"    「 ระบบอัตโนมัต 」    \n" + (text) + "\n By.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                                #time.sleep(0.1)
                  #  line.sendText(receiver,"「 ส่งกลุ่มที่ปักหมุดแล้ว 」")

                elif msg.contentType == 7:
                    if settings["checkSticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            line.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            #line.sendMessage(to, str(ret_))                            
                        except Exception as error:
                            line.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in lineMID:
                            try:
                                line.kickoutFromGroup(msg.to,[sender])
                                line.sendMessage("คุณพูดคำต้องห้าม จำเป็นต้องนำออก sorry(╯°□°）╯︵ ┻━┻", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "🔰เข้าร่วมไปในกลุ่ม??\n🔀👉 %s 👈 เรียบร้อยแล้ว\n🔷โดยผ่านการแชร์ด้วยลิ้งค์🔷" % str(group.name), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                if msg.toType == 0 and settings["autoReply"] and sender != lineMID:
                    contact = line.getContact(sender)
                    rjct = ["auto", "ngetag"]
                    validating = [a for a in rjct if a.lower() in text.lower()]
                    if validating != []: return
                    if contact.attributes != 32:
                        msgSticker = settings["messageSticker"]["listSticker"]["sleepSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                        if "@!" in settings["replyPesan"]:
                            msg_ = settings["replyPesan"].split("@!")
                            sendMention(to, sender, "Sleep Mode :\n" + msg_[0], msg_[1])
                        sendMention(to, sender, "Sleep Mode :\nว่าไงคับ", settings["replyPesan"])
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    if settings["detectMentionPM"] == True:
                        groupman = line.getGroup(msg.to)
                        contact = line.getContact(msg._from)
                        cName = contact.pictureStatus
                        mi_d = contact.mid
                        balas = ["http://dl.profile.line-cdn.net/" + cName]
                        ret_ = random.choice(balas)
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                #sendMention(sender, sender, "          「ตอบแทคอัตโนมัติ」          \n「จากห้อง」"+ str(groupman.name) +"\n", "\n"+ str(settings["pmMessage"]) +"\n\nBy.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                                #sendMention(sender, sender, "          「ตอบแทคอัตโนมัติ」          \n", "\n\n"+ str(settings["pmMessage"])+"\n\nBy.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                                #sendMention(msg.to, sender, "          「ตอบแทคอัตโนมัติ」          \n「จากห้อง」"+str(gs.name)+"\n", "\n"+ str(settings["pmMessage"])+"\n\nBy.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                                #sendMention(sender, sender, "「จากห้อง」"+str(gss.name))
                                #line.sendMessage(sender, to, "「จากห้อง」"+str(gss.name))
                                sendMention(sender, sender, "         「ตอบแทคอัตโนมัติ」         \n", "\nจากห้อง☞"+str(groupman.name)+"\n\n"+ str(settings["pmMessage"])+"\n\nBy.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                           #     line.sendMessage(sender, sender, "         「ตอบแทคอัตโนมัติ」         \n\nจากห้อง☞"+str(groupman.name)+"\n\n"+ str(settings["pmMessage"])+"\n\nBy.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                                #line.sendContact(sender, mi_d)
                                print ("[   0   ]『แทคกลับทางแชท』")
                               # line.sendImageWithURL(sender,ret_)
                                break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                         if settings["Mentiongift"] == True:
                             groupman = line.getGroup(msg.to)
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                  if mention ['M'] in lineMID:
                                     #idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                                     idth = ["ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","a0768339-c2d3-4189-9653-2909e9bb6f58","a0768339-c2d3-4189-9653-2909e9bb6f58","3cc08ba6-5d04-4c52-ab76-651231ead8ef"]
                                     plihth = random.choice(idth)
                                     jenis = ["8","7","6","5"]
                                     plihjenis = random.choice(jenis)
                                     line.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                                     line.sendMessage(msg._from, None, contentMetadata={'mid':"u6fc71977555896280f337a1094664f5f"}, contentType=13)
                                     line.sendMessage(msg._from, "🎁จากเพจ 『ℳ₳N』฿✪₮ᴸᴵᶰᵉ ☝ ครับ🎁\n💞ฝาก@เพื่อน กดติดดาว🌟ฝากไลค์ ฝากแชร์ให้ด้วยนะครับ ขอบคุณมากๆครับ😘")
                                     print ("[   0   ]『แจกของขวัญคนแทค』")
                                     break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
        	             if settings['kickMention'] == True:
        		             contact = line.getContact(msg._from)
        		             cName = contact.displayName
        		             balas = ["เนื่องจากตอนนี้ผมเปิดระบบเตะคนแทคไว้ " + "\n👉" + cName + "\n🙏ต้องขออภัยด้วยจริงๆ🙏Bye!!!"]
        		             ret_ = "" + random.choice(balas)                     
        		             name = re.findall(r'@(\w+)', msg.text)
        		             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
        		             mentionees = mention["MENTIONEES"]
        		             for mention in mentionees:
        			               if mention['M'] in admin:
        				                  line.sendText(msg.to,ret_)
        				                  line.kickoutFromGroup(msg.to,[msg._from])
        				                  print ("[   0   ]『เตะคนแทค』")
                                          #print ("[   0   ]『เตะคนแทค』")
                                          #break
        				                  break                                  
        
        			               if mention['M'] in lineMID:
        				                  line.sendText(msg.to,ret_)
        				                  line.kickoutFromGroup(msg.to,[msg._from])
        				                  break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          line.sendContact(msg.to, mi_d)
                                          print ("[   0   ]『รูปคนแทค』")
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             #icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                             #name = "ข้อความคนแทค"                   
                             #link = "http://line.me/ti/p/~botline2034"
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["『 ตอบกลับคำแทคอัตโนมัติ』\n\n " + cName]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          #line.sendMessage(to,ret_, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                                          line.sendMentionFooter(to,  "『 ตอบกลับคำแทคอัตโนมัติ』\n\n", contact.mid, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(contact.mid).pictureStatus, line.getContact(contact.mid).displayName)
                                          line.sendMessage(to,str(settings["Respontag"]), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                                          msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                                          if msgSticker != None:
                                              sid = msgSticker["STKID"]
                                              spkg = msgSticker["STKPKGID"]
                                              sver = msgSticker["STKVER"]
                                              sendSticker(to, sver, spkg, sid)
                                              print ("[   0   ]『ตอบแทคออโต้』")
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['delayMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          sendMessageWithMention(to, contact.mid)
                                          break

#===========บอทแทค========
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                elif msg.text.lower().startswith("พูด "):
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        sep = text.split(" ")
                        say = text.replace(sep[0] + " ","")
                        lang = 'th'
                        tts = gTTS(text=say, lang=lang)
                        tts.save("hasil.mp3")
                        line.sendAudio(msg.to,"hasil.mp3")
                elif text.lower() == 'แจก':
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        line.sendGift(msg.to,str(settings["Ssk"]),'sticker')
                elif msg.text.lower().startswith("id "):
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        id = msg.text.lower().replace("id ","")
                        conn = line.findContactsByUserid(id)
                        if True:                                      
                            line.sendMessage(to,"http://line.me/ti/p/~" + id)
                            line.sendContact(to,conn.mid)
                elif msg.text.lower().startswith("id: "):
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        id = msg.text.lower().replace("id: ","")
                        conn = line.findContactsByUserid(id)
                        if True:                                      
                            line.sendMessage(to,"http://line.me/ti/p/~" + id)
                            line.sendContact(to,conn.mid)
                elif msg.text.lower().startswith("id:"):
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        id = msg.text.lower().replace("id:","")
                        conn = line.findContactsByUserid(id)
                        if True:                                      
                            line.sendMessage(to,"http://line.me/ti/p/~" + id)
                            line.sendContact(to,conn.mid)
                elif msg.text.lower().startswith("ไอดีไลน์ "):
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        id = msg.text.lower().replace("ไอดีไลน์ ","")
                        conn = line.findContactsByUserid(id)
                        if True:                                      
                            line.sendMessage(to,"http://line.me/ti/p/~" + id)
                            line.sendContact(to,conn.mid)
                elif msg.text.lower().startswith("เขียน "):
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        sep = msg.text.split(" ")
                        textnya = msg.text.replace(sep[0] + " ","")
                        urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                        line.sendImageWithURL(msg.to, urlnya)
                elif text.lower() == 'แอด':
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        group = line.getGroup(to)
                        GS = group.creator.mid
                        line.sendContact(to, GS)
                        line.sendMessage(to, "⬆️⬆️ผู้สร้างกลุ่ม⬆️⬆️")
                elif "ยูทูป " in msg.text.lower():
                    if botman["Manbot"] == True:
                     if msg._from in settings["admin1"]:
                        sep = text.split(" ")
                        search = text.replace(sep[0] + " ","")
                        params = {"search_query": search}
                        with requests.session() as web:
                            web.headers["User-Agent"] = random.choice(settings["userAgent"])
                            r = web.get("https://www.youtube.com/results", params = params)
                            soup = BeautifulSoup(r.content, "html.parser")
                            ret_ = "╔══[ ผลการค้นหา ]"
                            datas = []
                            for data in soup.select(".yt-lockup-title > a[title]"):
                                if "&lists" not in data["href"]:
                                    datas.append(data)
                            for data in datas:
                                ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                                ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                            ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                            line.sendMessage(to, str(ret_))
                elif msg.text in ["กลุ่ม"]:
                    if botman["Manbot"] == True:
                     #if msg._from in admin1:
                     if msg._from in settings["admin1"]:
                        group = line.getGroup(to)
                        try:
                            gCreator = group.creator.displayName
                        except:
                            gCreator = "ผู้สร้างได้ลบบัญชีไปแล้ว"
                        if group.invitee is None:
                            gPending = "0"
                        else:
                            gPending = str(len(group.invitee))
                        if group.preventedJoinByTicket == True:
                            gQr = "ปิด"
                            gTicket = "ลิ้งกลุ่มปิดอยู่"
                        else:
                            gQr = "เปิด"
                            gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                        timeCreated = []
                        timeCreated1 = []
                        timeCreated.append(time.strftime("%d-%m-%Y", time.localtime(int(group.createdTime) / 1000)))
                        timeCreated1.append(time.strftime("%H:%M:%S", time.localtime(int(group.createdTime) / 1000)))
                        path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        ret_ = "╔══[ ข้อมูลกลุ่ม ]"
                        ret_ += "\n╠ ชื่อกลุ่ม : {}".format(str(group.name))
                        ret_ += "\n╠ ID กลุ่ม : {}".format(group.id)
                        ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                        ret_ += "\n╠ วันที่สร้างกลุ่ม : {}".format(str(timeCreated))
                        ret_ += "\n╠ เวลาที่สร้างกลุ่ม : {}".format(str(timeCreated1))
                        ret_ += "\n╠ จำนวน สมาชิก : {}".format(str(len(group.members)))
                        ret_ += "\n╠ จำนวน ค้างเชิญ : {}".format(gPending)
                        ret_ += "\n╠ ลิ้งกลุ่ม : {}".format(gQr)
                        ret_ += "\n╠ ลิ้ง : {}".format(gTicket)
                        ret_ += "\n╚══[ By. ℳ₳N ※ ฿✪₮]"
                        line.sendMessage(to, str(ret_))
                        line.sendImageWithURL(to, path)
                elif msg.text.lower().startswith("me "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                     if msg._from in settings["admin1"]:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                     if msg._from in settings["admin1"]:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                         if msg._from in settings["admin1"]:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text in ["คิกมา","บอทมา","กลับมา"]:
                    if msg._from in settings["admin1"]:
                     if msg.toType == 2:
                 #    if msg._from in admin:
                        group = line.getGroup(to)
                        group.preventedJoinByTicket = False
                        line.updateGroup(group)
                        invsend = 0
                        ticket = line.reissueGroupTicket(to)
                        m1.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        #kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        #time.sleep(0.01)
                       # kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        #time.sleep(0.01)
                        #ke.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        #time.sleep(0.01)
                        group.preventedJoinByTicket = True
                        m1.updateGroup(group)
                        print ("Kicker Join")
              #  elif msg.text in ["คิกออก","บอทออก","คิกเกอร์ออก"]:
                  #  if msg._from in settings["admin1"]:
                 #       m1.leaveGroup(msg.to)
                       # kk.leaveGroup(msg.to)
                        #kc.leaveGroup(msg.to)
                       # ke.leaveGroup(msg.to)                        
                      #  print ("Kicker Leave")
                #elif msg.text in ["แมนออก"]:
                    #if msg._from in settings["admin1"]:
                        #m1.leaveGroup(msg.to)
                      #  kk.leaveGroup(msg.to)
                       # kc.leaveGroup(msg.to)
                     #   ke.leaveGroup(msg.to)
                        #line.leaveGroup(msg.to)
                        #kc.leaveGroup(msg.to)
                       # ke.leaveGroup(msg.to)                        
                        #print ("Kicker Leave")
                elif 'เตะ' in text.lower():
                    if msg._from in settings["admin1"]:
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               m1.kickoutFromGroup(msg.to,[target])           
                               print ("K1 Kick User")
                           except:
                               m1.sendMessage(msg.to,"Limit kaka 😫")
                elif msg.text in ["แอดมิน","เชคแอดมิน","Listadmin"]:
                  if botman["Manbot"] == True:
                    if msg._from in settings["admin1"]:
                        ma = ""
                        mb = ""
                        mc = ""
                        a = 0
                        b = 0
                        c = 0
                        for m_id in settings["admin1"]:
                            b = b + 1
                            end = '\n'
                            mb += str(b) + ". " +line.getContact(m_id).displayName + "\n"
                        #line.sendMessage(msg.to,"💻 BOT admin\n\nAdmin:\n"+mb+"\nTotal「%s」Admin" %(str(len(admin))))
                        #line.sendMessage(msg.to,"💻 BOT admin\n\nAdmin:\n"+mb+"\nTotal「%s」Admin" %(str(len(settings["admin1"]))))
                        line.sendMessage(msg.to,"    「 รายชื่อแอดมิน 」\n\n"+mb+"\n   จำนวน「%s」แอดมิน" %(str(len(settings["admin1"]))))
                elif msg.text in ["เชคดำ"]:
                  if botman["Manbot"] == True:
                    if msg._from in settings["admin1"]:
                        ma = ""
                        mb = ""
                        mc = ""
                        a = 0
                        b = 0
                        c = 0
                        for m_id in settings["blacklist"]:
                            b = b + 1
                            end = '\n'
                            mb += str(b) + ". " +line.getContact(m_id).displayName + "\n"
                        #line.sendMessage(msg.to,"💻 BOT admin\n\nAdmin:\n"+mb+"\nTotal「%s」Admin" %(str(len(admin))))
                        line.sendMessage(msg.to,"☠รายชื่อผู้ติดดำ☠\n\n"+mb+"\nจำนาน「%s」คน" %(str(len(settings["blacklist"]))))
                elif msg.text in ["Cctv on","เปิด อ่าน.","เปิดอ่าน.","เปิดแอบ"]:
                    if msg._from in settings["admin1"]:
                     try:
                     #if msg._from in settings["admin1"]:
                         del RfuCctv['point'][msg.to]
                         del RfuCctv['sidermem'][msg.to]
                         del RfuCctv['cyduk'][msg.to]
                     except:
                         pass
                     RfuCctv['point'][msg.to] = msg.id
                     RfuCctv['sidermem'][msg.to] = ""
                     RfuCctv['cyduk'][msg.to]=True
                     line.sendMessage(msg.to,"แสดงรายชื่อคนที่อ่านทีละคนเริ่มทำงาน")
                elif msg.text in ["Cctv off","ปิดอ่าน.","ปิด อ่าน.","ปิดแอบ"]:
                   # if msg.to in RfuCctv['point']:
                    if msg._from in settings["admin1"]:
                   #  if msg._from in settings["admin1"]:
                     if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    #else:
                        #line.sendMessage(msg.to, "Cctv Already Off")
                #elif msg.text in ["Me","me","คท","ใครหล่อ","ใครสวย"]:
                elif msg.text in [".คท"]:
                    sendMessageWithMention(to, sender)
                    line.sendContact(to, sender)
                    #line.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                    line.sendText(receiver,sender)
                elif msg.text in ["Me","me","คท"]:
                  if msg._from in settings["admin1"]:
                    sendMessageWithMention(to, sender)
                    line.sendContact(to, sender)
                    #line.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                    line.sendText(receiver,sender)
                elif 'Gift: ' in msg.text:
                  if botman["Manbot"] == True:
                   if msg._from in settings["admin1"]:
                      korban = msg.text.replace('Gift: ','')
                      korban2 = korban.split()
                      midd = korban2[0]
                      jumlah = int(korban2[1])
                      if jumlah <= 1000:
                          for var in range(0,jumlah):
                              ki.sendMessage(midd, None, contentMetadata={'PRDID': '168d03c3-dbc2-456f-b982-3d6f85f52af2', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}, contentType=9)
                elif msg.text in ["/เปิดลิ้ง"]:
                  if msg._from in settings["admin1"]:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "➠ ลิ้งเปิดยุแล้ว")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "➠ เปิดลิ้งแล้ว")
                elif msg.text in ["ปิดลิ้ง"]:
                  if msg._from in settings["admin1"]:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "➠ ลิ้งปิดยุแร้ว")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "➠ ปิดลิ้งแร้ว")
                elif msg.text.lower() == 'เปิดลิ้ง':
                  if botman["Manbot"] == True:
                    #if msg._from in admin:
                    if msg._from in settings["admin1"]:
                        if msg.toType == 2:
                           x = line.getGroup(msg.to)
                           if x.preventedJoinByTicket == True:
                              x.preventedJoinByTicket = False
                              line.updateGroup(x)
                           gurl = line.reissueGroupTicket(msg.to)
                           line.sendMessage(msg.to, "ชื่อกลุ่ม : "+str(x.name)+ "\nลิ้งกลุ่ม : http://line.me/R/ti/g/"+gurl)
#===================================                
                elif msg.text in ["นับ"]:
                  if msg._from in settings["admin1"]:
                    line.sendMessage(msg.to, "กรุณาพิม➠ อ่าน")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("นับ")
                elif msg.text in ["อ่าน"]:
                  if msg._from in settings["admin1"]:
                    if msg.to in wait2['readPoint']:
                        print ("อ่าน")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        #line.sendText(msg.to, "🌟รายชื่อคนที่อ่าน🌟%s\n\n🌟รายชื่อคนที่อ่าน🌟\n%s\nสั่งนับเวลา[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        line.sendText(msg.to, "           [ By. ℳ₳N ※ ฿✪₮]%s\n          🌟รายชื่อคนที่อ่าน🌟\n%s\n🌹🌹สั่งนับเมื่อเวลา[%s]🌹🌹" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        line.sendMessage(msg.to, "ไม่สามารถทำการอ่านได้กรุณาพิม➠ นับ")
                elif msg.text in ["แทค","มอง"]:
                  if msg._from in settings["admin1"]:
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    else:
                        line.sendMessage(to, "「 จำนวนสมาชิก {} คน 」".format(str(len(nama))))
#=============================================
#=======
                elif text.lower() == 'คำสั่ง':
                  if msg._from in settings["admin1"]:
                    helpKi = helpki()
                    line.sendMessage(to, str(helpKi))
                elif msg.text in ["///ล้างดำ"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"➠ ทำการลบบัญชีดำทั้งหมดเรียบร้อยแล้ว")
                    print ("Clear Ban")

                elif msg.text in ["แมน","พี่แมน","ตาแมน"]:
                    line.sendMentionFooter(to,  "『 ข้อความอัตโนมัต 』\n\nเรียกผมมีธุระอะไรครับ\n", sender, "https://line.me/ti/p/manbotline", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                    print ("แมน มีคนเรียก")
#================================
#===========ชุด API คำสั่งใช้งานบอทสิริเชนวี10 ========================== 
        if op.type == 26:
            msg = op.message
            if settings ["Aip"] == True:
            	if msg.text in ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ",".","ปลิว"]:
                    line.kickoutFromGroup(receiver,[sender])
                    line.sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")
            if settings ["Aip"] == True:
                if msg.text in ["ควย","หี","แตด","เย็ดแม่","เย็ดเข้","ค.วย","สัส","เหี้ย","ไอ้เหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้แมน","ไอ้เหี้ยแมน","ไอ่แมน","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ"]:
                    line.kickoutFromGroup(receiver,[sender])
                    line.sendText(msg.to,"ตรวจพบคำพูดหยาบคายไม่สุภาพ จำเป็นต้องนำออกเพื่อความสงบสุขของสมาชิก (｀・ω・´)")
           # if settings ["Api"] == True:
            #    if msg.text in ["ป๊า","ป๊าเรส","ลุง","เรส","นาย","เพื่อน","จาร์ย","อาจาร์ย","เฮีย"]:
                #    line.sendMessage(msg.to, str(settings["comment1"]))
          #  if settings ["Api"] == True:
              #  if msg.text in ["เซล","เซลบอท","selfbot","ขายบอท"]:
                   # line.sendMessage(msg.to, str(settings["comment"]))
                 #   line.sendMessage(msg.to, None, contentMetadata={"STKID":"52114123","STKPKGID":"11539","STKVER":"1"}, contentType=7)
         #   if settings ["Api"] == True:
            #    if msg.text in ["55","555","5555","55555","55+","555+","5555+","ขำ",".ขำ"]:
                   # line.sendText(msg.to,"ฮ่าๆๆๆ..ขำไรจ๊ะ..\n😆มึงไปโดนตัวใหนมาเนี่ย😆")
                  #  line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626504","STKPKGID":"11538","STKVER":"1"}, contentType=7)
           # if settings ["Api"] == True:
              #  if msg.text in [".ประกาศ","โฆษณา","ประชาสัมพัน","ประกาศ"]:
             #       line.sendMessage(msg.to, str(settings["comment1"]))
                #    line.sendMessage(msg.to, None, contentMetadata={"STKID":"52114123","STKPKGID":"11539","STKVER":"1"}, contentType=7)
           # if settings["Api"] == True:
             #   if msg.text in ["กำ","กำหำ","กำหอย"]:
                 #   line.sendText(msg.to,"กำเบาๆนะเค้าเจ็บ😁😁")
                   # line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626498","STKPKGID":"11538","STKVER":"1"}, contentType=7)
           # if settings["Api"] == True:
               # if msg.text in ["งง","งงง",]:
                   # line.sendText(msg.to,"ไม่ต้องงงคับ ผมหล่อแบบนี้มาตั้งนานแล้ว😂😂")
                   # line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626512","STKPKGID":"11538","STKVER":"1"}, contentType=7)
           # if settings["Api"] == True:
               # if msg.text in ["หรา","หราา",]:
                   # line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626516","STKPKGID":"11538","STKVER":"1"}, contentType=7)
            #if settings ["Api"] == True:
               # if msg.text in ["อยู่ไหม","เช็คบอท","/เทส","ออนใหม"]:
                   # line.sendText(msg.to,"🔷บอททำงานอยู่ 100%🔶")
            if settings ["Api"] == True:
                if msg.text in ["สวัดดี","หวัดดี","ดีจ้า","ดีครับ","ดี","สวัสดีครับ","สวัสดีค่ะ","ดีงับๆ","ดีงับ","หวัดดีงับๆ"]:
                    line.sendText(msg.to,"สวัสดีครับ ผมชื่อแมนนะ ยินดีที่ได้รู้จัก")
          #  if settings ["Api"] == True:
              #  if msg.text in ["/ตั้งเวลา",".ตั้งเวลา",".ตั้ง","/ตั้ง","/จับ"]:
                   # line.sendText(msg.to,"🔷กำลังรีเซ็ทระบบตั้งค่าคนอ่าน🔷")
                   # line.sendText(msg.to,".จับ")
            #if settings ["Api"] == True:
              #  if msg.text in ["/อ่าน",".คนอ่าน","/คนอ่าน","/ใครอ่าน",".ใครอ่าน"]:
                  #  line.sendText(msg.to,"🔷ตรวจสอบรายชือคนอ่าน🔷")
                  #  line.sendText(msg.to,".อ่าน") 
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                        try:
                            ret_ = "[ ข้อมูลของโพสนี้ ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = line.getContact(msg._from)
                                auth = "\n  ผู้เขียนโพส : {}".format(str(contact.displayName))
                            else:
                                auth = "\n  ผู้เขียนโพส : {}".format(str(msg.contentMetadata["serviceName"]))
                            purl = "\n  ลิ้งโพส : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                            ret_ += auth
                            ret_ += purl
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n  Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "text" in msg.contentMetadata:
                                text = "\n ข้อความโดยย่อ : {}".format(str(msg.contentMetadata["text"]))
                                ret_ += text
                            ret_ += "\n[ สิ้นสุดการเช็คโพส ]"
                            line.sendMessage(to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        except:
                            line.sendMessage(to, "เกิดข้อผิดะลาดในการเช็คโพสนี้", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})

        #if op.type in [25,26]:
        if op.type ==25:
            msg = op.message
            if settings ["Api"] == True:
                if msg.text in ["รองแอด","รอง","แอดรอง","แอดสำรอง","@2","@@"]:
                    line.sendText(msg.to,"Siriv10:extracreator")
                    line.sendText(msg.to,"👆คนนี้คือแอดสำรองห้องนี้")#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})            
            if settings ["Api"] == True:
                if msg.text in ["เช็ค","เช็คตั้งค่า","ตั้งค่า","เชค"]:
                    line.sendText(msg.to,"Set:status")
                    line.sendText(msg.to,"เช็คการตั้งค่าบอทสิริ")                     
            if settings ["Api"] == True:
                if msg.text in ["ตั้งแอดรอง","ตั้งรอง","ตั้งแอดรอง"]:
                    line.sendText(msg.to,"設定:予備作者変更")
                    line.sendText(msg.to,"ลงคำสั่งแล้ว ส่ง คท. แอดรองลงครับ") 
            if settings ["Api"] == True:
                if msg.text in ["แอด","@","@1"]:
                    line.sendText(msg.to,"Siri:groupcreator")
                    line.sendText(msg.to,"👆คนนี้คือแอดมินกลุ่มนี้ ")
            if settings ["Api"] == True:
                if msg.text in ["สลับ","สลับแอด"]:
                    line.sendText(msg.to,"設定:作者交換")
                    line.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะแอดมินหลักกับรอง\nลงคำสั่ง 1 ครับพอนะครับ")     
            if settings ["Api"] == True:
                if msg.text in ["ปลดแอด","ปลดแอดมิน","ล้างแอด"]:
                    line.sendText(msg.to,"siri:forcerelease")
                    line.sendText(msg.to,"คำสั่งนี้ใช้ในกรณีที่แอดห้องลบบัญชี\nให้ลงคำสั่ง 1 ครั้ง\nแล้วรอ5นาทีแล้วเช็คแอดดูครับ ")       
            if settings ["Api"] == True:
                if msg.text in ["ทวิทเต้อ","ทวิท","ผูกทวิทเต้อ"]:
                    line.sendText(msg.to,"Siri:Twitter紐付け")
                    line.sendText(msg.to,"คำสั่งเฉพาะคนขายตั๋ว \nใช้ผูททวิทเต้อเพื่อซื้อตั๋ว")    
            if settings ["Api"] == True:
                if msg.text in ["ย้ายตั๋ว","ส่งตั๋ว","ขายตั๋ว"]:
                    line.sendText(msg.to,"Siri:招待券移行:1")
                    line.sendText(msg.to,"ใช้สำหรับส่งตั๋วเชิญบอทให้คนที่ซื้อ\nลงคำสั่ง1ครั้ง แล้วลง คท. ลูกค้าที่ซื้อตั๋ว 2 ครั้งครับ\n(สั่งในบอทสิริเซ็นเตอร์)")      
            if settings ["Api"] == True:
                if msg.text in ["เชคตั๋ว","เช็คตั๋ว"]:
                    line.sendText(msg.to,"Siri:tickets")
                    line.sendText(msg.to,"ใช้สำหรับเช็คตั๋วเชิญบอทเข้ากลุ่ม\nลงคำสั่ง1ครั้งในบอทสิริเซ็นเตอร์")
            if settings ["Api"] == True:
                if msg.text in ["บอทหลัก","ขอบอทหลัก"]:
                    line.sendText(msg.to,"Siri:contact")
                    line.sendText(msg.to,"ใช้สำหรับขอบอทหลัก\nลงคำสั่ง1ครั้งในบอทสิริเซ็นเตอร์")
            if settings ["Api"] == True:
                if msg.text in ["บอทเสริม","ขอบอทเสริม"]:
                    line.sendText(msg.to,"Siri:extraaccount")
                    line.sendText(msg.to,"ใช้สำหรับขอบอทเสริม\nลงคำสั่ง1ครั้งในบอทสิริเซ็นเตอร์")
            if settings ["Api"] == True:
                if msg.text in ["กลับ","บอทกลับ","มา"]:
                    line.sendText(msg.to,"Siriv10:reinvite")
                    line.sendText(msg.to,"คำสั่งเรียกบอทกลับห้อง") 
            if settings ["Api"] == True:
                if msg.text in ["ชุดล็อค","ชุดล็อคen","ชุดล๊อคen","ชุดล๊อค"]:
                    line.sendText(msg.to,"Siriv10:DenyURLInvite")
                    line.sendText(msg.to,"Set:iconlock:on")
                    line.sendText(msg.to,"Set:blockinvite:on")
                    line.sendText(msg.to,"Set:ownerlock:on")
                    line.sendText(msg.to,"Set:changenamelock:on")
                    line.sendText(msg.to,"Set:StampLimitation:On")
                    line.sendText(msg.to,"ชุดล๊อคห้องสิริวี10 ให้คัดลอกคำสั่ง\nแล้วางลงห้องทีละคำครับ")            
            if settings ["Api"] == True:
                if msg.text in ["ดำ","สั่งดำ","เพิ่มดำ"]:
                    line.sendText(msg.to,"Set:addblacklist")
                    line.sendText(msg.to,"เพิ่มบัญชีดำ(วิธีสั่ง>ลงคำสั่ง+ส่งข้อมูล)")    
            if settings ["Api"] == True:
                if msg.text in ["ขาว","แก้ดำ","เพิ่มขาว"]:
                    line.sendText(msg.to,"Set:addwhitelist")
                    line.sendText(msg.to,"เพิ่มบัญชีขาว(วิธีสั่ง>ลงคำสั่ง+ส่งข้อมูล)")          
            if settings ["Api"] == True:
                if msg.text in ["ลบค้างเขิญ","ลบเชิญ","ยกิเชิญ"]:
                    line.sendText(msg.to,"Siriv10:cancelinvite")
                    line.sendText(msg.to,"ลบค้างเชิญ (สั่ง2ครั้ง)")    
            if settings ["Api"] == True:
                if msg.text in ["เปลี่ยนแอด","เปลี่ยนหัว","ตั้งแอด"]:
                    line.sendText(msg.to,"Set:changeowner")
                    line.sendText(msg.to,"เปลี่ยนหัวห้อง(วิธีสั่ง>ลงคำสั่ง+ส่งข้อมูล)")   
            if settings ["Api"] == True:
                if msg.text in ["ปิดลิ้ง","ปิดลิ้งค์"]:
                    line.sendText(msg.to,"Siriv10:DenyURLInvite")
                    line.sendText(msg.to,"คำสั่งปิดลิ้งห้อง")          
            if settings ["Api"] == True:
                if msg.text in ["ตั้งเวลา","ตั้งอ่าน","รีเซ็ท","นับ"]:
                    line.sendText(msg.to,"SetLastPoint")
                    line.sendText(msg.to,"กำลังตั่งค่าการอ่าน บอทสิริ.")   
            if settings ["Api"] == True:
                if msg.text in ["ใครอ่าน","อ่าน","คนแอบ"]:
                    line.sendText(msg.to,"Viewlastseen")
                    line.sendText(msg.to,"ดูคนที่กำลังอ่านตอนนี้")
            if settings ["Api"] == True:
                if msg.text in ["ล็อคแอด","ล๊อคแอด","ล๊อคแอดมิน"]:
                    line.sendText(msg.to,"設定:作成者ロック:オン")
                    line.sendText(msg.to,"คำสั่งใช้ล๊อคแอดมิน\nกันโดนเตะออกจากห้อง")
            if settings ["Api"] == True:
                if msg.text in ["ปิดการเชิญ","ปิดเชิญ"]:
                    line.sendText(msg.to,"設定:招待拒否:オン")
                    line.sendText(msg.to,"คำสั่งปฏิเสธการเชิญสมาชิกคนนอก")
            if settings ["Api"] == True:
                if msg.text in ["รันติก","ล๊อคติก","ล็อคติก"]:
                    line.sendText(msg.to,"Set:StampLimitation:On")
                    line.sendText(msg.to,"คำสั่งห้ามคนรันติกเก้อร์เกิน15ตัว")
            if settings ["Api"] == True:
                if msg.text in ["เปิดเชิญ","อนุญาติเชิญ"]:
                    line.sendText(msg.to,"設定:招待拒否:オフ")
                    line.sendText(msg.to,"อนุญาติการเชิญสมาชิกเข้าร่วมกลุ่ม")
            if settings ["Api"] == True:
                if msg.text in ["เปิดพูด","เปิดบอท","เปิดตอบ"]:
                    line.sendText(msg.to,"Siriv10:オン")
                    line.sendText(msg.to,"เปิดใช้งานบอทอ่าน")
            if settings ["Api"] == True:
                if msg.text in ["ปิดพูด","ปิดตอบ","ปิดบอท"]:
                    line.sendText(msg.to,"Siriv10:オフ")
                    line.sendText(msg.to,"คำสั่งปิดใช้งานบอทอ่านสิริ")
            if settings ["Api"] == True:
                if msg.text in ["คัดลอก",".Copy","copy"]:
                    line.sendText(msg.to,"Set:copyownlist")   
                    line.sendText(msg.to,"คำสั่งคัดลอกบัญชีห้อง")
            if settings ["Api"] == True:
                if msg.text in ["เซ็ตบัญชี","ลบรีส","ตั้งค่าบัญชี"]:
                    line.sendText(msg.to,"Set:deletelist")
                    line.sendText(msg.to,"คำสั่งตั้งค่าใหม่สำหรับ\nการคัดลอกครั้งใหม่")
            if settings ["Api"] == True:
                if msg.text in ["ปิดลิ้ง"]:
                    line.sendText(msg.to,"Siriv10:DenyURLInvite")
                    line.sendText(msg.to,"สั่งปิดลิ้งห้อง")
            if settings ["Api"] == True:
                if msg.text in ["เปิดลิ้งค์","เปิดลิ้ง"]:
                    line.sendText(msg.to,"Siriv10:inviteurl")
                    line.sendText(msg.to,"คำสั่งเปิดลิ้งห้อง")
            if settings ["Api"] == True:
                if msg.text in ["ล็อครูป","ล๊อครูป","ลอครูป"]:
                    line.sendText(msg.to,"Set:iconlock:on")
                    line.sendText(msg.to,"คำสั่งล็อครูปห้อง")
            if settings ["Api"] == True:
                if msg.text in ["ลอคชื่อ","ล็อคชื่อ","ล๊อคชื่อ"]:
                    line.sendText(msg.to,"Set:changenamelock:on")
                    line.sendText(msg.to,"คำสั่งล็อคชื่อห้อง")
            if settings ["Api"] == True:
                if msg.text in ["ล๊อคแอด","ลอคแอด","ล็อคแอด"]:
                    line.sendText(msg.to,"Set:ownerlock:on")
                    line.sendText(msg.to,"คำสั่งใช้ล๊อคแอดมินห้อง")
            if settings ["Api"] == True:
                if msg.text in ["ล๊อคเชิญ","ลอคเชิญ","ล็อคเชิญ"]:
                    line.sendText(msg.to,"Set:blockinvite:on")
                    line.sendText(msg.to,"คำสั่งล็อคการเชิญสมาชิก")
            if settings ["Api"] == True:
                if msg.text in ["ชุดล๊อคjp","ชุดล็อค2","ชุดล็อคjp","ชุดล๊อค2"]:
                    line.sendText(msg.to,"Siriv10:招待URL拒否")
                    line.sendText(msg.to,"設定:スタンプ規制:オン")
                    line.sendText(msg.to,"設定:招待拒否:オン")
                    line.sendText(msg.to,"設定:アイコンロック:オン")
                    line.sendText(msg.to,"設定:グループ名ロック:オン")
                    line.sendText(msg.to,"設定:作成者ロック:オン")
                    line.sendText(msg.to,"ชุดคำสั่งล๊อคห้องภาษาญี่ปุ่น")
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                        try:
                            ret_ = "[ ข้อมูลของโพสนี้ ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = line.getContact(msg._from)
                                auth = "\n  ผู้เขียนโพส : {}".format(str(contact.displayName))
                            else:
                                auth = "\n  ผู้เขียนโพส : {}".format(str(msg.contentMetadata["serviceName"]))
                            purl = "\n  ลิ้งโพส : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                            ret_ += auth
                            ret_ += purl
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n  Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "text" in msg.contentMetadata:
                                text = "\n ข้อความโดยย่อ : {}".format(str(msg.contentMetadata["text"]))
                                ret_ += text
                            ret_ += "\n[ สิ้นสุดการเช็คโพส ]"
                            line.sendMessage(to, str(ret_), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
                        except:
                            line.sendMessage(to, "เกิดข้อผิดะลาดในการเช็คโพสนี้", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
        if op.type == 17:
           #print ("[ 17 ]  ข้อความ สมาชิกเข้าร่วมกลุ่ม")
           if settings["Wc"] == True:
             if op.param2 in lineMID:
                 return
             #icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
             #name = "ข้อความต้อนรับ"                   
             #link = "http://line.me/ti/p/~tome2527"
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             sendMessageWithMention(op.param1, op.param2)
             #line.sendMentionFooter(op.param1, str(settings["welcome1"]) +" ", op.param2, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(op.param2).pictureStatus, line.getContact(op.param2).displayName)
             
             #line.sendMessage(op.param1, str(settings["welcome"] +"\nสวัสดีจ้าคนมาใหม่\n╔┓┏╦━━╦┓╔┓╔━━╗╔╗\n║┗┛║┗━╣┃║┃║╯╰║║║\n║┏┓║┏━╣┗╣┗╣╰╯║╠╣\n╚┛┗╩━━╩━╩━╩━━╝╚╝\n 􀬁􀅳sparkle􏿿• 􂘁􀄗w􏿿􂘁􀄅e􏿿􂘁􀄌l􏿿􂘁􀄃c􏿿􂘁􀄏o􏿿􂘁􀄍m􏿿􂘁􀄅e􏿿 •􀬁􀅳sparkle􏿿\n🙏 {} 🙏\n❂➣ᵀᴼ ᴳᴿᴼᵁᴾ👉{}👈\n 􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿\n\n??เข้ามาแล้วก็ทำตัวให้น่ารักๆน๊ะ\n🔇อย่าลืมปิดแจ้งตื่นกันด้วยนะจ๊ะ\n🎙มีข้อสงสัยติดต่อถามได้ที่แอดมินนนะจ๊ะ".format(str(dan.displayName),str(tgb.name))), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
             line.sendMessage(op.param1, str(settings["welcome"] +" ".format(str(dan.displayName),str(tgb.name))), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})
             #sendMention(op.param1, str, "          「ข้อความต้อนรับ」          \n", "\n"+ str(settings["welcome"])+"\n\nBy.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
             #line.sendMessage(op.param1,"สวัสดี?? {} 🙏 ยินดีต้อนรับสู่กลุ่ม {}\nนะ (｀・ω・´)".format(str(dan.displayName),str(tgb.name)) + str(settings["welcome"]))
            # line.sendContact(op.param1, op.param2)
             #line.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
             line.sendContact(op.param1, op.param2)
             print ("[ 17 ]  ข้อความ สมาชิกเข้าร่วมกลุ่ม")
        if op.type == 19:
           #print ("[ 19 ]  ข้อความ เมื่อสมาชิกโดนเตะ")
           if settings["Nk"] == True:
             if op.param2 in lineMID:
                 return             
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             sendMessageWithMention(op.param1, op.param2)
             line.sendMessage(op.param1, str(settings["kick"] +"\n▄︻̷̿ {} ┻̿═━一 ได้ทำการลบสมาชิกในกลุ่ม Σ(っﾟДﾟ；)っ ".format(str(dan.displayName))))
             line.sendContact(op.param1, op.param2)
             #line.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
             print ("[ 19 ]  ข้อความ เมื่อสมาชิกโดนเตะ")
        if op.type == 15:
           #print ("ข้อความสมาชิกออกห้อง")
           if settings["Lv"] == True:
             if op.param2 in lineMID:
                 return
             #icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
             #name = "ข้อความคนออก"                   
             #link = "http://line.me/ti/p/~tome2527"
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             sendMessageWithMention(op.param1, op.param2)
             #line.sendMessage(op.param1, str(settings["bye"] +"\n🌠สมาชิกชื่อว่า🌠\n👉  {}  👈\nได้ออกจากกลุ่ม\n👉 {} 👈\n✨🇬 🇴 🇴 🇩 🇧 🇾 🇪✨\nไปแล้ว  (｀・ω・´)👀ก็ขอให้โชคดีน๊ะจ๊ะ\n      􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿".format(str(dan.displayName),str(tgb.name))), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})#,link ,icon,name)))
             line.sendMessage(op.param1, str(settings["bye"] +" ".format(str(dan.displayName),str(tgb.name))), contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+line.getContact(lineMID).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://line.me/ti/p/Rvv5zHBLDO'})#,link ,icon,name)))
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath)) 
             print ("[ 15 ]  ข้อความสมาชิกออกห้อง")
             
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            #pref=['💜💜สวัสดีครับ💜💜','💚💚สวัสดีครับ💚💚','💟💟สวัสดีครับ💟💟','💖💖สวัสดีครับ💖💖']
                            line.sendMentionFooter(op.param1, str(settings["คนแอบ"]), op.param2, "https://line.me/ti/p/FMRCTkb0nl", "http://dl.profile.line-cdn.net/"+line.getContact(op.param2).pictureStatus, line.getContact(op.param2).displayName)
                            #sendMessageWithMention(op.param1, op.param2)
                            #line.sendMessage(op.param1, str(random.choice(pref))) # + '\n♪ ♬ ヾ(´︶`♡)ﾉ ♬ ♪')
                            line.sendContact(op.param1, op.param2)
                            msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                            if msgSticker != None:
                                sid = msgSticker["STKID"]
                                spkg = msgSticker["STKPKGID"]
                                sver = msgSticker["STKVER"]
                                sendSticker(op.param1, sver, spkg, sid)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            #print ("─┅❈͜͡✯『ℳ₳N』฿✪₮ᴸᴵᶰᵉ ✯͜͡❈┅─")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass

            try:
                if op.param1 in wait2['readPoint']:
                    Name = line.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        #wait2['readMember'][op.param1] += "\n➠" + Name
                        wait2['ROM'][op.param1][op.param2] = "➠" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass

    except Exception as error:
        logError(error)
#==============================================================================#
def autoLike():
    while True:
        if settings['autoLike']["status"] == True:
            a = line.getFeed()                                           
            for i in a["result"]["feeds"]:
                c = i['post']['postInfo']['postId']
                d = i['post']['userInfo']['mid']
                if i['post']['postInfo']['liked'] == False:
                    try:
                        line.likePost(d,c,random.choice([1001,1003]))

                        line.createComment(d,c,settings['comment'])
                    except:
                        pass
                else:
                    time.sleep(0.01)
            else:
                time.sleep(0.01)
threads = threading.Thread(target=autoLike)
threads.daemon = True
threads.start()

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True        

while True:
    try:
        ops = oepoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
