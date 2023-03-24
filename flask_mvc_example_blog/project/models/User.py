from .. import mongodb

class User:
    def __init__(self, user_id, user_pw):
        self.uid = None
        self.user_id = user_id
        self.user_pw = user_pw
    
    #-------------------------------------------------
    def create(self):
        data = {  "user_id":self.user_id , 
                  "user_pw":self.user_pw }
        
        if data['user_id'] == '': return
        if data['user_pw'] == '': return
        
        users = mongodb.user
        users = [data for data in users.find({'user_id':self.user_id})]
        if users == []:
            print("생성하였습니다.")
            mongodb.user.insert_one(data)
        else:
            print("중복된 ID 입니다")

    # -------------------------------------------------
    @staticmethod
    def read(user_id, user_pw):
        users = mongodb.user
        users = [data for data in users.find({'user_id':user_id})]
        if users == []: return None
        else:
            for user in users:
                if user['user_pw'] == user_pw:
                    print("login success", user_id, " : ", user_pw)
                    return User(user_id, user_pw)
        print("login fail")
        return None

    # -------------------------------------------------
    def delete(self):
        data = {"user_id": self.user_id,
                "user_pw": self.user_pw}
        users = mongodb.user
        users = [data for data in users.find({'user_id': self.user_id})]
        if users == []:
            print("삭제할 계정조회를 실패하였습니다")
        else:
            print("삭제하였습니다.")
            mongodb.delete_one(data)

    def toJson(self):
        data = {"user_id": self.user_id,
                "user_pw": self.user_pw}
        return data