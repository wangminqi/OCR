import streamlink
streams = streamlink.streams("https://www.douyu.com/70231")
stream = streams["source"]
fd = stream.open()
data = fd.read(1024)
fd.close()

print(streams)

# session = streamlink.Streamlink()
# streams = session.streams("https://www.douyu.com/70231")
# session.set_option("rtmp-rtmpdump", "/path/to/rtmpdump")
#
