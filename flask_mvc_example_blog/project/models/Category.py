from .. import mongodb
from .Page import *

class Category:
    def __init__(self, user_id, name):
        self.user_id = user_id # 소유자
        self.name = name # string

    # -------------------------------------------------
    def create(self):
        if self.user_id == '': return
        if self.name == '': return

        # 해당 유저가 유효한지 체크
        user = mongodb.user
        user = [data for data in user.find({'user_id': self.user_id})]
        if user == []: return 
        
        # 해당 카테고리가 중복인지 체크
        category = mongodb.category
        category = [data for data in category.find(
            {'name': self.name,
             'user_id': self.user_id})]
        if category == []:
            print("생성하였습니다.")
            mongodb.category.insert_one({
                "user_id": self.user_id,  # user
                "name": self.name})  # category name
        else:
            print("중복된 카테고리 입니다")

    # -------------------------------------------------
    @staticmethod
    def read(user_id, name=None):
        category = mongodb.category
        if name != None:
            category = [data for data in category.find({'user_id': user_id,'name': name})]
            if category != []:
                category = Category(user_id, name)
                return category
        else:
            return [data for data in category.find({'user_id': user_id})]
        
        print("카테고리를 찾을 수 없습니다")

            
    # -------------------------------------------------
    def delete(self):
        # 하위항목 Page 삭제
        pages = Page.read(self.user_id, self.name)
        for page in pages:
            page = Page.get2Json(page)
            page.delete()

        data = {
            "user_id": self.user_id,
            "name": self.name
        }
        category = mongodb.category
        category = [data for data in category.find({'name': self.name})]
        if category != []:
            print(self.name,"카테고리를 삭제하였습니다.")
            mongodb.category.delete_one(data)
        else:
            print("카테고리를 찾을 수 없습니다")
            
        

    def toJson(self):
        data = {
            "user_id": self.user_id,
            "name": self.name}
        return data
