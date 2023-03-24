from .. import mongodb


class Page:
    def __init__(self, user_id, category, name, contents):
        self.user_id = user_id # 소유자
        self.category = category
        self.name = name # string
        self.contents = contents
    
    @staticmethod
    def get2Json (json):
        return Page (
            json['user_id'],
            json['category'],
            json['name'],
            json['contents']
        )

    # -------------------------------------------------
    def create(self):
        data = {
            "user_id": self.user_id, # user
            "category": self.category,
            "contents": self.contents,
            "name": self.name} # category name
        
        # 제목이 공백이 아닌지 체크
        if data['name'] == '': return
        
        # 해당 유저가 유효한지 체크 (상위)
        user = mongodb.user
        user = [data for data in user.find({'user_id': self.user_id})]
        if user == []: return 
        
        # 해당 카테고리가 유효한지 체크 (상위)
        category = mongodb.category
        category = [data for data in category.find(
            {'name': self.category,
             'user_id': self.user_id})]
        if category == []: return 
        
        # 해당 페이지가 중복인지 체크
        page = mongodb.page
        page = [data for data in page.find(
            {'name': self.name,
             'category': self.category,
             'user_id': self.user_id})]
        if page == []:
            print("생성하였습니다.")
            mongodb.page.insert_one(data)
        else:
            print(data)
            print("생성실패하였습니다.")


    # -------------------------------------------------
    @staticmethod
    def read(user_id, category, name=None):
        page = mongodb.page
        if name != None:
            page = Page.find(user_id, category, name)
            if page != []:
                return Page(
                    page[0]['user_id'],
                    page[0]['category'],
                    page[0]['name'],
                    page[0]['contents'])
        else:
            return [data for data in page.find( {'user_id': user_id, 'category':category})]
        
        print("페이지를 찾을 수 없습니다")

            
    # -------------------------------------------------
    def delete(self):
        page = Page.find(self.user_id, self.category, self.name)
        if page != []:
            print(self.name,"페이지를 삭제하였습니다.")
            mongodb.page.delete_one({
                'name': self.name,
                'user_id': self.user_id,
                'category': self.category,
            })
        else:
            print("페이지를 찾을 수 없습니다")

    # -------------------------------------------------
    def toJson(self):
        query = {
            'name': self.name,
            'user_id': self.user_id,
            'category': self.category,
            'contents': self.contents
        }
        return query

    # -------------------------------------------------
    @staticmethod
    def find (user_id, category, name):
        page = mongodb.page
        query = {
            'name': name,
            'user_id': user_id,
            'category': category,
        }
        page = [data for data in page.find(query)]
        return page