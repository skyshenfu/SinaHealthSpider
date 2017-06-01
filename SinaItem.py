class SinaItem:
    title=''
    img=''
    detailurl=''
    def __init__(self,title,detailurl,img=''):
        self.title=title
        self.detailurl=detailurl
        self.img=img
    def getTitle(self):
        return self.title
    def getImg(self):
        return self.title
    def getDetailurl(self):
        return self.detailurl
    def __str__(self):
        return  self.title + ":"+self.detailurl