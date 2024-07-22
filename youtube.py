import pytube  # pip install -U pytube

stream = pytube.YouTube("https://www.youtube.com/watch?v=xro9U8hTbik").streams.first()
if stream:
    result = stream.download()
    print(result)
else:
    print("Something went wrong with getting the stream to download.")
