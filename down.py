import pafy
flag=0
type=raw_input("Hit 1 for video,2 for playlist")
type=int(type)
qual=raw_input("Hit 1 for best clarity, 2 for worst, 3 for other")
qual=int(qual)
if qual==3:
	flag=1
c=0
if type==1:
	url = "https://www.youtube.com/watch?v=NTNp1IbNLzA"
	video = pafy.new(url)
	best = video.streams
	for b in best:
		print str(c)+str(b)
		c+=1;
	if flag==1:
		index=raw_input("Enter index")
		index=int(index)
	elif qual==2:
		index=c-1
	elif qual==1:
		index=0
		
	filename = video.streams[index]
	print filename
	x=filename.download(filepath=filename.title + "." + filename.extension)

else:
	url="http://www.youtube.com/playlist?list=PLs-C3tTf69dlw30_oE0GbT5j_SzZgcugk"
	video=pafy.get_playlist(url)
	for i in xrange(1,100):
		c=0
		best=video['items'][i]['pafy'].streams
		for b in best:
			print str(c)+str(b)
			c+=1
		if flag==1:
			index=raw_input("Enter index")
			index=int(index)
		elif qual==2:
			index=c-1
		elif qual==1:
			index=0
		filename=video['items'][i]['pafy'].streams[index]
		x=filename.download(filepath="D:/python")
		
