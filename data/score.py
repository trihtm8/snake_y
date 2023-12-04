import pygame
import sys
from data import input

def get_score_array():
	f=open("data/score.txt", "r")
	score_string=f.read()
	f.close()
	a=score_string.split("\n")
	return a

def splitRecord(recordStr):
	recordArr=recordStr.split(":")
	recordDic={"index":recordArr[0], "name":recordArr[1], "score":recordArr[2]}
	return recordDic

def mergeRecord(recordDic):
	return recordDic["index"]+":"+recordDic["name"]+":"+recordDic["score"]

def mergeRecords(recordDics):
	returnText=""
	for recordDic in recordDics:
		returnText=returnText+mergeRecord(recordDic)+"\n"
	returnText=returnText[0:-1]
	return returnText

def sortRecordDics(beforeSortRecordDics):
	afterSortRecordDics=[]
	for i in range(1,31):
		for j in beforeSortRecordDics:
			if j["index"] == str(i):
				afterSortRecordDics.append(j)
				beforeSortRecordDics.remove(j)
	return afterSortRecordDics

def checkHighscore(newscore):
	recordStrs=get_score_array()
	for recordStr in recordStrs:
		recordDic=splitRecord(recordStr)
		if int(recordDic["score"])<=newscore:
			return recordDic["index"]
	return False

def fluidIndexAfter(beforeFluidRecordDics, fromIndex):
	afterFluidRecordDics=[]
	for i in range(1, int(fromIndex)):
		for recordDic in beforeFluidRecordDics:
			if recordDic["index"]==str(i):
				afterFluidRecordDics.append(recordDic)
				beforeFluidRecordDics.remove(recordDic)
	for i in range(int(fromIndex), 31):
		for recordDic in beforeFluidRecordDics:
			if recordDic["index"]==str(i):
				newRecord={"index":str(i+1), "name":recordDic["name"], "score":recordDic["score"]}
				afterFluidRecordDics.append(newRecord)
				beforeFluidRecordDics.remove(recordDic)
	return afterFluidRecordDics

def addHighScore(score, mainSurface):
	isHighScore = checkHighscore(score)
	if isHighScore != False:
		index = isHighScore
		recordStrs=get_score_array()
		recordDics=[]
		for recordStr in recordStrs:
			recordDics.append(splitRecord(recordStr))
		recordDics = fluidIndexAfter(recordDics, index)
		name=input.inputIn(mainSurface)
		recordDics.append({"index":index, "name":name, "score":str(score)})
		recordDics=sortRecordDics(recordDics)
		returnText=mergeRecords(recordDics)
		f=open("data/score.txt", "w")
		f.write(returnText)
		f.close()
		return True
	else:
		return False

def show_score(mainSurface):
	show=True
	while show:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					show=False

		font=pygame.font.Font("Genshin.ttf", 30)
		mainSurface.fill((255,255,255))
		i=0
		texts=[]
		for record in get_score_array():
			texts.append(font.render(record, True, (200,0,0)))
			i+=1
		for x_pos in ((10,[0,10]), (310,[10,20]), (600,[20,30])):
			y_pos=10
			for text in texts[x_pos[1][0]:x_pos[1][1]]:
				mainSurface.blit(text, (x_pos[0],y_pos))
				y_pos+=50
		text=font.render("Press Enter to return...", True, (200,0,0))
		mainSurface.blit(text, (280, 550))
		pygame.display.update()