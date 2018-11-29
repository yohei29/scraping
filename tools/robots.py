import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('http://gihyo.jp/robots.text')
rp.read()

rp.can_fetch('mybot', 'http;//gihyo.jp/')