from TikTokApi import TikTokApi
 
def CollectUserData(name):
    with TikTokApi() as api:
        data = api.user(username=name).info_full()
        followers = data["stats"]["followerCount"]
        print(f'Число подписчиков - {followers}')
 
user = input("Введите ваш никнейм: ")
 
CollectUserData(user)